---
tipo: conceito
subtipo: "métrica"
titulo: "Métricas de mudança semântica (SeK, SCS, SCOT)"
aliases: ["Métricas de mudança semântica (SeK, SCS, SCOT)"]
pasta_tematica: "06_Validacao"
n_artigos: 7
tags: [conceito, metrica]
---

# Métricas de mudança semântica (SeK, SCS, SCOT)

**Natureza:** métrica. A base distingue algoritmo, arquitetura, ferramenta, tarefa, etapa metodológica, dado e desenho de validação por este campo.

> *Definição, pressupostos e limitações* abaixo são **interpretação/conhecimento geral da base**, salvo onde há token de página. Os fatos dos artigos estão na tabela de evidências.

## Definição

Métricas criadas para mudança rara e semântica: SeK (P19), SCS = média(BC, SC) (P12) e SCOT, que combina rastreamento e mudança de objetos (P10).

## Finalidade

Avaliar onde e para qual classe houve mudança sem que a classe "sem mudança" domine o resultado.

## Entradas

Mapas antes/depois e referência; polígonos com ID para SCOT.

## Saídas

Valores por métrica.

## Pressupostos

Referência com pares de classes e máscara de não-mudança.

## Limitações

Valores não comparáveis entre datasets distintos.

## Evidência nos artigos lidos

| Artigo | Relação | Ocorrências | Páginas | Status de leitura |
|---|---|---:|---|---|
| [[Etten_2021_MultiTemporalUrban\|Etten 2021]] | referencia (suporte manual da leitura) | — | ver nota do artigo | lido (profundo) |
| [[Etten_2021_SpaceNetMultiTemporal\|Etten 2021]] | referência (curado pela leitura) | — | ver nota do artigo | lido (profundo) |
| [[Toker_2022_DynamicEarthNetDailyMulti\|Toker 2022]] | referencia (suporte manual da leitura) | — | ver nota do artigo | lido (profundo) |
| [[Vincent_2024_SatelliteImageTime\|Vincent 2024]] | referencia (suporte manual da leitura) | — | ver nota do artigo | lido (profundo) |
| [[Yang_2021_AsymmetricSiameseNetworks\|Yang 2021]] | referencia (suporte manual da leitura) | — | ver nota do artigo | lido (profundo) |
| [[Chen_2024_ChangeMambaRemoteSensing\|Chen 2024]] | referência (curado pela leitura) | — | ver nota do artigo | lido (profundo) |
| [[Shen_2026_FoundationModelDriven\|Shen 2026]] | referência (curado pela leitura) | — | ver nota do artigo | lido (profundo) |

## Navegação

- Mapa: [[MOC_07_MudancaSeries|Detecção de mudanças e séries temporais]]
- Mapa: [[MOC_08_ValidacaoIncerteza|Validação e incerteza]]
- Lacuna que afeta este conceito: [[L03_MudancaRara|Mudança rara: métricas e perdas ainda penalizam eventos]]
- Lacuna que afeta este conceito: [[L06_MetricasIncomparaveis|Métricas e benchmarks não são comparáveis entre estudos]]
- Lacuna que afeta este conceito: [[L10_TaxonomiaTransicoes|Transições (from–to) são pouco padronizadas]]
