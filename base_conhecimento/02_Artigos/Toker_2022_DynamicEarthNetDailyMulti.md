---
tipo: artigo
id_origem: P12
titulo: "DynamicEarthNet: Daily Multi-Spectral Satellite Dataset for Semantic Change Segmentation"
ano: 2022
autores: ["Aysim Toker", "Lukas Kondmann", "Mark C. Weber", "Marvin Eisenberger", "Andrés Camero", "Jingliang Hu", "Ariadna Pregel Hoderlein", "Çağlar Şenaras"]
doi: "10.48550/arXiv.2203.12560"
arquivo_fonte: "coleta/P12_Toker2022_DynamicEarthNet-Daily-Multi-Spectral-Satellite-Dataset-for-S.pdf"
markdown_fonte: "output/pdf/P12_Toker2022_DynamicEarthNet-Daily-Multi-Spectral-Satellite-Dataset-for-S/document.md"
paginas: 18
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "A"
tarefas: ["[[SITS|Séries temporais de imagens (SITS)]]", "[[MudancaSemantica|Mudança semântica (from–to)]]"]
sensores: ["[[PlanetProdutos|Produtos Planet (visão geral)]]"]
conjuntos_dados: ["[[DynamicEarthNet|DynamicEarthNet]]"]
metodos: ["[[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]]", "[[UTAE|U-TAE (U-Net com atenção temporal)]]", "[[LSTM|Redes recorrentes (LSTM)]]"]
preparo: []
validacao: ["[[Desbalanceamento|Desbalanceamento de classes]]"]
ferramentas: []
tags: [artigo, leitura/profunda, relevancia/A]
---

# Toker 2022 — DynamicEarthNet: Daily Multi-Spectral Satellite Dataset for Semantic Change Segmentation

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **A** — Planet Fusion diário de 3 m com rótulos mensais de mudança semântica (DynamicEarthNet).

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Aysim Toker, Lukas Kondmann, Mark C. Weber, Marvin Eisenberger et al. (2022). DynamicEarthNet: Daily Multi-Spectral Satellite Dataset for Semantic Change Segmentation. IEEE Computer Society Conference on Computer Vision and Pattern Recognition. Tipo no catálogo: Dataset.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2203.12560
- **Arquivo de origem:** `coleta/P12_Toker2022_DynamicEarthNet-Daily-Multi-Spectral-Satellite-Dataset-for-S.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P12_Toker2022_DynamicEarthNet-Daily-Multi-Spectral-Satellite-Dataset-for-S/document.md` — 18 páginas, 15 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Benchmark de **segmentação semântica de mudança** em séries diárias Planet: além do mapa de cobertura de cada mês, avaliar se o modelo acerta *onde* houve mudança e *para qual classe* mudou. Introduz a métrica **SCS**.

