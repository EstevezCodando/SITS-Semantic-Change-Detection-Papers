---
tipo: artigo
id_origem: P09
titulo: "Tropical dry forest land use/land cover change detection using semi-supervised deep learning algorithms and remote sensing"
ano: 2026
autores: ["Juan Carlos Gonzalez-Velez", "Maria Constanza Torres-Madronero", "Juan D. Martinez-Vargas", "Paula Rodríguez-Marín", "Jheison Perez-Guerra", "Veronica Herrera-Ruiz"]
doi: "10.1007/s10661-025-14897-4"
arquivo_fonte: "coleta/P09_Gonzalez-Velez2026_Tropical-dry-forest-land-use-land-cover-change-detection-usi.pdf"
markdown_fonte: "output/pdf/P09_Gonzalez-Velez2026_Tropical-dry-forest-land-use-land-cover-change-detection-usi/document.md"
paginas: 27
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "A"
tarefas: ["[[ClassificacaoCobertura|Classificação de cobertura e uso da terra]]", "[[Desmatamento|Desmatamento]]"]
sensores: ["[[Sentinel2|Sentinel-2]]", "[[PlanetNICFI|Planet NICFI (basemaps)]]", "[[Sentinel1|Sentinel-1]]"]
conjuntos_dados: []
metodos: ["[[UNet|U-Net]]", "[[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]", "[[IndicesEspectrais|Índices espectrais (NDVI etc.)]]"]
validacao: []
ferramentas: []
tags: [artigo, leitura/profunda, relevancia/A]
---

# GonzalezVelez 2026 — Tropical dry forest land use/land cover change detection using semi-supervised deep learning algorithms and remote sensing

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **A** — NICFI de 5 m com Sentinel-1 em floresta seca; Y-Net semissupervisionada; divisão por tiles, mas sem validação independente da mudança.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Juan Carlos Gonzalez-Velez, Maria Constanza Torres-Madronero, Juan D. Martinez-Vargas, Paula Rodríguez-Marín et al. (2026). Tropical dry forest land use/land cover change detection using semi-supervised deep learning algorithms and remote sensing. Environmental Monitoring and Assessment. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1007/s10661-025-14897-4
- **Arquivo de origem:** `coleta/P09_Gonzalez-Velez2026_Tropical-dry-forest-land-use-land-cover-change-detection-usi.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P09_Gonzalez-Velez2026_Tropical-dry-forest-land-use-land-cover-change-detection-usi/document.md` — 27 páginas, 57 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Detectar mudança de **uso e cobertura (LULC) em floresta tropical seca** no vale do Rio Cauca (Antioquia, Colômbia) com **fusão óptico–radar** (PlanetScope NICFI a 5 m + Sentinel-1 a 10 m) e um **framework semissupervisionado** (pseudo-rótulos de k-means + uma rede Y-Net de dois codificadores), para o período 2017–2021 (p. 1–3). A mudança é obtida pela diferença dos mapas de 2017, 2019 e 2021.

- “This study aims to overcome these limitations.” (p. 3, seção Introduction)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “3 Study area: a localization, b RGB composition of the optical image from Planet Scope 2017, c Official IDEAM Corine Land Cover (CLC) map 2019 (derived from images of 2017) concatenated with TDF map from Instituto Alexander Von Humboldt der” (p. 7, seção Experiments)
- “Finally, Experiment 6 applies the optimized model for temporal LULC change detection (2017–2021), and Experiment 7 assesses the framework’s scalability on an extended study area.” (p. 7, seção Experiments)
- “The proposed semi-supervised framework is applied to reveal TDF changes in the Cauca River Valley in Antioquia (Colombia) using satellite images between 2017 and 2021.” (p. 1, seção V. Herrera‑Ruiz)
- “The temporal resolution of these products changed over time: biannual (6-month) mosaics are available for the 2015–2020 period, while monthly mosaics are provided from September 2020 onwards.” (p. 7, seção Experiments)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- **PlanetScope NICFI** (analysis-ready mosaics, RGB+NIR): mosaicos de 6 meses para 2017 e 2019 e mosaico anual agregado de meses para 2021, porque o NICFI é bianual até 2020 e mensal depois de set/2020; reamostrados a **5 m** na exportação do GEE (p. 7–8).
- **Sentinel-1** GRD (IW, órbita ascendente): mediana anual de 2017, 2019 e 2021 em quatro bandas (VV, VH, HH, HV) ("pseudo-quad-pol") (p. 8). **Sentinel-2** L2A (10 m) só nos experimentos 1 e 2 (p. 8).
- Área: ~18.000 ha de TDF no recorte inicial e ~15.000 km² na área estendida "Centro de Antioquia" (p. 7–9).
- Referência: mapa **Corine Land Cover/IDEAM 2019** (derivado de imagens de 2017; unidade mínima 25 ha, 5 ha para superfícies artificiais) e mapa de TDF do Instituto Humboldt (Pizano et al., 2015) (p. 9–10).

