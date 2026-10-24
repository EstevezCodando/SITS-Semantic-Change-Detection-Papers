---
tipo: artigo
id_origem: P145
titulo: "UniChange: Unifying Change Detection with Multimodal Large Language Model"
ano: 2025
autores: ["Xu Zhang", "Danyang Li", "Xiaohang Dong", "Tianhao Wu", "Hualong Yu", "Wang, Jianye", "Qicheng Li", "Xiang Li"]
doi: "10.48550/arXiv.2511.02607"
arquivo_fonte: "coleta/P145_Zhang2025_UniChange-Unifying-Change-Detection-with-Multimodal-Large-La.pdf"
markdown_fonte: "output/pdf/P145_Zhang2025_UniChange-Unifying-Change-Detection-with-Multimodal-Large-La/document.md"
paginas: 15
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[ClassificacaoCobertura|Classificação de cobertura e uso da terra]]"]
sensores: []
conjuntos_dados: ["[[WHUCD|WHU-CD]]", "[[S2Looking|S2Looking]]", "[[LEVIRCD|LEVIR-CD]]"]
metodos: ["[[SAM|Segment Anything (SAM)]]", "[[Transformer|Transformers]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Zhang 2025 — UniChange: Unifying Change Detection with Multimodal Large Language Model

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Xu Zhang, Danyang Li, Xiaohang Dong, Tianhao Wu et al. (2025). UniChange: Unifying Change Detection with Multimodal Large Language Model. arXiv (Cornell University). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2511.02607
- **Arquivo de origem:** `coleta/P145_Zhang2025_UniChange-Unifying-Change-Detection-with-Multimodal-Large-La.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P145_Zhang2025_UniChange-Unifying-Change-Detection-with-Multimodal-Large-La/document.md` — 15 páginas, 106 recortes de figuras, 1 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Change detection (CD) is a fundamental task for moni- toring and analysing land cover dynamics. While recent high performance models and high quality datasets have significantly advanced the field, a critical limitation per- sists. Current models typically acquire limited knowledge from single-type annotated data and cannot concurrently leverage diverse binary change detection (BCD) and se- mantic change detection (SCD) datasets. This constraint leads to poor generalisation and limited versatility. The recent advancements in Multimodal Large Language Mod- els (MLLMs) introduce new possibilities for a unified CD framework. We leverage the language priors and unifica- tion capabilities of MLLMs to develop UniChange, the first MLLM-based unified change detection model. UniChange integrates generative language abilities with specialised CD functionalities.…

- “We introduce three special tokens: [T1], [T2], and [CHANGE], utilising their embeddings as the key to query variations.” (p. 1, seção Abstract)
- “To address the fundamental challenges within the change detection domain, we propose UniChange.” (p. 2, seção 1. Introduction)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- conjunto de dados **WHU-CD**: 19 ocorrências (p. 1, 6, 7, 8, 9)
- conjunto de dados **S2Looking**: 16 ocorrências (p. 1, 6, 7, 8, 9)
- conjunto de dados **LEVIR-CD**: 12 ocorrências (p. 1, 6, 7, 8, 9)
- conjunto de dados **HRSCD**: 3 ocorrências (p. 2, 3, 7)
- “For standardised evaluation, we crop these large images into 1024 × 1024 patches.” (p. 6, seção 4.2. Datasets)
- “The S2Looking dataset provides a total of 5000 image pairs captured from side-looking rural areas globally.” (p. 6, seção 4.2. Datasets)
- “It provides 985 pairs of 1024 × 1024 images, primarily focusing on building changes.” (p. 6, seção 4.2. Datasets)
- “RS-specific MLLMs such as RSGPT , GeoChat , and GeoPixel have emerged, but these methods largely focus on single-image interpretation.” (p. 3, seção 2.2. Multimodal Large Language Model)
- “Both of them optimise the model’s prediction by applying supervision between the predicted change masks and the ground truth change masks.” (p. 5, seção 3.3. Training Strategy)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 6 ocorrências (p. 1, 2, 5, 7)
- **Recorte em patches/tiles**: 5 ocorrências (p. 6)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal / pares (auto: 9 menções)
**Métodos detectados automaticamente:**
- método/família **SAM**: 13 ocorrências (p. 2, 3, 5, 7, 8)
- método/família **Transformer**: 8 ocorrências (p. 2, 3, 5, 7, 8)
- método/família **Transfer learning**: 7 ocorrências (p. 4, 7)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 5 × 10 [−] ” (p. 6)
- batch: “batch size of 1 and a gradient accumulation step o” (p. 6)
- épocas/iterações: “10 epochs” (p. 6)
- otimizador: “AdamW optimizer with a base learning rate of ” (p. 6)
- perda: “Dice loss, Semantic Segmentation loss, and Semant” (p. 5)
- tamanho do patch: “1024 × 1024 patch” (p. 6)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Teste externo / generalização**: 5 ocorrências (p. 1, 2, 3, 6)
- métrica **IoU**: 41 ocorrências (p. 1, 6, 7, 8)
- métrica **F1**: 26 ocorrências (p. 6, 7, 8)
- métrica **Precisão/Recall**: 6 ocorrências (p. 6)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “However, a fundamental limitation of these methods is the necessity of training a specialised model for each individual dataset.” (p. 2, seção 1. Introduction)
- “However, its framework is essentially tailored to building-related tasks and cannot be extended to other categories of land cover change.” (p. 2, seção 1. Introduction)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/Erxucomeon/UniChange (p. 1)
- URL citada: https://github.com/Erxucomeon/UniChange (p. 1)
- declaração: “The code is available at [https://github.com/Erxucomeon/UniChange.](https://github.com/Erxucomeon/UniChange) - Equal Contribution - Corresponding Author … Figure 1.” (p. 1)

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- emprega conjunto de dados: [[WHUCD|WHU-CD]] — 19 ocorrências (p. 1, 6, 7, 8, 9)
- emprega conjunto de dados: [[S2Looking|S2Looking]] — 16 ocorrências (p. 1, 6, 7, 8, 9)
- emprega conjunto de dados: [[LEVIRCD|LEVIR-CD]] — 12 ocorrências (p. 1, 6, 7, 8, 9)
- utiliza método: [[SAM|Segment Anything (SAM)]] — 13 ocorrências (p. 2, 3, 5, 7, 8)
- utiliza método: [[Transformer|Transformers]] — 8 ocorrências (p. 2, 3, 5, 7, 8)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[ClassificacaoCobertura|Classificação de cobertura e uso da terra]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
