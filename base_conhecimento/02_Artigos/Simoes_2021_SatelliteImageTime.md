---
tipo: artigo
id_origem: P70
titulo: "Satellite Image Time Series Analysis for Big Earth Observation Data"
ano: 2021
autores: ["Rolf Ezequiel de Oliveira Simões", "Gilberto Câmara", "Gilberto Ribeiro de Queiroz", "Felipe Carvalho de Souza", "Pedro R. Andrade", "Lorena Santos", "Alexandre Carvalho", "Karine Reis Ferreira"]
doi: "10.3390/rs13132428"
arquivo_fonte: "coleta/P70_Simoes2021_Satellite-Image-Time-Series-Analysis-for-Big-Earth-Observati.pdf"
markdown_fonte: "output/pdf/P70_Simoes2021_Satellite-Image-Time-Series-Analysis-for-Big-Earth-Observati/document.md"
paginas: 23
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[SITS|Séries temporais de imagens (SITS)]]"]
sensores: ["[[Landsat|Landsat]]", "[[Sentinel2|Sentinel-2]]"]
conjuntos_dados: ["[[BrazilDataCube|Brazil Data Cube]]"]
metodos: []
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Simoes 2021 — Satellite Image Time Series Analysis for Big Earth Observation Data

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Rolf Ezequiel de Oliveira Simões, Gilberto Câmara, Gilberto Ribeiro de Queiroz, Felipe Carvalho de Souza et al. (2021). Satellite Image Time Series Analysis for Big Earth Observation Data. Remote Sensing. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.3390/rs13132428
- **Arquivo de origem:** `coleta/P70_Simoes2021_Satellite-Image-Time-Series-Analysis-for-Big-Earth-Observati.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P70_Simoes2021_Satellite-Image-Time-Series-Analysis-for-Big-Earth-Observati/document.md` — 23 páginas, 10 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Abstract: The development of analytical software for big Earth observation data faces several challenges. Designers need to balance between conflicting factors. Solutions that are efficient for specific hardware architectures can not be used in other environments. Packages that work on generic hardware and open standards will not have the same performance as dedicated solutions. Software that assumes that its users are computer programmers are flexible but may be difficult to learn for a wide audience. This paper describes sits, an open-source R package for satellite image time series analysis using machine learning. To allow experts to use satellite imagery to the fullest extent, sits adopts a time-first, space-later approach.…

- “We propose a conceptual approach, following the idea of EO data cubes as geographical fields [ 24, 25 ].” (p. 3, seção 2. Earth Observation Data Cubes)
- “Given this situation, we developed a customised parallel processing implementation for sits to work well with big EO data.” (p. 10, seção 6. Include innovative methods for spatial post-processing.)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “This set ranges from 2000 to 2017 and includes 50,160 land use and land cover samples divided into 12 labels: Dunes, Fallow–Cotton, Millet-Cotton, Soy–Corn, Soy–Cotton, Soy–Fallow, Pasture, Rocky Savanna, Savanna, Dense Woodland, Savanna Pa” (p. 8, seção 6. Include innovative methods for spatial post-processing.)
- “The one-year classification period ranges from September 2017 to August 2018, following the agricultural calendar.” (p. 13, seção 4. Results and Discussion)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Landsat**: 8 ocorrências (p. 2, 7, 13, 14)
- sensor/produto **Sentinel-2**: 7 ocorrências (p. 2, 4, 7)
- conjunto de dados **Brazil Data Cube**: 3 ocorrências (p. 4, 7, 13)
- “Consider the neighbouring Sentinel-2 tiles “20LLP” and “20LKP” for the period 13 July 2018 to 28 July 2019.” (p. 4, seção 2. Earth Observation Data Cubes)
- “2021, 13, 2428 8 of 23 Time series tables store training data used for land use and land cover classification.” (p. 8, seção 6. Include innovative methods for spatial post-processing.)
- “In this section, we present an application of sits to produce a one-year land use and cover classification of the Cerrado biome in Brazil using Landsat-8 images.” (p. 13, seção 4. Results and Discussion)
- “Based on field observations or by interpreting high-resolution images, experts provide samples with valid locations, labels, and dates.” (p. 8, seção 6. Include innovative methods for spatial post-processing.)
- “They were interpreted by five specialists using high resolution images from the same period of the classification.” (p. 16, seção 4. Results and Discussion)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 15 ocorrências (p. 3, 4, 7, 13, 14)
- **Índices espectrais**: 3 ocorrências (p. 13, 14)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 180 menções vs 0 de pares)
**Métodos detectados automaticamente:**
- método/família **CNN**: 6 ocorrências (p. 6, 9, 14, 17)
- método/família **Random Forest**: 4 ocorrências (p. 6, 9, 17)
- método/família **BFAST**: 4 ocorrências (p. 17)
- método/família **CCDC**: 4 ocorrências (p. 17)
**Hiperparâmetros detectados automaticamente (verificar):**
- tamanho do patch: “204 × 7324 pixel” (p. 13)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Validação cruzada**: 2 ocorrências (p. 12)
- métrica **Acurácia global**: 3 ocorrências (p. 12, 16)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “The overall accuracy of the classification was 0.86.” (p. 16, seção 4. Results and Discussion)
- “Labels Producer’s Accuracy User’s Accuracy Annual Crop 0.81 0.88 Cerrado 0.89 0.91 Natural Non Vegetated 0.63 0.95 Pasture 0.82 0.76 Perennial Crop 0.51 0.74 Silviculture 0.83 0.91 Sugarcane 0.96 0.81 Water 0.93 0.97 Overall Accuracy: 0.86.” (p. 17, seção 4. Results and Discussion)
- “The classes that have the worst performance are “Perennial Crop” and “Natural Non Vegetated” with producer’s accuracy of 51% and 63%, respectively.” (p. 17, seção 4. Results and Discussion)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “If a worker fails to process a block, provide failure recovery and ensure the worker completes the job.” (p. 10, seção 4. After all the subimages are produced, join them to obtain)
- “ODC allows users to complete flexibility in the Python ecosystem, at the cost of limitations when working with large areas and requiring programming skills.” (p. 18, seção 5. Comparative Analysis)
- “Therefore, each of these solutions has benefits and drawbacks.” (p. 18, seção 5. Comparative Analysis)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/e-sensing/sitsdata (p. 20)
- URL citada: https://github.com/e-sensing/sitsdata (p. 20)
- URL citada: https://github.com/e- (p. 20)
- URL citada: https://github.com/e-sensing/sits (p. 20)
- declaração: “This paper describes sits, an open-source R package for satellite image time series analysis using machine learning.” (p. 1)
- declaração: “This paper describes sits, an open-source R package for satellite image time series analysis using machine learning that adopts a time-first, space-later approach.” (p. 2)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Sistema operacional 2 (p. 5, 18); Custo 2 (p. 18); Quase tempo real 1 (p. 3); Alertas 1 (p. 5); Latência / frequência 1 (p. 2)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Landsat|Landsat]] — 8 ocorrências (p. 2, 7, 13, 14)
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 7 ocorrências (p. 2, 4, 7)
- emprega conjunto de dados: [[BrazilDataCube|Brazil Data Cube]] — 3 ocorrências (p. 4, 7, 13)
- trata a tarefa: [[SITS|Séries temporais de imagens (SITS)]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
