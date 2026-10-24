---
tipo: artigo
id: P52
titulo: "Very High Resolution Object-Based Land Use-Land Cover Urban Classification Using Extreme Gradient Boosting"
autores: "Stefanos Georganos, Taïs Grippa, Sabine G. Vanhuysse, Moritz Lennert"
ano: 2018
secao: F
categoria: "XGBoost, LightGBM e atributos"
tipo_publicacao: "Artigo"
papel: ["baseline tabular (ML)"]
prioridade: média
doi: "10.1109/LGRS.2018.2803259"
pdf: "coleta/P52_Georganos2018_Very-High-Resolution-Object-Based-Land-Use-Land-Cover-Urban-.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 17
sensores: ["[[Imagens aéreas-VHR|Imagens aéreas/VHR]]", "[[Planet (mosaicos e cenas)]]"]
tarefas: []
metodos: ["[[SVM]]", "[[OBIA - objetos|OBIA / objetos]]", "[[XGBoost]]", "[[Random Forest]]", "[[SAM]]"]
datasets: []
metricas: ["[[Acurácia global]]"]
ferramentas: []
etapas_pipeline: ["[[E05 Atributos e representações|E05]]", "[[E06 Modelos-base de cobertura|E06]]"]
status_leitura: não lido
tags: [artigo, secao/F, prioridade/média, etapa/E05, etapa/E06]
---

# P52 — Very High Resolution Object-Based Land Use-Land Cover Urban Classification Using Extreme Gradient Boosting

**Stefanos Georganos, Taïs Grippa, Sabine G. Vanhuysse** · 2018 · Artigo · IEEE Geoscience and Remote Sensing Letters · [publicação](https://doi.org/10.1109/LGRS.2018.2803259) · [PDF](../../coleta/P52_Georganos2018_Very-High-Resolution-Object-Based-Land-Use-Land-Cover-Urban-.pdf)

Seção: **XGBoost, LightGBM e atributos** · Prioridade: **média** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Uso proposto:** fundamento para classificar segmentos por espectro, textura e forma.
- **Código:** https://github.com/ANAGEO/Xgboost_FeatureSelection_Opt
- **Receita de treino extraída:** taxa de aprendizado — `learning rate, tree depth and subsampling of training data and ` (confirmar nos chunks).
- **Métricas usadas:** [[Acurácia global]]

## Método e dados (da revisão original)

- **Método:** XGBoost por objetos, seleção de atributos e parametrização bayesiana; comparação com RF/SVM em ambientes urbanos.

## Limites e cuidados

- classificação urbana VHR, sem demonstração de catálogo temporal Planet. Substituir a segmentação original por SAM constitui um novo experimento.

## Contextos de uso no projeto

- Etapas do pipeline: [[E05 Atributos e representações|E05]], [[E06 Modelos-base de cobertura|E06]]
- Sensores/produtos: [[Imagens aéreas-VHR|Imagens aéreas/VHR]], [[Planet (mosaicos e cenas)]]
- Métodos: [[SVM]], [[OBIA - objetos|OBIA / objetos]], [[XGBoost]], [[Random Forest]], [[SAM]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Imagens aéreas-VHR\|Imagens aéreas/VHR]] | 8 |
| sensor | [[Planet (mosaicos e cenas)]] | 1 |
| metodo | [[SVM]] | 26 |
| metodo | [[OBIA - objetos\|OBIA / objetos]] | 8 |
| metodo | [[XGBoost]] | 4 |
| metodo | [[Random Forest]] | 3 |
| metodo | [[SAM]] | 1 |
| metrica | [[Acurácia global]] | 8 |

## Resultados citados pelos autores (extraídos automaticamente)

> The highest recorded accuracy (OA=82.10%) is obtained when Xgboost trained with the full set of features.
> The highest recorded accuracy (OA=82.10%) is obtained when Xgboost trained with the full set of features.
> SVM and RF largely underperformed in comparison to Xgboost with quasi 5% and 2% differences in OA.

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P52 chunks]] (17 chunks; resumo 1, introdução 10, resultados 3, discussão 2, conclusão 1)
- Resumo: [[P52 chunks#^P52_c001|c001]]
- Hiperparâmetros / treino: [[P52 chunks#^P52_c011|c011]]
- Resultados numéricos: [[P52 chunks#^P52_c012|c012]], [[P52 chunks#^P52_c013|c013]], [[P52 chunks#^P52_c014|c014]]
- Limitações / discussão: [[P52 chunks#^P52_c015|c015]], [[P52 chunks#^P52_c016|c016]]

## Relações

- Relação explícita: [[P51 Rodrigues 2025|P51]]
- Vizinhos por entidades em comum: [[P51 Rodrigues 2025|P51]], [[P53 Tianqi 2016|P53]], [[P80 Feng 2025|P80]], [[P60 Wang 2024|P60]]

## Anotações

- 
