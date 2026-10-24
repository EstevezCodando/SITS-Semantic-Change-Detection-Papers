---
tipo: artigo
id: P15
titulo: "Panoptic Segmentation of Satellite Image Time Series With Convolutional Temporal Attention Networks"
autores: "Vivien Sainte Fare Garnot, Loïc Landrieu"
ano: 2021
secao: B
categoria: "Séries temporais, edificações e transições semânticas"
tipo_publicacao: "Artigo"
papel: ["benchmark/método temporal"]
prioridade: média
doi: "10.1109/iccv48922.2021.00483"
pdf: "coleta/P15_Garnot2021_Panoptic-Segmentation-of-Satellite-Image-Time-Series-With-Co.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 33
sensores: ["[[Sentinel-2]]"]
tarefas: ["[[Séries temporais de imagens]]", "[[Segmentação semântica]]"]
metodos: ["[[LSTM-ConvLSTM|LSTM/ConvLSTM]]", "[[Atenção temporal (U-TAE)]]", "[[U-Net]]"]
datasets: ["[[PASTIS]]"]
metricas: ["[[IoU - mIoU|IoU / mIoU]]", "[[Acurácia global]]"]
ferramentas: []
etapas_pipeline: ["[[E07 Modelos de mudança em pares|E07]]", "[[E08 Modelos de série temporal|E08]]"]
status_leitura: não lido
tags: [artigo, secao/B, prioridade/média, etapa/E07, etapa/E08]
---

# P15 — Panoptic Segmentation of Satellite Image Time Series With Convolutional Temporal Attention Networks

**Vivien Sainte Fare Garnot, Loïc Landrieu** · 2021 · Artigo · IEEE · [publicação](https://openaccess.thecvf.com/content/ICCV2021/papers/Garnot_Panoptic_Segmentation_of_Satellite_Image_Time_Series_With_Convolutional_Temporal_ICCV_2021_paper.pdf) · [PDF](../../coleta/P15_Garnot2021_Panoptic-Segmentation-of-Satellite-Image-Time-Series-With-Co.pdf)

Seção: **Séries temporais, edificações e transições semânticas** · Prioridade: **média** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Uso proposto:** referência de encoder espaço-temporal para aproveitar várias observações.
- **Código:** https://github.com/VSainteuf/utae-paps
- **Receita de treino extraída:** função de perda — `cross-entropy loss, and the size prediction with a no` (confirmar nos chunks).
- **Métricas usadas:** [[IoU - mIoU|IoU / mIoU]], [[Acurácia global]]
- **Dados/benchmarks citados:** [[PASTIS]]

## Método e dados (da revisão original)

- **Método/dados:** U-TAE, PaPs e PASTIS; atenção temporal em séries Sentinel-2.

## Limites e cuidados

- segmentação agrícola/panóptica não é um detector pronto de supressão e construção; exige adaptação da tarefa e dos rótulos.

## Contextos de uso no projeto

- Etapas do pipeline: [[E07 Modelos de mudança em pares|E07]], [[E08 Modelos de série temporal|E08]]
- Tarefas: [[Séries temporais de imagens]], [[Segmentação semântica]]
- Sensores/produtos: [[Sentinel-2]]
- Métodos: [[LSTM-ConvLSTM|LSTM/ConvLSTM]], [[Atenção temporal (U-TAE)]], [[U-Net]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Sentinel-2]] | 1 |
| dataset | [[PASTIS]] | 7 |
| metodo | [[LSTM-ConvLSTM\|LSTM/ConvLSTM]] | 20 |
| metodo | [[Atenção temporal (U-TAE)]] | 17 |
| metodo | [[U-Net]] | 12 |
| metrica | [[IoU - mIoU\|IoU / mIoU]] | 6 |
| metrica | [[Acurácia global]] | 3 |
| tarefa | [[Séries temporais de imagens]] | 12 |
| tarefa | [[Segmentação semântica]] | 10 |

## Chunks

- Arquivo de chunks: [[P15 chunks]] (33 chunks; resumo 2, introdução 4, trabalhos relacionados 3, métodos 15, dados 8, conclusão 1)
- Resumo: [[P15 chunks#^P15_c001|c001]], [[P15 chunks#^P15_c002|c002]]
- Dados / área de estudo: [[P15 chunks#^P15_c025|c025]], [[P15 chunks#^P15_c026|c026]]
- Método: [[P15 chunks#^P15_c010|c010]], [[P15 chunks#^P15_c011|c011]], [[P15 chunks#^P15_c012|c012]]
- Hiperparâmetros / treino: [[P15 chunks#^P15_c021|c021]], [[P15 chunks#^P15_c022|c022]], [[P15 chunks#^P15_c027|c027]]

## Relações

- Vizinhos por entidades em comum: [[P127 Miller 2024|P127]], [[P12 Toker 2022|P12]], [[P146 Papadomanolaki 2019|P146]], [[P32 Szwarcman 2024|P32]]

## Anotações

- 
