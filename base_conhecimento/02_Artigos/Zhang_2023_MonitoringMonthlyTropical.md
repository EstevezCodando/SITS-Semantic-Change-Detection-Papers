---
tipo: artigo
id_origem: P91
titulo: "Monitoring monthly tropical humid forest disturbances with Planet NICFI images in Cameroon"
ano: 2023
autores: ["Yihang Zhang", "Xia Wang", "Xiaodong Li", "Yun Du", "Peter M. Atkinson"]
doi: "10.1016/j.agrformet.2023.109676"
arquivo_fonte: "coleta/P91_Zhang2023_Monitoring-monthly-tropical-humid-forest-disturbances-with-P.pdf"
markdown_fonte: "output/pdf/P91_Zhang2023_Monitoring-monthly-tropical-humid-forest-disturbances-with-P/document.md"
paginas: 30
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[DegradacaoFlorestal|Degradação e perturbação florestal]]", "[[Edificacoes|Edificações e urbanização]]"]
sensores: ["[[PlanetProdutos|Produtos Planet (visão geral)]]", "[[PlanetNICFI|Planet NICFI (basemaps)]]", "[[Landsat|Landsat]]"]
conjuntos_dados: ["[[GlobalForestChange|Global Forest Change (Hansen)]]"]
metodos: []
preparo: ["[[MascaraNuvem|Máscara de nuvem e sombra]]", "[[MosaicosCompostos|Mosaicos e compostos temporais]]", "[[IndicesEspectrais|Índices espectrais (NDVI etc.)]]", "[[PatchesTiles|Recorte em patches/tiles]]"]
validacao: ["[[AmostragemEstratificada|Amostragem estratificada]]", "[[EstimativaArea|Estimativa de área com intervalo de confiança]]"]
ferramentas: ["[[GoogleEarthEngine|Google Earth Engine]]"]
tags: [artigo, leitura/automatica]
---

