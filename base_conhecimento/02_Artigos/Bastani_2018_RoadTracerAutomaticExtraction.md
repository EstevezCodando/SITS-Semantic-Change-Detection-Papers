---
tipo: artigo
id_origem: P37
titulo: "RoadTracer: Automatic Extraction of Road Networks From Aerial Images"
ano: 2018
autores: ["Favyen Bastani", "Songtao He", "Sofiane Abbar", "Mohammad Alizadeh", "Hari Balakrishnan", "Sanjay Chawla", "Samuel R. Madden", "David J. DeWitt"]
doi: "10.1109/cvpr.2018.00496"
arquivo_fonte: "coleta/P37_Bastani2018_RoadTracer-Automatic-Extraction-of-Road-Networks-From-Aerial.pdf"
markdown_fonte: "output/pdf/P37_Bastani2018_RoadTracer-Automatic-Extraction-of-Road-Networks-From-Aerial/document.md"
paginas: 9
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[Vias|Vias e estradas]]"]
sensores: ["[[ImagensAereas|Imagens aéreas]]"]
conjuntos_dados: ["[[OpenStreetMap|OpenStreetMap]]"]
metodos: ["[[CNN|Redes convolucionais (CNN)]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Bastani 2018 — RoadTracer: Automatic Extraction of Road Networks From Aerial Images

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Favyen Bastani, Songtao He, Sofiane Abbar, Mohammad Alizadeh et al. (2018). RoadTracer: Automatic Extraction of Road Networks From Aerial Images. IEEE Computer Society Conference on Computer Vision and Pattern Recognition. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1109/cvpr.2018.00496
- **Arquivo de origem:** `coleta/P37_Bastani2018_RoadTracer-Automatic-Extraction-of-Road-Networks-From-Aerial.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P37_Bastani2018_RoadTracer-Automatic-Extraction-of-Road-Networks-From-Aerial/document.md` — 9 páginas, 12 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Mapping road networks is currently both expensive and labor-intensive. High-resolution aerial imagery provides a promising avenue to automatically infer a road network. Prior work uses convolutional neural networks (CNNs) to detect which pixels belong to a road (segmentation), and then uses complex post-processing heuristics to infer graph connectivity. We show that these segmentation methods have high error rates because noisy CNN outputs are difficult to correct. We propose RoadTracer, a new method to automatically construct accurate road network maps from aerial images. RoadTracer uses an iterative search process guided by a CNN-based decision function to derive the road network graph directly from the output of the CNN. We compare our approach with a segmentation method on fifteen cities, and find that at a 5% error rate, RoadTracer correctly captures 45% more junctions across these …

- “We propose RoadTracer, a new method to automatically construct accurate road network maps from aerial images.” (p. 1, seção Abstract)
- “We compare our approach with a segmentation method on fifteen cities, and find that at a 5% error rate, RoadTracer correctly captures 45% more junctions across these cities.” (p. 1, seção Abstract)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Imagens aéreas**: 16 ocorrências (p. 1, 2, 3, 4, 6)
- conjunto de dados **OpenStreetMap**: 8 ocorrências (p. 1, 3, 4, 6, 8)
- resolução mencionada: 60 cm (p. 6)
- “In fact, even obtaining “ground truth” maps in well-traveled areas may be difficult; recent work reported that the discrepancy between OpenStreetMap (OSM) and the TorontoCity dataset was 14% (the recall according to a certain metric for OSM” (p. 1, seção 1. Introduction)
- “They then implement a complex postprocessing pipeline to interpret the segmentation output and extract topological structure to construct a map.” (p. 1, seção 1. Introduction)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 16 ocorrências (p. 1, 2, 3, 4, 5)
- **Recorte em patches/tiles**: 3 ocorrências (p. 7)
- **Segmentação em objetos**: 2 ocorrências (p. 2)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **CNN**: 47 ocorrências (p. 1, 2, 3, 4, 5)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 3 ocorrências (p. 6, 7)
- métrica **Precisão/Recall**: 18 ocorrências (p. 1, 6, 7)
- métrica **IoU**: 5 ocorrências (p. 6, 7)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “In fact, even obtaining “ground truth” maps in well-traveled areas may be difficult; recent work reported that the discrepancy between OpenStreetMap (OSM) and the TorontoCity dataset was 14% (the recall according to a certain metric for OSM was 0.86).” (p. 1, seção 1. Introduction)
- “DeepRoadMapper fails to produce maps with better than a 19% average error rate.” (p. 2, seção 25 other cities. We make our code and a demonstrat)
- “Average TOPO recall and error rate over the test cities. |Scheme|Correct|Long|Short|NoPath| |---|---|---|---|---| |DeepRoadMapper|0.21|0.29|0.03|0.47| |Seg.” (p. 7, seção 5. Evaluation)
- “The map with 18% error is too noisy to be useful. one axis corresponds to recall and the other corresponds to error rate.” (p. 7, seção 5. Evaluation)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “DeepRoadMapper fails to produce maps with better than a 19% average error rate.” (p. 2, seção 25 other cities. We make our code and a demonstration of)
- “However, the output of road segmentation, consisting of a probability of each pixel being part of a road, cannot be directly used as a road network graph.” (p. 2, seção 2. Related Work)
- “The CNN does not output the ideal angle at the turn; this causes it to quickly veer off the actual road because it never saw such deviations from the road during training, and hence it cannot correct course.” (p. 5, seção 4.1. Static Training Dataset)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 7)
- declaração: “We include more outputs in the supplementary material, and make our code, full-resolution outputs, and videos 4726” (p. 7)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[ImagensAereas|Imagens aéreas]] — 16 ocorrências (p. 1, 2, 3, 4, 6)
- emprega conjunto de dados: [[OpenStreetMap|OpenStreetMap]] — 8 ocorrências (p. 1, 3, 4, 6, 8)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 47 ocorrências (p. 1, 2, 3, 4, 5)
- trata a tarefa: [[Vias|Vias e estradas]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
