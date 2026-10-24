---
tipo: lacuna
titulo: "Quase nenhum estudo avalia monitoramento contínuo"
tema: monitoramento
status: aberta
tags: [lacuna]
---

# Quase nenhum estudo avalia monitoramento contínuo

## Descrição

Os estudos lidos são retrospectivos. Nenhum dos artigos aprofundados reporta latência de alerta, falsos alertas por km²/mês, custo de revisão humana ou drift em operação contínua.

## Evidências nos artigos

- [[Wagner_2023_MappingTropicalForest|Wagner 2023]] (p. 16): para detecção rápida, o autor aponta o radar.
- [[Vincent_2024_SatelliteImageTime|Vincent 2024]] (p. 1): o artigo reconhece a necessidade, mas mede só um ano de shift temporal.
- [[Toker_2022_DynamicEarthNetDailyMulti|Toker 2022]] e [[Etten_2021_MultiTemporalUrban|Etten 2021]] são benchmarks com rótulos mensais, sem medir operação.

## O que isto afeta (método, dado ou resultado)

- afeta operação: [[Alertas|Alertas de mudança]]

## Oportunidade (interpretação)

Desenhar um experimento retrospectivo que simule o regime operacional (só o passado disponível) e meça falsos alertas e tempo de revisão.

[[00_Sintese_Lacunas|← Síntese das lacunas]]