**Detectado automaticamente (verificar):**
- sensor/produto **SAR**: 42 ocorrências (p. 1, 2, 3, 5, 7)
- sensor/produto **PlanetScope**: 13 ocorrências (p. 7, 8, 10, 12, 22)
- sensor/produto **Sentinel-2**: 12 ocorrências (p. 7, 8, 10, 12, 18)
- sensor/produto **Planet NICFI**: 10 ocorrências (p. 7, 8, 10, 11)
- resolução mencionada: 5 m (p. 3)
- resolução mencionada: 10 m (p. 3)
- resolução mencionada: 4.7 m (p. 7)
- “To prevent temporal leakage, the training and validation sets were constructed exclusively from 2017 imagery, whereas the 2019 and 2021 images were reserved for inference.” (p. 10, seção 2 Sentinel-1 SAR 10 m VV – HH – VV + VH 2017, 2019, 2021)
- “Y-Net was designed using PyTorch and trained each run for 300 epochs with a batch size of 10 images, using the AdamW optimizer with a weight decay of 5 × 10 ⁻ and an initial learning rate of 1.58 × 10 ⁻ that was modulated each step by a One” (p. 12, seção 10 to 90% unlabeled. Pseudo-labels for the unlabeled)
- “15,000 ­km ), incorporating a larger volume of unlabeled data (4,470 patches) to assess performance on a broader regional scale.” (p. 12, seção 10 to 90% unlabeled. Pseudo-labels for the unlabeled)
- “The map derives from images taken in 2017 and corresponds with the classes at the first level of the adapted CLC methodology for Colombia using a combination of manually annotated images from Sentinel-1, Landsat and medium/high resolution c” (p. 8, seção 2 Sentinel-1 SAR 10 m VV – HH – VV + VH 2017, 2019, 2021)
- “To compute these performance metrics, the labeled validation dataset was used as ground truth.” (p. 11, seção 2 Sentinel-1 SAR 10 m VV – HH – VV + VH 2017, 2019, 2021)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 62 ocorrências (p. 1, 2, 3, 8, 10)
- **Mosaicos e compostos**: 21 ocorrências (p. 7, 8)
- **Recorte em patches/tiles**: 13 ocorrências (p. 2, 8, 10, 12, 15)
- **Máscara de nuvem e sombra**: 10 ocorrências (p. 2, 7, 24, 25)
- **Índices espectrais**: 9 ocorrências (p. 10, 11, 13)
- **Normalização / escala**: 7 ocorrências (p. 5, 8, 10, 11, 24)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Preparação:**

- Máscara de nuvem por banda QA do Sentinel-2 e composição semestral/anual; NDVI e GNDVI como índices (EVI e NDWI excluídos de propósito) (p. 7, 10).
- Patches com **mesma área no terreno (~2,88 km²)**: 288 × 288 px a 10 m e 576 × 576 px a 5 m (p. 10). Normalização global com mínimo e máximo do treino de 2017 aplicada ao resto (p. 10).
- Divisão: 70 % treino+validação (85/15) e 30 % teste, **por tiles inteiros** para reduzir autocorrelação espacial; treino e validação só com imagens de **2017**; 2019 e 2021 reservadas para inferência (p. 10).

**Evidência (leitura) — Método:**

- **Supervisionado:** U-Net e PSPNet com encoders ResNet-18/50/101/152, óptico (Exp. 1) e óptico+SAR concatenado (Exp. 2) (p. 10, 12).
- **Y-Net** (dois codificadores, óptico 5 m e SAR 10 m, com **fusão precoce** por concatenação após a primeira convolução), sem reamostrar as entradas (p. 3–5).
- **Pseudo-rótulos:** k-means, k-means++ e PCA k-means (k = 6) com **voto de maioria**; rótulos gerados uma só vez, **sem filtro de confiança** (p. 5, 11).
- **Treino:** PyTorch, AdamW (weight decay 5e-4), lr inicial 1,58e-3 com OneCycleLR, 300 épocas, batch 10, parada antecipada com 10 épocas sem melhora, perda Jaccard (p. 12; valores de expoente conferir no PDF).
- **Mudança:** 5 execuções com sementes diferentes; mudança só quando ≥ 3 dos 5 modelos concordam; análise de hotspots Getis-Ord Gi (p. 12).

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **U-Net**: 47 ocorrências (p. 1, 5, 7, 10, 12)
- método/família **Semi/auto-supervisionado**: 28 ocorrências (p. 1, 2, 3, 5, 7)
- método/família **CNN**: 4 ocorrências (p. 5, 22, 23)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 1.58 × 10 ⁻ that was modulated each step by a O” (p. 12)
- batch: “batch size of 10 images, using the AdamW optimizer” (p. 12)
- épocas/iterações: “300 epochs” (p. 12)
- otimizador: “AdamW optimizer with a weight decay of 5 × 10” (p. 12)
- tamanho do patch: “288 × 288 pixel” (p. 10)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 7 ocorrências (p. 10, 11)
- **Teste externo / generalização**: 7 ocorrências (p. 2, 9, 12, 15, 23)
- métrica **IoU**: 53 ocorrências (p. 1, 10, 11, 12, 13)
- métrica **F1**: 17 ocorrências (p. 11, 13, 14, 15, 18)
- métrica **Acurácia global**: 12 ocorrências (p. 1, 10, 11, 13, 14)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Métricas e resultados:**

