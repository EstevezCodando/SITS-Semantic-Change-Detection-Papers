# Dados disponíveis e o que eles permitem

Origem: `D:\PT2-build\Imagens de Satelite` (somente leitura). Gerado pelos scripts de `pipeline/` dessa pasta (`p01` a `p05`, `cbers_baixar.py`, `gerar_catalogo.py`). Descrição conferida em 2026-10-24 por inspeção dos arquivos.

## Área de estudo

- `Jardim_Interlagos.geojson`: bairro Jardim Interlagos, Maricá/RJ (2º Distrito, Ponta Negra), uma península entre duas lagoas. A geometria foi **reconstituída** por diferença entre distritos e bairros e exige confirmação cadastral (propriedades do próprio arquivo).
- Bloco de análise: bbox da AOI + 100 m, em **EPSG:32723**. A máscara da AOI (1 dentro, 0 fora) fica em arquivo separado; os rasters **não** são recortados pelo polígono.
- Paisagem: loteamento peri-urbano em adensamento, vias de terra e asfalto, vegetação arbórea e rasteira, brejo, solo exposto e lâmina d'água. Entre 2020-01 e 2026-09 há mudanças visíveis: novas edificações, novas vias, supressão de vegetação e uma intervenção grande no canto nordeste.

## Fontes

| Fonte | Série | Grade | Bandas | Observações |
|---|---|---|---|---|
| `planet_basemaps/global_monthly` | 81 meses, 2020-01 a 2026-09 (mensal contínua) | 4,5 m, 725 × 659 | RGB + alfa, `uint8` | Basemap visual mensal; nativo 4,777 m reamostrado. **Série principal.** |
| `planet_basemaps/medres_normalized` | 74 mosaicos, 2020-06 a 2026-09 (o primeiro agrega 2020-06 a 2020-08; depois mensal) | 4,5 m, 725 × 659 | RGB + alfa, `uint8` | Produto analítico "normalizado" renderizado em 8 bits; candidato a ter radiometria mais estável. **Verificar** (skill `inventario-dados`). |
| `planet_basemaps/sentinel2_8b` | 2026-08 e 2026-09 | 4,5 m | RGB + alfa, `uint8` | Só dois meses: não serve para série. |
| `planet_psscene/mosaico_2026-10-23` | 1 data (2026-10-09), 1 cena | 3 m, 1087 × 988 | RGB + alfa, `uint8` | Mosaico de PSScene com raster de datas (`*_datas.tif`) e `meta.json`. Útil como **imagem nova** para testar a inferência e como apoio de rotulagem. |
| `CBERS/wpm_fused_2m` | 21 datas, 2023-04 a 2026-10 | 2 m, 1631 × 1482 | RGB fundida (PCA), 3 bandas `uint8` | Resolução maior, **não** é Planet. Serve para **confirmar eventos** na rotulagem; sem filtro de nuvem automático (ver `catalogo_cbers.csv` e o PNG). |
| `data/catalogo/mosaicos.{csv,json}` | — | — | — | Metadados dos basemaps: nome, id, família, início, fim, resolução, cobertura. |
| `catalogo.html` | — | — | — | Catálogo autocontido com miniaturas, cobertura por mês e resolução ao longo do tempo. |

Cada GeoTIFF vem com um `.png` de visualização (data na faixa inferior). O `.png` não carrega georreferência confiável nem os valores originais: **não o use como entrada**.

## O que a natureza dos dados implica

1. **Sem NIR e sem reflectância.** O produto é visual (RGB de 8 bits, balanço de cor da Planet). NDVI e índices espectrais de vegetação não existem. A literatura de NICFI de 5 m usa 4 bandas; aqui há três. O índice Hue (Zhang 2023) usa só RGB e continua aplicável, mas os limiares dele foram calibrados em outra paisagem e em outro produto; **recalibre**.
2. **Sem máscara de qualidade (UDM).** Nuvem, sombra e névoa precisam ser estimadas pelo próprio pipeline (brilho, saturação, consistência temporal). A série mensal já é composta para reduzir nuvem, mas restam artefatos de mosaico.
3. **Inconsistência radiométrica entre meses.** Mosaicos visuais mensais mudam de brilho e matiz por composição, estação, ângulo e algoritmo. Além disso, os estudos com basemaps Planet documentam **mudança de processamento em 2022 (nitidez e super-resolução)**, que desloca a distribuição das imagens (Glazer 2025, p. 2–3). Medir isso é a primeira tarefa de análise; sem tratar, o modelo aprende diferença de produto como se fosse mudança de terreno.
4. **Resolução efetiva.** Grade de 4,5 m; um pixel de edificação pequena mistura telhado, solo e vegetação. A menor área detectável deve ser medida, não presumida.
5. **Alfa.** O canal alfa indica onde não há dado do sensor. Pixels com alfa 0 não podem entrar em treino, avaliação nem vetores.
6. **Uma AOI.** ~3,3 × 3,0 km. Para estimar generalização é preciso mais áreas (ver `docs/roteiro.md`, fase 8).

## Lacunas de dados a resolver

- Nenhuma referência de mudança (rótulos) existe. Precisa ser criada.
- Sem controle de "áreas estáveis" definidas, não se mede falso alarme por radiometria.
- Falta decidir qual família (`global_monthly` ou `medres_normalized`) é a entrada principal; decidir por evidência (estabilidade de áreas estáveis, ver `inventario-dados`).
- Datas: o campo `inicio`/`fim` do catálogo é o período do basemap. A data do evento, no vetor, é o **mês** do mosaico, não o dia.
