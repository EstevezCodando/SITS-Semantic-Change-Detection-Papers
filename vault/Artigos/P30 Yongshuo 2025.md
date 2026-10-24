---
tipo: artigo
id: P30
titulo: "Semantic-CD: Remote Sensing Image Semantic Change Detection towards Open-vocabulary Setting"
autores: "Zhu, Yongshuo, Li, Lu, Keyan Chen, Liu, Chenyang"
ano: 2025
secao: C
categoria: "Detectores profundos e modelos fundacionais"
tipo_publicacao: "Preprint"
papel: ["baseline/método de mudança", "preprint"]
prioridade: baixa
doi: "10.48550/arXiv.2501.06808"
pdf: "coleta/P30_Yongshuo2025_Semantic-CD-Remote-Sensing-Image-Semantic-Change-Detection-t.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 17
sensores: []
tarefas: ["[[Detecção de mudança (binária)]]", "[[Mudança semântica]]"]
metodos: ["[[CLIP - visão-linguagem|CLIP / visão-linguagem]]", "[[Modelo fundacional]]", "[[Transformer]]"]
datasets: ["[[SECOND]]", "[[HRSCD]]"]
metricas: ["[[F1]]"]
ferramentas: ["[[PyTorch]]"]
etapas_pipeline: ["[[E05 Atributos e representações|E05]]", "[[E07 Modelos de mudança em pares|E07]]"]
status_leitura: não lido
tags: [artigo, secao/C, prioridade/baixa, etapa/E05, etapa/E07]
---

# P30 — Semantic-CD: Remote Sensing Image Semantic Change Detection towards Open-vocabulary Setting

**Zhu, Yongshuo, Li, Lu, Keyan Chen** · 2025 · Preprint · arXiv (Cornell University) · [publicação](https://arxiv.org/abs/2501.06808) · [PDF](../../coleta/P30_Yongshuo2025_Semantic-CD-Remote-Sensing-Image-Semantic-Change-Detection-t.pdf)

Seção: **Detectores profundos e modelos fundacionais** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Uso proposto:** investigar categorias descritas por texto e assistência à classificação.
- **Receita de treino extraída:** batch size — `batch size of 1 and trained for 300 epochs`; épocas — `300 epochs`; função de perda — `cross-entropy loss for supervised training, as detail` (confirmar nos chunks).
- **Métricas usadas:** [[F1]]
- **Dados/benchmarks citados:** [[SECOND]], [[HRSCD]]

## Método e dados (da revisão original)

- **Método:** CLIP, prompts semânticos e decodificação de mudança binária/semântica.

## Limites e cuidados

- vocabulário aberto não equivale a reconhecer com confiabilidade toda classe territorial local.

## Contextos de uso no projeto

- Etapas do pipeline: [[E05 Atributos e representações|E05]], [[E07 Modelos de mudança em pares|E07]]
- Tarefas: [[Detecção de mudança (binária)]], [[Mudança semântica]]
- Métodos: [[CLIP - visão-linguagem|CLIP / visão-linguagem]], [[Modelo fundacional]], [[Transformer]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| dataset | [[SECOND]] | 5 |
| dataset | [[HRSCD]] | 2 |
| metodo | [[CLIP - visão-linguagem\|CLIP / visão-linguagem]] | 49 |
| metodo | [[Modelo fundacional]] | 9 |
| metodo | [[Transformer]] | 5 |
| metrica | [[F1]] | 12 |
| tarefa | [[Detecção de mudança (binária)]] | 32 |
| tarefa | [[Mudança semântica]] | 22 |
| ferramenta | [[PyTorch]] | 2 |

## Chunks

- Arquivo de chunks: [[P30 chunks]] (17 chunks; resumo 1, introdução 3, métodos 10, experimentos 1, dados 1, conclusão 1)
- Resumo: [[P30 chunks#^P30_c001|c001]]
- Dados / área de estudo: [[P30 chunks#^P30_c013|c013]]
- Método: [[P30 chunks#^P30_c005|c005]], [[P30 chunks#^P30_c006|c006]], [[P30 chunks#^P30_c007|c007]]
- Hiperparâmetros / treino: [[P30 chunks#^P30_c011|c011]], [[P30 chunks#^P30_c014|c014]], [[P30 chunks#^P30_c015|c015]]

## Relações

- Vizinhos por entidades em comum: [[P31 Huang 2025|P31]], [[P34 Shen 2026|P34]], [[P20 Zheng 2022|P20]], [[P19 Yang 2021|P19]]

## Anotações

- 
