---
tipo: artigo
id_origem: P17
titulo: "Urban Change Forecasting from Satellite Images"
ano: 2023
autores: ["Nando Metzger", "Mehmet Özgür Türkoglu", "Rodrigo Caye Daudt", "Jan Dirk Wegner", "Konrad Schindler"]
doi: "10.1007/s41064-023-00258-8"
arquivo_fonte: "coleta/P17_Metzger2023_Urban-Change-Forecasting-from-Satellite-Images.pdf"
markdown_fonte: "output/pdf/P17_Metzger2023_Urban-Change-Forecasting-from-Satellite-Images/document.md"
paginas: 10
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "A"
tarefas: ["[[Edificacoes|Edificações e urbanização]]", "[[Deteccao_Mudanca|Detecção de mudanças]]"]
sensores: ["[[PlanetProdutos|Produtos Planet (visão geral)]]"]
conjuntos_dados: ["[[SpaceNet7_MUDS|SpaceNet 7 / MUDS]]"]
metodos: ["[[UNet|U-Net]]", "[[RedeSiamesa|Redes siamesas]]", "[[TransferLearning|Aprendizado por transferência]]"]
preparo: []
validacao: ["[[Desbalanceamento|Desbalanceamento de classes]]", "[[F1|F1]]"]
ferramentas: []
tags: [artigo, leitura/profunda, relevancia/A]
---

# Metzger 2023 — Urban Change Forecasting from Satellite Images

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **A** — Previsão de construção no SpaceNet 7 (Planet de 4 m) com pré-treino em detecção de mudança.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Nando Metzger, Mehmet Özgür Türkoglu, Rodrigo Caye Daudt, Jan Dirk Wegner et al. (2023). Urban Change Forecasting from Satellite Images. PFG – Journal of Photogrammetry Remote Sensing and Geoinformation Science. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1007/s41064-023-00258-8
- **Arquivo de origem:** `coleta/P17_Metzger2023_Urban-Change-Forecasting-from-Satellite-Images.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P17_Metzger2023_Urban-Change-Forecasting-from-Satellite-Images/document.md` — 10 páginas, 21 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

**Prever onde e quando surgirão novas edificações** a partir de **uma única imagem anterior à construção** (previsão de mudança), com uma U-Net pré-treinada em detecção de mudança, no **SpaceNet 7** (Planet 4 m, 960 km², 24 meses) (p. 1–2). É diferente da detecção; mas o desenho de dados, o desbalanceamento e o pré-treino interessam à detecção de início de construção.

**Resumo detectado automaticamente (p. 1):** Forecasting where and when new buildings will emerge is a rather unexplored topic, but one that is very useful in many disciplines such as urban planning, agriculture, resource management, and even autonomous flying. In the present work, we present a method that accomplishes this task with a deep neural network and a custom pretraining procedure. In Stage 1, a U-Net backbone is pretrained within a Siamese network architecture that aims to solve a (building) change detection task. In Stage 2, the backbone is repurposed to forecast the emergence of new buildings based solely on one image acquired before its construction. Furthermore, we also present a model that forecasts the time range within which the change will occur. We validate our approach using the SpaceNet7 dataset, which covers an area of 960 km at 24 points in time across 2 years. In our experiments, we found that our proposed p…

