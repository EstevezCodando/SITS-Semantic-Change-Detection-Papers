---
tipo: artigo
id: P65
titulo: "DINO Soars: DINOv3 for Open-Vocabulary Semantic Segmentation of Remote Sensing Imagery"
autores: "Ryan Faulkenberry, Saurabh Prasad"
ano: 2026
secao: G
categoria: "Pré-catalogação SAM/YOLO e representações"
tipo_publicacao: "Preprint"
papel: ["pré-anotação/representação", "preprint"]
prioridade: baixa
doi: "10.48550/arXiv.2605.03175"
pdf: "coleta/P65_Faulkenberry2026_DINO-Soars-DINOv3-for-Open-Vocabulary-Semantic-Segmentation-.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 29
sensores: ["[[Planet (mosaicos e cenas)]]"]
tarefas: []
metodos: ["[[DINO-DINOv3|DINO/DINOv3]]", "[[Transfer learning]]", "[[CLIP - visão-linguagem|CLIP / visão-linguagem]]", "[[Transformer]]", "[[Modelo fundacional]]", "[[Semi-auto-supervisionado|Semi/auto-supervisionado]]"]
datasets: []
metricas: ["[[IoU - mIoU|IoU / mIoU]]"]
ferramentas: []
etapas_pipeline: ["[[E04 Rotulagem e pré-anotação|E04]]", "[[E05 Atributos e representações|E05]]"]
status_leitura: não lido
tags: [artigo, secao/G, prioridade/baixa, etapa/E04, etapa/E05]
---

# P65 — DINO Soars: DINOv3 for Open-Vocabulary Semantic Segmentation of Remote Sensing Imagery

**Ryan Faulkenberry, Saurabh Prasad** · 2026 · Preprint · arXiv (Cornell University) · [publicação](https://arxiv.org/abs/2605.03175) · [PDF](../../coleta/P65_Faulkenberry2026_DINO-Soars-DINOv3-for-Open-Vocabulary-Semantic-Segmentation-.pdf)

Seção: **Pré-catalogação SAM/YOLO e representações** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Uso proposto:** candidato de pré-classificação de cenas e cobertura.
- **Código:** https://github.com/rfaulk/DINO_Soars · https://github.com/rfaulk/DINO_Soars.
- **Receita de treino extraída:** batch size — `batch size of 4 for 45,000 iterations`; tamanho do patch — `512 × 512 and perform sliding window` (confirmar nos chunks).
- **Métricas usadas:** [[IoU - mIoU|IoU / mIoU]]

## Método e dados (da revisão original)

- **Método:** CAFe-DINO, agregação e aumento de resolução de similaridades texto–imagem para segmentação aberta.

## Limites e cuidados

- ausência de fine-tuning em imagens remotas não significa ausência total de treinamento; o resumo descreve ajuste em subconjunto de COCO-Stuff. Ainda requer teste em Planet.

## Contextos de uso no projeto

- Etapas do pipeline: [[E04 Rotulagem e pré-anotação|E04]], [[E05 Atributos e representações|E05]]
- Sensores/produtos: [[Planet (mosaicos e cenas)]]
- Métodos: [[DINO-DINOv3|DINO/DINOv3]], [[Transfer learning]], [[CLIP - visão-linguagem|CLIP / visão-linguagem]], [[Transformer]], [[Modelo fundacional]], [[Semi-auto-supervisionado|Semi/auto-supervisionado]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Planet (mosaicos e cenas)]] | 1 |
| metodo | [[DINO-DINOv3\|DINO/DINOv3]] | 97 |
| metodo | [[Transfer learning]] | 25 |
| metodo | [[CLIP - visão-linguagem\|CLIP / visão-linguagem]] | 21 |
| metodo | [[Transformer]] | 11 |
| metodo | [[Modelo fundacional]] | 6 |
| metodo | [[Semi-auto-supervisionado\|Semi/auto-supervisionado]] | 3 |
| metrica | [[IoU - mIoU\|IoU / mIoU]] | 9 |

## Resultados citados pelos autores (extraídos automaticamente)

> 63.9 53.8 34.9 58.6 is necessary for competitive performance, yielding, in the worst case, an 11.9% mIoU gain compared to freezing the backbone completely.

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P65 chunks]] (29 chunks; resumo 2, introdução 4, dados 2, trabalhos relacionados 6, métodos 6, experimentos 1, resultados 6, conclusão 1, discussão 1)
- Resumo: [[P65 chunks#^P65_c001|c001]], [[P65 chunks#^P65_c002|c002]]
- Dados / área de estudo: [[P65 chunks#^P65_c007|c007]], [[P65 chunks#^P65_c021|c021]]
- Método: [[P65 chunks#^P65_c014|c014]], [[P65 chunks#^P65_c015|c015]], [[P65 chunks#^P65_c016|c016]]
- Hiperparâmetros / treino: [[P65 chunks#^P65_c020|c020]]
- Resultados numéricos: [[P65 chunks#^P65_c027|c027]]
- Limitações / discussão: [[P65 chunks#^P65_c029|c029]]

## Relações

- Vizinhos por entidades em comum: [[P76 Kerdreux 2025|P76]], [[P62 Carion 2025|P62]], [[P67 Xiong 2024|P67]], [[P63 Dabaja 2026|P63]]

## Anotações

- 
