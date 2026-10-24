---
tipo: artigo
id: P184
titulo: "Prediction and Simulation of Land Use and Land Cover Changes Using Open Source QGIS. A Case Study of Purwokerto, Central Java, Indonesia"
autores: "Gian Felix Ramadan, Iswari Nur Hidayati"
ano: 2022
secao: N
categoria: "GeoAI e QGIS"
tipo_publicacao: "Artigo"
papel: ["GeoAI/QGIS"]
prioridade: baixa
doi: "10.22146/ijg.68702"
pdf: "coleta/P184_Ramadan2022_Prediction-and-Simulation-of-Land-Use-and-Land-Cover-Changes.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 23
sensores: ["[[Landsat]]"]
tarefas: ["[[Classificação de cobertura]]", "[[Vias-estradas|Vias/estradas]]"]
metodos: []
datasets: []
metricas: ["[[Kappa]]"]
ferramentas: ["[[MOLUSCE]]", "[[QGIS]]"]
etapas_pipeline: ["[[E11 Operação e atualização|E11]]"]
status_leitura: não lido
tags: [artigo, secao/N, prioridade/baixa, etapa/E11]
---

# P184 — Prediction and Simulation of Land Use and Land Cover Changes Using Open Source QGIS. A Case Study of Purwokerto, Central Java, Indonesia

**Gian Felix Ramadan, Iswari Nur Hidayati** · 2022 · Artigo · Indonesian Journal of Geography · [publicação](https://doi.org/10.22146/ijg.68702) · [PDF](../../coleta/P184_Ramadan2022_Prediction-and-Simulation-of-Land-Use-and-Land-Cover-Changes.pdf)

Seção: **GeoAI e QGIS** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Relevância:** Previsão e simulação de mudança de uso/cobertura com QGIS de código aberto.
- **Receita de treino extraída:** taxa de aprendizado — `learning rate, and the neighborhood` (confirmar nos chunks).
- **Métricas usadas:** [[Kappa]]

## Limites e cuidados

- Conferir resolução, bandas, região e rótulos antes de transferir resultados; síntese baseada em registro e metadados.

## Contextos de uso no projeto

- Etapas do pipeline: [[E11 Operação e atualização|E11]]
- Tarefas: [[Classificação de cobertura]], [[Vias-estradas|Vias/estradas]]
- Sensores/produtos: [[Landsat]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Landsat]] | 14 |
| metrica | [[Kappa]] | 9 |
| tarefa | [[Classificação de cobertura]] | 104 |
| tarefa | [[Vias-estradas\|Vias/estradas]] | 18 |
| ferramenta | [[MOLUSCE]] | 10 |
| ferramenta | [[QGIS]] | 4 |

## Resultados citados pelos autores (extraídos automaticamente)

> The LULC classifications for 2008, 2013, and 2018 were 88%, 86%, and 88% accurate, while the prediction was 75.26% accurate, with a kappa of 0.634.
> In the current study, this technique employed the maximum likelihood algorithm, producing five LULC classes for 2008, 2013, and 2018 data with 88%, 86%, and 88% accuracy.
> With these rates, the classification results meet the minimum requirement for accuracy, 85 % (Anderson, 1971).

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P184 chunks]] (23 chunks; resumo 2, introdução 4, métodos 6, resultados 10, conclusão 1)
- Resumo: [[P184 chunks#^P184_c001|c001]], [[P184 chunks#^P184_c002|c002]]
- Método: [[P184 chunks#^P184_c007|c007]], [[P184 chunks#^P184_c008|c008]], [[P184 chunks#^P184_c009|c009]]
- Hiperparâmetros / treino: [[P184 chunks#^P184_c020|c020]]
- Resultados numéricos: [[P184 chunks#^P184_c013|c013]], [[P184 chunks#^P184_c014|c014]], [[P184 chunks#^P184_c020|c020]]

## Relações

- Vizinhos por entidades em comum: [[P55 Magidi 2024|P55]], [[P159 Cubillas 2024|P159]], [[P91 Zhang 2023|P91]], [[P47 Stehman 2019|P47]]

## Anotações

- 
