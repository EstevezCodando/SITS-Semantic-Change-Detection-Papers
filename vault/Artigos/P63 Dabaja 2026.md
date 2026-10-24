---
tipo: artigo
id: P63
titulo: "Promptable Concept Segmentation from Above: Evaluating SAM 3’s Zero-Shot and One-Shot Capabilities in Remote Sensing"
autores: "Mohammad Dabaja, Turgay Çelik"
ano: 2026
secao: G
categoria: "Pré-catalogação SAM/YOLO e representações"
tipo_publicacao: "Preprint"
papel: ["pré-anotação/representação", "preprint"]
prioridade: baixa
doi: "10.48550/arXiv.2607.09583"
pdf: "coleta/P63_Dabaja2026_Promptable-Concept-Segmentation-from-Above-Evaluating-SAM-3s.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 54
sensores: ["[[Imagens aéreas-VHR|Imagens aéreas/VHR]]", "[[Planet (mosaicos e cenas)]]"]
tarefas: ["[[Detecção de objetos]]"]
metodos: ["[[SAM]]", "[[CLIP - visão-linguagem|CLIP / visão-linguagem]]", "[[Transfer learning]]", "[[Modelo fundacional]]", "[[Transformer]]", "[[Grounding DINO]]"]
datasets: []
metricas: ["[[mAP]]", "[[IoU - mIoU|IoU / mIoU]]", "[[Precisão-Recall|Precisão/Recall]]"]
ferramentas: []
etapas_pipeline: ["[[E04 Rotulagem e pré-anotação|E04]]", "[[E05 Atributos e representações|E05]]"]
status_leitura: não lido
tags: [artigo, secao/G, prioridade/baixa, etapa/E04, etapa/E05]
---

# P63 — Promptable Concept Segmentation from Above: Evaluating SAM 3’s Zero-Shot and One-Shot Capabilities in Remote Sensing

**Mohammad Dabaja, Turgay Çelik** · 2026 · Preprint · arXiv (Cornell University) · [publicação](https://arxiv.org/html/2607.09583v1) · [PDF](../../coleta/P63_Dabaja2026_Promptable-Concept-Segmentation-from-Above-Evaluating-SAM-3s.pdf)

Seção: **Pré-catalogação SAM/YOLO e representações** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Uso proposto:** ajuda a avaliar objetivamente quando texto ou exemplo visual são úteis para pré-catalogar.
- **Receita de treino extraída:** tamanho do patch — `600 × 600 pixel` (confirmar nos chunks).
- **Métricas usadas:** [[mAP]], [[IoU - mIoU|IoU / mIoU]], [[Precisão-Recall|Precisão/Recall]]

## Método e dados (da revisão original)

- **Método:** avaliação de SAM 3 em classificação de cenas, detecção e segmentação de instâncias no domínio remoto.

## Limites e cuidados

- os autores relatam dificuldades de transferência e interferência entre modalidades de prompt. É evidência contra presumir confiabilidade zero-shot universal, não uma validação Planet local.

## Contextos de uso no projeto

- Etapas do pipeline: [[E04 Rotulagem e pré-anotação|E04]], [[E05 Atributos e representações|E05]]
- Tarefas: [[Detecção de objetos]]
- Sensores/produtos: [[Imagens aéreas-VHR|Imagens aéreas/VHR]], [[Planet (mosaicos e cenas)]]
- Métodos: [[SAM]], [[CLIP - visão-linguagem|CLIP / visão-linguagem]], [[Transfer learning]], [[Modelo fundacional]], [[Transformer]], [[Grounding DINO]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Imagens aéreas-VHR\|Imagens aéreas/VHR]] | 4 |
| sensor | [[Planet (mosaicos e cenas)]] | 1 |
| metodo | [[SAM]] | 77 |
| metodo | [[CLIP - visão-linguagem\|CLIP / visão-linguagem]] | 36 |
| metodo | [[Transfer learning]] | 17 |
| metodo | [[Modelo fundacional]] | 12 |
| metodo | [[Transformer]] | 3 |
| metodo | [[Grounding DINO]] | 3 |
| metrica | [[mAP]] | 40 |
| metrica | [[IoU - mIoU\|IoU / mIoU]] | 6 |
| metrica | [[Precisão-Recall\|Precisão/Recall]] | 4 |
| tarefa | [[Detecção de objetos]] | 10 |

## Resultados citados pelos autores (extraídos automaticamente)

> Metrics are reported for mAP (IoU 0.50:0.95) and AP@50.
> mAP (IoU 0.50:0.95) AP@50 Class Concept T TB B TBF TF T TB B TBF TF Airplane 60.22 63.56 65.68 65.73 62.39 91.43 91.52 93.64 95.66 95.61 Airport 92.25 92.34 92.39 98.69 98.87 98.99 Baseball Field 0.01 59.87 77.54 60.98 0.01 0.01 6
> Metrics are reported for mAP (IoU 0.50:0.95) and AP@50.

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P63 chunks]] (54 chunks; resumo 2, introdução 5, métodos 12, trabalhos relacionados 6, experimentos 9, resultados 17, conclusão 3)
- Resumo: [[P63 chunks#^P63_c001|c001]], [[P63 chunks#^P63_c002|c002]]
- Método: [[P63 chunks#^P63_c008|c008]], [[P63 chunks#^P63_c015|c015]], [[P63 chunks#^P63_c016|c016]]
- Hiperparâmetros / treino: [[P63 chunks#^P63_c015|c015]], [[P63 chunks#^P63_c016|c016]]
- Resultados numéricos: [[P63 chunks#^P63_c022|c022]], [[P63 chunks#^P63_c023|c023]], [[P63 chunks#^P63_c027|c027]]

## Relações

- Vizinhos por entidades em comum: [[P65 Faulkenberry 2026|P65]], [[P57 Ren 2024|P57]], [[P64 Siméoni 2025|P64]], [[P62 Carion 2025|P62]]

## Anotações

- 
