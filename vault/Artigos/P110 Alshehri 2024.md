---
tipo: artigo
id: P110
titulo: "Deep Transformer-Based Network Deforestation Detection in the Brazilian Amazon Using Sentinel-2 Imagery"
autores: "Mariam Alshehri, Anes Ouadou, Grant J. Scott"
ano: 2024
secao: L
categoria: "Desmatamento e alertas"
tipo_publicacao: "Artigo"
papel: ["desmatamento/alerta"]
prioridade: baixa
doi: "10.1109/lgrs.2024.3355104"
pdf: "coleta/P110_Alshehri2024_Deep-Transformer-Based-Network-Deforestation-Detection-in-th.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 20
sensores: ["[[Sentinel-2]]", "[[Landsat]]"]
tarefas: ["[[Desmatamento]]"]
metodos: ["[[Transformer]]", "[[NDVI-índices|NDVI/índices]]"]
datasets: ["[[PRODES]]"]
metricas: ["[[IoU - mIoU|IoU / mIoU]]", "[[F1]]", "[[Precisão-Recall|Precisão/Recall]]", "[[Acurácia global]]"]
ferramentas: []
etapas_pipeline: ["[[E06 Modelos-base de cobertura|E06]]", "[[E11 Operação e atualização|E11]]"]
status_leitura: não lido
tags: [artigo, secao/L, prioridade/baixa, etapa/E06, etapa/E11]
---

# P110 — Deep Transformer-Based Network Deforestation Detection in the Brazilian Amazon Using Sentinel-2 Imagery

**Mariam Alshehri, Anes Ouadou, Grant J. Scott** · 2024 · Artigo · IEEE Geoscience and Remote Sensing Letters · [publicação](https://doi.org/10.1109/lgrs.2024.3355104) · [PDF](../../coleta/P110_Alshehri2024_Deep-Transformer-Based-Network-Deforestation-Detection-in-th.pdf)

Seção: **Desmatamento e alertas** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Relevância:** Rede baseada em transformers para desmatamento na Amazônia com Sentinel-2.
- **Receita de treino extraída:** taxa de aprendizado — `learning rates 0.01 - 0.0001 Loss functions Cross-Entropy (CE), I`; épocas — `200 epochs`; otimizador — `SGD, Adam, AdamW learning rates 0`; função de perda — `cross-entropy loss with AdamW optimizer resulted in t`; tamanho do patch — `256×256 pixel` (confirmar nos chunks).
- **Métricas usadas:** [[IoU - mIoU|IoU / mIoU]], [[F1]], [[Precisão-Recall|Precisão/Recall]], [[Acurácia global]]
- **Dados/benchmarks citados:** [[PRODES]]

## Limites e cuidados

- Conferir resolução, bandas, região e rótulos antes de transferir resultados; síntese baseada em registro e metadados.

## Contextos de uso no projeto

- Etapas do pipeline: [[E06 Modelos-base de cobertura|E06]], [[E11 Operação e atualização|E11]]
- Tarefas: [[Desmatamento]]
- Sensores/produtos: [[Sentinel-2]], [[Landsat]]
- Métodos: [[Transformer]], [[NDVI-índices|NDVI/índices]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Sentinel-2]] | 10 |
| sensor | [[Landsat]] | 3 |
| dataset | [[PRODES]] | 5 |
| metodo | [[Transformer]] | 18 |
| metodo | [[NDVI-índices\|NDVI/índices]] | 3 |
| metrica | [[IoU - mIoU\|IoU / mIoU]] | 13 |
| metrica | [[F1]] | 8 |
| metrica | [[Precisão-Recall\|Precisão/Recall]] | 8 |
| metrica | [[Acurácia global]] | 6 |
| tarefa | [[Desmatamento]] | 26 |

## Resultados citados pelos autores (extraídos automaticamente)

> The model achieved an overall accuracy of 93% with corresponding F1 score of 90% and IoU score of 82%.
> For more information, see https://creativecommons.org/licenses/by/4.0/ TABLE III TOP FIVE SCORING HYPERPARAMETER CONFIGURATIONS FOR 256 × 256 (TOP) AND 512 × 512 (BOTTOM) CHIP SIZES chip size optimizer loss lr OA mIoU mF1 IoU-1 F1
> However, the ChangeFormer model obtained at least 80.9% F1-score for the change class (F1-1) across both chip sizes.

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P110 chunks]] (20 chunks; resumo 1, introdução 5, métodos 1, dados 7, experimentos 2, resultados 3, conclusão 1)
- Resumo: [[P110 chunks#^P110_c001|c001]]
- Dados / área de estudo: [[P110 chunks#^P110_c008|c008]], [[P110 chunks#^P110_c009|c009]]
- Método: [[P110 chunks#^P110_c007|c007]]
- Hiperparâmetros / treino: [[P110 chunks#^P110_c001|c001]], [[P110 chunks#^P110_c013|c013]], [[P110 chunks#^P110_c014|c014]]
- Resultados numéricos: [[P110 chunks#^P110_c016|c016]], [[P110 chunks#^P110_c018|c018]], [[P110 chunks#^P110_c019|c019]]

## Relações

- Vizinhos por entidades em comum: [[P115 McCallum 2023|P115]], [[P109 Torres 2021|P109]], [[P108 Bem 2020|P108]], [[P88 Aragon 2021|P88]]

## Anotações

- 
