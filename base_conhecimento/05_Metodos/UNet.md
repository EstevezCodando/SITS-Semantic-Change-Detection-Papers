---
tipo: conceito
subtipo: "arquitetura"
titulo: "U-Net"
aliases: ["U-Net"]
pasta_tematica: "05_Metodos"
n_artigos: 33
tags: [conceito, arquitetura]
---

# U-Net

**Natureza:** arquitetura. A base distingue algoritmo, arquitetura, ferramenta, tarefa, etapa metodológica, dado e desenho de validação por este campo.

> *Definição, pressupostos e limitações* abaixo são **interpretação/conhecimento geral da base**, salvo onde há token de página. Os fatos dos artigos estão na tabela de evidências.

## Definição

Rede encoder–decoder com conexões de salto para segmentação semântica.

## Finalidade

Segmentar cobertura, edificações e vias.

## Entradas

Patches (por exemplo 256×256×4).

## Saídas

Máscara por pixel.

## Pressupostos

Rótulos densos.

## Limitações

Opera em uma imagem por vez, a menos de adaptações temporais; a mudança exige comparar saídas.

## Evidência nos artigos lidos

| Artigo | Relação | Ocorrências | Páginas | Status de leitura |
|---|---|---:|---|---|
| [[Jelas_2024_DeforestationDetectionDeep\|Jelas 2024]] | utiliza método | 94 | 1, 6, 7, 8, 9 | extraído automaticamente (não lido) |
| [[GonzalezVelez_2026_TropicalDryForest\|GonzalezVelez 2026]] | utiliza método | 47 | 1, 5, 7, 10, 12 | extraído automaticamente (não lido) |
| [[Crato_2025_DetectionRuralRoads\|Crato 2025]] | utiliza método | 30 | 1, 2, 3, 5, 6 | extraído automaticamente (não lido) |
| [[Szwarcman_2024_PrithviVersatileMultitemporal\|Szwarcman 2024]] | utiliza método | 30 | 2, 5, 8, 9, 12 | extraído automaticamente (não lido) |
| [[Wagner_2023_MappingTropicalForest\|Wagner 2023]] | utiliza método | 25 | 3, 4, 6, 7, 8 | lido (profundo) |
| [[ZarazaAguilera_2022_ChangeDetectionOver\|ZarazaAguilera 2022]] | utiliza método | 24 | 1, 2, 3, 4, 5 | lido (profundo) |
| [[Miller_2024_DeepLearningSatellite\|Miller 2024]] | utiliza método | 24 | 13, 14, 17, 19, 20 | extraído automaticamente (não lido) |
| [[Shafique_2022_DeepLearningChange\|Shafique 2022]] | utiliza método | 23 | 15, 16, 18, 19, 20 | extraído automaticamente (não lido) |
| [[Bou_2026_RemoteSensingChange\|Bou 2026]] | utiliza método | 23 | 1, 5, 6, 7, 8 | extraído automaticamente (não lido) |
| [[Carter_2024_DetectionForestDisturbance\|Carter 2024]] | utiliza método | 22 | 1, 2, 3, 4, 6 | extraído automaticamente (não lido) |
| [[Boutayeb_2024_ComprehensiveGeoAIReview\|Boutayeb 2024]] | utiliza método | 21 | 6, 17, 18, 19, 20 | extraído automaticamente (não lido) |
| [[Sanca_2023_ENDENDDEEP\|Sanca 2023]] | utiliza método | 18 | 1, 2, 3, 5 | extraído automaticamente (não lido) |
| [[Wang_2024_ValidationDeforestationHigh\|Wang 2024]] | utiliza método | 17 | 2, 3, 4, 5 | extraído automaticamente (não lido) |
| [[Benidir_2025_ChangeYouWant\|Benidir 2025]] | utiliza método | 16 | 3, 5, 6, 7 | extraído automaticamente (não lido) |
| [[Xu_2024_SpecializedFoundationModels\|Xu 2024]] | utiliza método | 14 | 1, 2, 4, 5, 6 | extraído automaticamente (não lido) |
| [[Garnot_2021_PanopticSegmentationSatellite\|Garnot 2021]] | utiliza método | 12 | 2, 3, 4, 7, 8 | extraído automaticamente (não lido) |
| [[Chen_2024_ChangeMambaRemoteSensing\|Chen 2024]] | utiliza método | 12 | 3, 10, 14, 15, 17 | extraído automaticamente (não lido) |
| [[Buslaev_2018_FullyConvolutionalNetwork\|Buslaev 2018]] | utiliza método | 12 | 1, 2, 3 | extraído automaticamente (não lido) |
| [[Papadomanolaki_2019_DetectingUrbanChanges\|Papadomanolaki 2019]] | utiliza método | 11 | 1, 2, 3, 4 | extraído automaticamente (não lido) |
| [[Lei_2026_RemoteSensingImage\|Lei 2026]] | utiliza método | 10 | 12, 14, 16, 17, 21 | extraído automaticamente (não lido) |
| [[Toker_2022_DynamicEarthNetDailyMulti\|Toker 2022]] | utiliza método | 9 | 6, 7 | lido (profundo) |
| [[Cortinhas_2024_UncontrolledIllegalMining\|Cortinhas 2024]] | utiliza método | 9 | 9, 10, 12, 14 | extraído automaticamente (não lido) |
| [[Masolele_2024_MappingDiversityLand\|Masolele 2024]] | utiliza método | 7 | 3, 8, 9, 10, 12 | extraído automaticamente (não lido) |
| [[Metzger_2023_UrbanChangeForecasting\|Metzger 2023]] | utiliza método | 7 | 1, 2, 3 | extraído automaticamente (não lido) |
| [[Glazer_2025_TEMPOGlobalTemporal\|Glazer 2025]] | utiliza método | 6 | 6, 10, 15 | extraído automaticamente (não lido) |
| [[Etten_2021_SpaceNetMultiTemporal\|Etten 2021]] | utiliza método | 6 | 7, 8 | extraído automaticamente (não lido) |
| [[Daudt_2018_FullyConvolutionalSiamese\|Daudt 2018]] | utiliza método | 6 | 2, 3, 5 | extraído automaticamente (não lido) |
| [[Chen_2021_RemoteSensingImage\|Chen 2021]] | utiliza método | 5 | 1, 2, 7, 12, 14 | extraído automaticamente (não lido) |
| [[Ding_2022_TemporalSemanticReasoning\|Ding 2022]] | utiliza método | 4 | 8, 9, 10, 14 | extraído automaticamente (não lido) |
| [[McVicar_2023_SmartflowEnablingScalable\|McVicar 2023]] | utiliza método | 3 | 3, 4 | extraído automaticamente (não lido) |
| [[Andrade_2020_EVALUATIONSEMANTICSEGMENTATION\|Andrade 2020]] | utiliza método | 3 | 2, 3 | extraído automaticamente (não lido) |
| [[Vincent_2024_SatelliteImageTime\|Vincent 2024]] | utiliza método | 3 | 2, 6 | lido (profundo) |
| [[Chen_2021_SelfSupervisedChange\|Chen 2021]] | utiliza método | 3 | 6, 9, 13 | extraído automaticamente (não lido) |

## Navegação

- Mapa: [[MOC_06_DeepLearning|Deep Learning (arquiteturas e estratégias)]]
