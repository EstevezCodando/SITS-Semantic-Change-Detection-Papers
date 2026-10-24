---
tipo: artigo
id_origem: P03
titulo: "Detection of forest disturbance across California using deep-learning on PlanetScope imagery"
ano: 2024
autores: ["Griffin Carter", "Fabien Hubert Wagner", "Ricardo Dalagnol", "Sophia Roberts", "Alison L. Ritz", "Sassan S Saatchi"]
doi: "10.3389/frsen.2024.1409400"
arquivo_fonte: "coleta/P03_Carter2024_Detection-of-forest-disturbance-across-California-using-deep.pdf"
markdown_fonte: "output/pdf/P03_Carter2024_Detection-of-forest-disturbance-across-California-using-deep/document.md"
paginas: 15
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[DegradacaoFlorestal|Degradação e perturbação florestal]]", "[[Edificacoes|Edificações e urbanização]]"]
sensores: ["[[PlanetScope|PlanetScope (Dove/SuperDove)]]", "[[PlanetProdutos|Produtos Planet (visão geral)]]", "[[PlanetNICFI|Planet NICFI (basemaps)]]"]
conjuntos_dados: ["[[GlobalForestChange|Global Forest Change (Hansen)]]"]
metodos: ["[[UNet|U-Net]]", "[[CNN|Redes convolucionais (CNN)]]", "[[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]]"]
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]", "[[MosaicosCompostos|Mosaicos e compostos temporais]]", "[[Textura|Textura (GLCM)]]", "[[Rotulagem|Rotulagem e anotação]]", "[[AumentoDados|Aumento de dados]]"]
validacao: ["[[AmostraIndependente|Amostra independente]]", "[[PrecisaoRecall|Precisão e recall]]", "[[F1|F1]]", "[[AcuraciaGlobal|Acurácia global (OA)]]", "[[EstimativaArea|Estimativa de área com intervalo de confiança]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Carter 2024 — Detection of forest disturbance across California using deep-learning on PlanetScope imagery

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Griffin Carter, Fabien Hubert Wagner, Ricardo Dalagnol, Sophia Roberts et al. (2024). Detection of forest disturbance across California using deep-learning on PlanetScope imagery. Frontiers in Remote Sensing. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.3389/frsen.2024.1409400
- **Arquivo de origem:** `coleta/P03_Carter2024_Detection-of-forest-disturbance-across-California-using-deep.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P03_Carter2024_Detection-of-forest-disturbance-across-California-using-deep/document.md` — 15 páginas, 19 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “We introduce a novel method of tracking California forest cover using a supervised U-Net deep learning architecture and PlanetScope’s Visual dataset which provides 3-band RGB (Red, Green, and Blue) mosaicked imagery.” (p. 1, seção Início)
- “We compared our high-resolution disturbance maps with wildfire GIS survey data from CALFIRE, and satellitebased forest cover changes and achieved an F-1 score of 54% and 88% respectively.” (p. 1, seção Início)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The highest observed forest loss rate was located at the Sierra Nevada mountains at 21.4% of the forested area being disturbed between 2020 and 2021.” (p. 1, seção Início)
- “Our study site covers the entire state boundary of California, United States (Figure 1).” (p. 2, seção 2.1 Study site)
- “From 2020 to 2021, California maintained 30,923.5 sq km of forest while 5,994.9 sq km were disturbed.” (p. 1, seção Início)
- “The highest observed forest loss rate was located at the Sierra Nevada mountains at 21.4% of the forested area being disturbed between 2020 and 2021.” (p. 1, seção Início)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **PlanetScope**: 15 ocorrências (p. 1, 2, 3, 4, 11)
- sensor/produto **Planet (mosaicos e cenas)**: 12 ocorrências (p. 2, 4, 5, 12, 13)
- sensor/produto **Planet NICFI**: 3 ocorrências (p. 2, 12, 13)
- sensor/produto **Sentinel-2**: 3 ocorrências (p. 2, 13)
- conjunto de dados **Global Forest Change**: 3 ocorrências (p. 2, 6)
- resolução mencionada: 500 m (p. 1)
- resolução mencionada: 5 m (p. 1)
- resolução mencionada: 4.77 m (p. 1)
- “These data are organized in 1,866 tiles of 20 km × 20 km (4,096 × 4,096 pixels) covering the entirety of California, United States (Figure 1).” (p. 4, seção 2.2 PlanetScope satellite images)
- “From the total 8113.8 km of forest covered by 9188 canopy height tiles, we randomly selected 1,000 tiles to be used as our reference data which covered 895 km .” (p. 4, seção 2.3 Airborne LiDAR data)
- “After verifying the k-texture results on the 120 images, the training dataset consisted of 3930 training samples of 256 × 256 pixels extracted from 23 images where the forest segmentation was deemed accurate according to visual interpretati” (p. 4, seção 2.5 Label production and training)
- “From the total 8113.8 km of forest covered by 9188 canopy height tiles, we randomly selected 1,000 tiles to be used as our reference data which covered 895 km .” (p. 4, seção 2.3 Airborne LiDAR data)
- “After verifying the k-texture results on the 120 images, the training dataset consisted of 3930 training samples of 256 × 256 pixels extracted from 23 images where the forest segmentation was deemed accurate according to visual interpretati” (p. 4, seção 2.5 Label production and training)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 24 ocorrências (p. 1, 2, 3, 4, 5)
- **Mosaicos e compostos**: 22 ocorrências (p. 1, 2, 3, 4, 5)
- **Textura (GLCM)**: 8 ocorrências (p. 3, 4, 12, 13)
- **Rotulagem / anotação**: 5 ocorrências (p. 4, 12, 13)
- **Aumento de dados**: 3 ocorrências (p. 4, 5)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **U-Net**: 22 ocorrências (p. 1, 2, 3, 4, 6)
- método/família **CNN**: 7 ocorrências (p. 1, 2, 12, 13)
- método/família **Semi/auto-supervisionado**: 3 ocorrências (p. 3, 4, 13)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 0.0001” (p. 4)
- batch: “batch size of 256 images and the model with the be” (p. 4)
- épocas/iterações: “25,000 epochs” (p. 4)
- otimizador: “Adam optimizer with a learning rate of 0” (p. 4)
- perda: “binary cross-entropy and Dice coefficient-related lo” (p. 4)
- tamanho do patch: “256 × 256 pixel” (p. 3)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Amostra independente**: 3 ocorrências (p. 1, 6, 13)
- métrica **Precisão/Recall**: 8 ocorrências (p. 1, 6, 7)
- métrica **F1**: 3 ocorrências (p. 6, 7)
- métrica **Acurácia global**: 3 ocorrências (p. 1, 6, 13)
- métrica **Estimativa de área**: 3 ocorrências (p. 6, 12)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “The network was trained for 25,000 epochs with a batch size of 256 images and the model with the best weighted accuracy was kept for prediction (epoch 22,794 and training/validation accuracy of 98.97% and 95.02%, respectively, and training/validation loss of 0” (p. 4, seção 21 more images to increase the robustness of the a)
- “Our U-net model has a training accuracy of 98.97%, validation accuracy of 95.5%, a precision of 82%, a recall of 74%, and an F-1 score of 0.778.” (p. 6, seção 3.1 Training validation)
- “The validation accuracy is conducted over the 20% of the training dataset that is not included in the training of the U-net to ensure independence.” (p. 6, seção 3.1 Training validation)
- “Setting the height threshold at 5 m, according to the International Geosphere-Biosphere Program (IGBP) definition for forest cover, we saw an overall accuracy of 77.77%, an 82% precision of pixels predicted as forest cover and 74% precision of pixels predicted” (p. 6, seção 3.2 Validation of individual predictions using)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “These limitations can be circumvented by using AI and cloud computing optimization techniques.” (p. 2, seção 1 Introduction)
- “The CALFIRE dataset is the most up to date data on fire and logging available in California but presents limitations such as areas which may be shown as undisturbed forest within the disturbed polygons perimeter, or disturbed forests outsid” (p. 6, seção 2.8 Validation and comparison with)
- “A limitation for our model comes from the topography and seasonality of California.” (p. 13, seção 4.5 Topography and seasonality of data)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 13)
- declaração: “The creation of such accurate, high resolution forest cover maps at a wide range of scales can help track and monitor forest changes across various biomes. ## Data availability statement The raw data supporting the conclusion of this articl” (p. 13)

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Latência / frequência 1 (p. 2); Revisão humana 1 (p. 4)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[PlanetScope|PlanetScope (Dove/SuperDove)]] — 15 ocorrências (p. 1, 2, 3, 4, 11)
- utiliza dado/sensor: [[PlanetProdutos|Produtos Planet (visão geral)]] — 12 ocorrências (p. 2, 4, 5, 12, 13)
- utiliza dado/sensor: [[PlanetNICFI|Planet NICFI (basemaps)]] — 3 ocorrências (p. 2, 12, 13)
- emprega conjunto de dados: [[GlobalForestChange|Global Forest Change (Hansen)]] — 3 ocorrências (p. 2, 6)
- utiliza método: [[UNet|U-Net]] — 22 ocorrências (p. 1, 2, 3, 4, 6)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 7 ocorrências (p. 1, 2, 12, 13)
- utiliza método: [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 3 ocorrências (p. 3, 4, 13)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 8 ocorrências (p. 1, 6, 7)
- é avaliado por: [[F1|F1]] — 3 ocorrências (p. 6, 7)
- é avaliado por: [[AcuraciaGlobal|Acurácia global (OA)]] — 3 ocorrências (p. 1, 6, 13)
- é avaliado por: [[EstimativaArea|Estimativa de área com intervalo de confiança]] — 3 ocorrências (p. 6, 12)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 24 ocorrências (p. 1, 2, 3, 4, 5)
- aplica etapa de preparo: [[MosaicosCompostos|Mosaicos e compostos temporais]] — 22 ocorrências (p. 1, 2, 3, 4, 5)
- aplica etapa de preparo: [[Textura|Textura (GLCM)]] — 8 ocorrências (p. 3, 4, 12, 13)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 5 ocorrências (p. 4, 12, 13)
- aplica etapa de preparo: [[AumentoDados|Aumento de dados]] — 3 ocorrências (p. 4, 5)
- adota desenho de validação: [[AmostraIndependente|Amostra independente]] — 3 ocorrências (p. 1, 6, 13)
- trata a tarefa: [[DegradacaoFlorestal|Degradação e perturbação florestal]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
