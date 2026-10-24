---
tipo: lacuna
titulo: "Divisão aleatória ou por pixel é comum e infla as métricas"
tema: validacao
status: aberta
tags: [lacuna]
---

# Divisão aleatória ou por pixel é comum e infla as métricas

## Descrição

Vários estudos Planet dividem treino e teste ao acaso ou por pixel, o que deixa vizinhos espaciais nos dois conjuntos; outros dividem por tile, bloco ou região.

## Evidências nos artigos

- [[Simsek_2025_DeterminationLandLand|Simsek 2025]] (p. 6): 70% e 30% dos pixels de referência.
- [[Wang_2024_ValidationDeforestationHigh|Wang 2024]] (p. 3): divisão aleatória 80/10/10.
- [[GonzalezVelez_2026_TropicalDryForest|GonzalezVelez 2026]] e [[Vincent_2024_SatelliteImageTime|Vincent 2024]]: divisão por tiles inteiros e por regimes de shift, como alternativa.

## O que isto afeta (método, dado ou resultado)

- afeta desenho de validação: [[DivisaoEspacialBlocos|Divisão espacial por blocos e áreas]]
- afeta desenho de validação: [[Generalizacao|Generalização e domain shift]]

## Oportunidade (interpretação)

Adotar blocos com buffer e teste em região independente como padrão do projeto.

[[00_Sintese_Lacunas|← Síntese das lacunas]]
