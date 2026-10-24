---
tipo: lacuna
titulo: "Transições (from–to) são pouco padronizadas"
tema: dados
status: aberta
tags: [lacuna]
---

# Transições (from–to) são pouco padronizadas

## Descrição

DynamicEarthNet usa 7 classes, SECOND 6 (30 transições) e HRSCD 5 no nível L1; causa e legalidade não são observáveis em imagem.

## Evidências nos artigos

- [[Toker_2022_DynamicEarthNetDailyMulti|Toker 2022]] (p. 3): 7 classes.
- [[Yang_2021_AsymmetricSiameseNetworks|Yang 2021]] (p. 6): 6 classes → 30 tipos.
- [[Daudt_2019_MultitaskLearningLarge|Daudt 2019]] (p. 5): 5 classes no nível L1.

## O que isto afeta (método, dado ou resultado)

- afeta métrica: [[MetricasMudancaSemantica|Métricas de mudança semântica (SeK, SCS, SCOT)]]
- afeta conjunto de dados: [[DynamicEarthNet|DynamicEarthNet]]
- afeta conjunto de dados: [[SECOND|SECOND]]
- afeta conjunto de dados: [[HRSCD|HRSCD]]

## Oportunidade (interpretação)

Fixar uma taxonomia enxuta e validar com amostras locais.

[[00_Sintese_Lacunas|← Síntese das lacunas]]
