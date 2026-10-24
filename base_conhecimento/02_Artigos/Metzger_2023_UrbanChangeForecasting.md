---
tipo: artigo
id_origem: P17
titulo: "Urban Change Forecasting from Satellite Images"
ano: 2023
autores: ["Nando Metzger", "Mehmet Özgür Türkoglu", "Rodrigo Caye Daudt", "Jan Dirk Wegner", "Konrad Schindler"]
doi: "10.1007/s41064-023-00258-8"
arquivo_fonte: "coleta/P17_Metzger2023_Urban-Change-Forecasting-from-Satellite-Images.pdf"
markdown_fonte: "output/pdf/P17_Metzger2023_Urban-Change-Forecasting-from-Satellite-Images/document.md"
paginas: 10
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[Edificacoes|Edificações e urbanização]]"]
sensores: []
conjuntos_dados: ["[[SpaceNet7_MUDS|SpaceNet 7 / MUDS]]"]
metodos: ["[[UNet|U-Net]]", "[[RedeSiamesa|Redes siamesas]]", "[[TransferLearning|Aprendizado por transferência]]", "[[CNN|Redes convolucionais (CNN)]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]", "[[PatchesTiles|Recorte em patches/tiles]]"]
validacao: ["[[Desbalanceamento|Desbalanceamento de classes]]", "[[DivisaoTreinoTeste|Divisão treino/validação/teste]]", "[[PrecisaoRecall|Precisão e recall]]", "[[F1|F1]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Metzger 2023 — Urban Change Forecasting from Satellite Images

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Nando Metzger, Mehmet Özgür Türkoglu, Rodrigo Caye Daudt, Jan Dirk Wegner et al. (2023). Urban Change Forecasting from Satellite Images. PFG – Journal of Photogrammetry Remote Sensing and Geoinformation Science. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1007/s41064-023-00258-8
- **Arquivo de origem:** `coleta/P17_Metzger2023_Urban-Change-Forecasting-from-Satellite-Images.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P17_Metzger2023_Urban-Change-Forecasting-from-Satellite-Images/document.md` — 10 páginas, 21 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Forecasting where and when new buildings will emerge is a rather unexplored topic, but one that is very useful in many disciplines such as urban planning, agriculture, resource management, and even autonomous flying. In the present work, we present a method that accomplishes this task with a deep neural network and a custom pretraining procedure. In Stage 1, a U-Net backbone is pretrained within a Siamese network architecture that aims to solve a (building) change detection task. In Stage 2, the backbone is repurposed to forecast the emergence of new buildings based solely on one image acquired before its construction. Furthermore, we also present a model that forecasts the time range within which the change will occur. We validate our approach using the SpaceNet7 dataset, which covers an area of 960 km at 24 points in time across 2 years. In our experiments, we found that our proposed p…

- “In the present work, we present a method that accomplishes this task with a deep neural network and a custom pretraining procedure.” (p. 1, seção Abstract)
- “We develop a 2-stage training strategy (as shown in Fig.” (p. 1, seção 60 locations with a total extent of 960 km and a ground)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “We validate our approach using the SpaceNet7 dataset, which covers an area of 960 km at 24 points in time across 2 years.” (p. 1, seção Abstract)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- conjunto de dados **SpaceNet 7 (MUDS)**: 5 ocorrências (p. 1, 4, 9)
- resolução mencionada: 4 m (p. 1)
- “For example, when we want to forecast for the smallest possible range (i.e., one month), the subset of pairs that are one month apart contains 5000 samples, whereas, for the largest forecasting range of 24 months, we only obtain 200 samples” (p. 5, seção 60 locations with a total extent of 960 km and a ground)
- “The predicted score p̂ e is a measure of the likelihood that a given pixel will undergo an “early change”, and is trained with a cross-entropy loss w.r.t. the ground truth label y e (1 for early change, 0 for late change).” (p. 3, seção 60 locations with a total extent of 960 km and a ground)
- “The dataset also contains a set of manually labeled building footprints, where each image of the time series is labeled individually.” (p. 5, seção 60 locations with a total extent of 960 km and a ground)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 7 ocorrências (p. 1, 3, 5, 6, 7)
- **Recorte em patches/tiles**: 4 ocorrências (p. 4, 5)
- **Mosaicos e compostos**: 2 ocorrências (p. 5)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **U-Net**: 7 ocorrências (p. 1, 2, 3)
- método/família **Rede siamesa**: 7 ocorrências (p. 1, 2, 3)
- método/família **Transfer learning**: 4 ocorrências (p. 3, 5, 6, 7)
- método/família **CNN**: 3 ocorrências (p. 1, 2, 6)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 10 [−] ” (p. 4)
- batch: “batch size of 16, except for the largest forecasti” (p. 4)
- otimizador: “Adam optimizer (Kingma and Ba 2014) with def” (p. 4)
- perda: “binary cross-entropy loss” (p. 3)
- tamanho do patch: “224 × 224 pixel” (p. 5)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Desbalanceamento**: 8 ocorrências (p. 4, 5, 6, 7)
- **Conjuntos treino/val/teste**: 3 ocorrências (p. 4, 5)
- métrica **Precisão/Recall**: 28 ocorrências (p. 4, 6, 7)
- métrica **F1**: 10 ocorrências (p. 4, 5, 6, 7, 9)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “The curve exhibits a bias toward favoring recall over precision—meaning, a significant amount of recall must be relinquished to see an increase in precision larger than 20%.” (p. 6, seção 60 locations with a total extent of 960 km and a g)
- “The results show that our custom pretraining approach indeed improves performance by 3% in both accuracy and F1 score, further supporting the effectiveness of our proposed methodology.” (p. 7, seção 60 locations with a total extent of 960 km and a g)
- “We note that the “early” class exhibits a precision of 60.0%, while the precision of the “late” class amounts to 68.2%, suggesting that the later changes might be easier to detect than the earlier ones.” (p. 7, seção 60 locations with a total extent of 960 km and a g)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “The limitation to a fixed forecasting range comes with a disadvantage, namely that one can only use a subset of the overall data for training that has the appropriate temporal spacing.” (p. 3, seção 60 locations with a total extent of 960 km and a ground)
- “This is not surprising given the inherent ambiguity of the task— from the early earthworks and preparations it is not possible to determine the precise outlines of the future buildings.” (p. 6, seção 60 locations with a total extent of 960 km and a ground)
- “Understandably, our model struggles when there is no indication of imminent construction at all— producing false negatives (blue marker).” (p. 8, seção 60 locations with a total extent of 960 km and a ground)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/nandometzger/ChangePrediction (p. 4)
- URL citada: https://github.com/nandometzger/ChangePrediction (p. 4)
- declaração: “Data Availability The SpaceNet7 dataset is publicly available (Van Etten et al.” (p. 9)
- declaração: “Code Availability [The code is available at https://​github.​com/​nando​](https://github.com/nandometzger/ChangePrediction) [metzg​er/​Chang​ePred​iction.](https://github.com/nandometzger/ChangePrediction) Declarations Conflict of Interest ” (p. 9)
- hiperparâmetros **não detectados** automaticamente: épocas/iterações (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- emprega conjunto de dados: [[SpaceNet7_MUDS|SpaceNet 7 / MUDS]] — 5 ocorrências (p. 1, 4, 9)
- utiliza método: [[UNet|U-Net]] — 7 ocorrências (p. 1, 2, 3)
- utiliza método: [[RedeSiamesa|Redes siamesas]] — 7 ocorrências (p. 1, 2, 3)
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 4 ocorrências (p. 3, 5, 6, 7)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 3 ocorrências (p. 1, 2, 6)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 28 ocorrências (p. 4, 6, 7)
- é avaliado por: [[F1|F1]] — 10 ocorrências (p. 4, 5, 6, 7, 9)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 7 ocorrências (p. 1, 3, 5, 6, 7)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 4 ocorrências (p. 4, 5)
- adota desenho de validação: [[Desbalanceamento|Desbalanceamento de classes]] — 8 ocorrências (p. 4, 5, 6, 7)
- adota desenho de validação: [[DivisaoTreinoTeste|Divisão treino/validação/teste]] — 3 ocorrências (p. 4, 5)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
