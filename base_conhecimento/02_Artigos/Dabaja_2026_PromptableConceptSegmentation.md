---
tipo: artigo
id_origem: P63
titulo: "Promptable Concept Segmentation from Above: Evaluating SAM 3’s Zero-Shot and One-Shot Capabilities in Remote Sensing"
ano: 2026
autores: ["Mohammad Dabaja", "Turgay Çelik"]
doi: "10.48550/arXiv.2607.09583"
arquivo_fonte: "coleta/P63_Dabaja2026_Promptable-Concept-Segmentation-from-Above-Evaluating-SAM-3s.pdf"
markdown_fonte: "output/pdf/P63_Dabaja2026_Promptable-Concept-Segmentation-from-Above-Evaluating-SAM-3s/document.md"
paginas: 14
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: []
sensores: ["[[ImagensAereas|Imagens aéreas]]"]
conjuntos_dados: []
metodos: ["[[SAM|Segment Anything (SAM)]]", "[[TransferLearning|Aprendizado por transferência]]", "[[ModeloFundacional|Modelos fundacionais]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Dabaja 2026 — Promptable Concept Segmentation from Above: Evaluating SAM 3’s Zero-Shot and One-Shot Capabilities in Remote Sensing

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Mohammad Dabaja, Turgay Çelik (2026). Promptable Concept Segmentation from Above: Evaluating SAM 3’s Zero-Shot and One-Shot Capabilities in Remote Sensing. arXiv (Cornell University). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2607.09583
- **Arquivo de origem:** `coleta/P63_Dabaja2026_Promptable-Concept-Segmentation-from-Above-Evaluating-SAM-3s.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P63_Dabaja2026_Promptable-Concept-Segmentation-from-Above-Evaluating-SAM-3s/document.md` — 14 páginas, 10 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “Driven by SAM 3’s per- formance disparities in highly specialized domains, we present a comprehensive, multi-task empirical evaluation across remote sensing scene classification, object detection, and instance seg- mentation under strict ze” (p. 1, seção Início)
- “To achieve this, we introduce a structural adaptation of SAM 3 by repurposing its decoupled binary presence head into a standalone zero-shot classifier.” (p. 1, seção Início)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Imagens aéreas**: 5 ocorrências (p. 1, 4, 14)
- resolução mencionada: 0.5 m (p. 4)
- resolução mencionada: 8 m (p. 4)
- “Key challenges include substantial intra-class variation and interclass similarity arising from the multi-source nature of the imagery. • The Object Detection in Optical Remote Sensing Images Dataset (DIOR) is a benchmark for object detecti” (p. 4, seção III. M ETHODOLOGY)
- “The dataset is partitioned into training, validation, and test subsets of 5,862, 5,863, and 11,738 images, respectively.” (p. 4, seção 0.5 m to 30 m per pixel, with images sourced from)
- “The dataset is partitioned into training, validation, and test subsets of 1,411, 458, and 937 images, respectively.” (p. 4, seção 15 categories, combining instance-level detection with)
- “Let f c ∈{ 0 , 1 } be a binary indicator function that returns 1 if at least one instance of concept c is present in the ground truth of image I, and 0 otherwise.” (p. 5, seção 15 categories, combining instance-level detection with)
- “Observing the airplane task in Figure 3a, the text prompt successfully captures the airplanes but hallucinates false-positive boxes over background vehicles that are not labeled in the ground truth.” (p. 9, seção 66.55 mAP (79.51 AP@50). This proves conclusively that)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 8 ocorrências (p. 2, 4, 5, 9)
- **Normalização / escala**: 4 ocorrências (p. 2, 4, 5, 13)
- **Recorte em patches/tiles**: 3 ocorrências (p. 1, 5, 7)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **SAM**: 76 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Transfer learning**: 14 ocorrências (p. 1, 2, 4, 5, 8)
- método/família **Modelo fundacional**: 12 ocorrências (p. 1, 2, 4, 13, 14)
- método/família **Transformer**: 4 ocorrências (p. 2, 14)
**Hiperparâmetros detectados automaticamente (verificar):**
- tamanho do patch: “600 × 600 pixel” (p. 4)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 2 ocorrências (p. 4)
- **Teste externo / generalização**: 2 ocorrências (p. 4, 14)
- métrica **mAP**: 34 ocorrências (p. 5, 8, 9, 10, 11)
- métrica **IoU**: 10 ocorrências (p. 5, 10, 13)
- métrica **Precisão/Recall**: 4 ocorrências (p. 3, 5, 12, 13)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “5 To measure open-vocabulary generalizability without penalizing balanced model, we compute the standard Harmonic Mean (HM) at the 50% IoU threshold using these baseline metrics: HM = [ ·] [ AP] 50 [B] [·] [ AP] [N] 50 (7) AP [B] 50 [+][ AP] [N] 50 To evaluate” (p. 5, seção 0.50 to 0.95, as well as the mAP at the 0.50 thres)
- “Similarly, Baseball Field sits at a nonfunctional 0.01 mAP under the pure text modality, peaks at 77.54 mAP under the visual prompt configuration, and suffers a massive drop back down to 60.98 mAP under the multimodal configuration with oracle filtering.” (p. 8, seção 66.55 mAP (79.51 AP@50). This proves conclusively )
- “Metrics are reported for mAP (IoU 0.50:0.95) and AP@50.” (p. 10, seção 28.18 mAP under the multimodal configuration with)
- “Metrics are reported for mAP (IoU 0.50:0.95) and AP@50.” (p. 13, seção 4.00 mAP in text mode and managing only 24.78 mAP)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “Observing the image, the pure visual prompt fails to isolate the overpass, instead scattering bounding boxes across the connected highway system, while the pure text prompt yields zero detections.” (p. 8, seção 66.55 mAP (79.51 AP@50). This proves conclusively that)
- “Because the textvision alignment layers were pre-trained predominantly on ground-level imagery, the multimodal decoder struggles to map the purely semantic text embedding of “windmill” to this unfamiliar top-down visual representation.” (p. 8, seção 66.55 mAP (79.51 AP@50). This proves conclusively that)
- “Observing the visual outputs, the model completely fails to segment targets like roundabouts (Figure 4d) and baseball diamonds (Figure 4c) when given only a text prompt.” (p. 11, seção 28.18 mAP under the multimodal configuration with)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Sistema operacional 6 (p. 7, 8, 12, 13); Persistência / confirmação 2 (p. 7, 12)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[ImagensAereas|Imagens aéreas]] — 5 ocorrências (p. 1, 4, 14)
- utiliza método: [[SAM|Segment Anything (SAM)]] — 76 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 14 ocorrências (p. 1, 2, 4, 5, 8)
- utiliza método: [[ModeloFundacional|Modelos fundacionais]] — 12 ocorrências (p. 1, 2, 4, 13, 14)

## Anotações do leitor

- 
