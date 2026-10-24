---
tipo: pipeline
etapa: E06
tags: [pipeline, etapa/E06]
---
# E06 — Modelos-base de cobertura

**Objetivo:** Baselines: Random Forest/XGBoost/LightGBM sobre atributos e U-Net mensal; regra de persistência temporal.

**Entradas:** Atributos, rótulos, partições  
**Saídas:** Mapas mensais de cobertura com probabilidade

**Anterior:** [[E05 Atributos e representações]] · **Próxima:** [[E07 Modelos de mudança em pares]]

## Como fazer (decisões da literatura e do documento original)

- Começar por RF/XGBoost/LightGBM e U-Net mensal + regra de persistência.
- Reportar métricas de cobertura por mês separadas das de mudança.
- Usar como baseline contra o qual os modelos de mudança devem ganhar.

**Risco principal:** Acurácia global alta escondendo baixa detecção de eventos raros.

## Conceitos relacionados

[[Random Forest]], [[XGBoost]], [[LightGBM]], [[SVM]], [[U-Net]]

## Artigos de apoio (56)

| Prioridade | Artigo | Título | O que aproveitar |
|---|---|---|---|
| alta | [[P01 Wagner 2023\|P01 Wagner 2023]] | Mapping Tropical Forest Cover and Deforestation with Planet  | principal ponto de partida para a frente de supressão vegetal no Brasil. |
| alta | [[P02 Dalagnol 2023\|P02 Dalagnol 2023]] | Mapping tropical forest degradation with deep learning and P | permite formular uma classe de degradação, além da supressão completa. |
| alta | [[P05 Zaraza-Aguilera 2022\|P05 Zaraza-Aguilera 2022]] | Change Detection over mining areas using Deep Neural Network | evidência para comparar duas estratégias no seu piloto, incluindo solo exposto e alteração de grandes superfíc |
| alta | [[P07 Vizzari 2022\|P07 Vizzari 2022]] | PlanetScope, Sentinel-2, and Sentinel-1 Data Integration for | baseline de ML para testar se o custo adicional do deep learning produz benefício real. |
| média | [[P03 Carter 2024\|P03 Carter 2024]] | Detection of forest disturbance across California using deep | especialmente relevante se seus mosaicos forem RGB, sem NIR. |
| média | [[P04 Wang 2024\|P04 Wang 2024]] | AI-based Validation of Deforestation Using High-Resolution S | arquitetura em duas etapas: gerar candidatos e verificar mudanças em alta resolução. |
| média | [[P06 Şimşek 2025\|P06 Şimşek 2025]] | Determination of land use and land cover change using multi- | classificação multitemporal e localização de áreas que exigem atualização cartográfica. |
| média | [[P33 Bou 2026\|P33 Bou 2026]] | Remote Sensing Change Detection via Weak Temporal Supervisio | aproveitar seu acervo longo com rótulos limitados. |
| média | [[P51 Rodrigues 2025\|P51 Rodrigues 2025]] | Machine Learning-Based Cerrado Land Cover Classification Usi | baseline prioritário de cobertura vegetal. É classificação, não validação de todas as transições mensais ou de |
| média | [[P52 Georganos 2018\|P52 Georganos 2018]] | Very High Resolution Object-Based Land Use-Land Cover Urban  | fundamento para classificar segmentos por espectro, textura e forma. |
| média | [[P54 Gündüz 2026\|P54 Gündüz 2026]] | An Explainable and Optimized Machine Learning Framework for  | referência especialmente útil de **ciência de dados aplicada**: seleção, otimização e interpretação. No experi |
| baixa | [[P08 Debus 2025\|P08 Debus 2025]] | Evaluating satellite data and deep learning for identifying  | investigar a ocupação posterior à perda vegetal, indo além do mapa binário. |
| baixa | [[P09 Gonzalez-Velez 2026\|P09 Gonzalez-Velez 2026]] | Tropical dry forest land use/land cover change detection usi | escassez de rótulos e confusão entre formações vegetais, áreas abertas e regeneração. |
| baixa | [[P32 Szwarcman 2024\|P32 Szwarcman 2024]] | Prithvi-EO-2.0: A Versatile Multitemporal Foundation Model f | backbone candidato, principalmente em experimentos que integrem outras fontes. |
| baixa | [[P48 Peng 2025\|P48 Peng 2025]] | Deep learning change detection techniques for optical remote |  |
| baixa | [[P50 Jabbarizadegan 2026\|P50 Jabbarizadegan 2026]] | Change Detection in Remote Sensing Imagery: A Systematic Rev |  |
| baixa | [[P53 Tianqi 2016\|P53 Tianqi 2016]] | XGBoost: A Scalable Tree Boosting System | fundamentar implementação e processamento de uma tabela de atributos por pixel, objeto ou trajetória. |
| baixa | [[P55 Magidi 2024\|P55 Magidi 2024]] | Land use and land cover changes in Notwane watershed, Botswa | exemplo concreto de XGBoost dentro de um fluxo de mudança por pós-classificação. |
| baixa | [[P91 Zhang 2023\|P91 Zhang 2023]] | Monitoring monthly tropical humid forest disturbances with P | Perturbações florestais mensais com mosaicos Planet NICFI em Camarões; próximo da cadência mensal do projeto. |
| baixa | [[P92 Yang 2025\|P92 Yang 2025]] | Mapping forest-agroforest frontiers in the Peruvian Amazon w | Fronteiras floresta–agrofloresta na Amazônia peruana com deep learning e PlanetScope. |
| baixa | [[P93 Wagner 2025\|P93 Wagner 2025]] | Wall‐to‐wall Amazon forest height mapping with Planet NICFI  | Altura de floresta amazônica com Planet NICFI, LiDAR e U-Net; exemplo de uso estrutural dos mosaicos. |
| baixa | [[P94 Pachêco 2025\|P94 Pachêco 2025]] | Land Cover Transformations in Mining-Influenced Areas Using  | Transformações de cobertura em áreas de mineração com PlanetScope, índices espectrais e aprendizado de máquina |
| baixa | [[P95 Huang 2022\|P95 Huang 2022]] | An evaluation of PlanetScope images for 3D reconstruction an | Avaliação de PlanetScope para reconstrução 3D e detecção de mudanças; limites geométricos das imagens. |
| baixa | [[P96 Wang 2022\|P96 Wang 2022]] | An MLC and U-Net Integrated Method for Land Use/Land Cover C | MLC e U-Net para mudança de uso/cobertura com série temporal de NDVI. |
| baixa | [[P97 Deigele 2020\|P97 Deigele 2020]] | A Hierarchical Deep-Learning Approach for Rapid Windthrow De | Detecção hierárquica de áreas de vendaval em PlanetScope e imagens de alta resolução. |
| baixa | [[P98 Martins 2022\|P98 Martins 2022]] | Deep learning high resolution burned area mapping by transfe | Mapeamento de área queimada em PlanetScope por transferência de aprendizado de Landsat-8. |
| baixa | [[P99 Ossa 2023\|P99 Ossa 2023]] | Land Cover Classification in the Antioquia Region of the Tro | Classificação de cobertura em Antioquia (Andes) com dados NICFI e rótulos; referência regional de dados. |
| baixa | [[P100 Crato 2025\|P100 Crato 2025]] | Detection of rural roads from planet images using convolutio | Detecção de estradas rurais em imagens Planet com redes convolucionais (autores brasileiros). |
| baixa | [[P101 Winiwarter 2024\|P101 Winiwarter 2024]] | Extraction of Forest Road Information from CubeSat Imagery U | Extração de estradas florestais em imagens CubeSat com CNN; escala comparável a 3–5 m. |
| baixa | [[P102 Masolele 2024\|P102 Masolele 2024]] | Mapping the diversity of land uses following deforestation a | Usos do solo após o desmatamento na África; útil para pensar a classe posterior à perda de floresta. |
| baixa | [[P103 Glazer 2025\|P103 Glazer 2025]] | TEMPO: Global Temporal Building Density and Height Estimatio | TEMPO: densidade e altura de edificações com basemaps PlanetScope trimestrais (2018–2025). |
| baixa | [[P104 McVicar 2023\|P104 McVicar 2023]] | Smartflow: Enabling Scalable Spatiotemporal Geospatial Resea | Smartflow: aprendizado profundo para construção pesada em grandes áreas, incluindo imagens Planet. |
| baixa | [[P105 He 2022\|P105 He 2022]] | Tracking Urbanization in Developing Regions with Remote Sens | Acompanhamento da urbanização com super-resolução espaço-temporal (SpaceNet 7). |
| baixa | [[P106 Rahul 2023\|P106 Rahul 2023]] | An Aligned Multi-Temporal Multi-Resolution Satellite Image D | Dataset multitemporal e multirresolução alinhado para pesquisa em detecção de mudanças. |
| baixa | [[P107 Wang 2024\|P107 Wang 2024]] | BuildMon: Building Extraction and Change Monitoring in Time  | BuildMon: extração e monitoramento de edificações em séries temporais de sensoriamento remoto. |
| baixa | [[P108 Bem 2020\|P108 Bem 2020]] | Change Detection of Deforestation in the Brazilian Amazon Us | Detecção de desmatamento na Amazônia brasileira com Landsat e CNN; referência clássica de DL para PRODES. |
| baixa | [[P109 Torres 2021\|P109 Torres 2021]] | Deforestation Detection with Fully Convolutional Networks in | Redes totalmente convolucionais para desmatamento na Amazônia com Landsat-8 e Sentinel-2. |
| baixa | [[P110 Alshehri 2024\|P110 Alshehri 2024]] | Deep Transformer-Based Network Deforestation Detection in th | Rede baseada em transformers para desmatamento na Amazônia com Sentinel-2. |
| baixa | [[P111 Andrade 2022\|P111 Andrade 2022]] | Deforestation Detection in the Amazon Using DeepLabv3+ Seman | Variantes do DeepLabv3+ para desmatamento na Amazônia. |
| baixa | [[P112 Andrade 2020\|P112 Andrade 2020]] | EVALUATION OF SEMANTIC SEGMENTATION METHODS FOR DEFORESTATIO | Avaliação de métodos de segmentação semântica para desmatamento na Amazônia. |

*(+16 artigos de prioridade menor; veja a tag `etapa/E06`.)*

## Experimentos ligados


