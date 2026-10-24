---
tipo: artigo
id_origem: P151
titulo: "Vision Foundation Models in Remote Sensing: A survey"
ano: 2025
autores: ["Siqi Lu", "Junlin Guo", "James R. Zimmer-Dauphinee", "Jordan M. Nieusma", "Xiao Wang", "Parker VanValkenburgh", "Steven A. Wernke", "Yuankai Huo"]
doi: "10.1109/mgrs.2025.3541952"
arquivo_fonte: "coleta/P151_Lu2025_Vision-Foundation-Models-in-Remote-Sensing-A-survey.pdf"
markdown_fonte: "output/pdf/P151_Lu2025_Vision-Foundation-Models-in-Remote-Sensing-A-survey/document.md"
paginas: 26
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: []
sensores: ["[[Sentinel2|Sentinel-2]]", "[[SAR|Radar (SAR)]]", "[[Sentinel1|Sentinel-1]]"]
conjuntos_dados: ["[[LEVIRCD|LEVIR-CD]]", "[[OSCD|OSCD]]"]
metodos: ["[[Transformer|Transformers]]", "[[ModeloFundacional|Modelos fundacionais]]", "[[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Lu 2025 — Vision Foundation Models in Remote Sensing: A survey

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Siqi Lu, Junlin Guo, James R. Zimmer-Dauphinee, Jordan M. Nieusma et al. (2025). Vision Foundation Models in Remote Sensing: A survey. IEEE Geoscience and Remote Sensing Magazine. Tipo no catálogo: Revisão.
- **DOI/URL:** https://doi.org/10.1109/mgrs.2025.3541952
- **Arquivo de origem:** `coleta/P151_Lu2025_Vision-Foundation-Models-in-Remote-Sensing-A-survey.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P151_Lu2025_Vision-Foundation-Models-in-Remote-Sensing-A-survey/document.md` — 26 páginas, 73 recortes de figuras, 6 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Abstract —Artificial Intelligence (AI) technologies have profoundly transformed the field of remote sensing, revo- lutionizing data collection, processing, and analysis. Tradi- tionally reliant on manual interpretation and task-specific models, remote sensing research has been significantly enhanced by the advent of foundation models—large- scale, pre-trained AI models capable of performing a wide array of tasks with unprecedented accuracy and efficiency. This paper provides a comprehensive survey of foundation models in the remote sensing domain. We categorize these models based on their architectures, pre-training datasets, and methodologies. Through detailed performance com- parisons, we highlight emerging trends and the signifi- cant advancements achieved by those foundation models. Additionally, we discuss technical challenges, practical implications, and future research directions,…

- “This paper aims to provide a comprehensive survey of vision foundation models in the remote sensing domain ad rem, and is limited to foundation models released between June 2021 and June 2024.” (p. 1, seção I. I NTRODUCTION)
- “To highlight the versatility of foundation models in remote sensing, we present table VI-B that categorizes models based on their applicability to various applications, as well as the different image analysis methods used.” (p. 12, seção VI. D ATA AND T ASKS)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “This paper aims to provide a comprehensive survey of vision foundation models in the remote sensing domain ad rem, and is limited to foundation models released between June 2021 and June 2024.” (p. 1, seção I. I NTRODUCTION)
- “5 Building on these reviews, our study provides a comprehensive analysis of foundation models developed from June 2021 to June 2024, focusing on advances in self-supervised learning and transformer-based architectures.” (p. 5, seção III. RELATED REVIEW PAPERS)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-2**: 25 ocorrências (p. 8, 9, 20, 21)
- sensor/produto **SAR**: 18 ocorrências (p. 3, 4, 5, 9, 10)
- sensor/produto **Sentinel-1**: 8 ocorrências (p. 20, 21)
- sensor/produto **Landsat**: 8 ocorrências (p. 2, 9, 20, 21)
- conjunto de dados **LEVIR-CD**: 4 ocorrências (p. 15, 17)
- conjunto de dados **OSCD**: 4 ocorrências (p. 15, 17)
- “117,000 images with a patch size of 256 pixels and spatial resolutions ranging from 0.5 to 2 meters per pixel.” (p. 20, seção VIII. C ONCLUSION)
- “It includes 11,268 images of various resolutions from Google Earth, GF-2 Satellite, and aerial sources, covering 18 categories globally.” (p. 20, seção VIII. C ONCLUSION)
- “Another significant dataset, SEN12MS , released in June 2019, contains 541,986 images from Sentinel-1, Sentinel-2, and MODIS Land Cover.” (p. 20, seção VIII. C ONCLUSION)
- “Tradi- tionally reliant on manual interpretation and task-specific models, remote sensing research has been significantly enhanced by the advent of foundation models—large- scale, pre-trained AI models capable of performing a wide array of ” (p. 1, seção 6 Department of Computer Science, Vanderbilt University,)
- “Traditionally, remote sensing projects relied heavily on manual interpretation and task-specific models that required extensive labeled datasets and significant computational resources.” (p. 1, seção I. I NTRODUCTION)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 26 ocorrências (p. 1, 3, 5, 6, 7)
- **Recorte em patches/tiles**: 14 ocorrências (p. 3, 7, 12, 17, 20)
- **Textura (GLCM)**: 4 ocorrências (p. 6, 11, 17, 20)
- **Máscara de nuvem e sombra**: 2 ocorrências (p. 6, 20)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 14 menções vs 0 de pares)
**Métodos detectados automaticamente:**
- método/família **Transformer**: 93 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Modelo fundacional**: 90 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Semi/auto-supervisionado**: 31 ocorrências (p. 1, 3, 4, 5, 6)
- método/família **CNN**: 19 ocorrências (p. 2, 3, 4, 5, 9)
- método/família **Transfer learning**: 6 ocorrências (p. 3, 18, 22, 23, 25)
**Hiperparâmetros detectados automaticamente (verificar):**
- tamanho do patch: “256x256 pixel” (p. 20)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Teste externo / generalização**: 6 ocorrências (p. 1, 5, 7, 12, 14)
- métrica **F1**: 13 ocorrências (p. 14, 15, 17)
- métrica **mAP**: 13 ocorrências (p. 14, 15, 16, 17)
- métrica **Precisão/Recall**: 10 ocorrências (p. 11, 15, 17, 18)
- métrica **IoU**: 7 ocorrências (p. 15, 16)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “However, the dependency on large-scale labeled datasets presents a major limitation.” (p. 7, seção 2 Object detection and Segmentation © MAXAR 2024, provided)
- “Such limitations have motivated the development of alternative approaches, including self-supervised pretraining methods, which leverage the abundance of unlabeled data to learn general-purpose representations without manual annotation.” (p. 7, seção 2 Object detection and Segmentation © MAXAR 2024, provided)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Quase tempo real 2 (p. 16, 18); Custo 2 (p. 5, 16); Sistema operacional 1 (p. 16); Persistência / confirmação 1 (p. 5)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 25 ocorrências (p. 8, 9, 20, 21)
- utiliza dado/sensor: [[SAR|Radar (SAR)]] — 18 ocorrências (p. 3, 4, 5, 9, 10)
- utiliza dado/sensor: [[Sentinel1|Sentinel-1]] — 8 ocorrências (p. 20, 21)
- emprega conjunto de dados: [[LEVIRCD|LEVIR-CD]] — 4 ocorrências (p. 15, 17)
- emprega conjunto de dados: [[OSCD|OSCD]] — 4 ocorrências (p. 15, 17)
- utiliza método: [[Transformer|Transformers]] — 93 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[ModeloFundacional|Modelos fundacionais]] — 90 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 31 ocorrências (p. 1, 3, 4, 5, 6)

## Anotações do leitor

- 
