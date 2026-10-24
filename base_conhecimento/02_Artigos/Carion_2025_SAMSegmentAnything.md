---
tipo: artigo
id_origem: P62
titulo: "SAM 3: Segment Anything with Concepts"
ano: 2025
autores: ["Nicolas Carion", "Laura Gustafson", "Yuan-Ting Hu", "Shoubhik Debnath", "Ronghang Hu", "Dídac Surís", "Chaitanya K. Ryali", "Kalyan Vasudev Alwala"]
doi: "10.48550/arXiv.2511.16719"
arquivo_fonte: "coleta/P62_Carion2025_SAM-3-Segment-Anything-with-Concepts.pdf"
markdown_fonte: "output/pdf/P62_Carion2025_SAM-3-Segment-Anything-with-Concepts/document.md"
paginas: 78
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: []
sensores: []
conjuntos_dados: []
metodos: ["[[SAM|Segment Anything (SAM)]]", "[[TransferLearning|Aprendizado por transferência]]", "[[Transformer|Transformers]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Carion 2025 — SAM 3: Segment Anything with Concepts

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Nicolas Carion, Laura Gustafson, Yuan-Ting Hu, Shoubhik Debnath et al. (2025). SAM 3: Segment Anything with Concepts. arXiv (Cornell University). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2511.16719
- **Arquivo de origem:** `coleta/P62_Carion2025_SAM-3-Segment-Anything-with-Concepts.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P62_Carion2025_SAM-3-Segment-Anything-with-Concepts/document.md` — 78 páginas, 416 recortes de figuras, 2 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “To fill this gap, we present SAM 3, a model that achieves a step change in promptable segmentation in images and videos, improving PVS relative to SAM 2 and setting a new standard for Promptable Concept Segmentation (PCS) .” (p. 2, seção 1 Introduction)
- “To address the challenge of open-vocabulary concept detection, we introduce a separate presence head to decouple recognition and localization, which is especially effective when training with challenging negative phrases .” (p. 2, seção 1 Introduction)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- “CountBench (Paiss et al., 2023) contains 540 images and their captions, with 2-10 objects in each image.” (p. 47, seção 3.1 model.)
- “By removing images with unavailable links, we test on 487 images.” (p. 47, seção 3.1 model.)
- “PixMo-Count (Deitke et al., 2025) contains 540 images and their text descriptions in the form of simple noun phrases, with 2 to 10 objects in each image.” (p. 47, seção 3.1 model.)
- “There can be multiple interpretations of phrases arising from polysemy (“mouse” device vs. animal), subjective descriptors (“cozy”, “large”), vague or context-dependent phrases that may not even be groundable (“brand identity”), boundary am” (p. 3, seção 2 Promptable Concept Segmentation (PCS))
- “We address the ambiguity problem by collecting test annotations from three experts, adapting the evaluation protocol to allow multiple valid interpretations (§E.3), designing the data pipeline/guidelines to minimize ambiguity in annotation,” (p. 3, seção 2 Promptable Concept Segmentation (PCS))

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 322 ocorrências (p. 1, 2, 3, 5, 6)
- **Mosaicos e compostos**: 3 ocorrências (p. 26)
- **Recorte em patches/tiles**: 3 ocorrências (p. 14, 31)
- **Aumento de dados**: 2 ocorrências (p. 25)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **SAM**: 468 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Transfer learning**: 30 ocorrências (p. 2, 5, 6, 8, 10)
- método/família **Transformer**: 19 ocorrências (p. 2, 3, 4, 5, 19)
- método/família **Semi/auto-supervisionado**: 8 ocorrências (p. 2, 10, 16, 24, 29)
- método/família **Modelo fundacional**: 5 ocorrências (p. 14, 28)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate decay (Clark et al” (p. 24)
- batch: “batch size of 896 with 5k warm up and cooldown ste” (p. 24)
- épocas/iterações: “5 iterations” (p. 24)
- otimizador: “AdamW (Loshchilov & Hutter, 2019)” (p. 24)
- perda: “binary cross-entropy loss” (p. 13)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 8 ocorrências (p. 10, 29, 36, 39, 54)
- **Teste externo / generalização**: 8 ocorrências (p. 3, 14, 18, 19, 30)
- métrica **IoU**: 36 ocorrências (p. 5, 8, 9, 22, 23)
- métrica **F1**: 16 ocorrências (p. 7, 36, 37, 38, 48)
- métrica **mAP**: 14 ocorrências (p. 8, 9, 51, 65, 68)
- métrica **Precisão/Recall**: 9 ocorrências (p. 7, 24, 28, 30, 33)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “When computing pmF 1, we averaged the results over multiple volume IoU thresholds from 0.5 to 0.95 with increments of 0.05, similar to how it is computed on images.” (p. 49, seção 3.1 model.)
- “Model 2023 Val Set (AP @ IoU=0.50:0.95) Name Version AP AP-categ AP-descr AP-descr-pos AP-descr-S AP-descr-M AP-descr-L FIBER FIBER-B 25.7 30.3 22.3 34.8 38.6 19.5 12.4 GLIP GLIP-T 19.3 23.6 16.4 25.8 29.4 14.8 8.2 GLIP GLIP-L 25.8 32.9 21.2 33.2 37.7 18.9 10.” (p. 62, seção 3.1 model.)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “All prompts must be consistent in their category definition, or the model’s behavior is undefined; e.g., “fish” cannot be refined with subsequent exemplar prompts of just the tail; instead the text prompt should be updated.” (p. 3, seção 2 Promptable Concept Segmentation (PCS))
- “We build an efficient data engine that iteratively generates annotated data via a feedback loop with SAM 3, human annotators, and AI annotators, actively mining media-phrase pairs on which the current version of SAM 3 fails to produce high-” (p. 5, seção 4 Data Engine)
- “Performance plateaus after 4 clicks, as exemplars cannot fix poor-quality masks.” (p. 8, seção 6 Experiments)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/facebookresearch/sam3 (p. 68)
- URL citada: https://github.com/facebookresearch/sam3 (p. 68)
- declaração: “We open-source the SA-Co benchmark and release the SAM 3 checkpoints and inference code.” (p. 2)
- declaração: “12 visualizes statistics on these subsets in comparison with existing open-source image and video detection and instance segmentation datasets as well as the distribution of top-level SA-Co ontology categories on image datasets.” (p. 34)

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Persistência / confirmação 13 (p. 23, 44); Custo 7 (p. 10, 16, 19, 23, 64); Latência / frequência 5 (p. 2, 65, 66, 67); Revisão humana 3 (p. 18, 38); Quase tempo real 2 (p. 2, 19)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza método: [[SAM|Segment Anything (SAM)]] — 468 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 30 ocorrências (p. 2, 5, 6, 8, 10)
- utiliza método: [[Transformer|Transformers]] — 19 ocorrências (p. 2, 3, 4, 5, 19)

## Anotações do leitor

- 
