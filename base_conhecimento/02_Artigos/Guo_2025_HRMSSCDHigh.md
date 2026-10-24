---
tipo: artigo
id_origem: P141
titulo: "HRMS-SCD:A High-Resolution Multi-Scene Satellite Imagery Dataset for Comprehensive Land-Cover Semantic Change Detection"
ano: 2025
autores: ["Peixin Guo", "Siyu Yang", "Hanchao Zhang", "Xiao Huang", "Xiaogang Ning", "Yilong Han", "Ruiqian Zhang", "Minghui Hao"]
doi: "10.5194/isprs-annals-x-g-2025-323-2025"
arquivo_fonte: "coleta/P141_Guo2025_HRMS-SCD-A-High-Resolution-Multi-Scene-Satellite-Imagery-Dat.pdf"
markdown_fonte: "output/pdf/P141_Guo2025_HRMS-SCD-A-High-Resolution-Multi-Scene-Satellite-Imagery-Dat/document.md"
paginas: 9
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[MudancaSemantica|Mudança semântica (from–to)]]", "[[Edificacoes|Edificações e urbanização]]", "[[ClassificacaoCobertura|Classificação de cobertura e uso da terra]]"]
sensores: ["[[ImagensAereas|Imagens aéreas]]", "[[Landsat|Landsat]]"]
conjuntos_dados: ["[[HRSCD|HRSCD]]"]
metodos: ["[[Transformer|Transformers]]", "[[CNN|Redes convolucionais (CNN)]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]"]
validacao: ["[[Desbalanceamento|Desbalanceamento de classes]]", "[[IoU|IoU / mIoU]]", "[[AcuraciaGlobal|Acurácia global (OA)]]", "[[F1|F1]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Guo 2025 — HRMS-SCD:A High-Resolution Multi-Scene Satellite Imagery Dataset for Comprehensive Land-Cover Semantic Change Detection

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Peixin Guo, Siyu Yang, Hanchao Zhang, Xiao Huang et al. (2025). HRMS-SCD:A High-Resolution Multi-Scene Satellite Imagery Dataset for Comprehensive Land-Cover Semantic Change Detection. ISPRS annals of the photogrammetry, remote sensing and spatial information sciences. Tipo no catálogo: Dataset.
- **DOI/URL:** https://doi.org/10.5194/isprs-annals-x-g-2025-323-2025
- **Arquivo de origem:** `coleta/P141_Guo2025_HRMS-SCD-A-High-Resolution-Multi-Scene-Satellite-Imagery-Dat.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P141_Guo2025_HRMS-SCD-A-High-Resolution-Multi-Scene-Satellite-Imagery-Dat/document.md` — 9 páginas, 26 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Semantic change detection (SCD) focuses on identifying changes in surface coverage while simultaneously classifying the types of changes. This approach provides detailed information valuable for urban planning, environmental monitoring, and other applications, making it a key area of interest in remote sensing research. Despite recent advances, existing SCD studies are hindered by the lack of high-resolution satellite imagery datasets and insufficiently comprehensive semantic label coverage in publicly available datasets. To address these limitations, we have developed a large-scale high-resolution remote sensing dataset consisting of 11,587 satellite image pairs, each with 1-meter spatial resolution and a size of 512 × 512 pixels, representing land cover changes across Beijing between 2017 and 2018. This dataset encompasses diverse land surface scenes with comprehensive semantic annotat…

- “To address these shortcomings, we introduce the HRMS-SCD dataset—a large-scale, high-resolution, multi-scene satellite imagery dataset for semantic change detection.” (p. 1, seção Abstract)
- “To assess the effectiveness of our proposed HRMS-SCD dataset, we compare it against existing general semantic change detection datasets, presenting their differences in Table 1.” (p. 2, seção Abstract)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “To address these limitations, we have developed a large-scale high-resolution remote sensing dataset consisting of 11,587 satellite image pairs, each with 1-meter spatial resolution and a size of 512 × 512 pixels, representing land cover ch” (p. 1, seção Abstract)
- “This dataset consists of 11,587 image pairs with a spatial resolution of 1 meter, each sized at 512 × 512 pixels, collected over Beijing from 2017 to 2018.” (p. 1, seção Abstract)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Imagens aéreas**: 7 ocorrências (p. 1, 2, 3)
- sensor/produto **Landsat**: 4 ocorrências (p. 1, 2)
- conjunto de dados **HRSCD**: 7 ocorrências (p. 1, 2, 3, 5)
- “This dataset consists of 11,587 image pairs with a spatial resolution of 1 meter, each sized at 512 × 512 pixels, collected over Beijing from 2017 to 2018.” (p. 1, seção Abstract)
- “Hi-UCD (Tian et al., 2022) expands upon the Hi-UCD (mini) dataset, covering 102 square kilometers in Tallinn with 40,800 image pairs, supporting multi-temporal semantic This contribution has been peer-reviewed.” (p. 2, seção 2.1. Semantic Change Detection Dataset)
- “The dataset consists of 11,587 images with a size of 512 × 512 pixels and a resolution of 1 meter, which were acquired via the Resource 1, Resource 2, and Beijing 2 satellites, and cover the whole land category changes in Beijing during 201” (p. 3, seção 3.1. Basic Image Information)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 12 ocorrências (p. 1, 2, 3, 4, 6)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal / pares (auto: 10 menções)
**Métodos detectados automaticamente:**
- método/família **Transformer**: 7 ocorrências (p. 1, 3, 5)
- método/família **CNN**: 5 ocorrências (p. 1, 3)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 0.1” (p. 5)
- batch: “batch size is 4 and the model is trained for 50 ep” (p. 5)
- épocas/iterações: “50 epochs” (p. 5)
- otimizador: “SGD optimizer with an initial learning rate” (p. 5)
- tamanho do patch: “512 × 512 pixel” (p. 1)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Desbalanceamento**: 7 ocorrências (p. 2, 3, 6, 7, 8)
- **Teste externo / generalização**: 2 ocorrências (p. 2, 3)
- métrica **IoU**: 13 ocorrências (p. 5, 6)
- métrica **Acurácia global**: 6 ocorrências (p. 5, 6)
- métrica **F1**: 3 ocorrências (p. 6, 7)
- métrica **Precisão/Recall**: 3 ocorrências (p. 6)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “Each dataset offers unique features; however, they also present certain limitations that impact their applicability across various scenarios.” (p. 2, seção 2.1. Semantic Change Detection Dataset)
- “While these existing datasets each contribute significantly to the field, they also exhibit limitations: aerial imagery is costly, offers limited coverage, and is susceptible to weather conditions; low- and medium-resolution satellite image” (p. 3, seção 2.1. Semantic Change Detection Dataset)
- “To address some limitations of prior methods, SSCD-l extends previous work by using two separate CNN encoders to extract temporal semantic features and merging them through a deep change detection unit, optimizing for changes over time.” (p. 3, seção 2.2. Semantic Change Detection Algorithm)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/17x-osborn/HRMS-SCD (p. 1)
- URL citada: https://github.com/17x-osborn/HRMS-SCD (p. 1)
- hiperparâmetros **não detectados** automaticamente: perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[ImagensAereas|Imagens aéreas]] — 7 ocorrências (p. 1, 2, 3)
- utiliza dado/sensor: [[Landsat|Landsat]] — 4 ocorrências (p. 1, 2)
- emprega conjunto de dados: [[HRSCD|HRSCD]] — 7 ocorrências (p. 1, 2, 3, 5)
- utiliza método: [[Transformer|Transformers]] — 7 ocorrências (p. 1, 3, 5)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 5 ocorrências (p. 1, 3)
- é avaliado por: [[IoU|IoU / mIoU]] — 13 ocorrências (p. 5, 6)
- é avaliado por: [[AcuraciaGlobal|Acurácia global (OA)]] — 6 ocorrências (p. 5, 6)
- é avaliado por: [[F1|F1]] — 3 ocorrências (p. 6, 7)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 12 ocorrências (p. 1, 2, 3, 4, 6)
- adota desenho de validação: [[Desbalanceamento|Desbalanceamento de classes]] — 7 ocorrências (p. 2, 3, 6, 7, 8)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[MudancaSemantica|Mudança semântica (from–to)]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[ClassificacaoCobertura|Classificação de cobertura e uso da terra]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