- Exp. 1 (S2, U-Net ResNet-18): acurácia de teste 94,2 % e mIoU 82,1 % contra 91,7 % e 75,4 % do PSPNet (p. 13, tabela 2).
- Exp. 3: **Y-Net** acurácia de teste 96,3 % e mIoU 84,7 % contra 93,8 % e 82,8 % da U-Net (média de 4 execuções; p. 13, tabela 4). Na classe TDF, IoU 77,8 % e F1 87,5 % (p. 13).
- Exp. 4: k-means++ 86,8 % de acurácia de teste; PCA k-means F1 79,7 %; k-means 79,2 %/77,3 % (p. 14, tabela 7).
- Exp. 5 (SSL): com **10 % não rotulados** a acurácia de teste foi 97,5 % e o mIoU 85,1 %, acima da Y-Net supervisionada; a acurácia cai com mais pseudo-rótulos: 90,4 % com 40 % não rotulados, 85,0 % com 60 %, 62,0 % com 90 % (p. 15, tabela 8).
- Exp. 7 (área estendida, 4.470 patches não rotulados + 561 rotulados): acurácia de teste 95,3 % e **mIoU 88,1 %** (p. 15, 18, tabela 9).
- **Mudança de TDF:** 21.307 ha (2017, do mapa de referência), 19.645 ha (2019, −7,8 %) e 18.586 ha (2021, −5,4 %), com margem de ±235 ha e ±223 ha (1,2 %) (p. 15, 18, tabela 11).

**Trechos numéricos detectados automaticamente (verificar):**
- “Four experiments were carried out for each model, randomly splitting the dataset into training (70%) and testing (30%) using the accuracy and F1 score as performance metrics.” (p. 11, seção 2 Sentinel-1 SAR 10 m VV – HH – VV + VH 2017, 2019)
- “This fixed mapping (e.g., “Cluster 1” = “Forest”) was then applied to the unseen 30% test set to calculate the final accuracy and F1 scores reported in Table 7.” (p. 11, seção 2 Sentinel-1 SAR 10 m VV – HH – VV + VH 2017, 2019)
- “Supervised model In Experiment 1 (optical-only classification with Sentinel-2), U-Net generally outperformed PSPNet across most metrics, achieving higher test accuracies (above 93%) and mIoU scores (above 80%).” (p. 12, seção Results)
- “For example, U-Net with a ResNet-18 encoder achieved a test accu racy of 94.2% and a test mIoU of 82.1%, whereas PSPNet with the same encoder reached 91.7% accu racy and 75.4% mIoU.” (p. 12, seção Results)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites declarados e observações:**

- A Y-Net é mais complexa e sensível: um ramo pode dominar o outro se o treino for mal ajustado (p. 24).
- Pseudo-rótulos sem filtro de confiança e geradas por três variantes do mesmo algoritmo: risco de reforçar viés sistemático (p. 24).
- **Incerteza da referência:** descompasso de escala entre 5 m e o CLC, rótulos de TDF incluem áreas de transição e regeneração ambíguas; erros do mapa de 2017 são propagados (p. 24).
- **Sem validação independente da mudança**: "falta um conjunto externo de polígonos de mudança rotulados por especialistas" (p. 24). A incerteza por pixel (softmax) não foi propagada (p. 24).
- Composição anual **atenua a fenologia intra-anual** do TDF (p. 7, 24).
- **Observações minhas:** (a) a "perda de 7,8 % entre 2017 e 2019" compara o **mapa de referência de 2017** (Pizano) com a **predição de 2019**, fontes diferentes (tabela 11, p. 18), então parte da diferença pode ser artefato de fonte; (b) o texto troca F1 e IoU da classe TDF no Exp. 7 (diz F1 87,9 % e IoU 93,6 %; a tabela 10 mostra IoU 0,879 e F1 0,936; p. 15, 18); (c) o resultado do Exp. 7 tem acurácia menor que a Y-Net supervisionada (0,953 vs 0,963) e mIoU maior (0,881 vs 0,847), e o desvio entre as execuções não é informado; (d) a margem de ±1,2 % é a taxa de classificação errada do TDF, não um intervalo de confiança amostral.

