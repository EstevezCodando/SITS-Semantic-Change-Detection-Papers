---
tipo: artigo
id_origem: P38
titulo: "Fully Convolutional Network for Automatic Road Extraction From Satellite Imagery"
ano: 2018
autores: ["Alexander Pavlovich Buslaev", "Selim Seferbekov", "Vladimir Iglovikov", "Alexey A. Shvets"]
doi: "10.1109/cvprw.2018.00035"
arquivo_fonte: "coleta/P38_Buslaev2018_Fully-Convolutional-Network-for-Automatic-Road-Extraction-Fr.pdf"
markdown_fonte: "output/pdf/P38_Buslaev2018_Fully-Convolutional-Network-for-Automatic-Road-Extraction-Fr/document.md"
paginas: 4
tipo_documento: "artigo curto (≤4 páginas; verificar)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Vias|Vias e estradas]]"]
sensores: []
conjuntos_dados: []
metodos: ["[[UNet|U-Net]]"]
preparo: ["[[AumentoDados|Aumento de dados]]", "[[Rotulagem|Rotulagem e anotação]]"]
validacao: ["[[IoU|IoU / mIoU]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Buslaev 2018 — Fully Convolutional Network for Automatic Road Extraction From Satellite Imagery

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Alexander Pavlovich Buslaev, Selim Seferbekov, Vladimir Iglovikov, Alexey A. Shvets (2018). Fully Convolutional Network for Automatic Road Extraction From Satellite Imagery. IEEE. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1109/cvprw.2018.00035
- **Arquivo de origem:** `coleta/P38_Buslaev2018_Fully-Convolutional-Network-for-Automatic-Road-Extraction-Fr.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P38_Buslaev2018_Fully-Convolutional-Network-for-Automatic-Road-Extraction-Fr/document.md` — 4 páginas, 2 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo curto (≤4 páginas; verificar).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Analysis of high-resolution satellite images has been an important research topic for traffic management, city plan- ning, and road monitoring. One of the problems here is automatic and precise road extraction. From an original image, it is difficult and computationally expensive to ex- tract roads due to presences of other road-like features with straight edges. In this paper, we propose an approach for automatic road extraction based on a fully convolutional neural network of U-net family. This network consists of ResNet-34 pre-trained on ImageNet and decoder adapted from vanilla U-Net. Based on validation results, leader- board and our own experience this network shows superior results for the DEEPGLOBE - CVPR 2018 road extraction sub-challenge. Moreover, this network uses moderate mem- ory that allows using just one GTX 1080 or 1080ti video cards to perform whole training and makes p…

- “In this paper, we propose an approach for automatic road extraction based on a fully convolutional neural network of U-net family.” (p. 1, seção Abstract)
- “We developed a binary segmentation model using the encoder-decoder network with skip connections.” (p. 3, seção 5. Conclusions)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Imagens aéreas**: 2 ocorrências (p. 1)
- resolução mencionada: 50 cm (p. 2)
- “One video card GTX1080 Ti with 11 Gb of memory allows using the batch size of 8 images.” (p. 3, seção 4. Training)
- “It can be interpreted as a similarity measure between a finite number of sets.” (p. 2, seção 4. Training)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Aumento de dados**: 5 ocorrências (p. 3, 4)
- **Rotulagem / anotação**: 4 ocorrências (p. 2, 3, 4)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **U-Net**: 12 ocorrências (p. 1, 2, 3)
- método/família **CNN**: 4 ocorrências (p. 1)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate 1e-4 and decay 1e-4 ” (p. 3)
- batch: “batch size of 8 images” (p. 3)
- otimizador: “Adam optimizer with learning rate 1e-4 and d” (p. 3)
- perda: “binary cross entropy, while for a multi-class segmen” (p. 3)
- tamanho do patch: “1024x1024 pixel” (p. 2)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- métrica **IoU**: 3 ocorrências (p. 2, 3)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado
- hiperparâmetros **não detectados** automaticamente: épocas/iterações (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 1 (p. 2)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza método: [[UNet|U-Net]] — 12 ocorrências (p. 1, 2, 3)
- é avaliado por: [[IoU|IoU / mIoU]] — 3 ocorrências (p. 2, 3)
- aplica etapa de preparo: [[AumentoDados|Aumento de dados]] — 5 ocorrências (p. 3, 4)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 4 ocorrências (p. 2, 3, 4)
- trata a tarefa: [[Vias|Vias e estradas]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
