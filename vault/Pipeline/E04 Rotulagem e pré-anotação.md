---
tipo: pipeline
etapa: E04
tags: [pipeline, etapa/E04]
---
# E04 — Rotulagem e pré-anotação

**Objetivo:** Criar rótulos de áreas estáveis e mudanças reais; pré-anotar com SAM/YOLO e revisar; priorizar por aprendizado ativo.

**Entradas:** Cubo + amostra espacial/temporal  
**Saídas:** Conjunto anotado com origem e revisor; catálogo semântico preliminar

**Anterior:** [[E03 Cubo espaço-temporal e partições]] · **Próxima:** [[E05 Atributos e representações]]

## Como fazer (decisões da literatura e do documento original)

- Comparar três condições na mesma amostra: manual, pré-anotação com correção e pré-anotação sem correção.
- Medir tempo total, falsos positivos removidos e omissões acrescentadas.
- Manter amostra probabilística independente, separada da escolhida por aprendizado ativo.

**Risco principal:** Máscaras convincentes porém sistematicamente erradas (viés de confirmação).

## Conceitos relacionados

[[Anotação-rotulagem|Anotação/rotulagem]], [[Aprendizado ativo]], [[Supervisão fraca]], [[Semi-auto-supervisionado|Semi/auto-supervisionado]], [[SAM]], [[YOLO]], [[Grounding DINO]]

## Artigos de apoio (32)

