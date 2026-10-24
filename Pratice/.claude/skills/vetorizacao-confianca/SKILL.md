---
name: vetorizacao-confianca
description: Transformar mapas de mudança em vetores com atributos de especificação e de confiabilidade, gerar o delta mensal e o consolidado anual, calibrar a confiança e validar o esquema de saída. Use ao implementar ou alterar as etapas S4 a S7 do pipeline, ao mudar atributos ou ao reclassificar mudanças provisórias.
---

# Vetorização, confiança e consolidação

Contrato dos vetores: `docs/esquema_vetores.md` e `configs/esquema_vetor.yaml` (fonte da verdade). Base de conhecimento: `..\base_conhecimento\08_Monitoramento\PersistenciaConfirmacao.md`, `..\base_conhecimento\02_Artigos\Reiche_2024_IntegratingSatelliteForest.md`, `Zhang_2023_MonitoringMonthlyTropical.md`.

## 1. Raster → polígonos (S5)

1. Entrada: máscara binária de mudança do par `(M-1, M)` (já pós-processada em S4) e mapas de probabilidade e de classe.
2. Componentes conexos (conectividade 8), remoção de manchas menores que `posproc.area_min_m2` e fechamento de vazios menores que `posproc.fechar_vazios_m2`.
3. `rasterio.features.shapes` → polígonos em EPSG:32723 → `shapely.make_valid` → manter só `Polygon` simples (explodir multipartes).
4. Recorte pela máscara da AOI e **remoção do que toca alfa 0** em qualquer das duas datas.
5. Atributos geométricos (área, perímetro, compacidade, largura média para vias) e de proveniência (imagens, run, modelo).
6. Tipo e de→para por **regra determinística**: `classe_de` e `classe_para` são as classes dominantes (por área) dentro do polígono nos mapas de classe de `M-1` e `M`; `tipo_alteracao` sai da tabela `configs/classes.yaml:tipo_alteracao`; vias por forma (compacidade baixa e largura < ~4 pixels).

```python
import hashlib, numpy as np, geopandas as gpd, rasterio
from rasterio import features
from shapely.geometry import shape
from shapely.validation import make_valid
from scipy import ndimage as ndi

def poligonos(mask, transform, area_min_m2, res):
    lab, n = ndi.label(mask, structure=np.ones((3, 3)))
    geoms = []
    for g, v in features.shapes(lab.astype("int32"), mask=lab > 0, transform=transform):
        geom = make_valid(shape(g))
        for p in getattr(geom, "geoms", [geom]):
            if p.geom_type == "Polygon" and p.area >= area_min_m2:
                geoms.append(p)
    return geoms

def id_estavel(mes, geom, nd=0):
    """Identificador determinístico: mesmo mês e mesma geometria (arredondada) geram o mesmo id."""
    chave = f"{mes}|{round(geom.centroid.x, nd)}|{round(geom.centroid.y, nd)}|{round(geom.area, nd)}"
    return hashlib.sha1(chave.encode()).hexdigest()[:12]

def atributos_geom(g):
    a, p = g.area, g.length
    return dict(area_m2=a, area_ha=a / 1e4, perimetro_m=p, compacidade=4 * np.pi * a / (p ** 2), largura_media_m=2 * a / p)
```

## 2. Rastreio e eventos (S4/S7)

- Ligue polígonos de meses consecutivos por sobreposição (IoU ≥ `posproc.janela_rastreio_iou`, 0,3) ou toque: mesmo `id_evento`. O mês mais antigo dá o `mes_primeira_deteccao`.
- `estagio`: `novo` no primeiro mês; `em_expansao` se a área cresce nos meses seguintes; `consolidado` quando para de crescer e persiste; `revertido` quando a mudança desaparece (rebrota, demolição).
- Um evento nunca perde histórico: guarde a lista de `id_mudanca` que o formaram.

## 3. Confiança (S6)

Componentes (todos em [0, 1]):

| Componente | Como calcular |
|---|---|
| `conf_modelo` | média (ou o percentil 25) da probabilidade **calibrada** do detector nos pixels do polígono |
| `conf_persistencia` | `n_obs_confirma / min(3, n_obs_disponiveis)`; nulo e `provisoria` enquanto faltarem os meses seguintes (Zhang 2023: ≥ 3 observações) |
| `conf_qualidade` | 1 menos a fração de pixels com nuvem, sombra, borda de mosaico ou baixa qualidade nas duas datas |
| `conf_concordancia` | IoU com o polígono de um segundo método independente (por exemplo, `baseline_hue`) |
| `conf_tamanho` | função crescente da área acima de `posproc.area_min_m2` (por exemplo, `min(1, area / (4 * area_min))`) |

