---
tipo: artigo
id_origem: P103
titulo: "TEMPO: Global Temporal Building Density and Height Estimation from Satellite Imagery"
ano: 2025
autores: ["Tammy Glazer", "Gilles Hacheme", "Akram Zaytar", "Marotti, Luana", "Michaels, Amy", "Girmaw Abebe Tadesse", "White, Kevin", "Rahul Dodhia"]
doi: "10.48550/arXiv.2511.12104"
arquivo_fonte: "coleta/P103_Glazer2025_TEMPO-Global-Temporal-Building-Density-and-Height-Estimation.pdf"
markdown_fonte: "output/pdf/P103_Glazer2025_TEMPO-Global-Temporal-Building-Density-and-Height-Estimation/document.md"
paginas: 17
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "A"
tarefas: ["[[Edificacoes|Edificações e urbanização]]", "[[SITS|Séries temporais de imagens (SITS)]]"]
sensores: ["[[PlanetProdutos|Produtos Planet (visão geral)]]", "[[Sentinel2|Sentinel-2]]"]
conjuntos_dados: ["[[SpaceNet7_MUDS|SpaceNet 7 / MUDS]]"]
metodos: ["[[UNet|U-Net]]", "[[SupervisaoFraca|Supervisão fraca]]"]
preparo: ["[[MascaraNuvem|Máscara de nuvem e sombra]]"]
validacao: ["[[F1|F1]]"]
ferramentas: []
tags: [artigo, leitura/profunda, relevancia/A]
---

# Glazer 2025 — TEMPO: Global Temporal Building Density and Height Estimation from Satellite Imagery

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **A** — Basemaps Planet de 4,7 m trimestrais; densidade e altura de edificações; F1 de presença de 0,85–0,88, sem acurácia de mudança.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Tammy Glazer, Gilles Hacheme, Akram Zaytar, Marotti, Luana et al. (2025). TEMPO: Global Temporal Building Density and Height Estimation from Satellite Imagery. arXiv (Cornell University). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2511.12104
- **Arquivo de origem:** `coleta/P103_Glazer2025_TEMPO-Global-Temporal-Building-Density-and-Height-Estimation.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P103_Glazer2025_TEMPO-Global-Temporal-Building-Density-and-Height-Estimation/document.md` — 17 páginas, 8 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Gerar o **TEMPO**, um conjunto global e trimestral de **densidade e altura de edificações** a partir de **basemaps PlanetScope RGB de 4,7 m**, com uma U-Net multitarefa, e usá-lo para detectar **crescimento construído** em séries de 2020 a 2025 (p. 1–2). A saída é de 37,6 m por pixel (blocos de 8 × 8 pixels) e a mudança é derivada dos mapas por data, não de um modelo de mudança.

**Resumo detectado automaticamente (p. 1):** We present TEMPO, a global, temporally resolved dataset of building density and height derived from high-resolution satellite imagery using deep learning models. We pair building footprint and height data from existing datasets with quarterly PlanetScope basemap satellite images to train a multi-task deep learning model that predicts building density and building height at a 37.6-meter per pixel resolution. We apply this model to global PlanetScope basemaps from Q1 2018 through Q2 2025 to create global, temporal maps of building density and height. We validate these maps by comparing against existing building footprint datasets. Our estimates achieve an F1 score between 85% and 88% on different hand-labeled subsets, and are temporally stable, with a 0.96 five-year trend-consistency score. TEMPO captures quarterly changes in built settlements at a fraction of the computational cost of com…

