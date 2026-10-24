---
tipo: artigo
id: P26
titulo: "A Transformer-Based Siamese Network for Change Detection"
autores: "Wele Gedara Chaminda Bandara, Vishal M. Patel"
ano: 2022
secao: C
categoria: "Detectores profundos e modelos fundacionais"
tipo_publicacao: "Artigo"
papel: ["baseline/método de mudança"]
prioridade: média
doi: "10.48550/arXiv.2201.01293"
pdf: "coleta/P26_Bandara2022_A-Transformer-Based-Siamese-Network-for-Change-Detection.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 19
sensores: []
tarefas: []
metodos: ["[[Transformer]]", "[[Rede siamesa]]", "[[U-Net]]"]
datasets: ["[[LEVIR-CD]]"]
metricas: ["[[Acurácia global]]", "[[F1]]", "[[IoU - mIoU|IoU / mIoU]]", "[[Precisão-Recall|Precisão/Recall]]"]
ferramentas: []
etapas_pipeline: ["[[E07 Modelos de mudança em pares|E07]]"]
status_leitura: não lido
tags: [artigo, secao/C, prioridade/média, etapa/E07]
---

# P26 — A Transformer-Based Siamese Network for Change Detection

**Wele Gedara Chaminda Bandara, Vishal M. Patel** · 2022 · Artigo · IEEE International Geoscience and Remote Sensing Symposium (IGARSS) · [publicação](https://arxiv.org/abs/2201.01293) · [PDF](../../coleta/P26_Bandara2022_A-Transformer-Based-Siamese-Network-for-Change-Detection.pdf)

Seção: **Detectores profundos e modelos fundacionais** · Prioridade: **média** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Uso proposto:** comparar com U-Net/FC-Siam sob os mesmos dados, rótulos e orçamento.
- **Código:** https://github.com/wgcban/ChangeFormer
- **Receita de treino extraída:** taxa de aprendizado — `learning rate is initially set to 0.0001 and linearly decays to `; batch size — `batch size of 16 to train the model`; épocas — `200 epochs`; otimizador — `AdamW optimizer with weight decay equal to 0`; aumento de dados — `data augmentation through random flip, random re-scale (0` (confirmar nos chunks).
- **Métricas usadas:** [[Acurácia global]], [[F1]], [[IoU - mIoU|IoU / mIoU]], [[Precisão-Recall|Precisão/Recall]]
- **Dados/benchmarks citados:** [[LEVIR-CD]]

## Método e dados (da revisão original)

- **Método:** rede siamesa com transformers para pares corregistrados.

## Limites e cuidados

- adaptação para bandas adicionais e saída semântica deve ser explícita.

## Contextos de uso no projeto

- Etapas do pipeline: [[E07 Modelos de mudança em pares|E07]]
- Métodos: [[Transformer]], [[Rede siamesa]], [[U-Net]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| dataset | [[LEVIR-CD]] | 9 |
| metodo | [[Transformer]] | 41 |
| metodo | [[Rede siamesa]] | 11 |
| metodo | [[U-Net]] | 1 |
| metrica | [[Acurácia global]] | 7 |
| metrica | [[F1]] | 6 |
| metrica | [[IoU - mIoU\|IoU / mIoU]] | 6 |
| metrica | [[Precisão-Recall\|Precisão/Recall]] | 6 |

## Resultados citados pelos autores (extraídos automaticamente)

> In particular, our ChangeFormer improves previous SOTA in F1/IoU/OA by 1.2/2.2/0.1% and 20.0/44.3/6.4% for LEVIR-CD and DSIFN-CD, respectively.

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P26 chunks]] (19 chunks; resumo 2, introdução 2, métodos 9, dados 1, experimentos 1, resultados 3, conclusão 1)
- Resumo: [[P26 chunks#^P26_c001|c001]], [[P26 chunks#^P26_c002|c002]]
- Dados / área de estudo: [[P26 chunks#^P26_c013|c013]]
- Método: [[P26 chunks#^P26_c005|c005]], [[P26 chunks#^P26_c006|c006]], [[P26 chunks#^P26_c007|c007]]
- Hiperparâmetros / treino: [[P26 chunks#^P26_c014|c014]]
- Resultados numéricos: [[P26 chunks#^P26_c018|c018]]

## Relações

- Vizinhos por entidades em comum: [[P25 Chen 2021|P25]], [[P133 Ding 2024|P133]], [[P49 Lei 2026|P49]], [[P132 Zhou 2025|P132]]

## Anotações

- 
