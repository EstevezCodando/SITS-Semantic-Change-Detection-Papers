---
tipo: artigo
id_origem: P06
titulo: "Determination of land use and land cover change using multi-temporal PlanetScope images and deep learning CNN model"
ano: 2025
autores: ["Fatih Fehmi Şimşek"]
doi: "10.1007/s10333-025-01024-9"
arquivo_fonte: "coleta/P06_Simsek2025_Determination-of-land-use-and-land-cover-change-using-multi-.pdf"
markdown_fonte: "output/pdf/P06_Simsek2025_Determination-of-land-use-and-land-cover-change-using-multi-/document.md"
paginas: 19
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[Edificacoes|Edificações e urbanização]]", "[[ClassificacaoCobertura|Classificação de cobertura e uso da terra]]"]
sensores: ["[[PlanetScope|PlanetScope (Dove/SuperDove)]]", "[[Sentinel2|Sentinel-2]]", "[[PlanetProdutos|Produtos Planet (visão geral)]]"]
conjuntos_dados: []
metodos: ["[[CNN|Redes convolucionais (CNN)]]", "[[RandomForest|Random Forest]]", "[[SVM|SVM]]"]
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]", "[[IndicesEspectrais|Índices espectrais (NDVI etc.)]]", "[[Rotulagem|Rotulagem e anotação]]", "[[MosaicosCompostos|Mosaicos e compostos temporais]]", "[[Normalizacao|Normalização e escala radiométrica]]"]
validacao: ["[[PrecisaoRecall|Precisão e recall]]", "[[F1|F1]]", "[[AcuraciaGlobal|Acurácia global (OA)]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Simsek 2025 — Determination of land use and land cover change using multi-temporal PlanetScope images and deep learning CNN model

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Fatih Fehmi Şimşek (2025). Determination of land use and land cover change using multi-temporal PlanetScope images and deep learning CNN model. Paddy and Water Environment. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1007/s10333-025-01024-9
- **Arquivo de origem:** `coleta/P06_Simsek2025_Determination-of-land-use-and-land-cover-change-using-multi-.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P06_Simsek2025_Determination-of-land-use-and-land-cover-change-using-multi-/document.md` — 19 páginas, 13 recortes de figuras, 1 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Land use and land cover (LULC), an important component of Earth observation technology, plays a crucial role in image classification. Detailed LULC information is of great importance for monitoring agriculture and wetlands, urban and rural planning, land resource management, and the monitoring and detection of climate change-induced changes. To create a detailed LULC, high-resolution satellite imagery, ground truth data, and a model that provides high accuracy are required. For this reason, 8-band PlanetScope images with 3 m spatial resolution, Land Parcel Identification System (LPIS) physical blocks (1:5000 scale), and a convolutional neural network (CNN) model were used as ground truth data. While using the CNN model, hyperparameter optimization was performed to determine the most suitable parameters for achieving high classification accuracy. As a result of the classification, the ove…

- “This study presents a novel approach by integrating high-resolution, multi-temporal PlanetScope imagery with LPIS data and employing a CNN-based deep learning model optimized for LULC classification.” (p. 3, seção 1 TÜBİTAK Space Technologies Research Institute,)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The study area (27° 43′–28° 50′ E, 38° 39′–38° 30′ N) is situated within the Gediz Plain in the city of Manisa, western Turkey (Fig.” (p. 3, seção Study area)
- “The north-western part of the study area (520 ­km ) features Çal Mountain, with an elevation of 1034 m, and the Gediz River flows through the southern part of the area.” (p. 3, seção Study area)
- “(2023) analyzed six PlanetScope (PS) monthly mosaics from the 2021/2022 season to identify double-cropping areas in Goiatuba, Goiás State, Brazil.” (p. 3, seção 1 TÜBİTAK Space Technologies Research Institute,)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **PlanetScope**: 34 ocorrências (p. 1, 2, 3, 4, 5)
- sensor/produto **Sentinel-2**: 19 ocorrências (p. 2, 3, 4, 5, 6)
- sensor/produto **Planet (mosaicos e cenas)**: 13 ocorrências (p. 2, 3, 4, 5, 6)
- sensor/produto **Sentinel-1**: 5 ocorrências (p. 3, 16, 17)
- resolução mencionada: 3 m (p. 1)
- resolução mencionada: 10 m (p. 2)
- “(2022) conducted an LULC study (grassland, arable land, tree crops, vineyard, wetland, artificial surface, and forest) in Greece (Fthiotida Prefecture and Central Greece District) using four different Sentinel-2 images from 2018, LPIS physi” (p. 2, seção 1 TÜBİTAK Space Technologies Research Institute,)
- “To create a detailed LULC, high-resolution satellite imagery, ground truth data, and a model that provides high accuracy are required.” (p. 1, seção Abstract)
- “For this reason, 8-band PlanetScope images with 3 m spatial resolution, Land Parcel Identification System (LPIS) physical blocks (1:5000 scale), and a convolutional neural network (CNN) model were used as ground truth data.” (p. 1, seção Abstract)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 25 ocorrências (p. 2, 3, 4, 6, 9)
- **Índices espectrais**: 20 ocorrências (p. 2, 3, 6, 7, 9)
- **Rotulagem / anotação**: 10 ocorrências (p. 1, 3, 6, 12, 17)
- **Mosaicos e compostos**: 8 ocorrências (p. 2, 3, 7, 8, 15)
- **Normalização / escala**: 5 ocorrências (p. 6, 7, 11)
- **Correção atmosférica / reflectância**: 4 ocorrências (p. 1, 6)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 16 menções vs 0 de pares)
**Métodos detectados automaticamente:**
- método/família **CNN**: 43 ocorrências (p. 1, 2, 3, 6, 8)
- método/família **Random Forest**: 8 ocorrências (p. 2, 3, 16, 17)
- método/família **SVM**: 5 ocorrências (p. 2, 3)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate, etc” (p. 12)
- batch: “batch size, loss function, learning rate, etc” (p. 12)
- otimizador: “Adam optimizer was used to reduce the traini” (p. 12)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- métrica **Precisão/Recall**: 32 ocorrências (p. 12, 14)
- métrica **F1**: 9 ocorrências (p. 12, 14)
- métrica **Acurácia global**: 9 ocorrências (p. 1, 2, 3, 12, 15)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “As a result of the classification, the overall accuracy value was 93.14%, while the accuracy value for each class (arable land, artificial surface, forest, grassland, shrubland, tree crops, and water) was around 90%.” (p. 1, seção Abstract)
- “In the study, the overall accuracy value was 92.2%, with the highest accuracy observed for arable land and water (97%), while the lowest accuracy was found for grassland (88%) and tree crops (73%).” (p. 2, seção 1 TÜBİTAK Space Technologies Research Institute,)
- “As a result of this study using the random forest algorithm, the overall accuracy was 83.3%.” (p. 2, seção 1 TÜBİTAK Space Technologies Research Institute,)
- “When the LULC map and LPIS physical blocks were compared, it was found that there was a 31.5% increase in arable areas.” (p. 2, seção 1 TÜBİTAK Space Technologies Research Institute,)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “Despite the promising results, this study has some limitations.” (p. 17, seção Discussion)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 2)
- declaração: “Notably, DL-based LULC classification methods have outperformed traditional and ML methods, particularly 2017). when sufficient training data is available (Zhu et al.” (p. 2)
- hiperparâmetros **não detectados** automaticamente: épocas/iterações, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 3 (p. 10, 12, 17)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[PlanetScope|PlanetScope (Dove/SuperDove)]] — 34 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 19 ocorrências (p. 2, 3, 4, 5, 6)
- utiliza dado/sensor: [[PlanetProdutos|Produtos Planet (visão geral)]] — 13 ocorrências (p. 2, 3, 4, 5, 6)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 43 ocorrências (p. 1, 2, 3, 6, 8)
- utiliza método: [[RandomForest|Random Forest]] — 8 ocorrências (p. 2, 3, 16, 17)
- utiliza método: [[SVM|SVM]] — 5 ocorrências (p. 2, 3)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 32 ocorrências (p. 12, 14)
- é avaliado por: [[F1|F1]] — 9 ocorrências (p. 12, 14)
- é avaliado por: [[AcuraciaGlobal|Acurácia global (OA)]] — 9 ocorrências (p. 1, 2, 3, 12, 15)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 25 ocorrências (p. 2, 3, 4, 6, 9)
- aplica etapa de preparo: [[IndicesEspectrais|Índices espectrais (NDVI etc.)]] — 20 ocorrências (p. 2, 3, 6, 7, 9)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 10 ocorrências (p. 1, 3, 6, 12, 17)
- aplica etapa de preparo: [[MosaicosCompostos|Mosaicos e compostos temporais]] — 8 ocorrências (p. 2, 3, 7, 8, 15)
- aplica etapa de preparo: [[Normalizacao|Normalização e escala radiométrica]] — 5 ocorrências (p. 6, 7, 11)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[ClassificacaoCobertura|Classificação de cobertura e uso da terra]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
