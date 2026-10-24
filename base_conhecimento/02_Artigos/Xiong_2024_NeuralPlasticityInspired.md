---
tipo: artigo
id_origem: P67
titulo: "Neural Plasticity-Inspired Multimodal Foundation Model for Earth Observation"
ano: 2024
autores: ["Zhitong Xiong", "Yi Wang", "Fahong Zhang", "Adam J. Stewart", "Joëlle Hanna", "Damian Borth", "Ioannis Papoutsis", "Bertrand Le Saux"]
doi: "10.48550/arXiv.2403.15356"
arquivo_fonte: "coleta/P67_Xiong2024_Neural-Plasticity-Inspired-Multimodal-Foundation-Model-for-E.pdf"
markdown_fonte: "output/pdf/P67_Xiong2024_Neural-Plasticity-Inspired-Multimodal-Foundation-Model-for-E/document.md"
paginas: 19
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: []
sensores: ["[[Sentinel2|Sentinel-2]]", "[[Sentinel1|Sentinel-1]]", "[[SAR|Radar (SAR)]]"]
conjuntos_dados: []
metodos: ["[[Transformer|Transformers]]", "[[ModeloFundacional|Modelos fundacionais]]", "[[TransferLearning|Aprendizado por transferência]]", "[[CNN|Redes convolucionais (CNN)]]", "[[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]]"]
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]", "[[Normalizacao|Normalização e escala radiométrica]]"]
validacao: ["[[Generalizacao|Generalização e domain shift]]", "[[IoU|IoU / mIoU]]", "[[mAP|mAP]]", "[[F1|F1]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Xiong 2024 — Neural Plasticity-Inspired Multimodal Foundation Model for Earth Observation

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Zhitong Xiong, Yi Wang, Fahong Zhang, Adam J. Stewart et al. (2024). Neural Plasticity-Inspired Multimodal Foundation Model for Earth Observation. arXiv (Cornell University). Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2403.15356
- **Arquivo de origem:** `coleta/P67_Xiong2024_Neural-Plasticity-Inspired-Multimodal-Foundation-Model-for-E.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P67_Xiong2024_Neural-Plasticity-Inspired-Multimodal-Foundation-Model-for-E/document.md` — 19 páginas, 163 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “To address this, we propose the Dynamic One-For-All (DOFA) model, a unified, multimodal foundation framework designed for diverse vision tasks in EO.” (p. 1, seção Início)
- “In response to this challenge, we propose the Dynamic One-For-All (DOFA) model, a versatile, adaptive multimodal foundation model explicitly designed for the EO domain.” (p. 2, seção 1 Introduction)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-2**: 29 ocorrências (p. 4, 10, 11, 13, 14)
- sensor/produto **Sentinel-1**: 10 ocorrências (p. 4, 7, 10, 13, 14)
- sensor/produto **SAR**: 4 ocorrências (p. 3, 4)
- “The DIOR dataset is a largescale benchmark for remote sensing object detection, containing 23,463 images and 192,472 annotated instances across 20 object categories, covering diverse scenes with significant variation in scale, orientation, ” (p. 10, seção 4.3 Object Detection Experiments)
- “13 Ground truth RGB +COASTALAEROSOL +REDEDGE1 +REDEDGE2 +REDEDGE3 S2 Image RGB Bands +NIRBROAD +NIRNARROW +WATERVAPOR +CIRRUS +SWIR1 All bands Ground truth RGB +COASTALAEROSOL +REDEDGE1 +REDEDGE2 +REDEDGE3 All bands S2 Image RGB Bands +NIRB” (p. 13, seção 4.4 Ablation Studies)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 32 ocorrências (p. 3, 4, 5, 6, 7)
- **Normalização / escala**: 3 ocorrências (p. 4, 8, 15)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **Transformer**: 110 ocorrências (p. 2, 3, 4, 5, 8)
- método/família **Modelo fundacional**: 43 ocorrências (p. 1, 2, 3, 7, 8)
- método/família **Transfer learning**: 11 ocorrências (p. 2, 8, 9, 10)
- método/família **CNN**: 3 ocorrências (p. 10, 11)
- método/família **Semi/auto-supervisionado**: 3 ocorrências (p. 3, 4, 7)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rates and batch sizes tailored to enhance the performa” (p. 8)
- batch: “batch size from the notation of tensors” (p. 4)
- épocas/iterações: “50 epochs” (p. 8)
- otimizador: “AdamW optimizer, batch size 64, and an initia” (p. 8)
- perda: “cross-entropy loss for most datasets, except for m-bi” (p. 8)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Teste externo / generalização**: 6 ocorrências (p. 1, 8, 9, 13)
- métrica **IoU**: 11 ocorrências (p. 9, 10, 11, 12, 13)
- métrica **mAP**: 5 ocorrências (p. 10, 11, 13)
- métrica **F1**: 4 ocorrências (p. 12, 13)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “Using ViT-Base, DOFA+ improves frozen accuracy to 93.7%, while finetuning yields 97.5%.” (p. 10, seção 6 out of 8 tasks, with particularly strong perform)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “For instance, models such as GFM , ScaleMAE , SatMAE , CROMA , and SpectralGPT illustrate these limitations.” (p. 1, seção 1 Introduction)
- “In summary, existing approaches that develop separate foundation models or use isolated visual encoders for multi-sensor data fail to capture inter-sensor relationships, resulting in key limitations: 1.” (p. 2, seção 1 Introduction)
- “Addressing this critical limitation aligns with a central theme of open-world EO visual understanding: developing FMs capable of dynamically and efficiently adapting to downstream applications with flexible input data modalities.” (p. 2, seção 1 Introduction)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/zhu-xlab/ (p. 1)
- URL citada: https://github.com/zhu-xlab/ (p. 1)
- URL citada: https://github.com/zhu-xlab/DOFA (p. 1)
- URL citada: https://github.com/allenai/satlas/ (p. 15)
- URL citada: https://github.com/allenai/satlas/blob/main/SatlasPretrain.md#download (p. 15)
- declaração: “Building on this, we further propose DOFA+, which is initialized from a powerful open-source pre-trained vision model (DINOv2 ) and applies the MIM objective to enable Fig.” (p. 2)
- declaração: “In this section, we provide the download links to ensure data availability.” (p. 15)

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 8 (p. 2, 7, 8, 9, 15)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 29 ocorrências (p. 4, 10, 11, 13, 14)
- utiliza dado/sensor: [[Sentinel1|Sentinel-1]] — 10 ocorrências (p. 4, 7, 10, 13, 14)
- utiliza dado/sensor: [[SAR|Radar (SAR)]] — 4 ocorrências (p. 3, 4)
- utiliza método: [[Transformer|Transformers]] — 110 ocorrências (p. 2, 3, 4, 5, 8)
- utiliza método: [[ModeloFundacional|Modelos fundacionais]] — 43 ocorrências (p. 1, 2, 3, 7, 8)
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 11 ocorrências (p. 2, 8, 9, 10)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 3 ocorrências (p. 10, 11)
- utiliza método: [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 3 ocorrências (p. 3, 4, 7)
- é avaliado por: [[IoU|IoU / mIoU]] — 11 ocorrências (p. 9, 10, 11, 12, 13)
- é avaliado por: [[mAP|mAP]] — 5 ocorrências (p. 10, 11, 13)
- é avaliado por: [[F1|F1]] — 4 ocorrências (p. 12, 13)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 32 ocorrências (p. 3, 4, 5, 6, 7)
- aplica etapa de preparo: [[Normalizacao|Normalização e escala radiométrica]] — 3 ocorrências (p. 4, 8, 15)
- adota desenho de validação: [[Generalizacao|Generalização e domain shift]] — 6 ocorrências (p. 1, 8, 9, 13)

## Anotações do leitor

- 
