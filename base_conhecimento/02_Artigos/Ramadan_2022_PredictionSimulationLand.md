---
tipo: artigo
id_origem: P184
titulo: "Prediction and Simulation of Land Use and Land Cover Changes Using Open Source QGIS. A Case Study of Purwokerto, Central Java, Indonesia"
ano: 2022
autores: ["Gian Felix Ramadan", "Iswari Nur Hidayati"]
doi: "10.22146/ijg.68702"
arquivo_fonte: "coleta/P184_Ramadan2022_Prediction-and-Simulation-of-Land-Use-and-Land-Cover-Changes.pdf"
markdown_fonte: "output/pdf/P184_Ramadan2022_Prediction-and-Simulation-of-Land-Use-and-Land-Cover-Changes/document.md"
paginas: 8
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[ClassificacaoCobertura|Classificação de cobertura e uso da terra]]"]
sensores: ["[[Landsat|Landsat]]"]
conjuntos_dados: []
metodos: []
preparo: []
validacao: ["[[DivisaoTemporal|Divisão temporal]]", "[[Kappa|Coeficiente kappa]]"]
ferramentas: ["[[QGIS|QGIS]]"]
tags: [artigo, leitura/automatica]
---

# Ramadan 2022 — Prediction and Simulation of Land Use and Land Cover Changes Using Open Source QGIS. A Case Study of Purwokerto, Central Java, Indonesia

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Gian Felix Ramadan, Iswari Nur Hidayati (2022). Prediction and Simulation of Land Use and Land Cover Changes Using Open Source QGIS. A Case Study of Purwokerto, Central Java, Indonesia. Indonesian Journal of Geography. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.22146/ijg.68702
- **Arquivo de origem:** `coleta/P184_Ramadan2022_Prediction-and-Simulation-of-Land-Use-and-Land-Cover-Changes.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P184_Ramadan2022_Prediction-and-Simulation-of-Land-Use-and-Land-Cover-Changes/document.md` — 8 páginas, 13 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Abstract Population size multiplies along with the increasing need for residential space. As often occurs in developing cities like Purwokerto, population growth is associated with land use/land cover (LULC) change to accommodate housing demand both in the present and future. Therefore, this study was intended to map LULC changes in three different years: 2008, 2013, and 2018, and predict the change in 2023. For LULC data extraction, a pixel-based digital classification with a maximum likelihood algorithm was applied to Landsat images. In addition, the LULC change prediction was modeled with Modules for Land Use Change Simulations (MOLUSCE) from the QGIS plugins. It used two algorithms: artificial neural network (ANN) with a multilayer perceptron (MLP) and cellular automata (CA). The LULC classifications for 2008, 2013, and 2018 were 88%, 86%, and 88% accurate, while the prediction was 7…


## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “Study Area Data Collection The LULC conditions in three different years were determined from Landsat 5 Thematic Mapper (TM) image data recorded in 2008 and Landsat 8 Operational Land Imager (OLI) image data in 2013 and 2018 available at the” (p. 2, seção Study Area)
- “In addition, the Shuttle Radar Topography Mission (SRTM) Digital Elevation Model (DEM) with a spatial resolution of 30 meters (Table 2) was used to determine the elevation and slopes in the study area.” (p. 2, seção Study Area)
- “In this study, detection of changes in LULC was carried out according to the RPJMD period, namely 2008 to 2013 and 2013 to 2018 to determine the transition process.” (p. 1, seção 1. Introduction)
- “Study Area Data Collection The LULC conditions in three different years were determined from Landsat 5 Thematic Mapper (TM) image data recorded in 2008 and Landsat 8 Operational Land Imager (OLI) image data in 2013 and 2018 available at the” (p. 2, seção Study Area)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Landsat**: 13 ocorrências (p. 1, 2, 3, 4)
- resolução mencionada: 30 m (p. 3)
- “The field data were obtained from interviews, observations of a collection of Google Earth images, and direct observations in the field.” (p. 2, seção Study Area)
- “An accuracy of 85% is considered to have a maximum error rate between the results of the LULC classification and the reference data so an accuracy of more than 85% is still acceptable. ​ Multitemporal LULC Changes The LULC conditions in PNA” (p. 4, seção 3. Result and Discussion)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 2 ocorrências (p. 4)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate, and the neighborhood” (p. 6)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Divisão temporal**: 3 ocorrências (p. 1, 2, 3)
- métrica **Kappa**: 8 ocorrências (p. 1, 6, 7)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “The LULC classifications for 2008, 2013, and 2018 were 88%, 86%, and 88% accurate, while the prediction was 75.26% accurate, with a kappa of 0.634.” (p. 1, seção 1. Introduction)
- “With these rates, the classification results meet the minimum requirement for accuracy, 85 % (Anderson, 1971).” (p. 4, seção 3. Result and Discussion)
- “An accuracy of 85% is considered to have a maximum error rate between the results of the LULC classification and the reference data so an accuracy of more than 85% is still acceptable. ​ Multitemporal LULC Changes The LULC conditions in PNAR Purwokerto were co” (p. 4, seção 3. Result and Discussion)
- “The results of the MLP modeling in Figure 5 obtained a kappa validation value of 0.789 with an overall minimum error of 0.03837.” (p. 6, seção 3. This map shows that vegetation was mainly scatt)

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 1)
- declaração: “ISSN 2354-9114 (online), ISSN 0024-9521 (print) Indonesian Journal of Geography Vol 54, No 3 (2022): 344-351 DOI: 10.22146/ijg.68702 website: htps://jurnal.ugm.ac.id/ijg ©2022 Faculty of Geography UGM and The Indonesian Geographers Associat” (p. 1)
- declaração: “Integrating remote sensing with GIS is applied in this study using open source QGIS.” (p. 1)
- hiperparâmetros **não detectados** automaticamente: batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Quase tempo real 1 (p. 1)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Landsat|Landsat]] — 13 ocorrências (p. 1, 2, 3, 4)
- é avaliado por: [[Kappa|Coeficiente kappa]] — 8 ocorrências (p. 1, 6, 7)
- usa ferramenta: [[QGIS|QGIS]] — 4 ocorrências (p. 1, 3)
- adota desenho de validação: [[DivisaoTemporal|Divisão temporal]] — 3 ocorrências (p. 1, 2, 3)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[ClassificacaoCobertura|Classificação de cobertura e uso da terra]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
