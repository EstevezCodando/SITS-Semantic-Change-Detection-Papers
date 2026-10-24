---
tipo: artigo
id_origem: P137
titulo: "A New Learning Paradigm for Foundation Model-Based Remote-Sensing Change Detection"
ano: 2024
autores: ["Kaiyu Li", "Xiangyong Cao", "Deyu Meng"]
doi: "10.1109/tgrs.2024.3365825"
arquivo_fonte: "coleta/P137_Li2024_A-New-Learning-Paradigm-for-Foundation-Model-Based-Remote-Se.pdf"
markdown_fonte: "output/pdf/P137_Li2024_A-New-Learning-Paradigm-for-Foundation-Model-Based-Remote-Se/document.md"
paginas: 13
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "B"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]"]
sensores: ["[[Landsat|Landsat]]"]
conjuntos_dados: ["[[LEVIRCD|LEVIR-CD]]", "[[S2Looking|S2Looking]]", "[[WHUCD|WHU-CD]]"]
metodos: ["[[ModeloFundacional|Modelos fundacionais]]", "[[Transformer|Transformers]]", "[[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]]", "[[TransferLearning|Aprendizado por transferência]]"]
preparo: []
validacao: ["[[Generalizacao|Generalização e domain shift]]"]
ferramentas: []
tags: [artigo, leitura/profunda, relevancia/B]
---

# Li 2024 — A New Learning Paradigm for Foundation Model-Based Remote-Sensing Change Detection

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **B** — Side-tuning de modelo fundacional congelado para poucos rótulos; RGB bitemporal.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Kaiyu Li, Xiangyong Cao, Deyu Meng (2024). A New Learning Paradigm for Foundation Model-Based Remote-Sensing Change Detection. IEEE Transactions on Geoscience and Remote Sensing. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1109/tgrs.2024.3365825
- **Arquivo de origem:** `coleta/P137_Li2024_A-New-Learning-Paradigm-for-Foundation-Model-Based-Remote-Se.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P137_Li2024_A-New-Learning-Paradigm-for-Foundation-Model-Based-Remote-Se/document.md` — 13 páginas, 103 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Como **reaproveitar o conhecimento de modelos fundacionais** (CLIP, RemoteCLIP, ViTs pré-treinados) para melhorar modelos de **detecção de mudanças bitemporal** que sofrem com poucos rótulos. Propõe o **BAN (Bi-Temporal Adapter Network)**, um arcabouço de *side-tuning* em que o modelo fundacional fica **congelado** e um ramo bitemporal treinável (Bi-TAB, qualquer modelo de mudança) recebe as características gerais por módulos de ponte (p. 1–2).

- “In this paper, we propose a Bi-Temporal Adapter Network (BAN), which is a universal foundation model-based CD adaptation framework aiming to extract the knowledge of foundation models for CD.” (p. 1, seção Início)
- “To alleviate the two issues, in this paper, we propose a universal framework, i.e., bi-temporal adapter networks (BAN for short), for tuning and adapting foundation models to the CD task.” (p. 2, seção I. I NTRODUCTION)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “It provides two annotated maps for each pair of images, indicating new and demolished building areas, which we use to generate a change map. • WHU-CD dataset contains a pair of images taken in the same area from 2012 and 2016, each with a s” (p. 6, seção IV. E XPERIMENTS)
- “With multiple types of annotations, the BANDON dataset can also be used for the SCD task. • The Landsat-SCD dataset consists of 8,468 image pairs collected between 1990 and 2020, each with a size of 416 × 416 and a spatial resolution of 30 ” (p. 7, seção IV. E XPERIMENTS)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- Cinco benchmarks RGB, todos **bitemporais e de alta ou média resolução**: **LEVIR-CD** (637 pares 1024², 0,5 m, Google Earth; 445/64/128), **S2Looking** (5.000 pares de visada lateral, 0,5–0,8 m), **WHU-CD** (recortes de 256²; 5.947/743/744), **BANDON** (aéreo fora do nadir, 0,6 m; 1.689/202/392; teste dividido em domínio interno e externo, de cidades diferentes) e **Landsat-SCD** (8.468 pares de 416² a **30 m**, 1990–2020, "sem mudança" + 10 tipos de mudança semântica) (p. 6–7).
- Nenhum dado de satélite de 3–5 m e nenhum Planet.

