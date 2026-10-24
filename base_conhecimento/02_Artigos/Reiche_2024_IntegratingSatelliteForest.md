---
tipo: artigo
id_origem: P118
titulo: "Integrating satellite-based forest disturbance alerts improves detection timeliness and confidence"
ano: 2024
autores: ["Johannes Reiche", "Johannes Balling", "Amy Pickens", "Robert N. Masolele", "Anika Berger", "Mikaela Weisse", "Daniel Mannarino", "Yaqing Gou"]
doi: "10.1088/1748-9326/ad2d82"
arquivo_fonte: "coleta/P118_Reiche2024_Integrating-satellite-based-forest-disturbance-alerts-improv.pdf"
markdown_fonte: "output/pdf/P118_Reiche2024_Integrating-satellite-based-forest-disturbance-alerts-improv/document.md"
paginas: 23
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Desmatamento|Desmatamento]]", "[[DegradacaoFlorestal|Degradação e perturbação florestal]]", "[[Edificacoes|Edificações e urbanização]]"]
sensores: ["[[Landsat|Landsat]]", "[[Sentinel1|Sentinel-1]]", "[[Sentinel2|Sentinel-2]]"]
conjuntos_dados: ["[[GlobalForestChange|Global Forest Change (Hansen)]]", "[[MapBiomas|MapBiomas]]"]
metodos: []
preparo: ["[[MascaraNuvem|Máscara de nuvem e sombra]]", "[[Rotulagem|Rotulagem e anotação]]"]
validacao: []
ferramentas: ["[[GoogleEarthEngine|Google Earth Engine]]"]
tags: [artigo, leitura/automatica]
---

# Reiche 2024 — Integrating satellite-based forest disturbance alerts improves detection timeliness and confidence

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Johannes Reiche, Johannes Balling, Amy Pickens, Robert N. Masolele et al. (2024). Integrating satellite-based forest disturbance alerts improves detection timeliness and confidence. Environmental Research Letters. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1088/1748-9326/ad2d82
- **Arquivo de origem:** `coleta/P118_Reiche2024_Integrating-satellite-based-forest-disturbance-alerts-improv.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P118_Reiche2024_Integrating-satellite-based-forest-disturbance-alerts-improv/document.md` — 23 páginas, 12 recortes de figuras, 5 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 2):** Satellite-based near-real-time forest disturbance alerting systems have been widely used to support law enforcement actions against illegal and unsustainable human activities in tropical forests. The availability of multiple optical and radar-based forest disturbance alerts, each with varying detection capabilities depending mainly on the satellite sensor used, poses a challenge for users in selecting the most suitable system for their monitoring needs and workflow. Integrating multiple alerts holds the potential to address the limitations of individual systems. We integrated radar-based RAdar for Detecting Deforestation (RADD) (Sentinel-1), and optical-based Global Land Analysis and Discovery Sentinel-2 (GLAD-S2) and GLAD-Landsat alerts using two confidence rulesets at ten 1 [◦] sites across the Amazon Basin. Alert integration resulted in faster detection of new disturbances by days to …

