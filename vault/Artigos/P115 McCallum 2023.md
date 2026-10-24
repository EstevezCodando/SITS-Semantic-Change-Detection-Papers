---
tipo: artigo
id: P115
titulo: "Crowd-Driven Deep Learning Tracks Amazon Deforestation"
autores: "Ian McCallum, Jon Walker, Steffen Fritz, Markus Grau"
ano: 2023
secao: L
categoria: "Desmatamento e alertas"
tipo_publicacao: "Artigo"
papel: ["desmatamento/alerta"]
prioridade: baixa
doi: "10.3390/rs15215204"
pdf: "coleta/P115_McCallum2023_Crowd-Driven-Deep-Learning-Tracks-Amazon-Deforestation.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 32
sensores: ["[[Sentinel-2]]"]
tarefas: ["[[Desmatamento]]", "[[Degradação florestal]]"]
metodos: ["[[ResNet]]"]
datasets: ["[[PRODES]]", "[[Global Forest Change (Hansen)]]"]
metricas: []
ferramentas: []
etapas_pipeline: ["[[E06 Modelos-base de cobertura|E06]]", "[[E11 Operação e atualização|E11]]"]
status_leitura: não lido
tags: [artigo, secao/L, prioridade/baixa, etapa/E06, etapa/E11]
---

# P115 — Crowd-Driven Deep Learning Tracks Amazon Deforestation

**Ian McCallum, Jon Walker, Steffen Fritz** · 2023 · Artigo · Remote Sensing · [publicação](https://doi.org/10.3390/rs15215204) · [PDF](../../coleta/P115_McCallum2023_Crowd-Driven-Deep-Learning-Tracks-Amazon-Deforestation.pdf)

Seção: **Desmatamento e alertas** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Relevância:** Deep learning com participação coletiva (crowd) para rastrear desmatamento na Amazônia.
- **Receita de treino extraída:** taxa de aprendizado — `learning rate of 1 × 10−3, a batch size of 32, and an L2 regula`; batch size — `batch size of 32, and an L2 regularization paramet`; épocas — `30 epochs`; função de perda — `cross-entropy loss J as follows: J(Θ) = −1 N∑ N n=1[y` (confirmar nos chunks).
- **Dados/benchmarks citados:** [[PRODES]], [[Global Forest Change (Hansen)]]

## Limites e cuidados

- Conferir resolução, bandas, região e rótulos antes de transferir resultados; síntese baseada em registro e metadados.

## Contextos de uso no projeto

- Etapas do pipeline: [[E06 Modelos-base de cobertura|E06]], [[E11 Operação e atualização|E11]]
- Tarefas: [[Desmatamento]], [[Degradação florestal]]
- Sensores/produtos: [[Sentinel-2]]
- Métodos: [[ResNet]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Sentinel-2]] | 8 |
| dataset | [[PRODES]] | 13 |
| dataset | [[Global Forest Change (Hansen)]] | 2 |
| metodo | [[ResNet]] | 14 |
| tarefa | [[Desmatamento]] | 105 |
| tarefa | [[Degradação florestal]] | 16 |

## Resultados citados pelos autores (extraídos automaticamente)

> Training a suite of AI models with results from the crowd, we achieved an accuracy greater than 90% in detecting new and existing deforestation.
> This resulted in a spatial accuracy between the crowd and the PRODES and tree cover loss products of 92% and 89%, respectively (Supplementary Tables S1 and S2).
> The model’s accuracy was measured against a test set of 8774 images that had been labeled by the crowd but not previously seen by the model, achieving agreement with the crowd on 94.8% of the images.

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P115 chunks]] (32 chunks; resumo 3, introdução 5, dados 9, resultados 6, discussão 6, conclusão 3)
- Resumo: [[P115 chunks#^P115_c001|c001]], [[P115 chunks#^P115_c002|c002]]
- Dados / área de estudo: [[P115 chunks#^P115_c009|c009]], [[P115 chunks#^P115_c010|c010]]
- Hiperparâmetros / treino: [[P115 chunks#^P115_c016|c016]], [[P115 chunks#^P115_c017|c017]]
- Resultados numéricos: [[P115 chunks#^P115_c020|c020]], [[P115 chunks#^P115_c023|c023]]
- Limitações / discussão: [[P115 chunks#^P115_c024|c024]], [[P115 chunks#^P115_c025|c025]]

## Relações

- Vizinhos por entidades em comum: [[P118 Reiche 2024|P118]], [[P117 Doblas 2022|P117]], [[P120 Ygorra 2024|P120]], [[P119 Reiche 2021|P119]]

## Anotações

- 
