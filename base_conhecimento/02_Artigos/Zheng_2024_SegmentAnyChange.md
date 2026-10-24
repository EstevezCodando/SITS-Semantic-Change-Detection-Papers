---
tipo: artigo
id_origem: P29
titulo: "Segment Any Change"
ano: 2024
autores: ["Zhuo Zheng", "Liangpei Zhang", "Liangpei Zhang", "Stefano Ermon"]
doi: "10.48550/arXiv.2402.01188"
arquivo_fonte: "coleta/P29_Zheng2024_Segment-Any-Change.pdf"
markdown_fonte: "output/pdf/P29_Zheng2024_Segment-Any-Change/document.md"
paginas: 15
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]"]
sensores: []
conjuntos_dados: ["[[S2Looking|S2Looking]]", "[[LEVIRCD|LEVIR-CD]]", "[[SECOND|SECOND]]"]
metodos: ["[[SAM|Segment Anything (SAM)]]", "[[Transformer|Transformers]]", "[[ModeloFundacional|Modelos fundacionais]]", "[[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]]", "[[TransferLearning|Aprendizado por transferência]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]"]
validacao: ["[[Generalizacao|Generalização e domain shift]]", "[[PrecisaoRecall|Precisão e recall]]", "[[F1|F1]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Zheng 2024 — Segment Any Change

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Zhuo Zheng, Liangpei Zhang, Liangpei Zhang, Stefano Ermon (2024). Segment Any Change. neural information processing systems. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2402.01188
- **Arquivo de origem:** `coleta/P29_Zheng2024_Segment-Any-Change.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P29_Zheng2024_Segment-Any-Change/document.md` — 15 páginas, 85 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Visual foundation models have achieved remarkable results in zero-shot image classification and segmentation, but zero-shot change detection remains an open problem. In this paper, we propose the segment any change models (AnyChange), a new type of change detection model that supports zero-shot prediction and generalization on unseen change types and data distributions. AnyChange is built on the segment anything model (SAM) via our training-free adaptation method, bitemporal latent matching. By revealing and exploiting intra-image and inter-image semantic similarities in SAM’s latent space, bitemporal latent matching endows SAM with zero-shot change detection capabilities in a training-free way. We also propose a point query mechanism to enable AnyChange’s zero-shot object-centric change detection capability. We perform extensive experiments to confirm the effectiveness of AnyChange for …

- “In this paper, we propose the segment any change models (AnyChange), a new type of change detection model that supports zero-shot prediction and generalization on unseen change types and data distributions.” (p. 1, seção Abstract)
- “To close this gap, we present Segment Any Change, the first change detection model with zero-shot generalization on unseen change types and data distributions.” (p. 1, seção Abstract)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- conjunto de dados **S2Looking**: 10 ocorrências (p. 2, 6, 7, 8, 9)
- conjunto de dados **LEVIR-CD**: 7 ocorrências (p. 2, 6, 7, 8)
- conjunto de dados **SECOND**: 5 ocorrências (p. 1, 7, 9, 10)
- “The setting follows I3PE 3 The training set of S2Looking has 3,500 image pairs.” (p. 9, seção 2 Visual foundation model, like SAM, CLIP, and DINOv2, etc.)
- “Note that the metric names rendered with gray represent inaccurate estimations due to the absence of ground truth of “any change”, but reflect whether their predictions approximate the naive baseline (predict all as “change” class).” (p. 7, seção 2 Visual foundation model, like SAM, CLIP, and DINOv2, etc.)
- “We set the fine-tuning on 100% ground truth as the upper bound, which achieved 66.3% F 1 .” (p. 9, seção 2 Visual foundation model, like SAM, CLIP, and DINOv2, etc.)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 13 ocorrências (p. 1, 4, 6, 7, 8)
- **Normalização / escala**: 2 ocorrências (p. 5)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal e série (auto: 30 pares; 6 série)
**Métodos detectados automaticamente:**
- método/família **SAM**: 64 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Transformer**: 29 ocorrências (p. 4, 7, 8, 9, 10)
- método/família **Modelo fundacional**: 15 ocorrências (p. 1, 2, 3, 6, 7)
- método/família **Semi/auto-supervisionado**: 10 ocorrências (p. 8, 9, 10)
- método/família **Transfer learning**: 5 ocorrências (p. 3, 6, 9)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Teste externo / generalização**: 10 ocorrências (p. 1, 2, 3, 4)
- métrica **Precisão/Recall**: 22 ocorrências (p. 5, 6, 7, 8)
- métrica **F1**: 6 ocorrências (p. 7, 8, 9, 10)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “AnyChange sets a new record on the SECOND benchmark for unsupervised change detection, exceeding the previous SOTA by up to 4.4% F 1 score, and achieving comparable accuracy with negligible manual annotations (1 pixel per image) for supervised change detection” (p. 1, seção Abstract)
- “From the unsupervised change detection perspective, AnyChange beats the previous state-of-the-art model, I3PE (Chen et al., 2023), setting a new record of 48.2% F 1 on SECOND.” (p. 3, seção Abstract)
- “By matching with all proposals from the image at t 2, we obtain three basically consistent results (F 1 of 68.1% ± 0.67% and recall of 96.2% ± 0.66%), as shown in Fig.” (p. 5, seção Abstract)

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/Z-Zheng/pytorch-change-models (p. 1)
- URL citada: https://github.com/Z-Zheng/pytorch-change-models (p. 1)
- declaração: “Code is available at [https://github.com/Z-Zheng/pytorch-change-models](https://github.com/Z-Zheng/pytorch-change-models) .” (p. 1)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 6 (p. 2, 4, 7, 8, 9)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- emprega conjunto de dados: [[S2Looking|S2Looking]] — 10 ocorrências (p. 2, 6, 7, 8, 9)
- emprega conjunto de dados: [[LEVIRCD|LEVIR-CD]] — 7 ocorrências (p. 2, 6, 7, 8)
- emprega conjunto de dados: [[SECOND|SECOND]] — 5 ocorrências (p. 1, 7, 9, 10)
- utiliza método: [[SAM|Segment Anything (SAM)]] — 64 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[Transformer|Transformers]] — 29 ocorrências (p. 4, 7, 8, 9, 10)
- utiliza método: [[ModeloFundacional|Modelos fundacionais]] — 15 ocorrências (p. 1, 2, 3, 6, 7)
- utiliza método: [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 10 ocorrências (p. 8, 9, 10)
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 5 ocorrências (p. 3, 6, 9)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 22 ocorrências (p. 5, 6, 7, 8)
- é avaliado por: [[F1|F1]] — 6 ocorrências (p. 7, 8, 9, 10)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 13 ocorrências (p. 1, 4, 6, 7, 8)
- adota desenho de validação: [[Generalizacao|Generalização e domain shift]] — 10 ocorrências (p. 1, 2, 3, 4)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
