---
tipo: artigo
id: P37
titulo: "RoadTracer: Automatic Extraction of Road Networks From Aerial Images"
autores: "Favyen Bastani, Songtao He, Sofiane Abbar, Mohammad Alizadeh"
ano: 2018
secao: D
categoria: "Vias, redes viárias e cartografia prévia"
tipo_publicacao: "Artigo"
papel: ["vias e cartografia"]
prioridade: baixa
doi: "10.1109/cvpr.2018.00496"
pdf: "coleta/P37_Bastani2018_RoadTracer-Automatic-Extraction-of-Road-Networks-From-Aerial.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 31
sensores: ["[[Imagens aéreas-VHR|Imagens aéreas/VHR]]", "[[Planet (mosaicos e cenas)]]"]
tarefas: ["[[Vias-estradas|Vias/estradas]]", "[[Edificações]]"]
metodos: []
datasets: ["[[OpenStreetMap]]"]
metricas: ["[[Precisão-Recall|Precisão/Recall]]", "[[IoU - mIoU|IoU / mIoU]]"]
ferramentas: []
etapas_pipeline: ["[[E09 Pós-processamento e eventos|E09]]"]
status_leitura: não lido
tags: [artigo, secao/D, prioridade/baixa, etapa/E09]
---

# P37 — RoadTracer: Automatic Extraction of Road Networks From Aerial Images

**Favyen Bastani, Songtao He, Sofiane Abbar** · 2018 · Artigo · IEEE Computer Society Conference on Computer Vision and Pattern Recogn · [publicação](https://openaccess.thecvf.com/content_cvpr_2018/html/Bastani_RoadTracer_Automatic_Extraction_CVPR_2018_paper.html) · [PDF](../../coleta/P37_Bastani2018_RoadTracer-Automatic-Extraction-of-Road-Networks-From-Aerial.pdf)

Seção: **Vias, redes viárias e cartografia prévia** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Uso proposto:** fundamentar avaliação de conectividade, além de sobreposição de pixels.
- **Código:** https://roadmaps.csail.mit.edu/roadtracer/
- **Métricas usadas:** [[Precisão-Recall|Precisão/Recall]], [[IoU - mIoU|IoU / mIoU]]
- **Dados/benchmarks citados:** [[OpenStreetMap]]

## Método e dados (da revisão original)

- **Método:** extração da rede viária como estrutura conectada.

## Limites e cuidados

- extração em uma data não é detecção temporal; imagens e escalas distintas de Planet.

## Contextos de uso no projeto

- Etapas do pipeline: [[E09 Pós-processamento e eventos|E09]]
- Tarefas: [[Vias-estradas|Vias/estradas]], [[Edificações]]
- Sensores/produtos: [[Imagens aéreas-VHR|Imagens aéreas/VHR]], [[Planet (mosaicos e cenas)]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Imagens aéreas-VHR\|Imagens aéreas/VHR]] | 17 |
| sensor | [[Planet (mosaicos e cenas)]] | 1 |
| dataset | [[OpenStreetMap]] | 8 |
| metrica | [[Precisão-Recall\|Precisão/Recall]] | 18 |
| metrica | [[IoU - mIoU\|IoU / mIoU]] | 7 |
| tarefa | [[Vias-estradas\|Vias/estradas]] | 98 |
| tarefa | [[Edificações]] | 17 |

## Chunks

- Arquivo de chunks: [[P37 chunks]] (31 chunks; resumo 2, introdução 4, trabalhos relacionados 3, métodos 8, experimentos 9, dados 4, conclusão 1)
- Resumo: [[P37 chunks#^P37_c001|c001]], [[P37 chunks#^P37_c002|c002]]
- Dados / área de estudo: [[P37 chunks#^P37_c019|c019]], [[P37 chunks#^P37_c020|c020]]
- Método: [[P37 chunks#^P37_c010|c010]], [[P37 chunks#^P37_c011|c011]], [[P37 chunks#^P37_c012|c012]]
- Resultados numéricos: [[P37 chunks#^P37_c028|c028]]

## Relações

- Vizinhos por entidades em comum: [[P158 Febrita 2025|P158]], [[P60 Wang 2024|P60]], [[P40 Lee 2026|P40]], [[P104 McVicar 2023|P104]]

## Anotações

- 
