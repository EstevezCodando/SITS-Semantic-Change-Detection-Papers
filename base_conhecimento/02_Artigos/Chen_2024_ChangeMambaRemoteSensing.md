---
tipo: artigo
id_origem: P28
titulo: "ChangeMamba: Remote Sensing Change Detection With Spatiotemporal State Space Model"
ano: 2024
autores: ["Hongruixuan Chen", "Jian Hui Song", "Chengxi Han", "Junshi Xia", "Naoto Yokoya"]
doi: "10.48550/arXiv.2404.03425"
arquivo_fonte: "coleta/P28_Chen2024_ChangeMamba-Remote-Sensing-Change-Detection-With-Spatiotempo.pdf"
markdown_fonte: "output/pdf/P28_Chen2024_ChangeMamba-Remote-Sensing-Change-Detection-With-Spatiotempo/document.md"
paginas: 19
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]"]
sensores: ["[[ImagensAereas|Imagens aéreas]]"]
conjuntos_dados: ["[[xBD|xBD]]", "[[HRSCD|HRSCD]]", "[[LEVIRCD|LEVIR-CD]]", "[[WHUCD|WHU-CD]]"]
metodos: ["[[Transformer|Transformers]]", "[[Mamba|Mamba / modelos de espaço de estados]]", "[[CNN|Redes convolucionais (CNN)]]", "[[RedeSiamesa|Redes siamesas]]", "[[UNet|U-Net]]", "[[TransferLearning|Aprendizado por transferência]]"]
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]", "[[Rotulagem|Rotulagem e anotação]]", "[[Normalizacao|Normalização e escala radiométrica]]"]
validacao: ["[[DivisaoTreinoTeste|Divisão treino/validação/teste]]", "[[F1|F1]]", "[[IoU|IoU / mIoU]]", "[[AcuraciaGlobal|Acurácia global (OA)]]", "[[PrecisaoRecall|Precisão e recall]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Chen 2024 — ChangeMamba: Remote Sensing Change Detection With Spatiotemporal State Space Model

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Hongruixuan Chen, Jian Hui Song, Chengxi Han, Junshi Xia et al. (2024). ChangeMamba: Remote Sensing Change Detection With Spatiotemporal State Space Model. IEEE Transactions on Geoscience and Remote Sensing. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2404.03425
- **Arquivo de origem:** `coleta/P28_Chen2024_ChangeMamba-Remote-Sensing-Change-Detection-With-Spatiotempo.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P28_Chen2024_ChangeMamba-Remote-Sensing-Change-Detection-With-Spatiotempo/document.md` — 19 páginas, 254 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “For the change decoder, which is available in all three architectures, we propose three spatio-temporal relationship modeling mechanisms, which can be naturally combined with the Mamba architecture and fully utilize its attribute to achieve” (p. 1, seção Início)
- “In this paper, we present the first attempt at introducing Mamba architecture for CD tasks and propose several spatiotemporal state space models (collectively called ChangeMamba) to realize effective and robust CD.” (p. 2, seção I. I NTRODUCTION)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “Dataset Study site Number of image pairs Size Resolution Evaluation task SYSU Hong Kong 20,000 256 × 256 0.5m BCD (category-agnostic) LEVIR-CD+ Texas of the U.S.” (p. 9, seção 1 Mamba architectures sometimes are abbreviated as the S6 mo)
- “The aerial images captured in 2012 cover an area of 20.5 km , featuring 12,796 buildings, while the image captured in 2016 shows an increase to 16,077 buildings within the same area, reflecting significant urban development over the four-ye” (p. 9, seção IV. E XPERIMENTS A ND D ISCUSSIONS)
- “Datasets 1) SYSU-CD : This dataset is a category-agnostic CD dataset, which introduces a comprehensive collection of 20,000 pairs of 0.5 meter/pixel resolution aerial images from Hong Kong, spanning 2007 to 2014.” (p. 9, seção IV. E XPERIMENTS A ND D ISCUSSIONS)
- “It comprises two aerial datasets from Christchurch, New Zealand, captured in April 2012 and 2016, with a spatial resolution of 0.3 meters/pixel.” (p. 9, seção IV. E XPERIMENTS A ND D ISCUSSIONS)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Imagens aéreas**: 5 ocorrências (p. 9, 18)
- conjunto de dados **xBD**: 11 ocorrências (p. 3, 9, 10, 12, 13)
- conjunto de dados **HRSCD**: 9 ocorrências (p. 10, 13)
- conjunto de dados **LEVIR-CD**: 6 ocorrências (p. 9, 11, 17, 18)
- conjunto de dados **WHU-CD**: 6 ocorrências (p. 9, 11, 12)
- “For effective deep learning application, the dataset is structured into training, validation, and test sets following a 6:2:2 ratio, with 20,000 patches of 256 × 256.” (p. 9, seção IV. E XPERIMENTS A ND D ISCUSSIONS)
- “It can be seen that the proposed methods accurately detect changes with varying types, scales, and numbers contained in these image pairs, very close to the change reference maps.” (p. 11, seção IV. E XPERIMENTS A ND D ISCUSSIONS)
- “Firstly, we can find that the “from-to” transition matrices obtained by our methods are very close to the ground truth, demonstrating the effectiveness of our MambaSCD architecture again.” (p. 12, seção IV. E XPERIMENTS A ND D ISCUSSIONS)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 6 ocorrências (p. 1, 2, 3, 9, 19)
- **Rotulagem / anotação**: 4 ocorrências (p. 3, 9, 12)
- **Normalização / escala**: 3 ocorrências (p. 7, 15)
- **Aumento de dados**: 2 ocorrências (p. 9, 11)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 33 menções vs 10 de pares)
**Métodos detectados automaticamente:**
- método/família **Transformer**: 73 ocorrências (p. 1, 2, 3, 4, 6)
- método/família **Mamba**: 49 ocorrências (p. 1, 2, 4, 5, 6)
- método/família **CNN**: 32 ocorrências (p. 1, 2, 3, 4, 10)
- método/família **Rede siamesa**: 20 ocorrências (p. 2, 3, 5, 10, 14)
- método/família **U-Net**: 12 ocorrências (p. 3, 10, 14, 15, 17)
- método/família **Transfer learning**: 4 ocorrências (p. 2, 18, 19)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 1 e [−] and a weight decay of 5 e [−] ” (p. 9)
- batch: “batch size is set to 16” (p. 9)
- otimizador: “AdamW optimizer with a learning rate of 1 e [” (p. 9)
- perda: “focal loss , deep supervision , multi-scale traini” (p. 8)
- tamanho do patch: “1024 × 1024 pixel” (p. 9)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 8 ocorrências (p. 9, 11, 12, 13, 14)
- **Desbalanceamento**: 3 ocorrências (p. 8)
- métrica **F1**: 25 ocorrências (p. 10, 11, 12, 13, 16)
- métrica **IoU**: 12 ocorrências (p. 10, 11, 12, 13, 16)
- métrica **Acurácia global**: 12 ocorrências (p. 10, 11, 12, 13, 16)
- métrica **Precisão/Recall**: 3 ocorrências (p. 5, 10)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/ChenHongruixuan/MambaCD (p. 1)
- URL citada: https://github.com/ChenHongruixuan/MambaCD (p. 1)
- declaração: “The source code is available in [https://github.com/ChenHongruixuan/MambaCD.](https://github.com/ChenHongruixuan/MambaCD) Index Terms —State space model, Mamba, binary change de- tection, semantic change detection, building damage assessmen” (p. 1)
- declaração: “Type Method Rec Pre OA F1 IoU KC C T FC-EF 71.77 69.12 97.54 70.42 54.34 69.14 FC-Siam-Diff 74.02 81.49 98.26 77.57 63.36 76.67 FC-Siam-Conc 78.49 78.39 98.24 78.44 64.53 77.52 SiamCRNN-18 84.25 81.22 98.56 82.71 70.52 81.96 SiamCRNN-34 83.” (p. 11)
- hiperparâmetros **não detectados** automaticamente: épocas/iterações (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 6 (p. 2, 3, 13, 15, 17)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[ImagensAereas|Imagens aéreas]] — 5 ocorrências (p. 9, 18)
- emprega conjunto de dados: [[xBD|xBD]] — 11 ocorrências (p. 3, 9, 10, 12, 13)
- emprega conjunto de dados: [[HRSCD|HRSCD]] — 9 ocorrências (p. 10, 13)
- emprega conjunto de dados: [[LEVIRCD|LEVIR-CD]] — 6 ocorrências (p. 9, 11, 17, 18)
- emprega conjunto de dados: [[WHUCD|WHU-CD]] — 6 ocorrências (p. 9, 11, 12)
- utiliza método: [[Transformer|Transformers]] — 73 ocorrências (p. 1, 2, 3, 4, 6)
- utiliza método: [[Mamba|Mamba / modelos de espaço de estados]] — 49 ocorrências (p. 1, 2, 4, 5, 6)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 32 ocorrências (p. 1, 2, 3, 4, 10)
- utiliza método: [[RedeSiamesa|Redes siamesas]] — 20 ocorrências (p. 2, 3, 5, 10, 14)
- utiliza método: [[UNet|U-Net]] — 12 ocorrências (p. 3, 10, 14, 15, 17)
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 4 ocorrências (p. 2, 18, 19)
- é avaliado por: [[F1|F1]] — 25 ocorrências (p. 10, 11, 12, 13, 16)
- é avaliado por: [[IoU|IoU / mIoU]] — 12 ocorrências (p. 10, 11, 12, 13, 16)
- é avaliado por: [[AcuraciaGlobal|Acurácia global (OA)]] — 12 ocorrências (p. 10, 11, 12, 13, 16)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 3 ocorrências (p. 5, 10)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 6 ocorrências (p. 1, 2, 3, 9, 19)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 4 ocorrências (p. 3, 9, 12)
- aplica etapa de preparo: [[Normalizacao|Normalização e escala radiométrica]] — 3 ocorrências (p. 7, 15)
- adota desenho de validação: [[DivisaoTreinoTeste|Divisão treino/validação/teste]] — 8 ocorrências (p. 9, 11, 12, 13, 14)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
