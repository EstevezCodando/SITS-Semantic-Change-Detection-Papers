---
tipo: resultado
titulo: "Síntese — métricas por tarefa e armadilhas"
tags: [resultado]
---

# Síntese — métricas por tarefa e armadilhas

> Síntese herdada do vault anterior (`vault/`); os links de artigos foram convertidos para esta base. Afirmações sobre artigos têm fonte nas respectivas notas; itens “hipótese” são interpretação.

# Métricas por tarefa e armadilhas

| Tarefa | Métrica recomendada pelos artigos | Quando usar | Armadilha apontada |
|---|---|---|---|
| Cobertura mensal | IoU/F1 por classe, mIoU | segmentar cobertura em cada mês | mIoU alto não implica boa mudança ([[Toker_2022_DynamicEarthNetDailyMulti\|Toker 2022]]) |
| Mudança binária | F1/IoU da classe "mudança", precisão e recall, curva PR | detectar *onde* | OA e acurácia enganam: 99,2 % dos pixels não mudam ([[Daudt_2019_MultitaskLearningLarge\|Daudt 2019]]) |
| Mudança semântica (from–to) | **SeK** + mIoU ([[Yang_2021_AsymmetricSiameseNetworks\|Yang 2021]]); **SCS = média(BC, SC)** ([[Toker_2022_DynamicEarthNetDailyMulti\|Toker 2022]]) | transições entre classes | κ ainda é dominado pela não-mudança ([[Yang_2021_AsymmetricSiameseNetworks\|Yang 2021]]); SCS fica em ~19 mesmo nos melhores baselines |
| Edificações com identidade | **SCOT** (IoU > 0,25, `F_track` + `F_change`, β = 2) ([[Etten_2021_MultiTemporalUrban\|Etten 2021]]) | contar edifícios novos e acompanhá-los | modelo estático tem termo de mudança 0; exigir também F1 por faixa de tamanho |
| Cobertura de classes (testes de hipótese) | PA/UA/F por classe + **McNemar** ([[Vizzari_2022_PlanetScopeSentinelSentinel\|Vizzari 2022]]) | comparar classificadores no mesmo conjunto | κ não é calculável com testes dependentes ([[Vizzari_2022_PlanetScopeSentinelSentinel\|Vizzari 2022]]) |
| Área alterada | **estimativa amostral com IC** ([[Olofsson_2014_GoodPracticesEstimating\|Olofsson 2014]]) | relatar hectares | área mapeada ≠ área estimada; usar amostra probabilística independente |
| Validação de cobertura arbórea | acurácia + validação com LiDAR ([[Wagner_2023_MappingTropicalForest\|Wagner 2023]]) | referência independente | acurácia de 98 % é de cobertura, não de evento |

## Números de referência (para calibrar expectativas, não para comparar)
- DynamicEarthNet (Planet 3 m, 6–7 classes): melhor SCS de baseline 19,1; BC ≈ 10 % ([[Toker_2022_DynamicEarthNetDailyMulti|Toker 2022]]); com o modelo de [[Vincent_2024_SatelliteImageTime|Vincent 2024]], SCS 31,7 sem shift e 15,8 com shift espacial.
- SpaceNet 7 (Planet 4 m, edificações): F1 0,45, tracking 0,40, **mudança 0,06**, SCOT 0,17 ([[Etten_2021_MultiTemporalUrban|Etten 2021]]).
- SECOND (aéreo 512²): SeK 15,5–16,8 com ASN ([[Yang_2021_AsymmetricSiameseNetworks|Yang 2021]]).
- HRSCD (aéreo 0,5 m): kappa de mudança 25,5 com a melhor estratégia ([[Daudt_2019_MultitaskLearningLarge|Daudt 2019]]).
- Mineração PlanetScope: kappa > 0,92 em detecção direta, validado por amostra probabilística ([[ZarazaAguilera_2022_ChangeDetectionOver|ZarazaAguilera 2022]]).

## Regras para o projeto
1. Reportar **três blocos separados**: cobertura por mês, mudança (onde) e transições (para quê) — nunca misturados.
2. Evitar OA e κ como métricas principais; incluir PA/UA/F1 por classe e por transição.
3. Reportar **por faixa de tamanho** (≥ 4 px², 10–50 px², etc.) e por tipo de evento.
4. Incluir **erro de data** (mês de origem) e **falsos alertas por km²/mês**.
5. Estimar áreas com IC segundo [[Olofsson_2014_GoodPracticesEstimating|Olofsson 2014]].
6. Não comparar números entre benchmarks diferentes (resolução, classes, prevalência e divisão diferem).

[[00_Inicio|← Painel]]
