---
tipo: lacuna
titulo: "Mudança rara: métricas e perdas ainda penalizam eventos"
tema: validacao
status: aberta
tags: [lacuna]
---

# Mudança rara: métricas e perdas ainda penalizam eventos

## Descrição

A fração de pixels que mudam é pequena (≈5% mensal no DynamicEarthNet, 1,28% e 0,03% em P13; 0,115% de transições raras em HRSCD).

## Evidências nos artigos

- [[Vincent_2024_SatelliteImageTime|Vincent 2024]] (p. 9): BC abaixo de 23% em todos os métodos.
- [[Daudt_2019_MultitaskLearningLarge|Daudt 2019]] (p. 6): 99,232% dos pixels sem mudança.
- [[Toker_2022_DynamicEarthNetDailyMulti|Toker 2022]] (p. 5): ≈5% de pixels mudam de um mês para outro.

## O que isto afeta (método, dado ou resultado)

- afeta problema de validação: [[Desbalanceamento|Desbalanceamento de classes]]
- afeta métrica: [[MetricasMudancaSemantica|Métricas de mudança semântica (SeK, SCS, SCOT)]]
- afeta métrica: [[AcuraciaGlobal|Acurácia global (OA)]]

## Oportunidade (interpretação)

Combinar perdas para classes raras, amostragem estratificada de eventos e métricas por evento.

[[00_Sintese_Lacunas|← Síntese das lacunas]]
