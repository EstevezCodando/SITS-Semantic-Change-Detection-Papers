---
tipo: pipeline
etapa: E11
tags: [pipeline, etapa/E11]
---
# E11 — Operação e atualização

**Objetivo:** Atualização incremental, alertas com regime operacional (só passado), revisão humana em QGIS, rastreabilidade.

**Entradas:** Novos mosaicos mensais  
**Saídas:** Eventos revisados e versionados

**Anterior:** [[E10 Avaliação e incerteza]]

## Como fazer (decisões da literatura e do documento original)

- Distinguir avaliação retrospectiva (pode usar meses futuros) de alerta operacional (só passado).
- Definir quais produtos são invalidados quando um mosaico histórico é corrigido.
- Usar QGIS/GeoAI/Deepness/Geo-SAM para revisão humana e pré-anotação, medindo o custo por evento confirmado.

## Conceitos relacionados

[[QGIS]], [[GeoAI (opengeos)]], [[MOLUSCE]], [[SCP (QGIS)]], [[Google Earth Engine]]

## Artigos de apoio (48)

| Prioridade | Artigo | Título | O que aproveitar |
|---|---|---|---|
| alta | [[P155 Wu 2026\|P155 Wu 2026]] | GeoAI: A Python package for integrating artificial intellige | Artigo do pacote GeoAI (opengeos/geoai, PyPI geoai-py), que inclui plugin para QGIS: busca/baixa dados, prepar |
| alta | [[P156 Aszkowski 2023\|P156 Aszkowski 2023]] | Deepness: Deep neural remote sensing plugin for QGIS | Deepness: plugin QGIS que executa modelos ONNX de segmentação, detecção e regressão em camadas raster. |
| alta | [[P157 Tresson 2026\|P157 Tresson 2026]] | IAMAP: Unlocking Deep Learning in QGIS for non-coders and li | IAMAP: plugin QGIS para extração de características com modelos fundacionais autossupervisionados, agrupamento |
| alta | [[P164 Wang 2024\|P164 Wang 2024]] | Geo-Sam: Testing the Reliability and Limits of Mine Feature  | Geo-SAM (plugin QGIS com SAM): teste de confiabilidade e limites na delineação de feições de mineração. |
| baixa | [[P108 Bem 2020\|P108 Bem 2020]] | Change Detection of Deforestation in the Brazilian Amazon Us | Detecção de desmatamento na Amazônia brasileira com Landsat e CNN; referência clássica de DL para PRODES. |
| baixa | [[P109 Torres 2021\|P109 Torres 2021]] | Deforestation Detection with Fully Convolutional Networks in | Redes totalmente convolucionais para desmatamento na Amazônia com Landsat-8 e Sentinel-2. |
| baixa | [[P110 Alshehri 2024\|P110 Alshehri 2024]] | Deep Transformer-Based Network Deforestation Detection in th | Rede baseada em transformers para desmatamento na Amazônia com Sentinel-2. |
| baixa | [[P111 Andrade 2022\|P111 Andrade 2022]] | Deforestation Detection in the Amazon Using DeepLabv3+ Seman | Variantes do DeepLabv3+ para desmatamento na Amazônia. |
| baixa | [[P112 Andrade 2020\|P112 Andrade 2020]] | EVALUATION OF SEMANTIC SEGMENTATION METHODS FOR DEFORESTATIO | Avaliação de métodos de segmentação semântica para desmatamento na Amazônia. |
| baixa | [[P113 Jelas 2024\|P113 Jelas 2024]] | Deforestation detection using deep learning-based semantic s | Revisão sistemática de segmentação semântica por deep learning para desmatamento. |
| baixa | [[P114 Wang 2023\|P114 Wang 2023]] | SiamHRnet-OCR: A Novel Deforestation Detection Model with Hi | SiamHRnet-OCR: modelo siamês para desmatamento em imagens de alta resolução. |
| baixa | [[P115 McCallum 2023\|P115 McCallum 2023]] | Crowd-Driven Deep Learning Tracks Amazon Deforestation | Deep learning com participação coletiva (crowd) para rastrear desmatamento na Amazônia. |
| baixa | [[P116 Doblas 2024\|P116 Doblas 2024]] | DETER-RT: The new INPE-TropiSCO deforestation monitoring sys | DETER-RT: novo sistema de monitoramento de desmatamento do INPE. |
| baixa | [[P117 Doblas 2022\|P117 Doblas 2022]] | DETER-R: An Operational Near-Real Time Tropical Forest Distu | DETER-R: sistema operacional de alerta de perturbação florestal baseado em Sentinel-1. |
| baixa | [[P118 Reiche 2024\|P118 Reiche 2024]] | Integrating satellite-based forest disturbance alerts improv | Integração de alertas de distúrbio florestal baseados em satélite para melhorar prazo e confiança. |
| baixa | [[P119 Reiche 2021\|P119 Reiche 2021]] | Forest disturbance alerts for the Congo Basin using Sentinel | Alertas de distúrbio florestal na Bacia do Congo com Sentinel-1. |
| baixa | [[P120 Ygorra 2024\|P120 Ygorra 2024]] | A near-real-time tropical deforestation monitoring algorithm | Algoritmo quase em tempo real para desmatamento tropical baseado em CuSum. |
| baixa | [[P121 Çamalan 2022\|P121 Çamalan 2022]] | Change Detection of Amazonian Alluvial Gold Mining Using Dee | Mudança por garimpo aluvial na Amazônia com aprendizado profundo e Sentinel-2. |
| baixa | [[P122 Cortinhas 2024\|P122 Cortinhas 2024]] | Uncontrolled Illegal Mining and Garimpo in the Brazilian Ama | Mineração ilegal (garimpo) na Amazônia brasileira; contexto de uma transição relevante ao projeto. |
| baixa | [[P123 Alencar 2020\|P123 Alencar 2020]] | Mapping Three Decades of Changes in the Brazilian Savanna Na | Três décadas de mudança na vegetação nativa do Cerrado (Landsat/MapBiomas). |
| baixa | [[P124 Hansen 2013\|P124 Hansen 2013]] | High-Resolution Global Maps of 21st-Century Forest Cover Cha | Hansen et al. (2013): mapas globais de mudança da cobertura florestal; base de comparação histórica. |
| baixa | [[P158 Febrita 2025\|P158 Febrita 2025]] | Evaluating AI-Driven Automated Map Digitization in QGIS | Avaliação do Deepness para digitalização automática de mapas, comparada ao OpenStreetMap (F1). |
| baixa | [[P159 Cubillas 2024\|P159 Cubillas 2024]] | Land Classification Plugin for QGIS Using Pix2Pix | Plugin QGIS de classificação de cobertura com Pix2Pix (aplicado principalmente a Landsat). |
| baixa | [[P160 Guillou 2026\|P160 Guillou 2026]] | SemanticSeg4EO: An open-source unified framework and QGIS pl | SemanticSeg4EO: framework e plugin QGIS para segmentação semântica em observação da Terra; cita o GeoAI. |
| baixa | [[P161 Ciecholewski 2026\|P161 Ciecholewski 2026]] | YOLO-MOD: YOLO-based multi-category object detection plugin  | YOLO-MOD: plugin QGIS de detecção de objetos baseado em YOLO. |
| baixa | [[P162 Ruiz-Hurtado 2025\|P162 Ruiz-Hurtado 2025]] | TreeEyed: A QGIS plugin for tree monitoring in silvopastoral | TreeEyed: plugin QGIS para monitoramento de árvores com modelos de IA. |
| baixa | [[P163 Thomas 2026\|P163 Thomas 2026]] | Spectral Imaging Deep Learning Mapper - SpecDeepMap: An open | SpecDeepMap: aplicação de segmentação semântica para o EnMAP-Box (QGIS). |
| baixa | [[P165 Wang 2025\|P165 Wang 2025]] | MO-SAM: Testing the reliability and limits of mine feature d | MO-SAM: confiabilidade do Geo-SAM na delineação de feições de mineração. |
| baixa | [[P166 Jeon 2026\|P166 Jeon 2026]] | Systematic evaluation of SAM prompting strategies for agricu | Avaliação sistemática de estratégias de prompt do SAM com GeoSAM para extração de áreas agrícolas. |
| baixa | [[P167 Wu 2023\|P167 Wu 2023]] | samgeo: A Python package for segmenting geospatial data with | samgeo (segment-geospatial): SAM para dados geoespaciais; integra-se ao ecossistema opengeos/geoai. |
| baixa | [[P168 Wu 2020\|P168 Wu 2020]] | geemap: A Python package for interactive mapping with Google | geemap: mapeamento interativo com Google Earth Engine, do mesmo autor do GeoAI. |
| baixa | [[P169 Congedo 2021\|P169 Congedo 2021]] | Semi-Automatic Classification Plugin: A Python tool for the  | Semi-Automatic Classification Plugin (SCP): download e classificação de imagens de satélite no QGIS. |
| baixa | [[P170 Zhou 2026\|P170 Zhou 2026]] | Measuring the spatial explicitness of GeoAI and geospatial f | Revisão sistemática sobre explicitação espacial em GeoAI e modelos fundacionais geoespaciais; cita o GeoAI. |
| baixa | [[P171 Boutayeb 2024\|P171 Boutayeb 2024]] | A comprehensive GeoAI review: Progress, Challenges and Outlo | Revisão abrangente de GeoAI: progresso, desafios e perspectivas. |
| baixa | [[P172 Mai 2025\|P172 Mai 2025]] | Towards the next generation of Geospatial Artificial Intelli | Rumo à próxima geração de inteligência artificial geoespacial. |
| baixa | [[P173 Mai 2024\|P173 Mai 2024]] | On the Opportunities and Challenges of Foundation Models for | Oportunidades e desafios dos modelos fundacionais para GeoAI. |
| baixa | [[P174 Carvalho 2026\|P174 Carvalho 2026]] | Remote SAMsing: From segment anything to segment everything | Remote SAMsing: do segment anything ao segment everything em sensoriamento remoto. |
| baixa | [[P175 Šanca 2023\|P175 Šanca 2023]] | AN END-TO-END DEEP LEARNING WORKFLOW FOR BUILDING SEGMENTATI | Fluxo de aprendizado profundo para segmentação, regularização de bordas e vetorização de edificações. |
| baixa | [[P176 Kleebauer 2025\|P176 Kleebauer 2025]] | Globally Scalable, QGIS-Integrated Workflow for Solar Photov | Fluxo integrado ao QGIS para segmentação de usinas fotovoltaicas em escala global. |
| baixa | [[P177 Gluski 2024\|P177 Gluski 2024]] | Remote detection of asbestos-cement roofs: Evaluating a QGIS | Avaliação de plugin QGIS para detecção remota de telhados de amianto. |

*(+8 artigos de prioridade menor; veja a tag `etapa/E11`.)*

## Experimentos ligados


