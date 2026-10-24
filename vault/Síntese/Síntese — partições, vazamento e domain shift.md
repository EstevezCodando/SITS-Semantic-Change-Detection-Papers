---
tipo: sintese
etapas: ["[[E03 Cubo espaço-temporal e partições|E03]]", "[[E10 Avaliação e incerteza|E10]]"]
tags: [sintese]
---

# Partições, vazamento e domain shift

| Artigo | Unidade de partição | Detalhe | Observação |
|---|---|---|---|
| [[P13 Vincent 2024]] | série/área inteira + ano | três regimes: sem shift, shift temporal (treino 2018, teste 2019) e shift espacial (5 folds de áreas) | **desenho de referência**; queda média de 31,9 % no mIoU e 39,0 % no SCS sob shift espacial (DynamicEarthNet) |
| [[P12 Toker 2022]] | área (AOI) | 55 / 10 / 10 áreas, classes balanceadas | teste oculto, avaliado em servidor |
| [[P10 Etten 2021]] | cubo (área inteira) | 60 treino, 41 teste | patches da mesma área nunca cruzam a divisão |
| [[P05 Zaraza-Aguilera 2022]] | bloco 1,6 km com folga de 0,4 km | 42 / 11 / 4 blocos | folga entre blocos reduz vazamento por vizinhança |
| [[P18 Daudt 2019]] | par de imagens | 146 / 145 pares | crítica ao split aleatório de pixels (lago Eppalock) |
| [[P19 Yang 2021]] | par de imagens | 2.968 / 1.694 | — |
| [[P07 Vizzari 2022]] | pontos 70/30 | mesmos pontos para os 10 modelos | testes dependentes entre abordagens, por isso McNemar e sem κ |
| [[P01 Wagner 2023]] | patches 80/20 + LiDAR independente | validação adicional fora da amostra de treino | acurácia dos patches não mede evento |

## O que a literatura diz
- **Shift espacial é o que mais degrada** (segmentação e mudança); **shift temporal prejudica principalmente a detecção de mudança** ([[P13 Vincent 2024]]).
- Superfície impermeável/edificada generaliza melhor entre áreas que agricultura ou áreas úmidas ([[P13 Vincent 2024]]).
- Observações muito próximas no tempo são altamente correlacionadas e desestabilizam o treino ([[P12 Toker 2022]]).
- Partições por pixel ou por patch vizinho geram overfitting ([[P18 Daudt 2019]]).

## Protocolo proposto (a validar)
1. **Blocos geográficos** (≥ 1,6 km) com folga de pelo menos 0,4 km entre treino, validação e teste ([[P05 Zaraza-Aguilera 2022]]).
2. **Teste espacial** em áreas inéditas e **teste temporal** em período posterior; relatar os dois e o cruzamento dos dois ([[P13 Vincent 2024]]).
3. **Amostra probabilística de avaliação** separada do conjunto escolhido por aprendizado ativo ([[P46 Olofsson 2014]]).
4. Documentar se o teste também muda produto ou resolução (3 m × 5 m).

Etapa relacionada: [[E03 Cubo espaço-temporal e partições]].