- “In the present work, we present a method that accomplishes this task with a deep neural network and a custom pretraining procedure.” (p. 1, seção Abstract)
- “We develop a 2-stage training strategy (as shown in Fig.” (p. 1, seção 60 locations with a total extent of 960 km and a ground)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “We validate our approach using the SpaceNet7 dataset, which covers an area of 960 km at 24 points in time across 2 years.” (p. 1, seção Abstract)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- **SpaceNet 7:** 60 locais rotulados, 24 mosaicos Planet RGB mensais de 4 × 4 km² cada, GSD de 4 m, 960 km² (p. 4–5).
- **Pares de datas** do mesmo local, com máscara de mudança obtida por **subtração das máscaras de área construída**; casos de edificação removida foram **omitidos** (muitos eram erro de alinhamento entre vetorizações) (p. 5).
- ≈ **16.000 pares únicos**, 264.000 pares de recortes de 224 × 224; **fração média de pixels de mudança 0,3 %** e só 1 de 7 recortes com > 0,5 % de positivos (p. 5).
- Divisão **estratificada por continente e por local**: 42 locais de treino (70 %), 6 de validação e 12 de teste (p. 5).

**Detectado automaticamente (verificar):**
- conjunto de dados **SpaceNet 7 (MUDS)**: 5 ocorrências (p. 1, 4, 9)
- resolução mencionada: 4 m (p. 1)
- “For example, when we want to forecast for the smallest possible range (i.e., one month), the subset of pairs that are one month apart contains 5000 samples, whereas, for the largest forecasting range of 24 months, we only obtain 200 samples” (p. 5, seção 60 locations with a total extent of 960 km and a ground)
- “The predicted score p̂ e is a measure of the likelihood that a given pixel will undergo an “early change”, and is trained with a cross-entropy loss w.r.t. the ground truth label y e (1 for early change, 0 for late change).” (p. 3, seção 60 locations with a total extent of 960 km and a ground)
- “The dataset also contains a set of manually labeled building footprints, where each image of the time series is labeled individually.” (p. 5, seção 60 locations with a total extent of 960 km and a ground)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 7 ocorrências (p. 1, 3, 5, 6, 7)
- **Recorte em patches/tiles**: 4 ocorrências (p. 4, 5)
- **Mosaicos e compostos**: 2 ocorrências (p. 5)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Método:**

- **Estágio 1 — detecção de mudança:** U-Net com encoder ResNet50 em rede **siamesa**, treinada com pares de datas com intervalos misturados; perda BCE; serve de **pré-treino no domínio de satélite** em vez de ImageNet (p. 3).
- **Estágio 2 — previsão:** o backbone vira extrator de uma imagem só; um classificador por horizonte (**1, 3, 6, 9, 12, 15, 18, 21 e 24 meses**) e um modelo de **janela temporal** (mudança "cedo" em 1–12 meses ou "tarde" em 12–24) com três saídas e duas perdas combinadas (λ ≈ 10³) (p. 3–4).
- **Desbalanceamento:** amostragem de recortes proporcional a (a + nº de pixels de mudança) com a ≈ 50, e **limiar escolhido por F1** em média móvel dos últimos 500 lotes em vez de 0,5 (p. 5).
- Adam, lr 1e-4, lote 16 (4 nos horizontes de 21 e 24), aumento por recorte, afins, espelhamento e color jitter; cabeça congelada por 5.000 iterações e depois ajuste fino geral com lr 1e-5 (p. 5).

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **U-Net**: 7 ocorrências (p. 1, 2, 3)
- método/família **Rede siamesa**: 7 ocorrências (p. 1, 2, 3)
- método/família **Transfer learning**: 4 ocorrências (p. 3, 5, 6, 7)
- método/família **CNN**: 3 ocorrências (p. 1, 2, 6)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 10 [−] ” (p. 4)
- batch: “batch size of 16, except for the largest forecasti” (p. 4)
- otimizador: “Adam optimizer (Kingma and Ba 2014) with def” (p. 4)
- perda: “binary cross-entropy loss” (p. 3)
- tamanho do patch: “224 × 224 pixel” (p. 5)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Desbalanceamento**: 8 ocorrências (p. 4, 5, 6, 7)
- **Conjuntos treino/val/teste**: 3 ocorrências (p. 4, 5)
- métrica **Precisão/Recall**: 28 ocorrências (p. 4, 6, 7)
- métrica **F1**: 10 ocorrências (p. 4, 5, 6, 7, 9)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Resultados:**

- O pré-treino em mudança **supera o pré-treino em ImageNet em 2–3 pontos de F1** em todos os horizontes; no horizonte de 1 mês, **8,0 % contra 1,1 %** (p. 7).
- F1 de previsão fica em cerca de **10 %** na maior parte dos horizontes e chega a **15 %** em 24 meses; a detecção melhora com o horizonte porque os rótulos ficam menos desbalanceados (p. 7, figura 4).
- Precisão maior nos primeiros 12 meses e recall maior nos 12 seguintes (p. 7).
- Os valores de F1 da detecção (limite superior) estão só em figura; o texto lido não os traz.

**Trechos numéricos detectados automaticamente (verificar):**
- “The curve exhibits a bias toward favoring recall over precision—meaning, a significant amount of recall must be relinquished to see an increase in precision larger than 20%.” (p. 6, seção 60 locations with a total extent of 960 km and a g)
- “The results show that our custom pretraining approach indeed improves performance by 3% in both accuracy and F1 score, further supporting the effectiveness of our proposed methodology.” (p. 7, seção 60 locations with a total extent of 960 km and a g)
- “We note that the “early” class exhibits a precision of 60.0%, while the precision of the “late” class amounts to 68.2%, suggesting that the later changes might be easier to detect than the earlier ones.” (p. 7, seção 60 locations with a total extent of 960 km and a g)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites e observações:**

- O método prevê **área provável** de construção, não a obra em si; as cifras de F1 são **baixas** em termos absolutos.
- **Observações minhas:** (a) o F1 de ~10 % significa que o modelo serve como mapa de **probabilidade de risco**, não como detector; (b) para 1 mês só ~5.000 amostras e para 24 meses ~200 (p. 5); (c) a abordagem de omitir remoções simplifica o problema e exclui demolições; (d) o artigo mostra que o **pré-treino em tarefa de mudança no domínio Planet** ajuda mais que ImageNet, mas o ganho é de apenas 2–3 pontos sobre uma base baixa.

**Trechos detectados automaticamente (verificar contexto):**
- “The limitation to a fixed forecasting range comes with a disadvantage, namely that one can only use a subset of the overall data for training that has the appropriate temporal spacing.” (p. 3, seção 60 locations with a total extent of 960 km and a ground)
- “This is not surprising given the inherent ambiguity of the task— from the early earthworks and preparations it is not possible to determine the precise outlines of the future buildings.” (p. 6, seção 60 locations with a total extent of 960 km and a ground)
- “Understandably, our model struggles when there is no indication of imminent construction at all— producing false negatives (blue marker).” (p. 8, seção 60 locations with a total extent of 960 km and a ground)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- Código público em github.com/nandometzger/ChangePrediction (nota de rodapé, p. 5).

- **Código/dados:** sim: github.com/nandometzger/ChangePrediction (p. 4)
- URL citada: https://github.com/nandometzger/ChangePrediction (p. 4)
- declaração: “Data Availability The SpaceNet7 dataset is publicly available (Van Etten et al.” (p. 9)
- declaração: “Code Availability [The code is available at https://​github.​com/​nando​](https://github.com/nandometzger/ChangePrediction) [metzg​er/​Chang​ePred​iction.](https://github.com/nandometzger/ChangePrediction) Declarations Conflict of Interest ” (p. 9)
- hiperparâmetros **não detectados** automaticamente: épocas/iterações (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (previsão). Previsão com horizonte de 1 a 24 meses sobre dados históricos.

**Interpretação — O que reaproveitar:**

- **Pré-treino siamês em detecção de mudança** com pares de intervalos variados, depois reaproveitado como backbone.
- **Amostragem proporcional à quantidade de mudança** e **limiar de decisão ajustado por F1** em lotes, para lidar com 0,3 % de positivos.
- **Derivação de máscaras de mudança** por subtração de máscaras de cobertura por data.
- **Divisão por continente/local** para avaliar generalização.

**Interpretação — Cuidados para o nosso projeto:**

- Não é detecção; usar só como fonte de técnicas de treino em SpaceNet 7.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- referência (curado pela leitura): [[PlanetProdutos|Produtos Planet (visão geral)]] — suporte vindo da leitura/título/resumo
- emprega conjunto de dados: [[SpaceNet7_MUDS|SpaceNet 7 / MUDS]] — 5 ocorrências (p. 1, 4, 9)
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- utiliza método: [[UNet|U-Net]] — 7 ocorrências (p. 1, 2, 3)
- utiliza método: [[RedeSiamesa|Redes siamesas]] — 7 ocorrências (p. 1, 2, 3)
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 4 ocorrências (p. 3, 5, 6, 7)
- adota desenho de validação: [[Desbalanceamento|Desbalanceamento de classes]] — 8 ocorrências (p. 4, 5, 6, 7)
- referência (curado pela leitura): [[DivisaoEspacialBlocos|Divisão espacial por blocos e áreas]] — suporte vindo da leitura/título/resumo
- é avaliado por: [[F1|F1]] — 10 ocorrências (p. 4, 5, 6, 7, 9)

**Comparações substantivas com outros artigos:**
- este artigo usa o conjunto de dados do desafio de [[Etten_2021_SpaceNetMultiTemporal|Etten 2021]] — P17 treina a previsão de construção no SpaceNet 7 e deriva as máscaras de mudança por subtração de máscaras de edificação.

## Figuras selecionadas

![[Metzger_2023_UrbanChangeForecasting_p6_Fig.5.png|520]]
*Fig. 5 Precision and recall of the foreground class of our change forecasting model w.r.t. the prediction range. The shown numbers correspon (p. 6; recorte do PDF convertido)*

![[Metzger_2023_UrbanChangeForecasting_p4_Fig.2.png|520]]
*Fig. 2 Spatial distribution of (p. 4; recorte do PDF convertido)*

![[Metzger_2023_UrbanChangeForecasting_p6_Fig.6.png|520]]
*Fig. 6 Precision-recall curve for the change forecast model with time (p. 6; recorte do PDF convertido)*


## Anotações do leitor

- 
