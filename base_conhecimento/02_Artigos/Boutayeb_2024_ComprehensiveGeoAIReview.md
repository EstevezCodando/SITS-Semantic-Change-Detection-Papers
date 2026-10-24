---
tipo: artigo
id_origem: P171
titulo: "A comprehensive GeoAI review: Progress, Challenges and Outlooks"
ano: 2024
autores: ["Anasse Boutayeb", "Iyad Lahsen-Cherif", "Ahmed El Khadimi"]
doi: "10.48550/arXiv.2412.11643"
arquivo_fonte: "coleta/P171_Boutayeb2024_A-comprehensive-GeoAI-review-Progress-Challenges-and-Outlook.pdf"
markdown_fonte: "output/pdf/P171_Boutayeb2024_A-comprehensive-GeoAI-review-Progress-Challenges-and-Outlook/document.md"
paginas: 50
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: []
sensores: ["[[UAV|UAV / drones]]", "[[SAR|Radar (SAR)]]", "[[Landsat|Landsat]]"]
conjuntos_dados: ["[[OpenStreetMap|OpenStreetMap]]", "[[xBD|xBD]]"]
metodos: ["[[CNN|Redes convolucionais (CNN)]]", "[[LSTM|Redes recorrentes (LSTM)]]", "[[RandomForest|Random Forest]]", "[[UNet|U-Net]]", "[[XGBoost|XGBoost]]", "[[SVM|SVM]]"]
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]", "[[Rotulagem|Rotulagem e anotação]]", "[[IndicesEspectrais|Índices espectrais (NDVI etc.)]]", "[[Normalizacao|Normalização e escala radiométrica]]", "[[Corregistro|Corregistro e georreferenciamento]]"]
validacao: ["[[ValidacaoCruzada|Validação cruzada]]", "[[PrecisaoRecall|Precisão e recall]]", "[[F1|F1]]", "[[AcuraciaGlobal|Acurácia global (OA)]]", "[[mAP|mAP]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Boutayeb 2024 — A comprehensive GeoAI review: Progress, Challenges and Outlooks

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Anasse Boutayeb, Iyad Lahsen-Cherif, Ahmed El Khadimi (2024). A comprehensive GeoAI review: Progress, Challenges and Outlooks. arXiv (Cornell University). Tipo no catálogo: Revisão.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2412.11643
- **Arquivo de origem:** `coleta/P171_Boutayeb2024_A-comprehensive-GeoAI-review-Progress-Challenges-and-Outlook.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P171_Boutayeb2024_A-comprehensive-GeoAI-review-Progress-Challenges-and-Outlook/document.md` — 50 páginas, 52 recortes de figuras, 1 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “According to Gao , GeoAI can be regarded as : # “ a branch of AI whose objective is to implement intelligent computer programs aiming to imitate human perception, particularly with regard to spatial reasoning and geographical dynamics. # ” ” (p. 2, seção 1 Introduction)
- “Furthermore, and to situate the aim of this work in relation to previous works, a great deal of research is carried out on this subject, as shown in Table 1, while touching on different sub-branches of geospatial field, but without giving a” (p. 2, seção 1 Introduction)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “Apart from satellite imagery, several studies explored the importance of high-resolution UAV imagery, for more accurate crop mapping, particularly in small-scale study areas.” (p. 17, seção 4 GeoAI applications)
- “Figure 15: Explanations of the difference between DSM and DTM by horizontal view (a) and by raster view (b) . - Copernicus DEM : contains digital surface models (DSMs) from TanDEM-X satellite between 2011 and 2015 .” (p. 12, seção 30 land use classes, and publicly available in .)
- “Using 3 raster maps with dates of 2000, 2010 and 2020, the tests have showed significant effectiveness for the classification task in question.” (p. 19, seção 0.01 and an R of 85%. Hajjar et al. proposed an LSTM)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **UAV**: 24 ocorrências (p. 1, 11, 12, 13, 17)
- sensor/produto **SAR**: 15 ocorrências (p. 12, 13, 16, 17, 28)
- sensor/produto **Landsat**: 13 ocorrências (p. 11, 17, 18, 19, 21)
- sensor/produto **Imagens aéreas**: 10 ocorrências (p. 11, 12, 18, 21, 27)
- conjunto de dados **OpenStreetMap**: 6 ocorrências (p. 13, 14, 15, 20, 21)
- conjunto de dados **xBD**: 3 ocorrências (p. 12, 27)
- resolução mencionada: 0.5 m (p. 11)
- resolução mencionada: 2 m (p. 11)
- resolução mencionada: 1 m (p. 11)
- “AID dataset contains 10,000 images of 0.5m to 2m resolution belonging to” (p. 11, seção 4 provides detailed informations on each dataset.)
- “Table 4: xView datasets. |References|Dataset|Task|Images<br>number|Annotations<br>number|Classes<br>number|Imagessource| |---|---|---|---|---|---|---| ||xView-1|Detection of several object classes.|1127|One Million|60|WorldView-3 30 cm imag” (p. 12, seção 30 land use classes, and publicly available in .)
- “This dataset, comprising 21 land use classes such as buildings, airports and parking lots, and totalling 2100 images , is used for training and benchmarking classification models, and it is accessed via Kaggle platform . - UAVid : is a UAV ” (p. 12, seção 30 land use classes, and publicly available in .)
- “More specifically, AI is a key tool allowing the management and exploitation of geospatial data, paving the way for a new era of analysis and interpretation, particularly when it comes to massive and complex data, or when it comes to sophis” (p. 1, seção 1 Introduction)
- “GeoAI generation geospatial|Present the close and the domain. between relationship deep very quickly learning geospatial|DiscoverthephilosophicalfoundationsoftheGeoAIwhilehighlightingfundamentalissuessuchasthelack of ethical of the and its ” (p. 4, seção 1 Introduction)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 21 ocorrências (p. 1, 8, 14, 16, 17)
- **Rotulagem / anotação**: 17 ocorrências (p. 3, 6, 9, 10, 11)
- **Índices espectrais**: 14 ocorrências (p. 18, 22, 24, 25, 28)
- **Normalização / escala**: 10 ocorrências (p. 2, 8, 9, 10, 25)
- **Corregistro / georreferenciamento**: 3 ocorrências (p. 12, 20)
- **Aumento de dados**: 2 ocorrências (p. 18, 28)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 19 menções vs 1 de pares)
**Métodos detectados automaticamente:**
- método/família **CNN**: 35 ocorrências (p. 6, 7, 16, 17, 18)
- método/família **LSTM / recorrente**: 29 ocorrências (p. 7, 20, 21, 22, 23)
- método/família **Random Forest**: 29 ocorrências (p. 5, 17, 18, 20, 22)
- método/família **U-Net**: 21 ocorrências (p. 6, 17, 18, 19, 20)
- método/família **XGBoost**: 15 ocorrências (p. 6, 18, 22, 23, 24)
- método/família **SVM**: 15 ocorrências (p. 5, 18, 20, 24, 25)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Validação cruzada**: 3 ocorrências (p. 26, 28)
- **Desbalanceamento**: 2 ocorrências (p. 8, 10)
- métrica **Precisão/Recall**: 58 ocorrências (p. 1, 2, 9, 10, 13)
- métrica **F1**: 19 ocorrências (p. 10, 17, 18, 19, 21)
- métrica **Acurácia global**: 12 ocorrências (p. 17, 19, 21, 22, 23)
- métrica **IoU**: 7 ocorrências (p. 10)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “Note: It is very common to use the mAP50 metric, measuring the mAP value for an IoU threshold of 50%, since it offers a compromise between high object location accuracy and error tolerances of this location.” (p. 10, seção 1 Introduction)
- “meters only on the European continent for EEA-10 products, with a good altimetric accuracy Linear error 90% (LE90) of 4m.” (p. 12, seção 30 meters for GLO-90 products, as well as a resolu)
- “The reasonable size of these data in memory and the possibility of extracting them from several sources, including images and maps, encourage users to employ them in various applications, among which vector geospatial datasets: 14 - Microsoft Global Building F” (p. 14, seção 30 meters for GLO-90 products, as well as a resolu)
- “Overall Accuracy (OA) and F1-Score metrics are used during the evaluation phase, obtaining average values across all classes of 96% and 74% respectively.” (p. 17, seção 4 GeoAI applications)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “GeoAI generation geospatial|Present the close and the domain. between relationship deep very quickly learning geospatial|DiscoverthephilosophicalfoundationsoftheGeoAIwhilehighlightingfundamentalissuessuchasthelack of ethical of the and its ” (p. 4, seção 1 Introduction)
- “Explore Discover of Present Discover of Exploring of Determine Provide its Discover cations GeoAI and on and (2020) of Thirteenth Com- Data Peo- Technology Electronics, Informa- Wuhan Applications Geography Intelligence Engineering Protec- ” (p. 4, seção 1 Introduction)
- “For example, Abu Talib et al. provided a systematic review comparing the performance of a multitude hardware accelerators when running DNNs, especially FPGA, GPU and ASIC, and concluded that FGPAs provide a high reconfiguration capacity, de” (p. 16, seção 30 meters for GLO-90 products, as well as a resolution of 10)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Quase tempo real 9 (p. 15, 16, 17, 26, 28); Custo 7 (p. 6, 8, 14, 24, 32); Alertas 2 (p. 15, 32); Sistema operacional 1 (p. 15); Latência / frequência 1 (p. 29)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[UAV|UAV / drones]] — 24 ocorrências (p. 1, 11, 12, 13, 17)
- utiliza dado/sensor: [[SAR|Radar (SAR)]] — 15 ocorrências (p. 12, 13, 16, 17, 28)
- utiliza dado/sensor: [[Landsat|Landsat]] — 13 ocorrências (p. 11, 17, 18, 19, 21)
- emprega conjunto de dados: [[OpenStreetMap|OpenStreetMap]] — 6 ocorrências (p. 13, 14, 15, 20, 21)
- emprega conjunto de dados: [[xBD|xBD]] — 3 ocorrências (p. 12, 27)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 35 ocorrências (p. 6, 7, 16, 17, 18)
- utiliza método: [[LSTM|Redes recorrentes (LSTM)]] — 29 ocorrências (p. 7, 20, 21, 22, 23)
- utiliza método: [[RandomForest|Random Forest]] — 29 ocorrências (p. 5, 17, 18, 20, 22)
- utiliza método: [[UNet|U-Net]] — 21 ocorrências (p. 6, 17, 18, 19, 20)
- utiliza método: [[XGBoost|XGBoost]] — 15 ocorrências (p. 6, 18, 22, 23, 24)
- utiliza método: [[SVM|SVM]] — 15 ocorrências (p. 5, 18, 20, 24, 25)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 58 ocorrências (p. 1, 2, 9, 10, 13)
- é avaliado por: [[F1|F1]] — 19 ocorrências (p. 10, 17, 18, 19, 21)
- é avaliado por: [[AcuraciaGlobal|Acurácia global (OA)]] — 12 ocorrências (p. 17, 19, 21, 22, 23)
- é avaliado por: [[mAP|mAP]] — 6 ocorrências (p. 10, 20, 21, 30)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 21 ocorrências (p. 1, 8, 14, 16, 17)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 17 ocorrências (p. 3, 6, 9, 10, 11)
- aplica etapa de preparo: [[IndicesEspectrais|Índices espectrais (NDVI etc.)]] — 14 ocorrências (p. 18, 22, 24, 25, 28)
- aplica etapa de preparo: [[Normalizacao|Normalização e escala radiométrica]] — 10 ocorrências (p. 2, 8, 9, 10, 25)
- aplica etapa de preparo: [[Corregistro|Corregistro e georreferenciamento]] — 3 ocorrências (p. 12, 20)
- adota desenho de validação: [[ValidacaoCruzada|Validação cruzada]] — 3 ocorrências (p. 26, 28)
- discute aspecto de monitoramento: [[QuaseTempoReal|Quase tempo real e latência]] — 9 ocorrências (p. 15, 16, 17, 26, 28)

## Anotações do leitor

- 
