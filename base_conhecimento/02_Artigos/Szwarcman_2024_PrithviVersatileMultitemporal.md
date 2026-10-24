---
tipo: artigo
id_origem: P32
titulo: "Prithvi-EO-2.0: A Versatile Multitemporal Foundation Model for Earth Observation Applications"
ano: 2024
autores: ["Daniela Szwarcman", "Sujit Roy", "Paolo Fraccaro", "Þorsteinn Elí Gíslason", "Benedikt Blumenstiel", "Rinki Ghosal", "Pedro Henrique de Oliveira", "Joao Lucas de Sousa Almeida"]
doi: "10.48550/arXiv.2412.02732"
arquivo_fonte: "coleta/P32_Szwarcman2025_Prithvi-EO-2-0-A-Versatile-Multitemporal-Foundation-Model-fo.pdf"
markdown_fonte: "output/pdf/P32_Szwarcman2025_Prithvi-EO-2-0-A-Versatile-Multitemporal-Foundation-Model-fo/document.md"
paginas: 21
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: []
sensores: ["[[Sentinel2|Sentinel-2]]", "[[Sentinel1|Sentinel-1]]", "[[Landsat|Landsat]]"]
conjuntos_dados: []
metodos: ["[[ModeloFundacional|Modelos fundacionais]]", "[[Transformer|Transformers]]", "[[TransferLearning|Aprendizado por transferência]]", "[[UNet|U-Net]]", "[[XGBoost|XGBoost]]", "[[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]]"]
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]", "[[AumentoDados|Aumento de dados]]", "[[Rotulagem|Rotulagem e anotação]]", "[[MascaraNuvem|Máscara de nuvem e sombra]]", "[[IndicesEspectrais|Índices espectrais (NDVI etc.)]]"]
validacao: ["[[DivisaoTreinoTeste|Divisão treino/validação/teste]]", "[[IoU|IoU / mIoU]]", "[[F1|F1]]", "[[PrecisaoRecall|Precisão e recall]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Szwarcman 2024 — Prithvi-EO-2.0: A Versatile Multitemporal Foundation Model for Earth Observation Applications

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Daniela Szwarcman, Sujit Roy, Paolo Fraccaro, Þorsteinn Elí Gíslason et al. (2024). Prithvi-EO-2.0: A Versatile Multitemporal Foundation Model for Earth Observation Applications. IEEE Transactions on Geoscience and Remote Sensing. Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2412.02732
- **Arquivo de origem:** `coleta/P32_Szwarcman2025_Prithvi-EO-2-0-A-Versatile-Multitemporal-Foundation-Model-fo.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P32_Szwarcman2025_Prithvi-EO-2-0-A-Versatile-Multitemporal-Foundation-Model-fo/document.md` — 21 páginas, 48 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “1 ## Prithvi-EO-2.0: A Versatile Multi-Temporal Foundation Model for Earth Observation Applications Daniela Szwarcman [1,] [†], Sujit Roy [2,3,] [ †] [,] [ ‡] (Senior Member, IEEE), Paolo Fraccaro [1,] [ †] [,] [ ‡], Þorsteinn Elí Gíslason ” (p. 1, seção Início)
- “within the EO community, we developed a new multi-temporal GFM called Prithvi-EO-2.0 .” (p. 2, seção I. I NTRODUCTION)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “Each image covers an area of 640 m × 640 m, which contrasts with our pretraining dataset, where the images are 224 × 224 pixels with a resolution of 30 m, covering approximately 6,720 m × 6,720 m—over 100 times the area of the Sen4Map sampl” (p. 8, seção 0.1. As described in section III-A, the samples have shape)
- “To achieve this, we built temporal sequences of four HLS images with intervals of one to six months between consecutive times tamps, spanning the period from 2014 and 2023.” (p. 3, seção III. M ETHODS)
- “The dataset consists of 446 512 × 512 images covering 14 biomes, 357 ecoregions, and 6 continents of the world across 11 flood events between 2018 and 2020.” (p. 6, seção 0.1. As described in section III-A, the samples have shape)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-2**: 37 ocorrências (p. 2, 6, 7, 8, 9)
- sensor/produto **Sentinel-1**: 14 ocorrências (p. 2, 6, 7, 9, 18)
- sensor/produto **Landsat**: 8 ocorrências (p. 1, 2, 6, 7, 18)
- sensor/produto **SAR**: 8 ocorrências (p. 15, 16, 18)
- resolução mencionada: 30 m (p. 2)
- resolução mencionada: 10 m (p. 8)
- “Despite its spatiotemporal design, U-BARN is trained with small 64 × 64 patches and a very restricted pretraining dataset, considering only nine Sentinel-2 tiles from France over two years .” (p. 2, seção 12 months of data from different sources, with each month)
- “The sequences were iteratively sampled from the selected HLS tiles until all candidates (minimum of four timestamps) were processed or 1,500 samples per tile (250 for validation) were reached.” (p. 3, seção III. M ETHODS)
- “Then, the sequences were split into nonoverlapping 256 × 256 patches with four consecutive timestamps.” (p. 3, seção III. M ETHODS)
- “These models can help address longstanding challenges in EO by reducing the need for manually labeled samples, which are usually hard to obtain at scale .” (p. 1, seção I. I NTRODUCTION)
- “It measures the average overlap between predicted and ground truth regions across all classes, defined as: where C is the total number of classes and prediction c and truth c denote the predicted and ground truth regions for class c, respec” (p. 5, seção 0.1. As described in section III-A, the samples have shape)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 70 ocorrências (p. 1, 2, 3, 4, 5)
- **Aumento de dados**: 10 ocorrências (p. 2, 5, 6, 8, 9)
- **Rotulagem / anotação**: 9 ocorrências (p. 1, 2, 5, 8, 10)
- **Máscara de nuvem e sombra**: 7 ocorrências (p. 3, 7, 9, 10)
- **Índices espectrais**: 6 ocorrências (p. 10, 16)
- **Normalização / escala**: 4 ocorrências (p. 5, 8, 9)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 37 menções vs 0 de pares)
**Métodos detectados automaticamente:**
- método/família **Modelo fundacional**: 288 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Transformer**: 59 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Transfer learning**: 32 ocorrências (p. 1, 2, 5, 7, 8)
- método/família **U-Net**: 30 ocorrências (p. 2, 5, 8, 9, 12)
- método/família **XGBoost**: 7 ocorrências (p. 10, 16)
- método/família **Semi/auto-supervisionado**: 7 ocorrências (p. 1, 2, 3, 8, 18)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 5e-4 and linear warmup for 40 epochs starting ” (p. 5)
- batch: “batch size (i” (p. 5)
- épocas/iterações: “400 epochs” (p. 5)
- otimizador: “Adam optimizer with a learning rate of 1e-5” (p. 8)
- perda: “cross-entropy and the models ran for 50 epochs with e” (p. 6)
- tamanho do patch: “64 × 64 patch” (p. 2)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 27 ocorrências (p. 5, 6, 8, 9, 11)
- **Validação cruzada**: 2 ocorrências (p. 10, 17)
- métrica **IoU**: 45 ocorrências (p. 5, 6, 8, 9, 11)
- métrica **F1**: 18 ocorrências (p. 5, 6, 8, 9, 12)
- métrica **Precisão/Recall**: 14 ocorrências (p. 5, 13)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “Through extensive benchmarking with GEO-Bench, the model outperforms the previous Prithvi- EO model by 8% across a range of tasks.” (p. 1, seção 2 data archive at 30-m resolution, the new model i)
- “Interestingly, although the mIoU is generally low for all models, they seem capable of distinguishing unburnt from burnt areas, with IoU 0 above 67%.” (p. 12, seção 2.0 improves over its previous version. Given the )
- “Prithvi-EO-2.0600M, trained with weighted cross-entropy loss, exhibited a slightly lower mIoU of 70.4% and an F1 score of 58.6%, but achieved a higher recall than Prithvi-EO-2.0-300M.” (p. 13, seção 2.0 improves over its previous version. Given the )
- “Recall mAcc U-Net wCE 70.4 59.7 56.2 63.6 98.4 U-Net++ wCE 69.0 57.0 50.2 68.4 98.0 Prithvi-EO-2.0-300M Lovasz 71.3 60.7 57.1 64.7 98.4 Prithvi-EO-2.0-600M wCE 70.4 58.6 51.1 68.6 98.2 TABLE VIII: Performance metrics on the test set of L4S for models trained w” (p. 13, seção 2.0 improves over its previous version. Given the )

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “However, all models seem to struggle to differentiate between the various severity classes, with the Prithvi models demonstrating better overall performance.” (p. 13, seção 2.0 improves over its previous version. Given the unbalanced)
- “This is because multispectral sensors are only capable of sensing the reflectance of the top layer of canopy, and so cannot be used to accurately estimate biomass of vegetation obscured by a full canopy.” (p. 15, seção 2.0 improves over its previous version. Given the unbalanced)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: huggingface.co/ibm-nasa-geospatial/Prithvi-EO-2 (p. 1)
- URL citada: https://huggingface.co/ibm-nasa-geospatial/Prithvi-EO-2 (p. 1)
- URL citada: https://huggingface.co/ibm-nasa-geospatial/Prithvi-EO-2.0 (p. 1)
- URL citada: https://github.com/NASA-IMPACT/Prithvi-EO-2.0 (p. 1)
- URL citada: https://github.com/IBM/terratorch (p. 2)
- declaração: “Prithvi-EO-2.0 is available as an open-source model on Hugging Face and IBM TerraTorch, with additional resources on GitHub.” (p. 1)
- declaração: “Code available at: https://github.com/NASA-IMPACT/Prithvi-EO-2.0](https://huggingface.co/ibm-nasa-geospatial/Prithvi-EO-2.0)” (p. 1)

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Rastreabilidade 4 (p. 2, 5, 7); Latência / frequência 1 (p. 1); Persistência / confirmação 1 (p. 3); Custo 1 (p. 16)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 37 ocorrências (p. 2, 6, 7, 8, 9)
- utiliza dado/sensor: [[Sentinel1|Sentinel-1]] — 14 ocorrências (p. 2, 6, 7, 9, 18)
- utiliza dado/sensor: [[Landsat|Landsat]] — 8 ocorrências (p. 1, 2, 6, 7, 18)
- utiliza método: [[ModeloFundacional|Modelos fundacionais]] — 288 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[Transformer|Transformers]] — 59 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 32 ocorrências (p. 1, 2, 5, 7, 8)
- utiliza método: [[UNet|U-Net]] — 30 ocorrências (p. 2, 5, 8, 9, 12)
- utiliza método: [[XGBoost|XGBoost]] — 7 ocorrências (p. 10, 16)
- utiliza método: [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 7 ocorrências (p. 1, 2, 3, 8, 18)
- é avaliado por: [[IoU|IoU / mIoU]] — 45 ocorrências (p. 5, 6, 8, 9, 11)
- é avaliado por: [[F1|F1]] — 18 ocorrências (p. 5, 6, 8, 9, 12)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 14 ocorrências (p. 5, 13)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 70 ocorrências (p. 1, 2, 3, 4, 5)
- aplica etapa de preparo: [[AumentoDados|Aumento de dados]] — 10 ocorrências (p. 2, 5, 6, 8, 9)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 9 ocorrências (p. 1, 2, 5, 8, 10)
- aplica etapa de preparo: [[MascaraNuvem|Máscara de nuvem e sombra]] — 7 ocorrências (p. 3, 7, 9, 10)
- aplica etapa de preparo: [[IndicesEspectrais|Índices espectrais (NDVI etc.)]] — 6 ocorrências (p. 10, 16)
- adota desenho de validação: [[DivisaoTreinoTeste|Divisão treino/validação/teste]] — 27 ocorrências (p. 5, 6, 8, 9, 11)

## Anotações do leitor

- 
