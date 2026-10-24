---
tipo: artigo
id_origem: P138
titulo: "Recurrent Semantic Change Detection in VHR Remote Sensing Images Using Visual Foundation Models"
ano: 2025
autores: ["Jing Zhang", "Lei Ding", "Tingyuan Zhou", "Jian Wang", "Peter M. Atkinson", "Lorenzo Bruzzone"]
doi: "10.1109/tgrs.2025.3546808"
arquivo_fonte: "coleta/P138_Zhang2025_Recurrent-Semantic-Change-Detection-in-VHR-Remote-Sensing-Im.pdf"
markdown_fonte: "output/pdf/P138_Zhang2025_Recurrent-Semantic-Change-Detection-in-VHR-Remote-Sensing-Im/document.md"
paginas: 15
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[MudancaSemantica|Mudança semântica (from–to)]]"]
sensores: ["[[Landsat|Landsat]]"]
conjuntos_dados: ["[[HRSCD|HRSCD]]", "[[SECOND|SECOND]]"]
metodos: ["[[SAM|Segment Anything (SAM)]]", "[[CNN|Redes convolucionais (CNN)]]", "[[RedeSiamesa|Redes siamesas]]", "[[Transformer|Transformers]]", "[[TransferLearning|Aprendizado por transferência]]", "[[LSTM|Redes recorrentes (LSTM)]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]"]
validacao: ["[[Generalizacao|Generalização e domain shift]]", "[[IoU|IoU / mIoU]]", "[[AcuraciaGlobal|Acurácia global (OA)]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Zhang 2025 — Recurrent Semantic Change Detection in VHR Remote Sensing Images Using Visual Foundation Models

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Jing Zhang, Lei Ding, Tingyuan Zhou, Jian Wang et al. (2025). Recurrent Semantic Change Detection in VHR Remote Sensing Images Using Visual Foundation Models. IEEE Transactions on Geoscience and Remote Sensing. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1109/tgrs.2025.3546808
- **Arquivo de origem:** `coleta/P138_Zhang2025_Recurrent-Semantic-Change-Detection-in-VHR-Remote-Sensing-Im.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P138_Zhang2025_Recurrent-Semantic-Change-Detection-in-VHR-Remote-Sensing-Im/document.md` — 15 páginas, 98 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “In this paper, we propose a novel vision Foundation Model architecture for SCD, designated as VFM-ReSCD.” (p. 1, seção Início)
- “Moreover, we introduce a Recurrent Neural Network (RNN) to model semantic correlation and capture feature changes.” (p. 1, seção Início)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The Landsat-SCD dataset is made up of Landsat images collected between 1990 and 2020.” (p. 6, seção IV. D ATASET D ESCRIPTION AND E XPERIMENTAL)
- “Bruzzone, “Bi-directional temporal modelling for semantic change detection in remote sensing images,” in IGARSS 2023-2023 IEEE International Geoscience and Remote Sensing Sympo- sium .” (p. 13, seção VI. C ONCLUSIONS)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Landsat**: 13 ocorrências (p. 6, 7, 8, 10, 11)
- conjunto de dados **HRSCD**: 8 ocorrências (p. 8, 11, 12)
- conjunto de dados **SECOND**: 7 ocorrências (p. 6, 8, 9, 11, 12)
- conjunto de dados **OpenStreetMap**: 2 ocorrências (p. 3)
- resolução mencionada: 3 m (p. 6)
- resolução mencionada: 30 m (p. 6)
- “We further split them into a training set and a test set with a proportion of 4 : 1 (i.e., 2375 image pairs for training, 593 for testing).” (p. 6, seção IV. D ATASET D ESCRIPTION AND E XPERIMENTAL)
- “They proposed a convolutional adapter to focus on specific ground objects and introduced a task-agnostic semantic learning branch to leverage semantic features in bi-temporal remote sensing images, thereby enhancing the model’s ability to u” (p. 2, seção I. I NTRODUCTION)
- “The semantic loss L sem is calculated as the multiclass cross-entropy loss between the semantic segmentation results P 1 , P 2 and the corresponding ground truth (GT) semantic change maps L 1 , L 2 .” (p. 5, seção III. P ROPOSED VFM-R E SCD A RCHITECTURE FOR SCD)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 10 ocorrências (p. 3, 4, 5, 6)
- **Aumento de dados**: 3 ocorrências (p. 7)
- **Recorte em patches/tiles**: 2 ocorrências (p. 5)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal e série (auto: 31 pares; 16 série)
**Métodos detectados automaticamente:**
- método/família **SAM**: 35 ocorrências (p. 1, 2, 3, 4, 8)
- método/família **CNN**: 17 ocorrências (p. 1, 2, 3, 8, 12)
- método/família **Rede siamesa**: 14 ocorrências (p. 2, 3, 12, 13, 14)
- método/família **Transformer**: 9 ocorrências (p. 1, 2, 8, 13)
- método/família **Transfer learning**: 9 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **LSTM / recorrente**: 5 ocorrências (p. 1, 4, 13, 14)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate at 0.1 and updated it at each iteration to 0 ” (p. 7)
- épocas/iterações: “100 epochs” (p. 7)
- otimizador: “SGD) with Nesterov momentum” (p. 7)
- perda: “cross-entropy loss between the semantic segmentation ” (p. 5)
- tamanho do patch: “512 × 512 pixel” (p. 6)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Teste externo / generalização**: 3 ocorrências (p. 3, 14)
- métrica **IoU**: 21 ocorrências (p. 6, 7, 8, 12)
- métrica **Acurácia global**: 12 ocorrências (p. 6, 7, 8)
- métrica **Precisão/Recall**: 3 ocorrências (p. 7)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/Gaia0811/VFM-SCD (p. 7)
- URL citada: https://github.com/Gaia0811/VFM-SCD (p. 7)
- hiperparâmetros **não detectados** automaticamente: batch (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 7 (p. 2, 7, 8); Falsos alertas 1 (p. 2)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Landsat|Landsat]] — 13 ocorrências (p. 6, 7, 8, 10, 11)
- emprega conjunto de dados: [[HRSCD|HRSCD]] — 8 ocorrências (p. 8, 11, 12)
- emprega conjunto de dados: [[SECOND|SECOND]] — 7 ocorrências (p. 6, 8, 9, 11, 12)
- utiliza método: [[SAM|Segment Anything (SAM)]] — 35 ocorrências (p. 1, 2, 3, 4, 8)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 17 ocorrências (p. 1, 2, 3, 8, 12)
- utiliza método: [[RedeSiamesa|Redes siamesas]] — 14 ocorrências (p. 2, 3, 12, 13, 14)
- utiliza método: [[Transformer|Transformers]] — 9 ocorrências (p. 1, 2, 8, 13)
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 9 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[LSTM|Redes recorrentes (LSTM)]] — 5 ocorrências (p. 1, 4, 13, 14)
- é avaliado por: [[IoU|IoU / mIoU]] — 21 ocorrências (p. 6, 7, 8, 12)
- é avaliado por: [[AcuraciaGlobal|Acurácia global (OA)]] — 12 ocorrências (p. 6, 7, 8)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 10 ocorrências (p. 3, 4, 5, 6)
- adota desenho de validação: [[Generalizacao|Generalização e domain shift]] — 3 ocorrências (p. 3, 14)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[MudancaSemantica|Mudança semântica (from–to)]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
