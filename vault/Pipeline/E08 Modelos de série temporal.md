---
tipo: pipeline
etapa: E08
tags: [pipeline, etapa/E08]
---
# E08 — Modelos de série temporal

**Objetivo:** Usar o histórico completo (TSSCD, U-TAE, BFAST/CCDC) para localizar quando e o que mudou.

**Entradas:** Cubo temporal  
**Saídas:** Mapa de mudança com data/intervalo e transição

**Anterior:** [[E07 Modelos de mudança em pares]] · **Próxima:** [[E09 Pós-processamento e eventos]]

## Como fazer (decisões da literatura e do documento original)

- Testar se o histórico mensal melhora a detecção em relação a pares de datas.
- Avaliar anos e áreas inéditos (domain shift), não só patches da mesma paisagem.
- Registrar intervalo de ocorrência, não dia exato inferido do nome do arquivo.

## Conceitos relacionados

[[Séries temporais de imagens]], [[Atenção temporal (U-TAE)]], [[BFAST]], [[CCDC]], [[LandTrendr]], [[LSTM-ConvLSTM|LSTM/ConvLSTM]]

## Artigos de apoio (20)

| Prioridade | Artigo | Título | O que aproveitar |
|---|---|---|---|
| alta | [[P10 Etten 2021\|P10 Etten 2021]] | The Multi-Temporal Urban Development SpaceNet Dataset | referência prioritária para novas construções e acompanhamento de objetos em resolução próxima à sua. |
| alta | [[P12 Toker 2022\|P12 Toker 2022]] | DynamicEarthNet: Daily Multi-Spectral Satellite Dataset for  | benchmark central para mudanças multiclasse, e não apenas edifícios. |
| alta | [[P13 Vincent 2024\|P13 Vincent 2024]] | Satellite Image Time Series Semantic Change Detection: Novel | fundamenta avaliar anos e áreas inéditos, em vez de apenas sortear patches da mesma paisagem. |
| alta | [[P14 He 2024\|P14 He 2024]] | Time-series land cover change detection using deep learning- | correspondência conceitual muito alta com o projeto. |
| alta | [[P18 Daudt 2019\|P18 Daudt 2019]] | Multitask Learning for Large-scale Semantic Change Detection | base para dois mapas semânticos e uma máscara de mudança coerentes entre si. |
| alta | [[P19 Yang 2021\|P19 Yang 2021]] | Asymmetric Siamese Networks for Semantic Change Detection in | organizar avaliação de transições semânticas. |
| média | [[P11 Etten 2021\|P11 Etten 2021]] | The SpaceNet Multi-Temporal Urban Development Challenge | consultar desenho da avaliação, associação entre meses e soluções reproduzíveis. |
| média | [[P15 Garnot 2021\|P15 Garnot 2021]] | Panoptic Segmentation of Satellite Image Time Series With Co | referência de encoder espaço-temporal para aproveitar várias observações. |
| média | [[P20 Zheng 2022\|P20 Zheng 2022]] | ChangeMask: Deep multi-task encoder-transformer-decoder arch | candidato a modelo conjunto para evitar divergência entre “mudou” e classes previstas. |
| média | [[P21 Ding 2022\|P21 Ding 2022]] | Bi-Temporal Semantic Reasoning for the Semantic Change Detec | reduzir inconsistências na interpretação das transições. |
| média | [[P41 Verbesselt 2010\|P41 Verbesselt 2010]] | Detecting trend and seasonal changes in satellite image time | baseline temporal para distinguir sazonalidade de mudança persistente. |
| média | [[P42 Zhu 2014\|P42 Zhu 2014]] | Continuous change detection and classification of land cover | referência para separar detecção do evento e atribuição da cobertura. |
| baixa | [[P16 Zhao 2025\|P16 Zhao 2025]] | HiSTENet: History-Integrated Spatial–Temporal Information Ex | candidato adicional para comparar histórico multitemporal com pares isolados. |
| baixa | [[P17 Metzger 2023\|P17 Metzger 2023]] | Urban Change Forecasting from Satellite Images | extensão futura para previsão de expansão, depois de validar mudanças observadas. |
| baixa | [[P22 Tang 2024\|P22 Tang 2024]] | The ClearSCD model: Comprehensively leveraging semantics and | avaliar transições com probabilidades, não apenas subtrair rótulos rígidos. |
| baixa | [[P43 Kennedy 2010\|P43 Kennedy 2010]] | Detecting trends in forest disturbance and recovery using ye | produto anual complementar e interpretação de regeneração. |
| baixa | [[P44 Pasquarella 2022\|P44 Pasquarella 2022]] | Demystifying LandTrendr and CCDC temporal segmentation | orientar escolha de frequência temporal e interpretação dos segmentos. |
| baixa | [[P126 Shafique 2022\|P126 Shafique 2022]] | Deep Learning-Based Change Detection in Remote Sensing Image | Revisão de detecção de mudanças por DL em sensoriamento remoto. |
| baixa | [[P127 Miller 2024\|P127 Miller 2024]] | Deep Learning for Satellite Image Time-Series Analysis: A re | Revisão de deep learning para séries temporais de imagens de satélite. |
| baixa | [[P146 Papadomanolaki 2019\|P146 Papadomanolaki 2019]] | Detecting Urban Changes with Recurrent Neural Networks from  | Mudança urbana com redes recorrentes em séries Sentinel-2 (OSCD). |

## Experimentos ligados


