---
tipo: conceito
subtipo: "arquitetura"
titulo: "U-Net"
aliases: ["U-Net"]
pasta_tematica: "05_Metodos"
n_artigos: 14
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
| [[Jelas_2024_DeforestationDetectionDeep\|Jelas 2024]] | utiliza método | 94 | 1, 6, 7, 8, 9 | lido (parcial) |
| [[GonzalezVelez_2026_TropicalDryForest\|GonzalezVelez 2026]] | utiliza método | 47 | 1, 5, 7, 10, 12 | lido (profundo) |
| [[Crato_2025_DetectionRuralRoads\|Crato 2025]] | utiliza método | 30 | 1, 2, 3, 5, 6 | lido (profundo) |
| [[Wagner_2023_MappingTropicalForest\|Wagner 2023]] | utiliza método | 25 | 3, 4, 6, 7, 8 | lido (profundo) |
| [[ZarazaAguilera_2022_ChangeDetectionOver\|ZarazaAguilera 2022]] | utiliza método | 24 | 1, 2, 3, 4, 5 | lido (profundo) |
| [[Carter_2024_DetectionForestDisturbance\|Carter 2024]] | utiliza método | 22 | 1, 2, 3, 4, 6 | lido (profundo) |
| [[Boutayeb_2024_ComprehensiveGeoAIReview\|Boutayeb 2024]] | utiliza método | 21 | 6, 17, 18, 19, 20 | lido (parcial) |
| [[Wang_2024_ValidationDeforestationHigh\|Wang 2024]] | utiliza método | 17 | 2, 3, 4, 5 | lido (profundo) |
| [[Masolele_2024_MappingDiversityLand\|Masolele 2024]] | utiliza método | 7 | 3, 8, 9, 10, 12 | lido (profundo) |
| [[Metzger_2023_UrbanChangeForecasting\|Metzger 2023]] | utiliza método | 7 | 1, 2, 3 | lido (profundo) |
| [[Glazer_2025_TEMPOGlobalTemporal\|Glazer 2025]] | utiliza método | 6 | 6, 10, 15 | lido (profundo) |
| [[Etten_2021_SpaceNetMultiTemporal\|Etten 2021]] | utiliza método | 6 | 7, 8 | lido (profundo) |
| [[Dalagnol_2023_MappingTropicalForest\|Dalagnol 2023]] | referência (curado pela leitura) | — | ver nota do artigo | lido (parcial) |
| [[Etten_2021_MultiTemporalUrban\|Etten 2021]] | referência (curado pela leitura) | — | ver nota do artigo | lido (profundo) |

## Navegação

