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
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[ClassificacaoCobertura|Classificação de cobertura e uso da terra]]"]
sensores: ["[[SAR|Radar (SAR)]]", "[[PlanetScope|PlanetScope (Dove/SuperDove)]]", "[[Sentinel2|Sentinel-2]]"]
conjuntos_dados: []
metodos: ["[[UNet|U-Net]]", "[[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]]", "[[CNN|Redes convolucionais (CNN)]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]", "[[MosaicosCompostos|Mosaicos e compostos temporais]]", "[[PatchesTiles|Recorte em patches/tiles]]", "[[MascaraNuvem|Máscara de nuvem e sombra]]", "[[IndicesEspectrais|Índices espectrais (NDVI etc.)]]"]
validacao: ["[[DivisaoTreinoTeste|Divisão treino/validação/teste]]", "[[Generalizacao|Generalização e domain shift]]", "[[IoU|IoU / mIoU]]", "[[F1|F1]]", "[[AcuraciaGlobal|Acurácia global (OA)]]"]
ferramentas: ["[[GoogleEarthEngine|Google Earth Engine]]"]
tags: [artigo, leitura/automatica]
---

# GonzalezVelez 2026 — Tropical dry forest land use/land cover change detection using semi-supervised deep learning algorithms and remote sensing

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Juan Carlos Gonzalez-Velez, Maria Constanza Torres-Madronero, Juan D. Martinez-Vargas, Paula Rodríguez-Marín et al. (2026). Tropical dry forest land use/land cover change detection using semi-supervised deep learning algorithms and remote sensing. Environmental Monitoring and Assessment. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1007/s10661-025-14897-4
- **Arquivo de origem:** `coleta/P09_Gonzalez-Velez2026_Tropical-dry-forest-land-use-land-cover-change-detection-usi.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P09_Gonzalez-Velez2026_Tropical-dry-forest-land-use-land-cover-change-detection-usi/document.md` — 27 páginas, 57 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “This study aims to overcome these limitations.” (p. 3, seção Introduction)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “3 Study area: a localization, b RGB composition of the optical image from Planet Scope 2017, c Official IDEAM Corine Land Cover (CLC) map 2019 (derived from images of 2017) concatenated with TDF map from Instituto Alexander Von Humboldt der” (p. 7, seção Experiments)
- “Finally, Experiment 6 applies the optimized model for temporal LULC change detection (2017–2021), and Experiment 7 assesses the framework’s scalability on an extended study area.” (p. 7, seção Experiments)
- “The proposed semi-supervised framework is applied to reveal TDF changes in the Cauca River Valley in Antioquia (Colombia) using satellite images between 2017 and 2021.” (p. 1, seção V. Herrera‑Ruiz)
- “The temporal resolution of these products changed over time: biannual (6-month) mosaics are available for the 2015–2020 period, while monthly mosaics are provided from September 2020 onwards.” (p. 7, seção Experiments)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

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

**Trechos numéricos detectados automaticamente (verificar):**
- “Four experiments were carried out for each model, randomly splitting the dataset into training (70%) and testing (30%) using the accuracy and F1 score as performance metrics.” (p. 11, seção 2 Sentinel-1 SAR 10 m VV – HH – VV + VH 2017, 2019)
- “This fixed mapping (e.g., “Cluster 1” = “Forest”) was then applied to the unseen 30% test set to calculate the final accuracy and F1 scores reported in Table 7.” (p. 11, seção 2 Sentinel-1 SAR 10 m VV – HH – VV + VH 2017, 2019)
- “Supervised model In Experiment 1 (optical-only classification with Sentinel-2), U-Net generally outperformed PSPNet across most metrics, achieving higher test accuracies (above 93%) and mIoU scores (above 80%).” (p. 12, seção Results)
- “For example, U-Net with a ResNet-18 encoder achieved a test accu racy of 94.2% and a test mIoU of 82.1%, whereas PSPNet with the same encoder reached 91.7% accu racy and 75.4% mIoU.” (p. 12, seção Results)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “Additionally, exploring learned up-sampling or multiscale fusion strategies could further improve robustness and will be investigated in future work.” (p. 11, seção 2 Sentinel-1 SAR 10 m VV – HH – VV + VH 2017, 2019, 2021)
- “197 Page 12 of 27 confidence-thresholded pseudo-labeling is a standard SSL practice and will be incorporated in future work (Sohn et al., 2020).” (p. 12, seção 10 to 90% unlabeled. Pseudo-labels for the unlabeled)
- “In contrast, standard k-means had the lowest performance (mean test accuracy 79.2% and F1 77.3%), suggesting it struggled to segregate the complex feature space as effectively.” (p. 22, seção Discussion)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 7)
- declaração: “This selection was driven by the program’s data availability structure and the objective to minimize cloud cover artifacts.” (p. 7)
- declaração: “Data availability No datasets were generated or analysed during the current study.” (p. 25)
- hiperparâmetros **não detectados** automaticamente: perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Persistência / confirmação 2 (p. 2); Custo 2 (p. 23, 24); Rastreabilidade 1 (p. 8)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[SAR|Radar (SAR)]] — 42 ocorrências (p. 1, 2, 3, 5, 7)
- utiliza dado/sensor: [[PlanetScope|PlanetScope (Dove/SuperDove)]] — 13 ocorrências (p. 7, 8, 10, 12, 22)
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 12 ocorrências (p. 7, 8, 10, 12, 18)
- utiliza método: [[UNet|U-Net]] — 47 ocorrências (p. 1, 5, 7, 10, 12)
- utiliza método: [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 28 ocorrências (p. 1, 2, 3, 5, 7)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 4 ocorrências (p. 5, 22, 23)
- é avaliado por: [[IoU|IoU / mIoU]] — 53 ocorrências (p. 1, 10, 11, 12, 13)
- é avaliado por: [[F1|F1]] — 17 ocorrências (p. 11, 13, 14, 15, 18)
- é avaliado por: [[AcuraciaGlobal|Acurácia global (OA)]] — 12 ocorrências (p. 1, 10, 11, 13, 14)
- usa ferramenta: [[GoogleEarthEngine|Google Earth Engine]] — 8 ocorrências (p. 7, 8)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 62 ocorrências (p. 1, 2, 3, 8, 10)
- aplica etapa de preparo: [[MosaicosCompostos|Mosaicos e compostos temporais]] — 21 ocorrências (p. 7, 8)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 13 ocorrências (p. 2, 8, 10, 12, 15)
- aplica etapa de preparo: [[MascaraNuvem|Máscara de nuvem e sombra]] — 10 ocorrências (p. 2, 7, 24, 25)
- aplica etapa de preparo: [[IndicesEspectrais|Índices espectrais (NDVI etc.)]] — 9 ocorrências (p. 10, 11, 13)
- adota desenho de validação: [[DivisaoTreinoTeste|Divisão treino/validação/teste]] — 7 ocorrências (p. 10, 11)
- adota desenho de validação: [[Generalizacao|Generalização e domain shift]] — 7 ocorrências (p. 2, 9, 12, 15, 23)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[ClassificacaoCobertura|Classificação de cobertura e uso da terra]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
