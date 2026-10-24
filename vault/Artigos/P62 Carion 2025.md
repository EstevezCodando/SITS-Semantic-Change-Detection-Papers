---
tipo: artigo
id: P62
titulo: "SAM 3: Segment Anything with Concepts"
autores: "Nicolas Carion, Laura Gustafson, Yuan-Ting Hu, Shoubhik Debnath"
ano: 2025
secao: G
categoria: "Pré-catalogação SAM/YOLO e representações"
tipo_publicacao: "Preprint"
papel: ["pré-anotação/representação", "preprint"]
prioridade: média
doi: "10.48550/arXiv.2511.16719"
pdf: "coleta/P62_Carion2025_SAM-3-Segment-Anything-with-Concepts.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 54
sensores: []
tarefas: ["[[Anotação-rotulagem|Anotação/rotulagem]]"]
metodos: ["[[SAM]]", "[[CLIP - visão-linguagem|CLIP / visão-linguagem]]", "[[Transfer learning]]", "[[Semi-auto-supervisionado|Semi/auto-supervisionado]]", "[[Transformer]]", "[[DINO-DINOv3|DINO/DINOv3]]"]
datasets: []
metricas: ["[[mAP]]", "[[IoU - mIoU|IoU / mIoU]]", "[[RMSE-MAE|RMSE/MAE]]"]
ferramentas: []
etapas_pipeline: ["[[E04 Rotulagem e pré-anotação|E04]]", "[[E05 Atributos e representações|E05]]"]
status_leitura: não lido
tags: [artigo, secao/G, prioridade/média, etapa/E04, etapa/E05]
---

# P62 — SAM 3: Segment Anything with Concepts

**Nicolas Carion, Laura Gustafson, Yuan-Ting Hu** · 2025 · Preprint · arXiv (Cornell University) · [publicação](https://arxiv.org/abs/2511.16719) · [PDF](../../coleta/P62_Carion2025_SAM-3-Segment-Anything-with-Concepts.pdf)

Seção: **Pré-catalogação SAM/YOLO e representações** · Prioridade: **média** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Uso proposto:** candidato recente para catalogação orientada por conceitos e seleção assistida de objetos.
- **Código:** https://github.com/JonathonLuiten/TrackEval · https://github.com/facebookresearch/sam3
- **Métricas usadas:** [[mAP]], [[IoU - mIoU|IoU / mIoU]], [[RMSE-MAE|RMSE/MAE]]

## Método e dados (da revisão original)

- **Método:** detecção, segmentação e rastreamento com prompts conceituais textuais ou exemplos visuais.

## Limites e cuidados

- rastreamento em vídeo não equivale à associação de objetos entre mosaicos mensais com mudanças radiométricas e grandes intervalos. A transferência exige avaliação própria.

## Contextos de uso no projeto

- Etapas do pipeline: [[E04 Rotulagem e pré-anotação|E04]], [[E05 Atributos e representações|E05]]
- Tarefas: [[Anotação-rotulagem|Anotação/rotulagem]]
- Métodos: [[SAM]], [[CLIP - visão-linguagem|CLIP / visão-linguagem]], [[Transfer learning]], [[Semi-auto-supervisionado|Semi/auto-supervisionado]], [[Transformer]], [[DINO-DINOv3|DINO/DINOv3]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| metodo | [[SAM]] | 222 |
| metodo | [[CLIP - visão-linguagem\|CLIP / visão-linguagem]] | 15 |
| metodo | [[Transfer learning]] | 9 |
| metodo | [[Semi-auto-supervisionado\|Semi/auto-supervisionado]] | 6 |
| metodo | [[Transformer]] | 5 |
| metodo | [[DINO-DINOv3\|DINO/DINOv3]] | 5 |
| metrica | [[mAP]] | 10 |
| metrica | [[IoU - mIoU\|IoU / mIoU]] | 8 |
| metrica | [[RMSE-MAE\|RMSE/MAE]] | 5 |
| tarefa | [[Anotação-rotulagem\|Anotação/rotulagem]] | 62 |

## Chunks

- Arquivo de chunks: [[P62 chunks]] (54 chunks; resumo 1, introdução 35, trabalhos relacionados 3, conclusão 1, resultados 14)
- Resumo: [[P62 chunks#^P62_c001|c001]]

## Relações

- Vizinhos por entidades em comum: [[P65 Faulkenberry 2026|P65]], [[P64 Siméoni 2025|P64]], [[P56 Osco 2023|P56]], [[P57 Ren 2024|P57]]

## Anotações

- 
