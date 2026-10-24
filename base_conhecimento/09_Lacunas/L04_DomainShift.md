---
tipo: lacuna
titulo: "Domain shift espacial e temporal degrada mudança e segmentação"
tema: validacao
status: aberta
tags: [lacuna]
---

# Domain shift espacial e temporal degrada mudança e segmentação

## Descrição

O desempenho cai quando se muda de área e, para a detecção de mudança, quando se muda de ano.

## Evidências nos artigos

- [[Vincent_2024_SatelliteImageTime|Vincent 2024]] (p. 9): queda média do SCS de 39,0% (DynamicEarthNet) e 20,7% (MUDS) sob shift espacial; o shift temporal afeta sobretudo a mudança.

## O que isto afeta (método, dado ou resultado)

- afeta desenho de validação: [[Generalizacao|Generalização e domain shift]]
- afeta desenho de validação: [[DivisaoEspacialBlocos|Divisão espacial por blocos e áreas]]
- afeta desenho de validação: [[DivisaoTemporal|Divisão temporal]]

## Oportunidade (interpretação)

Adotar os três regimes de validação como padrão do projeto e testar com mais de dois anos.

[[00_Sintese_Lacunas|← Síntese das lacunas]]