**Trechos detectados automaticamente (verificar contexto):**
- “Additionally, exploring learned up-sampling or multiscale fusion strategies could further improve robustness and will be investigated in future work.” (p. 11, seção 2 Sentinel-1 SAR 10 m VV – HH – VV + VH 2017, 2019, 2021)
- “197 Page 12 of 27 confidence-thresholded pseudo-labeling is a standard SSL practice and will be incorporated in future work (Sohn et al., 2020).” (p. 12, seção 10 to 90% unlabeled. Pseudo-labels for the unlabeled)
- “In contrast, standard k-means had the lowest performance (mean test accuracy 79.2% and F1 77.3%), suggesting it struggled to segregate the complex feature space as effectively.” (p. 22, seção Discussion)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- "Nenhum conjunto de dados foi gerado ou analisado" na declaração de disponibilidade; os dados vêm do GEE e de mapas públicos; código não informado (p. 25).

- **Código/dados:** declarado sem URL localizada (p. 7)
- declaração: “This selection was driven by the program’s data availability structure and the objective to minimize cloud cover artifacts.” (p. 7)
- declaração: “Data availability No datasets were generated or analysed during the current study.” (p. 25)
- hiperparâmetros **não detectados** automaticamente: perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo. Mapas de 2017, 2019 e 2021 comparados depois; sem avaliação independente da mudança.
- menções de termos de monitoramento (contagem, não avaliação): Persistência / confirmação 2 (p. 2); Custo 2 (p. 23, 24); Rastreabilidade 1 (p. 8)

**Interpretação — O que reaproveitar:**

- **Fusão óptico–radar sem reamostrar** (Y-Net) onde nuvem é frequente, e a prática de **chunks com mesma área no terreno** entre sensores de resolução diferente.
- **Divisão por tiles inteiros e por ano** (treino em 2017, inferência em 2019/2021) como guarda contra vazamento espacial e temporal.
- **Conjunto de 5 execuções com voto ≥ 3/5** para filtrar mudanças instáveis, e **hotspots Getis-Ord** para priorizar revisão humana.
- **Pseudo-rótulos por clusterização** como pré-anotação barata, desde que se meça o efeito (queda forte acima de ~40 % de pseudo-rótulos).

**Interpretação — Cuidados para o nosso projeto:**

- O mosaico NICFI aqui é **semestral/anual agregado**, não mensal; não serve para datar eventos mensais.
- Os números de acurácia são de cobertura contra mapas de referência de 25 ha; a mudança não foi validada de forma independente.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 12 ocorrências (p. 7, 8, 10, 12, 18)
- utiliza dado/sensor: [[PlanetNICFI|Planet NICFI (basemaps)]] — 10 ocorrências (p. 7, 8, 10, 11)
- utiliza dado/sensor: [[Sentinel1|Sentinel-1]] — 7 ocorrências (p. 7, 8, 10, 12, 18)
- trata a tarefa: [[ClassificacaoCobertura|Classificação de cobertura e uso da terra]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[Desmatamento|Desmatamento]] — suporte vindo da leitura/título/resumo
- utiliza método: [[UNet|U-Net]] — 47 ocorrências (p. 1, 5, 7, 10, 12)
- utiliza método: [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 28 ocorrências (p. 1, 2, 3, 5, 7)
- referência (curado pela leitura): [[DivisaoEspacialBlocos|Divisão espacial por blocos e áreas]] — suporte vindo da leitura/título/resumo
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 62 ocorrências (p. 1, 2, 3, 8, 10)
- aplica etapa de preparo: [[IndicesEspectrais|Índices espectrais (NDVI etc.)]] — 9 ocorrências (p. 10, 11, 13)

**Comparações substantivas com outros artigos:**
- [[Simsek_2025_DeterminationLandLand|Simsek 2025]] compartilha o problema de fontes diferentes com este artigo — P06 compara o mapa de 2023 com o cadastro de 2015, e P09 compara o mapa de 2019 com o de 2017 de outra fonte; ambos herdam diferenças de fonte.

## Figuras selecionadas

![[GonzalezVelez_2026_TropicalDryForest_p3_Fig.1.png|520]]
*Fig. 1 Proposed SSL framework to integrate optical and SAR images for LULC (p. 3; recorte do PDF convertido)*


## Anotações do leitor

- 
