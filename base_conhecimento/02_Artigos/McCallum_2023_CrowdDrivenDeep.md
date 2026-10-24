---
tipo: artigo
id_origem: P115
titulo: "Crowd-Driven Deep Learning Tracks Amazon Deforestation"
ano: 2023
autores: ["Ian McCallum", "Jon Walker", "Steffen Fritz", "Markus Grau", "Cassie Hannan", "I. F. Hsieh", "Deanna Lape", "Jen Mahone"]
doi: "10.3390/rs15215204"
arquivo_fonte: "coleta/P115_McCallum2023_Crowd-Driven-Deep-Learning-Tracks-Amazon-Deforestation.pdf"
markdown_fonte: "output/pdf/P115_McCallum2023_Crowd-Driven-Deep-Learning-Tracks-Amazon-Deforestation/document.md"
paginas: 14
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Desmatamento|Desmatamento]]"]
sensores: ["[[Sentinel2|Sentinel-2]]"]
conjuntos_dados: ["[[PRODES|PRODES (INPE)]]", "[[GlobalForestChange|Global Forest Change (Hansen)]]"]
metodos: []
preparo: ["[[Rotulagem|Rotulagem e anotação]]", "[[MascaraNuvem|Máscara de nuvem e sombra]]", "[[PatchesTiles|Recorte em patches/tiles]]"]
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica]
---

# McCallum 2023 — Crowd-Driven Deep Learning Tracks Amazon Deforestation

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Ian McCallum, Jon Walker, Steffen Fritz, Markus Grau et al. (2023). Crowd-Driven Deep Learning Tracks Amazon Deforestation. Remote Sensing. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.3390/rs15215204
- **Arquivo de origem:** `coleta/P115_McCallum2023_Crowd-Driven-Deep-Learning-Tracks-Amazon-Deforestation.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P115_McCallum2023_Crowd-Driven-Deep-Learning-Tracks-Amazon-Deforestation/document.md` — 14 páginas, 14 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Abstract: The Amazon forests act as a global reserve for carbon, have very high biodiversity, and provide a variety of additional ecosystem services. These forests are, however, under increasing pressure, coming mainly from deforestation, despite the fact that accurate satellite monitoring is in place that produces annual deforestation maps and timely alerts. Here, we present a proof of concept for rapid deforestation monitoring that engages the global community directly in the monitoring process via crowdsourcing while subsequently leveraging the power of deep learning. Offering no tangible incentives, we were able to sustain participation from more than 5500 active contributors from 96 different nations over a 6-month period, resulting in the crowd classification of 43,108 satellite images (representing around 390,000 km ). Training a suite of AI models with results from the crowd, we …

