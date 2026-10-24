---
tipo: artigo
id_origem: P35
titulo: "Seg2Change: Adapting Open-Vocabulary Semantic Segmentation Model for Remote Sensing Change Detection"
ano: 2026
autores: ["You Su", "Yonghong Song", "Jingqi Chen", "Zehan Wen"]
doi: "10.48550/arXiv.2604.11231"
arquivo_fonte: "coleta/P35_Su2026_Seg2Change-Adapting-Open-Vocabulary-Semantic-Segmentation-Mo.pdf"
markdown_fonte: "output/pdf/P35_Su2026_Seg2Change-Adapting-Open-Vocabulary-Semantic-Segmentation-Mo/document.md"
paginas: 21
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[ClassificacaoCobertura|Classificação de cobertura e uso da terra]]", "[[SegmentacaoSemantica|Segmentação semântica]]"]
sensores: []
conjuntos_dados: ["[[WHUCD|WHU-CD]]", "[[LEVIRCD|LEVIR-CD]]", "[[SECOND|SECOND]]"]
metodos: ["[[ModeloFundacional|Modelos fundacionais]]", "[[SAM|Segment Anything (SAM)]]", "[[TransferLearning|Aprendizado por transferência]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]", "[[PatchesTiles|Recorte em patches/tiles]]"]
validacao: ["[[DivisaoTreinoTeste|Divisão treino/validação/teste]]", "[[IoU|IoU / mIoU]]", "[[F1|F1]]", "[[Kappa|Coeficiente kappa]]", "[[PrecisaoRecall|Precisão e recall]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Su 2026 — Seg2Change: Adapting Open-Vocabulary Semantic Segmentation Model for Remote Sensing Change Detection

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** You Su, Yonghong Song, Jingqi Chen, Zehan Wen (2026). Seg2Change: Adapting Open-Vocabulary Semantic Segmentation Model for Remote Sensing Change Detection. arXiv (Cornell University). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2604.11231
- **Arquivo de origem:** `coleta/P35_Su2026_Seg2Change-Adapting-Open-Vocabulary-Semantic-Segmentation-Mo.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P35_Su2026_Seg2Change-Adapting-Open-Vocabulary-Semantic-Segmentation-Mo/document.md` — 21 páginas, 318 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Change detection is a fundamental task in remote sensing, aiming to quantify the impacts of human activities and ecological dynamics on land-cover changes. Existing change detection methods are limited to predefined classes in training datasets, which constrains their scalability in real-world scenarios. In recent years, numerous advanced open-vocabulary semantic segmentation models have emerged for remote sensing imagery. However, there is still a lack of an effective framework for directly applying these models to open-vocabulary change detection (OVCD), a novel task that integrates vision and language to detect changes across arbitrary categories. To address these challenges, we first construct a category-agnostic change detection dataset, termed CA-CDD. Further, we design a category-agnostic change head to detect the transitions of arbitrary categories and index them to specific clas…

- “Based on them, we propose Seg2Change, an adapter designed to adapt open-vocabulary semantic segmentation models to change detection task.” (p. 1, seção Abstract)
- “To this end, we propose Seg2Change, which serves as a competitive alternative for adapting open-vocabulary semantic segmentation (OVSS) models to change detection.” (p. 2, seção Abstract)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “It comprises two aerial datasets from Christchurch, New Zealand, captured in April 2012 and 2016, with a spatial resolution of 0.3 m/pixel.” (p. 9, seção Abstract)
- “The bi-temporal images in CLCD were collected by Gaofen-2 in Guangdong Province, China, in 2017 and 2019, respectively, with spatial resolutions ranging from” (p. 9, seção Abstract)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- conjunto de dados **WHU-CD**: 25 ocorrências (p. 1, 2, 3, 5, 6)
- conjunto de dados **LEVIR-CD**: 13 ocorrências (p. 2, 5, 6, 9, 10)
- conjunto de dados **SECOND**: 8 ocorrências (p. 4, 7, 8, 10, 12)
- resolução mencionada: 0.3 m (p. 9)
- resolução mencionada: 0.5 m (p. 9)
- “Following the default splits, we divided the dataset into training, validation, and testing sets, consisting of 3,000, 340, and 48 image pairs, respectively.” (p. 9, seção Abstract)
- “The training dataset consists of 1400 samples and the test dataset consists of 322 samples.” (p. 9, seção 0.5 to 2 m. Each sample pair consists of two 512 × 512 image)
- “Meanwhile, our method directly processes 512 × 512 images, thereby avoiding the adverse effects introduced by image cropping.” (p. 16, seção 0.5 to 2 m. Each sample pair consists of two 512 × 512 image)
- “AnyChange [ 79 ] utilizes latent matching of bi-temporal SAM image features, combined with manually annotated points, to cluster change categories of interest.” (p. 3, seção Abstract)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 22 ocorrências (p. 1, 2, 3, 4, 8)
- **Recorte em patches/tiles**: 6 ocorrências (p. 3, 4, 6, 9, 13)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal / pares (auto: 66 menções)
**Métodos detectados automaticamente:**
- método/família **Modelo fundacional**: 18 ocorrências (p. 2, 3, 4, 6, 7)
- método/família **SAM**: 10 ocorrências (p. 1, 2, 3, 6, 7)
- método/família **Transfer learning**: 3 ocorrências (p. 11, 14)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 1 × 10 [−], a batch size of 4, and 20 epochs” (p. 6)
- batch: “batch size of 4, and 20 epochs” (p. 6)
- épocas/iterações: “20 epochs” (p. 6)
- perda: “binary cross-entropy loss between the predicted chan” (p. 5)
- tamanho do patch: “613 × 19,990 pixel” (p. 9)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 5 ocorrências (p. 4, 9, 16)
- **Teste externo / generalização**: 2 ocorrências (p. 3, 10)
- métrica **IoU**: 49 ocorrências (p. 1, 6, 7, 8, 9)
- métrica **F1**: 38 ocorrências (p. 6, 7, 9, 10, 11)
- métrica **Kappa**: 37 ocorrências (p. 6, 7, 8, 9, 10)
- métrica **Precisão/Recall**: 10 ocorrências (p. 10, 12)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “Under the same identifier setting, our category-agnostic change map strategy improves the average IoU [𝑐] across the two datasets by nearly 9%.” (p. 7, seção Abstract)
- “With the integration of tailored language prompts, our method attains notable gains, improving F1 [𝑐] by 3.87% on DSIFN and 9.73% on CLCD.” (p. 7, seção Abstract)
- “Specifically, on the WHUCD dataset, our method surpasses all competitors, achieving an F1 [𝑐] of 86.18% and an IoU [𝑐] of 75.72%, and outperforming the previous best method, DynamicEarth, by a clear margin.” (p. 12, seção 0.5 to 2 m. Each sample pair consists of two 512 ×)
- “Meanwhile, Seg2Change achieves the highest OA of 98.91% and Kappa of 0.8562, indicating more reliable and consistent predictions.” (p. 12, seção 0.5 to 2 m. Each sample pair consists of two 512 ×)

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/yogurts-sy/Seg2Change (p. 1)
- URL citada: https://github.com/yogurts-sy/Seg2Change (p. 1)
- declaração: “Our code is [released at https://github.com/yogurts-sy/Seg2Change.](https://github.com/yogurts-sy/Seg2Change) Keywords Open-vocabulary change detection, remote sensing 1 Introduction The Earth, our shared home, is increasingly shaped by hum” (p. 1)
- hiperparâmetros **não detectados** automaticamente: otimizador (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Latência / frequência 3 (p. 2, 7, 11); Custo 3 (p. 7, 10, 11)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- emprega conjunto de dados: [[WHUCD|WHU-CD]] — 25 ocorrências (p. 1, 2, 3, 5, 6)
- emprega conjunto de dados: [[LEVIRCD|LEVIR-CD]] — 13 ocorrências (p. 2, 5, 6, 9, 10)
- emprega conjunto de dados: [[SECOND|SECOND]] — 8 ocorrências (p. 4, 7, 8, 10, 12)
- utiliza método: [[ModeloFundacional|Modelos fundacionais]] — 18 ocorrências (p. 2, 3, 4, 6, 7)
- utiliza método: [[SAM|Segment Anything (SAM)]] — 10 ocorrências (p. 1, 2, 3, 6, 7)
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 3 ocorrências (p. 11, 14)
- é avaliado por: [[IoU|IoU / mIoU]] — 49 ocorrências (p. 1, 6, 7, 8, 9)
- é avaliado por: [[F1|F1]] — 38 ocorrências (p. 6, 7, 9, 10, 11)
- é avaliado por: [[Kappa|Coeficiente kappa]] — 37 ocorrências (p. 6, 7, 8, 9, 10)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 10 ocorrências (p. 10, 12)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 22 ocorrências (p. 1, 2, 3, 4, 8)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 6 ocorrências (p. 3, 4, 6, 9, 13)
- adota desenho de validação: [[DivisaoTreinoTeste|Divisão treino/validação/teste]] — 5 ocorrências (p. 4, 9, 16)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[ClassificacaoCobertura|Classificação de cobertura e uso da terra]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[SegmentacaoSemantica|Segmentação semântica]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