Combinação **aprendida**, não escolhida à mão:

```python
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.isotonic import IsotonicRegression

COMP = ["conf_modelo", "conf_persistencia", "conf_qualidade", "conf_concordancia", "conf_tamanho"]

def ajustar_confianca(df_ajuste, df_calib):
    """df_*: DataFrame com COMP e 'real' (1 = evento confirmado na referência). Conjuntos separados."""
    X = df_ajuste[COMP].fillna(0).values
    lr = LogisticRegression(class_weight="balanced", max_iter=1000).fit(X, df_ajuste["real"])
    s = lr.decision_function(df_calib[COMP].fillna(0).values)
    iso = IsotonicRegression(out_of_bounds="clip", y_min=0, y_max=1).fit(s, df_calib["real"])
    return lr, iso

def classe_por_precisao(prob, real, meta_alta=0.90, meta_media=0.70):
    """Menor limiar cuja precisão acumulada (acima do limiar) atinge a meta."""
    ordem = np.argsort(-prob); p, r = prob[ordem], real[ordem]
    prec = np.cumsum(r) / np.arange(1, len(r) + 1)
    def limiar(meta):
        ok = np.where(prec >= meta)[0]
        return p[ok.max()] if len(ok) else 1.0
    return limiar(meta_alta), limiar(meta_media)
```

- Classes: `alta` (≥ limiar de precisão 0,90), `media` (≥ 0,70), `baixa`; `provisoria` enquanto a persistência não pode ser avaliada. As metas 0,90 e 0,70 são do projeto, não da literatura.
- Ajuste e calibração em **conjuntos distintos** da referência (validação), nunca no teste.
- Publique o diagrama de confiabilidade e o ECE com cada versão do modelo (skill `avaliacao-comparacao`).
- Reclassificação: quando chegam os meses seguintes, recalcule `conf_persistencia`, `confianca` e `classe_confianca` mantendo o `id_mudanca`.

## 4. Consolidado anual (S7)

1. Reúna as mudanças mensais do ano; agrupe por `id_evento`; **dissolva** as geometrias do evento (união) e some a área do último mês, não a soma das áreas mensais.
2. `tipo_alteracao`, `classe_de`, `classe_para`: voto ponderado pela confiança mensal; `classe_para` usa o mês mais recente.
3. **Comparação anual direta:** componha o fim do ano anterior (por exemplo, mediana dos 2–3 últimos meses sem nuvem) e o fim do ano atual e rode o detector; `conf_comparacao_anual` = IoU entre o evento e a mudança anual direta.
4. `confianca_anual` combina a confiança mensal máxima, a persistência ao longo do ano e `conf_comparacao_anual`, pela mesma estratégia aprendida (calibre no nível anual).
5. Escreva `consolidado_AAAA.gpkg` com as camadas `eventos`, `mudancas_mensais` e `resumo` (área por tipo e por classe de confiança).

## 5. Escrita e validação

- `gpd.GeoDataFrame(..., crs="EPSG:32723").to_file(caminho, layer="mudancas", driver="GPKG")`.
- Valide contra `configs/esquema_vetor.yaml`: campos obrigatórios, domínios, intervalos, geometria válida e simples, nada fora da AOI nem sobre alfa 0, `classe_de ≠ classe_para` (exceto `em_expansao`).
- Execute duas vezes e confira que os identificadores são idênticos (teste de determinismo).
- Grave `manifesto.json` com versões, configuração, arquivos de entrada com hash, contagens por tipo e classe de confiança.

## Armadilhas

- Somar áreas mensais no consolidado (conta a mesma área várias vezes).
- Declarar confiança sem calibração, ou calibrar no conjunto de teste.
- Perder `provisoria`: a mudança do último mês parece "confiante" só porque ainda não houve tempo de desmentir.
- Polígonos inválidos ou multipartes que quebram a gravação em GeoPackage.
- Gerar vetor sobre pixel sem dado do sensor.
