---
tipo: artigo
id: P01
titulo: "Mapping Tropical Forest Cover and Deforestation with Planet NICFI Satellite Images and Deep Learning in Mato Grosso State (Brazil) from 2015 to 2021"
autores: "Fabien Hubert Wagner, Ricardo Dalagnol, Celso H. L. Silva, Griffin Carter"
ano: 2023
secao: A
categoria: "Planet: aplicações diretas"
tipo_publicacao: "Artigo"
papel: ["aplicação Planet"]
prioridade: alta
doi: "10.3390/rs15020521"
pdf: "coleta/P01_Wagner2023_Mapping-Tropical-Forest-Cover-and-Deforestation-with-Planet-.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 46
sensores: ["[[Planet (mosaicos e cenas)]]", "[[Planet NICFI]]", "[[Landsat]]"]
tarefas: ["[[Desmatamento]]", "[[Séries temporais de imagens]]"]
metodos: ["[[U-Net]]"]
datasets: ["[[PRODES]]", "[[Global Forest Change (Hansen)]]"]
metricas: ["[[F1]]"]
ferramentas: ["[[TensorFlow]]"]
etapas_pipeline: ["[[E06 Modelos-base de cobertura|E06]]"]
status_leitura: não lido
tags: [artigo, secao/A, prioridade/alta, etapa/E06]
---

# P01 — Mapping Tropical Forest Cover and Deforestation with Planet NICFI Satellite Images and Deep Learning in Mato Grosso State (Brazil) from 2015 to 2021

**Fabien Hubert Wagner, Ricardo Dalagnol, Celso H. L. Silva** · 2023 · Artigo · Remote Sensing · [publicação](https://doi.org/10.3390/rs15020521) · [PDF](../../coleta/P01_Wagner2023_Mapping-Tropical-Forest-Cover-and-Deforestation-with-Planet-.pdf)

Seção: **Planet: aplicações diretas** · Prioridade: **alta** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Uso proposto:** principal ponto de partida para a frente de supressão vegetal no Brasil.
- **Receita de treino extraída:** taxa de aprendizado — `learning rate of 0.0001 was used`; batch size — `batch size of 256 images and the model with the be`; épocas — `20000 epochs`; função de perda — `binary cross-entropy and Dice coefficient-related lo`; tamanho do patch — `256 × 256 pixel` (confirmar nos chunks).
- **Métricas usadas:** [[F1]]
- **Dados/benchmarks citados:** [[PRODES]], [[Global Forest Change (Hansen)]]

## Método e dados (da revisão original)

- **Método/dados:** U-Net para cobertura arbórea e acompanhamento de perda usando Planet NICFI, aproximadamente 5 m.

## Limites e cuidados

- cobertura arbórea/não arbórea não distingue automaticamente construções, ruas e todas as formações vegetais; observar a mudança histórica da cadência NICFI.

## Contextos de uso no projeto

- Etapas do pipeline: [[E06 Modelos-base de cobertura|E06]]
- Tarefas: [[Desmatamento]], [[Séries temporais de imagens]]
- Sensores/produtos: [[Planet (mosaicos e cenas)]], [[Planet NICFI]], [[Landsat]]
- Métodos: [[U-Net]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Planet (mosaicos e cenas)]] | 79 |
| sensor | [[Planet NICFI]] | 27 |
| sensor | [[Landsat]] | 8 |
| dataset | [[PRODES]] | 15 |
| dataset | [[Global Forest Change (Hansen)]] | 6 |
| metodo | [[U-Net]] | 27 |
| metrica | [[F1]] | 3 |
| tarefa | [[Desmatamento]] | 203 |
| tarefa | [[Séries temporais de imagens]] | 13 |
| ferramenta | [[TensorFlow]] | 4 |

## Resultados citados pelos autores (extraídos automaticamente)

> The high-resolution data product showed relatively consistent agreement with the official deforestation map from Brazil (67.2%) but deviated significantly from year of fores 3.1 Tree cover validation with independent validation sa
> overall, based on the LiDAR data, it is observed that our tree cover model segment trees with a very high accuracy, that is, 98% non forest pixels have height below 5 m, and around 95 % of the tree cover pixels have height above 5
> our tree cover model segment trees with a very high accuracy, that is, 98% non forest pixels have height below 5 m, and around 95 % of the tree cover pixels have height above 5 m.

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P01 chunks]] (46 chunks; resumo 2, introdução 17, resultados 16, discussão 9, conclusão 2)
- Resumo: [[P01 chunks#^P01_c001|c001]], [[P01 chunks#^P01_c002|c002]]
- Hiperparâmetros / treino: [[P01 chunks#^P01_c007|c007]], [[P01 chunks#^P01_c014|c014]], [[P01 chunks#^P01_c016|c016]]
- Resultados numéricos: [[P01 chunks#^P01_c020|c020]], [[P01 chunks#^P01_c021|c021]]
- Limitações / discussão: [[P01 chunks#^P01_c036|c036]], [[P01 chunks#^P01_c037|c037]]

## Relações

- Vizinhos por entidades em comum: [[P04 Wang 2024|P04]], [[P117 Doblas 2022|P117]], [[P03 Carter 2024|P03]], [[P91 Zhang 2023|P91]]

## Anotações

- 
