# Mapa do conhecimento para este projeto

Caminhos relativos a `Pratice/`. Abra `..\base_conhecimento` no Obsidian ou leia os `.md` diretamente. A trilha completa (fluxo, tabela de resultados, proposta e lacunas) está em `..\base_conhecimento\01_Mapas\Trilha_Objetivo_Planet5m.md`.

## Por etapa do pipeline

| Etapa | Leia primeiro | O que traz |
|---|---|---|
| Dados e cadência | `02_Artigos\Zhang_2023_MonitoringMonthlyTropical.md`, `02_Artigos\Glazer_2025_TEMPOGlobalTemporal.md` | NICFI mensal de 5 m (p. 6–7); UDM, mudança de processamento da Planet em 2022 e deslocamento de distribuição (p. 2–3) |
| QC e nuvem | `Zhang_2023`, `Glazer_2025` (p. 7–8) | máscara de nuvem por floresta aleatória e HOT; clareza do pixel em níveis |
| Rótulos | `02_Artigos\Masolele_2024_MappingDiversityLand.md`, `04_Preparo\AprendizadoAtivo.md`, `07_Resultados\Sintese_Rotulagem.md`, `04_Preparo\RotulagemTemporal.md` | aprendizado ativo por entropia (F1 43% → 84% em dois ciclos); rótulos sequenciais com mês de início |
| Baselines | `Zhang_2023` (p. 9–13) | Hue referenciado à vizinhança e persistência de 3 meses, sem treinar |
| Modelos | `Wang_2024_ValidationDeforestationHigh.md`, `Wagner_2023_MappingTropicalForest.md`, `Metzger_2023_UrbanChangeForecasting.md`, `Vincent_2024_SatelliteImageTime.md`, `Etten_2021_SpaceNetMultiTemporal.md` | U-Net bitemporal e por data; pré-treino em mudança; U-TAE; desafio SpaceNet 7 |
| Pós-processamento | `Etten_2021_SpaceNetMultiTemporal` (p. 8–9), `Glazer_2025` (p. 7–8), `Zhang_2023` (p. 13), `05_Metodos\PosProcessamentoTemporal.md` | colapso temporal, janela de 4 datas, persistência |
| Validação | `06_Validacao\DivisaoEspacialBlocos.md`, `Olofsson_2014_GoodPracticesEstimating.md`, `Vincent_2024`, `07_Resultados\Sintese_Particoes.md`, `Sintese_Metricas.md` | blocos com folga; três regimes de shift; estimativa de área com intervalo; métricas de mudança |
| Confiança e operação | `Reiche_2024_IntegratingSatelliteForest.md`, `Reiche_2021_ForestDisturbanceAlerts.md`, `Ygorra_2024_NearRealTime.md`, `08_Monitoramento\PersistenciaConfirmacao.md` | classes de confiança por concordância, atualização bayesiana, latência |
| Lacunas | `09_Lacunas\00_Sintese_Lacunas.md` | L01 a L14, com evidência e oportunidade |

## Sínteses práticas herdadas

- `07_Resultados\Sintese_Receitas.md` e `Sintese_Decisoes.md`: receitas de pipeline e decisões de projeto da primeira rodada de leitura.
- `07_Resultados\Sintese_Planet.md`: o que se sabe sobre produtos Planet.
- `07_Resultados\Matriz_Comparativa.md`: uma linha por estudo (dados, método, validação, métricas, limitações). **Não ordena modelos.**

## Resultados mais próximos do objetivo (valores relatados em cada estudo)

| Estudo | Dado | Alvo | Resultado relatado | Força da validação (nossa leitura) |
|---|---|---|---|---|
| Zhang 2023 | NICFI mensal 5 m | perda de dossel | usuário 84,7 ± 2,9%; produtor 61,5 ± 46,4% | alta; omissão incerta |
| Etten 2021 | SpaceNet 7, ~4 m | construção | campeão: mudança 0,20; SCOT 0,41 | média |
| Wang 2024 | par NICFI | confirmação de supressão | F1 0,825 (U-Net) vs 0,55 (RF) | baixa (divisão aleatória) |
| Masolele 2024 | NICFI 5 m | uso após desmatamento | F1 84 ± 0,7% | média |
| Glazer 2025 | basemaps 4,7 m | edificações | F1 de presença 0,85–0,88 | média (não mede mudança) |

Ficha por estudo: `..\dados\leitura_profunda\Pxx.md` (com página para cada afirmação). O texto integral convertido de cada artigo está em `..\output\pdf\`.

## O que a base **não** sabe

- Se esses métodos funcionam em **RGB visual de 8 bits** sem NIR (os estudos usam 4 bandas analíticas ou RGB em outros produtos).
- O desempenho em uma AOI peri-urbana do litoral do RJ.
- Como a confiança se comporta com **calibração**: nenhum estudo lido calibra a confiança de polígonos por regressão (a proposta aqui é nossa).
- O custo real de rotulagem de eventos com mês de início para esta área.

Registre cada resposta que o projeto obtiver em `runs/` e, quando fizer sentido, em uma nota nova na base de conhecimento (com página ou número do experimento).
