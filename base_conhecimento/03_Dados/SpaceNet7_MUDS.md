---
tipo: conceito
subtipo: "conjunto de dados"
titulo: "SpaceNet 7 / MUDS"
aliases: ["SpaceNet 7 / MUDS"]
pasta_tematica: "03_Dados"
n_artigos: 6
tags: [conceito, conjunto-de-dados]
---

# SpaceNet 7 / MUDS

**Natureza:** conjunto de dados. A base distingue algoritmo, arquitetura, ferramenta, tarefa, etapa metodológica, dado e desenho de validação por este campo.

> *Definição, pressupostos e limitações* abaixo são **interpretação/conhecimento geral da base**, salvo onde há token de página. Os fatos dos artigos estão na tabela de evidências.

## Definição

Mosaicos mensais Planet RGB de ~4 m, com polígonos de edificações e IDs persistentes: [[Etten_2021_MultiTemporalUrban|Etten 2021]] (p. 2).

## Finalidade

Acompanhar construção e demolição em séries mensais.

## Entradas

Mosaicos mensais e UDM.

## Saídas

Polígonos com identidade temporal.

## Pressupostos

Rótulos temporalmente consistentes.

## Limitações

Rótulos feitos com apoio de mapa de alta resolução; mudança rara.

## Evidência nos artigos lidos

| Artigo | Relação | Ocorrências | Páginas | Status de leitura |
|---|---|---:|---|---|
| [[Vincent_2024_SatelliteImageTime\|Vincent 2024]] | emprega conjunto de dados | 31 | 1, 3, 4, 5, 6 | lido (profundo) |
| [[Etten_2021_SpaceNetMultiTemporal\|Etten 2021]] | emprega conjunto de dados | 26 | 1, 2, 3, 5, 6 | lido (profundo) |
| [[Etten_2021_MultiTemporalUrban\|Etten 2021]] | emprega conjunto de dados | 24 | 1, 2, 3, 4, 5 | lido (profundo) |
| [[Glazer_2025_TEMPOGlobalTemporal\|Glazer 2025]] | emprega conjunto de dados | 10 | 4, 5, 10, 12 | lido (profundo) |
| [[He_2022_TrackingUrbanizationDeveloping\|He 2022]] | emprega conjunto de dados | 8 | 2, 3, 4, 5 | extraído automaticamente (não lido) |
| [[Metzger_2023_UrbanChangeForecasting\|Metzger 2023]] | emprega conjunto de dados | 5 | 1, 4, 9 | lido (profundo) |

## Navegação

- Mapa: [[MOC_01_AquisicaoDados|Aquisição e seleção de dados]]
- Mapa: [[MOC_07_MudancaSeries|Detecção de mudanças e séries temporais]]
- Lacuna que afeta este conceito: [[L07_ResolucaoObjetosPequenos|Objetos de poucos pixels limitam edificações e vias em 3–5 m]]
- Lacuna que afeta este conceito: [[L11_InicioConstrucao5m|Início de construção em ~5 m: o melhor escore de mudança relatado é baixo]]
