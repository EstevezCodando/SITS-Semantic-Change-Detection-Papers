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
status_leitura: "lido (parcial)"
relevancia_objetivo: "B"
tarefas: ["[[Desmatamento|Desmatamento]]"]
sensores: ["[[Sentinel1|Sentinel-1]]", "[[PlanetNICFI|Planet NICFI (basemaps)]]"]
conjuntos_dados: ["[[DETER|DETER (INPE)]]"]
metodos: []
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/parcial, relevancia/B]
---

# Doblas 2022 — DETER-R: An Operational Near-Real Time Tropical Forest Disturbance Warning System Based on Sentinel-1 Time Series Analysis

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (parcial). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **B** — DETER-R: alerta operacional por radar; Planet NICFI na validação visual.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Juan Doblas, Mariane Souza Reis, Amanda Pinoti Belluzzo, Camila Barata Quadros et al. (2022). DETER-R: An Operational Near-Real Time Tropical Forest Disturbance Warning System Based on Sentinel-1 Time Series Analysis. Remote Sensing. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.3390/rs14153658
- **Arquivo de origem:** `coleta/P117_Doblas2022_DETER-R-An-Operational-Near-Real-Time-Tropical-Forest-Distur.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P117_Doblas2022_DETER-R-An-Operational-Near-Real-Time-Tropical-Forest-Distur/document.md` — 21 páginas, 27 recortes de figuras, 2 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Descrever o **DETER-R**, sistema **operacional** de alerta de desmatamento da Amazônia brasileira baseado em **séries Sentinel-1 no Google Earth Engine**, analisadas diariamente, com vetorização de aglomerados de pixels desmatados e envio dos polígonos à agência de fiscalização (p. 1).

**Resumo detectado automaticamente (p. 1):** Abstract: Continuous monitoring of forest disturbance on tropical forests is a fundamental tool to support proactive preservation actions and to stop further destruction of native vegetation. Currently most of the monitoring systems in operation are based on optical imagery, and thus are flaw-prone on areas with frequent cloud cover. As this, several Synthetic Aperture Radar (SAR)-based systems have been developed recently, aiming all-weather disturbance detection. This article presents the main aspects and the results of the first year of operation of the SAR based Near Real-Time Deforestation Detection System (DETER-R), an automated deforestation detection system focused on the Brazilian Amazon. DETER-R uses the Google Earth Engine platform to preprocess and analyze Sentinel-1 SAR time series. New images are treated and analyzed daily. After the automated analysis, the system vectorize…

- “The goal of Sentinel-1 images preprocessing is (1) To correct the variation on backscatter intensity due to variations on the local incidence angle (LIA), (2) to reduce the speckle associated with the SAR signal, and (3) to reduce backscatt” (p. 7, seção 3.2.1. Preprocessing)
- “The objective of the mission was to test the reliability of the warnings on an operational context.” (p. 12, seção 4. Results)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “DETER started issuing alerts in 2004, as part of the Action Plan for the Prevention and Control of Deforestation in the Legal Amazon (PPCDAm), which, coupled with the deployment of law-enforcement teams on the field and the delimitation of ” (p. 2, seção 1. Introduction)
- “After running a prototype of the system from November 2020 to March 2021 over a set of five areas subject to special monitoring by the Brazilian National Institute for Space Research (INPE), the system was made operational, covering the Bra” (p. 3, seção 42 days.)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- Sentinel-1 (radar) como entrada de detecção.
- **Planet Basemaps (NICFI), mosaicos mensais e semestrais** são usados como **imagem óptica de referência** para a validação humana e para os comparativos com o DETER óptico (p. 5–6, figuras com fundo Planet).

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



## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Resultados (resumo do artigo):**

- **88.572 alertas** em 12 meses de operação; validação humana com **menos de 0,2 % da área detectada** correspondendo a falso positivo (p. 1).
- **33.234 alertas** de interesse não detectados pelo DETER óptico no mesmo período, **105.238,5 ha (~5 %) das detecções**; na estação chuvosa a taxa adicional sobe para **8,1 %** (p. 1).

**Trechos numéricos detectados automaticamente (verificar):**
- “If we assume the Major disagreement to represent the misdetections of the DETER-R system, we can conclude that our system has a User’s Accuracy of 99.4%.” (p. 18, seção 5. Discussion)
- “Conversely, DETER-R achieved a poor Producer’s Accuracy (around 50%) when compared to GLAD-S2 (85%).” (p. 18, seção 5. Discussion)
- “Nonetheless, the Producer’s Accuracy for DETER-R is higher than the one obtained by JJFast (23%).” (p. 18, seção 5. Discussion)
- “For instance, they proposed an example of such a process, in which results of the tuned system are comparable to other SAR NRT detection systems, with User’s Accuracy of around 98% and Producer’s Accuracy around 90%.” (p. 18, seção 5. Discussion)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites e observações:**

- **Observações minhas:** (a) a baixa taxa de falsos positivos é medida **sobre o que os analistas revisaram e confirmaram**; não é uma estimativa de omissão; (b) por ser radar C-band, o método tem omissão conhecida em fogo e restos de corte (ver P118); (c) como li o artigo só em parte, não descrevo os parâmetros do algoritmo.

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

- **Classificação (evidência):** sistema operacional (alertas). Sistema do INPE com análise diária e validação humana; 88.572 alertas em 12 meses.
- menções de termos de monitoramento (contagem, não avaliação): Sistema operacional 25 (p. 1, 2, 3, 4, 5); Quase tempo real 19 (p. 1, 2, 3, 17, 18); Alertas 12 (p. 2, 3, 8, 10, 12); Persistência / confirmação 8 (p. 8, 12, 13, 19); Falsos alertas 7 (p. 3, 10, 19)

**Interpretação — O que reaproveitar:**

- **Fluxo operacional** (automático → polígonos → validação humana → agência) e a **métrica de alertas complementares** (o que o óptico não viu) como forma de avaliar valor adicional de um novo detector.
- Uso de **Planet NICFI como fundo de validação visual**.

**Interpretação — Cuidados para o nosso projeto:**

- Não é detector de imagem Planet; conferir os detalhes do algoritmo no PDF antes de citar parâmetros.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Sentinel1|Sentinel-1]] — 10 ocorrências (p. 1, 2, 4, 7, 10)
- referência (curado pela leitura): [[PlanetNICFI|Planet NICFI (basemaps)]] — suporte vindo da leitura/título/resumo
- discute aspecto de monitoramento: [[QuaseTempoReal|Quase tempo real e latência]] — 19 ocorrências (p. 1, 2, 3, 17, 18)
- discute aspecto de monitoramento: [[Alertas|Alertas de mudança]] — 12 ocorrências (p. 2, 3, 8, 10, 12)
- emprega conjunto de dados: [[DETER|DETER (INPE)]] — 108 ocorrências (p. 1, 2, 3, 4, 5)
- trata a tarefa: [[Desmatamento|Desmatamento]] — suporte vindo da leitura/título/resumo

**Comparações substantivas com outros artigos:**
- este artigo é sistema paralelo ao [[Reiche_2021_ForestDisturbanceAlerts|Reiche 2021]] — DETER-R (INPE) e RADD (Wageningen) são alertas por radar Sentinel-1; ambos usam Planet na validação.

## Figuras selecionadas

![[Doblas_2022_DETEROperationalNear_p6_Figure3.png|520]]
*Figure 3. Flowchart depicting the daily operational routine of the DETER-R system. (p. 6; recorte do PDF convertido)*


## Anotações do leitor

- 
