---
tipo: artigo
id_origem: P113
titulo: "Deforestation detection using deep learning-based semantic segmentation techniques: a systematic review"
ano: 2024
autores: ["Imran Md Jelas", "Mohd Asyraf Zulkifley", "Mardina Abdullah", "Martin Spraggon"]
doi: "10.3389/ffgc.2024.1300060"
arquivo_fonte: "coleta/P113_Jelas2024_Deforestation-detection-using-deep-learning-based-semantic-s.pdf"
markdown_fonte: "output/pdf/P113_Jelas2024_Deforestation-detection-using-deep-learning-based-semantic-s/document.md"
paginas: 24
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Desmatamento|Desmatamento]]", "[[SegmentacaoSemantica|Segmentação semântica]]"]
sensores: ["[[UAV|UAV / drones]]", "[[Landsat|Landsat]]", "[[Sentinel2|Sentinel-2]]"]
conjuntos_dados: ["[[PRODES|PRODES (INPE)]]", "[[DETER|DETER (INPE)]]"]
metodos: ["[[UNet|U-Net]]", "[[CNN|Redes convolucionais (CNN)]]", "[[RandomForest|Random Forest]]", "[[SVM|SVM]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]", "[[PatchesTiles|Recorte em patches/tiles]]", "[[AumentoDados|Aumento de dados]]"]
validacao: ["[[Generalizacao|Generalização e domain shift]]", "[[DivisaoTreinoTeste|Divisão treino/validação/teste]]", "[[PrecisaoRecall|Precisão e recall]]", "[[F1|F1]]", "[[IoU|IoU / mIoU]]", "[[AcuraciaGlobal|Acurácia global (OA)]]"]
ferramentas: ["[[QGIS|QGIS]]", "[[GoogleEarthEngine|Google Earth Engine]]"]
tags: [artigo, leitura/automatica]
---