**Detectado automaticamente (verificar):**
- sensor/produto **Landsat**: 5 ocorrências (p. 7, 9)
- sensor/produto **Imagens aéreas**: 2 ocorrências (p. 7, 12)
- conjunto de dados **LEVIR-CD**: 11 ocorrências (p. 1, 6, 7, 8, 9)
- conjunto de dados **S2Looking**: 6 ocorrências (p. 6, 7, 8)
- conjunto de dados **WHU-CD**: 5 ocorrências (p. 6, 7, 9, 11)
- resolução mencionada: 0.5 m (p. 6)
- resolução mencionada: 0.8 m (p. 6)
- “To ensure standardized evaluation, the dataset is divided into three subsets: training, validation, and testing, containing 445, 64 and 128 image pairs. • S2Looking is a building CD dataset that contains large-scale side-looking satellite i” (p. 6, seção IV. E XPERIMENTS)
- “To better evaluate the generalization ability of models, the testing set is divided into an in-domain set and an out-domain set (collected from different cities) containing 207 and 185 image pairs.” (p. 7, seção IV. E XPERIMENTS)
- “With multiple types of annotations, the BANDON dataset can also be used for the SCD task. • The Landsat-SCD dataset consists of 8,468 image pairs collected between 1990 and 2020, each with a size of 416 × 416 and a spatial resolution of 30 ” (p. 7, seção IV. E XPERIMENTS)
- “Therefore, analyzing the time-series remote sensing (RS) data is an important topic in Earth vision, and change detection (CD) techniques have become an indispensable tool for this task, contributing to the comprehensive interpretation of s” (p. 1, seção I. I NTRODUCTION)
- “8, AUGUST 2023 6 𝑥 1 𝑥 2 ground truth BiT BAN-BiT CF BAN-CF (a) (b) (c) (d) (e) (f) (g) Fig.” (p. 6, seção III. M ETHOD)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 24 ocorrências (p. 1, 6, 7, 8, 9)
- **Recorte em patches/tiles**: 15 ocorrências (p. 2, 3, 5, 6, 7)
- **Aumento de dados**: 5 ocorrências (p. 1, 3, 7, 12)
- **Normalização / escala**: 3 ocorrências (p. 3, 5, 6)
- **Reamostragem**: 2 ocorrências (p. 2, 5)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Método:**

- **Três partes:** modelo fundacional congelado (principalmente o ViT-L/14 do CLIP), **Bi-TAB** (BiT, ChangeFormer ou blocos empilhados) e **módulos de ponte** (p. 1–4).
- **ARIS (resolução assimétrica):** o modelo fundacional recebe imagens redimensionadas à sua resolução de pré-treino (224 ou 336 px) e o Bi-TAB mantém 256² ou 512² (p. 4).
- **Ponte:** normaliza e projeta a característica geral, calcula uma **matriz de afinidade por cosseno** com a característica do Bi-TAB, reamostra o conhecimento geral por atenção e soma por resíduo (p. 5, equações 4–6).
- Perda: entropia cruzada por pixel; para mudança semântica o ChangeFormer ganha duas cabeças de segmentação (CF-SCD) (p. 5).
- Treino: **AdamW, lr 1e-4** (10× na cabeça do Bi-TAB), decaimento poly, batch 8, random crop 512², flips e distorção fotométrica; 40 mil iterações em LEVIR-CD e BANDON, 80 mil em S2Looking, 100 e 50 épocas em WHU-CD e Landsat-SCD; GPUs RTX 4090 e A6000 (p. 7).

