---
tipo: artigo
id: P03
titulo: "Detection of forest disturbance across California using deep-learning on PlanetScope imagery"
autores: "Griffin Carter, Fabien Hubert Wagner, Ricardo Dalagnol, Sophia Roberts"
ano: 2024
secao: A
categoria: "Planet: aplicações diretas"
tipo_publicacao: "Artigo"
papel: ["aplicação Planet"]
prioridade: média
doi: "10.3389/frsen.2024.1409400"
pdf: "coleta/P03_Carter2024_Detection-of-forest-disturbance-across-California-using-deep.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 45
sensores: ["[[PlanetScope]]", "[[Planet (mosaicos e cenas)]]", "[[Planet NICFI]]"]
tarefas: ["[[Desmatamento]]", "[[Degradação florestal]]"]
metodos: ["[[U-Net]]", "[[Semi-auto-supervisionado|Semi/auto-supervisionado]]"]
datasets: ["[[Global Forest Change (Hansen)]]"]
metricas: ["[[Precisão-Recall|Precisão/Recall]]", "[[F1]]", "[[Acurácia global]]", "[[Estimativa de área - IC|Estimativa de área / IC]]"]
ferramentas: ["[[TensorFlow]]"]
etapas_pipeline: ["[[E06 Modelos-base de cobertura|E06]]"]
status_leitura: não lido
tags: [artigo, secao/A, prioridade/média, etapa/E06]
---

# P03 — Detection of forest disturbance across California using deep-learning on PlanetScope imagery

**Griffin Carter, Fabien Hubert Wagner, Ricardo Dalagnol** · 2024 · Artigo · Frontiers in Remote Sensing · [publicação](https://doi.org/10.3389/frsen.2024.1409400) · [PDF](../../coleta/P03_Carter2024_Detection-of-forest-disturbance-across-California-using-deep.pdf)

Seção: **Planet: aplicações diretas** · Prioridade: **média** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Uso proposto:** especialmente relevante se seus mosaicos forem RGB, sem NIR.
- **Receita de treino extraída:** taxa de aprendizado — `learning rate of 0.0001`; batch size — `batch size of 256 images and the model with the be`; épocas — `25,000 epochs`; otimizador — `Adam optimizer with a learning rate of 0`; função de perda — `binary cross-entropy and Dice coefficient-related lo` (confirmar nos chunks).
- **Métricas usadas:** [[Precisão-Recall|Precisão/Recall]], [[F1]], [[Acurácia global]], [[Estimativa de área - IC|Estimativa de área / IC]]
- **Dados/benchmarks citados:** [[Global Forest Change (Hansen)]]

## Método e dados (da revisão original)

- **Método/dados:** U-Net, mosaicos visuais RGB a 4,77 m, mapas mensais de 2020–2022 e pós-processamento temporal.

## Limites e cuidados

- contexto florestal e climático diferente. O artigo apresenta avaliações distintas de cobertura e perturbação; não confundir a acurácia da cobertura com a precisão de eventos de mudança.

## Contextos de uso no projeto

- Etapas do pipeline: [[E06 Modelos-base de cobertura|E06]]
- Tarefas: [[Desmatamento]], [[Degradação florestal]]
- Sensores/produtos: [[PlanetScope]], [[Planet (mosaicos e cenas)]], [[Planet NICFI]]
- Métodos: [[U-Net]], [[Semi-auto-supervisionado|Semi/auto-supervisionado]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[PlanetScope]] | 16 |
| sensor | [[Planet (mosaicos e cenas)]] | 12 |
| sensor | [[Planet NICFI]] | 3 |
| dataset | [[Global Forest Change (Hansen)]] | 4 |
| metodo | [[U-Net]] | 22 |
| metodo | [[Semi-auto-supervisionado\|Semi/auto-supervisionado]] | 4 |
| metrica | [[Precisão-Recall\|Precisão/Recall]] | 8 |
| metrica | [[F1]] | 3 |
| metrica | [[Acurácia global]] | 3 |
| metrica | [[Estimativa de área - IC\|Estimativa de área / IC]] | 3 |
| tarefa | [[Desmatamento]] | 56 |
| tarefa | [[Degradação florestal]] | 15 |
| ferramenta | [[TensorFlow]] | 2 |

## Resultados citados pelos autores (extraídos automaticamente)

> We then detected changes of tree cover and disturbance with the U-Net model, achieving an overall accuracy of 98.97% over training data set, and 95.5% over an independent validation dataset, obtaining a precision of 82%, and a rec
> Our individual predictions showed promising results with a validation accuracy of 95.02% and an independent validation of 77.77% at 4.77 m spatial resolution when forests are defined with a height greater than 5 m based on airborn
> We then filtered the monthly maps to create annual forest cover maps which had an overall accuracy of 82%.

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P03 chunks]] (45 chunks; resumo 3, introdução 5, dados 3, métodos 6, experimentos 15, resultados 11, conclusão 2)
- Resumo: [[P03 chunks#^P03_c001|c001]], [[P03 chunks#^P03_c002|c002]]
- Dados / área de estudo: [[P03 chunks#^P03_c009|c009]], [[P03 chunks#^P03_c010|c010]]
- Método: [[P03 chunks#^P03_c012|c012]], [[P03 chunks#^P03_c033|c033]], [[P03 chunks#^P03_c034|c034]]
- Hiperparâmetros / treino: [[P03 chunks#^P03_c010|c010]], [[P03 chunks#^P03_c012|c012]], [[P03 chunks#^P03_c013|c013]]
- Resultados numéricos: [[P03 chunks#^P03_c016|c016]], [[P03 chunks#^P03_c024|c024]], [[P03 chunks#^P03_c025|c025]]

## Relações

- Vizinhos por entidades em comum: [[P02 Dalagnol 2023|P02]], [[P04 Wang 2024|P04]], [[P01 Wagner 2023|P01]], [[P93 Wagner 2025|P93]]

## Anotações

- 
