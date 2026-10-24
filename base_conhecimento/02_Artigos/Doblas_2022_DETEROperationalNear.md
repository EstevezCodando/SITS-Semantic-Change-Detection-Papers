---
tipo: artigo
id_origem: P117
titulo: "DETER-R: An Operational Near-Real Time Tropical Forest Disturbance Warning System Based on Sentinel-1 Time Series Analysis"
ano: 2022
autores: ["Juan Doblas", "Mariane Souza Reis", "Amanda Pinoti Belluzzo", "Camila Barata Quadros", "Douglas Rafael Vidal de Moraes", "Claudio Aparecido Almeida", "Luís Eduardo Pinheiro Maurano", "André Carvalho"]
doi: "10.3390/rs14153658"
arquivo_fonte: "coleta/P117_Doblas2022_DETER-R-An-Operational-Near-Real-Time-Tropical-Forest-Distur.pdf"
markdown_fonte: "output/pdf/P117_Doblas2022_DETER-R-An-Operational-Near-Real-Time-Tropical-Forest-Distur/document.md"
paginas: 21
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[SITS|Séries temporais de imagens (SITS)]]", "[[Desmatamento|Desmatamento]]", "[[DegradacaoFlorestal|Degradação e perturbação florestal]]", "[[Edificacoes|Edificações e urbanização]]"]
sensores: ["[[SAR|Radar (SAR)]]", "[[Sentinel1|Sentinel-1]]", "[[PlanetProdutos|Produtos Planet (visão geral)]]"]
conjuntos_dados: ["[[DETER|DETER (INPE)]]", "[[PRODES|PRODES (INPE)]]"]
metodos: []
preparo: ["[[MascaraNuvem|Máscara de nuvem e sombra]]", "[[Rotulagem|Rotulagem e anotação]]", "[[Normalizacao|Normalização e escala radiométrica]]", "[[PatchesTiles|Recorte em patches/tiles]]"]
validacao: []
ferramentas: ["[[GoogleEarthEngine|Google Earth Engine]]"]
tags: [artigo, leitura/automatica]
---

# Doblas 2022 — DETER-R: An Operational Near-Real Time Tropical Forest Disturbance Warning System Based on Sentinel-1 Time Series Analysis

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Juan Doblas, Mariane Souza Reis, Amanda Pinoti Belluzzo, Camila Barata Quadros et al. (2022). DETER-R: An Operational Near-Real Time Tropical Forest Disturbance Warning System Based on Sentinel-1 Time Series Analysis. Remote Sensing. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.3390/rs14153658
- **Arquivo de origem:** `coleta/P117_Doblas2022_DETER-R-An-Operational-Near-Real-Time-Tropical-Forest-Distur.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P117_Doblas2022_DETER-R-An-Operational-Near-Real-Time-Tropical-Forest-Distur/document.md` — 21 páginas, 27 recortes de figuras, 2 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Abstract: Continuous monitoring of forest disturbance on tropical forests is a fundamental tool to support proactive preservation actions and to stop further destruction of native vegetation. Currently most of the monitoring systems in operation are based on optical imagery, and thus are flaw-prone on areas with frequent cloud cover. As this, several Synthetic Aperture Radar (SAR)-based systems have been developed recently, aiming all-weather disturbance detection. This article presents the main aspects and the results of the first year of operation of the SAR based Near Real-Time Deforestation Detection System (DETER-R), an automated deforestation detection system focused on the Brazilian Amazon. DETER-R uses the Google Earth Engine platform to preprocess and analyze Sentinel-1 SAR time series. New images are treated and analyzed daily. After the automated analysis, the system vectorize…

- “The goal of Sentinel-1 images preprocessing is (1) To correct the variation on backscatter intensity due to variations on the local incidence angle (LIA), (2) to reduce the speckle associated with the SAR signal, and (3) to reduce backscatt” (p. 7, seção 3.2.1. Preprocessing)
- “The objective of the mission was to test the reliability of the warnings on an operational context.” (p. 12, seção 4. Results)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “DETER started issuing alerts in 2004, as part of the Action Plan for the Prevention and Control of Deforestation in the Legal Amazon (PPCDAm), which, coupled with the deployment of law-enforcement teams on the field and the delimitation of ” (p. 2, seção 1. Introduction)
- “After running a prototype of the system from November 2020 to March 2021 over a set of five areas subject to special monitoring by the Brazilian National Institute for Space Research (INPE), the system was made operational, covering the Bra” (p. 3, seção 42 days.)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **SAR**: 26 ocorrências (p. 1, 2, 3, 4, 6)
- sensor/produto **Sentinel-1**: 10 ocorrências (p. 1, 2, 4, 7, 10)
- sensor/produto **Planet (mosaicos e cenas)**: 5 ocorrências (p. 11, 13, 14, 15)
- sensor/produto **Planet NICFI**: 2 ocorrências (p. 6)
- conjunto de dados **DETER**: 108 ocorrências (p. 1, 2, 3, 4, 5)
- conjunto de dados **PRODES**: 11 ocorrências (p. 5, 8, 11, 16, 19)
- resolução mencionada: 3 m (p. 6)
- resolução mencionada: 10 m (p. 6)
- “# remote sensing Article ## DETER-R: An Operational Near-Real Time Tropical Forest Disturbance Warning System Based on Sentinel-1 Time Series Analysis Juan Doblas , Mariane S.” (p. 1, seção Início)
- “DETER-R: An Operational Near-Real Time Forest Disturbance Warning System Based on Sentinel-1 Time Series Analysis.” (p. 1, seção Início)
- “The RADD system was originally developed at the Laboratory of Geo-information Science and Remote Sensing of the Wageningen University, while researching the suitability of the Bayesian classification and update approach to detect deforestat” (p. 2, seção 42 days.)
- “INPE’s Forest/Non-forest map, built by visual interpretation.” (p. 5, seção 1. deforestation map produced by the Program for Deforestati)
- “Validation Imagery During the first year of operation, the warnings issued by DETER-R were validated by the visual interpretation of optical images.” (p. 6, seção 3. The German Aerospace Center (Deutsches Zentrum für Luft-u)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Máscara de nuvem e sombra**: 7 ocorrências (p. 1, 2, 19)
- **Rotulagem / anotação**: 7 ocorrências (p. 10, 11, 12, 17, 18)
- **Normalização / escala**: 6 ocorrências (p. 3, 4, 6, 7)
- **Recorte em patches/tiles**: 5 ocorrências (p. 2, 5, 10)
- **Mosaicos e compostos**: 2 ocorrências (p. 6)
- **Textura (GLCM)**: 2 ocorrências (p. 18, 19)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 20 menções vs 0 de pares)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

