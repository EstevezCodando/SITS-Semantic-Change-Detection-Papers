---
tipo: artigo
id_origem: P104
titulo: "Smartflow: Enabling Scalable Spatiotemporal Geospatial Research"
ano: 2023
autores: ["David McVicar", "Brian Avant", "Adrian Gould", "Diego Torrejon", "Charles Della Porta", "Ryan Mukherjee"]
doi: "10.48550/arXiv.2506.03022"
arquivo_fonte: "coleta/P104_McVicar2023_Smartflow-Enabling-Scalable-Spatiotemporal-Geospatial-Resear.pdf"
markdown_fonte: "output/pdf/P104_McVicar2023_Smartflow-Enabling-Scalable-Spatiotemporal-Geospatial-Resear/document.md"
paginas: 4
tipo_documento: "artigo curto (≤4 páginas; verificar)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[Edificacoes|Edificações e urbanização]]"]
sensores: []
conjuntos_dados: []
metodos: []
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# McVicar 2023 — Smartflow: Enabling Scalable Spatiotemporal Geospatial Research

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** David McVicar, Brian Avant, Adrian Gould, Diego Torrejon et al. (2023). Smartflow: Enabling Scalable Spatiotemporal Geospatial Research. IEEE International Geoscience and Remote Sensing Symposium (IGARSS). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2506.03022
- **Arquivo de origem:** `coleta/P104_McVicar2023_Smartflow-Enabling-Scalable-Spatiotemporal-Geospatial-Resear.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P104_McVicar2023_Smartflow-Enabling-Scalable-Spatiotemporal-Geospatial-Resear/document.md` — 4 páginas, 28 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo curto (≤4 páginas; verificar).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** BlackSky introduces Smartflow, a cloud-based framework enabling scalable spatiotemporal geospatial research built on open-source tools and technologies. Using STAC-compliant catalogs as a common input, heterogeneous geospatial data can be processed into standardized datacubes for analysis and model training. Model experimentation is managed using a combination of tools, including ClearML, Tensorboard, and Apache Superset. Underpinning Smartflow is Kubernetes, which orchestrates the provisioning and execution of workflows to support both horizontal and vertical scalability. This combination of features makes Smartflow well-suited for geospatial model development and analysis over large geographic areas, time scales, and expansive image archives. We also present a novel neural architecture, built using Smartflow, to monitor large geographic areas for heavy construction. Qualitative results…

- “Using Smartflow, we developed a novel deep-learning model to identify heavy construction occurring over broad geographic areas, time scales, and heterogeneous sensor data, including Sentinel-2, Landsat, WorldView, and Planet.” (p. 2, seção 3. CONSTRUCTION MODEL)
- “We introduced Smartflow, a novel framework that enables scalable spatiotemporal geospatial research built upon opensource tools and cloud computing.” (p. 3, seção 4. CONCLUSION)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- “In the figure, a sequence of 5 images is shown for each construction site with the detected construction bound aries outlined in red.” (p. 3, seção 3. CONSTRUCTION MODEL)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 3 ocorrências (p. 3, 4)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **U-Net**: 3 ocorrências (p. 3, 4)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

Não informado (nada detectado automaticamente).

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/stac-utils/pystac (p. 1)
- URL citada: https://github.com/stac-utils/pystac (p. 1)
- declaração: “BlackSky introduces Smartflow, a cloud-based framework enabling scalable spatiotemporal geospatial research built on open-source tools and technologies.” (p. 1)
- declaração: “GeoEngine assembles a mix of proprietary and open-source tools into an architecture for supporting model training and experimentation, as well as model inference and deployment.” (p. 1)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 3 (p. 1, 2); Revisão humana 2 (p. 1); Latência / frequência 1 (p. 1)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
