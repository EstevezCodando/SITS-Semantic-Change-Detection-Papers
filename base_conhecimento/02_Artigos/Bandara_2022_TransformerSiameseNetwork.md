---
tipo: artigo
id_origem: P26
titulo: "A Transformer-Based Siamese Network for Change Detection"
ano: 2022
autores: ["Wele Gedara Chaminda Bandara", "Vishal M. Patel"]
doi: "10.48550/arXiv.2201.01293"
arquivo_fonte: "coleta/P26_Bandara2022_A-Transformer-Based-Siamese-Network-for-Change-Detection.pdf"
markdown_fonte: "output/pdf/P26_Bandara2022_A-Transformer-Based-Siamese-Network-for-Change-Detection/document.md"
paginas: 5
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]"]
sensores: []
conjuntos_dados: ["[[LEVIRCD|LEVIR-CD]]"]
metodos: ["[[Transformer|Transformers]]", "[[RedeSiamesa|Redes siamesas]]"]
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]"]
validacao: ["[[AcuraciaGlobal|Acurácia global (OA)]]", "[[F1|F1]]", "[[IoU|IoU / mIoU]]", "[[PrecisaoRecall|Precisão e recall]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Bandara 2022 — A Transformer-Based Siamese Network for Change Detection

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Wele Gedara Chaminda Bandara, Vishal M. Patel (2022). A Transformer-Based Siamese Network for Change Detection. IEEE International Geoscience and Remote Sensing Symposium (IGARSS). Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2201.01293
- **Arquivo de origem:** `coleta/P26_Bandara2022_A-Transformer-Based-Siamese-Network-for-Change-Detection.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P26_Bandara2022_A-Transformer-Based-Siamese-Network-for-Change-Detection/document.md` — 5 páginas, 40 recortes de figuras, 1 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** This paper presents a transformer-based Siamese network architecture (abbreviated by ChangeFormer ) for Change Detection (CD) from a pair of co-registered remote sensing images. Different from recent CD frameworks, which are based on fully convolutional networks (ConvNets), the proposed method unifies hierarchically structured transformer encoder with Multi-Layer Perception (MLP) decoder in a Siamese network architecture to efficiently render multi-scale long-range details required for accurate CD. Experiments on two CD datasets show that the proposed end-to-end trainable ChangeFormer architecture achieves better CD performance than previous counterparts. Our code and pre-trained models are available at github . com / [wgcban](https://github.com/wgcban/ChangeFormer) / ChangeFormer . Index Terms — Change detection, transformer Siamese network, attention mechanism, multilayer perceptron, r…

- “This paper presents a transformer-based Siamese network architecture (abbreviated by ChangeFormer ) for Change Detection (CD) from a pair of co-registered remote sensing images.” (p. 1, seção ABSTRACT)
- “In this section, we compare the CD performance of our ChangeFormer with existing SOTA methods: - FC-EF : concatenates bi-temporal images and processes them through a ConvNet to detect changes. - FC-Siam-Di : is a feature-difference method, ” (p. 3, seção 4. RESULTS AND DISCUSSION)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Imagens aéreas**: 2 ocorrências (p. 5)
- conjunto de dados **LEVIR-CD**: 7 ocorrências (p. 3, 4)
- “For experiments, we create non-overlapping patches of size 256 × 256 from the 512 × 512 images while utilizing the authors’ default train/val/test sets.” (p. 3, seção 3.1. Datasets)
- “This results in 14400/1360/192 samples for training/val/test, respectively, for the DSIFN dataset.” (p. 3, seção 3.1. Datasets)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 5 ocorrências (p. 2, 3)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal / pares (auto: 10 menções)
**Métodos detectados automaticamente:**
- método/família **Transformer**: 55 ocorrências (p. 1, 2, 4, 5)
- método/família **Rede siamesa**: 14 ocorrências (p. 1, 3, 4, 5)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate is initially set to 0.0001 and linearly decays to ” (p. 3)
- batch: “batch size of 16 to train the model” (p. 3)
- épocas/iterações: “200 epochs” (p. 3)
- otimizador: “AdamW optimizer with weight decay equal to 0” (p. 3)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 3 ocorrências (p. 3)
- métrica **Acurácia global**: 7 ocorrências (p. 3, 4)
- métrica **F1**: 6 ocorrências (p. 3, 4)
- métrica **IoU**: 6 ocorrências (p. 3, 4)
- métrica **Precisão/Recall**: 6 ocorrências (p. 3, 4)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “Even though the attention-based methods are effective in capturing global details, they struggle to relate long-range details in space-time because they use attention to re-weight the bi-temporal features obtained through ConvNets in the ch” (p. 1, seção 1. INTRODUCTION)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/wgcban/ChangeFormer (p. 1)
- URL citada: https://github.com/wgcban/ChangeFormer (p. 1)
- declaração: “Our code and pre-trained models are available at github . com / [wgcban](https://github.com/wgcban/ChangeFormer) / ChangeFormer .” (p. 1)
- hiperparâmetros **não detectados** automaticamente: perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- emprega conjunto de dados: [[LEVIRCD|LEVIR-CD]] — 7 ocorrências (p. 3, 4)
- utiliza método: [[Transformer|Transformers]] — 55 ocorrências (p. 1, 2, 4, 5)
- utiliza método: [[RedeSiamesa|Redes siamesas]] — 14 ocorrências (p. 1, 3, 4, 5)
- é avaliado por: [[AcuraciaGlobal|Acurácia global (OA)]] — 7 ocorrências (p. 3, 4)
- é avaliado por: [[F1|F1]] — 6 ocorrências (p. 3, 4)
- é avaliado por: [[IoU|IoU / mIoU]] — 6 ocorrências (p. 3, 4)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 6 ocorrências (p. 3, 4)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 5 ocorrências (p. 2, 3)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
