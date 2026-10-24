---
tipo: artigo
id_origem: P137
titulo: "A New Learning Paradigm for Foundation Model-Based Remote-Sensing Change Detection"
ano: 2024
autores: ["Kaiyu Li", "Xiangyong Cao", "Deyu Meng"]
doi: "10.1109/tgrs.2024.3365825"
arquivo_fonte: "coleta/P137_Li2024_A-New-Learning-Paradigm-for-Foundation-Model-Based-Remote-Se.pdf"
markdown_fonte: "output/pdf/P137_Li2024_A-New-Learning-Paradigm-for-Foundation-Model-Based-Remote-Se/document.md"
paginas: 13
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]"]
sensores: ["[[Landsat|Landsat]]"]
conjuntos_dados: ["[[LEVIRCD|LEVIR-CD]]", "[[S2Looking|S2Looking]]", "[[WHUCD|WHU-CD]]"]
metodos: ["[[ModeloFundacional|Modelos fundacionais]]", "[[Transformer|Transformers]]", "[[RedeSiamesa|Redes siamesas]]", "[[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]]", "[[CNN|Redes convolucionais (CNN)]]", "[[TransferLearning|Aprendizado por transferência]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]", "[[PatchesTiles|Recorte em patches/tiles]]", "[[AumentoDados|Aumento de dados]]", "[[Normalizacao|Normalização e escala radiométrica]]"]
validacao: ["[[DivisaoTreinoTeste|Divisão treino/validação/teste]]", "[[Generalizacao|Generalização e domain shift]]", "[[IoU|IoU / mIoU]]", "[[PrecisaoRecall|Precisão e recall]]", "[[AcuraciaGlobal|Acurácia global (OA)]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Li 2024 — A New Learning Paradigm for Foundation Model-Based Remote-Sensing Change Detection

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Kaiyu Li, Xiangyong Cao, Deyu Meng (2024). A New Learning Paradigm for Foundation Model-Based Remote-Sensing Change Detection. IEEE Transactions on Geoscience and Remote Sensing. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1109/tgrs.2024.3365825
- **Arquivo de origem:** `coleta/P137_Li2024_A-New-Learning-Paradigm-for-Foundation-Model-Based-Remote-Se.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P137_Li2024_A-New-Learning-Paradigm-for-Foundation-Model-Based-Remote-Se/document.md` — 13 páginas, 103 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “In this paper, we propose a Bi-Temporal Adapter Network (BAN), which is a universal foundation model-based CD adaptation framework aiming to extract the knowledge of foundation models for CD.” (p. 1, seção Início)
- “To alleviate the two issues, in this paper, we propose a universal framework, i.e., bi-temporal adapter networks (BAN for short), for tuning and adapting foundation models to the CD task.” (p. 2, seção I. I NTRODUCTION)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “It provides two annotated maps for each pair of images, indicating new and demolished building areas, which we use to generate a change map. • WHU-CD dataset contains a pair of images taken in the same area from 2012 and 2016, each with a s” (p. 6, seção IV. E XPERIMENTS)
- “With multiple types of annotations, the BANDON dataset can also be used for the SCD task. • The Landsat-SCD dataset consists of 8,468 image pairs collected between 1990 and 2020, each with a size of 416 × 416 and a spatial resolution of 30 ” (p. 7, seção IV. E XPERIMENTS)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Landsat**: 5 ocorrências (p. 7, 9)
- sensor/produto **Imagens aéreas**: 2 ocorrências (p. 7, 12)
- conjunto de dados **LEVIR-CD**: 11 ocorrências (p. 1, 6, 7, 8, 9)
- conjunto de dados **S2Looking**: 6 ocorrências (p. 6, 7, 8)
- conjunto de dados **WHU-CD**: 5 ocorrências (p. 6, 7, 9, 11)
- resolução mencionada: 0.5 m (p. 6)
- resolução mencionada: 0.8 m (p. 6)
- “To ensure standardized evaluation, the dataset is divided into three subsets: training, validation, and testing, containing 445, 64 and 128 image pairs. • S2Looking is a building CD dataset that contains large-scale side-looking satellite i” (p. 6, seção IV. E XPERIMENTS)
- “To better evaluate the generalization ability of models, the testing set is divided into an in-domain set and an out-domain set (collected from different cities) containing 207 and 185 image pairs.” (p. 7, seção IV. E XPERIMENTS)
- “With multiple types of annotations, the BANDON dataset can also be used for the SCD task. • The Landsat-SCD dataset consists of 8,468 image pairs collected between 1990 and 2020, each with a size of 416 × 416 and a spatial resolution of 30 ” (p. 7, seção IV. E XPERIMENTS)
- “Therefore, analyzing the time-series remote sensing (RS) data is an important topic in Earth vision, and change detection (CD) techniques have become an indispensable tool for this task, contributing to the comprehensive interpretation of s” (p. 1, seção I. I NTRODUCTION)
- “8, AUGUST 2023 6 𝑥 1 𝑥 2 ground truth BiT BAN-BiT CF BAN-CF (a) (b) (c) (d) (e) (f) (g) Fig.” (p. 6, seção III. M ETHOD)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 24 ocorrências (p. 1, 6, 7, 8, 9)
- **Recorte em patches/tiles**: 15 ocorrências (p. 2, 3, 5, 6, 7)
- **Aumento de dados**: 5 ocorrências (p. 1, 3, 7, 12)
- **Normalização / escala**: 3 ocorrências (p. 3, 5, 6)
- **Reamostragem**: 2 ocorrências (p. 2, 5)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal / pares (auto: 33 menções)
**Métodos detectados automaticamente:**
- método/família **Modelo fundacional**: 76 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Transformer**: 62 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Rede siamesa**: 15 ocorrências (p. 2, 3, 4, 5, 11)
- método/família **Semi/auto-supervisionado**: 12 ocorrências (p. 4, 7, 9, 10, 12)
- método/família **CNN**: 10 ocorrências (p. 1, 2, 3, 5, 13)
- método/família **Transfer learning**: 7 ocorrências (p. 3, 12)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate is set to 0.0001, and 10 × in Bi-TAB’s prediction ” (p. 7)
- batch: “batch size is set to 8” (p. 7)
- épocas/iterações: “50 epochs” (p. 7)
- otimizador: “AdamW optimizer” (p. 7)
- perda: “cross-entropy loss for BiT and ChangeFormer is adopte” (p. 5)
- tamanho do patch: “507 × 15,354 pixel” (p. 6)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 4 ocorrências (p. 6, 7)
- **Teste externo / generalização**: 4 ocorrências (p. 3, 7, 9, 12)
- métrica **IoU**: 41 ocorrências (p. 1, 7, 8, 9, 10)
- métrica **Precisão/Recall**: 14 ocorrências (p. 7, 9, 10, 11)
- métrica **Acurácia global**: 7 ocorrências (p. 7, 11)
- métrica **Kappa**: 4 ocorrências (p. 7)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/likyoo/BAN (p. 1)
- URL citada: https://github.com/likyoo/BAN (p. 1)
- URL citada: https://github.com/likyoo/open-cd (p. 1)
- declaração: “More importantly, these successful practices show us the potential of foundation models for remote sensing CD. [The code is available at https://github.com/likyoo/BAN and will](https://github.com/likyoo/BAN) be supported in our Open-CD [†] ” (p. 1)
- declaração: “Deyu Meng is with the School of Mathematics and Statistics and Ministry of Education Key Lab of Intelligent Network Security, Xi’an Jiaotong University, Xi’an 710049, China (email: dymeng@mail.xjtu.edu.cn). - [An open source CD toolbox: htt” (p. 1)

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 2 (p. 3, 8)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Landsat|Landsat]] — 5 ocorrências (p. 7, 9)
- emprega conjunto de dados: [[LEVIRCD|LEVIR-CD]] — 11 ocorrências (p. 1, 6, 7, 8, 9)
- emprega conjunto de dados: [[S2Looking|S2Looking]] — 6 ocorrências (p. 6, 7, 8)
- emprega conjunto de dados: [[WHUCD|WHU-CD]] — 5 ocorrências (p. 6, 7, 9, 11)
- utiliza método: [[ModeloFundacional|Modelos fundacionais]] — 76 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[Transformer|Transformers]] — 62 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[RedeSiamesa|Redes siamesas]] — 15 ocorrências (p. 2, 3, 4, 5, 11)
- utiliza método: [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 12 ocorrências (p. 4, 7, 9, 10, 12)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 10 ocorrências (p. 1, 2, 3, 5, 13)
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 7 ocorrências (p. 3, 12)
- é avaliado por: [[IoU|IoU / mIoU]] — 41 ocorrências (p. 1, 7, 8, 9, 10)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 14 ocorrências (p. 7, 9, 10, 11)
- é avaliado por: [[AcuraciaGlobal|Acurácia global (OA)]] — 7 ocorrências (p. 7, 11)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 24 ocorrências (p. 1, 6, 7, 8, 9)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 15 ocorrências (p. 2, 3, 5, 6, 7)
- aplica etapa de preparo: [[AumentoDados|Aumento de dados]] — 5 ocorrências (p. 1, 3, 7, 12)
- aplica etapa de preparo: [[Normalizacao|Normalização e escala radiométrica]] — 3 ocorrências (p. 3, 5, 6)
- adota desenho de validação: [[DivisaoTreinoTeste|Divisão treino/validação/teste]] — 4 ocorrências (p. 6, 7)
- adota desenho de validação: [[Generalizacao|Generalização e domain shift]] — 4 ocorrências (p. 3, 7, 9, 12)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