# Jelas 2024 — Deforestation detection using deep learning-based semantic segmentation techniques: a systematic review

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Imran Md Jelas, Mohd Asyraf Zulkifley, Mardina Abdullah, Martin Spraggon (2024). Deforestation detection using deep learning-based semantic segmentation techniques: a systematic review. Frontiers in Forests and Global Change. Tipo no catálogo: Revisão.
- **DOI/URL:** https://doi.org/10.3389/ffgc.2024.1300060
- **Arquivo de origem:** `coleta/P113_Jelas2024_Deforestation-detection-using-deep-learning-based-semantic-s.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P113_Jelas2024_Deforestation-detection-using-deep-learning-based-semantic-s/document.md` — 24 páginas, 15 recortes de figuras, 6 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “To address these issues, this study aims to contribute to the development of a more precise and automated approach for deforestation detection using satellite data through comparative evaluations of the reviewed models, showcasing the benef” (p. 3, seção 1 Introduction)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “TABLE 3 Summary of prevailing and recent deep learning research works. |Article|Dataset|Architecture|Strength|Weakness| |---|---|---|---|---| |A Sentinel-2 based multispectral<br>convolutional neural network for<br>detecting artisanal small” (p. 7, seção 3.3 Remote sensing technology for)
- “FCN32-VGG16|– Performance of Attention U-Net achieved<br>the best deforestation masks across all<br>datasets, with average pixel-wise F1-scores<br>of 0.9550, 0.9769, and 0.9461 for each<br>dataset, respectively.<br>– Accuracy of non-forest ” (p. 7, seção 3.3 Remote sensing technology for)
- “We employed specific keywords (“deforestation,” “segmentation,” “deep learning”) in search strings on the WoS and Scopus databases, resulting in the retrieval of 95 articles (70 from Scopus, 25 from WoS) between 2018 and 2022.” (p. 4, seção 2.1 Identification stage)
- “This review focuses exclusively on English-language studies within the 2018–2022 timeframe, ensuring relevance and validity, as detailed in Table 2 .” (p. 4, seção 2.2 Screening stage)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **UAV**: 41 ocorrências (p. 2, 6, 7, 8, 12)
- sensor/produto **Landsat**: 32 ocorrências (p. 2, 8, 9, 10, 12)
- sensor/produto **Sentinel-2**: 30 ocorrências (p. 7, 8, 9, 12, 14)
- sensor/produto **Sentinel-1**: 8 ocorrências (p. 10, 11, 15, 21)
- conjunto de dados **PRODES**: 8 ocorrências (p. 9, 15, 17, 21)
- conjunto de dados **DETER**: 5 ocorrências (p. 9, 15, 21)
- conjunto de dados **Global Forest Change**: 3 ocorrências (p. 2)
- “A decoder.|– High accuracy: Achieved an accuracy of<br>98.143%<br>– High speciﬁcity of 96.599%<br>– High Sensitivity of 95.556%<br>– Similarity to ground truth.<br>– Capability to handle occlusion.|– Limited dataset generalization.<br>– Hig” (p. 7, seção 3.3 Remote sensing technology for)
- “TABLE 3 (Continued) |Article|Dataset|Architecture|Strength|Weakness| |---|---|---|---|---| |Deep learning-based automated forest<br>health diagnosis from aerial images<br>(Chiang et al., 2020)|– Dataset: Synthetic dataset from the raw<br>da” (p. 9, seção 3.3 Remote sensing technology for)
- “Resnet-FPN (backbone)|– The best model achieved a mean average<br>precision score (mAP) of 54%.<br>– Produces images and annotations<br>eﬃciently.<br>– Less complexity reduction during<br>implementation.<br>– Rare False Positive detection.|” (p. 9, seção 3.3 Remote sensing technology for)
- “Throughout the data analysis process, a comprehensive log was maintained to record analyses, viewpoints, questions, and other relevant thoughts for data interpretation.” (p. 5, seção 2.4 Data abstraction and analysis)
- “FCN32-VGG16|– Performance of Attention U-Net achieved<br>the best deforestation masks across all<br>datasets, with average pixel-wise F1-scores<br>of 0.9550, 0.9769, and 0.9461 for each<br>dataset, respectively.<br>– Accuracy of non-forest ” (p. 7, seção 3.3 Remote sensing technology for)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 43 ocorrências (p. 2, 7, 9, 13, 16)
- **Recorte em patches/tiles**: 21 ocorrências (p. 2, 7, 8, 9, 11)
- **Aumento de dados**: 19 ocorrências (p. 8, 11, 13, 16, 17)
- **Máscara de nuvem e sombra**: 2 ocorrências (p. 7)
- **Mosaicos e compostos**: 2 ocorrências (p. 12)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 20 menções vs 0 de pares)
**Métodos detectados automaticamente:**
- método/família **U-Net**: 94 ocorrências (p. 1, 6, 7, 8, 9)
- método/família **CNN**: 46 ocorrências (p. 2, 3, 6, 7, 8)
- método/família **YOLO**: 8 ocorrências (p. 11, 19)
- método/família **LSTM / recorrente**: 4 ocorrências (p. 8)
- método/família **Random Forest**: 4 ocorrências (p. 2, 10, 17, 19)
- método/família **SVM**: 3 ocorrências (p. 2, 12)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 0.003, a batch size of 16, and the Adaptive Mom” (p. 20)
- batch: “batch size of 16, and the Adaptive Moment Estimati” (p. 20)
- épocas/iterações: “90 epochs” (p. 11)
- otimizador: “Adam) optimizer” (p. 20)
- perda: “binary crossentropy as a loss function to enhance ne” (p. 19)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Teste externo / generalização**: 11 ocorrências (p. 7, 8, 13, 16, 17)
- **Conjuntos treino/val/teste**: 7 ocorrências (p. 13, 16, 17)
- **Desbalanceamento**: 2 ocorrências (p. 17)
- métrica **Precisão/Recall**: 40 ocorrências (p. 3, 9, 10, 11, 19)
- métrica **F1**: 34 ocorrências (p. 3, 7, 9, 10, 11)
- métrica **IoU**: 13 ocorrências (p. 8, 10, 12, 17, 19)
- métrica **Acurácia global**: 10 ocorrências (p. 2, 7, 10, 11, 19)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “(2021) proposed a convolutional neural network-based method for detecting deforestation in Finland, achieving an overall accuracy of 92.78%.” (p. 2, seção 1 Introduction)
- “(2020) developed a deep learning-based framework for detecting deforestation in Greater Khingan Mountains in northeast China, achieving an overall accuracy of 93.60% by using direct method, while 93.80% by using indirect method.” (p. 2, seção 1 Introduction)
- “Highest Accuracy (0.98)<br>4.” (p. 9, seção 3.3 Remote sensing technology for)
- “Highest Precision (0.989)<br>5.” (p. 9, seção 3.3 Remote sensing technology for)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “Conventional machine learning algorithms such as Support Vector Machine (SVM) and Random Forest (RF), while effective, have limitations compared to deep learning algorithms in detecting the deforestation (Alonso et al., 2020).” (p. 2, seção 1 Introduction)
- “Subsequently, Section 4 engages in a “Discussion” on the strengths and limitations of the current state-of-the-art methods for deforestation detection using deep learning and remote sensing.” (p. 3, seção 1 Introduction)
- “The paper is concluded in Section 5, providing the “Conclusion and future work.” This section summarizes the main contributions and implications of the review while suggesting a few future research directions.” (p. 3, seção 1 Introduction)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 7)
- declaração: “TABLE 3 Summary of prevailing and recent deep learning research works. |Article|Dataset|Architecture|Strength|Weakness| |---|---|---|---|---| |A Sentinel-2 based multispectral<br>convolutional neural network for<br>detecting artisanal small” (p. 7)
- declaração: “Spectral Random Multi-Layer Incorporating Skip U-Net Residual ResNet50-SegNet FCN32-VGG16 Architecture An Atrous A SegNet U-Net Architecture Architecture: network and open-source satellite Benchmark 1.” (p. 7)

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Falsos alertas 1 (p. 19); Custo 1 (p. 20)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[UAV|UAV / drones]] — 41 ocorrências (p. 2, 6, 7, 8, 12)
- utiliza dado/sensor: [[Landsat|Landsat]] — 32 ocorrências (p. 2, 8, 9, 10, 12)
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 30 ocorrências (p. 7, 8, 9, 12, 14)
- emprega conjunto de dados: [[PRODES|PRODES (INPE)]] — 8 ocorrências (p. 9, 15, 17, 21)
- emprega conjunto de dados: [[DETER|DETER (INPE)]] — 5 ocorrências (p. 9, 15, 21)
- utiliza método: [[UNet|U-Net]] — 94 ocorrências (p. 1, 6, 7, 8, 9)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 46 ocorrências (p. 2, 3, 6, 7, 8)
- utiliza método: [[RandomForest|Random Forest]] — 4 ocorrências (p. 2, 10, 17, 19)
- utiliza método: [[SVM|SVM]] — 3 ocorrências (p. 2, 12)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 40 ocorrências (p. 3, 9, 10, 11, 19)
- é avaliado por: [[F1|F1]] — 34 ocorrências (p. 3, 7, 9, 10, 11)
- é avaliado por: [[IoU|IoU / mIoU]] — 13 ocorrências (p. 8, 10, 12, 17, 19)
- é avaliado por: [[AcuraciaGlobal|Acurácia global (OA)]] — 10 ocorrências (p. 2, 7, 10, 11, 19)
- usa ferramenta: [[QGIS|QGIS]] — 6 ocorrências (p. 14, 15, 16)
- usa ferramenta: [[GoogleEarthEngine|Google Earth Engine]] — 6 ocorrências (p. 15, 20, 21)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 43 ocorrências (p. 2, 7, 9, 13, 16)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 21 ocorrências (p. 2, 7, 8, 9, 11)
- aplica etapa de preparo: [[AumentoDados|Aumento de dados]] — 19 ocorrências (p. 8, 11, 13, 16, 17)
- adota desenho de validação: [[Generalizacao|Generalização e domain shift]] — 11 ocorrências (p. 7, 8, 13, 16, 17)
- adota desenho de validação: [[DivisaoTreinoTeste|Divisão treino/validação/teste]] — 7 ocorrências (p. 13, 16, 17)
- trata a tarefa: [[Desmatamento|Desmatamento]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[SegmentacaoSemantica|Segmentação semântica]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
