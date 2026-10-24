---
tipo: artigo
id: P13
titulo: "Satellite Image Time Series Semantic Change Detection: Novel Architecture and Analysis of Domain Shift"
autores: "Elliot Vincent, Jean Ponce, Mathieu Aubry"
ano: 2024
secao: B
categoria: "Séries temporais, edificações e transições semânticas"
tipo_publicacao: "Preprint"
papel: ["benchmark/método temporal", "preprint"]
prioridade: alta
doi: "10.48550/arXiv.2407.07616"
pdf: "coleta/P13_Vincent2024_Satellite-Image-Time-Series-Semantic-Change-Detection-Novel-.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 31
sensores: []
tarefas: ["[[Séries temporais de imagens]]", "[[Detecção de mudança (binária)]]", "[[Mudança semântica]]", "[[Segmentação semântica]]", "[[Edificações]]"]
metodos: ["[[Atenção temporal (U-TAE)]]", "[[U-Net]]", "[[Transformer]]", "[[FCN]]", "[[OBIA - objetos|OBIA / objetos]]"]
datasets: ["[[SpaceNet 7 (MUDS)]]", "[[DynamicEarthNet]]"]
metricas: ["[[IoU - mIoU|IoU / mIoU]]", "[[SCS (DynamicEarthNet)]]"]
ferramentas: []
etapas_pipeline: ["[[E08 Modelos de série temporal|E08]]", "[[E10 Avaliação e incerteza|E10]]"]
status_leitura: não lido
tags: [artigo, secao/B, prioridade/alta, etapa/E08, etapa/E10]
---

# P13 — Satellite Image Time Series Semantic Change Detection: Novel Architecture and Analysis of Domain Shift

**Elliot Vincent, Jean Ponce, Mathieu Aubry** · 2024 · Preprint · arXiv (Cornell University) · [publicação](https://arxiv.org/abs/2407.07616) · [PDF](../../coleta/P13_Vincent2024_Satellite-Image-Time-Series-Semantic-Change-Detection-Novel-.pdf)

Seção: **Séries temporais, edificações e transições semânticas** · Prioridade: **alta** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Uso proposto:** fundamenta avaliar anos e áreas inéditos, em vez de apenas sortear patches da mesma paisagem.
- **Código:** https://github.com/CUG-BEODL/TSSCD · https://github.com/VSainteuf/utae-paps · https://github.com/guanyuezhen/UFCD · https://github.com/michaeltrs/DeepSatModels
- **Receita de treino extraída:** taxa de aprendizado — `learning rate starting from 0 and gradually reaching 10−4 as a `; otimizador — `AdamW optimizer [28] with a learning rate sta`; função de perda — `focal loss [25] and the AdamW optimizer [28] with `; aumento de dados — `data augmentation, we randomly crop image patches of size 128×128 out of the ` (confirmar nos chunks).
- **Métricas usadas:** [[IoU - mIoU|IoU / mIoU]], [[SCS (DynamicEarthNet)]]
- **Dados/benchmarks citados:** [[SpaceNet 7 (MUDS)]], [[DynamicEarthNet]]

## Método e dados (da revisão original)

- **Método/dados:** arquitetura temporal avaliada em DynamicEarthNet e MUDS, com separação de mudanças de domínio espacial e temporal.

## Limites e cuidados

- o artigo evidencia dificuldades com mudanças raras e transferência; usar uma série longa não elimina a necessidade de rótulos representativos.

## Contextos de uso no projeto

- Etapas do pipeline: [[E08 Modelos de série temporal|E08]], [[E10 Avaliação e incerteza|E10]]
- Tarefas: [[Séries temporais de imagens]], [[Detecção de mudança (binária)]], [[Mudança semântica]], [[Segmentação semântica]], [[Edificações]]
- Métodos: [[Atenção temporal (U-TAE)]], [[U-Net]], [[Transformer]], [[FCN]], [[OBIA - objetos|OBIA / objetos]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| dataset | [[SpaceNet 7 (MUDS)]] | 39 |
| dataset | [[DynamicEarthNet]] | 34 |
| metodo | [[Atenção temporal (U-TAE)]] | 8 |
| metodo | [[U-Net]] | 4 |
| metodo | [[Transformer]] | 4 |
| metodo | [[FCN]] | 3 |
| metodo | [[OBIA - objetos\|OBIA / objetos]] | 3 |
| metrica | [[IoU - mIoU\|IoU / mIoU]] | 16 |
| metrica | [[SCS (DynamicEarthNet)]] | 16 |
| tarefa | [[Séries temporais de imagens]] | 34 |
| tarefa | [[Detecção de mudança (binária)]] | 23 |
| tarefa | [[Mudança semântica]] | 18 |
| tarefa | [[Segmentação semântica]] | 18 |
| tarefa | [[Edificações]] | 13 |

## Resultados citados pelos autores (extraídos automaticamente)

> For all evaluated methods, we observe an average relative drop of the mIoU from the setting without domain shift to the spatial shift setting of 31.9% on DynamicEarthNet and of 10.5% on MUDS.
> methods, we observe an average relative drop of the mIoU from the setting without domain shift to the spatial shift setting of 31.9% on DynamicEarthNet and of 10.5% on MUDS.

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P13 chunks]] (31 chunks; resumo 2, introdução 3, trabalhos relacionados 6, métodos 6, dados 7, resultados 6, conclusão 1)
- Resumo: [[P13 chunks#^P13_c001|c001]], [[P13 chunks#^P13_c002|c002]]
- Dados / área de estudo: [[P13 chunks#^P13_c018|c018]], [[P13 chunks#^P13_c019|c019]]
- Método: [[P13 chunks#^P13_c012|c012]], [[P13 chunks#^P13_c013|c013]], [[P13 chunks#^P13_c014|c014]]
- Hiperparâmetros / treino: [[P13 chunks#^P13_c017|c017]]
- Resultados numéricos: [[P13 chunks#^P13_c027|c027]], [[P13 chunks#^P13_c028|c028]]

## Relações

- Vizinhos por entidades em comum: [[P127 Miller 2024|P127]], [[P11 Etten 2021|P11]], [[P28 Chen 2024|P28]], [[P12 Toker 2022|P12]]

## Anotações

- 
