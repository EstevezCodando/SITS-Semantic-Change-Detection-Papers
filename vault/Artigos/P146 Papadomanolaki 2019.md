---
tipo: artigo
id: P146
titulo: "Detecting Urban Changes with Recurrent Neural Networks from Multitemporal Sentinel-2 Data"
autores: "Maria Papadomanolaki, Sagar Verma, Maria Vakalopoulou, Siddharth Gupta"
ano: 2019
secao: M
categoria: "Detecção de mudanças: métodos adicionais"
tipo_publicacao: "Artigo"
papel: ["método de mudança"]
prioridade: baixa
doi: "10.1109/igarss.2019.8900330"
pdf: "coleta/P146_Papadomanolaki2019_Detecting-Urban-Changes-with-Recurrent-Neural-Networks-from-.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 15
sensores: ["[[Sentinel-2]]"]
tarefas: ["[[Detecção de mudança (binária)]]"]
metodos: ["[[LSTM-ConvLSTM|LSTM/ConvLSTM]]", "[[U-Net]]", "[[FCN]]"]
datasets: ["[[OSCD]]"]
metricas: ["[[Precisão-Recall|Precisão/Recall]]", "[[F1]]", "[[Acurácia global]]"]
ferramentas: []
etapas_pipeline: ["[[E07 Modelos de mudança em pares|E07]]", "[[E08 Modelos de série temporal|E08]]"]
status_leitura: não lido
tags: [artigo, secao/M, prioridade/baixa, etapa/E07, etapa/E08]
---

# P146 — Detecting Urban Changes with Recurrent Neural Networks from Multitemporal Sentinel-2 Data

**Maria Papadomanolaki, Sagar Verma, Maria Vakalopoulou** · 2019 · Artigo · IEEE International Geoscience and Remote Sensing Symposium (IGARSS) · [publicação](https://doi.org/10.1109/igarss.2019.8900330) · [PDF](../../coleta/P146_Papadomanolaki2019_Detecting-Urban-Changes-with-Recurrent-Neural-Networks-from-.pdf)

Seção: **Detecção de mudanças: métodos adicionais** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Relevância:** Mudança urbana com redes recorrentes em séries Sentinel-2 (OSCD).
- **Receita de treino extraída:** taxa de aprendizado — `learning rate values were equal to 64 and 0.0001 respectively`; batch size — `batch size and learning rate values were equal to `; otimizador — `Adam while batch size and learning rate valu`; aumento de dados — `data augmentation approach to enrich the training samples that contain change` (confirmar nos chunks).
- **Métricas usadas:** [[Precisão-Recall|Precisão/Recall]], [[F1]], [[Acurácia global]]
- **Dados/benchmarks citados:** [[OSCD]]

## Limites e cuidados

- Conferir resolução, bandas, região e rótulos antes de transferir resultados; síntese baseada em registro e metadados.

## Contextos de uso no projeto

- Etapas do pipeline: [[E07 Modelos de mudança em pares|E07]], [[E08 Modelos de série temporal|E08]]
- Tarefas: [[Detecção de mudança (binária)]]
- Sensores/produtos: [[Sentinel-2]]
- Métodos: [[LSTM-ConvLSTM|LSTM/ConvLSTM]], [[U-Net]], [[FCN]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Sentinel-2]] | 5 |
| dataset | [[OSCD]] | 12 |
| metodo | [[LSTM-ConvLSTM\|LSTM/ConvLSTM]] | 22 |
| metodo | [[U-Net]] | 11 |
| metodo | [[FCN]] | 3 |
| metrica | [[Precisão-Recall\|Precisão/Recall]] | 10 |
| metrica | [[F1]] | 7 |
| metrica | [[Acurácia global]] | 3 |
| tarefa | [[Detecção de mudança (binária)]] | 12 |

## Resultados citados pelos autores (extraídos automaticamente)

> All the developed models during the validation phase have scored an overall accuracy of more than 95%, while the use of LSTMs and further temporal information, boost the F1 rate of the change class by an additional 1.5%.

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P146 chunks]] (15 chunks; resumo 2, introdução 3, métodos 2, dados 4, experimentos 2, conclusão 2)
- Resumo: [[P146 chunks#^P146_c001|c001]], [[P146 chunks#^P146_c002|c002]]
- Dados / área de estudo: [[P146 chunks#^P146_c008|c008]], [[P146 chunks#^P146_c009|c009]]
- Método: [[P146 chunks#^P146_c006|c006]], [[P146 chunks#^P146_c007|c007]]
- Hiperparâmetros / treino: [[P146 chunks#^P146_c010|c010]], [[P146 chunks#^P146_c011|c011]]
- Resultados numéricos: [[P146 chunks#^P146_c012|c012]], [[P146 chunks#^P146_c013|c013]]

## Relações

- Vizinhos por entidades em comum: [[P23 Daudt 2018|P23]], [[P150 Wu 2023|P150]], [[P126 Shafique 2022|P126]], [[P15 Garnot 2021|P15]]

## Anotações

- 