- **Estratégia temporal (detecção automática, verificar):** bitemporal / pares (auto: 33 menções)
**Métodos detectados automaticamente:**
- método/família **Modelo fundacional**: 76 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Transformer**: 62 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Rede siamesa**: 15 ocorrências (p. 2, 3, 4, 5, 11)
- método/família **Semi/auto-supervisionado**: 12 ocorrências (p. 4, 7, 9, 10, 12)
- método/família **CNN**: 10 ocorrências (p. 1, 2, 3, 5, 13)
- método/família **Transfer learning**: 7 ocorrências (p. 3, 12)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate is set to 0.0001, and 10 × in Bi-TAB’s prediction ” (p. 7)
- batch: “batch size is set to 8” (p. 7)
- épocas/iterações: “50 epochs” (p. 7)
- otimizador: “AdamW optimizer” (p. 7)
- perda: “cross-entropy loss for BiT and ChangeFormer is adopte” (p. 5)
- tamanho do patch: “507 × 15,354 pixel” (p. 6)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 4 ocorrências (p. 6, 7)
- **Teste externo / generalização**: 4 ocorrências (p. 3, 7, 9, 12)
- métrica **IoU**: 41 ocorrências (p. 1, 7, 8, 9, 10)
- métrica **Precisão/Recall**: 14 ocorrências (p. 7, 9, 10, 11)
- métrica **Acurácia global**: 7 ocorrências (p. 7, 11)
- métrica **Kappa**: 4 ocorrências (p. 7)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Métricas e resultados:**

- Mudança binária: IoU, F1, OA **sobre a classe de mudança** (p. 7). Mudança semântica: mIoU, **SeK** e um **Score ponderado** (0,7 SeK + 0,3 mIoU) (p. 7).
- **LEVIR-CD:** BiT 82,25 → BAN-BiT 84,93 de IoU (+2,68); ChangeFormer b0 82,48 → BAN-CF-b0 84,94 (+2,46), F1 91,86; blocos empilhados 81,38 → 84,61 (+3,23) (p. 9, tabela I).
- **S2Looking:** BiT 46,80 → 48,63; CF-b1 47,68 → 50,04 (+2,36) de IoU (p. 9, tabela II).
- **BANDON (dentro do domínio):** BiT 44,43 → 53,08 (+8,65); no domínio externo BiT 35,24 → 47,20 (**+11,96**) e CF +6,00 (p. 8, 10, tabela III).
- **Landsat-SCD:** CF-SCD-b0 Score 62,08 → 63,62 e CF-SCD-b1 64,78 → 66,92; SeK 52,69 → 54,56 e 55,69 → 58,56 (p. 9, tabela IV). BANDON-SCD: SeK 27,95 → 31,48 (b0) e 33,49 → 35,20 (b2) (p. 9, tabela V).
- **Semissupervisionado (parte dos rótulos):** com 20 % dos rótulos do WHU-CD o BAN atinge IoU 81,05 %, 6,25 pontos acima do SemiCD; com 40 %, 85,26 %, +8,06 (p. 9–10).
- **Ablações:** resoluções 224/336/512 mudam pouco o IoU (84,63–84,94 no CLIP) mas o FPS cai de 2,86 para 0,71 imagem/s (p. 10, tabela VII); modelos pré-treinados em dados de sensoriamento remoto (RemoteCLIP, GeoRSCLIP) ficam ligeiramente à frente: IoU 85,05–85,13 vs 84,94 (CLIP) e 84,60 (ImageNet-21k) (p. 10, tabela VIII); Bi-TABs maiores dão ganhos de 2,46 a 3,21 de IoU (p. 11).


## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites declarados e observações:**

- O artigo mostra que o ganho vem **com poucos parâmetros extras** (de 2,99 M para 3,80 M no BiT) (p. 9), mas a inferência fica mais lenta: 0,71 a 2,86 imagens/s em A6000 com janela deslizante (p. 10).
- O ganho de LEVIR-CD é de ~2–3 pontos sobre uma base já em ~90 % de F1; a saturação do benchmark é o argumento da introdução (p. 1).
- Só imagens **RGB**; extensão a multiespectral é "trabalho futuro" (p. 11).
- **Observações minhas:** (a) todos os benchmarks são **bitemporais**; não há avaliação em série temporal nem em 3–5 m; (b) o melhor ganho (+11,96 de IoU) é em BANDON fora do domínio, mas a base de partida é fraca (35 %) e há uma só divisão; (c) as comparações com métodos "reimplementados" mostram que ganhos pequenos podem depender da reimplementação; (d) a tabela de semissupervisionado do texto extraído está ilegível; usei apenas os valores do texto corrido.


## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- Código no GitHub (`likyoo/BAN`) e integrado ao **Open-CD**, citados na p. 1; hiperparâmetros listados (p. 7).

- **Código/dados:** sim: github.com/likyoo/BAN (p. 1)
- URL citada: https://github.com/likyoo/BAN (p. 1)
- URL citada: https://github.com/likyoo/open-cd (p. 1)
- declaração: “More importantly, these successful practices show us the potential of foundation models for remote sensing CD. [The code is available at https://github.com/likyoo/BAN and will](https://github.com/likyoo/BAN) be supported in our Open-CD [†] ” (p. 1)
- declaração: “Deyu Meng is with the School of Mathematics and Statistics and Ministry of Education Key Lab of Intelligent Network Security, Xi’an Jiaotong University, Xi’an 710049, China (email: dymeng@mail.xjtu.edu.cn). - [An open source CD toolbox: htt” (p. 1)

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 2 (p. 3, 8)

**Interpretação — O que reaproveitar:**

- **Side-tuning com modelo fundacional congelado** como forma de usar embeddings de CLIP/RemoteCLIP/ImageNet-21k sem refinar o modelo todo, útil com poucos rótulos de mudança.
- **ARIS:** processar o modelo fundacional em baixa resolução e o ramo de mudança em alta, para controlar custo.
- **Métrica composta SeK + mIoU (Score 0,7/0,3)** para comparar mudança semântica quando há dois componentes.
- **Teste de domínio interno vs externo** (BANDON) como protocolo de generalização espacial.

**Interpretação — Cuidados para o nosso projeto:**

- Não há evidência em Planet; os modelos fundacionais vistos esperam **RGB** de 224–336 px, e nossos mosaicos têm 4 bandas e 3–5 m.
- Resultados bitemporais não validam estratégia de série temporal.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza método: [[ModeloFundacional|Modelos fundacionais]] — 76 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[Transformer|Transformers]] — 62 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 12 ocorrências (p. 4, 7, 9, 10, 12)
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 7 ocorrências (p. 3, 12)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- emprega conjunto de dados: [[LEVIRCD|LEVIR-CD]] — 11 ocorrências (p. 1, 6, 7, 8, 9)
- emprega conjunto de dados: [[S2Looking|S2Looking]] — 6 ocorrências (p. 6, 7, 8)
- emprega conjunto de dados: [[WHUCD|WHU-CD]] — 5 ocorrências (p. 6, 7, 9, 11)
- utiliza dado/sensor: [[Landsat|Landsat]] — 5 ocorrências (p. 7, 9)
- adota desenho de validação: [[Generalizacao|Generalização e domain shift]] — 4 ocorrências (p. 3, 7, 9, 12)

**Comparações substantivas com outros artigos:**
- este artigo compartilha a abordagem de modelo fundacional com [[Shen_2026_FoundationModelDriven|Shen 2026]] — P137 congela um modelo fundacional (CLIP) e P34 usa o PerA com decodificador modular; ambos em benchmarks bitemporais.

## Figuras selecionadas

![[Li_2024_NewLearningParadigm_p8_Fig.5.png|520]]
*Fig. 5. Visualization results (semantic segmentation auxiliary task) of different methods on the BANDON dataset. (p. 8; recorte do PDF convertido)*

![[Li_2024_NewLearningParadigm_p4_Fig.2.png|520]]
*Fig. 2. The detailed illustration of BAN. The foundation model (blue area) accumulates general knowledge through pre-training techniques, an (p. 4; recorte do PDF convertido)*

![[Li_2024_NewLearningParadigm_p5_Fig.2.png|520]]
*Fig. 2(b). (p. 5; recorte do PDF convertido)*


## Anotações do leitor

- 
