---
tipo: mapa
titulo: "Trilha para o objetivo"
tags: [mapa, trilha]
---

# Trilha para o objetivo: detectar mudanças de cobertura com Planet de ~5 m

> **Objetivo:** identificar de forma automática mudanças na cobertura do solo com imagens ópticas Planet de ~5 m (início de construções, supressão da vegetação, vias). Esta página liga cada etapa do fluxo aos artigos que a sustentam. **Os valores são os relatados por cada estudo e não são comparáveis entre bases diferentes.** A última seção é proposta (interpretação), não resultado.

## Relevância dos artigos

Campo `relevancia_objetivo` de cada nota: **A** (16) dado Planet de 3–5 m e alvo próximo, texto lido; **B** (15) método, validação ou alerta transferível, texto lido; **C** (10) contexto, revisão ou ferramenta; **D** (62) não lido, ver [[Pendencias_Leitura]].

## Resultados mais próximos do objetivo

| Artigo | Dado | Alvo | Métrica relatada | Força da validação (minha leitura) |
|---|---|---|---|---|
| [[Zhang_2023_MonitoringMonthlyTropical\|Zhang 2023]] | NICFI mensal, 5 m | perda de dossel | usuário 84,7 ± 2,9%; produtor 61,5 ± 46,4% | alta (estratificada, três intérpretes); omissão incerta |
| [[Wagner_2023_MappingTropicalForest\|Wagner 2023]] | NICFI mensal, 4,77 m | cobertura arbórea e desmatamento | OA 98,11%; F1 0,982; interseção mediana de 67,2% com o PRODES | média (LiDAR e produtos de perda; sem amostragem probabilística) |
| [[Carter_2024_DetectionForestDisturbance\|Carter 2024]] | PlanetScope RGB mensal | perturbação florestal | LiDAR 77,77%; perda vs CALFIRE F1 54,5% | média (referência independente, mas frágil para perda) |
| [[Masolele_2024_MappingDiversityLand\|Masolele 2024]] | NICFI anual, 5 m | uso após desmatamento | F1 84 ± 0,7%; mapa com usuário 85% e produtor 84% | média (teste independente; uso de 2022 como proxy) |
| [[Wang_2024_ValidationDeforestationHigh\|Wang 2024]] | par NICFI | confirmação de supressão | F1 0,825 (U-Net) contra 0,55 (RF) | baixa (divisão aleatória, uma janela) |
| [[GonzalezVelez_2026_TropicalDryForest\|GonzalezVelez 2026]] | NICFI 5 m + Sentinel-1 | cobertura e mudança em floresta seca | mIoU 84,7–88,1%; TDF 21.307 → 18.586 ha | baixa para a mudança (sem validação independente) |
| [[Vincent_2024_SatelliteImageTime\|Vincent 2024]] | DynamicEarthNet e MUDS | mudança semântica em séries | SCS 31,7 e BC 22,4 sem shift; queda de 39% do SCS sob shift espacial | alta (três regimes) |
| [[Etten_2021_SpaceNetMultiTemporal\|Etten 2021]] | SpaceNet 7, ~4 m | construção de edificações | campeão: F1 0,61; mudança 0,20; SCOT 0,41 | média (rótulos oniscientes) |
| [[Glazer_2025_TEMPOGlobalTemporal\|Glazer 2025]] | basemaps trimestrais, 4,7 m | edificações | F1 de presença 0,85–0,88 (SpaceNet 7) | média (mede presença, não mudança) |
| [[ZarazaAguilera_2022_ChangeDetectionOver\|ZarazaAguilera 2022]] | PlanetScope 3 m | mineração | IoU 0,70–0,81; kappa > 0,92 | média (Olofsson; uma mina) |
| [[Toker_2022_DynamicEarthNetDailyMulti\|Toker 2022]] | Planet Fusion diário, 3 m | mudança semântica | mIoU 33,5–43,6%; SCS 15,6–19,1 | média |
| [[Crato_2025_DetectionRuralRoads\|Crato 2025]] | Planet ~5 m | estradas rurais | F1 69%; mIoU 55% | média-baixa (uma data) |
| [[Simsek_2025_DeterminationLandLand\|Simsek 2025]] | PlanetScope 3 m, 9 datas | cobertura e mudança cadastral | acurácia global 93,14% | baixa (divisão por pixel) |

