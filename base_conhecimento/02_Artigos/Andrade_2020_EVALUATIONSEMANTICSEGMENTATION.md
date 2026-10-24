---
tipo: artigo
id_origem: P112
titulo: "EVALUATION OF SEMANTIC SEGMENTATION METHODS FOR DEFORESTATION DETECTION IN THE AMAZON"
ano: 2020
autores: ["R. B. Andrade", "Gilson Alexandre Ostwald Pedro da Costa", "Guilherme Lúcio Abelha Mota", "Mabel X. Ortega", "Raul Queiroz Feitosa", "Pedro Juan Soto Vega", "Christian Heipke"]
doi: "10.5194/isprs-archives-xliii-b3-2020-1497-2020"
arquivo_fonte: "coleta/P112_Andrade2020_EVALUATION-OF-SEMANTIC-SEGMENTATION-METHODS-FOR-DEFORESTATIO.pdf"
markdown_fonte: "output/pdf/P112_Andrade2020_EVALUATION-OF-SEMANTIC-SEGMENTATION-METHODS-FOR-DEFORESTATIO/document.md"
paginas: 9
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[Desmatamento|Desmatamento]]", "[[SegmentacaoSemantica|Segmentação semântica]]"]
sensores: ["[[Landsat|Landsat]]"]
conjuntos_dados: ["[[PRODES|PRODES (INPE)]]"]
metodos: ["[[CNN|Redes convolucionais (CNN)]]", "[[RedeSiamesa|Redes siamesas]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Andrade 2020 — EVALUATION OF SEMANTIC SEGMENTATION METHODS FOR DEFORESTATION DETECTION IN THE AMAZON

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** R. B. Andrade, Gilson Alexandre Ostwald Pedro da Costa, Guilherme Lúcio Abelha Mota, Mabel X. Ortega et al. (2020). EVALUATION OF SEMANTIC SEGMENTATION METHODS FOR DEFORESTATION DETECTION IN THE AMAZON. The international archives of the photogrammetry, remote sensing and spatial information sciences. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.5194/isprs-archives-xliii-b3-2020-1497-2020
- **Arquivo de origem:** `coleta/P112_Andrade2020_EVALUATION-OF-SEMANTIC-SEGMENTATION-METHODS-FOR-DEFORESTATIO.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P112_Andrade2020_EVALUATION-OF-SEMANTIC-SEGMENTATION-METHODS-FOR-DEFORESTATIO/document.md` — 9 páginas, 22 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “We compare the results obtained with the devised approach to those obtained with previously proposed DL-based methods (Early Fusion and Siamese Convolutional Network) using Landsat OLI-8 images acquired at different dates, covering a region” (p. 1, seção XXIV ISPRS Congress (2020 edition))
- “In this work, we evaluate an approach based on a specific Deep Learning (DL) Fully Convolutional Network (FCN) architecture, the DeepLabv3+ (Chen et al., 2018b), which we adapted to deforestation change detection.” (p. 2, seção 25 ha, a new version of the project, the DETER-B, was launch)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “We also compare the results obtained with this approach to the ones reported in a previous work (Ortega et al., 2019) over the same study area.” (p. 2, seção 25 ha, a new version of the project, the DETER-B, was launch)
- “EXPERIMENTS 5.1 Data Set Description The study area is located in the Brazilian Legal Amazon, more specifically in Par´a State, Brazil, centered on coordinates of 03 [o] 17’ 23” S and 050 [o] 55’ 08” W.” (p. 4, seção XXIV ISPRS Congress (2020 edition))
- “Figure 4 shows the reference change map of deforestation that occurred between December 2016 and December 2017.” (p. 4, seção 3 shows the same area on July 20th, 2017. These dates were)
- “We evaluated the methods over Landsat OLI-8 images, acquired in 2016 and 2017 over the same region of the Brazilian Legal Amazon, and used deforestation polygons produced by the PRODES deforestation monitoring project, of the Brazilian Nati” (p. 6, seção XXIV ISPRS Congress (2020 edition))

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Landsat**: 4 ocorrências (p. 1, 2, 4, 6)
- conjunto de dados **PRODES**: 4 ocorrências (p. 2, 4, 6)
- “We compare the results obtained with the devised approach to those obtained with previously proposed DL-based methods (Early Fusion and Siamese Convolutional Network) using Landsat OLI-8 images acquired at different dates, covering a region” (p. 1, seção XXIV ISPRS Congress (2020 edition))
- “We divided the input images into tiles of the same size and obtained a total of 15 tiles.” (p. 5, seção XXIV ISPRS Congress (2020 edition))
- “Deforestation area in the training scenarios. |Trainingtiles|Area(pixels)|Proportion(%)| |---|---|---| |~~1 tile~~|~~2137~~|~~1.1~~| |~~2 tiles~~|~~12112~~|~~3.3~~| |~~3 tiles~~|~~16376~~|~~2.9~~| |~~4 tiles~~|~~24438~~|~~3.3~~| the defores” (p. 5, seção 14 and 15 for test. Figure 4 shows the image tile locations )
- “All the above mentioned projects, however, rely mostly on visual interpretation and manual operations.” (p. 2, seção 25 ha, a new version of the project, the DETER-B, was launch)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 61 ocorrências (p. 1, 2, 3, 4, 5)
- **Reamostragem**: 3 ocorrências (p. 3)
- **Rotulagem / anotação**: 3 ocorrências (p. 2, 4, 5)
- **Normalização / escala**: 2 ocorrências (p. 3, 5)
- **Índices espectrais**: 2 ocorrências (p. 5)
- **Aumento de dados**: 2 ocorrências (p. 5)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **CNN**: 18 ocorrências (p. 2, 3, 5, 6, 7)
- método/família **Rede siamesa**: 13 ocorrências (p. 1, 2, 3, 6)
- método/família **U-Net**: 3 ocorrências (p. 2, 3)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 0.001 and weight decay of 0.9” (p. 5)
- batch: “batch size was set to 32” (p. 5)
- épocas/iterações: “10 epochs” (p. 5)
- otimizador: “Adam optimizer, with the learning rate of 0” (p. 5)
- perda: “focal loss function (Lin et al” (p. 5)
- tamanho do patch: “64 × 64 pixel” (p. 4)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Desbalanceamento**: 6 ocorrências (p. 5, 7)
- **Conjuntos treino/val/teste**: 3 ocorrências (p. 5)
- **Teste externo / generalização**: 2 ocorrências (p. 7)
- métrica **F1**: 6 ocorrências (p. 1, 6, 7)
- métrica **Acurácia global**: 3 ocorrências (p. 1, 2, 6)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Sistema operacional 1 (p. 6); Revisão humana 1 (p. 2); Custo 1 (p. 6)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Landsat|Landsat]] — 4 ocorrências (p. 1, 2, 4, 6)
- emprega conjunto de dados: [[PRODES|PRODES (INPE)]] — 4 ocorrências (p. 2, 4, 6)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 18 ocorrências (p. 2, 3, 5, 6, 7)
- utiliza método: [[RedeSiamesa|Redes siamesas]] — 13 ocorrências (p. 1, 2, 3, 6)
- trata a tarefa: [[Desmatamento|Desmatamento]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[SegmentacaoSemantica|Segmentação semântica]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
