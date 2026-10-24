---
tipo: artigo
id_origem: P32
titulo: "Prithvi-EO-2.0: A Versatile Multitemporal Foundation Model for Earth Observation Applications"
ano: 2024
autores: ["Daniela Szwarcman", "Sujit Roy", "Paolo Fraccaro", "Þorsteinn Elí Gíslason", "Benedikt Blumenstiel", "Rinki Ghosal", "Pedro Henrique de Oliveira", "Joao Lucas de Sousa Almeida"]
doi: "10.48550/arXiv.2412.02732"
arquivo_fonte: "coleta/P32_Szwarcman2025_Prithvi-EO-2-0-A-Versatile-Multitemporal-Foundation-Model-fo.pdf"
markdown_fonte: "output/pdf/P32_Szwarcman2025_Prithvi-EO-2-0-A-Versatile-Multitemporal-Foundation-Model-fo/document.md"
paginas: 21
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (parcial)"
relevancia_objetivo: "B"
tarefas: ["[[SITS|Séries temporais de imagens (SITS)]]"]
sensores: ["[[Sentinel2|Sentinel-2]]", "[[Landsat|Landsat]]"]
conjuntos_dados: []
metodos: ["[[ModeloFundacional|Modelos fundacionais]]", "[[Transformer|Transformers]]", "[[TransferLearning|Aprendizado por transferência]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/parcial, relevancia/B]
---

# Szwarcman 2024 — Prithvi-EO-2.0: A Versatile Multitemporal Foundation Model for Earth Observation Applications

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (parcial). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **B** — Prithvi-EO-2.0: modelo fundacional multitemporal em HLS de 30 m; sem Planet.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Daniela Szwarcman, Sujit Roy, Paolo Fraccaro, Þorsteinn Elí Gíslason et al. (2024). Prithvi-EO-2.0: A Versatile Multitemporal Foundation Model for Earth Observation Applications. IEEE Transactions on Geoscience and Remote Sensing. Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2412.02732
- **Arquivo de origem:** `coleta/P32_Szwarcman2025_Prithvi-EO-2-0-A-Versatile-Multitemporal-Foundation-Model-fo.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P32_Szwarcman2025_Prithvi-EO-2-0-A-Versatile-Multitemporal-Foundation-Model-fo/document.md` — 21 páginas, 48 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Apresentar o **Prithvi-EO-2.0**, um **modelo fundacional geoespacial multitemporal** (MAE com ViT 3D) pré-treinado em séries do HLS a 30 m, e mostrar que serve a tarefas de resoluções e domínios diferentes (de 0,1 m a 15 m) com ajuste fino em uma só GPU (p. 1–2). **Não é um modelo de detecção de mudança**; é um backbone que se acopla a cabeças de segmentação, classificação ou regressão.

- “1 ## Prithvi-EO-2.0: A Versatile Multi-Temporal Foundation Model for Earth Observation Applications Daniela Szwarcman [1,] [†], Sujit Roy [2,3,] [ †] [,] [ ‡] (Senior Member, IEEE), Paolo Fraccaro [1,] [ †] [,] [ ‡], Þorsteinn Elí Gíslason ” (p. 1, seção Início)
- “within the EO community, we developed a new multi-temporal GFM called Prithvi-EO-2.0 .” (p. 2, seção I. I NTRODUCTION)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “Each image covers an area of 640 m × 640 m, which contrasts with our pretraining dataset, where the images are 224 × 224 pixels with a resolution of 30 m, covering approximately 6,720 m × 6,720 m—over 100 times the area of the Sen4Map sampl” (p. 8, seção 0.1. As described in section III-A, the samples have shape)
- “To achieve this, we built temporal sequences of four HLS images with intervals of one to six months between consecutive times tamps, spanning the period from 2014 and 2023.” (p. 3, seção III. M ETHODS)
- “The dataset consists of 446 512 × 512 images covering 14 biomes, 357 ecoregions, and 6 continents of the world across 11 flood events between 2018 and 2020.” (p. 6, seção 0.1. As described in section III-A, the samples have shape)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- **Pré-treino:** HLS (Landsat 8/9 + Sentinel-2) a 30 m, **seis bandas** (azul, verde, vermelho, NIR, SWIR1, SWIR2); sequências de **4 datas** com intervalo de 1 a 6 meses entre 2014 e 2023; patches 256 × 256; **4,2 M amostras de treino e 46 mil de validação**; descartes: > 1 % de pixels ausentes ou > 20 % de nuvem (Fmask); amostragem estratificada por cobertura (Copernicus Land Cover 100 m) e 846 ecorregiões; áreas urbanas sobreamostradas (p. 2–3).
- **GEO-Bench:** 6 conjuntos de classificação e 6 de segmentação (tabela I, p. 6); só as bandas multiespectrais compatíveis com cada modelo; imagens redimensionadas para 224 × 224 (p. 6).
- **Tarefas de aplicação (tabela III, p. 7):** inundação (Sen1Floods11, 446 imagens), cicatriz de incêndio (805), intensidade de queima (5.692, 3 datas), deslizamento (3.799), segmentação de cultura nos EUA (5.000, 3 datas) e na França (2.433 com 38–61 datas), classificação na Europa (335.125), GPP (975) e biomassa acima do solo (3.400 com 12 datas).
- Nenhum teste em Planet ou em mosaico 3–5 m.

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-2**: 37 ocorrências (p. 2, 6, 7, 8, 9)
- sensor/produto **Sentinel-1**: 14 ocorrências (p. 2, 6, 7, 9, 18)
- sensor/produto **Landsat**: 8 ocorrências (p. 1, 2, 6, 7, 18)
- sensor/produto **SAR**: 8 ocorrências (p. 15, 16, 18)
- resolução mencionada: 30 m (p. 2)
- resolução mencionada: 10 m (p. 8)
- “Despite its spatiotemporal design, U-BARN is trained with small 64 × 64 patches and a very restricted pretraining dataset, considering only nine Sentinel-2 tiles from France over two years .” (p. 2, seção 12 months of data from different sources, with each month)
- “The sequences were iteratively sampled from the selected HLS tiles until all candidates (minimum of four timestamps) were processed or 1,500 samples per tile (250 for validation) were reached.” (p. 3, seção III. M ETHODS)
- “Then, the sequences were split into nonoverlapping 256 × 256 patches with four consecutive timestamps.” (p. 3, seção III. M ETHODS)
- “These models can help address longstanding challenges in EO by reducing the need for manually labeled samples, which are usually hard to obtain at scale .” (p. 1, seção I. I NTRODUCTION)
- “It measures the average overlap between predicted and ground truth regions across all classes, defined as: where C is the total number of classes and prediction c and truth c denote the predicted and ground truth regions for class c, respec” (p. 5, seção 0.1. As described in section III-A, the samples have shape)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 70 ocorrências (p. 1, 2, 3, 4, 5)
- **Aumento de dados**: 10 ocorrências (p. 2, 5, 6, 8, 9)
- **Rotulagem / anotação**: 9 ocorrências (p. 1, 2, 5, 8, 10)
- **Máscara de nuvem e sombra**: 7 ocorrências (p. 3, 7, 9, 10)
- **Índices espectrais**: 6 ocorrências (p. 10, 16)
- **Normalização / escala**: 4 ocorrências (p. 5, 8, 9)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Método:**

- **MAE com ViT**, embeddings **3D** de patch e posição (cubos t = 1, h, w) e metadados opcionais de **latitude/longitude e ano/dia do ano**, somados como viés aprendido com probabilidade de descarte 0,1; versões 300 M (ViT-L) e 600 M (ViT-H), com e sem TL (p. 4–5).
- Pré-treino: 400 épocas em A100, ~21.000 GPU-horas (300 M) e ~58.000 (600 M); lote global 3.840, lr máx. 5e-4, weight decay 0,05, recorte 4 × 224 × 224 e flips (p. 5).
- **Protocolo de benchmark:** 10 tentativas de otimização bayesiana de hiperparâmetros (Optuna/TerraTorch-iterate), depois **10 repetições com sementes diferentes**; decodificador UPerNet para transformers e U-Net para ResNets; camada linear na classificação (p. 5–6). Fine-tuning de cada aplicação em uma única GPU (p. 5).

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 37 menções vs 0 de pares)
**Métodos detectados automaticamente:**
- método/família **Modelo fundacional**: 288 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Transformer**: 59 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Transfer learning**: 32 ocorrências (p. 1, 2, 5, 7, 8)
- método/família **U-Net**: 30 ocorrências (p. 2, 5, 8, 9, 12)
- método/família **XGBoost**: 7 ocorrências (p. 10, 16)
- método/família **Semi/auto-supervisionado**: 7 ocorrências (p. 1, 2, 3, 8, 18)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 5e-4 and linear warmup for 40 epochs starting ” (p. 5)
- batch: “batch size (i” (p. 5)
- épocas/iterações: “400 epochs” (p. 5)
- otimizador: “Adam optimizer with a learning rate of 1e-5” (p. 8)
- perda: “cross-entropy and the models ran for 50 epochs with e” (p. 6)
- tamanho do patch: “64 × 64 patch” (p. 2)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 27 ocorrências (p. 5, 6, 8, 9, 11)
- **Validação cruzada**: 2 ocorrências (p. 10, 17)
- métrica **IoU**: 45 ocorrências (p. 5, 6, 8, 9, 11)
- métrica **F1**: 18 ocorrências (p. 5, 6, 8, 9, 12)
- métrica **Precisão/Recall**: 14 ocorrências (p. 5, 13)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Métricas e resultados:**

- Acurácia (classificação), mIoU (segmentação), IoU da classe, F1, R² e RMSE conforme a tarefa (p. 5).
- **GEO-Bench:** os modelos 600 M e 600 M-TL têm o melhor desempenho combinado nos 12 conjuntos e nos de segmentação; na classificação DOFA aparece entre os melhores (p. 11). O Prithvi-EO-2.0-100M supera o Prithvi-EO-1.0-100M em ~3 % no escore geral, e o resumo fala em até 8 % (p. 1, 11). Modelos com TL superam os sem TL (p. 12).
- **Tarefas de alta resolução** (árvores por drone, gado) vão bem mesmo com pré-treino só em 30 m (p. 12).
- **Inundação** (tabela IV, p. 12): IoU da água 79,6 (v1.0-100M) → 83,1 (v2.0-600M-TL), +3,5; mIoU 88,3 → 90,3.
- **Cicatriz de incêndio** (tabela V, p. 12): IoU da cicatriz 76,8 → 83,2 (600 M), +5,6 a +6,4 conforme a versão.
- **Biomassa:** com apenas multiespectral aproxima modelos multimodais; **adicionar SAR como bandas não melhorou** (p. 16).
- **GPP** (tabela XV, p. 16): R² 2018–2021 de 0,88/0,80/0,83/0,74 para o 600 M-TL contra 0,72/0,77/0,73/0,66 do random forest com índices; média do ResNet18 0,75 vs 0,81.

**Trechos numéricos detectados automaticamente (verificar):**
- “Through extensive benchmarking with GEO-Bench, the model outperforms the previous Prithvi- EO model by 8% across a range of tasks.” (p. 1, seção 2 data archive at 30-m resolution, the new model i)
- “Interestingly, although the mIoU is generally low for all models, they seem capable of distinguishing unburnt from burnt areas, with IoU 0 above 67%.” (p. 12, seção 2.0 improves over its previous version. Given the )
- “Prithvi-EO-2.0600M, trained with weighted cross-entropy loss, exhibited a slightly lower mIoU of 70.4% and an F1 score of 58.6%, but achieved a higher recall than Prithvi-EO-2.0-300M.” (p. 13, seção 2.0 improves over its previous version. Given the )
- “Recall mAcc U-Net wCE 70.4 59.7 56.2 63.6 98.4 U-Net++ wCE 69.0 57.0 50.2 68.4 98.0 Prithvi-EO-2.0-300M Lovasz 71.3 60.7 57.1 64.7 98.4 Prithvi-EO-2.0-600M wCE 70.4 58.6 51.1 68.6 98.2 TABLE VIII: Performance metrics on the test set of L4S for models trained w” (p. 13, seção 2.0 improves over its previous version. Given the )

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites declarados e observações:**

- Trabalho futuro citado: comparar com modelos multimodais e avaliar o custo de acrescentar dados no ajuste fino (p. 17).
- **Observações minhas:** (a) o ganho de "até 8 %" e de "3 %" vem de agregados de benchmarks muito heterogêneos, em escalas de métrica diferentes (acurácia, mIoU, F1); o artigo mesmo diz que a média é "apropriada" apesar da natureza distinta; (b) a variação do m-cashew-plant depende de a classe 0 ausente no teste ser prevista ou não (p. 11), o que mostra sensibilidade da métrica; (c) vários ganhos são menores que 1 desvio-padrão (p. ex., inundação 600 M vs 300 M, tabela IV); (d) nenhuma das tarefas é detecção de mudança semântica bitemporal; o mais próximo é a cicatriz de incêndio e a intensidade de queima, mas com cabeça de segmentação, não comparação de datas; (e) o pré-treino é em **30 m**; para 3–5 m o artigo só afirma boa transferência em tarefas de alta resolução sem detalhar a perda; (f) como as tabelas II e IX–XIV foram lidas só em parte, não cito números delas.

**Trechos detectados automaticamente (verificar contexto):**
- “However, all models seem to struggle to differentiate between the various severity classes, with the Prithvi models demonstrating better overall performance.” (p. 13, seção 2.0 improves over its previous version. Given the unbalanced)
- “This is because multispectral sensors are only capable of sensing the reflectance of the top layer of canopy, and so cannot be used to accurately estimate biomass of vegetation obscured by a full canopy.” (p. 15, seção 2.0 improves over its previous version. Given the unbalanced)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- Pesos no Hugging Face (`ibm-nasa-geospatial/Prithvi-EO-2.0`), código no GitHub (`NASA-IMPACT/Prithvi-EO-2.0`) e integração ao **TerraTorch** com os carregadores das tarefas (p. 1–2).

- **Código/dados:** sim: huggingface.co/ibm-nasa-geospatial/Prithvi-EO-2 (p. 1)
- URL citada: https://huggingface.co/ibm-nasa-geospatial/Prithvi-EO-2 (p. 1)
- URL citada: https://huggingface.co/ibm-nasa-geospatial/Prithvi-EO-2.0 (p. 1)
- URL citada: https://github.com/NASA-IMPACT/Prithvi-EO-2.0 (p. 1)
- URL citada: https://github.com/IBM/terratorch (p. 2)
- declaração: “Prithvi-EO-2.0 is available as an open-source model on Hugging Face and IBM TerraTorch, with additional resources on GitHub.” (p. 1)
- declaração: “Code available at: https://github.com/NASA-IMPACT/Prithvi-EO-2.0](https://huggingface.co/ibm-nasa-geospatial/Prithvi-EO-2.0)” (p. 1)

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Rastreabilidade 4 (p. 2, 5, 7); Latência / frequência 1 (p. 1); Persistência / confirmação 1 (p. 3); Custo 1 (p. 16)

**Interpretação — O que reaproveitar:**

- **Backbone multitemporal pré-treinado** (sequência de datas + metadados de data/local) para extração de características de uma série de mosaicos, em vez de dois instantes.
- **Protocolo de comparação** do GEO-Bench com 10 repetições e ajuste de hiperparâmetros com o mesmo orçamento, útil para não comparar modelos com esforços desiguais.
- **TerraTorch** como infraestrutura de ajuste fino em uma GPU.
- **Descarte de metadados** durante o pré-treino para funcionar quando data e local faltam.

**Interpretação — Cuidados para o nosso projeto:**

- Seis bandas do HLS a 30 m: **não há as bandas Planet** (azul, verde, vermelho, NIR a 3–5 m); seria preciso reamostrar ou refazer o pré-treino, e o ganho nesse caso não foi medido.
- Não resolve a "pergunta de mudança" sozinho; precisa de cabeça e rótulos próprios.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza método: [[ModeloFundacional|Modelos fundacionais]] — 288 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[Transformer|Transformers]] — 59 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 32 ocorrências (p. 1, 2, 5, 7, 8)
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 37 ocorrências (p. 2, 6, 7, 8, 9)
- utiliza dado/sensor: [[Landsat|Landsat]] — 8 ocorrências (p. 1, 2, 6, 7, 18)
- referência (curado pela leitura): [[SITS|Séries temporais de imagens (SITS)]] — suporte vindo da leitura/título/resumo

**Comparações substantivas com outros artigos:**
- este artigo é modelo fundacional afim a [[Shen_2026_FoundationModelDriven|Shen 2026]] — P34 testa SatMAE, ScaleMAE e SeCo como encoders; P32 é um encoder multitemporal em HLS de 30 m (interpretação: candidato a encoder, sem teste em mudança).

## Figuras selecionadas

![[Szwarcman_2024_PrithviVersatileMultitemporal_p4_Fig.3.png|520]]
*Fig. 3: Prithvi-EO-2.0 architecture and general pretraining framework. (p. 4; recorte do PDF convertido)*

![[Szwarcman_2024_PrithviVersatileMultitemporal_p11_Figure6.png|520]]
*Figure 6 shows the aggregated results of benchmarking (p. 11; recorte do PDF convertido)*

![[Szwarcman_2024_PrithviVersatileMultitemporal_p7_Fig.4.png|520]]
*Fig. 4: Locations of the burn intensity dataset used in training (p. 7; recorte do PDF convertido)*


## Anotações do leitor

- 
