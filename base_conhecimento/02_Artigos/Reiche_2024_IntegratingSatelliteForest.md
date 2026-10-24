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
status_leitura: "lido (parcial)"
relevancia_objetivo: "B"
tarefas: ["[[Desmatamento|Desmatamento]]"]
sensores: ["[[Sentinel1|Sentinel-1]]", "[[Sentinel2|Sentinel-2]]", "[[PlanetScope|PlanetScope (Dove/SuperDove)]]"]
conjuntos_dados: []
metodos: []
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/parcial, relevancia/B]
---

# Reiche 2024 — Integrating satellite-based forest disturbance alerts improves detection timeliness and confidence

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (parcial). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **B** — Integração de alertas com validação em PlanetScope de 3,7 m.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Johannes Reiche, Johannes Balling, Amy Pickens, Robert N. Masolele et al. (2024). Integrating satellite-based forest disturbance alerts improves detection timeliness and confidence. Environmental Research Letters. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1088/1748-9326/ad2d82
- **Arquivo de origem:** `coleta/P118_Reiche2024_Integrating-satellite-based-forest-disturbance-alerts-improv.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P118_Reiche2024_Integrating-satellite-based-forest-disturbance-alerts-improv/document.md` — 23 páginas, 12 recortes de figuras, 5 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

**Integrar alertas de perturbação florestal** de sistemas diferentes (**RADD** de Sentinel-1, **GLAD-S2** de Sentinel-2 e **GLAD-Landsat**) para detectar mais cedo e com mais confiança, em **dez sítios de 1° (~12.000 km²) na Amazônia**, ao longo de 2021 (p. 1–5).

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

**Evidência (leitura):**

- Dez sítios com tipos de mudança diferentes (incêndio em larga escala, desmatamento grande e pequeno para agricultura, corte seletivo, mineração em pequena escala, grandes tombamentos) e diferentes frequências de nuvem; contagem média de observações por sítio em 2021 (Sentinel-1 28–88, Sentinel-2 17–42 e Landsat 8–22) (p. 5–6, tabela 1).
- Máscara de floresta úmida primária 2001 menos perda 2001–2020 e mangue (p. 5).
- **Validação com PlanetScope de 3,7 m**, com apoio de Sentinel e Landsat quando a nuvem impediu a leitura visual (p. 9).

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

**Evidência (leitura) — Método de integração:**

- **Regras de confiança** baixa, alta e **mais alta** (ruleset 1 e 2): mais alta quando três sistemas detectam (ao menos confiança baixa) ou dois com confiança alta; o ruleset 2 é mais conservador (p. 7–8).
- Integração por **pixel** e também com **regra de vizinhança** (alertas a até 20–100 m reforçam a confiança uns dos outros, limite de 180 dias) (p. 8–9).

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Hiperparâmetros detectados automaticamente (verificar):**
- tamanho do patch: “20 × 22 m (10 m pixel” (p. 6)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Evidência (leitura) — Avaliação:**

- **Latência:** diferença entre a data de cada sistema e a primeira data de baixa confiança entre os três; só alertas que chegaram à confiança alta (p. 9).
- **Acurácia:** usuário e produtor ajustados por área, **250 pontos por sítio em 5 estratos** (3 sistemas, 2, 1, sem perturbação em 200 m, sem perturbação fora), unidade de 10 m com **tolerância de 30 m** pela diferença de geometria entre radar e óptico (p. 9–10).



## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Resultados:**

- Em média, RADD detecta primeiro em 3 sítios e GLAD-S2 nos demais; o GLAD-Landsat tem maior atraso (p. 10).
- **Integração dos três:** detecção mais cedo em média 16 dias (vs RADD), 9 (vs GLAD-S2) e 38 (vs GLAD-L); até 53, 33 e 70 dias por sítio; o tempo até alta confiança cai para 26 dias, e para a mais alta confiança são 45 (ruleset 1) e 73 dias (ruleset 2) (p. 10).
- **Acurácia do produtor (todos os alertas):** GLAD-S2 85,7 %, RADD 60,2 %, GLAD-L 38,3 %; **combinados 97 %** (alta e mais alta: 92,2 %); a classe de confiança mais alta tem produtor 57,1 % (ruleset 1) e 50,3 % (ruleset 2) (p. 10–11). O resumo diz que a classe mais alta **não teve falso positivo** e que a regra de vizinhança aumenta a confiança mas também os falsos positivos (p. 1).
- RADD falha em fogo e em grandes limpezas com resto de material (backscatter semelhante ao da floresta) (p. 10–11).

**Trechos numéricos detectados automaticamente (verificar):**
- “Detection accuracy The producer’s accuracy (detection rate; 100%— omission error) for individual alert systems exhibit large site-specific differences (figure 5).” (p. 10, seção 45 d to achieve the highest confidence using rules)
- “Among the individual alert systems and considering all alerts (class low and greater ), GLAD-S2 had the highest average (mean across sites) producer’s accuracy of 85.7% (53.3%–100%).” (p. 10, seção 45 d to achieve the highest confidence using rules)
- “RADD followed with the second-highest producer’s accuracy averaging 60.2% (10.8%–84.6%).” (p. 10, seção 45 d to achieve the highest confidence using rules)
- “GLAD-L consistently displayed the lowest producer’s accuracy across all sites averaging 38.3% (14.2%–91.2%).” (p. 10, seção 45 d to achieve the highest confidence using rules)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites e observações:**

- **Observações minhas:** (a) é uma avaliação em **2021 e em dez sítios**; os números por sítio variam muito (RADD de 10,8 % a 84,6 % de produtor); (b) a referência PlanetScope de 3,7 m também é visual e limitada por nuvem (p. 9); (c) a combinação de 97 % pode vir com mais falsos positivos nos níveis baixos; o texto resume que a classe mais alta fica sem falso positivo, mas com produtor de ~50 %; (d) o trabalho trata de **alertas prontos**, não de aprendizado de máquina próprio.

**Trechos detectados automaticamente (verificar contexto):**
- “This approach falls short in providing a nuanced understanding of the distinct advantages and limitations of the systems associated with different change types (e.g. fine-scale detections or wildfires) and regions characterized by persisten” (p. 4, seção 10 m in Sentinel-1 and − 2 data, for instance, enables)
- “Integrating multiple forest disturbance alert systems holds the potential to address the limitations of individual systems and offer forest disturbance alert information that is more timely, confident and user-friendly.” (p. 4, seção 10 m in Sentinel-1 and − 2 data, for instance, enables)
- “However, this approach has two main drawbacks.” (p. 14, seção 5.1. Alert integration improves detection)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 16)
- declaração: “Data availability statement The data that support the findings of this study are available upon reasonable request from the authors.” (p. 16)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** avaliação de sistemas operacionais. Compara a latência de alertas operacionais e mostra ganhos de 9 a 38 dias ao integrá-los.
- menções de termos de monitoramento (contagem, não avaliação): Alertas 230 (p. 1, 2, 3, 4, 5); Persistência / confirmação 8 (p. 4, 5, 6, 7, 8); Quase tempo real 7 (p. 2, 3, 4, 7, 15); Sistema operacional 5 (p. 3, 4, 6, 14); Latência / frequência 2 (p. 3, 6)

