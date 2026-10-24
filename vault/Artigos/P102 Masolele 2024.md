---
tipo: artigo
id: P102
titulo: "Mapping the diversity of land uses following deforestation across Africa"
autores: "Robert N. Masolele, Diego Marcos, Veronique De Sy, Itohan‐Osa Abu"
ano: 2024
secao: K
categoria: "Planet: aplicações adicionais"
tipo_publicacao: "Artigo"
papel: ["aplicação Planet"]
prioridade: baixa
doi: "10.1038/s41598-024-52138-9"
pdf: "coleta/P102_Masolele2024_Mapping-the-diversity-of-land-uses-following-deforestation-a.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 49
sensores: ["[[Planet NICFI]]", "[[Planet (mosaicos e cenas)]]", "[[Sentinel-1-SAR|Sentinel-1/SAR]]"]
tarefas: ["[[Desmatamento]]", "[[Classificação de cobertura]]", "[[Vias-estradas|Vias/estradas]]", "[[Mineração]]"]
metodos: ["[[Aprendizado ativo]]", "[[U-Net]]", "[[NDVI-índices|NDVI/índices]]"]
datasets: []
metricas: ["[[F1]]", "[[Precisão-Recall|Precisão/Recall]]"]
ferramentas: ["[[TensorFlow]]"]
etapas_pipeline: ["[[E06 Modelos-base de cobertura|E06]]", "[[E09 Pós-processamento e eventos|E09]]"]
status_leitura: não lido
tags: [artigo, secao/K, prioridade/baixa, etapa/E06, etapa/E09]
---

# P102 — Mapping the diversity of land uses following deforestation across Africa

**Robert N. Masolele, Diego Marcos, Veronique De Sy** · 2024 · Artigo · Scientific Reports · [publicação](https://doi.org/10.1038/s41598-024-52138-9) · [PDF](../../coleta/P102_Masolele2024_Mapping-the-diversity-of-land-uses-following-deforestation-a.pdf)

Seção: **Planet: aplicações adicionais** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Relevância:** Usos do solo após o desmatamento na África; útil para pensar a classe posterior à perda de floresta.
- **Receita de treino extraída:** taxa de aprendizado — `learning rate of 10−4 `; batch size — `batch size of 64, using Adam optimization with a l`; épocas — `200 epochs`; otimizador — `Adam optimization with a learning rate of 10`; função de perda — `focal loss has shown to perform well on data with ` (confirmar nos chunks).
- **Métricas usadas:** [[F1]], [[Precisão-Recall|Precisão/Recall]]

## Limites e cuidados

- Conferir resolução, bandas, região e rótulos antes de transferir resultados; síntese baseada em registro e metadados.

## Contextos de uso no projeto

- Etapas do pipeline: [[E06 Modelos-base de cobertura|E06]], [[E09 Pós-processamento e eventos|E09]]
- Tarefas: [[Desmatamento]], [[Classificação de cobertura]], [[Vias-estradas|Vias/estradas]], [[Mineração]]
- Sensores/produtos: [[Planet NICFI]], [[Planet (mosaicos e cenas)]], [[Sentinel-1-SAR|Sentinel-1/SAR]]
- Métodos: [[Aprendizado ativo]], [[U-Net]], [[NDVI-índices|NDVI/índices]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Planet NICFI]] | 17 |
| sensor | [[Planet (mosaicos e cenas)]] | 10 |
| sensor | [[Sentinel-1-SAR\|Sentinel-1/SAR]] | 8 |
| metodo | [[Aprendizado ativo]] | 14 |
| metodo | [[U-Net]] | 8 |
| metodo | [[NDVI-índices\|NDVI/índices]] | 4 |
| metrica | [[F1]] | 17 |
| metrica | [[Precisão-Recall\|Precisão/Recall]] | 6 |
| tarefa | [[Desmatamento]] | 158 |
| tarefa | [[Classificação de cobertura]] | 44 |
| tarefa | [[Vias-estradas\|Vias/estradas]] | 18 |
| tarefa | [[Mineração]] | 15 |
| ferramenta | [[TensorFlow]] | 4 |

## Resultados citados pelos autores (extraídos automaticamente)

> Specifically, the macro average F1-score improved from 43% with the original data to 54% after the first AL round and to 84% after the second round (Fig.
> The map has a users accuracy of 85%, producers accuracy of 84%, and F1-score of 85% (Fig.
> For detailed visualisation, the predicted output map of land use following deforestation is available at this website: producers accuracy of 84%, and F1-score of 85% (Fig.

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P102 chunks]] (49 chunks; resumo 9, resultados 8, métodos 15, discussão 17)
- Resumo: [[P102 chunks#^P102_c001|c001]], [[P102 chunks#^P102_c002|c002]]
- Método: [[P102 chunks#^P102_c018|c018]], [[P102 chunks#^P102_c019|c019]], [[P102 chunks#^P102_c020|c020]]
- Hiperparâmetros / treino: [[P102 chunks#^P102_c026|c026]]
- Resultados numéricos: [[P102 chunks#^P102_c010|c010]], [[P102 chunks#^P102_c011|c011]]
- Limitações / discussão: [[P102 chunks#^P102_c033|c033]], [[P102 chunks#^P102_c034|c034]]

## Relações

- Vizinhos por entidades em comum: [[P04 Wang 2024|P04]], [[P93 Wagner 2025|P93]], [[P08 Debus 2025|P08]], [[P03 Carter 2024|P03]]

## Anotações

- 
