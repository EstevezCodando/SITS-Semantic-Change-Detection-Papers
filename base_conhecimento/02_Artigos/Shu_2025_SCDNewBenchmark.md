---
tipo: artigo
id_origem: P36
titulo: "RB-SCD: A New Benchmark for Semantic Change Detection of Roads and Bridges in Traffic Scenes"
ano: 2025
autores: ["Qinji Shu", "Si-Bao Chen", "Xiao Wang", "Zhihui You", "Wei Lu", "Jin Long Tang", "Bin Luo"]
doi: "10.48550/arXiv.2505.13212"
arquivo_fonte: "coleta/P36_Shu2026_RB-SCD-A-New-Benchmark-for-Semantic-Change-Detection-of-Road.pdf"
markdown_fonte: "output/pdf/P36_Shu2026_RB-SCD-A-New-Benchmark-for-Semantic-Change-Detection-of-Road/document.md"
paginas: 35
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[MudancaSemantica|Mudança semântica (from–to)]]", "[[Edificacoes|Edificações e urbanização]]", "[[Vias|Vias e estradas]]"]
sensores: ["[[Landsat|Landsat]]"]
conjuntos_dados: ["[[LEVIRCD|LEVIR-CD]]", "[[WHUCD|WHU-CD]]", "[[HRSCD|HRSCD]]"]
metodos: ["[[CNN|Redes convolucionais (CNN)]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]", "[[PatchesTiles|Recorte em patches/tiles]]", "[[AumentoDados|Aumento de dados]]"]
validacao: ["[[Desbalanceamento|Desbalanceamento de classes]]", "[[Generalizacao|Generalização e domain shift]]", "[[DivisaoTreinoTeste|Divisão treino/validação/teste]]", "[[IoU|IoU / mIoU]]", "[[F1|F1]]", "[[PrecisaoRecall|Precisão e recall]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Shu 2025 — RB-SCD: A New Benchmark for Semantic Change Detection of Roads and Bridges in Traffic Scenes

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Qinji Shu, Si-Bao Chen, Xiao Wang, Zhihui You et al. (2025). RB-SCD: A New Benchmark for Semantic Change Detection of Roads and Bridges in Traffic Scenes. Pattern Recognition. Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2505.13212
- **Arquivo de origem:** `coleta/P36_Shu2026_RB-SCD-A-New-Benchmark-for-Semantic-Change-Detection-of-Road.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P36_Shu2026_RB-SCD-A-New-Benchmark-for-Semantic-Change-Detection-of-Road/document.md` — 35 páginas, 214 recortes de figuras, 1 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Accurate detection of road and bridge changes is crucial for urban planning and trans portation management, yet presents unique challenges for general change detection (CD). Key difficulties arise from maintaining the continuity of roads and bridges as lin ear structures and disambiguating visually similar land covers (e.g., road construction vs. bare land). Existing spatial-domain models struggle with these issues, further hin dered by the lack of specialized, semantically rich datasets. To fill these gaps, we intro duce the Road and Bridge Semantic Change Detection (RB-SCD) dataset. As the first benchmark to systematically target semantic change detection of roads and bridges, RB-SCD offers comprehensive fine-grained annotations for 11 semantic change cat egories. This enables a detailed analysis of traffic infrastructure evolution. Building on this, we propose a novel framework, the M…

- “Building on this, we propose a novel framework, the Multimodal Frequency-Driven Change Detector (MFDCD).” (p. 1, seção Abstract)
- “Second, we propose a novel M ultimodal F requency- D riven C hange D etector ( MFDCD ).” (p. 5, seção 1. INTRODUCTION)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The image pairs are sourced from Google Earth, with a temporal coverage spanning from 2007 to 2022.” (p. 10, seção 8. fl->road)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Landsat**: 3 ocorrências (p. 2, 3, 6)
- sensor/produto **Imagens aéreas**: 2 ocorrências (p. 18)
- conjunto de dados **LEVIR-CD**: 12 ocorrências (p. 3, 18, 21, 22, 24)
- conjunto de dados **WHU-CD**: 9 ocorrências (p. 18, 21, 22, 24, 25)
- conjunto de dados **HRSCD**: 3 ocorrências (p. 2, 3, 6)
- resolução mencionada: 0.59 m (p. 10)
- resolução mencionada: 0.5 m (p. 18)
- “pairs of 256 × 256 patches, including 4,015 pairs for the training set and 1,001 pairs for the testing set.” (p. 11, seção 8. fl->road)
- “The Label row shows the ground truth. critical spatial information.” (p. 8, seção 2. Related Work)
- “This indicates that MFDCD demonstrates the best performance in terms of overlap between the predicted and ground truth change regions, enabling more precise localization of change areas.” (p. 21, seção 5. Experiments and Results)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 9 ocorrências (p. 1, 5, 6, 8, 21)
- **Recorte em patches/tiles**: 6 ocorrências (p. 3, 9, 10, 11, 18)
- **Aumento de dados**: 3 ocorrências (p. 11, 14, 19)
- **Textura (GLCM)**: 2 ocorrências (p. 20, 23)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal / pares (auto: 9 menções)
**Métodos detectados automaticamente:**
- método/família **CNN**: 4 ocorrências (p. 7, 17, 26)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 0.0001 and a weight decay parameter of 0.01” (p. 19)
- batch: “batch size, N is the sequence length (number of to” (p. 16)
- otimizador: “AdamW is employed, with a learning rate of 0” (p. 19)
- perda: “cross-entropy loss to mitigate the class imbalance is” (p. 11)
- tamanho do patch: “256 × 256 patch” (p. 11)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Desbalanceamento**: 5 ocorrências (p. 6, 11, 19)
- **Teste externo / generalização**: 4 ocorrências (p. 6, 7, 21, 29)
- **Conjuntos treino/val/teste**: 3 ocorrências (p. 9, 18)
- métrica **IoU**: 22 ocorrências (p. 19, 20, 21, 22, 24)
- métrica **F1**: 18 ocorrências (p. 19, 20, 21, 22)
- métrica **Precisão/Recall**: 4 ocorrências (p. 19, 23, 28)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “Specifically, for the easily de tectable categories like water- - bridge, bridge- - water, water- - road and farmland- - road, our model attains IoU scores of 86.83%, 83.58%, 71.68%, and 68.40%, respec 19” (p. 19, seção 5. Experiments and Results)
- “In terms of the IoU metric, our model ranks first with a score of 65.83%, slightly outperforming ELGC-Net , which achieves 65.53%.” (p. 21, seção 5. Experiments and Results)
- “Regarding the F1, our MFDCD model also leads with a score of 79.39%, followed closely by ELGC-Net at 79.18%.” (p. 21, seção 5. Experiments and Results)
- “Specifically, on the WHU-CD dataset, our approach outperforms the second-best method by 2.69% and 1.5% in IoU and F1, respectively.” (p. 22, seção 5. Experiments and Results)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “Although existing road extraction datasets , mainly focus on binary pixel segmentation of roads, they cannot be used to focus on road changes.” (p. 2, seção 1. INTRODUCTION)
- “The limitations of existing spatial-domain methods highlight the need for a new ap proach that operates in a more suitable domain.” (p. 4, seção 1. INTRODUCTION)
- “This frequency domain representation naturally filters out minor textual variations, providing a stable basis for a cleaner alignment with visual features and overcoming the core limitations of spatial-level fusion.” (p. 4, seção 1. INTRODUCTION)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/DaGuangDaGuang/RB-SCD (p. 2)
- URL citada: https://github.com/DaGuangDaGuang/RB-SCD (p. 2)
- declaração: “The code will be available at https://github.com/DaGuangDaGuang/RB-SCD.” (p. 2)
- hiperparâmetros **não detectados** automaticamente: épocas/iterações (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Quase tempo real 1 (p. 29); Custo 1 (p. 27)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Landsat|Landsat]] — 3 ocorrências (p. 2, 3, 6)
- emprega conjunto de dados: [[LEVIRCD|LEVIR-CD]] — 12 ocorrências (p. 3, 18, 21, 22, 24)
- emprega conjunto de dados: [[WHUCD|WHU-CD]] — 9 ocorrências (p. 18, 21, 22, 24, 25)
- emprega conjunto de dados: [[HRSCD|HRSCD]] — 3 ocorrências (p. 2, 3, 6)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 4 ocorrências (p. 7, 17, 26)
- é avaliado por: [[IoU|IoU / mIoU]] — 22 ocorrências (p. 19, 20, 21, 22, 24)
- é avaliado por: [[F1|F1]] — 18 ocorrências (p. 19, 20, 21, 22)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 4 ocorrências (p. 19, 23, 28)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 9 ocorrências (p. 1, 5, 6, 8, 21)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 6 ocorrências (p. 3, 9, 10, 11, 18)
- aplica etapa de preparo: [[AumentoDados|Aumento de dados]] — 3 ocorrências (p. 11, 14, 19)
- adota desenho de validação: [[Desbalanceamento|Desbalanceamento de classes]] — 5 ocorrências (p. 6, 11, 19)
- adota desenho de validação: [[Generalizacao|Generalização e domain shift]] — 4 ocorrências (p. 6, 7, 21, 29)
- adota desenho de validação: [[DivisaoTreinoTeste|Divisão treino/validação/teste]] — 3 ocorrências (p. 9, 18)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[MudancaSemantica|Mudança semântica (from–to)]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Vias|Vias e estradas]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
