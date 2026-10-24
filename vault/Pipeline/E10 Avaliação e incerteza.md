---
tipo: pipeline
etapa: E10
tags: [pipeline, etapa/E10]
---
# E10 — Avaliação e incerteza

**Objetivo:** Métricas por tarefa, matriz from–to, estimativa de área com IC, validação espacial/temporal e custo de revisão.

**Entradas:** Eventos + amostra probabilística independente  
**Saídas:** Métricas, áreas estimadas, falsos alertas por km²/mês

**Anterior:** [[E09 Pós-processamento e eventos]] · **Próxima:** [[E11 Operação e atualização]]

## Como fazer (decisões da literatura e do documento original)

- Métricas por tarefa (mudança, from–to, edificações por objeto e tamanho, vias por conectividade, data, área).
- Estimar área com amostragem probabilística e intervalo de confiança; área mapeada ≠ área estimada.
- Não comparar F1 publicado entre benchmarks distintos.

## Conceitos relacionados

[[Estimativa de área - IC|Estimativa de área / IC]], [[Matriz de confusão]], [[Kappa]], [[F1]], [[IoU - mIoU|IoU / mIoU]], [[Precisão-Recall|Precisão/Recall]], [[SeK]], [[SCS (DynamicEarthNet)]]

## Artigos de apoio (11)

| Prioridade | Artigo | Título | O que aproveitar |
|---|---|---|---|
| alta | [[P10 Etten 2021\|P10 Etten 2021]] | The Multi-Temporal Urban Development SpaceNet Dataset | referência prioritária para novas construções e acompanhamento de objetos em resolução próxima à sua. |
| alta | [[P12 Toker 2022\|P12 Toker 2022]] | DynamicEarthNet: Daily Multi-Spectral Satellite Dataset for  | benchmark central para mudanças multiclasse, e não apenas edifícios. |
| alta | [[P13 Vincent 2024\|P13 Vincent 2024]] | Satellite Image Time Series Semantic Change Detection: Novel | fundamenta avaliar anos e áreas inéditos, em vez de apenas sortear patches da mesma paisagem. |
| alta | [[P19 Yang 2021\|P19 Yang 2021]] | Asymmetric Siamese Networks for Semantic Change Detection in | organizar avaliação de transições semânticas. |
| alta | [[P46 Olofsson 2014\|P46 Olofsson 2014]] | Good practices for estimating area and assessing accuracy of | essencial para sustentar quantos hectares mudaram e a incerteza associada. |
| média | [[P47 Stehman 2019\|P47 Stehman 2019]] | Key issues in rigorous accuracy assessment of land cover pro | auditar independência da amostra, referência e inferência das métricas. |
| média | [[P75 Roberts 2017\|P75 Roberts 2017]] | Cross-validation strategies for data with temporal, spatial, | separar bairros/blocos e períodos, evitando a falsa independência de pixels e patches próximos. |
| baixa | [[P34 Shen 2026\|P34 Shen 2026]] | Foundation Model-Driven Semantic Change Detection in Remote  | candidato recente para fine-tuning semântico. |
| baixa | [[P76 Kerdreux 2025\|P76 Kerdreux 2025]] | Efficient Self-Supervised Learning for Earth Observation via | inspira seleção de amostras informativas em vez de treinar com todos os patches repetidos de meses estáveis. |
| baixa | [[P79 Reed 2022\|P79 Reed 2022]] | Scale-MAE: A Scale-Aware Masked Autoencoder for Multiscale G | estudar representações quando o acervo mistura resoluções e tamanhos físicos de objetos. |
| baixa | [[P80 Feng 2025\|P80 Feng 2025]] | BuildingSAM: A Dual-Branch Feature-Augmented Segment Anythin | candidato especializado para comparar com SAM genérico e YOLO-seg. |

## Leituras profundas e sínteses

- [[LP P10 Etten 2021]] → The Multi-Temporal Urban Development SpaceNet Dataset (nota: [[P10 Etten 2021|P10 Etten 2021]])
- [[LP P12 Toker 2022]] → DynamicEarthNet: Daily Multi-Spectral Satellite Dataset for Semantic C (nota: [[P12 Toker 2022|P12 Toker 2022]])
- [[LP P13 Vincent 2024]] → Satellite Image Time Series Semantic Change Detection: Novel Architect (nota: [[P13 Vincent 2024|P13 Vincent 2024]])
- [[LP P19 Yang 2021]] → Asymmetric Siamese Networks for Semantic Change Detection in Aerial Im (nota: [[P19 Yang 2021|P19 Yang 2021]])
- [[LP P46 Olofsson 2014]] → Good practices for estimating area and assessing accuracy of land chan (nota: [[P46 Olofsson 2014|P46 Olofsson 2014]])
- [[Síntese — decisões e hipóteses derivadas da leitura profunda]]
- [[Síntese — métricas por tarefa e armadilhas]]
- [[Síntese — partições, vazamento e domain shift]]
