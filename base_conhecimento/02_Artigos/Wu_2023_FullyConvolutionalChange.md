---
tipo: artigo
id_origem: P150
titulo: "Fully Convolutional Change Detection Framework With Generative Adversarial Network for Unsupervised, Weakly Supervised and Regional Supervised Change Detection"
ano: 2023
autores: ["Chen Wu", "Bo Du", "Liangpei Zhang"]
doi: "10.1109/tpami.2023.3237896"
arquivo_fonte: "coleta/P150_Wu2023_Fully-Convolutional-Change-Detection-Framework-With-Generati.pdf"
markdown_fonte: "output/pdf/P150_Wu2023_Fully-Convolutional-Change-Detection-Framework-With-Generati/document.md"
paginas: 13
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]"]
sensores: ["[[Sentinel2|Sentinel-2]]"]
conjuntos_dados: ["[[OSCD|OSCD]]"]
metodos: ["[[SupervisaoFraca|Supervisão fraca]]", "[[RedeSiamesa|Redes siamesas]]"]
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]", "[[Rotulagem|Rotulagem e anotação]]", "[[Normalizacao|Normalização e escala radiométrica]]"]
validacao: ["[[F1|F1]]", "[[AcuraciaGlobal|Acurácia global (OA)]]", "[[PrecisaoRecall|Precisão e recall]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Wu 2023 — Fully Convolutional Change Detection Framework With Generative Adversarial Network for Unsupervised, Weakly Supervised and Regional Supervised Change Detection

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Chen Wu, Bo Du, Liangpei Zhang (2023). Fully Convolutional Change Detection Framework With Generative Adversarial Network for Unsupervised, Weakly Supervised and Regional Supervised Change Detection. IEEE Transactions on Pattern Analysis and Machine Intelligence. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1109/tpami.2023.3237896
- **Arquivo de origem:** `coleta/P150_Wu2023_Fully-Convolutional-Change-Detection-Framework-With-Generati.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P150_Wu2023_Fully-Convolutional-Change-Detection-Framework-With-Generati/document.md` — 13 páginas, 113 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “Therefore, we proposed a fully convolutional change detection framework with generative adversarial network, to conclude unsupervised, weakly supervised, regional supervised, and fully supervised change detection tasks into one framework.” (p. 1, seção Início)
- “In order to conclude all these change detection tasks, in this paper, we propose a framework named fully convolutional change detection with generative adversarial network (FCD-GAN) for unsupervised, weakly supervised and regional supervise” (p. 2, seção 4. Fully Supervised CD)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “It aims at finding landscape changes from the multi-temporal remote sensing images observing the same study site at different time.” (p. 1, seção Início)
- “This dataset contains two aerial highresolution images, which were acquired in 2012 and 2016.” (p. 5, seção 2.4 Regional Supervised Change Detection)
- “Zhu et al., “A land cover change detection and classification protocol for updating Alaska NLCD 2001 to 2011,” Remote Sensing of Environment, vol.” (p. 11, seção 5.3 Limitation)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-2**: 3 ocorrências (p. 6, 9)
- sensor/produto **SAR**: 3 ocorrências (p. 12)
- sensor/produto **Landsat**: 2 ocorrências (p. 11)
- conjunto de dados **OSCD**: 9 ocorrências (p. 6, 8, 9, 10)
- resolução mencionada: 4 m (p. 5)
- resolução mencionada: 0.3 m (p. 5)
- resolução mencionada: 20 m (p. 6)
- “6 Changed (1) Unchanged (0) (a) (b) (c) (e) (f) (g) Figure 7 Samples for weakly supervised change detection, including a changed pair (a) before change, (b) after change, (c) reference, and an unchanged pair (c) before change, (b) after cha” (p. 6, seção 2.4 Regional Supervised Change Detection)
- “The task of fully supervised change de- tection (FSCD) can be considered as the full constraint to the reference map .” (p. 2, seção 4. Fully Supervised CD)
- “However, it is hard to always provide abundant FSCD training dataset in practical applications, since change detection is a complex task and needs to interpret multi-temporal image pair at the same time.” (p. 2, seção 4. Fully Supervised CD)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 8 ocorrências (p. 1, 3, 6)
- **Rotulagem / anotação**: 7 ocorrências (p. 1, 3, 4, 5, 10)
- **Normalização / escala**: 3 ocorrências (p. 3, 6, 7)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal e série (auto: 38 pares; 40 série)
**Métodos detectados automaticamente:**
- método/família **Supervisão fraca**: 30 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Rede siamesa**: 7 ocorrências (p. 3, 12)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of discriminator is” (p. 4)
- batch: “batch size for the training of generation and adve” (p. 7)
- otimizador: “Adam optimizer and warmup strategy are used ” (p. 4)
- perda: “focal loss etc” (p. 10)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- métrica **F1**: 11 ocorrências (p. 6, 7, 8, 9)
- métrica **Acurácia global**: 6 ocorrências (p. 6, 8, 9)
- métrica **Precisão/Recall**: 6 ocorrências (p. 4, 6, 7, 13)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “F1 mIOU cIOU RNN 0.9438 0.7296 0.8051 0.7222 0.7614 0.7765 0.6147 DSCN 0.9340 0.6709 0.7871 0.6428 0.7077 0.7379 0.5476 SiamCRNNFC 0.9454 0.7254 0.8500 0.6803 0.7557 0.7739 0.6074 SiamCRNNGRU 0.9508 0.7533 0.8745 0.7051 0.7807 0.7932 0.6403 SiamCRNNLSTM 0.9539” (p. 6, seção 4.1 Unsupervised Change Detection)
- “FCD-GN with only generation loss got a very low precision rate, since USCD finds all landscape changes, 0.55 0.50 0.45 0.40 0.35 0.30 0 50 100 150 200 0.35 0 50 100 150 200 (a) (b) Figure 11 Generation loss of unsupervised change detection for (a) WH dataset a” (p. 7, seção 4.2 Weakly Supervised Change Detection)
- “When FSCD model can only get an accuracy of 0.4044, the F1-score of 0.3508 for FCD-GAN is good enough considering RSCD is only trained with such a few supervision information.” (p. 9, seção 4.3 Regional Supervised Change Detection)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “For unsupervised change detection (USCD), although we have no pre-given samples or rules, there is a prior knowledge that, the representation of unchanged landscapes can be predicated from one image to another image, while the changed lands” (p. 2, seção 4. Fully Supervised CD)
- “F1 mIOU cIOU CAM 0.7929 0.4138 0.4940 0.6102 0.5460 0.5695 0.3755 FCD-GN (0.5) 0.5614 0.1667 0.2846 0.7594 0.4141 0.3710 0.2611 FCD-AN (0.5) 0.7055 0.3484 0.3921 0.8046 0.5272 0.5028 0.3580 FCD-GAN (0.5) 0.7526 0.3895 0.4364 0.7269 0.5452 0” (p. 8, seção 4.2 Weakly Supervised Change Detection)
- “Obviously, RSCD model cannot be comparable to FSCD model, whereas we can have a baseline for the performance of RSCD.” (p. 9, seção 4.3 Regional Supervised Change Detection)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado
- hiperparâmetros **não detectados** automaticamente: épocas/iterações (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Falsos alertas 8 (p. 7, 8, 9, 10)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 3 ocorrências (p. 6, 9)
- emprega conjunto de dados: [[OSCD|OSCD]] — 9 ocorrências (p. 6, 8, 9, 10)
- utiliza método: [[SupervisaoFraca|Supervisão fraca]] — 30 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[RedeSiamesa|Redes siamesas]] — 7 ocorrências (p. 3, 12)
- é avaliado por: [[F1|F1]] — 11 ocorrências (p. 6, 7, 8, 9)
- é avaliado por: [[AcuraciaGlobal|Acurácia global (OA)]] — 6 ocorrências (p. 6, 8, 9)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 6 ocorrências (p. 4, 6, 7, 13)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 8 ocorrências (p. 1, 3, 6)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 7 ocorrências (p. 1, 3, 4, 5, 10)
- aplica etapa de preparo: [[Normalizacao|Normalização e escala radiométrica]] — 3 ocorrências (p. 3, 6, 7)
- discute aspecto de monitoramento: [[FalsosAlertas|Falsos alertas]] — 8 ocorrências (p. 7, 8, 9, 10)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
