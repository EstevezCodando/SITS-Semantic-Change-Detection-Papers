---
tipo: artigo
id_origem: P127
titulo: "Deep Learning for Satellite Image Time-Series Analysis: A review"
ano: 2024
autores: ["Lynn Miller", "Charlotte Pelletier", "Geoffrey I. Webb"]
doi: "10.1109/mgrs.2024.3393010"
arquivo_fonte: "coleta/P127_Miller2024_Deep-Learning-for-Satellite-Image-Time-Series-Analysis-A-rev.pdf"
markdown_fonte: "output/pdf/P127_Miller2024_Deep-Learning-for-Satellite-Image-Time-Series-Analysis-A-rev/document.md"
paginas: 38
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[SITS|Séries temporais de imagens (SITS)]]"]
sensores: ["[[Sentinel2|Sentinel-2]]", "[[Landsat|Landsat]]", "[[SAR|Radar (SAR)]]"]
conjuntos_dados: []
metodos: ["[[CNN|Redes convolucionais (CNN)]]", "[[LSTM|Redes recorrentes (LSTM)]]", "[[Transformer|Transformers]]", "[[UNet|U-Net]]", "[[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]]", "[[OBIA|Análise baseada em objetos (OBIA)]]"]
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]", "[[Rotulagem|Rotulagem e anotação]]", "[[IndicesEspectrais|Índices espectrais (NDVI etc.)]]", "[[Normalizacao|Normalização e escala radiométrica]]", "[[SegmentacaoObjetos|Segmentação em objetos (SNIC/superpixels)]]"]
validacao: ["[[Generalizacao|Generalização e domain shift]]", "[[EstimativaArea|Estimativa de área com intervalo de confiança]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Miller 2024 — Deep Learning for Satellite Image Time-Series Analysis: A review

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Lynn Miller, Charlotte Pelletier, Geoffrey I. Webb (2024). Deep Learning for Satellite Image Time-Series Analysis: A review. IEEE Geoscience and Remote Sensing Magazine. Tipo no catálogo: Revisão.
- **DOI/URL:** https://doi.org/10.1109/mgrs.2024.3393010
- **Arquivo de origem:** `coleta/P127_Miller2024_Deep-Learning-for-Satellite-Image-Time-Series-Analysis-A-rev.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P127_Miller2024_Deep-Learning-for-Satellite-Image-Time-Series-Analysis-A-rev/document.md` — 38 páginas, 9 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “The purpose of this data separation is to help ensure reported accuracy is not biased and thus is a reliable measure of the model performance on unseen datasets .” (p. 7, seção 61 and time between acquisitions is uneven. Its multimodal)
- “The objective of land cover mapping is to identify the type of vegetative (e.g., forest, shrubland, grassland, or agricultural uses) or non-vegetative (e.g., bare land, water bodies, urban area) land cover at each point, to generate maps th” (p. 8, seção 61 and time between acquisitions is uneven. Its multimodal)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “While these studies have produced important results for specific applications, the differences in the study regions make it difficult to compare the advantages and disadvantages of the various algorithms.” (p. 5, seção 3. After implementation of the Take-5 experiment .)
- “It includes data collected for 2018 and 2019 from Sentinel-1, Sentinel-2, and Planet Fusion for two tiles located in Northern Germany.” (p. 6, seção 3. After implementation of the Take-5 experiment .)
- “A total of nine satellites were launched between 1972 and 2021, three of which are still” (p. 3, seção Início)
- “The [Satellite Image Time Series Datasets GitHub repository](https://github.com/corentin-dfg/Satellite-Image-Time-Series-Datasets) lists about 50 SITS datasets, collected between 2017 and 2023.” (p. 5, seção 3. After implementation of the Take-5 experiment .)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-2**: 38 ocorrências (p. 2, 3, 4, 5, 6)
- sensor/produto **Landsat**: 27 ocorrências (p. 1, 2, 3, 4, 5)
- sensor/produto **SAR**: 26 ocorrências (p. 1, 4, 5, 9, 11)
- sensor/produto **Sentinel-1**: 25 ocorrências (p. 5, 6, 7, 9, 11)
- resolução mencionada: 30 m (p. 4)
- resolução mencionada: 15 m (p. 4)
- “The BreizhCrops database contains one-year time series of Sentinel-2 images for Brittany, France for both 2017 and 2018.” (p. 5, seção 3. After implementation of the Take-5 experiment .)
- “The time series are of varying lengths, with European Union’s Horizon 2020 (H2020) program to enable either 51 or 102 images for the top-of-atmosphere time series the development of land cover products providing higher levels and an average” (p. 6, seção 3. After implementation of the Take-5 experiment .)
- “TimeSen2Crop is a pixel-based dataset of Sentinel-2 time series for the classification of sixteen crop types in Austria.” (p. 6, seção 3. After implementation of the Take-5 experiment .)
- “EuroCrops is a reference dataset for crop classification covering 16 European Union countries.” (p. 6, seção 61 and time between acquisitions is uneven. Its multimodal)
- “In addition to the reference data, the curators have made available the TinyEuroCrops dataset that contains Sentinel-2 time series for regions in Austria, Denmark, and Slovenia .” (p. 6, seção 61 and time between acquisitions is uneven. Its multimodal)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 87 ocorrências (p. 1, 3, 6, 8, 11)
- **Rotulagem / anotação**: 48 ocorrências (p. 1, 5, 6, 18, 20)
- **Índices espectrais**: 21 ocorrências (p. 5, 7, 9, 16, 17)
- **Normalização / escala**: 14 ocorrências (p. 6, 7, 8, 9, 14)
- **Segmentação em objetos**: 4 ocorrências (p. 19, 20)
- **Máscara de nuvem e sombra**: 3 ocorrências (p. 6, 7, 11)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 463 menções vs 7 de pares)
**Métodos detectados automaticamente:**
- método/família **CNN**: 111 ocorrências (p. 2, 3, 10, 11, 12)
- método/família **LSTM / recorrente**: 87 ocorrências (p. 10, 11, 12, 13, 14)
- método/família **Transformer**: 31 ocorrências (p. 7, 11, 13, 15, 16)
- método/família **U-Net**: 24 ocorrências (p. 13, 14, 17, 19, 20)
- método/família **Semi/auto-supervisionado**: 20 ocorrências (p. 1, 20, 21, 22, 23)
- método/família **OBIA**: 14 ocorrências (p. 2, 15, 17, 18, 19)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Divisão temporal**: 4 ocorrências (p. 22)
- **Teste externo / generalização**: 3 ocorrências (p. 22, 27)
- **Validação cruzada**: 2 ocorrências (p. 7)
- **Conjuntos treino/val/teste**: 2 ocorrências (p. 6, 7)
- **Amostragem estratificada**: 2 ocorrências (p. 7)
- métrica **Estimativa de área**: 3 ocorrências (p. 7, 14)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “However, models using NTL do not perform well in impoverished areas and cannot distinguish between wealthy sparsely populated regions and poor densely populated areas .” (p. 9, seção 61 and time between acquisitions is uneven. Its multimodal)
- “Several authors have claimed either that CNNs cannot learn temporal features , , , , or that RNNs outperform CNNs for land cover and crop type classification .” (p. 12, seção 61 and time between acquisitions is uneven. Its multimodal)
- “Various architectures that combine recurrent and convolutional layers into one hybrid model have been proposed to overcome this limitation (Table 5).” (p. 13, seção 61 and time between acquisitions is uneven. Its multimodal)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/corentin-dfg/Satellite-Image-Time-Series-Datasets (p. 5)
- URL citada: https://github.com/corentin-dfg/Satellite-Image-Time-Series-Datasets (p. 5)
- declaração: “More recently introduced in the literature, self-supervised When data are available for only some geographical areas and learning methods are generally divided into three categories: times, domain adaptation techniques address the problem o” (p. 21)
- declaração: “Approaches tailored for SITS have mainly focused on the unsupervised domain adaptation setting, where no target labeled data is available.” (p. 22)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Latência / frequência 5 (p. 3, 4, 24); Sistema operacional 2 (p. 9, 12); Persistência / confirmação 1 (p. 25); Custo 1 (p. 3)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 38 ocorrências (p. 2, 3, 4, 5, 6)
- utiliza dado/sensor: [[Landsat|Landsat]] — 27 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza dado/sensor: [[SAR|Radar (SAR)]] — 26 ocorrências (p. 1, 4, 5, 9, 11)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 111 ocorrências (p. 2, 3, 10, 11, 12)
- utiliza método: [[LSTM|Redes recorrentes (LSTM)]] — 87 ocorrências (p. 10, 11, 12, 13, 14)
- utiliza método: [[Transformer|Transformers]] — 31 ocorrências (p. 7, 11, 13, 15, 16)
- utiliza método: [[UNet|U-Net]] — 24 ocorrências (p. 13, 14, 17, 19, 20)
- utiliza método: [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 20 ocorrências (p. 1, 20, 21, 22, 23)
- utiliza método: [[OBIA|Análise baseada em objetos (OBIA)]] — 14 ocorrências (p. 2, 15, 17, 18, 19)
- é avaliado por: [[EstimativaArea|Estimativa de área com intervalo de confiança]] — 3 ocorrências (p. 7, 14)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 87 ocorrências (p. 1, 3, 6, 8, 11)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 48 ocorrências (p. 1, 5, 6, 18, 20)
- aplica etapa de preparo: [[IndicesEspectrais|Índices espectrais (NDVI etc.)]] — 21 ocorrências (p. 5, 7, 9, 16, 17)
- aplica etapa de preparo: [[Normalizacao|Normalização e escala radiométrica]] — 14 ocorrências (p. 6, 7, 8, 9, 14)
- aplica etapa de preparo: [[SegmentacaoObjetos|Segmentação em objetos (SNIC/superpixels)]] — 4 ocorrências (p. 19, 20)
- adota desenho de validação: [[Generalizacao|Generalização e domain shift]] — 3 ocorrências (p. 22, 27)
- trata a tarefa: [[SITS|Séries temporais de imagens (SITS)]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