- “We introduced the highest confidence class as an addition to the low and high confidence classes of the individual systems, and showed that this displayed no false detection.” (p. 2, seção Abstract)
- “In addition to the low and high confidence levels provided by the original alert products, we introduced the highest confidence level for the integrated alerts.” (p. 7, seção 3.2. Alert integration)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “Studies that introduced alert systems (Hansen et al 2016, Ballère et al 2021, Reiche et al 2021, Watanabe et al 2021, Doblas et al 2022) typically report a single accuracy metric summarizing the detection accuracy and timeliness across the ” (p. 4, seção 10 m in Sentinel-1 and − 2 data, for instance, enables)
- “The sites located in the 4 Guyana Shield (sites 2 and 3) experience notably high cloud cover persistent over most of the wet season.” (p. 5, seção 2.1. Study area and forest baseline)
- “We used a primary humid tropical forest mask for 2001 from (Turubanova et al 2018) and removed 2001–2020 forest loss (Hansen et al 2013) and mangrove forest (Bunting et al 2018).” (p. 5, seção 2.1. Study area and forest baseline)
- “However, it reports tree cover loss only within the boundary of the primary forest mask of (Turubanova et al 2018) with 2001–2018 forest loss from (Hansen et al 2013) removed.” (p. 7, seção 2.2. Satellite alert products)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Landsat**: 25 ocorrências (p. 2, 3, 4, 5, 6)
- sensor/produto **Sentinel-1**: 19 ocorrências (p. 2, 3, 5, 6, 8)
- sensor/produto **Sentinel-2**: 16 ocorrências (p. 2, 3, 4, 5, 6)
- sensor/produto **PlanetScope**: 5 ocorrências (p. 5, 8, 9, 16)
- conjunto de dados **Global Forest Change**: 18 ocorrências (p. 2, 3, 4, 5, 6)
- conjunto de dados **MapBiomas**: 3 ocorrências (p. 3, 4)
- conjunto de dados **DETER**: 2 ocorrências (p. 3)
- resolução mencionada: 50 m (p. 3)
- resolução mencionada: 10 m (p. 3)
- “We used probability sampling (Stehman 2014) with five strata with 50 samples each, comprising a total of 250 sample points per site.” (p. 8, seção 3.3. Evaluation)
- “Confirmation implies an independent assessment, such as ground truthing or visual evaluation of very high-resolution data, to validate that the change is indeed true.” (p. 7, seção 3.2. Alert integration)
- “In some cases, persistent cloud coverage hindered visual interpretation using PlanetScope data alone, and additional reference data were consulted, including Sentinel-1 and − 2, and Landsat-7 and 8 imagery.” (p. 8, seção 3.3. Evaluation)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Máscara de nuvem e sombra**: 24 ocorrências (p. 3, 4, 5, 6, 7)
- **Rotulagem / anotação**: 6 ocorrências (p. 2, 7, 8, 9, 14)
- **Mosaicos e compostos**: 2 ocorrências (p. 12, 13)
- **Normalização / escala**: 2 ocorrências (p. 7)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Hiperparâmetros detectados automaticamente (verificar):**
- tamanho do patch: “20 × 22 m (10 m pixel” (p. 6)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

Não informado (nada detectado automaticamente).

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “Detection accuracy The producer’s accuracy (detection rate; 100%— omission error) for individual alert systems exhibit large site-specific differences (figure 5).” (p. 10, seção 45 d to achieve the highest confidence using rules)
- “Among the individual alert systems and considering all alerts (class low and greater ), GLAD-S2 had the highest average (mean across sites) producer’s accuracy of 85.7% (53.3%–100%).” (p. 10, seção 45 d to achieve the highest confidence using rules)
- “RADD followed with the second-highest producer’s accuracy averaging 60.2% (10.8%–84.6%).” (p. 10, seção 45 d to achieve the highest confidence using rules)
- “GLAD-L consistently displayed the lowest producer’s accuracy across all sites averaging 38.3% (14.2%–91.2%).” (p. 10, seção 45 d to achieve the highest confidence using rules)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “This approach falls short in providing a nuanced understanding of the distinct advantages and limitations of the systems associated with different change types (e.g. fine-scale detections or wildfires) and regions characterized by persisten” (p. 4, seção 10 m in Sentinel-1 and − 2 data, for instance, enables)
- “Integrating multiple forest disturbance alert systems holds the potential to address the limitations of individual systems and offer forest disturbance alert information that is more timely, confident and user-friendly.” (p. 4, seção 10 m in Sentinel-1 and − 2 data, for instance, enables)
- “However, this approach has two main drawbacks.” (p. 14, seção 5.1. Alert integration improves detection)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 16)
- declaração: “Data availability statement The data that support the findings of this study are available upon reasonable request from the authors.” (p. 16)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** candidato a sistema operacional (verificar no texto). menções: operacional 5, alertas 230, quase tempo real 7
- menções de termos de monitoramento (contagem, não avaliação): Alertas 230 (p. 1, 2, 3, 4, 5); Persistência / confirmação 8 (p. 4, 5, 6, 7, 8); Quase tempo real 7 (p. 2, 3, 4, 7, 15); Sistema operacional 5 (p. 3, 4, 6, 14); Latência / frequência 2 (p. 3, 6)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Landsat|Landsat]] — 25 ocorrências (p. 2, 3, 4, 5, 6)
- utiliza dado/sensor: [[Sentinel1|Sentinel-1]] — 19 ocorrências (p. 2, 3, 5, 6, 8)
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 16 ocorrências (p. 2, 3, 4, 5, 6)
- emprega conjunto de dados: [[GlobalForestChange|Global Forest Change (Hansen)]] — 18 ocorrências (p. 2, 3, 4, 5, 6)
- emprega conjunto de dados: [[MapBiomas|MapBiomas]] — 3 ocorrências (p. 3, 4)
- usa ferramenta: [[GoogleEarthEngine|Google Earth Engine]] — 6 ocorrências (p. 2, 6, 7, 16)
- aplica etapa de preparo: [[MascaraNuvem|Máscara de nuvem e sombra]] — 24 ocorrências (p. 3, 4, 5, 6, 7)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 6 ocorrências (p. 2, 7, 8, 9, 14)
- discute aspecto de monitoramento: [[Alertas|Alertas de mudança]] — 230 ocorrências (p. 1, 2, 3, 4, 5)
- discute aspecto de monitoramento: [[PersistenciaConfirmacao|Persistência e confirmação]] — 8 ocorrências (p. 4, 5, 6, 7, 8)
- discute aspecto de monitoramento: [[QuaseTempoReal|Quase tempo real e latência]] — 7 ocorrências (p. 2, 3, 4, 7, 15)
- trata a tarefa: [[Desmatamento|Desmatamento]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[DegradacaoFlorestal|Degradação e perturbação florestal]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
