---
tipo: artigo
id_origem: P15
titulo: "Panoptic Segmentation of Satellite Image Time Series With Convolutional Temporal Attention Networks"
ano: 2021
autores: ["Vivien Sainte Fare Garnot", "Loïc Landrieu"]
doi: "10.1109/iccv48922.2021.00483"
arquivo_fonte: "coleta/P15_Garnot2021_Panoptic-Segmentation-of-Satellite-Image-Time-Series-With-Co.pdf"
markdown_fonte: "output/pdf/P15_Garnot2021_Panoptic-Segmentation-of-Satellite-Image-Time-Series-With-Co/document.md"
paginas: 17
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[SITS|Séries temporais de imagens (SITS)]]"]
sensores: []
conjuntos_dados: []
metodos: ["[[LSTM|Redes recorrentes (LSTM)]]", "[[UNet|U-Net]]", "[[UTAE|U-TAE (U-Net com atenção temporal)]]", "[[CNN|Redes convolucionais (CNN)]]"]
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]", "[[Rotulagem|Rotulagem e anotação]]", "[[MascaraNuvem|Máscara de nuvem e sombra]]", "[[Normalizacao|Normalização e escala radiométrica]]"]
validacao: ["[[IoU|IoU / mIoU]]", "[[AcuraciaGlobal|Acurácia global (OA)]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Garnot 2021 — Panoptic Segmentation of Satellite Image Time Series With Convolutional Temporal Attention Networks

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Vivien Sainte Fare Garnot, Loïc Landrieu (2021). Panoptic Segmentation of Satellite Image Time Series With Convolutional Temporal Attention Networks. IEEE. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1109/iccv48922.2021.00483
- **Arquivo de origem:** `coleta/P15_Garnot2021_Panoptic-Segmentation-of-Satellite-Image-Time-Series-With-Co.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P15_Garnot2021_Panoptic-Segmentation-of-Satellite-Image-Time-Series-With-Co/document.md` — 17 páginas, 138 recortes de figuras, 1 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Unprecedented access to multi-temporal satellite im- agery has opened new perspectives for a variety of Earth observation tasks. Among them, pixel-precise panoptic seg- mentation of agricultural parcels has major economic and environmental implications. While researchers have ex- plored this problem for single images, we argue that the complex temporal patterns of crop phenology are better ad- dressed with temporal sequences of images. In this pa- per, we present the first end-to-end, single-stage method for panoptic segmentation of Satellite Image Time Series (SITS). This module can be combined with our novel image sequence encoding network which relies on temporal self- attention to extract rich and adaptive multi-scale spatio- temporal features. We also introduce PASTIS, the first open- access SITS dataset with panoptic annotations. We demon- strate the superiority of our encoder for …

- “In this pa- per, we present the first end-to-end, single-stage method for panoptic segmentation of Satellite Image Time Series (SITS).” (p. 1, seção Abstract)
- “We propose an end-to-end, singlestage model for panoptic segmentation of agricultural parcels from time series of satellite images.” (p. 1, seção 1. Introduction)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “Each sequence contains between 38 and 61 observations taken between September 2018 and November 2019, for a total of over 2 billion pixels.” (p. 6, seção 4.1. The PASTIS Dataset)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-2**: 2 ocorrências (p. 6, 8)
- “PASTIS is comprised of 2 433 sequences of multi-spectral images of shape 10 × 128 × 128.” (p. 6, seção 4.1. The PASTIS Dataset)
- “We report for our method and six competing methods the model size in trainable parameters, Overall Accuracy (OA), mean Intersection over Union (mIoU), and Inference Time for one fold of ∼ 490 sequences (IT).” (p. 7, seção 4.2. Semantic Segmentation)
- “Inference on 490 sequences takes 129s: 26s to generate U-TAE embeddings, 1s for the heatmap and saliency, 90s for instance proposals, and 12s to merge them into a panoptic segmentation.” (p. 8, seção 4.3. Panoptic Segmentation)
- “The feature maps are projected in RGB space to help visual interpretation. the temporal dimension of the resulting sequence of feature maps into a single map for each level, (c) a spatial convolutional decoder produces a single feature map ” (p. 3, seção 3.1. Spatio-Temporal Encoding)
- “The ground truth instance masks (a) is used to construct a target heatmap (b).” (p. 4, seção 3.1. Spatio-Temporal Encoding)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 20 ocorrências (p. 1, 5, 6, 7, 8)
- **Rotulagem / anotação**: 10 ocorrências (p. 1, 2, 4, 6, 7)
- **Máscara de nuvem e sombra**: 5 ocorrências (p. 1, 6, 8)
- **Normalização / escala**: 5 ocorrências (p. 3, 5, 7, 8)
- **Reamostragem**: 2 ocorrências (p. 4, 6)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 78 menções vs 0 de pares)
**Métodos detectados automaticamente:**
- método/família **LSTM / recorrente**: 20 ocorrências (p. 2, 3, 7, 8)
- método/família **U-Net**: 12 ocorrências (p. 2, 3, 4, 7, 8)
- método/família **U-TAE**: 9 ocorrências (p. 2, 6, 7, 8)
- método/família **CNN**: 3 ocorrências (p. 6, 8)
**Hiperparâmetros detectados automaticamente (verificar):**
- perda: “cross-entropy loss, and the size prediction with a no” (p. 5)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Validação cruzada**: 2 ocorrências (p. 7, 8)
- métrica **IoU**: 5 ocorrências (p. 7, 8)
- métrica **Acurácia global**: 3 ocorrências (p. 7, 8)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “The French Payment Agency estimates the accuracy of the crop annotations via in situ control over 98% and the relative error in terms of surfaces under 0 .” (p. 7, seção 4.1. The PASTIS Dataset)

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/VSainteuf/utae-paps (p. 1)
- URL citada: https://github.com/VSainteuf/utae-paps (p. 1)
- URL citada: https://github.com/VSainteuf/pastis-benchmark (p. 6)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Latência / frequência 1 (p. 1); Revisão humana 1 (p. 3)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza método: [[LSTM|Redes recorrentes (LSTM)]] — 20 ocorrências (p. 2, 3, 7, 8)
- utiliza método: [[UNet|U-Net]] — 12 ocorrências (p. 2, 3, 4, 7, 8)
- utiliza método: [[UTAE|U-TAE (U-Net com atenção temporal)]] — 9 ocorrências (p. 2, 6, 7, 8)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 3 ocorrências (p. 6, 8)
- é avaliado por: [[IoU|IoU / mIoU]] — 5 ocorrências (p. 7, 8)
- é avaliado por: [[AcuraciaGlobal|Acurácia global (OA)]] — 3 ocorrências (p. 7, 8)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 20 ocorrências (p. 1, 5, 6, 7, 8)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 10 ocorrências (p. 1, 2, 4, 6, 7)
- aplica etapa de preparo: [[MascaraNuvem|Máscara de nuvem e sombra]] — 5 ocorrências (p. 1, 6, 8)
- aplica etapa de preparo: [[Normalizacao|Normalização e escala radiométrica]] — 5 ocorrências (p. 3, 5, 7, 8)
- trata a tarefa: [[SITS|Séries temporais de imagens (SITS)]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
