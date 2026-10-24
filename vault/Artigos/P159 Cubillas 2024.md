---
tipo: artigo
id: P159
titulo: "Land Classification Plugin for QGIS Using Pix2Pix"
autores: "James Earl Cubillas, Reynard Torculas, Jessie Mayol, Paul Justine Bajao"
ano: 2024
secao: N
categoria: "GeoAI e QGIS"
tipo_publicacao: "Software"
papel: ["GeoAI/QGIS", "ferramenta"]
prioridade: baixa
doi: "10.5194/isprs-annals-x-5-2024-33-2024"
pdf: "coleta/P159_Cubillas2024_Land-Classification-Plugin-for-QGIS-Using-Pix2Pix.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 22
sensores: ["[[Landsat]]"]
tarefas: ["[[Classificação de cobertura]]"]
metodos: []
datasets: ["[[OpenStreetMap]]"]
metricas: ["[[Acurácia global]]"]
ferramentas: ["[[QGIS]]", "[[PyTorch]]", "[[GDAL - rasterio|GDAL / rasterio]]"]
etapas_pipeline: ["[[E11 Operação e atualização|E11]]"]
status_leitura: não lido
tags: [artigo, secao/N, prioridade/baixa, etapa/E11]
---

# P159 — Land Classification Plugin for QGIS Using Pix2Pix

**James Earl Cubillas, Reynard Torculas, Jessie Mayol** · 2024 · Software · ISPRS annals of the photogrammetry, remote sensing and spatial informa · [publicação](https://doi.org/10.5194/isprs-annals-x-5-2024-33-2024) · [PDF](../../coleta/P159_Cubillas2024_Land-Classification-Plugin-for-QGIS-Using-Pix2Pix.pdf)

Seção: **GeoAI e QGIS** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Relevância:** Plugin QGIS de classificação de cobertura com Pix2Pix (aplicado principalmente a Landsat).
- **Métricas usadas:** [[Acurácia global]]
- **Dados/benchmarks citados:** [[OpenStreetMap]]

## Limites e cuidados

- Conferir resolução, bandas, região e rótulos antes de transferir resultados; síntese baseada em registro e metadados.

## Contextos de uso no projeto

- Etapas do pipeline: [[E11 Operação e atualização|E11]]
- Tarefas: [[Classificação de cobertura]]
- Sensores/produtos: [[Landsat]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Landsat]] | 1 |
| dataset | [[OpenStreetMap]] | 2 |
| metrica | [[Acurácia global]] | 4 |
| tarefa | [[Classificação de cobertura]] | 25 |
| ferramenta | [[QGIS]] | 25 |
| ferramenta | [[PyTorch]] | 4 |
| ferramenta | [[GDAL - rasterio\|GDAL / rasterio]] | 4 |

## Resultados citados pelos autores (extraídos automaticamente)

> The accuracy assessment of the LCP demonstrated an overall accuracy of 83.40% across diverse land cover classes, indicating its efficacy in classification tasks.
> As depicted in Table 1, the overall accuracy attained by our pre-trained model stands at 83.40%.
> This result implies that our pre-trained model demonstrates a commendable accuracy in classifying pixels across diverse land cover classes compared to SCP with 69.20%.

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P159 chunks]] (22 chunks; resumo 2, introdução 3, dados 7, resultados 9, conclusão 1)
- Resumo: [[P159 chunks#^P159_c001|c001]], [[P159 chunks#^P159_c002|c002]]
- Dados / área de estudo: [[P159 chunks#^P159_c006|c006]], [[P159 chunks#^P159_c007|c007]]
- Resultados numéricos: [[P159 chunks#^P159_c018|c018]], [[P159 chunks#^P159_c019|c019]]

## Relações

- Vizinhos por entidades em comum: [[P55 Magidi 2024|P55]], [[P184 Ramadan 2022|P184]], [[P47 Stehman 2019|P47]], [[P42 Zhu 2014|P42]]

## Anotações

- 
