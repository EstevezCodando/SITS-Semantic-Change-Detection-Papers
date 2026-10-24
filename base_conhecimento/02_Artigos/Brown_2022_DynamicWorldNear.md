---
tipo: artigo
id_origem: P45
titulo: "Dynamic World, Near real-time global 10 m land use land cover mapping"
ano: 2022
autores: ["Christopher F. Brown", "Steven P. Brumby", "Brookie Guzder-Williams", "Tanya Birch", "Samantha Brooks Hyde", "Joseph C. Mazzariello", "Wanda Czerwinski", "Valerie J. Pasquarella"]
doi: "10.1038/s41597-022-01307-4"
arquivo_fonte: "coleta/P45_Brown2022_Dynamic-World-Near-real-time-global-10-m-land-use-land-cover.pdf"
markdown_fonte: "output/pdf/P45_Brown2022_Dynamic-World-Near-real-time-global-10-m-land-use-land-cover/document.md"
paginas: 17
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[ClassificacaoCobertura|Classificação de cobertura e uso da terra]]"]
sensores: ["[[Sentinel2|Sentinel-2]]"]
conjuntos_dados: ["[[MapBiomas|MapBiomas]]"]
metodos: []
preparo: ["[[Rotulagem|Rotulagem e anotação]]", "[[PatchesTiles|Recorte em patches/tiles]]", "[[MascaraNuvem|Máscara de nuvem e sombra]]", "[[Normalizacao|Normalização e escala radiométrica]]", "[[MosaicosCompostos|Mosaicos e compostos temporais]]"]
validacao: ["[[DivisaoTreinoTeste|Divisão treino/validação/teste]]", "[[AmostragemEstratificada|Amostragem estratificada]]", "[[PrecisaoRecall|Precisão e recall]]", "[[EstimativaArea|Estimativa de área com intervalo de confiança]]"]
ferramentas: ["[[GoogleEarthEngine|Google Earth Engine]]"]
tags: [artigo, leitura/automatica]
---

