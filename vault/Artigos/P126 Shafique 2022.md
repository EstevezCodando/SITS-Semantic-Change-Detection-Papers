---
tipo: artigo
id: P126
titulo: "Deep Learning-Based Change Detection in Remote Sensing Images: A Review"
autores: "Ayesha Shafique, Guo Cao, Zia Uddin Khan, Muhammad Asad"
ano: 2022
secao: M
categoria: "Detecção de mudanças: métodos adicionais"
tipo_publicacao: "Revisão"
papel: ["método de mudança", "revisão"]
prioridade: baixa
doi: "10.3390/rs14040871"
pdf: "coleta/P126_Shafique2022_Deep-Learning-Based-Change-Detection-in-Remote-Sensing-Image.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 107
sensores: ["[[Sentinel-1-SAR|Sentinel-1/SAR]]", "[[Imagens aéreas-VHR|Imagens aéreas/VHR]]", "[[WorldView]]"]
tarefas: ["[[Detecção de mudança (binária)]]", "[[Séries temporais de imagens]]", "[[Edificações]]"]
metodos: ["[[U-Net]]", "[[Rede siamesa]]", "[[LSTM-ConvLSTM|LSTM/ConvLSTM]]", "[[Semi-auto-supervisionado|Semi/auto-supervisionado]]", "[[FCN]]", "[[SVM]]"]
datasets: ["[[HRSCD]]", "[[OSCD]]"]
metricas: ["[[Precisão-Recall|Precisão/Recall]]", "[[Kappa]]", "[[F1]]", "[[Acurácia global]]"]
ferramentas: []
etapas_pipeline: ["[[E04 Rotulagem e pré-anotação|E04]]", "[[E06 Modelos-base de cobertura|E06]]", "[[E07 Modelos de mudança em pares|E07]]", "[[E08 Modelos de série temporal|E08]]"]
status_leitura: não lido
tags: [artigo, secao/M, prioridade/baixa, etapa/E04, etapa/E06, etapa/E07, etapa/E08]
---

# P126 — Deep Learning-Based Change Detection in Remote Sensing Images: A Review

**Ayesha Shafique, Guo Cao, Zia Uddin Khan** · 2022 · Revisão · Remote Sensing · [publicação](https://doi.org/10.3390/rs14040871) · [PDF](../../coleta/P126_Shafique2022_Deep-Learning-Based-Change-Detection-in-Remote-Sensing-Image.pdf)

Seção: **Detecção de mudanças: métodos adicionais** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Relevância:** Revisão de detecção de mudanças por DL em sensoriamento remoto.
- **Revisão:** usar para expandir a bibliografia por rastreamento de referências (família de arquitetura, tipo de mudança).
- **Código:** https://github.com/yolalala/RS-source
- **Receita de treino extraída:** função de perda — `cross-entropy loss function, which allows using prior`; aumento de dados — `data augmentation` (confirmar nos chunks).
- **Métricas usadas:** [[Precisão-Recall|Precisão/Recall]], [[Kappa]], [[F1]], [[Acurácia global]]
- **Dados/benchmarks citados:** [[HRSCD]], [[OSCD]]

## Limites e cuidados

- Conferir resolução, bandas, região e rótulos antes de transferir resultados; síntese baseada em registro e metadados.

## Contextos de uso no projeto

- Etapas do pipeline: [[E04 Rotulagem e pré-anotação|E04]], [[E06 Modelos-base de cobertura|E06]], [[E07 Modelos de mudança em pares|E07]], [[E08 Modelos de série temporal|E08]]
- Tarefas: [[Detecção de mudança (binária)]], [[Séries temporais de imagens]], [[Edificações]]
- Sensores/produtos: [[Sentinel-1-SAR|Sentinel-1/SAR]], [[Imagens aéreas-VHR|Imagens aéreas/VHR]], [[WorldView]]
- Métodos: [[U-Net]], [[Rede siamesa]], [[LSTM-ConvLSTM|LSTM/ConvLSTM]], [[Semi-auto-supervisionado|Semi/auto-supervisionado]], [[FCN]], [[SVM]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Sentinel-1-SAR\|Sentinel-1/SAR]] | 70 |
| sensor | [[Imagens aéreas-VHR\|Imagens aéreas/VHR]] | 48 |
| sensor | [[WorldView]] | 10 |
| dataset | [[HRSCD]] | 3 |
| dataset | [[OSCD]] | 2 |
| metodo | [[U-Net]] | 23 |
| metodo | [[Rede siamesa]] | 18 |
| metodo | [[LSTM-ConvLSTM\|LSTM/ConvLSTM]] | 17 |
| metodo | [[Semi-auto-supervisionado\|Semi/auto-supervisionado]] | 17 |
| metodo | [[FCN]] | 14 |
| metodo | [[SVM]] | 13 |
| metrica | [[Precisão-Recall\|Precisão/Recall]] | 27 |
| metrica | [[Kappa]] | 14 |
| metrica | [[F1]] | 11 |
| metrica | [[Acurácia global]] | 11 |
| tarefa | [[Detecção de mudança (binária)]] | 69 |
| tarefa | [[Séries temporais de imagens]] | 22 |
| tarefa | [[Edificações]] | 15 |

## Chunks

- Arquivo de chunks: [[P126 chunks]] (107 chunks; resumo 3, introdução 9, dados 31, métodos 52, experimentos 9, discussão 1, conclusão 2)
- Resumo: [[P126 chunks#^P126_c001|c001]], [[P126 chunks#^P126_c002|c002]]
- Dados / área de estudo: [[P126 chunks#^P126_c013|c013]], [[P126 chunks#^P126_c014|c014]]
- Método: [[P126 chunks#^P126_c038|c038]], [[P126 chunks#^P126_c039|c039]], [[P126 chunks#^P126_c046|c046]]
- Hiperparâmetros / treino: [[P126 chunks#^P126_c061|c061]], [[P126 chunks#^P126_c062|c062]], [[P126 chunks#^P126_c063|c063]]
- Limitações / discussão: [[P126 chunks#^P126_c100|c100]]

## Relações

- Vizinhos por entidades em comum: [[P23 Daudt 2018|P23]], [[P28 Chen 2024|P28]], [[P18 Daudt 2019|P18]], [[P49 Lei 2026|P49]]

## Anotações

- 