A coluna final é interpretação desta base: resume o desenho de validação lido em cada ficha (divisão, referência independente e amostragem).

## 1. Dados e produto Planet

*Qual produto e qual cadência?*

- [[Zhang_2023_MonitoringMonthlyTropical|Zhang 2023]] (relevância A) — NICFI mensal de 4 bandas em reflectância de superfície, harmonizado entre satélites e coregistrado (p. 6–7); mosaicos mensais só desde set/2020.
- [[Wagner_2023_MappingTropicalForest|Wagner 2023]] (relevância A) — NICFI de 4,77 m, 32 datas e 2.658 tiles, base de uma U-Net para cobertura arbórea.
- [[GonzalezVelez_2026_TropicalDryForest|GonzalezVelez 2026]] (relevância A) — Mosaicos semestrais (2017 e 2019) e anual (2021), mais Sentinel-1; mostra o efeito da cadência.
- [[Glazer_2025_TEMPOGlobalTemporal|Glazer 2025]] (relevância A) — Basemaps trimestrais de 4,7 m; o UDM existe desde 2019 e a Planet mudou o processamento em 2022, criando deslocamento de distribuição (p. 2–3).
- [[Etten_2021_SpaceNetMultiTemporal|Etten 2021]] (relevância A) — Dataset de 24 mosaicos mensais em 101 locais, aberto na AWS.

**Conceitos:** [[PlanetNICFI|Planet NICFI (basemaps)]]

**Lacunas:** [[L02_CadenciaPlanet|A cadência real dos mosaicos Planet nem sempre é mensal]]

## 2. Preparo e qualidade da observação

*Como limpar nuvem, sombra e ruído antes do modelo?*

- [[Zhang_2023_MonitoringMonthlyTropical|Zhang 2023]] (relevância A) — Máscara de nuvem com floresta aleatória e índice HOT; índice Hue referenciado à mediana local de 300 m (p. 9–12).
- [[Glazer_2025_TEMPOGlobalTemporal|Glazer 2025]] (relevância A) — Clareza do pixel em 4 níveis pelo UDM e voto de maioria em 4 datas (p. 7–8).
- [[Wagner_2023_MappingTropicalForest|Wagner 2023]] (relevância A) — Filtro temporal de nuvem com ±3 datas; custo: atraso na data da mudança.
- [[Crato_2025_DetectionRuralRoads|Crato 2025]] (relevância A) — Janelas de 41 × 41 pixels e rótulo com buffer de 2 pixels para alvos lineares.
- [[Masolele_2024_MappingDiversityLand|Masolele 2024]] (relevância A) — NDVI, SAVI e NDMI como canais extras sobre as 4 bandas; patches escolhidos pela perda do Hansen.

**Conceitos:** [[MascaraNuvem|Máscara de nuvem e sombra]], [[IndicesEspectrais|Índices espectrais (NDVI etc.)]]

**Lacunas:** [[L02_CadenciaPlanet|A cadência real dos mosaicos Planet nem sempre é mensal]]

## 3. Rótulos e pré-anotação

*Como obter rótulos sem custo proibitivo?*

- [[Masolele_2024_MappingDiversityLand|Masolele 2024]] (relevância A) — Aprendizado ativo por entropia: F1 macro de 43% para 84% em dois ciclos (p. 2, 10).
- [[Wagner_2023_MappingTropicalForest|Wagner 2023]] (relevância A) — Rótulos por k-textures com correção manual.
- [[Carter_2024_DetectionForestDisturbance|Carter 2024]] (relevância A) — Três ciclos de aprendizado ativo, 7.141 patches de 256 × 256 (p. 4).
- [[GonzalezVelez_2026_TropicalDryForest|GonzalezVelez 2026]] (relevância A) — Pseudo-rótulos por clusterização; o desempenho cai com mais de ~40% de pseudo-rótulos (p. 15).
- [[Etten_2021_SpaceNetMultiTemporal|Etten 2021]] (relevância A) — Rótulos "oniscientes" em 7 meses, com imagem melhor que a de entrada (p. 3).