# Brown 2022 — Dynamic World, Near real-time global 10 m land use land cover mapping

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Christopher F. Brown, Steven P. Brumby, Brookie Guzder-Williams, Tanya Birch et al. (2022). Dynamic World, Near real-time global 10 m land use land cover mapping. Scientific Data. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1038/s41597-022-01307-4
- **Arquivo de origem:** `coleta/P45_Brown2022_Dynamic-World-Near-real-time-global-10-m-land-use-land-cover.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P45_Brown2022_Dynamic-World-Near-real-time-global-10-m-land-use-land-cover/document.md` — 17 páginas, 35 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “We developed a new automated approach for globally consistent, high resolution, near real-time (NRT) land use land cover (LULC) classification leveraging deep learning on 10 m Sentinel-2 imagery.” (p. 1, seção Início)
- “In this paper, we introduce a new NRT LULC dataset produced using a deep-learning modeling approach.” (p. 2, seção Início)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “Thus, unlike conventional map products, Dynamic World enables a greater degree of flexibility for users to generate custom aggregations and derivative products uniquely tailored to their needs and study areas.” (p. 14, seção Methods)
- “These maps include the National Aeronautics and Space Administration (NASA) MCD12Q1 500 m resolution dataset [,] (2001– 2018), the European Space Agency (ESA) Climate Change Initiative (CCI) 300 m dataset (1992–2018), and Copernicus Global ” (p. 1, seção Início)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-2**: 55 ocorrências (p. 1, 2, 3, 4, 5)
- conjunto de dados **Dynamic World**: 116 ocorrências (p. 1, 2, 3, 6, 7)
- conjunto de dados **MapBiomas**: 5 ocorrências (p. 2, 11, 12)
- resolução mencionada: 500 m (p. 1)
- resolução mencionada: 300 m (p. 1)
- resolução mencionada: 100 m (p. 1)
- “At each sample location, we performed an initial selection of Sentinel-2 images from 2019 scenes based on image cloudiness metadata reported in the Sentinel-2 tile’s QA60 band.” (p. 2, seção Methods)
- “To achieve a large dataset of labeled Sentinel-2 scenes, we worked with two groups of annotators.” (p. 2, seção Methods)
- “Our procedure is to first take the 10 m Sentinel-2 Cloud Probability (S2C) product available in Earth Engine and join it to our working set of Sentinel-2 scenes such that each image is paired with the corresponding mask.” (p. 3, seção Methods)
- “We find that our model exhibits strong agreement with expert annotations for an unseen validation dataset, and though difficult to compare with existing products due to differences in temporal resolution and classification schemes, achieves” (p. 2, seção Início)
- “The first group included 25 annotators with previous photo-interpretation and/or remote sensing experience.” (p. 2, seção Methods)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 72 ocorrências (p. 2, 3, 4, 5, 6)
- **Recorte em patches/tiles**: 53 ocorrências (p. 2, 3, 4, 8, 9)
- **Máscara de nuvem e sombra**: 11 ocorrências (p. 3, 4, 6, 8, 9)
- **Normalização / escala**: 9 ocorrências (p. 4, 5, 6, 8, 12)
- **Mosaicos e compostos**: 7 ocorrências (p. 1, 8, 12, 13, 14)
- **Reamostragem**: 5 ocorrências (p. 3, 4, 8, 11)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 8 menções vs 0 de pares)
**Hiperparâmetros detectados automaticamente (verificar):**
- tamanho do patch: “510 × 510 pixel” (p. 2)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 3 ocorrências (p. 2, 9)
- **Amostragem estratificada**: 3 ocorrências (p. 2, 14, 15)
- **Desbalanceamento**: 2 ocorrências (p. 4, 5)
- métrica **Precisão/Recall**: 11 ocorrências (p. 9, 10, 11, 15)
- métrica **Estimativa de área**: 3 ocorrências (p. 2, 15)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 1)
- declaração: “Simultaneous advances in large-scale cloud computing and machine learning algorithms in high-performance open source software frameworks (e.g., TensorFlow ) as well as increased access to satellite 1 Google, LLC, 1600 Amphitheatre Pkwy., Mo” (p. 1)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Quase tempo real 34 (p. 1, 2, 6, 7, 8); Custo 2 (p. 4, 14); Sistema operacional 1 (p. 2); Latência / frequência 1 (p. 8); Revisão humana 1 (p. 9)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 55 ocorrências (p. 1, 2, 3, 4, 5)
- emprega conjunto de dados: [[MapBiomas|MapBiomas]] — 5 ocorrências (p. 2, 11, 12)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 11 ocorrências (p. 9, 10, 11, 15)
- é avaliado por: [[EstimativaArea|Estimativa de área com intervalo de confiança]] — 3 ocorrências (p. 2, 15)
- usa ferramenta: [[GoogleEarthEngine|Google Earth Engine]] — 17 ocorrências (p. 2, 3, 4, 6, 8)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 72 ocorrências (p. 2, 3, 4, 5, 6)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 53 ocorrências (p. 2, 3, 4, 8, 9)
- aplica etapa de preparo: [[MascaraNuvem|Máscara de nuvem e sombra]] — 11 ocorrências (p. 3, 4, 6, 8, 9)
- aplica etapa de preparo: [[Normalizacao|Normalização e escala radiométrica]] — 9 ocorrências (p. 4, 5, 6, 8, 12)
- aplica etapa de preparo: [[MosaicosCompostos|Mosaicos e compostos temporais]] — 7 ocorrências (p. 1, 8, 12, 13, 14)
- adota desenho de validação: [[DivisaoTreinoTeste|Divisão treino/validação/teste]] — 3 ocorrências (p. 2, 9)
- adota desenho de validação: [[AmostragemEstratificada|Amostragem estratificada]] — 3 ocorrências (p. 2, 14, 15)
- discute aspecto de monitoramento: [[QuaseTempoReal|Quase tempo real e latência]] — 34 ocorrências (p. 1, 2, 6, 7, 8)
- trata a tarefa: [[ClassificacaoCobertura|Classificação de cobertura e uso da terra]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
