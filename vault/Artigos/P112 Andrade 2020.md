---
tipo: artigo
id: P112
titulo: "EVALUATION OF SEMANTIC SEGMENTATION METHODS FOR DEFORESTATION DETECTION IN THE AMAZON"
autores: "R. B. Andrade, Gilson Alexandre Ostwald Pedro da Costa, Guilherme Lúcio Abelha Mota, Mabel X. Ortega"
ano: 2020
secao: L
categoria: "Desmatamento e alertas"
tipo_publicacao: "Artigo"
papel: ["desmatamento/alerta"]
prioridade: baixa
doi: "10.5194/isprs-archives-xliii-b3-2020-1497-2020"
pdf: "coleta/P112_Andrade2020_EVALUATION-OF-SEMANTIC-SEGMENTATION-METHODS-FOR-DEFORESTATIO.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 30
sensores: ["[[Imagens aéreas-VHR|Imagens aéreas/VHR]]", "[[Landsat]]"]
tarefas: ["[[Desmatamento]]"]
metodos: ["[[DeepLab]]", "[[Rede siamesa]]", "[[FCN]]", "[[U-Net]]", "[[SVM]]"]
datasets: ["[[PRODES]]", "[[DETER]]"]
metricas: ["[[F1]]", "[[Acurácia global]]"]
ferramentas: []
etapas_pipeline: ["[[E06 Modelos-base de cobertura|E06]]", "[[E07 Modelos de mudança em pares|E07]]", "[[E11 Operação e atualização|E11]]"]
status_leitura: não lido
tags: [artigo, secao/L, prioridade/baixa, etapa/E06, etapa/E07, etapa/E11]
---

# P112 — EVALUATION OF SEMANTIC SEGMENTATION METHODS FOR DEFORESTATION DETECTION IN THE AMAZON

**R. B. Andrade, Gilson Alexandre Ostwald Pedro da Costa, Guilherme Lúcio Abelha Mota** · 2020 · Artigo · The international archives of the photogrammetry, remote sensing and · [publicação](https://doi.org/10.5194/isprs-archives-xliii-b3-2020-1497-2020) · [PDF](../../coleta/P112_Andrade2020_EVALUATION-OF-SEMANTIC-SEGMENTATION-METHODS-FOR-DEFORESTATIO.pdf)

Seção: **Desmatamento e alertas** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Relevância:** Avaliação de métodos de segmentação semântica para desmatamento na Amazônia.
- **Receita de treino extraída:** taxa de aprendizado — `learning rate of 0.001 and weight decay of 0.9`; batch size — `batch size was set to 32`; épocas — `10 epochs`; otimizador — `Adam optimizer, with the learning rate of 0`; função de perda — `focal loss function (Lin et al` (confirmar nos chunks).
- **Métricas usadas:** [[F1]], [[Acurácia global]]
- **Dados/benchmarks citados:** [[PRODES]], [[DETER]]

## Limites e cuidados

- Conferir resolução, bandas, região e rótulos antes de transferir resultados; síntese baseada em registro e metadados.

## Contextos de uso no projeto

- Etapas do pipeline: [[E06 Modelos-base de cobertura|E06]], [[E07 Modelos de mudança em pares|E07]], [[E11 Operação e atualização|E11]]
- Tarefas: [[Desmatamento]]
- Sensores/produtos: [[Imagens aéreas-VHR|Imagens aéreas/VHR]], [[Landsat]]
- Métodos: [[DeepLab]], [[Rede siamesa]], [[FCN]], [[U-Net]], [[SVM]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Imagens aéreas-VHR\|Imagens aéreas/VHR]] | 5 |
| sensor | [[Landsat]] | 4 |
| dataset | [[PRODES]] | 4 |
| dataset | [[DETER]] | 3 |
| metodo | [[DeepLab]] | 32 |
| metodo | [[Rede siamesa]] | 15 |
| metodo | [[FCN]] | 7 |
| metodo | [[U-Net]] | 3 |
| metodo | [[SVM]] | 3 |
| metrica | [[F1]] | 6 |
| metrica | [[Acurácia global]] | 3 |
| tarefa | [[Desmatamento]] | 72 |

## Resultados citados pelos autores (extraídos automaticamente)

> In the best result for the F1-score using 4 tiles for training, 71.8%, was obtained with the DLCD model, using a weight of 0.1 for the no-deforestation class and a weight of 0.9 for the deforestation class, and a γ equal to 0 (DLC
> In terms of Overall Accuracy, the best result, when using 4 tiles for training, was obtained using weight of 0.5 for both deforestation and no-deforestation classes, with γ equal to 1 (DLCD-3), with a score of 98.8%.

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P112 chunks]] (30 chunks; resumo 2, introdução 5, trabalhos relacionados 18, resultados 3, conclusão 2)
- Resumo: [[P112 chunks#^P112_c001|c001]], [[P112 chunks#^P112_c002|c002]]
- Hiperparâmetros / treino: [[P112 chunks#^P112_c017|c017]], [[P112 chunks#^P112_c018|c018]], [[P112 chunks#^P112_c020|c020]]
- Resultados numéricos: [[P112 chunks#^P112_c026|c026]], [[P112 chunks#^P112_c027|c027]]

## Relações

- Vizinhos por entidades em comum: [[P23 Daudt 2018|P23]], [[P113 Jelas 2024|P113]], [[P01 Wagner 2023|P01]], [[P126 Shafique 2022|P126]]

## Anotações

- 
