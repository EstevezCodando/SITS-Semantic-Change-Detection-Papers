# Banco da máscara de cobertura

Script: `db/mascara_cobertura.sql`. É um SQL plain para PostgreSQL 18 com PostGIS e cria tudo no esquema `mascara`. Guarda só os **rótulos** (a máscara). Os rasters ficam em `D:\PT2-build\Imagens de Satelite`, e o banco aponta para eles por `imagem.id`.

## Criar

```bash
createdb -U postgres mudanca_mascara
psql -U postgres -d mudanca_mascara -v ON_ERROR_STOP=1 -f db/mascara_cobertura.sql
```

Rode o script num banco vazio. Ele roda numa única transação: se algo falhar, nada fica gravado.

## Tabelas

| Tabela | Conteúdo |
|---|---|
| `classe` | O `id` é o valor do pixel no raster: 1 a 7 são as classes de cobertura de `configs/classes.yaml`, 251 a 255 são exclusões (nuvem, sombra, sem dado, borda de mosaico, ignorar) e 0 é "não rotulado". Cada classe tem um nome amigável e uma cor para o QGIS. |
| `fonte` | As famílias de imagem de `configs/pipeline.yaml`. |
| `imagem` | Uma linha por raster, com período (`data_ini`, `data_fim`), `data_referencia` e `mes_ref` (AAAA-MM). Vem pré-carregada com as 177 imagens existentes: 81 `global_monthly`, 74 `medres_normalized`, 1 `psscene` e 21 `cbers_wpm`. A extensão e o tamanho ficam nulos até o inventário preenchê-los. |
| `area_rotulada` | Recortes em que a classificação está completa (`completa = true`). Dentro deles todo pixel tem classe; fora, o pixel vale 0 e não entra no treino. |
| `cobertura` | Os polígonos da máscara. Cada um tem `id_imagem`, `data_referencia` (a data do que foi classificado), `id_classe`, a geometria MultiPolygon em EPSG:32723, `area_m2` calculada, a origem (manual, modelo ou importado), a confiança, uma `imagem_apoio` opcional (por exemplo, a CBERS de 2 m usada para decidir) e a revisão. |

## Regras aplicadas pelo banco

- Se `data_referencia` vier vazia, o banco usa a data da imagem.
- Uma geometria inválida, por exemplo com autointerseção, é corrigida com `ST_MakeValid`. Um polígono vazio é recusado.
- Dois polígonos de `cobertura` da **mesma imagem** não podem compartilhar área; encostar na borda é permitido. Em imagens diferentes não há restrição. Para desenhar por cima de polígonos existentes, chame antes `SELECT mascara.recortar_vizinhos(geom, id_imagem)`: a função subtrai a geometria nova dos vizinhos.

## Visões

| Visão | Uso |
|---|---|
| `v_cobertura` | Camada para editar e ver no QGIS, com classe, cor, fonte, arquivo e mês. |
| `v_mascara_entrada` | Entrada da rasterização: `valor` é o pixel e `ordem` é a ordem de queima (a área rotulada vale 0 e vai primeiro, depois as classes). Polígonos rejeitados na revisão ficam de fora. |
| `v_lacunas` | O que falta classificar dentro das áreas rotuladas completas. Deve estar vazia antes de gerar a máscara. |
| `v_resumo` | Área e número de polígonos por imagem e classe, para conferir o balanço de classes. |

## Gerar a máscara de uma imagem

Use a grade da própria imagem (mesma transformação e mesmo tamanho) e rasterize `v_mascara_entrada` filtrando por `id_imagem`, em ordem crescente de `ordem`. Pixel fora de área rotulada: 0 (ignorar). Exemplo com `geopandas` e `rasterio`:

```python
gdf = gpd.read_postgis(
    "select valor, geom from mascara.v_mascara_entrada where id_imagem = %(i)s order by ordem",
    con, params={"i": id_imagem}, geom_col="geom")
mask = rasterize(zip(gdf.geometry, gdf.valor), out_shape=(src.height, src.width),
                 transform=src.transform, fill=0, dtype="uint8")
```

No treino, use `ignore_index` para 0 e para 251 a 255.

## Testado

Em 2026-10-24 o script foi carregado num cluster PostgreSQL 18 + PostGIS temporário. Foram conferidos: as contagens de imagens por fonte; a data padrão vinda da imagem; a recusa de sobreposição na mesma imagem e a aceitação em imagens diferentes; a correção de um polígono com autointerseção; `recortar_vizinhos`; e as quatro visões. A rasterização com `read_postgis` não foi executada.
