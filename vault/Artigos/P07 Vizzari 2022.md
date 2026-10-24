---
tipo: artigo
id: P07
titulo: "PlanetScope, Sentinel-2, and Sentinel-1 Data Integration for Object-Based Land Cover Classification in Google Earth Engine"
autores: "Marco Vizzari"
ano: 2022
secao: A
categoria: "Planet: aplicações diretas"
tipo_publicacao: "Artigo"
papel: ["aplicação Planet"]
prioridade: alta
doi: "10.3390/rs14112628"
pdf: ""
texto_integral: sim
fonte_analise: "leitura profunda do texto integral (HTML aberto) + metadados"
n_chunks: 35
sensores: ["[[PlanetScope]]", "[[Sentinel-2]]", "[[Sentinel-1-SAR|Sentinel-1/SAR]]"]
tarefas: []
metodos: ["[[Random Forest]]"]
datasets: []
metricas: []
ferramentas: ["[[Google Earth Engine]]"]
etapas_pipeline: ["[[E06 Modelos-base de cobertura|E06]]"]
leitura_profunda: "[[LP P07 Vizzari 2022]]"
status_leitura: lido (profundo)
tags: [artigo, secao/A, prioridade/alta, etapa/E06]
---

# P07 — PlanetScope, Sentinel-2, and Sentinel-1 Data Integration for Object-Based Land Cover Classification in Google Earth Engine

**Marco Vizzari** · 2022 · Artigo · Remote Sensing · [publicação](https://doi.org/10.3390/rs14112628) · PDF indisponível em coleta/

Seção: **Planet: aplicações diretas** · Prioridade: **alta** · Análise: *leitura profunda do texto integral (HTML aberto) + metadados*

> [!success] Leitura profunda concluída: [[LP P07 Vizzari 2022]]

## O que reaproveitar

- **Pipeline OB (SNIC + GLCM + RF)** como baseline barato do EXP1, inclusive em Python (scikit-image `slic`/`skimage.feature.graycomatrix` + scikit-learn), definindo janelas em **metros** (não px) para 3 m e 5 m.
- **Fluxo de rotulagem no QGIS** com AcATaMa e pontos de um cubo de dados oficial (Brazil Data Cube) para ampliar a amostra.
- **McNemar** para comparar classificadores no mesmo conjunto de teste; ao relatar, usar PA/UA/F por classe.
- Regra de que **objetos + textura do PlanetScope** trazem o ganho espacial, enquanto S2/S1 acrescentam espectro/estrutura.

### Extraído automaticamente

- **Uso proposto:** baseline de ML para testar se o custo adicional do deep learning produz benefício real.

## Método e dados (da revisão original)

- **Método/dados:** Random Forest, segmentação em objetos, textura e integração de sensores; classificação de cobertura no Brasil.

## Limites e cuidados

- classificar cobertura em uma composição não equivale a validar transições mensais; o estudo é complementar à detecção de mudanças.

## Contextos de uso no projeto

- Etapas do pipeline: [[E06 Modelos-base de cobertura|E06]]
- Sensores/produtos: [[PlanetScope]], [[Sentinel-2]], [[Sentinel-1-SAR|Sentinel-1/SAR]]
- Métodos: [[Random Forest]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[PlanetScope]] | 1 |
| sensor | [[Sentinel-2]] | 1 |
| sensor | [[Sentinel-1-SAR\|Sentinel-1/SAR]] | 1 |
| metodo | [[Random Forest]] | 1 |
| ferramenta | [[Google Earth Engine]] | 1 |

## Chunks

- Arquivo de chunks: [[P07 chunks]] (35 chunks; introdução 6, dados 6, métodos 11, resultados 5, discussão 5, conclusão 2)
- Dados / área de estudo: [[P07 chunks#^P07_c007|c007]], [[P07 chunks#^P07_c008|c008]]
- Método: [[P07 chunks#^P07_c009|c009]], [[P07 chunks#^P07_c014|c014]], [[P07 chunks#^P07_c015|c015]]
- Hiperparâmetros / treino: [[P07 chunks#^P07_c015|c015]], [[P07 chunks#^P07_c016|c016]]
- Resultados numéricos: [[P07 chunks#^P07_c020|c020]]
- Limitações / discussão: [[P07 chunks#^P07_c025|c025]], [[P07 chunks#^P07_c026|c026]]

## Relações

- Vizinhos por entidades em comum: [[P86 Latte 2020|P86]], [[P169 Congedo 2021|P169]], [[P87 Sadeh 2020|P87]], [[P77 Shendryk 2019|P77]]

## Anotações

- 
