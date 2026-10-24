---
tipo: pipeline
etapa: E01
tags: [pipeline, etapa/E01]
---
# E01 — Inventário e catálogo

**Objetivo:** Identificar cada arquivo, período, produto, bandas, CRS e checksum; separar catálogo técnico de imagens e catálogo semântico de observações.

**Entradas:** Arquivos Planet brutos (3 m e 5 m), manifestos  
**Saídas:** Catálogo STAC/CSV de assets; manifestos

**Próxima:** [[E02 Qualidade e harmonização]]

## Como fazer (decisões da literatura e do documento original)

- Registrar para cada arquivo: produto, intervalo de composição, CRS, resolução, bandas, URI e checksum (`image_asset`).
- Manter o catálogo técnico (STAC) separado do catálogo semântico de observações.
- Preservar os originais; derivados apontam para a origem.

## Conceitos relacionados

[[Cubo de dados - STAC|Cubo de dados / STAC]], [[STAC (ferramenta)]]

## Artigos de apoio (7)

| Prioridade | Artigo | Título | O que aproveitar |
|---|---|---|---|
| média | [[P68 Ferreira 2020\|P68 Ferreira 2020]] | Earth Observation Data Cubes for Brazil: Requirements, Metho | principal referência brasileira para estruturar seu acervo espaço-temporal. |
| média | [[P70 Simões 2021\|P70 Simões 2021]] | Satellite Image Time Series Analysis for Big Earth Observati | referência de fluxo completo entre dados e classificação de séries, e não apenas escolha de modelo. |
| baixa | [[P69 Ferreira 2022\|P69 Ferreira 2022]] | Building Earth Observation Data Cubes on AWS | execução por tarefas, paralelismo e processamento de grandes coleções. |
| baixa | [[P71 Appel 2019\|P71 Appel 2019]] | On-Demand Processing of Data Cubes from Satellite Image Coll | evitar materializar combinações completas quando apenas recortes e operações específicas são necessários. |
| baixa | [[P72 Schramm 2021\|P72 Schramm 2021]] | The openEO API–Harmonising the Use of Earth Observation Clou | desacoplar especificação analítica e infraestrutura de execução. |
| baixa | [[P73 Trujillo 2026\|P73 Trujillo 2026]] | Incremental Data Cube Architecture for Sentinel-2 Time Serie | incorporar o próximo mês sem recomputar indiscriminadamente toda a série 2020–2026. |
| baixa | [[P74 Xi 2019\|P74 Xi 2019]] | A spatiotemporal cube model for analyzing satellite image ti | fundamenta a organização conjunta de espaço, tempo e atributos. |

## Experimentos ligados


