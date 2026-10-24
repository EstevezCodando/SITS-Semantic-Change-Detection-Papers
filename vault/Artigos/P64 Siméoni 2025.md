---
tipo: artigo
id: P64
titulo: "DINOv3"
autores: "Oriane Siméoni, Huy V. Vo, Maximilian Seitzer, Federico Baldassarre"
ano: 2025
secao: G
categoria: "Pré-catalogação SAM/YOLO e representações"
tipo_publicacao: "Artigo"
papel: ["pré-anotação/representação"]
prioridade: baixa
doi: "10.48550/arXiv.2508.10104"
pdf: "coleta/P64_Simeoni2025_DINOv3.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 107
sensores: ["[[Imagens aéreas-VHR|Imagens aéreas/VHR]]"]
tarefas: ["[[Anotação-rotulagem|Anotação/rotulagem]]", "[[Detecção de objetos]]", "[[Segmentação semântica]]"]
metodos: ["[[DINO-DINOv3|DINO/DINOv3]]", "[[Transformer]]", "[[CLIP - visão-linguagem|CLIP / visão-linguagem]]", "[[Semi-auto-supervisionado|Semi/auto-supervisionado]]", "[[Supervisão fraca]]", "[[Transfer learning]]"]
datasets: ["[[OpenStreetMap]]"]
metricas: ["[[IoU - mIoU|IoU / mIoU]]", "[[Precisão-Recall|Precisão/Recall]]", "[[RMSE-MAE|RMSE/MAE]]", "[[mAP]]"]
ferramentas: []
etapas_pipeline: ["[[E04 Rotulagem e pré-anotação|E04]]", "[[E05 Atributos e representações|E05]]"]
status_leitura: não lido
tags: [artigo, secao/G, prioridade/baixa, etapa/E04, etapa/E05]
---

# P64 — DINOv3

**Oriane Siméoni, Huy V. Vo, Maximilian Seitzer** · 2025 · Artigo · arXiv (Cornell University) · [publicação](https://arxiv.org/abs/2508.10104) · [PDF](../../coleta/P64_Simeoni2025_DINOv3.pdf)

Seção: **Pré-catalogação SAM/YOLO e representações** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Receita de treino extraída:** taxa de aprendizado — `learning rate, weight decay, and teacher EMA momentum`; batch size — `batch size of 131K`; épocas — `22 epochs`; otimizador — `AdamW (Loshchilov and Hutter, 2017), and set `; função de perda — `contrastive losses and the joint-training of caption rep` (confirmar nos chunks).
- **Métricas usadas:** [[IoU - mIoU|IoU / mIoU]], [[Precisão-Recall|Precisão/Recall]], [[RMSE-MAE|RMSE/MAE]], [[mAP]]
- **Dados/benchmarks citados:** [[OpenStreetMap]]

## Método e dados (da revisão original)

- **Método:** extração de representações densas; inclui treinamento e avaliação em dados geoespaciais.

## Limites e cuidados

- embedding não é classe; agrupamentos não são uma taxonomia validada. O checkpoint indicado é grande, e não uma indicação automática de melhor custo-benefício.

## Contextos de uso no projeto

- Etapas do pipeline: [[E04 Rotulagem e pré-anotação|E04]], [[E05 Atributos e representações|E05]]
- Tarefas: [[Anotação-rotulagem|Anotação/rotulagem]], [[Detecção de objetos]], [[Segmentação semântica]]
- Sensores/produtos: [[Imagens aéreas-VHR|Imagens aéreas/VHR]]
- Métodos: [[DINO-DINOv3|DINO/DINOv3]], [[Transformer]], [[CLIP - visão-linguagem|CLIP / visão-linguagem]], [[Semi-auto-supervisionado|Semi/auto-supervisionado]], [[Supervisão fraca]], [[Transfer learning]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Imagens aéreas-VHR\|Imagens aéreas/VHR]] | 6 |
| dataset | [[OpenStreetMap]] | 2 |
| metodo | [[DINO-DINOv3\|DINO/DINOv3]] | 342 |
| metodo | [[Transformer]] | 141 |
| metodo | [[CLIP - visão-linguagem\|CLIP / visão-linguagem]] | 25 |
| metodo | [[Semi-auto-supervisionado\|Semi/auto-supervisionado]] | 23 |
| metodo | [[Supervisão fraca]] | 19 |
| metodo | [[Transfer learning]] | 16 |
| metrica | [[IoU - mIoU\|IoU / mIoU]] | 32 |
| metrica | [[Precisão-Recall\|Precisão/Recall]] | 17 |
| metrica | [[RMSE-MAE\|RMSE/MAE]] | 16 |
| metrica | [[mAP]] | 9 |
| tarefa | [[Anotação-rotulagem\|Anotação/rotulagem]] | 13 |
| tarefa | [[Detecção de objetos]] | 11 |
| tarefa | [[Segmentação semântica]] | 10 |

## Resultados citados pelos autores (extraídos automaticamente)

> VOC NYUv2 ↓ KITTI ↓ Agglomerative backbones AM-RADIOv2.5 g/14 53.0 78.4 85.4 0.340 2.918 PEspatial G/14 49.3 73.2 82.7 0.362 3.082 Weakly-supervised backbones SigLIP 2 g/16 42.7 64.8 72.7 0.494 3.273 PEcore G/14 38.9 61.1 69.2 0.5
> 0.309 2.346 (mIoU) metric.
> Even there, DINOv3 outperforms its predecessor DINOv2 by 0.278 RMSE.

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P64 chunks]] (107 chunks; resumo 2, introdução 10, trabalhos relacionados 39, resultados 55, conclusão 1)
- Resumo: [[P64 chunks#^P64_c001|c001]], [[P64 chunks#^P64_c002|c002]]
- Hiperparâmetros / treino: [[P64 chunks#^P64_c017|c017]], [[P64 chunks#^P64_c018|c018]], [[P64 chunks#^P64_c033|c033]]
- Resultados numéricos: [[P64 chunks#^P64_c055|c055]], [[P64 chunks#^P64_c056|c056]], [[P64 chunks#^P64_c057|c057]]

## Relações

- Vizinhos por entidades em comum: [[P62 Carion 2025|P62]], [[P65 Faulkenberry 2026|P65]], [[P63 Dabaja 2026|P63]], [[P35 Su 2026|P35]]

## Anotações

- 
