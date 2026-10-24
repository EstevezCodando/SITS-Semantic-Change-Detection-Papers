---
tipo: leitura_profunda
paper: "P07"
leitura: "profunda (texto integral, MDPI HTML aberto)"
fonte_lida: "MDPI Remote Sensing 14(11):2628 lido no navegador (dados/textos_extra/P07_mdpi_html.txt); chunks P07_c001+"
etapas_pipeline: ["[[E06 Modelos-base de cobertura|E06]]"]
tags: [leitura_profunda, prioridade/alta]
---

# Leitura profunda — P07 Vizzari 2022

**PlanetScope, Sentinel-2, and Sentinel-1 Data Integration for Object-Based Land Cover Classification in Google Earth Engine**

Nota do artigo: [[P07 Vizzari 2022|P07 Vizzari 2022]] · Chunks: [[P07 chunks]] · Leitura: *profunda (texto integral, MDPI HTML aberto)*

> Leitura feita nesta coleta; valores e afirmações vêm do texto lido, com link para o chunk de origem. O que não foi verificado está marcado.

## Pergunta e escopo
Quanto se ganha em **classificação de cobertura** com PlanetScope NICFI ao (a) trocar a abordagem por pixel (PB) por **orientada a objetos** (OB: SNIC + GLCM) e (b) integrar PlanetScope com Sentinel-2 e Sentinel-1, tudo com Random Forest no Google Earth Engine. É um estudo de **cobertura estática** (um composto de 14 meses), não de mudança; serve como baseline de ML (EXP1).

## Dados
- Área de 69.272 km² no centro do Brasil (≈13,305°S, 46,770°O; TO/GO/BA), mosaico agrícola e natural ([[P07 chunks#^P07_c007|c007]]).
- **PlanetScope NICFI**: no período só havia **um composto semestral** de 4,77 m com 4 bandas; calculados NDVI e GNDVI. Sentinel-2 L2A: 547 imagens (1 ago 2018–30 set 2019) com NDVI, NDMI, GNDVI e BSI (média temporal); Sentinel-1: 212 imagens IW, VV e VH (média). S2 e S1 foram reamostrados para 4,77 m por interpolação bicúbica ([[P07 chunks#^P07_c011|c011]], [[P07 chunks#^P07_c012|c012]]).

## Rótulos
- 2.400 pontos distribuídos de forma homogênea: ≈850 do **Brazil Data Cube** (INPE) e o restante interpretado em QGIS com o plugin **AcATaMa** sobre Bing/Google/Planet; 7 classes ([[P07 chunks#^P07_c008|c008]]).

## Método
- **Textura:** GLCM sobre uma imagem de 8 bits (`0,3·NIR + 0,59·RED + 0,11·GREEN`; em S1 `(VH−VV)/(VH+VV)`), reescalada pelos percentis 2–98; janela de **2 px** para S2/S1 e **5 px** para PlanetScope; cinco índices de textura selecionados ([[P07 chunks#^P07_c014|c014]]).
- **Segmentação:** SNIC sobre as quatro bandas visíveis+NIR, `compactness 1`, `connectivity 8`, `neighborhood 128`, espaçamento de sementes 8 (S2) e 10 (PL); o valor de cada objeto é a média das camadas ([[P07 chunks#^P07_c016|c016]]).
- **Classificador:** Random Forest no GEE; 70 % / 30 % dos pontos para treino/validação, **os mesmos subconjuntos para os dez modelos**; `scale` de 20 m (S2/S1) e 10 m (PL) no `sampleRegion`; seleção iterativa de variáveis por importância ([[P07 chunks#^P07_c017|c017]]).

## Métricas
- OA, exatidão do produtor (PA = recall), do usuário (UA = precisão) e F-score; **teste de McNemar** (sem correção de continuidade; p < 0,05) para comparar modelos. **Kappa não calculado**, porque os dados de teste não são independentes entre as abordagens, e por críticas gerais ao kappa ([[P07 chunks#^P07_c018|c018]]).

## Resultados (OA)
| Abordagem | OA % |
|---|---|
| PB só S2 | 74,4 |
| OB só S2 | 81,6 |
| PB S2 + S1 | 81,2 |
| OB S2 + S1 | 83,5 |
| OB S2 + S1 + textura S1 | 86,2 |
| **PB só PlanetScope** | **66,7** |
| **OB só PlanetScope** | **82,2** |
| PB S2 + S1 + PL | 81,6 |
| OB (S2 + S1 espectral, PL textura/objeto) | 88,3 |
| **OB (PL espectral + S2 + S1)** | **90,6** |

- OB só com PL iguala OB só com S2 (82,2 vs 81,6; p = 0,892) com o dobro da resolução. A passagem de PB para OB com PL é significativa (82,2 vs 66,7; p = 0,000). Classes mais difíceis: arbustos, pastagens, solo exposto e edificado ([[P07 chunks#^P07_c020|c020]], [[P07 chunks#^P07_c023|c023]]).

## Limites declarados
- A integração é feita só na composição de bandas, sem técnicas de fusão; a janela de 14 meses mistura mudanças reais no composto ([[P07 chunks#^P07_c027|c027]], [[P07 chunks#^P07_c028|c028]]).
- Geometria dos objetos (tamanho/forma) e precisão geométrica não foram avaliadas; vetorização no GEE travou; seleção de variáveis e redução de dimensionalidade limitadas pelo GEE ([[P07 chunks#^P07_c032|c032]], [[P07 chunks#^P07_c033|c033]]).
- Código só por e-mail ao autor.

## O que reaproveitar
- **Pipeline OB (SNIC + GLCM + RF)** como baseline barato do EXP1, inclusive em Python (scikit-image `slic`/`skimage.feature.graycomatrix` + scikit-learn), definindo janelas em **metros** (não px) para 3 m e 5 m.
- **Fluxo de rotulagem no QGIS** com AcATaMa e pontos de um cubo de dados oficial (Brazil Data Cube) para ampliar a amostra.
- **McNemar** para comparar classificadores no mesmo conjunto de teste; ao relatar, usar PA/UA/F por classe.
- Regra de que **objetos + textura do PlanetScope** trazem o ganho espacial, enquanto S2/S1 acrescentam espectro/estrutura.

## Cuidados para o nosso projeto
- Um composto único não valida transições mensais; este baseline mede cobertura, não evento.
- A OA de 67 % em PB com PlanetScope puro mostra que o espectro de 4 bandas do Planet é pobre sem contexto espacial.
