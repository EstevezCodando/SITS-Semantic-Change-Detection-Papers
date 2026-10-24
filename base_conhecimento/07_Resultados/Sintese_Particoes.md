---
tipo: resultado
titulo: "Síntese — partições, vazamento e domain shift"
tags: [resultado]
---

# Síntese — partições, vazamento e domain shift

> Síntese herdada do vault anterior (`vault/`); os links de artigos foram convertidos para esta base. Afirmações sobre artigos têm fonte nas respectivas notas; itens “hipótese” são interpretação.

# Partições, vazamento e domain shift

| Artigo | Unidade de partição | Detalhe | Observação |
|---|---|---|---|
| [[Vincent_2024_SatelliteImageTime\|Vincent 2024]] | série/área inteira + ano | três regimes: sem shift, shift temporal (treino 2018, teste 2019) e shift espacial (5 folds de áreas) | **desenho de referência**; queda média de 31,9 % no mIoU e 39,0 % no SCS sob shift espacial (DynamicEarthNet) |
| [[Toker_2022_DynamicEarthNetDailyMulti\|Toker 2022]] | área (AOI) | 55 / 10 / 10 áreas, classes balanceadas | teste oculto, avaliado em servidor |
| [[Etten_2021_MultiTemporalUrban\|Etten 2021]] | cubo (área inteira) | 60 treino, 41 teste | patches da mesma área nunca cruzam a divisão |
| [[ZarazaAguilera_2022_ChangeDetectionOver\|ZarazaAguilera 2022]] | bloco 1,6 km com folga de 0,4 km | 42 / 11 / 4 blocos | folga entre blocos reduz vazamento por vizinhança |
| [[Daudt_2019_MultitaskLearningLarge\|Daudt 2019]] | par de imagens | 146 / 145 pares | crítica ao split aleatório de pixels (lago Eppalock) |
| [[Yang_2021_AsymmetricSiameseNetworks\|Yang 2021]] | par de imagens | 2.968 / 1.694 | — |
| [[Vizzari_2022_PlanetScopeSentinelSentinel\|Vizzari 2022]] | pontos 70/30 | mesmos pontos para os 10 modelos | testes dependentes entre abordagens, por isso McNemar e sem κ |
| [[Wagner_2023_MappingTropicalForest\|Wagner 2023]] | patches 80/20 + LiDAR independente | validação adicional fora da amostra de treino | acurácia dos patches não mede evento |

## O que a literatura diz
- **Shift espacial é o que mais degrada** (segmentação e mudança); **shift temporal prejudica principalmente a detecção de mudança** ([[Vincent_2024_SatelliteImageTime|Vincent 2024]]).
- Superfície impermeável/edificada generaliza melhor entre áreas que agricultura ou áreas úmidas ([[Vincent_2024_SatelliteImageTime|Vincent 2024]]).
- Observações muito próximas no tempo são altamente correlacionadas e desestabilizam o treino ([[Toker_2022_DynamicEarthNetDailyMulti|Toker 2022]]).
- Partições por pixel ou por patch vizinho geram overfitting ([[Daudt_2019_MultitaskLearningLarge|Daudt 2019]]).

## Protocolo proposto (a validar)
1. **Blocos geográficos** (≥ 1,6 km) com folga de pelo menos 0,4 km entre treino, validação e teste ([[ZarazaAguilera_2022_ChangeDetectionOver|ZarazaAguilera 2022]]).
2. **Teste espacial** em áreas inéditas e **teste temporal** em período posterior; relatar os dois e o cruzamento dos dois ([[Vincent_2024_SatelliteImageTime|Vincent 2024]]).
3. **Amostra probabilística de avaliação** separada do conjunto escolhido por aprendizado ativo ([[Olofsson_2014_GoodPracticesEstimating|Olofsson 2014]]).
4. Documentar se o teste também muda produto ou resolução (3 m × 5 m).

Etapa relacionada: E03 Cubo espaço-temporal e partições.

[[00_Inicio|← Painel]]