- “Here, we present a proof of concept for rapid deforestation monitoring that engages the global community directly in the monitoring process via crowdsourcing while subsequently leveraging the power of deep learning.” (p. 1, seção 5 SAS Netherlands B.V., 1272 PC Huizen, The Netherlands; mur)
- “Here, we investigate the application of supervised deep learning to automate the identification of satellite images that contain areas of significant deforestation.” (p. 2, seção 1. Introduction)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “Deforestation Data for Validation For the purposes of validation, we obtained forest deforestation annual products [from Brazil’s PRODES system located at http://terrabrasilis.dpi.inpe.br/en/download-2/](http://terrabrasilis.dpi.inpe.br/en/” (p. 5, seção 2. Materials and Methods)
- “A comparison of results from our crowdsourcing campaign with ( a ) global annual tree cover loss and ( b ) Brazil’s PRODES satellite deforestation datasets for a subset of the study area.” (p. 7, seção 3. Results)
- “Deforestation rates reached their peak in the Brazilian Amazon in the period 2003–2004 [ 7 ] at 29,000 km per year, thereafter declining to below 6000 km per year by 2014 [ 3 ].” (p. 1, seção 1. Introduction)
- “The retrieved images spanned the years 2018–2020, implying that, in some images, we would have missed the most recent activity.” (p. 3, seção 2. Materials and Methods)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-2**: 8 ocorrências (p. 3, 6, 9, 10)
- sensor/produto **Landsat**: 2 ocorrências (p. 2, 5)
- conjunto de dados **PRODES**: 13 ocorrências (p. 2, 5, 7, 12)
- conjunto de dados **Global Forest Change**: 2 ocorrências (p. 2, 11)
- resolução mencionada: 10 m (p. 2)
- “Approximately 300 images were removed in this manner.” (p. 5, seção 2. Materials and Methods)
- “These labeled images were retained for model training. disagreement = n de f orestation / n no de f orestation (6) In addition, we randomly sampled 200 images for expert review to measure how often the crowd labels aligned with expert label” (p. 5, seção 2. Materials and Methods)
- “The level of consensus or agreement among the crowd on the classification result was generally high, with most images (37,325 images out of 43,108) receiving over 80% percent consensus.” (p. 6, seção 3. Results)
- “One component of such a complementary verification system could include crowdsourcing, otherwise known as the outsourcing of tasks to the crowd [ 16 ], which has been used successfully in the past for image recognition tasks and the visual ” (p. 2, seção 1. Introduction)
- “These images could then be selected for labeling, potentially reducing the amount of data that must be manually labeled to train or refine an accurate model.” (p. 11, seção 4. Discussion)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 17 ocorrências (p. 3, 4, 5, 6, 9)
- **Máscara de nuvem e sombra**: 5 ocorrências (p. 2, 3, 6)
- **Recorte em patches/tiles**: 4 ocorrências (p. 1, 3, 11)
- **Índices espectrais**: 3 ocorrências (p. 11)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 1 × 10 [−] , a batch size of 32, and an L2 reg” (p. 6)
- batch: “batch size of 32, and an L2 regularization paramet” (p. 6)
- épocas/iterações: “30 epochs” (p. 5)
- perda: “cross-entropy loss J as follows: N ### J ( Θ ) = − N ” (p. 5)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 2 ocorrências (p. 7, 9)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “Training a suite of AI models with results from the crowd, we achieved an accuracy greater than 90% in detecting new and existing deforestation.” (p. 1, seção 5 SAS Netherlands B.V., 1272 PC Huizen, The Nether)
- “This resulted in a spatial accuracy between the crowd and the PRODES and tree cover loss products of 92% and 89%, respectively (Supplementary Tables S1 and S2).” (p. 7, seção 3. Results)
- “The model’s accuracy was measured against a test set of 8774 images that had been labeled by the crowd but not previously seen by the model, achieving agreement with the crowd on 94.8% of the images.” (p. 9, seção 3. Results)
- “The overall accuracy of this comparison was 84% (Supplementary Table S5).” (p. 9, seção 3. Results)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “While this would allow for labeling the most images in the shortest amount of time, we cannot assume that a randomly selected member of the public is skilled enough to accurately identify deforestation in a satellite image.” (p. 4, seção 2. Materials and Methods)
- “A qualitative analysis of the crowd and AI models indicated that the crowd appeared to perform better in terms of classifying rivers and roads, while the AI models tended to struggle with them.” (p. 10, seção 4. Discussion)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 12)
- declaração: “Data Availability Statement: Examples of the data generated in this study are publicly available in Zenodo.” (p. 12)
- hiperparâmetros **não detectados** automaticamente: otimizador (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** candidato a sistema operacional (verificar no texto). menções: operacional 4, alertas 21, quase tempo real 2
- menções de termos de monitoramento (contagem, não avaliação): Alertas 21 (p. 1, 2, 12); Sistema operacional 4 (p. 2, 11, 12); Quase tempo real 2 (p. 2); Latência / frequência 1 (p. 3); Revisão humana 1 (p. 2)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 8 ocorrências (p. 3, 6, 9, 10)
- emprega conjunto de dados: [[PRODES|PRODES (INPE)]] — 13 ocorrências (p. 2, 5, 7, 12)
- emprega conjunto de dados: [[GlobalForestChange|Global Forest Change (Hansen)]] — 2 ocorrências (p. 2, 11)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 17 ocorrências (p. 3, 4, 5, 6, 9)
- aplica etapa de preparo: [[MascaraNuvem|Máscara de nuvem e sombra]] — 5 ocorrências (p. 2, 3, 6)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 4 ocorrências (p. 1, 3, 11)
- discute aspecto de monitoramento: [[Alertas|Alertas de mudança]] — 21 ocorrências (p. 1, 2, 12)
- trata a tarefa: [[Desmatamento|Desmatamento]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
