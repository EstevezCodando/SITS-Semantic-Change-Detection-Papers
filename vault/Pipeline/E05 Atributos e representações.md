---
tipo: pipeline
etapa: E05
tags: [pipeline, etapa/E05]
---
# E05 — Atributos e representações

**Objetivo:** Extrair bandas/índices, textura, geometria, contexto e embeddings; testar por ablação.

**Entradas:** Cubo + máscaras/objetos  
**Saídas:** Tabela de atributos versionada; embeddings com procedência

**Anterior:** [[E04 Rotulagem e pré-anotação]] · **Próxima:** [[E06 Modelos-base de cobertura]]

## Como fazer (decisões da literatura e do documento original)

- Bandas/índices compatíveis com o produto; estatísticas por segmento; texturas em janelas definidas em metros.
- Testar grupos de atributos por ablação; ajustar seletores e hiperparâmetros só no treino.
- Registrar modelo, checkpoint, resolução e normalização dos embeddings.

## Conceitos relacionados

[[NDVI-índices|NDVI/índices]], [[OBIA - objetos|OBIA / objetos]], [[Modelo fundacional]], [[DINO-DINOv3|DINO/DINOv3]], [[Autoencoder mascarado (MAE)]], [[CLIP - visão-linguagem|CLIP / visão-linguagem]]

## Artigos de apoio (27)

| Prioridade | Artigo | Título | O que aproveitar |
|---|---|---|---|
| média | [[P51 Rodrigues 2025\|P51 Rodrigues 2025]] | Machine Learning-Based Cerrado Land Cover Classification Usi | baseline prioritário de cobertura vegetal. É classificação, não validação de todas as transições mensais ou de |
| média | [[P52 Georganos 2018\|P52 Georganos 2018]] | Very High Resolution Object-Based Land Use-Land Cover Urban  | fundamento para classificar segmentos por espectro, textura e forma. |
| média | [[P54 Gündüz 2026\|P54 Gündüz 2026]] | An Explainable and Optimized Machine Learning Framework for  | referência especialmente útil de **ciência de dados aplicada**: seleção, otimização e interpretação. No experi |
| média | [[P56 Osco 2023\|P56 Osco 2023]] | The Segment Anything Model (SAM) for remote sensing applicat | leitura prioritária para gerar máscaras preliminares e reduzir delineamento manual. |
| média | [[P57 Ren 2024\|P57 Ren 2024]] | Grounded SAM: Assembling Open-World Models for Diverse Visua | texto → caixas candidatas → máscaras → revisão. |
| média | [[P58 Hussain 2026\|P58 Hussain 2026]] | YOLOSAM: A YOLO-Guided SAM for Accurate Building Segmentatio | exemplo direto da catalogação prévia sugerida: detector localiza, segmentador delimita. |
| média | [[P59 Zhang 2025\|P59 Zhang 2025]] | Toward unsupervised building extraction from very high-resol | referência muito próxima da ideia de criar previamente um catálogo de objetos para treinamento. |
| média | [[P60 Wang 2024\|P60 Wang 2024]] | SAMPolyBuild: Adapting the Segment Anything Model for polygo | aproxima a saída do modelo de objetos GIS utilizáveis no catálogo. |
| média | [[P62 Carion 2025\|P62 Carion 2025]] | SAM 3: Segment Anything with Concepts | candidato recente para catalogação orientada por conceitos e seleção assistida de objetos. |
| baixa | [[P30 Yongshuo 2025\|P30 Yongshuo 2025]] | Semantic-CD: Remote Sensing Image Semantic Change Detection  | investigar categorias descritas por texto e assistência à classificação. |
| baixa | [[P32 Szwarcman 2024\|P32 Szwarcman 2024]] | Prithvi-EO-2.0: A Versatile Multitemporal Foundation Model f | backbone candidato, principalmente em experimentos que integrem outras fontes. |
| baixa | [[P34 Shen 2026\|P34 Shen 2026]] | Foundation Model-Driven Semantic Change Detection in Remote  | candidato recente para fine-tuning semântico. |
| baixa | [[P35 Su 2026\|P35 Su 2026]] | Seg2Change: Adapting Open-Vocabulary Semantic Segmentation M | linha exploratória para novas categorias sem refazer toda a taxonomia de treinamento. |
| baixa | [[P53 Tianqi 2016\|P53 Tianqi 2016]] | XGBoost: A Scalable Tree Boosting System | fundamentar implementação e processamento de uma tabela de atributos por pixel, objeto ou trajetória. |
| baixa | [[P55 Magidi 2024\|P55 Magidi 2024]] | Land use and land cover changes in Notwane watershed, Botswa | exemplo concreto de XGBoost dentro de um fluxo de mudança por pós-classificação. |
| baixa | [[P61 Wu 2025\|P61 Wu 2025]] | Remote Sensing Extraction of Damaged Buildings in the Shigat | demonstra integração detector–segmentador em sensoriamento remoto. |
| baixa | [[P63 Dabaja 2026\|P63 Dabaja 2026]] | Promptable Concept Segmentation from Above: Evaluating SAM 3 | ajuda a avaliar objetivamente quando texto ou exemplo visual são úteis para pré-catalogar. |
| baixa | [[P64 Siméoni 2025\|P64 Siméoni 2025]] | DINOv3 |  |
| baixa | [[P65 Faulkenberry 2026\|P65 Faulkenberry 2026]] | DINO Soars: DINOv3 for Open-Vocabulary Semantic Segmentation | candidato de pré-classificação de cenas e cobertura. |
| baixa | [[P66 Brown 2025\|P66 Brown 2025]] | AlphaEarth Foundations: An embedding field model for accurat | contexto e classificação auxiliar quando há poucos rótulos. |
| baixa | [[P67 Xiong 2024\|P67 Xiong 2024]] | Neural Plasticity-Inspired Multimodal Foundation Model for E | alternativa para investigar entrada multiespectral heterogênea. |
| baixa | [[P76 Kerdreux 2025\|P76 Kerdreux 2025]] | Efficient Self-Supervised Learning for Earth Observation via | inspira seleção de amostras informativas em vez de treinar com todos os patches repetidos de meses estáveis. |
| baixa | [[P79 Reed 2022\|P79 Reed 2022]] | Scale-MAE: A Scale-Aware Masked Autoencoder for Multiscale G | estudar representações quando o acervo mistura resoluções e tamanhos físicos de objetos. |
| baixa | [[P127 Miller 2024\|P127 Miller 2024]] | Deep Learning for Satellite Image Time-Series Analysis: A re | Revisão de deep learning para séries temporais de imagens de satélite. |
| baixa | [[P137 Li 2024\|P137 Li 2024]] | A New Learning Paradigm for Foundation Model-Based Remote-Se | Novo paradigma de aprendizado para detecção de mudanças com modelo fundacional. |
| baixa | [[P151 Lu 2025\|P151 Lu 2025]] | Vision Foundation Models in Remote Sensing: A survey | Levantamento sobre modelos fundacionais de visão em sensoriamento remoto. |
| baixa | [[P172 Mai 2025\|P172 Mai 2025]] | Towards the next generation of Geospatial Artificial Intelli | Rumo à próxima geração de inteligência artificial geoespacial. |

## Leituras profundas e sínteses

- [[Síntese — GeoAI e QGIS- o que cada ferramenta faz no nosso fluxo]]
