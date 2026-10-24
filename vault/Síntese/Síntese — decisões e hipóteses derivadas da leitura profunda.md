---
tipo: sintese
etapas: ["[[E03 Cubo espaço-temporal e partições|E03]]", "[[E04 Rotulagem e pré-anotação|E04]]", "[[E06 Modelos-base de cobertura|E06]]", "[[E07 Modelos de mudança em pares|E07]]", "[[E08 Modelos de série temporal|E08]]", "[[E10 Avaliação e incerteza|E10]]"]
tags: [sintese]
---

# Decisões e hipóteses derivadas da leitura profunda

Cada linha é uma **hipótese de trabalho** apoiada por evidência dos artigos lidos, a ser confirmada nos nossos dados. Nada aqui é resultado do projeto.

| # | Decisão / hipótese | Evidência | Etapa | Teste |
|---|---|---|---|---|
| D1 | Medir desempenho em **três regimes** (sem shift, shift temporal, shift espacial) | [[P13 Vincent 2024]] | [[E03 Cubo espaço-temporal e partições]] | relatar os três lado a lado |
| D2 | Usar **blocos de ≥ 1,6 km com folga** nas partições | [[P05 Zaraza-Aguilera 2022]] | E03 | verificar ausência de vizinhança entre treino e teste |
| D3 | **Evitar OA e κ**; usar SeK, SCS e F1 por classe e por transição | [[P18 Daudt 2019]], [[P19 Yang 2021]], [[P12 Toker 2022]] | [[E10 Avaliação e incerteza]] | tabela de métricas por bloco |
| D4 | **Estimar hectares por amostra probabilística com IC** | [[P46 Olofsson 2014]], [[P05 Zaraza-Aguilera 2022]] | E10 | comparar área mapeada × estimada |
| D5 | Rotular com **cópia sequencial e revisão pela série inteira**, com UDM de nuvem/co-registro | [[P10 Etten 2021]] | [[E04 Rotulagem e pré-anotação]] | medir tempo e acordo entre anotadores |
| D6 | Pré-anotar com **segmentação não supervisionada/SAM** e medir o ganho de tempo | [[P01 Wagner 2023]] | E04 | EXP6 com 3 condições |
| D7 | Baseline 1: **OB (SNIC + GLCM) + RF/XGBoost** com janelas em metros | [[P07 Vizzari 2022]] | [[E06 Modelos-base de cobertura]] | EXP1 |
| D8 | Baseline 2: **U-Net 256² × 4 bandas, BCE+Dice** com regra de persistência temporal | [[P01 Wagner 2023]] | E06 | EXP2 |
| D9 | Comparar **pós-classificação × mudança direta** nos mesmos blocos | [[P05 Zaraza-Aguilera 2022]] | [[E07 Modelos de mudança em pares]] | EXP2 × EXP3 |
| D10 | Para from–to, testar o **treino sequencial** (cobertura primeiro, mudança depois) | [[P18 Daudt 2019]] | E07 | EXP4 |
| D11 | Para série, **inferência com a série completa** e treino com meses sorteados | [[P13 Vincent 2024]] | [[E08 Modelos de série temporal]] | EXP5 |
| D12 | **Não depender de NDVI** como entrada no primeiro ciclo | [[P05 Zaraza-Aguilera 2022]] | E06 | ablação 4 × 5 bandas |
| D13 | Esperar **F1 de edificações ~0,45 e mudança < 0,1** em 4–5 px como patamar | [[P10 Etten 2021]], [[P13 Vincent 2024]] | E10 | relatar por faixa de tamanho |
| D14 | Tratar **degradação separada de desmatamento** | [[P01 Wagner 2023]], [[P02 Dalagnol 2023]] | E09 | classe própria na taxonomia |
| D15 | Dar prioridade ao **tratamento de nuvem** antes da pós-classificação | [[P05 Zaraza-Aguilera 2022]] | [[E02 Qualidade e harmonização]] | comparar com e sem máscara |

## Perguntas em aberto que a leitura não resolve
- A cadência real dos nossos arquivos é mensal? Quantos meses são válidos por área?
- Qual o menor evento detectável em 3 m vs 5 m?
- Um modelo de série supera o de pares quando a mudança é 0,03–1,3 % dos pixels? ([[P13 Vincent 2024]] sugere que não de forma consistente.)
- Quanto custa a revisão humana por evento confirmado?

## Lacunas de leitura
- [[P02 Dalagnol 2023]], [[P14 He 2024]], [[P46 Olofsson 2014]], [[P156 Aszkowski 2023]] e [[P164 Wang 2024]] foram lidos apenas em resumos, documentação e repositórios.

## Decisões adicionais (ferramentas GeoAI/QGIS)
| # | Decisão / hipótese | Evidência | Etapa | Teste |
|---|---|---|---|---|
| D16 | Usar **QGIS para pré-anotar, revisar e inspecionar**, e o pipeline Python para a detecção temporal | [[P155 Wu 2026]], [[P156 Aszkowski 2023]] | [[E04 Rotulagem e pré-anotação]] | EXP6 |
| D17 | Para SAM, partir de **20–30 pontos** e selecionar a máscara **sem usar a anotação** | [[P165 Wang 2025]] | E04 | variar pontos e medir mIoU e tempo |
| D18 | **Codificar cada mosaico uma vez** (Geo-SAM pré-codificado) para cliques rápidos | [[P164 Wang 2024]] | E04 | tempo por evento |
| D19 | **IAMAP** (similaridade/agrupamento) para escolher exemplos antes de rotular | [[P157 Tresson 2026]] | E04 / [[E05 Atributos e representações]] | amostras necessárias vs baseline EXP1 |
| D20 | **Registrar parâmetros dos plugins** (resolução, sobreposição, remoção de segmentos) como parte do `processing_run` | [[P158 Febrita 2025]] | E11 | auditoria de reprodutibilidade |
| D21 | Testar a rota **U-Net → ONNX → Deepness** para revisão em QGIS, verificando entradas de 4 bandas | [[P156 Aszkowski 2023]] | [[E11 Operação e atualização]] | teste de conversão |
