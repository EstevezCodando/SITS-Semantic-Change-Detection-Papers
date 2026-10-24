---
tipo: artigo
id: P158
titulo: "Evaluating AI-Driven Automated Map Digitization in QGIS"
autores: "Diana Febrita"
ano: 2025
secao: N
categoria: "GeoAI e QGIS"
tipo_publicacao: "Preprint"
papel: ["GeoAI/QGIS", "preprint"]
prioridade: baixa
doi: "10.48550/arXiv.2504.18777"
pdf: "coleta/P158_Febrita2025_Evaluating-AI-Driven-Automated-Map-Digitization-in-QGIS.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 15
sensores: []
tarefas: ["[[Edificações]]"]
metodos: []
datasets: ["[[OpenStreetMap]]"]
metricas: ["[[Precisão-Recall|Precisão/Recall]]", "[[F1]]", "[[IoU - mIoU|IoU / mIoU]]"]
ferramentas: ["[[QGIS]]", "[[GeoAI (opengeos)]]"]
etapas_pipeline: ["[[E11 Operação e atualização|E11]]"]
leitura_profunda: "[[LP P158 Febrita 2025]]"
status_leitura: lido (profundo)
tags: [artigo, secao/N, prioridade/baixa, etapa/E11]
---

# P158 — Evaluating AI-Driven Automated Map Digitization in QGIS

**Diana Febrita** · 2025 · Preprint · arXiv (Cornell University) · [publicação](https://doi.org/10.48550/arXiv.2504.18777) · [PDF](../../coleta/P158_Febrita2025_Evaluating-AI-Driven-Automated-Map-Digitization-in-QGIS.pdf)

Seção: **GeoAI e QGIS** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

> [!success] Leitura profunda concluída: [[LP P158 Febrita 2025]]

## O que reaproveitar

- **Lista de parâmetros que alteram muito o resultado** (resolução de processamento, sobreposição, remoção de segmentos pequenos) e a necessidade de **calibrar por área** antes de comparar modelos.
- **Protocolo de casamento por IoU > 0,5** para contagem de edificações e relatório de TP/FP/FN, em linha com o SCOT (IoU > 0,25) de [[P10 Etten 2021]].
- Reforça: **recall alto com precisão média** é adequado para triagem, e a revisão humana corrige os falsos positivos ([[E11 Operação e atualização]]).

### Extraído automaticamente

- **Relevância:** Avaliação do Deepness para digitalização automática de mapas, comparada ao OpenStreetMap (F1).
- **Métricas usadas:** [[Precisão-Recall|Precisão/Recall]], [[F1]], [[IoU - mIoU|IoU / mIoU]]
- **Dados/benchmarks citados:** [[OpenStreetMap]]

## Limites e cuidados

- Conferir resolução, bandas, região e rótulos antes de transferir resultados; síntese baseada em registro e metadados.

## Contextos de uso no projeto

- Etapas do pipeline: [[E11 Operação e atualização|E11]]
- Tarefas: [[Edificações]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| dataset | [[OpenStreetMap]] | 28 |
| metrica | [[Precisão-Recall\|Precisão/Recall]] | 16 |
| metrica | [[F1]] | 10 |
| metrica | [[IoU - mIoU\|IoU / mIoU]] | 7 |
| tarefa | [[Edificações]] | 77 |
| ferramenta | [[QGIS]] | 12 |
| ferramenta | [[GeoAI (opengeos)]] | 3 |

## Resultados citados pelos autores (extraídos automaticamente)

> Keywords: GeoAI, Deep Neural Remote Sensing, Deepness, QGIS, F1-score 1st Test Resolution = 300 cm/px Percentage Tiles Overlap = 0% 2nd Test Resolution = 300 cm/px Percentage Tiles Overlap = 12% 3rd Test Resolution = 300 cm/px Per
> Precision increased from 36.82% in the first test and 51.71% in the second test to 70.85% in the third test.
> Meanwhile, recall reached 88.12% in the final test.

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P158 chunks]] (15 chunks; resumo 2, introdução 2, métodos 7, resultados 3, conclusão 1)
- Resumo: [[P158 chunks#^P158_c001|c001]], [[P158 chunks#^P158_c002|c002]]
- Método: [[P158 chunks#^P158_c005|c005]], [[P158 chunks#^P158_c006|c006]], [[P158 chunks#^P158_c007|c007]]
- Resultados numéricos: [[P158 chunks#^P158_c013|c013]], [[P158 chunks#^P158_c014|c014]]

## Relações

- Vizinhos por entidades em comum: [[P37 Bastani 2018|P37]], [[P95 Huang 2022|P95]], [[P60 Wang 2024|P60]], [[P159 Cubillas 2024|P159]]

## Anotações

- 