Não informado (nada detectado automaticamente).

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “If we assume the Major disagreement to represent the misdetections of the DETER-R system, we can conclude that our system has a User’s Accuracy of 99.4%.” (p. 18, seção 5. Discussion)
- “Conversely, DETER-R achieved a poor Producer’s Accuracy (around 50%) when compared to GLAD-S2 (85%).” (p. 18, seção 5. Discussion)
- “Nonetheless, the Producer’s Accuracy for DETER-R is higher than the one obtained by JJFast (23%).” (p. 18, seção 5. Discussion)
- “For instance, they proposed an example of such a process, in which results of the tuned system are comparable to other SAR NRT detection systems, with User’s Accuracy of around 98% and Producer’s Accuracy around 90%.” (p. 18, seção 5. Discussion)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “DETER started issuing alerts in 2004, as part of the Action Plan for the Prevention and Control of Deforestation in the Legal Amazon (PPCDAm), which, coupled with the deployment of law-enforcement teams on the field and the delimitation of ” (p. 2, seção 1. Introduction)
- “In our case, after discussion with the system main users and stakeholders we decided to use a MMU of 1 ha, in order to encompass the main objectives of the environmental teams’ field campaigns and their budgetary limitations.” (p. 10, seção 1. Number of warnings: Polygon mean must be higher than 1. A)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/jdoblas/DETERRAMZ (p. 6)
- URL citada: https://github.com/jdoblas/DETERRAMZ (p. 6)
- declaração: “The code used by DETER-R is open-source and can be downloaded [at: https://github.com/jdoblas/DETERRAMZ (accessed on 15 March 2022).](https://github.com/jdoblas/DETERRAMZ) Figure 3.” (p. 6)
- declaração: “The code used by DETER-R is open-source and can be downloaded at: https://github.com/jdoblas/DETERRAMZ (accessed on 15 March 2022).” (p. 6)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** candidato a sistema operacional (verificar no texto). menções: operacional 25, alertas 12, quase tempo real 19
- menções de termos de monitoramento (contagem, não avaliação): Sistema operacional 25 (p. 1, 2, 3, 4, 5); Quase tempo real 19 (p. 1, 2, 3, 17, 18); Alertas 12 (p. 2, 3, 8, 10, 12); Persistência / confirmação 8 (p. 8, 12, 13, 19); Falsos alertas 7 (p. 3, 10, 19)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[SAR|Radar (SAR)]] — 26 ocorrências (p. 1, 2, 3, 4, 6)
- utiliza dado/sensor: [[Sentinel1|Sentinel-1]] — 10 ocorrências (p. 1, 2, 4, 7, 10)
- utiliza dado/sensor: [[PlanetProdutos|Produtos Planet (visão geral)]] — 5 ocorrências (p. 11, 13, 14, 15)
- emprega conjunto de dados: [[DETER|DETER (INPE)]] — 108 ocorrências (p. 1, 2, 3, 4, 5)
- emprega conjunto de dados: [[PRODES|PRODES (INPE)]] — 11 ocorrências (p. 5, 8, 11, 16, 19)
- usa ferramenta: [[GoogleEarthEngine|Google Earth Engine]] — 11 ocorrências (p. 1, 2, 3, 4, 6)
- aplica etapa de preparo: [[MascaraNuvem|Máscara de nuvem e sombra]] — 7 ocorrências (p. 1, 2, 19)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 7 ocorrências (p. 10, 11, 12, 17, 18)
- aplica etapa de preparo: [[Normalizacao|Normalização e escala radiométrica]] — 6 ocorrências (p. 3, 4, 6, 7)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 5 ocorrências (p. 2, 5, 10)
- discute aspecto de monitoramento: [[SistemaOperacional|Sistemas operacionais]] — 25 ocorrências (p. 1, 2, 3, 4, 5)
- discute aspecto de monitoramento: [[QuaseTempoReal|Quase tempo real e latência]] — 19 ocorrências (p. 1, 2, 3, 17, 18)
- discute aspecto de monitoramento: [[Alertas|Alertas de mudança]] — 12 ocorrências (p. 2, 3, 8, 10, 12)
- trata a tarefa: [[SITS|Séries temporais de imagens (SITS)]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Desmatamento|Desmatamento]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[DegradacaoFlorestal|Degradação e perturbação florestal]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
