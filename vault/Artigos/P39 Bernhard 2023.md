---
tipo: artigo
id: P39
titulo: "MapFormer: Boosting Change Detection by Using Pre-change Information"
autores: "Maximilian Bernhard, Niklas Strauß, Matthias Schubert"
ano: 2023
secao: D
categoria: "Vias, redes viárias e cartografia prévia"
tipo_publicacao: "Artigo"
papel: ["vias e cartografia"]
prioridade: baixa
doi: "10.48550/arXiv.2303.17859"
pdf: "coleta/P39_Bernhard2023_MapFormer-Boosting-Change-Detection-by-Using-Pre-change-Info.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 30
sensores: []
tarefas: ["[[Detecção de mudança (binária)]]", "[[Segmentação semântica]]"]
metodos: ["[[Transformer]]"]
datasets: ["[[DynamicEarthNet]]", "[[HRSCD]]", "[[LEVIR-CD]]", "[[S2Looking]]"]
metricas: ["[[IoU - mIoU|IoU / mIoU]]", "[[SCS (DynamicEarthNet)]]", "[[F1]]"]
ferramentas: []
etapas_pipeline: ["[[E09 Pós-processamento e eventos|E09]]"]
status_leitura: não lido
tags: [artigo, secao/D, prioridade/baixa, etapa/E09]
---

# P39 — MapFormer: Boosting Change Detection by Using Pre-change Information

**Maximilian Bernhard, Niklas Strauß, Matthias Schubert** · 2023 · Artigo · IEEE · [publicação](https://arxiv.org/abs/2303.17859) · [PDF](../../coleta/P39_Bernhard2023_MapFormer-Boosting-Change-Detection-by-Using-Pre-change-Info.pdf)

Seção: **Vias, redes viárias e cartografia prévia** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Uso proposto:** usar cartografia existente como informação adicional para localizar atualizações.
- **Código:** https://github.com/mxbh/mapformer · https://github.com/mxbh/mapformer.
- **Receita de treino extraída:** função de perda — `contrastive loss to guide the learning of visual represe` (confirmar nos chunks).
- **Métricas usadas:** [[IoU - mIoU|IoU / mIoU]], [[SCS (DynamicEarthNet)]], [[F1]]
- **Dados/benchmarks citados:** [[DynamicEarthNet]], [[HRSCD]], [[LEVIR-CD]], [[S2Looking]]

## Método e dados (da revisão original)

- **Método:** detecção condicionada por mapas semânticos prévios.

## Limites e cuidados

- mapa anterior desatualizado ou mal alinhado pode induzir erros. Avaliar qualidade e data da referência.

## Contextos de uso no projeto

- Etapas do pipeline: [[E09 Pós-processamento e eventos|E09]]
- Tarefas: [[Detecção de mudança (binária)]], [[Segmentação semântica]]
- Métodos: [[Transformer]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| dataset | [[DynamicEarthNet]] | 14 |
| dataset | [[HRSCD]] | 11 |
| dataset | [[LEVIR-CD]] | 2 |
| dataset | [[S2Looking]] | 2 |
| metodo | [[Transformer]] | 22 |
| metrica | [[IoU - mIoU\|IoU / mIoU]] | 24 |
| metrica | [[SCS (DynamicEarthNet)]] | 7 |
| metrica | [[F1]] | 4 |
| tarefa | [[Detecção de mudança (binária)]] | 35 |
| tarefa | [[Segmentação semântica]] | 24 |

## Resultados citados pelos autores (extraídos automaticamente)

> Our approach outperforms existing change detection methods by an absolute 11.7% and 18.4% in terms of binary change IoU on DynamicEarthNet and HRSCD, respectively.

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P39 chunks]] (30 chunks; resumo 2, introdução 4, trabalhos relacionados 5, métodos 7, dados 9, resultados 2, conclusão 1)
- Resumo: [[P39 chunks#^P39_c001|c001]], [[P39 chunks#^P39_c002|c002]]
- Dados / área de estudo: [[P39 chunks#^P39_c019|c019]], [[P39 chunks#^P39_c020|c020]]
- Método: [[P39 chunks#^P39_c012|c012]], [[P39 chunks#^P39_c013|c013]], [[P39 chunks#^P39_c014|c014]]
- Hiperparâmetros / treino: [[P39 chunks#^P39_c002|c002]], [[P39 chunks#^P39_c005|c005]], [[P39 chunks#^P39_c006|c006]]

## Relações

- Relação explícita: [[P40 Lee 2026|P40]]
- Vizinhos por entidades em comum: [[P145 Zhang 2025|P145]], [[P132 Zhou 2025|P132]], [[P31 Huang 2025|P31]], [[P30 Yongshuo 2025|P30]]

## Anotações

- 
