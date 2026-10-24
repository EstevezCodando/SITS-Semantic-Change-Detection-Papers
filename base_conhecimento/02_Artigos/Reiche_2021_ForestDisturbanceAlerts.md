---
tipo: artigo
id_origem: P119
titulo: "Forest disturbance alerts for the Congo Basin using Sentinel-1"
ano: 2021
autores: ["Johannes Reiche", "Adugna Mullissa", "Bart Slagter", "Yaqing Gou", "Nandin‐Erdene Tsendbazar", "Christelle Odongo-Braun", "Andreas Vollrath", "Mikaela Weisse"]
doi: "10.1088/1748-9326/abd0a8"
arquivo_fonte: "coleta/P119_Reiche2021_Forest-disturbance-alerts-for-the-Congo-Basin-using-Sentinel.pdf"
markdown_fonte: "output/pdf/P119_Reiche2021_Forest-disturbance-alerts-for-the-Congo-Basin-using-Sentinel/document.md"
paginas: 13
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[DegradacaoFlorestal|Degradação e perturbação florestal]]", "[[Edificacoes|Edificações e urbanização]]"]
sensores: ["[[Sentinel1|Sentinel-1]]", "[[Landsat|Landsat]]", "[[Sentinel2|Sentinel-2]]"]
conjuntos_dados: ["[[GlobalForestChange|Global Forest Change (Hansen)]]"]
metodos: []
preparo: ["[[MascaraNuvem|Máscara de nuvem e sombra]]", "[[MosaicosCompostos|Mosaicos e compostos temporais]]"]
validacao: []
ferramentas: ["[[GoogleEarthEngine|Google Earth Engine]]"]
tags: [artigo, leitura/automatica]
---

# Reiche 2021 — Forest disturbance alerts for the Congo Basin using Sentinel-1

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Johannes Reiche, Adugna Mullissa, Bart Slagter, Yaqing Gou et al. (2021). Forest disturbance alerts for the Congo Basin using Sentinel-1. Environmental Research Letters. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1088/1748-9326/abd0a8
- **Arquivo de origem:** `coleta/P119_Reiche2021_Forest-disturbance-alerts-for-the-Congo-Basin-using-Sentinel.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P119_Reiche2021_Forest-disturbance-alerts-for-the-Congo-Basin-using-Sentinel/document.md` — 13 páginas, 14 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 2):** A humid tropical forest disturbance alert using Sentinel-1 radar data is presented for the Congo Basin. Radar satellite signals can penetrate through clouds, allowing Sentinel-1 to provide gap-free observations for the tropics consistently every 6–12 days at 10 m spatial scale. In the densely cloud covered Congo Basin, this represents a major advantage for the rapid detection of small-scale forest disturbances such as subsistence agriculture and selective logging. Alerts were detected with latest available Sentinel-1 images and results are presented from January 2019 to July 2020. We mapped 4 million disturbance events during this period, totalling 1.4 million ha with nearly 80% of events smaller than 0.5 ha. Monthly distribution of alert totals varied widely across the Congo Basin countries and can be linked to regional differences in wet and dry season cycles, with more forest disturba…