**Conceitos:** [[Rotulagem|Rotulagem e anotação]], [[RotulagemTemporal|Rotulagem temporalmente consistente]], [[PreAnotacaoSAM|Pré-anotação assistida (SAM e plugins QGIS)]]

**Lacunas:** [[L05_RotulosTemporais|Rótulos temporais são caros e subjetivos]]

## 4. Modelos de partida

*Qual modelo testar primeiro?*

- [[Zhang_2023_MonitoringMonthlyTropical|Zhang 2023]] (relevância A) — Linha de base interpretável sem treino (rHue + persistência).
- [[Wang_2024_ValidationDeforestationHigh|Wang 2024]] (relevância A) — U-Net bitemporal de confirmação: F1 0,825 contra 0,55 do random forest em pixel isolado (p. 5).
- [[Masolele_2024_MappingDiversityLand|Masolele 2024]] (relevância A) — Attention U-Net com Focal Loss para classes raras.
- [[Vincent_2024_SatelliteImageTime|Vincent 2024]] (relevância A) — U-TAE modificado para série completa e mudança semântica; protocolo com shift.
- [[Shen_2026_FoundationModelDriven|Shen 2026]] (relevância B) — Modelo fundacional com decodificador modular; não testado em 3–5 m.

**Conceitos:** [[UNet|U-Net]], [[MudancaSemantica|Mudança semântica (from–to)]], [[UTAE|U-TAE (U-Net com atenção temporal)]], [[ModeloFundacional|Modelos fundacionais]]

**Lacunas:** [[L12_SupressaoSemComparacao|Supressão de vegetação em NICFI mensal: os métodos não foram comparados nos mesmos dados]]

## 5. Pós-processamento temporal

*Como transformar mapas por data em eventos confiáveis?*

- [[Zhang_2023_MonitoringMonthlyTropical|Zhang 2023]] (relevância A) — Persistência em ≥ 3 de 5 observações; confirma o evento ao custo de 3 meses (p. 13, 23).
- [[Etten_2021_SpaceNetMultiTemporal|Etten 2021]] (relevância A) — Colapso temporal: localizar uma vez e datar depois; mudança de 0,06 para 0,20 (p. 8–9).
- [[Glazer_2025_TEMPOGlobalTemporal|Glazer 2025]] (relevância A) — Janela de 4 trimestres; atraso de até um trimestre (p. 15).
- [[Ygorra_2024_NearRealTime|Ygorra 2024]] (relevância B) — 3 imagens depois da data; ~36 dias de atraso (p. 10).
- [[Reiche_2021_ForestDisturbanceAlerts|Reiche 2021]] (relevância B) — Confirmação bayesiana em até 90 dias (p. 5).

**Conceitos:** [[PersistenciaConfirmacao|Persistência e confirmação]], [[QuaseTempoReal|Quase tempo real e latência]]

**Lacunas:** [[L11_InicioConstrucao5m|Início de construção em ~5 m: o melhor escore de mudança relatado é baixo]]

## 6. Validação

*Como medir sem se enganar?*

- [[Zhang_2023_MonitoringMonthlyTropical|Zhang 2023]] (relevância A) — Amostragem estratificada por mês, 1.400 pontos e três intérpretes (p. 7).
- [[Carter_2024_DetectionForestDisturbance|Carter 2024]] (relevância A) — Referência independente por altura LiDAR.
- [[Vincent_2024_SatelliteImageTime|Vincent 2024]] (relevância A) — Três regimes: sem shift, temporal e espacial.
- [[GonzalezVelez_2026_TropicalDryForest|GonzalezVelez 2026]] (relevância A) — Divisão por tiles inteiros e por ano.
- [[Etten_2021_SpaceNetMultiTemporal|Etten 2021]] (relevância A) — Métrica SCOT para rastreio e mudança.

**Conceitos:** [[Generalizacao|Generalização e domain shift]], [[DivisaoEspacialBlocos|Divisão espacial por blocos e áreas]], [[AmostragemEstratificada|Amostragem estratificada]], [[EstimativaArea|Estimativa de área com intervalo de confiança]]

