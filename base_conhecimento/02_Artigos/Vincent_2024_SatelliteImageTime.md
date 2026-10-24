---
tipo: artigo
id_origem: P13
titulo: "Satellite Image Time Series Semantic Change Detection: Novel Architecture and Analysis of Domain Shift"
ano: 2024
autores: ["Elliot Vincent", "Jean Ponce", "Mathieu Aubry"]
doi: "10.48550/arXiv.2407.07616"
arquivo_fonte: "coleta/P13_Vincent2024_Satellite-Image-Time-Series-Semantic-Change-Detection-Novel-.pdf"
markdown_fonte: "output/pdf/P13_Vincent2024_Satellite-Image-Time-Series-Semantic-Change-Detection-Novel-/document.md"
paginas: 17
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "A"
tarefas: ["[[SITS|Séries temporais de imagens (SITS)]]", "[[MudancaSemantica|Mudança semântica (from–to)]]"]
sensores: []
conjuntos_dados: ["[[SpaceNet7_MUDS|SpaceNet 7 / MUDS]]", "[[DynamicEarthNet|DynamicEarthNet]]"]
metodos: ["[[UTAE|U-TAE (U-Net com atenção temporal)]]", "[[Transformer|Transformers]]"]
preparo: []
validacao: ["[[Generalizacao|Generalização e domain shift]]", "[[Desbalanceamento|Desbalanceamento de classes]]"]
ferramentas: []
tags: [artigo, leitura/profunda, relevancia/A]
---

# Vincent 2024 — Satellite Image Time Series Semantic Change Detection: Novel Architecture and Analysis of Domain Shift

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **A** — Séries Planet (DynamicEarthNet e MUDS) com validação contra shift espacial e temporal.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Elliot Vincent, Jean Ponce, Mathieu Aubry (2024). Satellite Image Time Series Semantic Change Detection: Novel Architecture and Analysis of Domain Shift. arXiv (Cornell University). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2407.07616
- **Arquivo de origem:** `coleta/P13_Vincent2024_Satellite-Image-Time-Series-Semantic-Change-Detection-Novel-.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P13_Vincent2024_Satellite-Image-Time-Series-Semantic-Change-Detection-Novel-/document.md` — 17 páginas, 144 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Arquitetura para **mudança semântica em séries temporais (SITS-SCD)** e uma análise do efeito de **domain shift espacial e temporal**. O trabalho mostra que a avaliação "no mesmo lugar e período" superestima o desempenho.

**Resumo detectado automaticamente (p. 1):** Satellite imagery plays a crucial role in monitoring changes happening on Earth’s surface and aiding in cli- mate analysis, ecosystem assessment, and disaster response. In this paper, we tackle semantic change detection with satellite image time series (SITS-SCD) which encompasses both change detection and semantic segmentation tasks. We propose a new architecture that improves over the state of the art, scales better with the number of parameters, and leverages long-term temporal information. However, for practical use cases, models need to adapt to spatial and temporal shifts, which remains a challenge. We investi- gate the impact of temporal and spatial shifts separately on global, multi-year SITS datasets using DynamicEarth- Net [ 43 ] and MUDS [ 44 ]. We show that the spatial do- main shift represents the most complex setting and that the impact of temporal shift on performance is m…

- “In this paper, we tackle semantic change detection with satellite image time series (SITS-SCD) which encompasses both change detection and semantic segmentation tasks.” (p. 1, seção Abstract)
- “We propose a new architecture that improves over the state of the art, scales better with the number of parameters, and leverages long-term temporal information.” (p. 1, seção Abstract)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The data from the 2021 IEEE GRSS Data Fusion Contest [ 23 ] contains time series but only extreme dates have annotations, the challenge focusing more on knowledge transfer from low to high resolution rather than SITS-SCD.” (p. 3, seção 2. Related work)
- “DynamicEarthNet and MUDS contain 2year image time series from January 2018 to December 2019.” (p. 5, seção 3.2. Analysis methodology)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- DynamicEarthNet (55 séries diárias com 6 classes, Planet, 3 m) e MUDS (60 séries mensais RGB com polígonos de edificação convertidos em máscara binária edifício/não, 18–24 imagens por série) (p. 5, 6).

