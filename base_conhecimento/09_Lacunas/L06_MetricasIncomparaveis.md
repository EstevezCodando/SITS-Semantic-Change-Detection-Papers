---
tipo: lacuna
titulo: "Métricas e benchmarks não são comparáveis entre estudos"
tema: validacao
status: aberta
tags: [lacuna]
---

# Métricas e benchmarks não são comparáveis entre estudos

## Descrição

F1, IoU, kappa, SeK, SCS e SCOT medem coisas diferentes, em bases, classes e resoluções diferentes.

## Evidências nos artigos

- [[Yang_2021_AsymmetricSiameseNetworks|Yang 2021]] (p. 6): OA e kappa enganosos; propõe SeK.
- [[Toker_2022_DynamicEarthNetDailyMulti|Toker 2022]] (p. 5): propõe SCS.
- [[Etten_2021_MultiTemporalUrban|Etten 2021]] (p. 1): propõe SCOT.
- [[Vizzari_2022_PlanetScopeSentinelSentinel|Vizzari 2022]] (§ 2.3.5): critica o kappa e usa McNemar.

## O que isto afeta (método, dado ou resultado)

- afeta métrica: [[MetricasMudancaSemantica|Métricas de mudança semântica (SeK, SCS, SCOT)]]
- afeta métrica: [[Kappa|Coeficiente kappa]]
- afeta métrica: [[F1|F1]]

## Oportunidade (interpretação)

Comparar métodos apenas no mesmo conjunto de dados, divisão e métrica; relatar blocos separados.

[[00_Sintese_Lacunas|← Síntese das lacunas]]
