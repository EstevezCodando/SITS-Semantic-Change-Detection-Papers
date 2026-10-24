---
tipo: artigo
id_origem: P127
titulo: "Deep Learning for Satellite Image Time-Series Analysis: A review"
ano: 2024
autores: ["Lynn Miller", "Charlotte Pelletier", "Geoffrey I. Webb"]
doi: "10.1109/mgrs.2024.3393010"
arquivo_fonte: "coleta/P127_Miller2024_Deep-Learning-for-Satellite-Image-Time-Series-Analysis-A-rev.pdf"
markdown_fonte: "output/pdf/P127_Miller2024_Deep-Learning-for-Satellite-Image-Time-Series-Analysis-A-rev/document.md"
paginas: 38
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (parcial)"
relevancia_objetivo: "C"
tarefas: ["[[SITS|Séries temporais de imagens (SITS)]]", "[[Deteccao_Mudanca|Detecção de mudanças]]"]
sensores: ["[[Sentinel2|Sentinel-2]]", "[[PlanetScope|PlanetScope (Dove/SuperDove)]]"]
conjuntos_dados: []
metodos: ["[[CNN|Redes convolucionais (CNN)]]", "[[LSTM|Redes recorrentes (LSTM)]]", "[[Transformer|Transformers]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/parcial, relevancia/C]
---

# Miller 2024 — Deep Learning for Satellite Image Time-Series Analysis: A review

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (parcial). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **C** — Revisão de aprendizado profundo em séries temporais (leitura parcial).

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Lynn Miller, Charlotte Pelletier, Geoffrey I. Webb (2024). Deep Learning for Satellite Image Time-Series Analysis: A review. IEEE Geoscience and Remote Sensing Magazine. Tipo no catálogo: Revisão.
- **DOI/URL:** https://doi.org/10.1109/mgrs.2024.3393010
- **Arquivo de origem:** `coleta/P127_Miller2024_Deep-Learning-for-Satellite-Image-Time-Series-Analysis-A-rev.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P127_Miller2024_Deep-Learning-for-Satellite-Image-Time-Series-Analysis-A-rev/document.md` — 38 páginas, 9 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Revisão de **aprendizado profundo aplicado a séries temporais de imagens de satélite (SITS)** para estimar variáveis de observação da Terra (classificação e regressão), com resumo das arquiteturas (RNN, CNN 1D, 3D-CNN, híbridas) e dos tipos de tarefa (p. 1–2). Não é focada em detecção de mudança.

- “The purpose of this data separation is to help ensure reported accuracy is not biased and thus is a reliable measure of the model performance on unseen datasets .” (p. 7, seção 61 and time between acquisitions is uneven. Its multimodal)
- “The objective of land cover mapping is to identify the type of vegetative (e.g., forest, shrubland, grassland, or agricultural uses) or non-vegetative (e.g., bare land, water bodies, urban area) land cover at each point, to generate maps th” (p. 8, seção 61 and time between acquisitions is uneven. Its multimodal)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “While these studies have produced important results for specific applications, the differences in the study regions make it difficult to compare the advantages and disadvantages of the various algorithms.” (p. 5, seção 3. After implementation of the Take-5 experiment .)
- “It includes data collected for 2018 and 2019 from Sentinel-1, Sentinel-2, and Planet Fusion for two tiles located in Northern Germany.” (p. 6, seção 3. After implementation of the Take-5 experiment .)
- “A total of nine satellites were launched between 1972 and 2021, three of which are still” (p. 3, seção Início)
- “The [Satellite Image Time Series Datasets GitHub repository](https://github.com/corentin-dfg/Satellite-Image-Time-Series-Datasets) lists about 50 SITS datasets, collected between 2017 and 2023.” (p. 5, seção 3. After implementation of the Take-5 experiment .)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- Tabela de sensores inclui a constelação **Planet (≈ 200 satélites "Flock", 3,7 m, diária, 4 bandas VIS/IR)**; a revisão cita bancos de dados que juntam **Planet Fusion** e Sentinel-2 e um conjunto de imagens diárias do Planet com mensais do Sentinel-2 (p. 4–5 e trechos de conjuntos de dados, linhas sobre Planet Fusion).

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-2**: 38 ocorrências (p. 2, 3, 4, 5, 6)
- sensor/produto **Landsat**: 27 ocorrências (p. 1, 2, 3, 4, 5)
- sensor/produto **SAR**: 26 ocorrências (p. 1, 4, 5, 9, 11)
- sensor/produto **Sentinel-1**: 25 ocorrências (p. 5, 6, 7, 9, 11)
- resolução mencionada: 30 m (p. 4)
- resolução mencionada: 15 m (p. 4)
- “The BreizhCrops database contains one-year time series of Sentinel-2 images for Brittany, France for both 2017 and 2018.” (p. 5, seção 3. After implementation of the Take-5 experiment .)
- “The time series are of varying lengths, with European Union’s Horizon 2020 (H2020) program to enable either 51 or 102 images for the top-of-atmosphere time series the development of land cover products providing higher levels and an average” (p. 6, seção 3. After implementation of the Take-5 experiment .)
- “TimeSen2Crop is a pixel-based dataset of Sentinel-2 time series for the classification of sixteen crop types in Austria.” (p. 6, seção 3. After implementation of the Take-5 experiment .)
- “EuroCrops is a reference dataset for crop classification covering 16 European Union countries.” (p. 6, seção 61 and time between acquisitions is uneven. Its multimodal)
- “In addition to the reference data, the curators have made available the TinyEuroCrops dataset that contains Sentinel-2 time series for regions in Austria, Denmark, and Slovenia .” (p. 6, seção 61 and time between acquisitions is uneven. Its multimodal)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 87 ocorrências (p. 1, 3, 6, 8, 11)
- **Rotulagem / anotação**: 48 ocorrências (p. 1, 5, 6, 18, 20)
- **Índices espectrais**: 21 ocorrências (p. 5, 7, 9, 16, 17)
- **Normalização / escala**: 14 ocorrências (p. 6, 7, 8, 9, 14)
- **Segmentação em objetos**: 4 ocorrências (p. 19, 20)
- **Máscara de nuvem e sombra**: 3 ocorrências (p. 6, 7, 11)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Seção de detecção de mudança (p. 15–16):**

- Métodos que usam **séries curtas** em vez de dois instantes: Papadomanolaki et al. (U-Net + LSTM multitarefa; SITS **superou claramente** o bitemporal nos conjuntos testados); **UTRNet** (não supervisionado, inclui o intervalo de tempo para tratar séries irregulares e reduzir "pseudomudanças" sazonais; pseudo-rótulos para escolher amostras balanceadas); Saha et al. (detecção de anomalia por reordenação das imagens com LSTM); Li et al. (mudança em edificações em resolução média, com Inception + LSTM) (p. 15).
- Poucos métodos dizem **quando** a mudança ocorreu: Chen et al. (pseudorrótulos entre pares, aprendizado contrastivo e rastreio de feições, melhor supressão de ruído sazonal que o UTRNet) (p. 15–16).

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 463 menções vs 7 de pares)
**Métodos detectados automaticamente:**
- método/família **CNN**: 111 ocorrências (p. 2, 3, 10, 11, 12)
- método/família **LSTM / recorrente**: 87 ocorrências (p. 10, 11, 12, 13, 14)
- método/família **Transformer**: 31 ocorrências (p. 7, 11, 13, 15, 16)
- método/família **U-Net**: 24 ocorrências (p. 13, 14, 17, 19, 20)
- método/família **Semi/auto-supervisionado**: 20 ocorrências (p. 1, 20, 21, 22, 23)
- método/família **OBIA**: 14 ocorrências (p. 2, 15, 17, 18, 19)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Divisão temporal**: 4 ocorrências (p. 22)
- **Teste externo / generalização**: 3 ocorrências (p. 22, 27)
- **Validação cruzada**: 2 ocorrências (p. 7)
- **Conjuntos treino/val/teste**: 2 ocorrências (p. 6, 7)
- **Amostragem estratificada**: 2 ocorrências (p. 7)
- métrica **Estimativa de área**: 3 ocorrências (p. 7, 14)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Desafios e conclusões (p. 26–28):**

- **Custo computacional** (1,5 trilhão de pixels para cobrir a terra a 10 m), **escassez de rótulos** e **adaptação de domínio entre continentes** (mudanças sazonais, vegetação e manejo diferentes) (p. 26–27).
- Conclusão: o aprendizado profundo em SITS é eficaz e supera outras técnicas de aprendizado de máquina; RNN e CNN 1D para o tempo e 3D-CNN e híbridas para o espaço-tempo (p. 27).


## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites e observações:**

- **Observações minhas:** (a) li só as partes que tocam o nosso objetivo; (b) os números de comparação entre as arquiteturas não foram verificados; (c) a revisão cobre os trabalhos até ~2023, antes dos modelos fundacionais temporais e do Mamba.

**Trechos detectados automaticamente (verificar contexto):**
- “However, models using NTL do not perform well in impoverished areas and cannot distinguish between wealthy sparsely populated regions and poor densely populated areas .” (p. 9, seção 61 and time between acquisitions is uneven. Its multimodal)
- “Several authors have claimed either that CNNs cannot learn temporal features , , , , or that RNNs outperform CNNs for land cover and crop type classification .” (p. 12, seção 61 and time between acquisitions is uneven. Its multimodal)
- “Various architectures that combine recurrent and convolutional layers into one hybrid model have been proposed to overcome this limitation (Table 5).” (p. 13, seção 61 and time between acquisitions is uneven. Its multimodal)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/corentin-dfg/Satellite-Image-Time-Series-Datasets (p. 5)
- URL citada: https://github.com/corentin-dfg/Satellite-Image-Time-Series-Datasets (p. 5)
- declaração: “More recently introduced in the literature, self-supervised When data are available for only some geographical areas and learning methods are generally divided into three categories: times, domain adaptation techniques address the problem o” (p. 21)
- declaração: “Approaches tailored for SITS have mainly focused on the unsupervised domain adaptation setting, where no target labeled data is available.” (p. 22)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Latência / frequência 5 (p. 3, 4, 24); Sistema operacional 2 (p. 9, 12); Persistência / confirmação 1 (p. 25); Custo 1 (p. 3)

**Interpretação — O que reaproveitar:**

- **Vocabulário e taxonomia** de modelos temporais e a distinção entre detecção "se mudou" e "quando mudou".
- **Argumento de que séries superam pares de datas** (Papadomanolaki) e de que considerar o **intervalo entre datas** reduz pseudomudança sazonal (UTRNet).
- **Lista de datasets de SITS** para localizar bases com Planet Fusion.

**Interpretação — Cuidados para o nosso projeto:**

- Não substitui a leitura dos artigos específicos; usar como mapa.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- trata a tarefa: [[SITS|Séries temporais de imagens (SITS)]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 111 ocorrências (p. 2, 3, 10, 11, 12)
- utiliza método: [[LSTM|Redes recorrentes (LSTM)]] — 87 ocorrências (p. 10, 11, 12, 13, 14)
- utiliza método: [[Transformer|Transformers]] — 31 ocorrências (p. 7, 11, 13, 15, 16)
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 38 ocorrências (p. 2, 3, 4, 5, 6)
- referência (curado pela leitura): [[PlanetScope|PlanetScope (Dove/SuperDove)]] — suporte vindo da leitura/título/resumo

## Figuras selecionadas

![[Miller_2024_DeepLearningSatellite_p19_FIGURE8.png|520]]
*FIGURE 8: A U-Net architecture. Image credit: A Novel (p. 19; recorte do PDF convertido)*

![[Miller_2024_DeepLearningSatellite_p10_FIGURE2.png|520]]
*FIGURE 2: An example of a recurrent neural network. At each (p. 10; recorte do PDF convertido)*

![[Miller_2024_DeepLearningSatellite_p10_FIGURE1.png|520]]
*FIGURE 1: Neural Networks and Activation Functions. (a) A (p. 10; recorte do PDF convertido)*


## Anotações do leitor

- 
