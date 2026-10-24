---
tipo: artigo
id: P17
titulo: "Urban Change Forecasting from Satellite Images"
autores: "Nando Metzger, Mehmet Özgür Türkoglu, Rodrigo Caye Daudt, Jan Dirk Wegner"
ano: 2023
secao: B
categoria: "Séries temporais, edificações e transições semânticas"
tipo_publicacao: "Artigo"
papel: ["benchmark/método temporal"]
prioridade: baixa
doi: "10.1007/s41064-023-00258-8"
pdf: "coleta/P17_Metzger2023_Urban-Change-Forecasting-from-Satellite-Images.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 26
sensores: []
tarefas: ["[[Previsão-forecasting|Previsão/forecasting]]", "[[Edificações]]", "[[Detecção de mudança (binária)]]", "[[Classificação de cobertura]]"]
metodos: ["[[U-Net]]", "[[Rede siamesa]]", "[[Transfer learning]]"]
datasets: ["[[SpaceNet 7 (MUDS)]]"]
metricas: ["[[Precisão-Recall|Precisão/Recall]]", "[[F1]]"]
ferramentas: []
etapas_pipeline: ["[[E07 Modelos de mudança em pares|E07]]", "[[E08 Modelos de série temporal|E08]]"]
status_leitura: não lido
tags: [artigo, secao/B, prioridade/baixa, etapa/E07, etapa/E08]
---

# P17 — Urban Change Forecasting from Satellite Images

**Nando Metzger, Mehmet Özgür Türkoglu, Rodrigo Caye Daudt** · 2023 · Artigo · PFG – Journal of Photogrammetry Remote Sensing and Geoinformation Scie · [publicação](https://doi.org/10.1007/s41064-023-00258-8) · [PDF](../../coleta/P17_Metzger2023_Urban-Change-Forecasting-from-Satellite-Images.pdf)

Seção: **Séries temporais, edificações e transições semânticas** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Uso proposto:** extensão futura para previsão de expansão, depois de validar mudanças observadas.
- **Receita de treino extraída:** taxa de aprendizado — `learning rate of 10−4 `; batch size — `batch size of 16, except for the largest forecasti`; otimizador — `Adam optimizer (Kingma and Ba 2014) with def`; função de perda — `binary cross-entropy loss`; tamanho do patch — `224×224 pixel` (confirmar nos chunks).
- **Métricas usadas:** [[Precisão-Recall|Precisão/Recall]], [[F1]]
- **Dados/benchmarks citados:** [[SpaceNet 7 (MUDS)]]

## Método e dados (da revisão original)

- **Método/dados:** previsão de mudança urbana usando SpaceNet 7 e aprendizado com arquitetura siamesa/U-Net.

## Limites e cuidados

- **forecasting é previsão**, não evidência de que uma nova construção já existe.

## Contextos de uso no projeto

- Etapas do pipeline: [[E07 Modelos de mudança em pares|E07]], [[E08 Modelos de série temporal|E08]]
- Tarefas: [[Previsão-forecasting|Previsão/forecasting]], [[Edificações]], [[Detecção de mudança (binária)]], [[Classificação de cobertura]]
- Métodos: [[U-Net]], [[Rede siamesa]], [[Transfer learning]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| dataset | [[SpaceNet 7 (MUDS)]] | 5 |
| metodo | [[U-Net]] | 8 |
| metodo | [[Rede siamesa]] | 8 |
| metodo | [[Transfer learning]] | 5 |
| metrica | [[Precisão-Recall\|Precisão/Recall]] | 33 |
| metrica | [[F1]] | 11 |
| tarefa | [[Previsão-forecasting\|Previsão/forecasting]] | 72 |
| tarefa | [[Edificações]] | 43 |
| tarefa | [[Detecção de mudança (binária)]] | 20 |
| tarefa | [[Classificação de cobertura]] | 11 |

## Chunks

- Arquivo de chunks: [[P17 chunks]] (26 chunks; resumo 2, introdução 24)
- Resumo: [[P17 chunks#^P17_c001|c001]], [[P17 chunks#^P17_c002|c002]]
- Hiperparâmetros / treino: [[P17 chunks#^P17_c009|c009]], [[P17 chunks#^P17_c010|c010]], [[P17 chunks#^P17_c011|c011]]

## Relações

- Vizinhos por entidades em comum: [[P11 Etten 2021|P11]], [[P139 Benidir 2025|P139]], [[P132 Zhou 2025|P132]], [[P138 Zhang 2025|P138]]

## Anotações

- 