**Detectado automaticamente (verificar):**
- conjunto de dados **SpaceNet 7 (MUDS)**: 31 ocorrências (p. 1, 3, 4, 5, 6)
- conjunto de dados **DynamicEarthNet**: 25 ocorrências (p. 1, 3, 4, 5, 6)
- “For data augmentation, we randomly crop image patches of size 128 × 128 out of the 1024 × 1024 images and additionally do random horizontal and vertical flips as well as random rotations.” (p. 5, seção 3.3. Training and implementation details)
- “Due to an excessive amount of clouds or haze some images were excluded from the dataset, causing a few gaps in some of the time series, with length ranging from 18 to 24 images per SITS.” (p. 6, seção 2 https://spacenet.ai/sn7-challenge/)
- “We evaluate our method along with baselines on DynamicEarthNet [ 43 ] and MUDS [ 44 ] datasets and more precisely on their training set for which ground truth annotations are available.” (p. 5, seção 4.1. Datasets and metrics)
- “The first day of each month is annotated, leading to 24 ground truth segmentation maps per area of interest (AoI).” (p. 6, seção 2 https://spacenet.ai/sn7-challenge/)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 14 ocorrências (p. 1, 3, 5, 6, 8)
- **Recorte em patches/tiles**: 6 ocorrências (p. 3, 4, 5)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Método:**

- Modificação do **U-TAE:** em vez de agregar o tempo, a atenção temporal produz **um mapa de segmentação por imagem de entrada**; pesos de atenção T × T por pixel do nível mais baixo (produto de matrizes de chaves e consultas), propagados por skip connections; decoder em paralelo em todas as datas; L = 4 níveis, D = 512, d = 4 (p. 3, 4, 5).
- Treino: perda focal, AdamW com aquecimento até 1e-4 em 5.000 iterações, 500.000 iterações, melhor checkpoint por SCS de validação; crops de 128 × 128 de imagens 1024²; flips e rotações; amostra 12 imagens mensais de 24 (6 de 12 no shift temporal); **inferência com a série completa** (p. 5).

**Evidência (leitura) — Baselines comparados:**

UTAE e TSViT (mono-temporais, mensal/semanal), A2Net e SCanNet (pares), TSSCD (pixel a pixel), mais um baseline aleatório (p. 6, 7).

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 156 menções vs 34 de pares)
**Métodos detectados automaticamente:**
- método/família **U-TAE**: 16 ocorrências (p. 2, 3, 6, 7, 8)
- método/família **U-Net**: 3 ocorrências (p. 2, 6)
- método/família **Transformer**: 3 ocorrências (p. 2, 6, 7)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate starting from 0 and gradually reaching 10 [−] as ” (p. 5)
- épocas/iterações: “5000 iterations” (p. 5)
- otimizador: “AdamW optimizer [ 28 ] with a learning rate s” (p. 5)
- perda: “focal loss [ 25 ] and the AdamW optimizer [ 28 ] w” (p. 5)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Evidência (leitura) — Os três regimes de partição (o ponto mais reaproveitável):**

1. **Sem shift:** cada série dividida em 4 subconjuntos (2 treino, 1 val, 1 teste), validação cruzada em 4 folds; as áreas se sobrepõem entre folds (p. 4).
2. **Shift temporal:** treino em 2018, validação e teste em 2019 (p. 5).
3. **Shift espacial:** áreas divididas em 5 subconjuntos (3 treino, 1 val, 1 teste), 5 folds; folds aleatórios no MUDS e balanceados por classe no DynamicEarthNet; é o regime usado nos desafios DynamicEarthNet e SpaceNet 7 (p. 5).

**Detectado automaticamente (verificar):**
- **Teste externo / generalização**: 50 ocorrências (p. 1, 2, 3, 4, 5)
- **Divisão temporal**: 21 ocorrências (p. 1, 2, 3, 4, 5)
- **Divisão espacial**: 17 ocorrências (p. 1, 2, 3, 4, 5)
- **Validação cruzada**: 3 ocorrências (p. 4, 5)
- **Conjuntos treino/val/teste**: 3 ocorrências (p. 4, 5)
- **Desbalanceamento**: 2 ocorrências (p. 2, 10)
- métrica **IoU**: 12 ocorrências (p. 6, 7, 8, 9)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Resultados:**

- DynamicEarthNet, sem shift: SCS 31,7 (SC 41,0; BC 22,4; mIoU 60,5), contra 26,7 do UTAE semanal e 12,0 do TSSCD pixel a pixel (p. 5).
- Shift espacial: SCS cai 39,0 % (DynamicEarthNet) e 20,7 % (MUDS); mIoU cai 31,9 % e 10,5 %. A classe superfície impermeável cai só 23 % contra 49,7 % das outras (p. 9).
- Shift temporal afeta sobretudo a **mudança** e pouco a segmentação (p. 9).
- BC < 23 % em todos os métodos; só 1,28 % (DEN) e 0,03 % (MUDS) dos pixels mudam por mês. No MUDS nenhum método supera claramente o aleatório no SCS (p. 10).
- **Quanto mais longa a série na inferência, melhor** (6, 8, 12, 24); sub-séries que cobrem os 24 meses superam fatias consecutivas (p. 8).

**Trechos numéricos detectados automaticamente (verificar):**
- “For all evaluated methods, we observe an average relative drop of the mIoU from the setting without domain shift to the spatial shift setting of 31.9% on DynamicEarthNet and of 10.5% on MUDS.” (p. 9, seção 4.3. Results)
- “The SCS score similarly decreases by 39.0% on DynamicEarthNet and by 20.7% on MUDS.” (p. 9, seção 4.3. Results)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites e cuidados:**

- Apenas 2 anos; o shift temporal avaliado é de 1 ano.
- No MUDS (edificações pequenas em RGB) o resultado fica próximo do acaso em SCS: expectativa realista para edificações em Planet.

**Trechos detectados automaticamente (verificar contexto):**
- “To overcome this limitation, another approach is to classify pairs of pixels with transition labels, considering all possible pairs of semantic classes [ 4 ].” (p. 2, seção 2. Related work)
- “4.3.3 Limits of current methods and future work Binary change detection on DynamicEarthNet and MUDS is a challenging task.” (p. 9, seção 4.3. Results)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/ElliotVincent/SitsSCD (p. 1)
- URL citada: https://github.com/ElliotVincent/SitsSCD (p. 1)
- declaração: “Our complete code is available at [https:](https://github.com/ElliotVincent/SitsSCD) [//github.com/ElliotVincent/SitsSCD.](https://github.com/ElliotVincent/SitsSCD)” (p. 1)
- hiperparâmetros **não detectados** automaticamente: batch (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo. Avaliação com divisões fixas; o artigo argumenta que o monitoramento prático exige análise online (p. 1) e mede só o shift de um ano.
- menções de termos de monitoramento (contagem, não avaliação): Latência / frequência 6 (p. 2, 6, 7, 8); Quase tempo real 1 (p. 1)

**Interpretação — O que reaproveitar:**

- **Os três regimes de validação** como desenho oficial da etapa E03 Cubo espaço-temporal e partições: sem shift, shift temporal (ano futuro) e shift espacial (áreas inéditas), reportados lado a lado.
- **Inferência com a série completa** e treino com subamostragem aleatória de meses.
- **Arquitetura** como candidata do EXP5 (modelo de série temporal); código dos autores (SitsSCD) referenciado no artigo.
- Evidência de que **mudança rara** exige tratar a escassez de eventos (reamostragem, perda focal, métricas por evento).

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- emprega conjunto de dados: [[SpaceNet7_MUDS|SpaceNet 7 / MUDS]] — 31 ocorrências (p. 1, 3, 4, 5, 6)
- emprega conjunto de dados: [[DynamicEarthNet|DynamicEarthNet]] — 25 ocorrências (p. 1, 3, 4, 5, 6)
- trata a tarefa: [[SITS|Séries temporais de imagens (SITS)]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[MudancaSemantica|Mudança semântica (from–to)]] — suporte vindo da leitura/título/resumo
- utiliza método: [[UTAE|U-TAE (U-Net com atenção temporal)]] — 16 ocorrências (p. 2, 3, 6, 7, 8)
- utiliza método: [[Transformer|Transformers]] — 3 ocorrências (p. 2, 6, 7)
- referencia (suporte manual da leitura): [[MetricasMudancaSemantica|Métricas de mudança semântica (SeK, SCS, SCOT)]] — suporte vindo da leitura/título/resumo
- referencia (suporte manual da leitura): [[DivisaoEspacialBlocos|Divisão espacial por blocos e áreas]] — suporte vindo da leitura/título/resumo
- adota desenho de validação: [[Generalizacao|Generalização e domain shift]] — 50 ocorrências (p. 1, 2, 3, 4, 5)
- referência (curado pela leitura): [[Desbalanceamento|Desbalanceamento de classes]] — suporte vindo da leitura/título/resumo

**Comparações substantivas com outros artigos:**
- este artigo emprega o conjunto de dados e a métrica de [[Toker_2022_DynamicEarthNetDailyMulti|Toker 2022]] — P13 treina e testa em DynamicEarthNet e usa as métricas BC, SC, SCS e mIoU definidas por P12 (p. 6).
- este artigo emprega o conjunto de dados de [[Etten_2021_MultiTemporalUrban|Etten 2021]] — P13 usa o MUDS de P10 como segundo benchmark e gera mapas binários a partir dos polígonos (p. 6).
- este artigo compara-se com o baseline [[He_2024_TimeSeriesLand|He 2024]] — TSSCD (P14) é o baseline pixel a pixel de P13 (p. 7); obtém SCS 12,0 e 11,7 na Tabela 1 de P13.

## Figuras selecionadas

![[Vincent_2024_SatelliteImageTime_p4_Figure1.png|520]]
*Figure 1. Overall architecture. Given an input SITS, we compute feature maps at various scales. Our contribution is the temporal attention (p. 4; recorte do PDF convertido)*

![[Vincent_2024_SatelliteImageTime_p4_Figure2.png|520]]
*Figure 2. Attention mechanism of TAE, LTAE and our method. (p. 4; recorte do PDF convertido)*

![[Vincent_2024_SatelliteImageTime_p5_Figure3.png|520]]
*Figure 3. Domain shift settings. We organize the dataset splits (p. 5; recorte do PDF convertido)*


## Anotações do leitor

- 
