---
tipo: pipeline
etapa: E07
tags: [pipeline, etapa/E07]
---
# E07 — Modelos de mudança em pares

**Objetivo:** Aprender a mudança diretamente (FC-Siam, ChangeFormer, ChangeMamba) e mudança semântica (HRSCD, SECOND, ChangeMask).

**Entradas:** Pares de datas corregistrados  
**Saídas:** Máscara de mudança + classes antes/depois

**Anterior:** [[E06 Modelos-base de cobertura]] · **Próxima:** [[E08 Modelos de série temporal]]

## Como fazer (decisões da literatura e do documento original)

- Comparar FC-Siam ou ChangeFormer com a pós-classificação nos mesmos dados, rótulos e orçamento.
- Modelos semânticos conjuntos devem manter coerência entre "mudou" e as classes.
- Binário não diz *o que* mudou: exigir saída semântica.

**Risco principal:** Resultados de benchmarks (LEVIR-CD, SECOND) não transferem para 3–5 m.

## Conceitos relacionados

[[Rede siamesa]], [[Transformer]], [[Mamba-SSM|Mamba/SSM]], [[Mudança semântica]], [[Detecção de mudança (binária)]]

## Artigos de apoio (57)

| Prioridade | Artigo | Título | O que aproveitar |
|---|---|---|---|
| alta | [[P10 Etten 2021\|P10 Etten 2021]] | The Multi-Temporal Urban Development SpaceNet Dataset | referência prioritária para novas construções e acompanhamento de objetos em resolução próxima à sua. |
| alta | [[P12 Toker 2022\|P12 Toker 2022]] | DynamicEarthNet: Daily Multi-Spectral Satellite Dataset for  | benchmark central para mudanças multiclasse, e não apenas edifícios. |
| alta | [[P18 Daudt 2019\|P18 Daudt 2019]] | Multitask Learning for Large-scale Semantic Change Detection | base para dois mapas semânticos e uma máscara de mudança coerentes entre si. |
| alta | [[P19 Yang 2021\|P19 Yang 2021]] | Asymmetric Siamese Networks for Semantic Change Detection in | organizar avaliação de transições semânticas. |
| média | [[P11 Etten 2021\|P11 Etten 2021]] | The SpaceNet Multi-Temporal Urban Development Challenge | consultar desenho da avaliação, associação entre meses e soluções reproduzíveis. |
| média | [[P15 Garnot 2021\|P15 Garnot 2021]] | Panoptic Segmentation of Satellite Image Time Series With Co | referência de encoder espaço-temporal para aproveitar várias observações. |
| média | [[P20 Zheng 2022\|P20 Zheng 2022]] | ChangeMask: Deep multi-task encoder-transformer-decoder arch | candidato a modelo conjunto para evitar divergência entre “mudou” e classes previstas. |
| média | [[P21 Ding 2022\|P21 Ding 2022]] | Bi-Temporal Semantic Reasoning for the Semantic Change Detec | reduzir inconsistências na interpretação das transições. |
| média | [[P23 Daudt 2018\|P23 Daudt 2018]] | Fully Convolutional Siamese Networks for Change Detection | baseline profundo simples, importante para comparar com redes mais complexas. |
| média | [[P26 Bandara 2022\|P26 Bandara 2022]] | A Transformer-Based Siamese Network for Change Detection | comparar com U-Net/FC-Siam sob os mesmos dados, rótulos e orçamento. |
| média | [[P28 Chen 2024\|P28 Chen 2024]] | ChangeMamba: Remote Sensing Change Detection With Spatiotemp | candidato moderno para comparar eficiência e desempenho semântico. |
| média | [[P29 Zheng 2024\|P29 Zheng 2024]] | Segment Any Change | gerar candidatos e apoiar exploração/anotação com pouca supervisão. |
| média | [[P33 Bou 2026\|P33 Bou 2026]] | Remote Sensing Change Detection via Weak Temporal Supervisio | aproveitar seu acervo longo com rótulos limitados. |
| baixa | [[P16 Zhao 2025\|P16 Zhao 2025]] | HiSTENet: History-Integrated Spatial–Temporal Information Ex | candidato adicional para comparar histórico multitemporal com pares isolados. |
| baixa | [[P17 Metzger 2023\|P17 Metzger 2023]] | Urban Change Forecasting from Satellite Images | extensão futura para previsão de expansão, depois de validar mudanças observadas. |
| baixa | [[P22 Tang 2024\|P22 Tang 2024]] | The ClearSCD model: Comprehensively leveraging semantics and | avaliar transições com probabilidades, não apenas subtrair rótulos rígidos. |
| baixa | [[P24 Chen 2020\|P24 Chen 2020]] | A Spatial-Temporal Attention-Based Method and a New Dataset  | atenção espacial/temporal e avaliação de construção. |
| baixa | [[P25 Chen 2021\|P25 Chen 2021]] | Remote Sensing Image Change Detection With Transformers | baseline de transformer para mudança binária. |
| baixa | [[P27 Zheng 2021\|P27 Zheng 2021]] | Change Is Everywhere: Single-Temporal Supervised Object Chan | aproveitar mapas e polígonos disponíveis quando faltam pares anotados. |
| baixa | [[P30 Yongshuo 2025\|P30 Yongshuo 2025]] | Semantic-CD: Remote Sensing Image Semantic Change Detection  | investigar categorias descritas por texto e assistência à classificação. |
| baixa | [[P31 Huang 2025\|P31 Huang 2025]] | TextSCD: Leveraging Text-based Semantic Guidance for Remote  | avaliar se descrições de classes ajudam na separação das transições. |
| baixa | [[P32 Szwarcman 2024\|P32 Szwarcman 2024]] | Prithvi-EO-2.0: A Versatile Multitemporal Foundation Model f | backbone candidato, principalmente em experimentos que integrem outras fontes. |
| baixa | [[P34 Shen 2026\|P34 Shen 2026]] | Foundation Model-Driven Semantic Change Detection in Remote  | candidato recente para fine-tuning semântico. |
| baixa | [[P35 Su 2026\|P35 Su 2026]] | Seg2Change: Adapting Open-Vocabulary Semantic Segmentation M | linha exploratória para novas categorias sem refazer toda a taxonomia de treinamento. |
| baixa | [[P36 Shu 2025\|P36 Shu 2025]] | RB-SCD: A New Benchmark for Semantic Change Detection of Roa | taxonomia e detecção de construção, reforma e remoção de infraestrutura viária. |
| baixa | [[P49 Lei 2026\|P49 Lei 2026]] | Remote sensing image change detection using deep learning te |  |
| baixa | [[P112 Andrade 2020\|P112 Andrade 2020]] | EVALUATION OF SEMANTIC SEGMENTATION METHODS FOR DEFORESTATIO | Avaliação de métodos de segmentação semântica para desmatamento na Amazônia. |
| baixa | [[P125 Jiang 2022\|P125 Jiang 2022]] | A Survey on Deep Learning-Based Change Detection from High-R | Levantamento de detecção de mudanças por DL em imagens de alta resolução. |
| baixa | [[P126 Shafique 2022\|P126 Shafique 2022]] | Deep Learning-Based Change Detection in Remote Sensing Image | Revisão de detecção de mudanças por DL em sensoriamento remoto. |
| baixa | [[P127 Miller 2024\|P127 Miller 2024]] | Deep Learning for Satellite Image Time-Series Analysis: A re | Revisão de deep learning para séries temporais de imagens de satélite. |
| baixa | [[P128 Peng 2025\|P128 Peng 2025]] | Toward Label‐Efficient Deep Learning Change Detection for Re | Detecção de mudanças com poucos rótulos: revisão abrangente. |
| baixa | [[P129 Peng 2019\|P129 Peng 2019]] | End-to-End Change Detection for High Resolution Satellite Im | UNet++ aprimorada para detecção de mudanças de ponta a ponta. |
| baixa | [[P130 Shen 2021\|P130 Shen 2021]] | S2Looking: A Satellite Side-Looking Dataset for Building Cha | S2Looking: dataset de edificações com visão lateral para detecção de mudanças. |
| baixa | [[P131 Yang 2025\|P131 Yang 2025]] | ConvFormer-CD: Hybrid CNN–Transformer With Temporal Attentio | ConvFormer-CD: CNN–transformer com atenção temporal para mudanças. |
| baixa | [[P132 Zhou 2025\|P132 Zhou 2025]] | SChanger: Change Detection From a Semantic Change and Spatia | SChanger: detecção de mudanças sob perspectiva de consistência semântica e espacial. |
| baixa | [[P133 Ding 2024\|P133 Ding 2024]] | Adapting Segment Anything Model for Change Detection in VHR  | Adaptação do SAM para detecção de mudanças em imagens VHR. |
| baixa | [[P134 Mei 2024\|P134 Mei 2024]] | SCD-SAM: Adapting Segment Anything Model for Semantic Change | SCD-SAM: SAM adaptado à detecção de mudança semântica. |
| baixa | [[P135 Wei 2025\|P135 Wei 2025]] | ASS-CD: Adapting Segment Anything Model and Swin-Transformer | ASS-CD: SAM e Swin-Transformer para detecção de mudanças. |
| baixa | [[P136 Zhang 2025\|P136 Zhang 2025]] | BCTDNet: Building Change-Type Detection Networks with the Se | BCTDNet: tipos de mudança em edificações com SAM. |
| baixa | [[P137 Li 2024\|P137 Li 2024]] | A New Learning Paradigm for Foundation Model-Based Remote-Se | Novo paradigma de aprendizado para detecção de mudanças com modelo fundacional. |

*(+17 artigos de prioridade menor; veja a tag `etapa/E07`.)*

## Experimentos ligados