**Lacunas:** [[L13_DivisaoAleatoriaComum|Divisão aleatória ou por pixel é comum e infla as métricas]], [[L14_ReferenciaVisualFragil|Referência visual tem discordância e depende de dados sem nuvem]], [[L04_DomainShift|Domain shift espacial e temporal degrada mudança e segmentação]]

## 7. Monitoramento e operação

*Como confirmar e operar?*

- [[Reiche_2024_IntegratingSatelliteForest|Reiche 2024]] (relevância B) — Integrar alertas adianta a detecção em 9 a 38 dias e eleva o produtor a 97% (p. 10–11).
- [[Doblas_2022_DETEROperationalNear|Doblas 2022]] (relevância B) — Sistema operacional: 88.572 alertas em 12 meses, falsos positivos < 0,2% da área revisada (p. 1).
- [[Reiche_2021_ForestDisturbanceAlerts|Reiche 2021]] (relevância B) — Alerta público com confirmação em até 90 dias.
- [[Wu_2026_GeoAIPythonPackage|Wu 2026]] (relevância C) — QGIS e GeoAI como apoio de revisão, sem avaliação quantitativa.

**Conceitos:** [[Alertas|Alertas de mudança]], [[QGIS|QGIS]]

**Lacunas:** [[L01_ValidacaoOperacional|Quase nenhum estudo avalia monitoramento contínuo]]

## Proposta de arquitetura inicial (interpretação)

Não é conclusão experimental: é um ponto de partida montado a partir do que as fichas mostram.

1. Dados: NICFI mensal de 4 bandas, com a cadência registrada por arquivo ([[Zhang_2023_MonitoringMonthlyTropical|Zhang 2023]], [[Wagner_2023_MappingTropicalForest|Wagner 2023]]).
2. Qualidade: máscara de nuvem com UDM e clareza do pixel; coregistro verificado ([[Zhang_2023_MonitoringMonthlyTropical|Zhang 2023]], [[Glazer_2025_TEMPOGlobalTemporal|Glazer 2025]]).
3. Supressão de vegetação: linha de base rHue com persistência de 3 meses ([[Zhang_2023_MonitoringMonthlyTropical|Zhang 2023]]), comparada com U-Net por data ([[Wagner_2023_MappingTropicalForest|Wagner 2023]], [[Carter_2024_DetectionForestDisturbance|Carter 2024]]) e U-Net bitemporal de confirmação ([[Wang_2024_ValidationDeforestationHigh|Wang 2024]]).
4. Construção e vias: detector por data com ampliação 3× e máscara de footprint, borda e contato, seguido de colapso temporal ([[Etten_2021_SpaceNetMultiTemporal|Etten 2021]]) ou janela de 4 datas ([[Glazer_2025_TEMPOGlobalTemporal|Glazer 2025]]).
5. Rótulos: aprendizado ativo por entropia ([[Masolele_2024_MappingDiversityLand|Masolele 2024]]) sobre pré-anotações por k-textures ou clusterização ([[Wagner_2023_MappingTropicalForest|Wagner 2023]], [[GonzalezVelez_2026_TropicalDryForest|GonzalezVelez 2026]]).
6. Validação: blocos com buffer e teste em região independente ([[GonzalezVelez_2026_TropicalDryForest|GonzalezVelez 2026]], [[Vincent_2024_SatelliteImageTime|Vincent 2024]]), amostragem estratificada por mês com três intérpretes ([[Zhang_2023_MonitoringMonthlyTropical|Zhang 2023]]) e métrica por evento ([[Etten_2021_SpaceNetMultiTemporal|Etten 2021]]).
7. Operação: confirmação por ≥ 3 observações e integração com alertas externos ([[Reiche_2021_ForestDisturbanceAlerts|Reiche 2021]], [[Reiche_2024_IntegratingSatelliteForest|Reiche 2024]]), com revisão humana ([[Doblas_2022_DETEROperationalNear|Doblas 2022]]).

Canvas desta trilha: `Canvas_Trilha_Objetivo.canvas` (pasta `01_Mapas`).

[[00_Inicio|← Painel]]