# Zhang 2023 — Monitoring monthly tropical humid forest disturbances with Planet NICFI images in Cameroon

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Yihang Zhang, Xia Wang, Xiaodong Li, Yun Du et al. (2023). Monitoring monthly tropical humid forest disturbances with Planet NICFI images in Cameroon. Agricultural and Forest Meteorology. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1016/j.agrformet.2023.109676
- **Arquivo de origem:** `coleta/P91_Zhang2023_Monitoring-monthly-tropical-humid-forest-disturbances-with-P.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P91_Zhang2023_Monitoring-monthly-tropical-humid-forest-disturbances-with-P/document.md` — 30 páginas, 71 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “In this paper, we develop a method to monitor monthly small-scale 20 tropical humid forest disturbances using 2021 Planet NICFI images.” (p. 1, seção 12 Chinese Academy of Sciences, Wuhan 430074, China;)
- “3, we developed a spatio-temporal filter to 12 / 30” (p. 12, seção 0 otherwise)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The entire CAM, which is a typical area 121 of selective logging and smallholder clearing in the Congo’s tropical forests (Tyukavina et al., 2018), 122 was chosen as the study site, and it is expected to use the proposed method to monitor h” (p. 5, seção 50 m Annual 2019-2022)
- “Study site and dataset 126 As shown in Fig.” (p. 5, seção 50 m Annual 2019-2022)
- “(2014) used 54 ALOS/ALOS-2 PALSAR/PALSAR-2, a dual-pole L-band Synthetic Aperture Radar (SAR), during 55 2007-2010 and 2015-2017 to estimate global forest cover maps with a spatial resolution of 25 m.” (p. 2, seção 44 Vancutsem et al., 2021; Zhu and Woodcock, 2014).)
- “(2021) 65 developed a 50 m spatial resolution near real-time forest early warning system in the tropics (JJ-FAST) 66 by using ALOS-2 PALSAR-2 mosaics during 2019-2022.” (p. 3, seção 59 disturbances (Francini et al., 2020).)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Planet (mosaicos e cenas)**: 87 ocorrências (p. 1, 2, 4, 5, 6)
- sensor/produto **Planet NICFI**: 56 ocorrências (p. 1, 2, 5, 6, 7)
- sensor/produto **Landsat**: 38 ocorrências (p. 1, 2, 3, 4, 5)
- sensor/produto **Sentinel-1**: 25 ocorrências (p. 1, 3, 4, 5, 6)
- conjunto de dados **Global Forest Change**: 11 ocorrências (p. 2, 5, 6, 10, 14)
- resolução mencionada: 10 m (p. 2)
- resolução mencionada: 250 m (p. 2)
- resolução mencionada: 25 m (p. 2)
- “(2021) applied Landsat 53 images to map 30 m global VCF and forest cover changes every five years.” (p. 2, seção 44 Vancutsem et al., 2021; Zhu and Woodcock, 2014).)
- “(2021) developed a 10 m forest disturbance alerting system based on 69 Sentinel-1 C-band SAR images, with the benefit of penetrating smoke, clouds and rain and a finer spatial 70 resolution compared to Landsat and PALSAR-2 images.” (p. 3, seção 59 disturbances (Francini et al., 2020).)
- “By analyzing two widely used humid tropical forest 136 disturbances based on Landsat images (Hansen et al., 2016) and Sentinel-1 images (Reiche et al., 2021), 137 we found that there were more forest disturbances during 2021 in CAM than in ” (p. 5, seção 50 m Annual 2019-2022)
- “Specifically, the time-series monthly Planet NICFI images were used 181 for the determination process based on visual interpretation.” (p. 7, seção 50 m Annual 2019-2022)
- “To decrease the uncertainty of visual interpretation, three experienced 183 interpreters interpreted visually the reference class of each sample unit with the help of time-series 184 monthly Planet NICFI images and very fine spatial resolut” (p. 7, seção 50 m Annual 2019-2022)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Máscara de nuvem e sombra**: 25 ocorrências (p. 1, 3, 8, 9, 10)
- **Mosaicos e compostos**: 16 ocorrências (p. 3, 5, 6, 7, 9)
- **Índices espectrais**: 7 ocorrências (p. 7, 26, 29, 30)
- **Recorte em patches/tiles**: 7 ocorrências (p. 6, 13, 18, 21)
- **Normalização / escala**: 2 ocorrências (p. 7, 29)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 12 menções vs 1 de pares)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Amostragem estratificada**: 9 ocorrências (p. 5, 7, 14, 15, 20)
- métrica **Estimativa de área**: 12 ocorrências (p. 1, 5, 7, 14, 15)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “216 We, therefore, collected cloud and non-cloud sample pixels by visual interpretation, which were used in 217 the RF model to establish the cloud cover possibility map for monthly Planet NICIF images, and 218 threshold values ranging from 20% to 40% were use” (p. 9, seção 50 m Annual 2019-2022)
- “As listed in Table 3, the possible monthly forest disturbance from January to December has the 450 best producer’s accuracy of 96.85 ± 2.65% but the least user’s accuracy of 21.37 ± 16.91%, which means 451 it has many commission errors (false positives).” (p. 20, seção 0 otherwise)
- “By contrast, the adjusted monthly forest disturbance map 452 has the best user’s accuracy of 84.67 ± 2.89% by eliminating many false positives with the spatio 453 temporal filer, but its producer’s accuracy, 61.46 ± 46.43%, is not that good, which means it has” (p. 20, seção 0 otherwise)
- “For the adjusted monthly forest disturbance map, the user’s accuracy 455 and producer’s accuracy of other land covers and stable humid forest are 88.50 ± 3.13% and 88.71 ± 456 2.72%, respectively.” (p. 20, seção 0 otherwise)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “529 5.2 Limitation and uncertainty 530 To improve the mapping of small-scale forest disturbances caused by selective logging and 531 smallholder clearing, we developed a rHueforest index and spatio-temporal filter to monitor possible 532 an” (p. 24, seção 0 otherwise)
- “579 5.3 Future research 580 Compared with the forest disturbance maps based on RADD Sentinel-1 and GFC Landsat, the 581 developed Planet NICFI possible and adjusted monthly forest disturbance maps also cannot find the 582 forest loss that o” (p. 26, seção 0 otherwise)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Alertas 10 (p. 3, 18, 19, 26, 28); Quase tempo real 9 (p. 2, 3, 4, 5, 11); Latência / frequência 5 (p. 3, 4, 24, 27); Revisão humana 3 (p. 7, 9); Persistência / confirmação 2 (p. 23, 29)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[PlanetProdutos|Produtos Planet (visão geral)]] — 87 ocorrências (p. 1, 2, 4, 5, 6)
- utiliza dado/sensor: [[PlanetNICFI|Planet NICFI (basemaps)]] — 56 ocorrências (p. 1, 2, 5, 6, 7)
- utiliza dado/sensor: [[Landsat|Landsat]] — 38 ocorrências (p. 1, 2, 3, 4, 5)
- emprega conjunto de dados: [[GlobalForestChange|Global Forest Change (Hansen)]] — 11 ocorrências (p. 2, 5, 6, 10, 14)
- é avaliado por: [[EstimativaArea|Estimativa de área com intervalo de confiança]] — 12 ocorrências (p. 1, 5, 7, 14, 15)
- usa ferramenta: [[GoogleEarthEngine|Google Earth Engine]] — 5 ocorrências (p. 6, 24, 26)
- aplica etapa de preparo: [[MascaraNuvem|Máscara de nuvem e sombra]] — 25 ocorrências (p. 1, 3, 8, 9, 10)
- aplica etapa de preparo: [[MosaicosCompostos|Mosaicos e compostos temporais]] — 16 ocorrências (p. 3, 5, 6, 7, 9)
- aplica etapa de preparo: [[IndicesEspectrais|Índices espectrais (NDVI etc.)]] — 7 ocorrências (p. 7, 26, 29, 30)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 7 ocorrências (p. 6, 13, 18, 21)
- adota desenho de validação: [[AmostragemEstratificada|Amostragem estratificada]] — 9 ocorrências (p. 5, 7, 14, 15, 20)
- discute aspecto de monitoramento: [[Alertas|Alertas de mudança]] — 10 ocorrências (p. 3, 18, 19, 26, 28)
- discute aspecto de monitoramento: [[QuaseTempoReal|Quase tempo real e latência]] — 9 ocorrências (p. 2, 3, 4, 5, 11)
- trata a tarefa: [[DegradacaoFlorestal|Degradação e perturbação florestal]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
