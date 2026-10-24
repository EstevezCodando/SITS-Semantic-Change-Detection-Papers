---
tipo: artigo
id: P32
titulo: "Prithvi-EO-2.0: A Versatile Multitemporal Foundation Model for Earth Observation Applications"
autores: "Daniela Szwarcman, Sujit Roy, Paolo Fraccaro, Þorsteinn Elí Gíslason"
ano: 2024
secao: C
categoria: "Detectores profundos e modelos fundacionais"
tipo_publicacao: "Preprint"
papel: ["baseline/método de mudança", "preprint"]
prioridade: baixa
doi: "10.48550/arXiv.2412.02732"
pdf: "coleta/P32_Szwarcman2025_Prithvi-EO-2-0-A-Versatile-Multitemporal-Foundation-Model-fo.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 70
sensores: ["[[Sentinel-2]]", "[[Sentinel-1-SAR|Sentinel-1/SAR]]", "[[Landsat]]"]
tarefas: ["[[Séries temporais de imagens]]", "[[Classificação de cobertura]]"]
metodos: ["[[Modelo fundacional]]", "[[Transfer learning]]", "[[U-Net]]", "[[Transformer]]", "[[ResNet]]", "[[Autoencoder mascarado (MAE)]]"]
datasets: ["[[PASTIS]]"]
metricas: ["[[IoU - mIoU|IoU / mIoU]]", "[[F1]]", "[[RMSE-MAE|RMSE/MAE]]", "[[Precisão-Recall|Precisão/Recall]]"]
ferramentas: ["[[Hugging Face]]"]
etapas_pipeline: ["[[E05 Atributos e representações|E05]]", "[[E06 Modelos-base de cobertura|E06]]", "[[E07 Modelos de mudança em pares|E07]]"]
status_leitura: não lido
tags: [artigo, secao/C, prioridade/baixa, etapa/E05, etapa/E06, etapa/E07]
---

# P32 — Prithvi-EO-2.0: A Versatile Multitemporal Foundation Model for Earth Observation Applications

**Daniela Szwarcman, Sujit Roy, Paolo Fraccaro** · 2024 · Preprint · IEEE Transactions on Geoscience and Remote Sensing · [publicação](https://arxiv.org/abs/2412.02732) · [PDF](../../coleta/P32_Szwarcman2025_Prithvi-EO-2-0-A-Versatile-Multitemporal-Foundation-Model-fo.pdf)

Seção: **Detectores profundos e modelos fundacionais** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Uso proposto:** backbone candidato, principalmente em experimentos que integrem outras fontes.
- **Código:** https://github.com/IBM/terratorch · https://github.com/IBM/terratorch-iterate · https://github.com/NASA-IMPACT/Prithvi-EO-2.0 · https://github.com/cloudtostreet/Sen1Floods11
- **Receita de treino extraída:** taxa de aprendizado — `learning rate of 5e-4 and linear warmup for 40 epochs starting `; batch size — `batch size (i`; épocas — `400 epochs`; otimizador — `Adam optimizer with a learning rate of 1e-5`; função de perda — `cross-entropy and the models ran for 50 epochs with e` (confirmar nos chunks).
- **Métricas usadas:** [[IoU - mIoU|IoU / mIoU]], [[F1]], [[RMSE-MAE|RMSE/MAE]], [[Precisão-Recall|Precisão/Recall]]
- **Dados/benchmarks citados:** [[PASTIS]]

## Método e dados (da revisão original)

- **Método:** modelo fundacional multitemporal para observação da Terra.

## Limites e cuidados

- não é detector Planet pronto. Conferir bandas, normalização, resolução e requisitos do checkpoint antes de ajustar.

## Contextos de uso no projeto

- Etapas do pipeline: [[E05 Atributos e representações|E05]], [[E06 Modelos-base de cobertura|E06]], [[E07 Modelos de mudança em pares|E07]]
- Tarefas: [[Séries temporais de imagens]], [[Classificação de cobertura]]
- Sensores/produtos: [[Sentinel-2]], [[Sentinel-1-SAR|Sentinel-1/SAR]], [[Landsat]]
- Métodos: [[Modelo fundacional]], [[Transfer learning]], [[U-Net]], [[Transformer]], [[ResNet]], [[Autoencoder mascarado (MAE)]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Sentinel-2]] | 41 |
| sensor | [[Sentinel-1-SAR\|Sentinel-1/SAR]] | 22 |
| sensor | [[Landsat]] | 7 |
| dataset | [[PASTIS]] | 5 |
| metodo | [[Modelo fundacional]] | 237 |
| metodo | [[Transfer learning]] | 37 |
| metodo | [[U-Net]] | 31 |
| metodo | [[Transformer]] | 31 |
| metodo | [[ResNet]] | 15 |
| metodo | [[Autoencoder mascarado (MAE)]] | 14 |
| metrica | [[IoU - mIoU\|IoU / mIoU]] | 45 |
| metrica | [[F1]] | 21 |
| metrica | [[RMSE-MAE\|RMSE/MAE]] | 18 |
| metrica | [[Precisão-Recall\|Precisão/Recall]] | 16 |
| tarefa | [[Séries temporais de imagens]] | 23 |
| tarefa | [[Classificação de cobertura]] | 17 |
| ferramenta | [[Hugging Face]] | 3 |

## Resultados citados pelos autores (extraídos automaticamente)

> Interestingly, although the mIoU is generally low for all models, they seem capable of distinguishing unburnt from burnt areas, with IoU0 above 67%.
> Prithvi-EO-2.0-600M achieves the higher IoU for class 0 (75.9%), representing a significant improvement over the U-Net models.
> Prithvi-EO-2.0600M, trained with weighted cross-entropy loss, exhibited a slightly lower mIoU of 70.4% and an F1 score of 58.6%, but achieved a higher recall than Prithvi-EO-2.0-300M.

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P32 chunks]] (70 chunks; resumo 3, introdução 5, trabalhos relacionados 3, métodos 37, resultados 21, conclusão 1)
- Resumo: [[P32 chunks#^P32_c001|c001]], [[P32 chunks#^P32_c002|c002]]
- Método: [[P32 chunks#^P32_c012|c012]], [[P32 chunks#^P32_c013|c013]], [[P32 chunks#^P32_c014|c014]]
- Hiperparâmetros / treino: [[P32 chunks#^P32_c009|c009]], [[P32 chunks#^P32_c010|c010]], [[P32 chunks#^P32_c011|c011]]
- Resultados numéricos: [[P32 chunks#^P32_c055|c055]], [[P32 chunks#^P32_c056|c056]], [[P32 chunks#^P32_c057|c057]]

## Relações

- Vizinhos por entidades em comum: [[P153 Xu 2024|P153]], [[P151 Lu 2025|P151]], [[P67 Xiong 2024|P67]], [[P127 Miller 2024|P127]]

## Anotações

- 
