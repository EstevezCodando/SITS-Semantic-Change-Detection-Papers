---
tipo: artigo
id_origem: P148
titulo: "Self-Supervised Change Detection in Multiview Remote Sensing Images"
ano: 2021
autores: ["Yuxing Chen", "Lorenzo Bruzzone"]
doi: "10.1109/tgrs.2021.3089453"
arquivo_fonte: "coleta/P148_Chen2021_Self-Supervised-Change-Detection-in-Multiview-Remote-Sensing.pdf"
markdown_fonte: "output/pdf/P148_Chen2021_Self-Supervised-Change-Detection-in-Multiview-Remote-Sensing/document.md"
paginas: 13
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]"]
sensores: ["[[SAR|Radar (SAR)]]", "[[Sentinel1|Sentinel-1]]", "[[Sentinel2|Sentinel-2]]"]
conjuntos_dados: ["[[OSCD|OSCD]]"]
metodos: ["[[RedeSiamesa|Redes siamesas]]", "[[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]]", "[[CNN|Redes convolucionais (CNN)]]", "[[UNet|U-Net]]"]
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]", "[[Rotulagem|Rotulagem e anotação]]", "[[Normalizacao|Normalização e escala radiométrica]]"]
validacao: ["[[AcuraciaGlobal|Acurácia global (OA)]]", "[[PrecisaoRecall|Precisão e recall]]", "[[F1|F1]]", "[[Kappa|Coeficiente kappa]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Chen 2021 — Self-Supervised Change Detection in Multiview Remote Sensing Images

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Yuxing Chen, Lorenzo Bruzzone (2021). Self-Supervised Change Detection in Multiview Remote Sensing Images. IEEE Transactions on Geoscience and Remote Sensing. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1109/tgrs.2021.3089453
- **Arquivo de origem:** `coleta/P148_Chen2021_Self-Supervised-Change-Detection-in-Multiview-Remote-Sensing.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P148_Chen2021_Self-Supervised-Change-Detection-in-Multiview-Remote-Sensing/document.md` — 13 páginas, 6 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “In this work, we present an approach to perform unsupervised change detection in multi-view remote sensing images, such as multi-temporal and multi-sensor images.” (p. 2, seção I. I NTRODUCTION)
- “In addition, we introduce a change score that can accurately model the feature distance between bi-temporal images.” (p. 2, seção I. I NTRODUCTION)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “1) OSCD S2S2/ S1S1/ S1S2/ L8S2: The Onera Satellite Change Detection (OSCD) dataset was created for bitemporal change detection using Sentinel-2 images acquired between 2015 and 2018.” (p. 6, seção IV. E XPERIMENTAL R ESULTS)
- “To use this dataset in self-supervised training, we downloaded additional Sentinel-2 images in the same location as the original bi-temporal images between 2016 and 2020.” (p. 6, seção IV. E XPERIMENTAL R ESULTS)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **SAR**: 15 ocorrências (p. 1, 3, 6, 7, 10)
- sensor/produto **Sentinel-1**: 13 ocorrências (p. 1, 6, 7, 10, 11)
- sensor/produto **Sentinel-2**: 12 ocorrências (p. 1, 6, 7, 8, 9)
- sensor/produto **Landsat**: 12 ocorrências (p. 1, 6, 7, 9, 11)
- conjunto de dados **OSCD**: 45 ocorrências (p. 6, 7, 8, 9, 10)
- resolução mencionada: 10 m (p. 6)
- resolução mencionada: 60 m (p. 6)
- resolução mencionada: 15 m (p. 6)
- “A possible example of this is the joint use of Sentinel-2 and Landsat-8 images for a regular and timely monitoring of burned areas .” (p. 1, seção I. I NTRODUCTION)
- “1) OSCD S2S2/ S1S1/ S1S2/ L8S2: The Onera Satellite Change Detection (OSCD) dataset was created for bitemporal change detection using Sentinel-2 images acquired between 2015 and 2018.” (p. 6, seção IV. E XPERIMENTAL R ESULTS)
- “The pixelwise ground truth labels, which were manually annotated, were also provided for each pair but with some errors due to the relatively limited resolution of Sentinel-2 images.” (p. 6, seção IV. E XPERIMENTAL R ESULTS)
- “Recent researches in contrastive self-supervised learning – encourage the network to learn more interpretable and meaningful feature representations.” (p. 2, seção I. I NTRODUCTION)
- “The dataset consists of 24 pairs of multispectral images and the corresponding pixel-wise ground truth acquired in different cities and including different landscapes.” (p. 6, seção IV. E XPERIMENTAL R ESULTS)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 21 ocorrências (p. 1, 2, 3, 5, 7)
- **Rotulagem / anotação**: 14 ocorrências (p. 1, 6, 7, 8)
- **Normalização / escala**: 6 ocorrências (p. 3, 4, 5)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal e série (auto: 50 pares; 30 série)
**Métodos detectados automaticamente:**
- método/família **Rede siamesa**: 30 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Semi/auto-supervisionado**: 19 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **CNN**: 6 ocorrências (p. 1, 2, 6, 13)
- método/família **U-Net**: 3 ocorrências (p. 6, 9, 13)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- métrica **Acurácia global**: 16 ocorrências (p. 7, 8, 9, 10, 11)
- métrica **Precisão/Recall**: 11 ocorrências (p. 7, 8, 9, 11)
- métrica **F1**: 7 ocorrências (p. 7, 8, 9, 11)
- métrica **Kappa**: 7 ocorrências (p. 7, 8, 9, 11)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “Dataset Method Prec(%) Rec(%) OA(%) F1 Kap SCCN 7.38 22.45 68.54 0.11 S1S2 CAA 21.91 28.71 84.79 0.25 0.17 Prop.” (p. 11, seção 2 image pair (OSCD S1S2) and a Sentinel-1/Landsat-)

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 12)
- declaração: “A CKNOWLEDGMENT The authors would like to thank Yuanlong Tian and Thalles Silva for their open-source code in their work.” (p. 12)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Falsos alertas 11 (p. 7, 8, 9, 10, 11); Sistema operacional 1 (p. 1)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[SAR|Radar (SAR)]] — 15 ocorrências (p. 1, 3, 6, 7, 10)
- utiliza dado/sensor: [[Sentinel1|Sentinel-1]] — 13 ocorrências (p. 1, 6, 7, 10, 11)
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 12 ocorrências (p. 1, 6, 7, 8, 9)
- emprega conjunto de dados: [[OSCD|OSCD]] — 45 ocorrências (p. 6, 7, 8, 9, 10)
- utiliza método: [[RedeSiamesa|Redes siamesas]] — 30 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 19 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 6 ocorrências (p. 1, 2, 6, 13)
- utiliza método: [[UNet|U-Net]] — 3 ocorrências (p. 6, 9, 13)
- é avaliado por: [[AcuraciaGlobal|Acurácia global (OA)]] — 16 ocorrências (p. 7, 8, 9, 10, 11)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 11 ocorrências (p. 7, 8, 9, 11)
- é avaliado por: [[F1|F1]] — 7 ocorrências (p. 7, 8, 9, 11)
- é avaliado por: [[Kappa|Coeficiente kappa]] — 7 ocorrências (p. 7, 8, 9, 11)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 21 ocorrências (p. 1, 2, 3, 5, 7)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 14 ocorrências (p. 1, 6, 7, 8)
- aplica etapa de preparo: [[Normalizacao|Normalização e escala radiométrica]] — 6 ocorrências (p. 3, 4, 5)
- discute aspecto de monitoramento: [[FalsosAlertas|Falsos alertas]] — 11 ocorrências (p. 7, 8, 9, 10, 11)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
