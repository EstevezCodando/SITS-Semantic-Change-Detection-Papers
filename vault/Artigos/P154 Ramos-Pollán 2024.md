---
tipo: artigo
id: P154
titulo: "Uncertainty and Generalizability in Foundation Models for Earth Observation"
autores: "Raúl Ramos-Pollán, Freddie Kalaitzis, Karthick Panner Selvam"
ano: 2024
secao: M
categoria: "Detecção de mudanças: métodos adicionais"
tipo_publicacao: "Preprint"
papel: ["método de mudança", "preprint"]
prioridade: baixa
doi: "10.48550/arXiv.2409.08744"
pdf: "coleta/P154_Ramos-Pollan2024_Uncertainty-and-Generalizability-in-Foundation-Models-for-Ea.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 22
sensores: ["[[Sentinel-1-SAR|Sentinel-1/SAR]]", "[[Sentinel-2]]"]
tarefas: ["[[Anotação-rotulagem|Anotação/rotulagem]]"]
metodos: ["[[Transformer]]", "[[Autoencoder mascarado (MAE)]]", "[[CLIP - visão-linguagem|CLIP / visão-linguagem]]"]
datasets: []
metricas: ["[[RMSE-MAE|RMSE/MAE]]", "[[Estimativa de área - IC|Estimativa de área / IC]]"]
ferramentas: []
etapas_pipeline: ["[[E07 Modelos de mudança em pares|E07]]"]
status_leitura: não lido
tags: [artigo, secao/M, prioridade/baixa, etapa/E07]
---

# P154 — Uncertainty and Generalizability in Foundation Models for Earth Observation

**Raúl Ramos-Pollán, Freddie Kalaitzis, Karthick Panner Selvam** · 2024 · Preprint · arXiv (Cornell University) · [publicação](https://doi.org/10.48550/arXiv.2409.08744) · [PDF](../../coleta/P154_Ramos-Pollan2024_Uncertainty-and-Generalizability-in-Foundation-Models-for-Ea.pdf)

Seção: **Detecção de mudanças: métodos adicionais** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Relevância:** Incerteza e generalização em modelos fundacionais para observação da Terra.
- **Código:** http://github.com/rramosp/geetiles · https://github.com/Clay-foundation/model
- **Receita de treino extraída:** tamanho do patch — `512 × 512 pixel` (confirmar nos chunks).
- **Métricas usadas:** [[RMSE-MAE|RMSE/MAE]], [[Estimativa de área - IC|Estimativa de área / IC]]

## Limites e cuidados

- Conferir resolução, bandas, região e rótulos antes de transferir resultados; síntese baseada em registro e metadados.

## Contextos de uso no projeto

- Etapas do pipeline: [[E07 Modelos de mudança em pares|E07]]
- Tarefas: [[Anotação-rotulagem|Anotação/rotulagem]]
- Sensores/produtos: [[Sentinel-1-SAR|Sentinel-1/SAR]], [[Sentinel-2]]
- Métodos: [[Transformer]], [[Autoencoder mascarado (MAE)]], [[CLIP - visão-linguagem|CLIP / visão-linguagem]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Sentinel-1-SAR\|Sentinel-1/SAR]] | 7 |
| sensor | [[Sentinel-2]] | 6 |
| metodo | [[Transformer]] | 10 |
| metodo | [[Autoencoder mascarado (MAE)]] | 7 |
| metodo | [[CLIP - visão-linguagem\|CLIP / visão-linguagem]] | 3 |
| metrica | [[RMSE-MAE\|RMSE/MAE]] | 9 |
| metrica | [[Estimativa de área - IC\|Estimativa de área / IC]] | 4 |
| tarefa | [[Anotação-rotulagem\|Anotação/rotulagem]] | 12 |

## Chunks

- Arquivo de chunks: [[P154 chunks]] (22 chunks; resumo 3, introdução 7, métodos 4, resultados 6, conclusão 2)
- Resumo: [[P154 chunks#^P154_c001|c001]], [[P154 chunks#^P154_c002|c002]]
- Método: [[P154 chunks#^P154_c011|c011]], [[P154 chunks#^P154_c012|c012]], [[P154 chunks#^P154_c013|c013]]
- Hiperparâmetros / treino: [[P154 chunks#^P154_c009|c009]]

## Relações

- Vizinhos por entidades em comum: [[P67 Xiong 2024|P67]], [[P62 Carion 2025|P62]], [[P32 Szwarcman 2024|P32]], [[P151 Lu 2025|P151]]

## Anotações

- 
