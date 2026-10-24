---
tipo: pipeline
etapa: E09
tags: [pipeline, etapa/E09]
---
# E09 — Pós-processamento e eventos

**Objetivo:** Persistência, ligação de identidades no tempo, taxonomia from–to, vetorização e eventos encadeados (supressão → obra → via).

**Entradas:** Mapas de cobertura/mudança  
**Saídas:** change_event com geometria, intervalo, classe anterior/posterior e evidências

**Anterior:** [[E08 Modelos de série temporal]] · **Próxima:** [[E10 Avaliação e incerteza]]

## Como fazer (decisões da literatura e do documento original)

- Aplicar a taxonomia from–to; guardar eventos encadeados (supressão → obra → via) sem contar a mesma área duas vezes.
- Associação temporal de objetos deve modelar divisão/fusão; o ID de uma máscara não é identidade no mundo.
- Saída mínima: id, geometria, classe anterior/posterior, intervalo, área, produto, observações válidas, confiança e revisão.

**Risco principal:** Contar repetidamente a mesma área como nova conversão independente.

## Conceitos relacionados

[[Edificações]], [[Vias-estradas|Vias/estradas]], [[Pós-classificação]], [[Mineração]]

## Artigos de apoio (25)

| Prioridade | Artigo | Título | O que aproveitar |
|---|---|---|---|
| alta | [[P10 Etten 2021\|P10 Etten 2021]] | The Multi-Temporal Urban Development SpaceNet Dataset | referência prioritária para novas construções e acompanhamento de objetos em resolução próxima à sua. |
| baixa | [[P36 Shu 2025\|P36 Shu 2025]] | RB-SCD: A New Benchmark for Semantic Change Detection of Roa | taxonomia e detecção de construção, reforma e remoção de infraestrutura viária. |
| baixa | [[P37 Bastani 2018\|P37 Bastani 2018]] | RoadTracer: Automatic Extraction of Road Networks From Aeria | fundamentar avaliação de conectividade, além de sobreposição de pixels. |
| baixa | [[P38 Buslaev 2018\|P38 Buslaev 2018]] | Fully Convolutional Network for Automatic Road Extraction Fr | baseline de máscara de vias, depois combinável entre datas. |
| baixa | [[P39 Bernhard 2023\|P39 Bernhard 2023]] | MapFormer: Boosting Change Detection by Using Pre-change Inf | usar cartografia existente como informação adicional para localizar atualizações. |
| baixa | [[P40 Lee 2026\|P40 Lee 2026]] | Road Change Detection Using Maps and Aerial Imagery for Digi | caso específico de mudança em ruas, complementar a P39. |
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
| baixa | [[P122 Cortinhas 2024\|P122 Cortinhas 2024]] | Uncontrolled Illegal Mining and Garimpo in the Brazilian Ama | Mineração ilegal (garimpo) na Amazônia brasileira; contexto de uma transição relevante ao projeto. |
| baixa | [[P165 Wang 2025\|P165 Wang 2025]] | MO-SAM: Testing the reliability and limits of mine feature d | MO-SAM: confiabilidade do Geo-SAM na delineação de feições de mineração. |

## Experimentos ligados