- “We present TEMPO, a global, temporally resolved dataset of building density and height derived from high-resolution satellite imagery using deep learning models.” (p. 1, seção Abstract)
- “In this paper, we introduce TEMPO, the first quarterly updated, global building dataset at a 37.6-meter spatial resolution derived from satellite imagery.” (p. 2, seção 1 Introduction)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “For images captured between 2019 and 2021, UDMs are 8-bit images that encode pixel clarity.” (p. 2, seção 2 Data)
- “For example, according to data derived 1 Note: RapidEye imagery is used in global basemaps generated between 2019 and 2020.” (p. 2, seção 2 Data)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- **Planet quarterly visual basemaps** (RGB, 8 bits, 4,7 m, quads de 4096 × 4096); a Planet mistura as melhores cenas de 3 meses. Limitações listadas: latência temporal, artefatos de mosaico, diferenças de calibração e ângulo, e **mudanças nos algoritmos de composição da Planet (nitidez e super-resolução desde 2022), que criam deslocamento de distribuição** (p. 2–3).
- **UDM** (máscara de dados utilizáveis) a partir do 3º trimestre de 2019; em 2023, 16 % dos quads globais tinham nuvem e 0,43 % dos pixels eram nublados (p. 2–3).
- **Rótulos fracos:** Google Open Buildings 2.5D (anual, Sentinel-2) como rótulo e **Overture Maps** como canal de prior; Microsoft/OSM, GHSL, WSF e GBA para alinhamento e validação (p. 3–5, 11).

**Detectado automaticamente (verificar):**
- sensor/produto **PlanetScope**: 20 ocorrências (p. 1, 2, 3, 5, 6)
- sensor/produto **Planet (mosaicos e cenas)**: 17 ocorrências (p. 2, 3, 5, 6, 7)
- sensor/produto **Sentinel-2**: 6 ocorrências (p. 3, 4, 15)
- sensor/produto **SAR**: 2 ocorrências (p. 3, 4)
- conjunto de dados **SpaceNet 7 (MUDS)**: 10 ocorrências (p. 4, 5, 10, 12)
- conjunto de dados **OpenStreetMap**: 7 ocorrências (p. 2, 3, 4, 5)
- “These challenges are compounded by uneven data availability across regions, where ground truth are disproportionately concentrated in wealthier and urbanized regions leaving vast, resource constrained areas underrepresented.” (p. 2, seção 1 Introduction)
- “F1 is well-suited for comparing against reference datasets that are available only at specific timestamps or at coarser spatial resolutions, and is robust in the presence of strong class imbalance.” (p. 9, seção 3 Density values > 2 / 255 are considered to represent a val)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 22 ocorrências (p. 2, 3, 4, 5, 6)
- **Rotulagem / anotação**: 15 ocorrências (p. 1, 2, 5, 6, 9)
- **Reamostragem**: 8 ocorrências (p. 4, 5, 6, 7, 12)
- **Normalização / escala**: 6 ocorrências (p. 3, 4, 5, 6, 8)
- **Aumento de dados**: 6 ocorrências (p. 6, 10, 11)
- **Mosaicos e compostos**: 4 ocorrências (p. 2, 4, 15)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Método:**

- **U-Net com EfficientNet-B6 (ImageNet)**, entrada de 4 canais (RGB + prior de densidade Overture), pooling médio 8 × 8 e duas cabeças 1 × 1 (densidade e altura) (p. 6).
- **Perda de Huber** (δ = 0,7) sobre ativação **hard sigmoid**; amostragem de quads **proporcional à densidade** de edificações; **janela aleatória apagada no canal de prior** (spatial dropout) para o modelo não depender dele; mistura de anos e trimestres em cada lote (p. 6).
- Treino: AdamW, lr 1,4e-3, lote 64, 1.200 épocas com cosseno; **≈ 2 % dos quads globais**, 1 % desses para validação, **divisão por quad (blocos espaciais)**; 72 horas de A100 (p. 6–7).
- **Pós-processamento:** agregação em **janela deslizante de 4 trimestres** (≥ 3 datas com edificação → mediana; ≥ 3 sem → 0; senão máximo ou 0 conforme a clareza do pixel pelo UDM), máscara de água (GSW) e de altitude > 5.100 m, mínimo de altura de 2,4 m (p. 7–8, algoritmo 1).
- Inferência global: 916.400 quads e 130 GPUs V100 (p. 8).

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 10 menções vs 1 de pares)
**Métodos detectados automaticamente:**
- método/família **U-Net**: 6 ocorrências (p. 6, 10, 15)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 1 ” (p. 6)
- batch: “batch size of 64” (p. 6)
- otimizador: “AdamW” optimizer with a tuned learning rate o” (p. 6)
- tamanho do patch: “4096 x 4096 pixel” (p. 2)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 3 ocorrências (p. 6, 7, 11)
- métrica **F1**: 15 ocorrências (p. 1, 9, 11, 12)
- métrica **Precisão/Recall**: 11 ocorrências (p. 8, 9, 12)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Métricas e resultados:**

