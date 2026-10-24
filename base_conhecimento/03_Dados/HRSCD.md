---
tipo: conceito
subtipo: "conjunto de dados"
titulo: "HRSCD"
aliases: ["HRSCD"]
pasta_tematica: "03_Dados"
n_artigos: 12
tags: [conceito, conjunto-de-dados]
---

# HRSCD

**Natureza:** conjunto de dados. A base distingue algoritmo, arquitetura, ferramenta, tarefa, etapa metodológica, dado e desenho de validação por este campo.

> *Definição, pressupostos e limitações* abaixo são **interpretação/conhecimento geral da base**, salvo onde há token de página. Os fatos dos artigos estão na tabela de evidências.

## Definição

Dataset de mudança semântica em larga escala com rótulos do Urban Atlas: [[Daudt_2019_MultitaskLearningLarge|Daudt 2019]] (p. 4).

## Finalidade

Treino supervisionado de mudança semântica.

## Entradas

Pares RGB de 0,5 m.

## Saídas

Mapas de cobertura e de mudança.

## Pressupostos

Rótulos do Urban Atlas representam a cobertura.

## Limitações

Rótulos com 80–85% de precisão e bordas de parcela.

## Evidência nos artigos lidos

| Artigo | Relação | Ocorrências | Páginas | Status de leitura |
|---|---|---:|---|---|
| [[Yang_2021_AsymmetricSiameseNetworks\|Yang 2021]] | emprega conjunto de dados | 35 | 4, 7, 8, 9, 10 | lido (profundo) |
| [[Ding_2022_TemporalSemanticReasoning\|Ding 2022]] | emprega conjunto de dados | 18 | 4, 9, 10, 12 | extraído automaticamente (não lido) |
| [[Daudt_2019_MultitaskLearningLarge\|Daudt 2019]] | emprega conjunto de dados | 16 | 3, 4, 5, 7, 10 | lido (profundo) |
| [[Bernhard_2023_MapFormerBoostingChange\|Bernhard 2023]] | emprega conjunto de dados | 10 | 1, 2, 5, 6, 7 | extraído automaticamente (não lido) |
| [[Chen_2024_ChangeMambaRemoteSensing\|Chen 2024]] | emprega conjunto de dados | 9 | 10, 13 | lido (profundo) |
| [[Zhang_2025_RecurrentSemanticChange\|Zhang 2025]] | emprega conjunto de dados | 8 | 8, 11, 12 | extraído automaticamente (não lido) |
| [[Guo_2025_HRMSSCDHigh\|Guo 2025]] | emprega conjunto de dados | 7 | 1, 2, 3, 5 | extraído automaticamente (não lido) |
| [[Shen_2026_FoundationModelDriven\|Shen 2026]] | emprega conjunto de dados | 5 | 3, 9, 11 | lido (profundo) |
| [[Toker_2022_DynamicEarthNetDailyMulti\|Toker 2022]] | emprega conjunto de dados | 3 | 2, 3 | lido (profundo) |
| [[Zhang_2025_UniChangeUnifyingChange\|Zhang 2025]] | emprega conjunto de dados | 3 | 2, 3, 7 | extraído automaticamente (não lido) |
| [[Shu_2025_SCDNewBenchmark\|Shu 2025]] | emprega conjunto de dados | 3 | 2, 3, 6 | lido (profundo) |
| [[Yongshuo_2025_SemanticRemoteSensing\|Yongshuo 2025]] | emprega conjunto de dados | 2 | 3, 4 | extraído automaticamente (não lido) |

## Navegação

- Mapa: [[MOC_01_AquisicaoDados|Aquisição e seleção de dados]]
- Mapa: [[MOC_07_MudancaSeries|Detecção de mudanças e séries temporais]]
- Lacuna que afeta este conceito: [[L10_TaxonomiaTransicoes|Transições (from–to) são pouco padronizadas]]
