---
tipo: pipeline
etapa: E03
tags: [pipeline, etapa/E03]
---
# E03 — Cubo espaço-temporal e partições

**Objetivo:** Montar o cubo (tempo × bandas × espaço), definir blocos geográficos e períodos de teste sem vazamento.

**Entradas:** Assets harmonizados  
**Saídas:** Cubo/coleção pronta para análise; evaluation_split versionado

**Anterior:** [[E02 Qualidade e harmonização]] · **Próxima:** [[E04 Rotulagem e pré-anotação]]

## Como fazer (decisões da literatura e do documento original)

- Separar treino/validação/teste por blocos geográficos e reservar períodos posteriores para teste temporal.
- Documentar quando o teste muda de produto/resolução ao mesmo tempo.
- Evitar patches vizinhos ou sobrepostos entre conjuntos.

**Risco principal:** Vazamento espacial/temporal que infla as métricas.

## Conceitos relacionados

—

## Artigos de apoio (11)

| Prioridade | Artigo | Título | O que aproveitar |
|---|---|---|---|
| média | [[P68 Ferreira 2020\|P68 Ferreira 2020]] | Earth Observation Data Cubes for Brazil: Requirements, Metho | principal referência brasileira para estruturar seu acervo espaço-temporal. |
| média | [[P70 Simões 2021\|P70 Simões 2021]] | Satellite Image Time Series Analysis for Big Earth Observati | referência de fluxo completo entre dados e classificação de séries, e não apenas escolha de modelo. |
| média | [[P75 Roberts 2017\|P75 Roberts 2017]] | Cross-validation strategies for data with temporal, spatial, | separar bairros/blocos e períodos, evitando a falsa independência de pixels e patches próximos. |
| baixa | [[P69 Ferreira 2022\|P69 Ferreira 2022]] | Building Earth Observation Data Cubes on AWS | execução por tarefas, paralelismo e processamento de grandes coleções. |
| baixa | [[P71 Appel 2019\|P71 Appel 2019]] | On-Demand Processing of Data Cubes from Satellite Image Coll | evitar materializar combinações completas quando apenas recortes e operações específicas são necessários. |
| baixa | [[P72 Schramm 2021\|P72 Schramm 2021]] | The openEO API–Harmonising the Use of Earth Observation Clou | desacoplar especificação analítica e infraestrutura de execução. |
| baixa | [[P73 Trujillo 2026\|P73 Trujillo 2026]] | Incremental Data Cube Architecture for Sentinel-2 Time Serie | incorporar o próximo mês sem recomputar indiscriminadamente toda a série 2020–2026. |
| baixa | [[P74 Xi 2019\|P74 Xi 2019]] | A spatiotemporal cube model for analyzing satellite image ti | fundamenta a organização conjunta de espaço, tempo e atributos. |
| baixa | [[P76 Kerdreux 2025\|P76 Kerdreux 2025]] | Efficient Self-Supervised Learning for Earth Observation via | inspira seleção de amostras informativas em vez de treinar com todos os patches repetidos de meses estáveis. |
| baixa | [[P79 Reed 2022\|P79 Reed 2022]] | Scale-MAE: A Scale-Aware Masked Autoencoder for Multiscale G | estudar representações quando o acervo mistura resoluções e tamanhos físicos de objetos. |
| baixa | [[P80 Feng 2025\|P80 Feng 2025]] | BuildingSAM: A Dual-Branch Feature-Augmented Segment Anythin | candidato especializado para comparar com SAM genérico e YOLO-seg. |

## Leituras profundas e sínteses

- [[Síntese — decisões e hipóteses derivadas da leitura profunda]]
- [[Síntese — partições, vazamento e domain shift]]
- [[Síntese — protocolos de rotulagem comparados]]
