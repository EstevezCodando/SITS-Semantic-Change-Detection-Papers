---
tipo: artigo
id_origem: P175
titulo: "AN END-TO-END DEEP LEARNING WORKFLOW FOR BUILDING SEGMENTATION, BOUNDARY REGULARIZATION AND VECTORIZATION OF BUILDING FOOTPRINTS"
ano: 2023
autores: ["Simon Šanca", "Sander Riisøen Jyhne", "Michele Gazzea", "Reza Arghandeh"]
doi: "10.5194/isprs-archives-xlviii-4-w7-2023-169-2023"
arquivo_fonte: "coleta/P175_Sanca2023_AN-END-TO-END-DEEP-LEARNING-WORKFLOW-FOR-BUILDING-SEGMENTATI.pdf"
markdown_fonte: "output/pdf/P175_Sanca2023_AN-END-TO-END-DEEP-LEARNING-WORKFLOW-FOR-BUILDING-SEGMENTATI/document.md"
paginas: 7
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[Edificacoes|Edificações e urbanização]]"]
sensores: ["[[ImagensAereas|Imagens aéreas]]"]
conjuntos_dados: []
metodos: ["[[Transformer|Transformers]]", "[[UNet|U-Net]]", "[[CNN|Redes convolucionais (CNN)]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Sanca 2023 — AN END-TO-END DEEP LEARNING WORKFLOW FOR BUILDING SEGMENTATION, BOUNDARY REGULARIZATION AND VECTORIZATION OF BUILDING FOOTPRINTS

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Simon Šanca, Sander Riisøen Jyhne, Michele Gazzea, Reza Arghandeh (2023). AN END-TO-END DEEP LEARNING WORKFLOW FOR BUILDING SEGMENTATION, BOUNDARY REGULARIZATION AND VECTORIZATION OF BUILDING FOOTPRINTS. The international archives of the photogrammetry, remote sensing and spatial information sciences. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.5194/isprs-archives-xlviii-4-w7-2023-169-2023
- **Arquivo de origem:** `coleta/P175_Sanca2023_AN-END-TO-END-DEEP-LEARNING-WORKFLOW-FOR-BUILDING-SEGMENTATI.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P175_Sanca2023_AN-END-TO-END-DEEP-LEARNING-WORKFLOW-FOR-BUILDING-SEGMENTATI/document.md` — 7 páginas, 6 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “To address this issue, we propose an end-to-end workflow that utilizes binary semantic segmentation, regularization, and vectorization.” (p. 1, seção 2 Norwegian Mapping Authority, Hønefoss, Norway - sander.jyh)
- “The purpose of our research is to develop an end-to-end workflow for accurate segmentation of building footprints including three major steps: (1) binary semantic segmentation with a CNN, (2) applying building boundary regularization and (3” (p. 1, seção 2 Norwegian Mapping Authority, Hønefoss, Norway - sander.jyh)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Imagens aéreas**: 3 ocorrências (p. 2, 3)
- resolução mencionada: 0.25 m (p. 2)
- “Predictions were performed on test set 1 on 1369 images.” (p. 3, seção 2. Second, we apply projectRegularization proposed by (Zorzi)
- “Both instance and semantic segmentation is trained in a supervised manner using image and ground truth pairs.” (p. 2, seção 2 Norwegian Mapping Authority, Hønefoss, Norway - sander.jyh)
- “Hyperparameters used during training We used the Adam optimizer with Binary Cross Entropy Loss with logits during training to measure the difference between the predicted output and the ground truth.” (p. 4, seção 2. Second, we apply projectRegularization proposed by (Zorzi)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 8 ocorrências (p. 1, 2, 3, 4, 5)
- **Normalização / escala**: 2 ocorrências (p. 2)
- **Recorte em patches/tiles**: 2 ocorrências (p. 3, 5)
- **Aumento de dados**: 2 ocorrências (p. 5)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **Transformer**: 20 ocorrências (p. 1, 2, 3, 5)
- método/família **U-Net**: 18 ocorrências (p. 1, 2, 3, 5)
- método/família **CNN**: 17 ocorrências (p. 1, 2, 3)
**Hiperparâmetros detectados automaticamente (verificar):**
- batch: “batch size, y i is the ground truth image for samp” (p. 4)
- otimizador: “Adam optimizer with Binary Cross Entropy Los” (p. 4)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 10 ocorrências (p. 2, 3)
- métrica **IoU**: 15 ocorrências (p. 4, 5, 7)
- métrica **Precisão/Recall**: 4 ocorrências (p. 1, 2, 4)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “We conclude that projectRegularization additionally improves the segmentation accuracy by an average value of 0.55 IoU, 0.35 in BIoU and 0.44 in S metric.” (p. 7, seção 5. The discriminator D estimates whether the regul)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “In contrary, the tested regularization method can help to improve the geometry of the buildings, but cannot be used to significantly improve the prediction accuracy.” (p. 5, seção 5. The discriminator D estimates whether the regularized ima)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/WangLibo1995/GeoSeg (p. 2)
- URL citada: https://github.com/WangLibo1995/GeoSeg (p. 2)
- URL citada: https://github.com/zorzi-s/projectRegularization (p. 2)
- URL citada: https://huggingface.co/datasets/sjyhne/mapai (p. 3)
- URL citada: https://huggingface.co/datasets/sjyhne/mapaidataset (p. 3)
- declaração: “The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, Volume XLVIII-4/W7-2023 FOSS4G (Free and Open Source Software for Geospatial) 2023 – Academic Track, 26 June–2 July 2023, Prizren, Kosovo AN ” (p. 1)
- declaração: “We have developed an implementation for building segmentation using open-source software libraries including Python, PyTorch, the Geospatial Data Abstraction Library (GDAL), QGIS and QtDesigner.” (p. 1)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, épocas/iterações, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 1 (p. 3)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[ImagensAereas|Imagens aéreas]] — 3 ocorrências (p. 2, 3)
- utiliza método: [[Transformer|Transformers]] — 20 ocorrências (p. 1, 2, 3, 5)
- utiliza método: [[UNet|U-Net]] — 18 ocorrências (p. 1, 2, 3, 5)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 17 ocorrências (p. 1, 2, 3)
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