- “Here we present a Sentinel-1-based forest disturbance alert system deployed and validated for the humid tropical forest of the Congo Basin.” (p. 3, seção 16 million ha of forest cleared between 2000 and)
- “This was done to not penalize our alerting system since the goal of alerting systems is the correct detection of new events and not the unbiased estimation of areas (Tang et al 2019).” (p. 6, seção 4.3. Validation)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “We defined the study area as humid tropical forest within the six Congo Basin countries (figure 2A).” (p. 4, seção 2. Study area and definitions)
- “Alerts were detected with latest available Sentinel-1 images and results are presented from January 2019 to July 2020.” (p. 2, seção Abstract)
- “With the European Sentinel-1A and 1B C-band radar satellites launched in 2014 and 2016 (Torres et al 2012), global temporally dense and high resolution radar data at 10 m spatial scale are freely available for the first time.” (p. 3, seção 16 million ha of forest cleared between 2000 and)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-1**: 44 ocorrências (p. 1, 2, 3, 4, 5)
- sensor/produto **Landsat**: 15 ocorrências (p. 3, 4, 6, 9, 10)
- sensor/produto **Sentinel-2**: 6 ocorrências (p. 6, 7, 9, 10, 11)
- sensor/produto **PlanetScope**: 5 ocorrências (p. 4, 6, 8)
- conjunto de dados **Global Forest Change**: 26 ocorrências (p. 2, 3, 4, 6, 9)
- resolução mencionada: 10 m (p. 2)
- resolução mencionada: 100 m (p. 3)
- resolução mencionada: 56 m (p. 3)
- “Alerts were detected with latest available Sentinel-1 images and results are presented from January 2019 to July 2020.” (p. 2, seção Abstract)
- “The new alert product can help to better study the forest dynamics in the Congo Basin with improved spatial and temporal detail and near real-time detections, and highlights the value of dense Sentinel-1 time series data for large-area trop” (p. 2, seção Abstract)
- “In this study, GRD images acquired in ascending and descending orbits were considered (figure 2B), which corresponded to an annual total of approximately 5300 images.” (p. 4, seção 3. Sentinel-1 satellite data)
- “The verification of fine-scale and low impact disturbances such as single tree canopy damages, however, is very challenging due to the shortage of high and very high-resolution and cloudfree reference data at weekly to monthly time steps.” (p. 11, seção 6. Conclusions)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Máscara de nuvem e sombra**: 9 ocorrências (p. 2, 3, 6, 10)
- **Mosaicos e compostos**: 4 ocorrências (p. 6, 7, 9, 10)
- **Correção atmosférica / reflectância**: 3 ocorrências (p. 5)
- **Normalização / escala**: 2 ocorrências (p. 5)
- **Rotulagem / anotação**: 2 ocorrências (p. 9, 11)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 14 menções vs 0 de pares)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

Não informado (nada detectado automaticamente).

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “We mapped 4 million disturbance events during this period, totalling 1.4 million ha with nearly 80% of events smaller than 0.5 ha.” (p. 2, seção Abstract)
- “For the period between January 2019 and July 2020, 72% of the benchmark forest map was covered every 12 days, 21% every 6 days, 7% less than” (p. 4, seção 3. Sentinel-1 satellite data)
- “Small forest disturbance events dominated the detected alerts, with 79.6% of all events having a mapped size between 0.2 and <0.5 ha (32.8% of the total mapped area).” (p. 8, seção 5.1. Forest disturbance alerts)
- “Disturbance events with a mapped size between 0.5 and <1 ha accounted for 12.8% (25.2% of the total mapped area), medium-scale events between” (p. 9, seção 5.1. Forest disturbance alerts)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “The primary limitations of the presented alerts are twofold.” (p. 11, seção 6. Conclusions)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 11)
- declaração: “Data availability statement The data that support the findings of this study are available upon reasonable request from the authors.” (p. 11)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** candidato a sistema operacional (verificar no texto). menções: operacional 5, alertas 78, quase tempo real 10
- menções de termos de monitoramento (contagem, não avaliação): Alertas 78 (p. 1, 2, 3, 4, 5); Persistência / confirmação 32 (p. 2, 3, 5, 7, 8); Quase tempo real 10 (p. 2, 3, 6, 8, 10); Latência / frequência 7 (p. 5, 10, 11); Sistema operacional 5 (p. 3, 4, 11)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Sentinel1|Sentinel-1]] — 44 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza dado/sensor: [[Landsat|Landsat]] — 15 ocorrências (p. 3, 4, 6, 9, 10)
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 6 ocorrências (p. 6, 7, 9, 10, 11)
- emprega conjunto de dados: [[GlobalForestChange|Global Forest Change (Hansen)]] — 26 ocorrências (p. 2, 3, 4, 6, 9)
- usa ferramenta: [[GoogleEarthEngine|Google Earth Engine]] — 6 ocorrências (p. 3, 4, 5)
- aplica etapa de preparo: [[MascaraNuvem|Máscara de nuvem e sombra]] — 9 ocorrências (p. 2, 3, 6, 10)
- aplica etapa de preparo: [[MosaicosCompostos|Mosaicos e compostos temporais]] — 4 ocorrências (p. 6, 7, 9, 10)
- discute aspecto de monitoramento: [[Alertas|Alertas de mudança]] — 78 ocorrências (p. 1, 2, 3, 4, 5)
- discute aspecto de monitoramento: [[PersistenciaConfirmacao|Persistência e confirmação]] — 32 ocorrências (p. 2, 3, 5, 7, 8)
- discute aspecto de monitoramento: [[QuaseTempoReal|Quase tempo real e latência]] — 10 ocorrências (p. 2, 3, 6, 8, 10)
- trata a tarefa: [[DegradacaoFlorestal|Degradação e perturbação florestal]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
