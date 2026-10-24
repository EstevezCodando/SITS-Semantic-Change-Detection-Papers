---
tipo: lacuna
titulo: "Supressão de vegetação em NICFI mensal: os métodos não foram comparados nos mesmos dados"
tema: validacao
status: aberta
tags: [lacuna]
---

# Supressão de vegetação em NICFI mensal: os métodos não foram comparados nos mesmos dados

## Descrição

P91 usa índice e persistência sem rótulos; P01 e P03 classificam por data com U-Net; P04 valida alertas com U-Net bitemporal. Nenhum estudo compara essas famílias na mesma área e com a mesma referência.

## Evidências nos artigos

- [[Zhang_2023_MonitoringMonthlyTropical|Zhang 2023]] (tabela 3, p. 21): usuário 84,7%, produtor 61,5 ± 46,4%.
- [[Wang_2024_ValidationDeforestationHigh|Wang 2024]] (tabela 1, p. 5): U-Net com F1 0,825, em divisão aleatória.
- [[Wagner_2023_MappingTropicalForest|Wagner 2023]] e [[Carter_2024_DetectionForestDisturbance|Carter 2024]]: classificação por data com validação por LiDAR e produtos de perda.

## O que isto afeta (método, dado ou resultado)

- afeta dado/produto: [[PlanetNICFI|Planet NICFI (basemaps)]]
- afeta tarefa: [[Desmatamento|Desmatamento]]

## Oportunidade (interpretação)

Comparar rHue com persistência, U-Net por data e U-Net bitemporal numa mesma área, com amostragem estratificada por mês.

[[00_Sintese_Lacunas|← Síntese das lacunas]]