**Resumo detectado automaticamente (p. 1):** Earth observation is a fundamental tool for monitoring the evolution of land use in specific areas of interest. Ob- serving and precisely defining change, in this context, re- quires both time-series data and pixel-wise segmentations. To that end, we propose the DynamicEarthNet dataset that consists of daily, multi-spectral satellite observations of 75 selected areas of interest distributed over the globe with im- agery from Planet Labs. These observations are paired with pixel-wise monthly semantic segmentation labels of 7 land use and land cover (LULC) classes. DynamicEarthNet is the first dataset that provides this unique combination of daily measurements and high-quality labels. In our experi- ments, we compare several established baselines that either utilize the daily observations as additional training data (semi-supervised learning) or multiple observations at once (spatio-tempor…

- “To that end, we propose the DynamicEarthNet dataset that consists of daily, multi-spectral satellite observations of 75 selected areas of interest distributed over the globe with im- agery from Planet Labs.” (p. 1, seção Abstract)
- “In our experi- ments, we compare several established baselines that either utilize the daily observations as additional training data (semi-supervised learning) or multiple observations at once (spatio-temporal learning) as a point of refer” (p. 1, seção Abstract)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The dataset comprises consistent, occlusion-free daily observations with multi-spectral imagery over the span of two years (2018-2019).” (p. 2, seção 1. Introduction)
- “The DynamicEarthNet dataset We present the DynamicEarthNet dataset that contains daily, cloud-free satellite data acquired from January 2018 to December 2019.” (p. 3, seção 2.2. Considered tasks)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- 75 áreas, jan/2018–dez/2019; **Planet Fusion** (produto diário gap-filled, 4 bandas RGB+NIR, 3 m, 1024 × 1024, calibrado ao espectro HLS); 730 imagens por área, 54.750 no total; Sentinel-2 mensal auxiliar para comparação (p. 4).
- Importante: **Planet Fusion não é o mosaico mensal convencional.** Radiometria e cadência diferem.

**Detectado automaticamente (verificar):**
- sensor/produto **Planet (mosaicos e cenas)**: 5 ocorrências (p. 1, 3, 4)
- sensor/produto **Sentinel-2**: 3 ocorrências (p. 2, 4)
- sensor/produto **Landsat**: 2 ocorrências (p. 4)
- conjunto de dados **DynamicEarthNet**: 17 ocorrências (p. 1, 2, 3, 4, 5)
- conjunto de dados **SpaceNet 7 (MUDS)**: 3 ocorrências (p. 2, 3, 8)
- conjunto de dados **HRSCD**: 3 ocorrências (p. 2, 3)
- conjunto de dados **DeepGlobe**: 2 ocorrências (p. 2, 3)
- “The DynamicEarthNet dataset contains 75 different AOIs across the globe, each of which consists of a sequence of 730 images covering two years from January 2018 to December 2019.” (p. 4, seção 3.3. Dataset statistics)
- “On the other hand, when using daily sequences of 28-31 images, the performance drops considerably.” (p. 6, seção 5.2. Land cover and land use segmentation)
- “The input sequence consists of 5 images (middle row) from September to October, spanning one month.” (p. 8, seção 5.3. Semantic change segmentation)
- “The first image was manually annotated for each AOI and used as a basis for the following months.” (p. 4, seção 2 https://earthdata.nasa.gov/esds/harmonized-landsat-sentine)
- “As an alternative to modeling the input images as sequences, we can interpret them as an unordered collection of training samples.” (p. 6, seção 5.1. Baselines)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Evidência (leitura) — Rótulos:**

- Mapas pixel a pixel no dia 1 de cada mês (24 por área, 1.800 no total), com 7 classes: superfície impermeável 7,1 %, agricultura 10,3 %, floresta e outra vegetação 44,9 %, áreas úmidas 0,7 %, solo 28,0 %, água 8,0 %, neve/gelo 1,0 % (descartada na avaliação por aparecer em 2 cubos) (p. 3, 4).
- Protocolo: **primeira imagem anotada manualmente e depois atualizada** só quando a mudança é evidente ao anotador; três portões de qualidade com anotadores diferentes (exatidão, topologia, formato) (p. 4).
- Só ~5 % dos pixels mudam de um mês para o outro (p. 5).

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 39 ocorrências (p. 1, 2, 3, 4, 5)
- **Recorte em patches/tiles**: 4 ocorrências (p. 2, 4, 6)
- **Máscara de nuvem e sombra**: 2 ocorrências (p. 3, 4)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 37 menções vs 8 de pares)
**Métodos detectados automaticamente:**
- método/família **U-Net**: 9 ocorrências (p. 6, 7)
- método/família **Semi/auto-supervisionado**: 9 ocorrências (p. 1, 6, 7, 8)
- método/família **LSTM / recorrente**: 5 ocorrências (p. 6, 7)
- método/família **U-TAE**: 5 ocorrências (p. 6, 7)
**Hiperparâmetros detectados automaticamente (verificar):**
- tamanho do patch: “1024x1024 with a pixel” (p. 4)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Evidência (leitura) — Divisão e métrica:**

- Treino/validação/teste: 55 / 10 / 10 áreas, balanceando classes; o teste é oculto (p. 4).
- **SCS = média(BC, SC):** BC é o IoU binário da máscara de mudança; SC é o IoU médio das classes **apenas nos pixels que realmente mudam**. Acumula as matrizes de confusão da série antes de calcular (p. 5).

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 13 ocorrências (p. 4, 5, 6, 7, 8)
- **Desbalanceamento**: 3 ocorrências (p. 3, 4, 5)
- métrica **IoU**: 15 ocorrências (p. 5, 6, 7, 8)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Baselines e resultados:**

- U-Net mensal; U-TAE, U-ConvLSTM e 3D-UNet com entradas semanais ou diárias; método semissupervisionado CAC (Lai et al.) com DeepLabv3+ (p. 6).
- mIoU de cobertura (val/teste): U-Net 33,5/37,6; U-TAE semanal 35,7/39,7; U-TAE diário 32,2/36,1; CAC diário 43,6 no teste (p. 6, 7).
- Mudança semântica (teste): SCS 17,3–19,1 e BC ≈ 10 %; U-TAE semanal 19,1 é o melhor SCS (p. 7).
- Agricultura e áreas úmidas são as classes mais difíceis (confusão com floresta e solo; áreas úmidas com IoU 0) (p. 7).
- Observações diárias são altamente correlacionadas: o ótimo para os baselines é **semanal**; sequências diárias desestabilizam o treino (p. 6, 7).
- mIoU alto não garante SCS alto (p. 7, 8).

**Trechos numéricos detectados automaticamente (verificar):**
- “It achieves 33.5% mIoU on the validation and 37.6% mIoU on the test set.” (p. 6, seção 5.2. Land cover and land use segmentation)
- “The obtained accuracy is 43.6% mIoU on the test set, with a considerable improvement over the monthly and weekly results of 37.9%.” (p. 7, seção 5.2. Land cover and land use segmentation)
- “Considering that the ground-truth change maps cover only 5% of all pixels on average, there exist a high number of potential false positives.” (p. 7, seção 5.3. Semantic change segmentation)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites e cuidados:**

- Produto Planet Fusion (diário, calibrado): não equivale ao mosaico mensal; testar transferência separadamente.
- Poucos exemplos de mudança (5 %/mês) e teste oculto; BC próximo de 10 % mostra que a deteção de mudança continua em aberto.

**Trechos detectados automaticamente (verificar contexto):**
- “Existing datasets often fail to provide these conditions.” (p. 1, seção 1. Introduction)
- “On the other hand, in certain areas, it is not able to distinguish between the generic forest & vegetation class and the ground-truth label agriculture.” (p. 8, seção 5.3. Semantic change segmentation)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 1)
- declaração: “The data is available [at: https://mediatum.ub.tum.de/1650201.](https://mediatum.ub.tum.de/1650201) Making peace with nature is the defining task of the 21st century.” (p. 1)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo. Benchmark com rótulos mensais; não mede latência nem falsos alertas.
- menções de termos de monitoramento (contagem, não avaliação): Latência / frequência 20 (p. 1, 2, 3, 5, 6); Persistência / confirmação 1 (p. 4)

**Interpretação — O que reaproveitar:**

- **Taxonomia de 6–7 classes** como ponto de partida para from–to: impermeável, agricultura, floresta/vegetação, áreas úmidas, solo, água.
- **SCS** para avaliar transições (BC + SC) em E10 Avaliação e incerteza; reportar sempre junto com mIoU de cobertura.
- **Protocolo de rotulagem com consistência temporal** (rótulo inicial manual + atualizações só quando há evidência; três portões de QC).
- **Subamostragem temporal:** nossa entrada mensal evita o problema de redundância diária, mas o resultado sugere testar 3–6 meses por janela.
- **Divisão por área** (não por patch) e distribuição de classes balanceada entre divisões.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[PlanetProdutos|Produtos Planet (visão geral)]] — 5 ocorrências (p. 1, 3, 4)
- emprega conjunto de dados: [[DynamicEarthNet|DynamicEarthNet]] — 17 ocorrências (p. 1, 2, 3, 4, 5)
- trata a tarefa: [[SITS|Séries temporais de imagens (SITS)]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[MudancaSemantica|Mudança semântica (from–to)]] — suporte vindo da leitura/título/resumo
- utiliza método: [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 9 ocorrências (p. 1, 6, 7, 8)
- utiliza método: [[UTAE|U-TAE (U-Net com atenção temporal)]] — 5 ocorrências (p. 6, 7)
- utiliza método: [[LSTM|Redes recorrentes (LSTM)]] — 5 ocorrências (p. 6, 7)
- referencia (suporte manual da leitura): [[MetricasMudancaSemantica|Métricas de mudança semântica (SeK, SCS, SCOT)]] — suporte vindo da leitura/título/resumo
- referencia (suporte manual da leitura): [[RotulagemTemporal|Rotulagem temporalmente consistente]] — suporte vindo da leitura/título/resumo
- referencia (suporte manual da leitura): [[DivisaoEspacialBlocos|Divisão espacial por blocos e áreas]] — suporte vindo da leitura/título/resumo
- adota desenho de validação: [[Desbalanceamento|Desbalanceamento de classes]] — 3 ocorrências (p. 3, 4, 5)

**Comparações substantivas com outros artigos:**
- [[Vincent_2024_SatelliteImageTime|Vincent 2024]] emprega o conjunto de dados e a métrica de este artigo — P13 treina e testa em DynamicEarthNet e usa as métricas BC, SC, SCS e mIoU definidas por P12 (p. 6).
- este artigo compara-se, na descrição do dataset, com [[Etten_2021_MultiTemporalUrban|Etten 2021]] — P12 cita o MUDS como o dataset temporal mais próximo: (p. 2).

## Figuras selecionadas

![[Toker_2022_DynamicEarthNetDailyMulti_p4_Figure2.png|520]]
*Figure 2. An example of a changing surface. We show four sample frames of one AOI from our dataset at different times. Two subregions are ma (p. 4; recorte do PDF convertido)*

![[Toker_2022_DynamicEarthNetDailyMulti_p1_Figure1.png|520]]
*Figure 1. Visualization of the DynamicEarthNet dataset. For a specific area of interest, we show two satellite observations, 2019-08-01 (p. 1; recorte do PDF convertido)*

![[Toker_2022_DynamicEarthNetDailyMulti_p8_Figure3.png|520]]
*Figure 3. Qualitative results on validation set. Semantic maps (bottom row) of the semi-supervised baseline CAC trained on (p. 8; recorte do PDF convertido)*


## Anotações do leitor

- 
