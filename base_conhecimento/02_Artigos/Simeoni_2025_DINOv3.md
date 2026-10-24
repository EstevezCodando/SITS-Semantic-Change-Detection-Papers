---
tipo: artigo
id_origem: P64
titulo: "DINOv3"
ano: 2025
autores: ["Oriane Siméoni", "Huy V. Vo", "Maximilian Seitzer", "Federico Baldassarre", "Maxime Oquab", "Cijo Jose", "Vasil Khalidov", "Marc Szafraniec"]
doi: "10.48550/arXiv.2508.10104"
arquivo_fonte: "coleta/P64_Simeoni2025_DINOv3.pdf"
markdown_fonte: "output/pdf/P64_Simeoni2025_DINOv3/document.md"
paginas: 67
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: []
sensores: ["[[ImagensAereas|Imagens aéreas]]"]
conjuntos_dados: []
metodos: ["[[ModeloFundacional|Modelos fundacionais]]", "[[Transformer|Transformers]]", "[[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]]", "[[SupervisaoFraca|Supervisão fraca]]", "[[TransferLearning|Aprendizado por transferência]]", "[[SAM|Segment Anything (SAM)]]"]
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]", "[[Rotulagem|Rotulagem e anotação]]", "[[Normalizacao|Normalização e escala radiométrica]]", "[[AumentoDados|Aumento de dados]]"]
validacao: ["[[DivisaoTreinoTeste|Divisão treino/validação/teste]]", "[[Generalizacao|Generalização e domain shift]]", "[[IoU|IoU / mIoU]]", "[[PrecisaoRecall|Precisão e recall]]", "[[mAP|mAP]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Simeoni 2025 — DINOv3

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Oriane Siméoni, Huy V. Vo, Maximilian Seitzer, Federico Baldassarre et al. (2025). DINOv3. arXiv (Cornell University). Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2508.10104
- **Arquivo de origem:** `coleta/P64_Simeoni2025_DINOv3.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P64_Simeoni2025_DINOv3/document.md` — 67 páginas, 173 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Self-supervised learning holds the promise of eliminating the need for manual data annotation, enabling models to scale effortlessly to massive datasets and larger architectures. By not being tailored to specific tasks or domains, this training paradigm has the potential to learn visual representations from diverse sources, ranging from natural to aerial images— using a single algorithm. This technical report introduces DINOv3, a major milestone toward realizing this vision by leveraging simple yet effective strategies. First, we leverage the benefit of scaling both dataset and model size by careful data preparation, design, and optimization. Second, we introduce a new method called Gram anchoring, which effectively addresses the known yet unsolved issue of dense feature maps degrading during long training schedules. Finally, we apply post-hoc strategies that further enhance our models’ …

- “Second, we introduce a new method called Gram anchoring, which effectively addresses the known yet unsolved issue of dense feature maps degrading during long training schedules.” (p. 1, seção Abstract)
- “As a result, we present a versatile vision foundation model that outperforms the specialized state of the art across a broad range of settings, without fine-tuning.” (p. 1, seção Abstract)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Imagens aéreas**: 3 ocorrências (p. 1, 2, 3)
- “As training progresses, these similarities increase and the performance on dense tasks decreases. a distributed implementation of Koleo in which the loss is applied in small batches of 16 samples—possibly across GPUs.” (p. 10, seção Abstract)
- “Following common practices, we use AdamW (Loshchilov and Hutter, 2017), and set the total batch size to 4096 images split across 256 GPUs.” (p. 10, seção Abstract)
- “|Col1|Col2|GPUs|Col4| |---|---|---|---| |Load B/NT<br>samples<br>Load B/NT<br>samples<br>Student S1 training<br>(B/NS1 samples per GPU)<br>Synchronize model<br>Wait|Load B/NT<br>samples<br>Load B/NT<br>samples<br>Student S1 training<br>(B/N” (p. 16, seção Abstract)
- “Given the complexity of manually labeling large datasets, weakly-supervised training —where annotations are derived from metadata associated with images—provides an effective alternative to supervised training.” (p. 6, seção Abstract)
- “The key innovation of DAv2 is to use a large collection of synthetically generated images with ground truth depth annotations.” (p. 27, seção Abstract)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 100 ocorrências (p. 2, 4, 5, 6, 7)
- **Rotulagem / anotação**: 21 ocorrências (p. 1, 2, 3, 5, 6)
- **Normalização / escala**: 4 ocorrências (p. 9, 10, 12, 33)
- **Aumento de dados**: 3 ocorrências (p. 22, 23, 26)
- **Textura (GLCM)**: 2 ocorrências (p. 24, 33)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **Modelo fundacional**: 283 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Transformer**: 122 ocorrências (p. 2, 3, 4, 5, 6)
- método/família **Semi/auto-supervisionado**: 22 ocorrências (p. 1, 2, 6, 7, 8)
- método/família **Supervisão fraca**: 17 ocorrências (p. 1, 2, 6, 7, 9)
- método/família **Transfer learning**: 16 ocorrências (p. 1, 5, 6, 7, 17)
- método/família **SAM**: 9 ocorrências (p. 7, 17, 19, 20, 27)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate, weight decay, and teacher EMA momentum” (p. 10)
- batch: “batch size of 131K” (p. 6)
- épocas/iterações: “22 epochs” (p. 26)
- otimizador: “AdamW (Loshchilov and Hutter, 2017), and set ” (p. 10)
- tamanho do patch: “1024 × 1024 pixel” (p. 14)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 9 ocorrências (p. 23, 26, 33, 34)
- **Teste externo / generalização**: 3 ocorrências (p. 1, 25, 35)
- métrica **IoU**: 23 ocorrências (p. 5, 9, 11, 13, 14)
- métrica **Precisão/Recall**: 9 ocorrências (p. 20, 25, 32)
- métrica **mAP**: 5 ocorrências (p. 5, 25, 26, 36)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “Empirically, we found this change to stabilize ImageNet kNNclassification late in training (+0.2 accuracy) and improve dense performance ( e.g . +1 mIoU on ADE20k segmentation, -0.02 RMSE on NYUv2 depth estimation).” (p. 9, seção Abstract)
- “IN1k ADE NYU Method Iteration Linear mIoU RMSE Baseline — — 88.2 50.3 0.307 GRAM 200k × 1 88.0 53.6 0.285 GRAM 200k × 2 88.0 55.7 0.281 GRAM 100k × 2 87.9 55.7 0.284 GRAM 1M × 2 88.1 54.9 0.290 (b) Ablation of Gram teachers and resolutions.” (p. 14, seção Abstract)
- “6% recall), and even falls behind Franca ( − 0 .” (p. 20, seção Abstract)
- “6% recall) and AM-RADIO (+1 .” (p. 20, seção Abstract)

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 6)
- declaração: “This highly successful approach inspired numerous open-source reproductions and scaling efforts .” (p. 6)
- declaração: “OpenCLIP (Cherti et al., 2023) was the first open-source effort to replicate CLIP by training on the LAION dataset (Schuhmann et al., 2021); following works leverage pre-trained backbones by fine-tuning them in a CLIP-style manner (Sun et a” (p. 6)
- hiperparâmetros **não detectados** automaticamente: perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 9 (p. 16, 17); Persistência / confirmação 1 (p. 2)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[ImagensAereas|Imagens aéreas]] — 3 ocorrências (p. 1, 2, 3)
- utiliza método: [[ModeloFundacional|Modelos fundacionais]] — 283 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[Transformer|Transformers]] — 122 ocorrências (p. 2, 3, 4, 5, 6)
- utiliza método: [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 22 ocorrências (p. 1, 2, 6, 7, 8)
- utiliza método: [[SupervisaoFraca|Supervisão fraca]] — 17 ocorrências (p. 1, 2, 6, 7, 9)
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 16 ocorrências (p. 1, 5, 6, 7, 17)
- utiliza método: [[SAM|Segment Anything (SAM)]] — 9 ocorrências (p. 7, 17, 19, 20, 27)
- é avaliado por: [[IoU|IoU / mIoU]] — 23 ocorrências (p. 5, 9, 11, 13, 14)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 9 ocorrências (p. 20, 25, 32)
- é avaliado por: [[mAP|mAP]] — 5 ocorrências (p. 5, 25, 26, 36)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 100 ocorrências (p. 2, 4, 5, 6, 7)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 21 ocorrências (p. 1, 2, 3, 5, 6)
- aplica etapa de preparo: [[Normalizacao|Normalização e escala radiométrica]] — 4 ocorrências (p. 9, 10, 12, 33)
- aplica etapa de preparo: [[AumentoDados|Aumento de dados]] — 3 ocorrências (p. 22, 23, 26)
- adota desenho de validação: [[DivisaoTreinoTeste|Divisão treino/validação/teste]] — 9 ocorrências (p. 23, 26, 33, 34)
- adota desenho de validação: [[Generalizacao|Generalização e domain shift]] — 3 ocorrências (p. 1, 25, 35)

## Anotações do leitor

- 
