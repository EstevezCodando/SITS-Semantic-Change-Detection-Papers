---
tipo: artigo
id: P51
titulo: "Machine Learning-Based Cerrado Land Cover Classification Using PlanetScope Imagery"
autores: "Thanan Rodrigues, Frederico Scherr Caldeira Takahashi, Arthur Dias, Taline Lima"
ano: 2025
secao: F
categoria: "XGBoost, LightGBM e atributos"
tipo_publicacao: "Artigo"
papel: ["baseline tabular (ML)"]
prioridade: média
doi: "10.3390/rs17030480"
pdf: ""
texto_integral: nao
fonte_analise: "apenas metadados e comentário (sem PDF)"
n_chunks: 0
sensores: ["[[PlanetScope]]"]
tarefas: []
metodos: ["[[XGBoost]]", "[[Random Forest]]", "[[SVM]]"]
datasets: []
metricas: ["[[F1]]"]
ferramentas: []
etapas_pipeline: ["[[E05 Atributos e representações|E05]]", "[[E06 Modelos-base de cobertura|E06]]"]
status_leitura: não lido
tags: [artigo, secao/F, prioridade/média, etapa/E05, etapa/E06]
---

# P51 — Machine Learning-Based Cerrado Land Cover Classification Using PlanetScope Imagery

**Thanan Rodrigues, Frederico Scherr Caldeira Takahashi, Arthur Dias** · 2025 · Artigo · Remote Sensing · [publicação](https://doi.org/10.3390/rs17030480) · PDF indisponível em coleta/

Seção: **XGBoost, LightGBM e atributos** · Prioridade: **média** · Análise: *apenas metadados e comentário (sem PDF)*

## O que reaproveitar

- **Uso proposto:** baseline prioritário de cobertura vegetal. É classificação, não validação de todas as transições mensais ou de edifícios. Não transportar a acurácia publicada para outra região.
- **Métricas usadas:** [[F1]]

## Método e dados (da revisão original)

- **Evidência direta:** compara **XGBoost, Random Forest e SVM em PlanetScope de 4,77 m** para classes de cobertura do Cerrado.
- **Resultado contextualizado:** tabela 5 apresenta F1 ponderado de 0,97 para XGBoost. Os testes entre classificadores apresentados não indicam diferenças significativas; não há suporte para afirmar superioridade geral do XGBoost.

## Limites e cuidados

- Conferir resolução, bandas, região e rótulos antes de transferir resultados; síntese baseada em registro e metadados.

## Contextos de uso no projeto

- Etapas do pipeline: [[E05 Atributos e representações|E05]], [[E06 Modelos-base de cobertura|E06]]
- Sensores/produtos: [[PlanetScope]]
- Métodos: [[XGBoost]], [[Random Forest]], [[SVM]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[PlanetScope]] | 2 |
| metodo | [[XGBoost]] | 3 |
| metodo | [[Random Forest]] | 1 |
| metodo | [[SVM]] | 1 |
| metrica | [[F1]] | 1 |

## Chunks

- Sem PDF em `coleta/` (acesso restrito ou bloqueado); chunking indisponível. Use o link da publicação.

## Relações

- Relação explícita: [[P52 Georganos 2018|P52]]
- Vizinhos por entidades em comum: [[P52 Georganos 2018|P52]], [[P07 Vizzari 2022|P07]], [[P06 Şimşek 2025|P06]], [[P97 Deigele 2020|P97]]

## Anotações

- 
