---
tipo: resultado
titulo: "Síntese — decisões e hipóteses derivadas da leitura profunda"
tags: [resultado]
---

# Síntese — decisões e hipóteses derivadas da leitura profunda

> Síntese herdada do vault anterior (`vault/`); os links de artigos foram convertidos para esta base. Afirmações sobre artigos têm fonte nas respectivas notas; itens “hipótese” são interpretação.

# Decisões e hipóteses derivadas da leitura profunda

Cada linha é uma **hipótese de trabalho** apoiada por evidência dos artigos lidos, a ser confirmada nos nossos dados. Nada aqui é resultado do projeto.

| # | Decisão / hipótese | Evidência | Etapa | Teste |
|---|---|---|---|---|
| D1 | Medir desempenho em **três regimes** (sem shift, shift temporal, shift espacial) | [[Vincent_2024_SatelliteImageTime\|Vincent 2024]] | E03 Cubo espaço-temporal e partições | relatar os três lado a lado |
| D2 | Usar **blocos de ≥ 1,6 km com folga** nas partições | [[ZarazaAguilera_2022_ChangeDetectionOver\|ZarazaAguilera 2022]] | E03 | verificar ausência de vizinhança entre treino e teste |
| D3 | **Evitar OA e κ**; usar SeK, SCS e F1 por classe e por transição | [[Daudt_2019_MultitaskLearningLarge\|Daudt 2019]], [[Yang_2021_AsymmetricSiameseNetworks\|Yang 2021]], [[Toker_2022_DynamicEarthNetDailyMulti\|Toker 2022]] | E10 Avaliação e incerteza | tabela de métricas por bloco |
| D4 | **Estimar hectares por amostra probabilística com IC** | [[Olofsson_2014_GoodPracticesEstimating\|Olofsson 2014]], [[ZarazaAguilera_2022_ChangeDetectionOver\|ZarazaAguilera 2022]] | E10 | comparar área mapeada × estimada |
| D5 | Rotular com **cópia sequencial e revisão pela série inteira**, com UDM de nuvem/co-registro | [[Etten_2021_MultiTemporalUrban\|Etten 2021]] | E04 Rotulagem e pré-anotação | medir tempo e acordo entre anotadores |
| D6 | Pré-anotar com **segmentação não supervisionada/SAM** e medir o ganho de tempo | [[Wagner_2023_MappingTropicalForest\|Wagner 2023]] | E04 | EXP6 com 3 condições |
| D7 | Baseline 1: **OB (SNIC + GLCM) + RF/XGBoost** com janelas em metros | [[Vizzari_2022_PlanetScopeSentinelSentinel\|Vizzari 2022]] | E06 Modelos-base de cobertura | EXP1 |
| D8 | Baseline 2: **U-Net 256² × 4 bandas, BCE+Dice** com regra de persistência temporal | [[Wagner_2023_MappingTropicalForest\|Wagner 2023]] | E06 | EXP2 |
| D9 | Comparar **pós-classificação × mudança direta** nos mesmos blocos | [[ZarazaAguilera_2022_ChangeDetectionOver\|ZarazaAguilera 2022]] | E07 Modelos de mudança em pares | EXP2 × EXP3 |
| D10 | Para from–to, testar o **treino sequencial** (cobertura primeiro, mudança depois) | [[Daudt_2019_MultitaskLearningLarge\|Daudt 2019]] | E07 | EXP4 |
| D11 | Para série, **inferência com a série completa** e treino com meses sorteados | [[Vincent_2024_SatelliteImageTime\|Vincent 2024]] | E08 Modelos de série temporal | EXP5 |
| D12 | **Não depender de NDVI** como entrada no primeiro ciclo | [[ZarazaAguilera_2022_ChangeDetectionOver\|ZarazaAguilera 2022]] | E06 | ablação 4 × 5 bandas |
| D13 | Esperar **F1 de edificações ~0,45 e mudança < 0,1** em 4–5 px como patamar | [[Etten_2021_MultiTemporalUrban\|Etten 2021]], [[Vincent_2024_SatelliteImageTime\|Vincent 2024]] | E10 | relatar por faixa de tamanho |
| D14 | Tratar **degradação separada de desmatamento** | [[Wagner_2023_MappingTropicalForest\|Wagner 2023]], [[Dalagnol_2023_MappingTropicalForest\|Dalagnol 2023]] | E09 | classe própria na taxonomia |
| D15 | Dar prioridade ao **tratamento de nuvem** antes da pós-classificação | [[ZarazaAguilera_2022_ChangeDetectionOver\|ZarazaAguilera 2022]] | E02 Qualidade e harmonização | comparar com e sem máscara |

## Perguntas em aberto que a leitura não resolve
- A cadência real dos nossos arquivos é mensal? Quantos meses são válidos por área?
- Qual o menor evento detectável em 3 m vs 5 m?
- Um modelo de série supera o de pares quando a mudança é 0,03–1,3 % dos pixels? ([[Vincent_2024_SatelliteImageTime|Vincent 2024]] sugere que não de forma consistente.)
- Quanto custa a revisão humana por evento confirmado?

## Lacunas de leitura
- [[Dalagnol_2023_MappingTropicalForest|Dalagnol 2023]], [[He_2024_TimeSeriesLand|He 2024]], [[Olofsson_2014_GoodPracticesEstimating|Olofsson 2014]], [[Aszkowski_2023_DeepnessDeepNeural|Aszkowski 2023]] e [[Wang_2024_GeoSamTesting|Wang 2024]] foram lidos apenas em resumos, documentação e repositórios.

## Decisões adicionais (ferramentas GeoAI/QGIS)
| # | Decisão / hipótese | Evidência | Etapa | Teste |
|---|---|---|---|---|
| D16 | Usar **QGIS para pré-anotar, revisar e inspecionar**, e o pipeline Python para a detecção temporal | [[Wu_2026_GeoAIPythonPackage\|Wu 2026]], [[Aszkowski_2023_DeepnessDeepNeural\|Aszkowski 2023]] | E04 Rotulagem e pré-anotação | EXP6 |
| D17 | Para SAM, partir de **20–30 pontos** e selecionar a máscara **sem usar a anotação** | [[Wang_2025_SAMTestingReliability\|Wang 2025]] | E04 | variar pontos e medir mIoU e tempo |
| D18 | **Codificar cada mosaico uma vez** (Geo-SAM pré-codificado) para cliques rápidos | [[Wang_2024_GeoSamTesting\|Wang 2024]] | E04 | tempo por evento |
| D19 | **IAMAP** (similaridade/agrupamento) para escolher exemplos antes de rotular | [[Tresson_2026_IAMAPUnlockingDeep\|Tresson 2026]] | E04 / E05 Atributos e representações | amostras necessárias vs baseline EXP1 |
| D20 | **Registrar parâmetros dos plugins** (resolução, sobreposição, remoção de segmentos) como parte do `processing_run` | [[Febrita_2025_EvaluatingDrivenAutomated\|Febrita 2025]] | E11 | auditoria de reprodutibilidade |
| D21 | Testar a rota **U-Net → ONNX → Deepness** para revisão em QGIS, verificando entradas de 4 bandas | [[Aszkowski_2023_DeepnessDeepNeural\|Aszkowski 2023]] | E11 Operação e atualização | teste de conversão |

[[00_Inicio|← Painel]]
