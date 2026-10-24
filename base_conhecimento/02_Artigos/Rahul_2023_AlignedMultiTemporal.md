---
tipo: artigo
id_origem: P106
titulo: "An Aligned Multi-Temporal Multi-Resolution Satellite Image Dataset for Change Detection Research"
ano: 2023
autores: ["Deshmukh, Rahul", "Constantine J. Roros", "Amith Kashyap", "Avinash C. Kak"]
doi: "10.48550/arXiv.2302.12301"
arquivo_fonte: "coleta/P106_Rahul2023_An-Aligned-Multi-Temporal-Multi-Resolution-Satellite-Image-D.pdf"
markdown_fonte: "output/pdf/P106_Rahul2023_An-Aligned-Multi-Temporal-Multi-Resolution-Satellite-Image-D/document.md"
paginas: 9
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]"]
sensores: ["[[Landsat|Landsat]]", "[[PlanetProdutos|Produtos Planet (visão geral)]]", "[[Sentinel2|Sentinel-2]]"]
conjuntos_dados: []
metodos: ["[[SuperResolucao|Super-resolução]]"]
preparo: ["[[MascaraNuvem|Máscara de nuvem e sombra]]", "[[Rotulagem|Rotulagem e anotação]]", "[[AumentoDados|Aumento de dados]]"]
validacao: ["[[PrecisaoRecall|Precisão e recall]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Rahul 2023 — An Aligned Multi-Temporal Multi-Resolution Satellite Image Dataset for Change Detection Research

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Deshmukh, Rahul, Constantine J. Roros, Amith Kashyap, Avinash C. Kak (2023). An Aligned Multi-Temporal Multi-Resolution Satellite Image Dataset for Change Detection Research. arXiv (Cornell University). Tipo no catálogo: Dataset.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2302.12301
- **Arquivo de origem:** `coleta/P106_Rahul2023_An-Aligned-Multi-Temporal-Multi-Resolution-Satellite-Image-D.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P106_Rahul2023_An-Aligned-Multi-Temporal-Multi-Resolution-Satellite-Image-D/document.md` — 9 páginas, 4 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** This paper presents an aligned multi-temporal and multi-resolution satellite image dataset for research in change detection. We expect our dataset to be useful to re- searchers who want to fuse information from multiple satel- lites for detecting changes on the surface of the earth that may not be fully visible in any single satellite. The dataset we present was created by augmenting the SpaceNet-7 dataset with temporally parallel stacks of Landsat and Sentinel images. The SpaceNet-7 dataset consists of time- sequenced Planet images recorded over 101 AOIs (Areas- of-Interest). In our dataset, for each of the 60 AOIs that are meant for training, we augment the Planet datacube with temporally parallel datacubes of Landsat and Sen- tinel images. The temporal alignments between the high- res Planet images, on the one hand, and the Landsat and Sentinel images, on the other, are approximate si…

- “This paper presents an aligned multi-temporal and multi-resolution satellite image dataset for research in change detection.” (p. 1, seção Abstract)
- “The dataset we present was created by augmenting the SpaceNet-7 dataset with temporally parallel stacks of Landsat and Sentinel images.” (p. 1, seção Abstract)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Landsat**: 52 ocorrências (p. 1, 2, 3, 4, 5)
- sensor/produto **Planet (mosaicos e cenas)**: 39 ocorrências (p. 1, 2, 3, 4, 5)
- sensor/produto **Sentinel-2**: 18 ocorrências (p. 1, 3, 4, 7, 8)
- sensor/produto **WorldView**: 4 ocorrências (p. 2, 5)
- resolução mencionada: 4 m (p. 1)
- resolução mencionada: 30 m (p. 2)
- resolução mencionada: 15 m (p. 2)
- “Sentinel-2 images for all 60 SpaceNet-7 AOIs that are meant for training.” (p. 1, seção 1 Our dataset includes temporally and spatially aligned Land)
- “It is an open research question at the moment whether we can super-resolve those neighborhood patterns to, say, the 15m resolution data for Landsat-8 images.” (p. 2, seção 2 For large-scale image alignment experiments, it must be re)
- “The data is based on WorldView-2 images at 50cm resolution.” (p. 2, seção 2.1. Satellite Image Datasets)
- “Creating the ground truth labels for the buildings (and roads) required semi-automated processing of the data.” (p. 2, seção 2.1. Satellite Image Datasets)
- “The views and conclu sions contained herein are those of the authors and should not be interpreted as necessarily representing the official policies, either expressed or implied, of ODNI, IARPA, or the U.S.” (p. 8, seção 10. Acknowledgment)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Máscara de nuvem e sombra**: 6 ocorrências (p. 1, 3, 4, 6)
- **Rotulagem / anotação**: 5 ocorrências (p. 2, 3, 8)
- **Aumento de dados**: 4 ocorrências (p. 2, 3, 4, 8)
- **Reamostragem**: 2 ocorrências (p. 5, 7)
- **Mosaicos e compostos**: 2 ocorrências (p. 1)
- **Recorte em patches/tiles**: 2 ocorrências (p. 4)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal e série (auto: 5 pares; 6 série)
**Métodos detectados automaticamente:**
- método/família **Super-resolução**: 5 ocorrências (p. 2, 5)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- métrica **Precisão/Recall**: 5 ocorrências (p. 2, 5, 8)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “Just to cite one AOI to highlight the alignment accuracy achieve, for the case of the Meridian, Idaho, AOI, the average RMSE went down from 0.939 to 0.521 for the Landsat stack and 0.772 to 0.397 for Sentinel stack using FAST+VGG for feature extraction and fea” (p. 7, seção 7. Cross-Satellite Alignment Results)

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Landsat|Landsat]] — 52 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza dado/sensor: [[PlanetProdutos|Produtos Planet (visão geral)]] — 39 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 18 ocorrências (p. 1, 3, 4, 7, 8)
- utiliza método: [[SuperResolucao|Super-resolução]] — 5 ocorrências (p. 2, 5)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 5 ocorrências (p. 2, 5, 8)
- aplica etapa de preparo: [[MascaraNuvem|Máscara de nuvem e sombra]] — 6 ocorrências (p. 1, 3, 4, 6)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 5 ocorrências (p. 2, 3, 8)
- aplica etapa de preparo: [[AumentoDados|Aumento de dados]] — 4 ocorrências (p. 2, 3, 4, 8)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
