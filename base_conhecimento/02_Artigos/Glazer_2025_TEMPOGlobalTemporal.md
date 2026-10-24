---
tipo: artigo
id_origem: P103
titulo: "TEMPO: Global Temporal Building Density and Height Estimation from Satellite Imagery"
ano: 2025
autores: ["Tammy Glazer", "Gilles Hacheme", "Akram Zaytar", "Marotti, Luana", "Michaels, Amy", "Girmaw Abebe Tadesse", "White, Kevin", "Rahul Dodhia"]
doi: "10.48550/arXiv.2511.12104"
arquivo_fonte: "coleta/P103_Glazer2025_TEMPO-Global-Temporal-Building-Density-and-Height-Estimation.pdf"
markdown_fonte: "output/pdf/P103_Glazer2025_TEMPO-Global-Temporal-Building-Density-and-Height-Estimation/document.md"
paginas: 17
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Edificacoes|Edificações e urbanização]]"]
sensores: ["[[PlanetScope|PlanetScope (Dove/SuperDove)]]", "[[PlanetProdutos|Produtos Planet (visão geral)]]", "[[Sentinel2|Sentinel-2]]"]
conjuntos_dados: ["[[SpaceNet7_MUDS|SpaceNet 7 / MUDS]]", "[[OpenStreetMap|OpenStreetMap]]"]
metodos: ["[[UNet|U-Net]]"]
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]", "[[Rotulagem|Rotulagem e anotação]]", "[[Reamostragem|Reamostragem]]", "[[Normalizacao|Normalização e escala radiométrica]]", "[[AumentoDados|Aumento de dados]]"]
validacao: ["[[DivisaoTreinoTeste|Divisão treino/validação/teste]]", "[[F1|F1]]", "[[PrecisaoRecall|Precisão e recall]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Glazer 2025 — TEMPO: Global Temporal Building Density and Height Estimation from Satellite Imagery

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Tammy Glazer, Gilles Hacheme, Akram Zaytar, Marotti, Luana et al. (2025). TEMPO: Global Temporal Building Density and Height Estimation from Satellite Imagery. arXiv (Cornell University). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2511.12104
- **Arquivo de origem:** `coleta/P103_Glazer2025_TEMPO-Global-Temporal-Building-Density-and-Height-Estimation.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P103_Glazer2025_TEMPO-Global-Temporal-Building-Density-and-Height-Estimation/document.md` — 17 páginas, 8 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** We present TEMPO, a global, temporally resolved dataset of building density and height derived from high-resolution satellite imagery using deep learning models. We pair building footprint and height data from existing datasets with quarterly PlanetScope basemap satellite images to train a multi-task deep learning model that predicts building density and building height at a 37.6-meter per pixel resolution. We apply this model to global PlanetScope basemaps from Q1 2018 through Q2 2025 to create global, temporal maps of building density and height. We validate these maps by comparing against existing building footprint datasets. Our estimates achieve an F1 score between 85% and 88% on different hand-labeled subsets, and are temporally stable, with a 0.96 five-year trend-consistency score. TEMPO captures quarterly changes in built settlements at a fraction of the computational cost of com…

- “We present TEMPO, a global, temporally resolved dataset of building density and height derived from high-resolution satellite imagery using deep learning models.” (p. 1, seção Abstract)
- “In this paper, we introduce TEMPO, the first quarterly updated, global building dataset at a 37.6-meter spatial resolution derived from satellite imagery.” (p. 2, seção 1 Introduction)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “For images captured between 2019 and 2021, UDMs are 8-bit images that encode pixel clarity.” (p. 2, seção 2 Data)
- “For example, according to data derived 1 Note: RapidEye imagery is used in global basemaps generated between 2019 and 2020.” (p. 2, seção 2 Data)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **PlanetScope**: 20 ocorrências (p. 1, 2, 3, 5, 6)
- sensor/produto **Planet (mosaicos e cenas)**: 17 ocorrências (p. 2, 3, 5, 6, 7)
- sensor/produto **Sentinel-2**: 6 ocorrências (p. 3, 4, 15)
- sensor/produto **SAR**: 2 ocorrências (p. 3, 4)
- conjunto de dados **SpaceNet 7 (MUDS)**: 10 ocorrências (p. 4, 5, 10, 12)
- conjunto de dados **OpenStreetMap**: 7 ocorrências (p. 2, 3, 4, 5)
- “These challenges are compounded by uneven data availability across regions, where ground truth are disproportionately concentrated in wealthier and urbanized regions leaving vast, resource constrained areas underrepresented.” (p. 2, seção 1 Introduction)
- “F1 is well-suited for comparing against reference datasets that are available only at specific timestamps or at coarser spatial resolutions, and is robust in the presence of strong class imbalance.” (p. 9, seção 3 Density values > 2 / 255 are considered to represent a val)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 22 ocorrências (p. 2, 3, 4, 5, 6)
- **Rotulagem / anotação**: 15 ocorrências (p. 1, 2, 5, 6, 9)
- **Reamostragem**: 8 ocorrências (p. 4, 5, 6, 7, 12)
- **Normalização / escala**: 6 ocorrências (p. 3, 4, 5, 6, 8)
- **Aumento de dados**: 6 ocorrências (p. 6, 10, 11)
- **Mosaicos e compostos**: 4 ocorrências (p. 2, 4, 15)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 10 menções vs 1 de pares)
**Métodos detectados automaticamente:**
- método/família **U-Net**: 6 ocorrências (p. 6, 10, 15)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 1 ” (p. 6)
- batch: “batch size of 64” (p. 6)
- otimizador: “AdamW” optimizer with a tuned learning rate o” (p. 6)
- tamanho do patch: “4096 x 4096 pixel” (p. 2)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 3 ocorrências (p. 6, 7, 11)
- métrica **F1**: 15 ocorrências (p. 1, 9, 11, 12)
- métrica **Precisão/Recall**: 11 ocorrências (p. 8, 9, 12)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “Our estimates achieve an F1 score between 85% and 88% on different hand-labeled subsets, and are temporally stable, with a 0.96 five-year trend-consistency score.” (p. 1, seção Abstract)
- “The inference workflow consists of running the model on nearly 1PB of quarterly PlanetScope basemap imagery from Q1 2018 through Q2 2025 with post-processing to improve temporal consistency. from Planet’s Q3 2023 UDMs, 16% of global basemap quads contain cloud” (p. 3, seção 2 Data)
- “Upper table: detection (F1 at 1% threshold); lower table: regression (MAE in % for density, m for height).” (p. 11, seção 4 Results)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “Even state-of-the-art building datasets struggle to achieve consistent performance across visually diverse geographies. .” (p. 2, seção 1 Introduction)
- “While PlanetScope visual basemaps are designed to provide consistent, high-resolution global imagery, they come with limitations for analytical use.” (p. 2, seção 2 Data)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/microsoft/buildings (p. 2)
- URL citada: https://github.com/microsoft/buildings (p. 2)
- declaração: “These challenges are compounded by uneven data availability across regions, where ground truth are disproportionately concentrated in wealthier and urbanized regions leaving vast, resource constrained areas underrepresented.” (p. 2)
- declaração: “Globally, the combined dataset contains 2.3 billion footprints and is the most comprehensive open-source set of building footprint data.” (p. 4)
- hiperparâmetros **não detectados** automaticamente: épocas/iterações, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Quase tempo real 2 (p. 2); Latência / frequência 2 (p. 2, 15); Custo 2 (p. 1, 15); Sistema operacional 1 (p. 8)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[PlanetScope|PlanetScope (Dove/SuperDove)]] — 20 ocorrências (p. 1, 2, 3, 5, 6)
- utiliza dado/sensor: [[PlanetProdutos|Produtos Planet (visão geral)]] — 17 ocorrências (p. 2, 3, 5, 6, 7)
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 6 ocorrências (p. 3, 4, 15)
- emprega conjunto de dados: [[SpaceNet7_MUDS|SpaceNet 7 / MUDS]] — 10 ocorrências (p. 4, 5, 10, 12)
- emprega conjunto de dados: [[OpenStreetMap|OpenStreetMap]] — 7 ocorrências (p. 2, 3, 4, 5)
- utiliza método: [[UNet|U-Net]] — 6 ocorrências (p. 6, 10, 15)
- é avaliado por: [[F1|F1]] — 15 ocorrências (p. 1, 9, 11, 12)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 11 ocorrências (p. 8, 9, 12)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 22 ocorrências (p. 2, 3, 4, 5, 6)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 15 ocorrências (p. 1, 2, 5, 6, 9)
- aplica etapa de preparo: [[Reamostragem|Reamostragem]] — 8 ocorrências (p. 4, 5, 6, 7, 12)
- aplica etapa de preparo: [[Normalizacao|Normalização e escala radiométrica]] — 6 ocorrências (p. 3, 4, 5, 6, 8)
- aplica etapa de preparo: [[AumentoDados|Aumento de dados]] — 6 ocorrências (p. 6, 10, 11)
- adota desenho de validação: [[DivisaoTreinoTeste|Divisão treino/validação/teste]] — 3 ocorrências (p. 6, 7, 11)
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