| Prioridade | Artigo | Título | O que aproveitar |
|---|---|---|---|
| média | [[P29 Zheng 2024\|P29 Zheng 2024]] | Segment Any Change | gerar candidatos e apoiar exploração/anotação com pouca supervisão. |
| média | [[P33 Bou 2026\|P33 Bou 2026]] | Remote Sensing Change Detection via Weak Temporal Supervisio | aproveitar seu acervo longo com rótulos limitados. |
| média | [[P56 Osco 2023\|P56 Osco 2023]] | The Segment Anything Model (SAM) for remote sensing applicat | leitura prioritária para gerar máscaras preliminares e reduzir delineamento manual. |
| média | [[P57 Ren 2024\|P57 Ren 2024]] | Grounded SAM: Assembling Open-World Models for Diverse Visua | texto → caixas candidatas → máscaras → revisão. |
| média | [[P58 Hussain 2026\|P58 Hussain 2026]] | YOLOSAM: A YOLO-Guided SAM for Accurate Building Segmentatio | exemplo direto da catalogação prévia sugerida: detector localiza, segmentador delimita. |
| média | [[P59 Zhang 2025\|P59 Zhang 2025]] | Toward unsupervised building extraction from very high-resol | referência muito próxima da ideia de criar previamente um catálogo de objetos para treinamento. |
| média | [[P60 Wang 2024\|P60 Wang 2024]] | SAMPolyBuild: Adapting the Segment Anything Model for polygo | aproxima a saída do modelo de objetos GIS utilizáveis no catálogo. |
| média | [[P62 Carion 2025\|P62 Carion 2025]] | SAM 3: Segment Anything with Concepts | candidato recente para catalogação orientada por conceitos e seleção assistida de objetos. |
| média | [[P78 Pogorzelski 2025\|P78 Pogorzelski 2025]] | Comparing Active Learning for Satellite Imagery: Contrastive | priorizar revisão humana por diversidade, incerteza e representatividade, comparando com seleção aleatória. |
| baixa | [[P09 Gonzalez-Velez 2026\|P09 Gonzalez-Velez 2026]] | Tropical dry forest land use/land cover change detection usi | escassez de rótulos e confusão entre formações vegetais, áreas abertas e regeneração. |
| baixa | [[P35 Su 2026\|P35 Su 2026]] | Seg2Change: Adapting Open-Vocabulary Semantic Segmentation M | linha exploratória para novas categorias sem refazer toda a taxonomia de treinamento. |
| baixa | [[P45 Brown 2022\|P45 Brown 2022]] | Dynamic World, Near real-time global 10 m land use land cove | fonte auxiliar de contexto, comparação e eventual pré-rotulagem. |
| baixa | [[P49 Lei 2026\|P49 Lei 2026]] | Remote sensing image change detection using deep learning te |  |
| baixa | [[P61 Wu 2025\|P61 Wu 2025]] | Remote Sensing Extraction of Damaged Buildings in the Shigat | demonstra integração detector–segmentador em sensoriamento remoto. |
| baixa | [[P63 Dabaja 2026\|P63 Dabaja 2026]] | Promptable Concept Segmentation from Above: Evaluating SAM 3 | ajuda a avaliar objetivamente quando texto ou exemplo visual são úteis para pré-catalogar. |
| baixa | [[P64 Siméoni 2025\|P64 Siméoni 2025]] | DINOv3 |  |
| baixa | [[P65 Faulkenberry 2026\|P65 Faulkenberry 2026]] | DINO Soars: DINOv3 for Open-Vocabulary Semantic Segmentation | candidato de pré-classificação de cenas e cobertura. |
| baixa | [[P66 Brown 2025\|P66 Brown 2025]] | AlphaEarth Foundations: An embedding field model for accurat | contexto e classificação auxiliar quando há poucos rótulos. |
| baixa | [[P67 Xiong 2024\|P67 Xiong 2024]] | Neural Plasticity-Inspired Multimodal Foundation Model for E | alternativa para investigar entrada multiespectral heterogênea. |
| baixa | [[P76 Kerdreux 2025\|P76 Kerdreux 2025]] | Efficient Self-Supervised Learning for Earth Observation via | inspira seleção de amostras informativas em vez de treinar com todos os patches repetidos de meses estáveis. |
| baixa | [[P79 Reed 2022\|P79 Reed 2022]] | Scale-MAE: A Scale-Aware Masked Autoencoder for Multiscale G | estudar representações quando o acervo mistura resoluções e tamanhos físicos de objetos. |
| baixa | [[P80 Feng 2025\|P80 Feng 2025]] | BuildingSAM: A Dual-Branch Feature-Augmented Segment Anythin | candidato especializado para comparar com SAM genérico e YOLO-seg. |
| baixa | [[P113 Jelas 2024\|P113 Jelas 2024]] | Deforestation detection using deep learning-based semantic s | Revisão sistemática de segmentação semântica por deep learning para desmatamento. |
| baixa | [[P126 Shafique 2022\|P126 Shafique 2022]] | Deep Learning-Based Change Detection in Remote Sensing Image | Revisão de detecção de mudanças por DL em sensoriamento remoto. |
| baixa | [[P127 Miller 2024\|P127 Miller 2024]] | Deep Learning for Satellite Image Time-Series Analysis: A re | Revisão de deep learning para séries temporais de imagens de satélite. |
| baixa | [[P130 Shen 2021\|P130 Shen 2021]] | S2Looking: A Satellite Side-Looking Dataset for Building Cha | S2Looking: dataset de edificações com visão lateral para detecção de mudanças. |
| baixa | [[P133 Ding 2024\|P133 Ding 2024]] | Adapting Segment Anything Model for Change Detection in VHR  | Adaptação do SAM para detecção de mudanças em imagens VHR. |
| baixa | [[P138 Zhang 2025\|P138 Zhang 2025]] | Recurrent Semantic Change Detection in VHR Remote Sensing Im | Mudança semântica recorrente em imagens VHR com modelos visuais fundacionais. |
| baixa | [[P148 Chen 2021\|P148 Chen 2021]] | Self-Supervised Change Detection in Multiview Remote Sensing | Detecção de mudanças autossupervisionada em imagens de múltiplas visadas. |
| baixa | [[P150 Wu 2023\|P150 Wu 2023]] | Fully Convolutional Change Detection Framework With Generati | Detecção de mudanças não supervisionada com GAN e rede totalmente convolucional. |
| baixa | [[P151 Lu 2025\|P151 Lu 2025]] | Vision Foundation Models in Remote Sensing: A survey | Levantamento sobre modelos fundacionais de visão em sensoriamento remoto. |
| baixa | [[P165 Wang 2025\|P165 Wang 2025]] | MO-SAM: Testing the reliability and limits of mine feature d | MO-SAM: confiabilidade do Geo-SAM na delineação de feições de mineração. |

## Leituras profundas e sínteses

- [[Síntese — decisões e hipóteses derivadas da leitura profunda]]
- [[Síntese — protocolos de rotulagem comparados]]