**Interpretação — O que reaproveitar:**

- **Integração de várias fontes com níveis de confiança** (um alerta confirmado por duas fontes sobe de classe) como modelo para combinar um detector Planet com alertas externos (RADD, GLAD, DETER).
- **Métrica de latência por pixel** (dias de atraso em relação ao primeiro alerta) para comparar sistemas.
- **Estratos de amostragem por concordância entre sistemas** (3, 2, 1 alertas) para estimar falso positivo.

**Interpretação — Cuidados para o nosso projeto:**

- Os alertas têm 10–30 m; o Planet de 5 m detecta clareiras menores (ver P91), então a combinação é complementar.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- discute aspecto de monitoramento: [[Alertas|Alertas de mudança]] — 230 ocorrências (p. 1, 2, 3, 4, 5)
- discute aspecto de monitoramento: [[PersistenciaConfirmacao|Persistência e confirmação]] — 8 ocorrências (p. 4, 5, 6, 7, 8)
- discute aspecto de monitoramento: [[QuaseTempoReal|Quase tempo real e latência]] — 7 ocorrências (p. 2, 3, 4, 7, 15)
- utiliza dado/sensor: [[Sentinel1|Sentinel-1]] — 19 ocorrências (p. 2, 3, 5, 6, 8)
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 16 ocorrências (p. 2, 3, 4, 5, 6)
- utiliza dado/sensor: [[PlanetScope|PlanetScope (Dove/SuperDove)]] — 5 ocorrências (p. 5, 8, 9, 16)
- referencia (suporte manual da leitura): [[AmostragemEstratificada|Amostragem estratificada]] — suporte vindo da leitura/título/resumo
- referencia (suporte manual da leitura): [[ReferenciaVisual|Referência por interpretação visual]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Desmatamento|Desmatamento]] — suporte vindo da leitura/título/resumo

**Comparações substantivas com outros artigos:**
- este artigo integra o alerta de [[Reiche_2021_ForestDisturbanceAlerts|Reiche 2021]] — P118 combina RADD (P119), GLAD-S2 e GLAD-Landsat; o produtor médio chega a 97%.

## Figuras selecionadas

![[Reiche_2024_IntegratingSatelliteForest_p12_Figure6.png|520]]
*Figure 6. Disturbance alerts at two sample locations for each of the individual alert systems and for the integrated alert based on (p. 12; recorte do PDF convertido)*


## Anotações do leitor

- 