- **Ablações** (p. 10–11): o modelo completo tem a menor perda (2,19e-4); remover o prior Overture ou usar só o prior causa as maiores perdas; duas cabeças e amostragem ponderada ajudam; conclusão dos autores: **a qualidade de rótulos e entradas pesa mais que a arquitetura**.
- **F1 de detecção contra referências** (tabela 3, p. 11): TEMPO-PP 0,87 contra Google 2.5D e 0,80 contra Overture; sem pós-processamento 0,85–0,86.
- **SpaceNet 7** (tabela 4, p. 12): F1 de presença de edificação 0,88 (Global South) e 0,85 (todos), com TEMPO-PP; TEMPO bruto 0,85 e 0,81. Overture tem a maior precisão (0,96) e GHSL o maior recall (0,98).
- **Estabilidade temporal** (tabela 5, p. 13): correlação anual 0,995–0,998 e AUC de monotonicidade 0,833–0,963 para TEMPO-PP, acima de Google 2.5D (0,701–0,896). O resumo cita "0,96 de consistência de tendência em 5 anos".
- **Estudos de caso de mudança** (p. 14–15): crescimento de Dallas–Fort Worth (limiar no percentil 95 do ganho de volume entre 2020 e 2025, polígonos com conectividade 8) e acampamento de refugiados Métché (Chade, criado no fim de 2023). Os casos são qualitativos, comparados com notícias e relatórios, **sem acurácia de mudança**.

**Trechos numéricos detectados automaticamente (verificar):**
- “Our estimates achieve an F1 score between 85% and 88% on different hand-labeled subsets, and are temporally stable, with a 0.96 five-year trend-consistency score.” (p. 1, seção Abstract)
- “The inference workflow consists of running the model on nearly 1PB of quarterly PlanetScope basemap imagery from Q1 2018 through Q2 2025 with post-processing to improve temporal consistency. from Planet’s Q3 2023 UDMs, 16% of global basemap quads contain cloud” (p. 3, seção 2 Data)
- “Upper table: detection (F1 at 1% threshold); lower table: regression (MAE in % for density, m for height).” (p. 11, seção 4 Results)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites declarados e observações:**

- Rótulos fracos herdam vieses espaciais; pode precisar de ajuste local; RGB de 4,7 m perde estruturas pequenas, de baixo contraste ou isoladas ("viés de dificuldade" contra moradias tradicionais); altura piora nas caudas; **reduções por dano ou demolição se confundem com sazonalidade e artefatos**; a agregação de 4 trimestres **atrasa a detecção de novas construções em até um trimestre** (p. 15).
- **Observações minhas:** (a) a validação mede **presença de edificação** (F1 de 0,85–0,88), **não a mudança**; para mudança só há dois estudos de caso; (b) o F1 é calculado com limiar de 1 % de densidade num pixel de 37,6 m, um critério bem mais tolerante que detecção de polígono; (c) as referências usadas como "verdade" são produtos modelados, não campo; (d) a estabilidade temporal alta pode refletir apenas a suavização de 4 trimestres e a baixa taxa de mudança real; (e) o artigo reconhece o deslocamento de distribuição por mudanças de processamento da Planet, o que importa para qualquer série de basemaps.

**Trechos detectados automaticamente (verificar contexto):**
- “Even state-of-the-art building datasets struggle to achieve consistent performance across visually diverse geographies. .” (p. 2, seção 1 Introduction)
- “While PlanetScope visual basemaps are designed to provide consistent, high-resolution global imagery, they come with limitations for analytical use.” (p. 2, seção 2 Data)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- Dados parciais em github.com/microsoft/buildings (densidade e altura globais de Q4 2023 a 100 m e séries trimestrais de cinco regiões) (p. 2). Código de treino não informado no trecho lido. Pipeline reproduzível com Sentinel-2 em resolução menor (p. 15).

