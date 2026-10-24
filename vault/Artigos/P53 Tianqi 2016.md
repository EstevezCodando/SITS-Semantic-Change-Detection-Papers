---
tipo: artigo
id: P53
titulo: "XGBoost: A Scalable Tree Boosting System"
autores: "Chen, Tianqi, Carlos Guestrin"
ano: 2016
secao: F
categoria: "XGBoost, LightGBM e atributos"
tipo_publicacao: "Artigo"
papel: ["baseline tabular (ML)"]
prioridade: baixa
doi: "10.48550/arXiv.1603.02754"
pdf: "coleta/P53_Tianqi2016_XGBoost-A-Scalable-Tree-Boosting-System.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 38
sensores: ["[[Planet (mosaicos e cenas)]]"]
tarefas: []
metodos: ["[[XGBoost]]"]
datasets: []
metricas: ["[[AUC]]"]
ferramentas: ["[[scikit-learn]]"]
etapas_pipeline: ["[[E05 Atributos e representações|E05]]", "[[E06 Modelos-base de cobertura|E06]]"]
status_leitura: não lido
tags: [artigo, secao/F, prioridade/baixa, etapa/E05, etapa/E06]
---

# P53 — XGBoost: A Scalable Tree Boosting System

**Chen, Tianqi, Carlos Guestrin** · 2016 · Artigo · arXiv (Cornell University) · [publicação](https://arxiv.org/abs/1603.02754) · [PDF](../../coleta/P53_Tianqi2016_XGBoost-A-Scalable-Tree-Boosting-System.pdf)

Seção: **XGBoost, LightGBM e atributos** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Uso proposto:** fundamentar implementação e processamento de uma tabela de atributos por pixel, objeto ou trajetória.
- **Código:** https://github.com/dmlc/rabit · https://github.com/dmlc/xgboost
- **Receita de treino extraída:** taxa de aprendizado — `learning rate in tochastic optimization, shrinkage reduces the ` (confirmar nos chunks).
- **Métricas usadas:** [[AUC]]

## Método e dados (da revisão original)

- **Contribuição:** artigo do sistema de gradient boosting escalável.

## Limites e cuidados

- referência geral de ML; não é um estudo de sensoriamento remoto e não comprova qualidade de classificação Planet.

## Contextos de uso no projeto

- Etapas do pipeline: [[E05 Atributos e representações|E05]], [[E06 Modelos-base de cobertura|E06]]
- Sensores/produtos: [[Planet (mosaicos e cenas)]]
- Métodos: [[XGBoost]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Planet (mosaicos e cenas)]] | 1 |
| metodo | [[XGBoost]] | 50 |
| metrica | [[AUC]] | 3 |
| ferramenta | [[scikit-learn]] | 11 |

## Chunks

- Arquivo de chunks: [[P53 chunks]] (38 chunks; resumo 2, introdução 5, trabalhos relacionados 30, conclusão 1)
- Resumo: [[P53 chunks#^P53_c001|c001]], [[P53 chunks#^P53_c002|c002]]
- Hiperparâmetros / treino: [[P53 chunks#^P53_c012|c012]]

## Relações

- Vizinhos por entidades em comum: [[P68 Ferreira 2020|P68]], [[P54 Gündüz 2026|P54]], [[P89 Kimm 2020|P89]], [[P81 Frazier 2021|P81]]

## Anotações

- 
