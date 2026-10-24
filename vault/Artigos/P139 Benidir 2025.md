---
tipo: artigo
id: P139
titulo: "The Change You Want To Detect: Semantic Change Detection In Earth Observation With Hybrid Data Generation"
autores: "Yanis Benidir, Nicolas Gonthier, Clément Mallet"
ano: 2025
secao: M
categoria: "Detecção de mudanças: métodos adicionais"
tipo_publicacao: "Artigo"
papel: ["método de mudança"]
prioridade: baixa
doi: "10.1109/cvpr52734.2025.00211"
pdf: "coleta/P139_Benidir2025_The-Change-You-Want-To-Detect-Semantic-Change-Detection-In-E.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 33
sensores: ["[[Imagens aéreas-VHR|Imagens aéreas/VHR]]"]
tarefas: ["[[Detecção de mudança (binária)]]", "[[Mudança semântica]]", "[[Classificação de cobertura]]"]
metodos: ["[[Transfer learning]]", "[[U-Net]]"]
datasets: ["[[S2Looking]]", "[[SECOND]]"]
metricas: ["[[IoU - mIoU|IoU / mIoU]]", "[[SCS (DynamicEarthNet)]]", "[[SeK]]"]
ferramentas: []
etapas_pipeline: ["[[E06 Modelos-base de cobertura|E06]]", "[[E07 Modelos de mudança em pares|E07]]"]
status_leitura: não lido
tags: [artigo, secao/M, prioridade/baixa, etapa/E06, etapa/E07]
---

# P139 — The Change You Want To Detect: Semantic Change Detection In Earth Observation With Hybrid Data Generation

**Yanis Benidir, Nicolas Gonthier, Clément Mallet** · 2025 · Artigo · IEEE Computer Society Conference on Computer Vision and Pattern Recogn · [publicação](https://doi.org/10.1109/cvpr52734.2025.00211) · [PDF](../../coleta/P139_Benidir2025_The-Change-You-Want-To-Detect-Semantic-Change-Detection-In-E.pdf)

Seção: **Detecção de mudanças: métodos adicionais** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Relevância:** Detecção de mudança semântica com geração híbrida de dados (CVPR 2025).
- **Receita de treino extraída:** taxa de aprendizado — `learning rate of 3e-4 with exponential decay (0.99 per epoch)`; batch size — `batch size of 32)`; função de perda — `Focal losses [31]: minimizing high-frequency error`; aumento de dados — `data augmentation` (confirmar nos chunks).
- **Métricas usadas:** [[IoU - mIoU|IoU / mIoU]], [[SCS (DynamicEarthNet)]], [[SeK]]
- **Dados/benchmarks citados:** [[S2Looking]], [[SECOND]]

## Limites e cuidados

- Conferir resolução, bandas, região e rótulos antes de transferir resultados; síntese baseada em registro e metadados.

## Contextos de uso no projeto

- Etapas do pipeline: [[E06 Modelos-base de cobertura|E06]], [[E07 Modelos de mudança em pares|E07]]
- Tarefas: [[Detecção de mudança (binária)]], [[Mudança semântica]], [[Classificação de cobertura]]
- Sensores/produtos: [[Imagens aéreas-VHR|Imagens aéreas/VHR]]
- Métodos: [[Transfer learning]], [[U-Net]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Imagens aéreas-VHR\|Imagens aéreas/VHR]] | 27 |
| dataset | [[S2Looking]] | 5 |
| dataset | [[SECOND]] | 2 |
| metodo | [[Transfer learning]] | 32 |
| metodo | [[U-Net]] | 19 |
| metrica | [[IoU - mIoU\|IoU / mIoU]] | 21 |
| metrica | [[SCS (DynamicEarthNet)]] | 11 |
| metrica | [[SeK]] | 3 |
| tarefa | [[Detecção de mudança (binária)]] | 33 |
| tarefa | [[Mudança semântica]] | 16 |
| tarefa | [[Classificação de cobertura]] | 14 |

## Chunks

- Arquivo de chunks: [[P139 chunks]] (33 chunks; resumo 2, introdução 3, trabalhos relacionados 12, dados 3, experimentos 9, métodos 3, conclusão 1)
- Resumo: [[P139 chunks#^P139_c001|c001]], [[P139 chunks#^P139_c002|c002]]
- Dados / área de estudo: [[P139 chunks#^P139_c018|c018]], [[P139 chunks#^P139_c019|c019]]
- Método: [[P139 chunks#^P139_c021|c021]], [[P139 chunks#^P139_c023|c023]], [[P139 chunks#^P139_c024|c024]]
- Hiperparâmetros / treino: [[P139 chunks#^P139_c004|c004]], [[P139 chunks#^P139_c013|c013]], [[P139 chunks#^P139_c014|c014]]
- Resultados numéricos: [[P139 chunks#^P139_c026|c026]], [[P139 chunks#^P139_c027|c027]], [[P139 chunks#^P139_c029|c029]]

## Relações

- Vizinhos por entidades em comum: [[P33 Bou 2026|P33]], [[P138 Zhang 2025|P138]], [[P19 Yang 2021|P19]], [[P18 Daudt 2019|P18]]

## Anotações

- 
