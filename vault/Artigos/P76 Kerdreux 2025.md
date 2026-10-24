---
tipo: artigo
id: P76
titulo: "Efficient Self-Supervised Learning for Earth Observation via Dynamic Dataset Curation"
autores: "Thomas Kerdreux, Alexandre Tuel, Quentin Febvre, Alexis Aurelien Mouche"
ano: 2025
secao: I
categoria: "Ciência de dados e curadoria"
tipo_publicacao: "Artigo"
papel: ["validação/curadoria"]
prioridade: baixa
doi: "10.48550/arXiv.2504.06962"
pdf: "coleta/P76_Kerdreux2025_Efficient-Self-Supervised-Learning-for-Earth-Observation-via.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 34
sensores: ["[[Sentinel-1-SAR|Sentinel-1/SAR]]", "[[Planet (mosaicos e cenas)]]"]
tarefas: []
metodos: ["[[Transformer]]", "[[Modelo fundacional]]", "[[Semi-auto-supervisionado|Semi/auto-supervisionado]]", "[[ResNet]]", "[[Transfer learning]]", "[[DINO-DINOv3|DINO/DINOv3]]"]
datasets: []
metricas: ["[[RMSE-MAE|RMSE/MAE]]"]
ferramentas: []
etapas_pipeline: ["[[E03 Cubo espaço-temporal e partições|E03]]", "[[E04 Rotulagem e pré-anotação|E04]]", "[[E05 Atributos e representações|E05]]", "[[E10 Avaliação e incerteza|E10]]"]
status_leitura: não lido
tags: [artigo, secao/I, prioridade/baixa, etapa/E03, etapa/E04, etapa/E05, etapa/E10]
---

# P76 — Efficient Self-Supervised Learning for Earth Observation via Dynamic Dataset Curation

**Thomas Kerdreux, Alexandre Tuel, Quentin Febvre** · 2025 · Artigo · IEEE · [publicação](https://arxiv.org/html/2504.06962v1) · [PDF](../../coleta/P76_Kerdreux2025_Efficient-Self-Supervised-Learning-for-Earth-Observation-via.pdf)

Seção: **Ciência de dados e curadoria** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Uso proposto:** inspira seleção de amostras informativas em vez de treinar com todos os patches repetidos de meses estáveis.
- **Receita de treino extraída:** taxa de aprendizado — `learning rate`; batch size — `batch size of 256, an AdamW optimizer, a cosine sc`; épocas — `200 epochs`; otimizador — `AdamW optimizer, a cosine scheduler with anne`; função de perda — `focal loss or self-paced reweighting [13, 26, 54]` (confirmar nos chunks).
- **Métricas usadas:** [[RMSE-MAE|RMSE/MAE]]

## Método e dados (da revisão original)

- **Contribuição:** seleção dinâmica para reduzir redundância e melhorar diversidade no pré-treinamento.

## Limites e cuidados

- experimentos em Sentinel-1 Wave Mode, predominantemente oceânico. É referência de curadoria, não evidência direta em cobertura terrestre Planet.

## Contextos de uso no projeto

- Etapas do pipeline: [[E03 Cubo espaço-temporal e partições|E03]], [[E04 Rotulagem e pré-anotação|E04]], [[E05 Atributos e representações|E05]], [[E10 Avaliação e incerteza|E10]]
- Sensores/produtos: [[Sentinel-1-SAR|Sentinel-1/SAR]], [[Planet (mosaicos e cenas)]]
- Métodos: [[Transformer]], [[Modelo fundacional]], [[Semi-auto-supervisionado|Semi/auto-supervisionado]], [[ResNet]], [[Transfer learning]], [[DINO-DINOv3|DINO/DINOv3]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Sentinel-1-SAR\|Sentinel-1/SAR]] | 40 |
| sensor | [[Planet (mosaicos e cenas)]] | 1 |
| metodo | [[Transformer]] | 32 |
| metodo | [[Modelo fundacional]] | 23 |
| metodo | [[Semi-auto-supervisionado\|Semi/auto-supervisionado]] | 19 |
| metodo | [[ResNet]] | 13 |
| metodo | [[Transfer learning]] | 12 |
| metodo | [[DINO-DINOv3\|DINO/DINOv3]] | 7 |
| metrica | [[RMSE-MAE\|RMSE/MAE]] | 9 |

## Chunks

- Arquivo de chunks: [[P76 chunks]] (34 chunks; resumo 3, introdução 4, trabalhos relacionados 5, métodos 13, experimentos 2, dados 6, discussão 1)
- Resumo: [[P76 chunks#^P76_c001|c001]], [[P76 chunks#^P76_c002|c002]]
- Dados / área de estudo: [[P76 chunks#^P76_c023|c023]], [[P76 chunks#^P76_c024|c024]]
- Método: [[P76 chunks#^P76_c013|c013]], [[P76 chunks#^P76_c014|c014]], [[P76 chunks#^P76_c015|c015]]
- Hiperparâmetros / treino: [[P76 chunks#^P76_c008|c008]], [[P76 chunks#^P76_c009|c009]], [[P76 chunks#^P76_c012|c012]]
- Limitações / discussão: [[P76 chunks#^P76_c033|c033]]

## Relações

- Vizinhos por entidades em comum: [[P65 Faulkenberry 2026|P65]], [[P67 Xiong 2024|P67]], [[P34 Shen 2026|P34]], [[P151 Lu 2025|P151]]

## Anotações

- 