- **Código/dados:** sim: github.com/microsoft/buildings (p. 2)
- URL citada: https://github.com/microsoft/buildings (p. 2)
- declaração: “These challenges are compounded by uneven data availability across regions, where ground truth are disproportionately concentrated in wealthier and urbanized regions leaving vast, resource constrained areas underrepresented.” (p. 2)
- declaração: “Globally, the combined dataset contains 2.3 billion footprints and is the most comprehensive open-source set of building footprint data.” (p. 4)
- hiperparâmetros **não detectados** automaticamente: épocas/iterações, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** série retrospectiva com aviso de latência. Série trimestral de 2020 a 2025; a janela de 4 trimestres atrasa a detecção em até um trimestre.
- menções de termos de monitoramento (contagem, não avaliação): Quase tempo real 2 (p. 2); Latência / frequência 2 (p. 2, 15); Custo 2 (p. 1, 15); Sistema operacional 1 (p. 8)

**Interpretação — O que reaproveitar:**

- **Pós-processamento com janela de 4 datas e UDM** (voto de maioria com clareza do pixel) como filtro de falsos positivos em séries de basemaps, ao custo de um trimestre de atraso.
- **Prior de footprints + dropout espacial do prior** para reduzir dependência de dados externos.
- **Validação sem verdade de campo:** alinhamento entre produtos, estabilidade temporal (correlação, AUC de monotonicidade) e SpaceNet 7.
- **Máscaras auxiliares:** água (GSW) e altitude para cortar falsos positivos.
- **Amostragem proporcional à densidade** do alvo para treinar com poucos exemplos positivos.

**Interpretação — Cuidados para o nosso projeto:**

- O produto estima **estoque de edificações por data**; a mudança sai da diferença de mapas e herda erro dos dois.
- Pixel de saída de 37,6 m: serve para aviso de expansão, não para localizar a obra individual.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[PlanetProdutos|Produtos Planet (visão geral)]] — 17 ocorrências (p. 2, 3, 5, 6, 7)
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 6 ocorrências (p. 3, 4, 15)
- emprega conjunto de dados: [[SpaceNet7_MUDS|SpaceNet 7 / MUDS]] — 10 ocorrências (p. 4, 5, 10, 12)
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[SITS|Séries temporais de imagens (SITS)]] — suporte vindo da leitura/título/resumo
- utiliza método: [[UNet|U-Net]] — 6 ocorrências (p. 6, 10, 15)
- referência (curado pela leitura): [[SupervisaoFraca|Supervisão fraca]] — suporte vindo da leitura/título/resumo
- referencia (suporte manual da leitura): [[PosProcessamentoTemporal|Pós-processamento temporal (persistência, janela e colapso)]] — suporte vindo da leitura/título/resumo
- aplica etapa de preparo: [[MascaraNuvem|Máscara de nuvem e sombra]] — 3 ocorrências (p. 2, 3)
- é avaliado por: [[F1|F1]] — 15 ocorrências (p. 1, 9, 11, 12)

**Comparações substantivas com outros artigos:**
- este artigo valida com o benchmark de [[Etten_2021_SpaceNetMultiTemporal|Etten 2021]] — P103 valida a presença de edificação no SpaceNet 7 (F1 0,85–0,88, p. 12), sem medir a mudança.

## Figuras selecionadas

![[Glazer_2025_TEMPOGlobalTemporal_p3_Figure2.png|520]]
*Figure 2: Our methods are split into a training workflow ( top ) and inference workflow ( bottom ). The training (p. 3; recorte do PDF convertido)*

![[Glazer_2025_TEMPOGlobalTemporal_p7_Figure4.png|520]]
*Figure 4: Examples of Planet quarterly imagery for 2023, digital elevation model data, water masks, UDMs, (p. 7; recorte do PDF convertido)*

![[Glazer_2025_TEMPOGlobalTemporal_p5_Figure3.png|520]]
*Figure 3: SpaceNet7 building density labels by geographic location. (p. 5; recorte do PDF convertido)*


## Anotações do leitor

- 
