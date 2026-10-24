---
tipo: artigo
id_origem: P169
titulo: "Semi-Automatic Classification Plugin: A Python tool for the download and processing of remote sensing images in QGIS"
ano: 2021
autores: ["Luca Congedo"]
doi: "10.21105/joss.03172"
arquivo_fonte: "coleta/P169_Congedo2021_Semi-Automatic-Classification-Plugin-A-Python-tool-for-the-d.pdf"
markdown_fonte: "output/pdf/P169_Congedo2021_Semi-Automatic-Classification-Plugin-A-Python-tool-for-the-d/document.md"
paginas: 6
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: []
sensores: ["[[Sentinel1|Sentinel-1]]", "[[Sentinel2|Sentinel-2]]", "[[Landsat|Landsat]]"]
conjuntos_dados: []
metodos: []
preparo: []
validacao: []
ferramentas: ["[[QGIS|QGIS]]", "[[GDAL|GDAL / rasterio]]"]
tags: [artigo, leitura/automatica]
---

# Congedo 2021 — Semi-Automatic Classification Plugin: A Python tool for the download and processing of remote sensing images in QGIS

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Luca Congedo (2021). Semi-Automatic Classification Plugin: A Python tool for the download and processing of remote sensing images in QGIS. The Journal of Open Source Software. Tipo no catálogo: Software.
- **DOI/URL:** https://doi.org/10.21105/joss.03172
- **Arquivo de origem:** `coleta/P169_Congedo2021_Semi-Automatic-Classification-Plugin-A-Python-tool-for-the-d.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P169_Congedo2021_Semi-Automatic-Classification-Plugin-A-Python-tool-for-the-d/document.md` — 6 páginas, 8 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “The aim of this paper is to describe the main characteristics of the Semi-Automatic Classification Plugin for the land cover classification of remote sensing images. ## Statement of need Remote sensing is the measurement, by a sensor instal” (p. 1, seção Início)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-1**: 4 ocorrências (p. 2, 3)
- sensor/produto **Sentinel-2**: 3 ocorrências (p. 1, 2, 3)
- sensor/produto **Landsat**: 3 ocorrências (p. 1, 2, 3)
- “- Conversion to reflectance for ASTER, GOES, Landsat, MODIS, Sentinel-1, Sentinel-2, and Sentinel-3 images; - Clip multiple rasters at once; - Cloud masking based on the values of a raster mask; - Mosaic band sets, merging the corresponding” (p. 3, seção Início)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

Não informado (nada detectado automaticamente).

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

Não informado (nada detectado automaticamente).

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/openjournals/joss-reviews/issues/3172 (p. 1)
- URL citada: https://github.com/openjournals/joss-reviews/issues/3172 (p. 1)
- URL citada: https://github.com/semiautomaticgit/SemiAutomaticClassificationPlugin (p. 1)
- URL citada: https://github.com/bstabler (p. 1)
- URL citada: https://github.com/joferkington (p. 1)
- declaração: “The development of open source GIS and processing software can foster environmental monitoring, which can be performed with no cost for software and remote sensing images considering the free data availability.” (p. 1)
- declaração: “QGIS is an open source GIS software which provides several tools for data visualization and analysis; it is mainly written in C++ code, but it also allows to extend the functions thereof through API and plugins written in Python (QGIS Devel” (p. 1)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 1 (p. 1)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Sentinel1|Sentinel-1]] — 4 ocorrências (p. 2, 3)
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 3 ocorrências (p. 1, 2, 3)
- utiliza dado/sensor: [[Landsat|Landsat]] — 3 ocorrências (p. 1, 2, 3)
- usa ferramenta: [[QGIS|QGIS]] — 12 ocorrências (p. 1, 2, 3)
- usa ferramenta: [[GDAL|GDAL / rasterio]] — 3 ocorrências (p. 2, 3)

## Anotações do leitor

- 
