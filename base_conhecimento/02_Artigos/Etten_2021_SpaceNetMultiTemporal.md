---
tipo: artigo
id_origem: P11
titulo: "The SpaceNet Multi-Temporal Urban Development Challenge"
ano: 2021
autores: ["A. Van Etten", "Hogan, Daniel"]
doi: "10.48550/arXiv.2102.11958"
arquivo_fonte: "coleta/P11_Etten2021_The-SpaceNet-Multi-Temporal-Urban-Development-Challenge.pdf"
markdown_fonte: "output/pdf/P11_Etten2021_The-SpaceNet-Multi-Temporal-Urban-Development-Challenge/document.md"
paginas: 15
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[SITS|Séries temporais de imagens (SITS)]]", "[[Edificacoes|Edificações e urbanização]]"]
sensores: ["[[PlanetProdutos|Produtos Planet (visão geral)]]"]
conjuntos_dados: ["[[SpaceNet7_MUDS|SpaceNet 7 / MUDS]]"]
metodos: ["[[UNet|U-Net]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]", "[[MosaicosCompostos|Mosaicos e compostos temporais]]"]
validacao: ["[[DivisaoTreinoTeste|Divisão treino/validação/teste]]", "[[IoU|IoU / mIoU]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Etten 2021 — The SpaceNet Multi-Temporal Urban Development Challenge

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** A. Van Etten, Hogan, Daniel (2021). The SpaceNet Multi-Temporal Urban Development Challenge. arXiv (Cornell University). Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2102.11958
- **Arquivo de origem:** `coleta/P11_Etten2021_The-SpaceNet-Multi-Temporal-Urban-Development-Challenge.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P11_Etten2021_The-SpaceNet-Multi-Temporal-Urban-Development-Challenge/document.md` — 15 páginas, 18 recortes de figuras, 1 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Building footprints provide a useful proxy for many humanitarian applications. For example, building footprints are useful for high fidelity population estimates, and quantifying population statistics is fundamental to ∼ 1 / 4 of the United Nations Sustainable Development Goals Indicators. In this paper we (the SpaceNet Partners) discuss efforts to develop techniques for precise building footprint localization, tracking, and change detection via the SpaceNet Multi-Temporal Urban Development Challenge (also known as SpaceNet 7). In this NeurIPS 2020 competition, participants were asked identify and track buildings in satellite imagery time series collected over rapidly urbanizing areas. The competition centered around a brand new open source dataset of Planet Labs satellite imagery mosaics at 4m resolution, which includes 24 images (one per month) covering ≈ 100 unique geographies. Tracki…

- “To evaluate model performance on a time series of identifier-tagged footprints, we introduce a new evaluation metric: the SpaceNet Change and Object Tracking (SCOT) metric.” (p. 5, seção 1 https://registry.opendata.aws/spacenet/)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The SpaceNet 7 Challenge used a brand-new, open source dataset of medium-resolution ( ≈ 4 m) satellite imagery collected by Planet Labs’ Dove Satellites between 2017 and 2020.” (p. 3, seção 7 Challenge.)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Planet (mosaicos e cenas)**: 6 ocorrências (p. 1, 3, 10)
- conjunto de dados **SpaceNet 7 (MUDS)**: 26 ocorrências (p. 1, 2, 3, 5, 6)
- resolução mencionada: 4 m (p. 1)
- “The competition centered around a brand new open source dataset of Planet Labs satellite imagery mosaics at 4m resolution, which includes 24 images (one per month) covering ≈ 100 unique geographies.” (p. 1, seção Abstract)
- “4 Metric For this competition we defined successful building footprint identifications as proposals which overlap ground truth ( GT ) annotations with an Intersection-over-Union ( IoU ) score above a threshold of 0.25.” (p. 5, seção 1 https://registry.opendata.aws/spacenet/)
- “(a) (b) Figure 5: (a) Visualization of temporal collapse for ground truth (top row) and predictions (bottom row).” (p. 9, seção 3. There are three scenarios for all building candidates:)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 19 ocorrências (p. 3, 4, 5, 9, 10)
- **Mosaicos e compostos**: 3 ocorrências (p. 1, 3)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 24 menções vs 2 de pares)
**Métodos detectados automaticamente:**
- método/família **U-Net**: 6 ocorrências (p. 7, 8)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 3 ocorrências (p. 3, 6, 11)
- métrica **IoU**: 7 ocorrências (p. 5, 11, 12)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “4 Metric For this competition we defined successful building footprint identifications as proposals which overlap ground truth ( GT ) annotations with an Intersection-over-Union ( IoU ) score above a threshold of 0.25.” (p. 5, seção 1 https://registry.opendata.aws/spacenet/)
- “Therefore latitude (or more precisely, the absolute value of latitude) is negatively correlated with tracking (-0.39), change (-0.65) and SCOT (-0.70) score.” (p. 10, seção 3. There are three scenarios for all building cand)
- “Figure 8: Building recall as a function of area for the winning submission (IoU ≥ 0.25).” (p. 11, seção 3. There are three scenarios for all building cand)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “The closest comparison is the xView2 challenge , which examined building damage in satellite image pairs acquired before and after natural disasters; however, this task fails to address the complexities and opportunities posed by analysis o” (p. 2, seção 7 Challenge.)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 1)
- declaração: “The competition centered around a brand new open source dataset of Planet Labs satellite imagery mosaics at 4m resolution, which includes 24 images (one per month) covering ≈ 100 unique geographies.” (p. 1)
- declaração: “SpaceNet is a nonprofit LLC dedicated to accelerating open source, artificial intelligence applied research for geospatial applications, specifically foundational mapping ( i.e. building footprint & road network detection).” (p. 1)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[PlanetProdutos|Produtos Planet (visão geral)]] — 6 ocorrências (p. 1, 3, 10)
- emprega conjunto de dados: [[SpaceNet7_MUDS|SpaceNet 7 / MUDS]] — 26 ocorrências (p. 1, 2, 3, 5, 6)
- utiliza método: [[UNet|U-Net]] — 6 ocorrências (p. 7, 8)
- é avaliado por: [[IoU|IoU / mIoU]] — 7 ocorrências (p. 5, 11, 12)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 19 ocorrências (p. 3, 4, 5, 9, 10)
- aplica etapa de preparo: [[MosaicosCompostos|Mosaicos e compostos temporais]] — 3 ocorrências (p. 1, 3)
- adota desenho de validação: [[DivisaoTreinoTeste|Divisão treino/validação/teste]] — 3 ocorrências (p. 3, 6, 11)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[SITS|Séries temporais de imagens (SITS)]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
