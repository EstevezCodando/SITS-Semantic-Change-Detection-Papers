---
tipo: artigo
id_origem: P100
titulo: "Detection of rural roads from planet images using convolutional neural networks"
ano: 2025
autores: ["Jorgiana Kamila Teixeira do Crato", "Mário Ernesto Jijón-Palma", "Jorge Antônio Silva Centeno"]
doi: "10.1590/s1982-21702025000100004"
arquivo_fonte: "coleta/P100_Crato2025_Detection-of-rural-roads-from-planet-images-using-convolutio.pdf"
markdown_fonte: "output/pdf/P100_Crato2025_Detection-of-rural-roads-from-planet-images-using-convolutio/document.md"
paginas: 15
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Vias|Vias e estradas]]"]
sensores: ["[[PlanetProdutos|Produtos Planet (visão geral)]]"]
conjuntos_dados: []
metodos: ["[[UNet|U-Net]]", "[[CNN|Redes convolucionais (CNN)]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]"]
validacao: ["[[PrecisaoRecall|Precisão e recall]]", "[[IoU|IoU / mIoU]]", "[[F1|F1]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Crato 2025 — Detection of rural roads from planet images using convolutional neural networks

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Jorgiana Kamila Teixeira do Crato, Mário Ernesto Jijón-Palma, Jorge Antônio Silva Centeno (2025). Detection of rural roads from planet images using convolutional neural networks. Boletim de Ciências Geodésicas. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1590/s1982-21702025000100004
- **Arquivo de origem:** `coleta/P100_Crato2025_Detection-of-rural-roads-from-planet-images-using-convolutio.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P100_Crato2025_Detection-of-rural-roads-from-planet-images-using-convolutio/document.md` — 15 páginas, 15 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “This study proposes to use high-resolution satellite images from Planet constellation, in conjunction with artificial intelligence, specifically UNet, to automatically identify rural roads in the metropolitan region of Curitiba, Paraná, Bra” (p. 1, seção Início)
- “Moreover, convolutional networks can be employed for the purpose of mapping roads in images.” (p. 2, seção 1. Introduction)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “Detection of rural roads from planet images using convolutional neural networks 4 Figure 1: Location map of the study area.” (p. 4, seção 2. Material and Method)
- “A) Presents the study area, containing the scenes used in this study in relation to the municipality of Curitiba.” (p. 4, seção 2. Material and Method)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Planet (mosaicos e cenas)**: 10 ocorrências (p. 1, 3, 4, 13)
- sensor/produto **Planet NICFI**: 2 ocorrências (p. 3)
- resolução mencionada: 4.7 m (p. 3)
- resolução mencionada: 5 m (p. 13)
- “The training set was obtained from 10 scenes out of 12 scenes acquired on May 21, 2022.” (p. 7, seção 2.1.1 Preprocessing)
- “The training set consists of 9760 samples, where 70% of the samples were used to adjust the parameters of the net and the remaining samples (30%) were used as test samples.” (p. 8, seção 2.1.2 Processing)
- “The validation of the net was performed with a new set of 1783 samples not used during training.” (p. 8, seção 2.1.2 Processing)
- “The Google Colab platform was used with the python language interpreter to develop the necessary programs.” (p. 4, seção 2. Material and Method)
- “The initial stage of the process entails a visual examination of the image, with the purpose of generating a ground truth map, which will be utilized in the subsequent stages.” (p. 5, seção 2.1.1 Preprocessing)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 20 ocorrências (p. 5, 6, 8, 10, 12)
- **Índices espectrais**: 2 ocorrências (p. 13, 14)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **U-Net**: 30 ocorrências (p. 1, 2, 3, 5, 6)
- método/família **CNN**: 15 ocorrências (p. 1, 2, 4, 6, 8)
**Hiperparâmetros detectados automaticamente (verificar):**
- batch: “batch size, Epochs), the number of neurons influen” (p. 9)
- épocas/iterações: “50 epochs” (p. 7)
- tamanho do patch: “41x41 pixel” (p. 6)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- métrica **Precisão/Recall**: 15 ocorrências (p. 1, 2, 3, 8, 9)
- métrica **IoU**: 10 ocorrências (p. 8, 9, 10, 13)
- métrica **F1**: 9 ocorrências (p. 1, 8, 9, 10, 12)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “Parameters Test 1 Test 2 Epochs 50 50 Batch Size 32 32 Neurons 16 32 Accuracy 91.85% 91.95% Precision 75.80% 75.83% Recall 63.71% 65.92% F1-Score 68.99% 69.07% mIoU 53.94% 55.01% Time 04h:53min 06:08min Boletim de Ciências Geodésicas, 31: e2025004, 2025” (p. 9, seção 3. Results and Discussion)
- “Detection of rural roads from planet images using convolutional neural networks 10 The benefits were notably limited: a gain of only 0.10% in accuracy, 0.03% in precision, and 0.08% in F1-Score.” (p. 10, seção 3. Results and Discussion)
- “Even for metrics where the improvement was a little more significant, such as Recall, which showed an increase of 2.21%, and mIoU, with an improvement of 1.07%, the gain is still considered low.” (p. 10, seção 3. Results and Discussion)
- “Considering the quality metrics, the accuracy lies above 90%, which is relatively high.” (p. 10, seção 3. Results and Discussion)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “The deployment of the UNet in conjunction with these images facilitates the automated identification and mapping of roads in rural areas with high precision, offering an efficient alternative to traditional manual delimitation methods.” (p. 3, seção 1. Introduction)
- “Despite the limitations of using the GPU in the Colab environment, it has great applicability in the field of machine learning, as it includes many machine-learning libraries in Python.” (p. 4, seção 2. Material and Method)
- “It is a commercial platform designed to offer a programming environment, but with limitations for free use.” (p. 12, seção 3. Results and Discussion)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 3)
- declaração: “Additionally, the data are available at a monthly temporal resolution.” (p. 3)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 3 (p. 1, 9)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[PlanetProdutos|Produtos Planet (visão geral)]] — 10 ocorrências (p. 1, 3, 4, 13)
- utiliza método: [[UNet|U-Net]] — 30 ocorrências (p. 1, 2, 3, 5, 6)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 15 ocorrências (p. 1, 2, 4, 6, 8)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 15 ocorrências (p. 1, 2, 3, 8, 9)
- é avaliado por: [[IoU|IoU / mIoU]] — 10 ocorrências (p. 8, 9, 10, 13)
- é avaliado por: [[F1|F1]] — 9 ocorrências (p. 1, 8, 9, 10, 12)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 20 ocorrências (p. 5, 6, 8, 10, 12)
- trata a tarefa: [[Vias|Vias e estradas]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
