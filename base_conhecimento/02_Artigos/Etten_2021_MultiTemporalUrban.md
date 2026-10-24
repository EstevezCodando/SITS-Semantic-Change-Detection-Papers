---
tipo: artigo
id_origem: P10
titulo: "The Multi-Temporal Urban Development SpaceNet Dataset"
ano: 2021
autores: ["A. Van Etten", "Daniel Hogan", "Jesus Martinez-Manso", "Jacob Shermeyer", "Nicholas Weir", "Ryan Lewis"]
doi: "10.48550/arXiv.2102.04420"
arquivo_fonte: "coleta/P10_Etten2021_The-Multi-Temporal-Urban-Development-SpaceNet-Dataset.pdf"
markdown_fonte: "output/pdf/P10_Etten2021_The-Multi-Temporal-Urban-Development-SpaceNet-Dataset/document.md"
paginas: 10
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "A"
tarefas: ["[[Edificacoes|Edificações e urbanização]]", "[[SITS|Séries temporais de imagens (SITS)]]"]
sensores: ["[[PlanetProdutos|Produtos Planet (visão geral)]]"]
conjuntos_dados: ["[[SpaceNet7_MUDS|SpaceNet 7 / MUDS]]"]
metodos: ["[[UNet|U-Net]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]", "[[MascaraNuvem|Máscara de nuvem e sombra]]"]
validacao: ["[[F1|F1]]"]
ferramentas: []
tags: [artigo, leitura/profunda, relevancia/A]
---

# Etten 2021 — The Multi-Temporal Urban Development SpaceNet Dataset

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **A** — MUDS/SpaceNet 7: mosaicos Planet mensais de ~4 m com rótulos de edificação ao longo de 24 meses.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** A. Van Etten, Daniel Hogan, Jesus Martinez-Manso, Jacob Shermeyer et al. (2021). The Multi-Temporal Urban Development SpaceNet Dataset. IEEE Computer Society Conference on Computer Vision and Pattern Recognition. Tipo no catálogo: Dataset.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2102.04420
- **Arquivo de origem:** `coleta/P10_Etten2021_The-Multi-Temporal-Urban-Development-SpaceNet-Dataset.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P10_Etten2021_The-Multi-Temporal-Urban-Development-SpaceNet-Dataset/document.md` — 10 páginas, 18 recortes de figuras, 1 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Dataset e tarefa de **rastreamento de edificações em séries mensais Planet**: detectar todas as edificações de cada mês e manter o mesmo identificador ao longo do tempo, de modo a medir construção e demolição. É a referência mais próxima, em produto e resolução, de novas construções em mosaicos mensais de ~4 m.

**Resumo detectado automaticamente (p. 1):** Satellite imagery analytics have numerous human de- velopment and disaster response applications, particularly when time series methods are involved. For example, quan- tifying population statistics is fundamental to 67 of the 231 United Nations Sustainable Development Goals Indicators, but the World Bank estimates that over 100 countries cur- rently lack effective Civil Registration systems. To help ad- dress this deficit and develop novel computer vision meth- ods for time series data, we present the Multi-Temporal Urban Development SpaceNet (MUDS, also known as SpaceNet 7) dataset. This open source dataset consists of medium resolution (4.0m) satellite imagery mosaics, which includes ≈ 24 images (one per month) covering > 100 unique geographies, and comprises > 40 , 000 km of im- agery and exhaustive polygon labels of building footprints therein, totaling over 11M individual annotatio…

- “To help ad- dress this deficit and develop novel computer vision meth- ods for time series data, we present the Multi-Temporal Urban Development SpaceNet (MUDS, also known as SpaceNet 7) dataset.” (p. 1, seção Abstract)
- “To evaluate model performance on a time series of identifier-tagged footprints such as MUDS, we introduce a new evaluation metric: the SpaceNet Change and Object Tracking (SCOT) metric .” (p. 5, seção 4. Evaluation Metrics)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The Multi-Temporal Urban Development SpaceNet (MUDS) dataset consists of 101 labelled sequences of satellite imagery collected by Planet Labs’ Dove constellation between 2017 and 2020, coupled with building footprint labels for every image.” (p. 2, seção 3. Data)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- 101 áreas (AOIs) em 6 continentes, 2017–2020; mosaicos mensais Planet RGB de ~4 m ("global monthly basemaps"); 1024 × 1024 px (~18 km²); 41.250 km² no total; 18 a 26 meses por área (mediana 24); imagens muito nubladas foram excluídas, deixando lacunas (p. 2, 3).
- Licença CC BY-SA 4.0, no registro aberto da AWS (SpaceNet).

**Detectado automaticamente (verificar):**
- sensor/produto **Planet (mosaicos e cenas)**: 3 ocorrências (p. 2, 5)
- conjunto de dados **SpaceNet 7 (MUDS)**: 24 ocorrências (p. 1, 2, 3, 4, 5)
- resolução mencionada: 4.0 m (p. 1)
- resolução mencionada: 4 m (p. 7)
- “This open source dataset consists of medium resolution (4.0m) satellite imagery mosaics, which includes ≈ 24 images (one per month) covering > 100 unique geographies, and comprises > 40 , 000 km of im- agery and exhaustive polygon labels of” (p. 1, seção Abstract)
- “train the segmentation models with an Adam optimizer on the 1424 images of the training set for 300 epochs and a learning rate of 10 [−] (baseline) or 100 epochs and a learning rate of 2 × 10 [−] (EfficentNet).” (p. 7, seção 60 data cubes, testing on the remaining 41 data cubes. We)
- “ing “matches” between ground truth building footprints and proposal building footprints for each month.” (p. 6, seção 4. Evaluation Metrics)
- “A pair of footprints (one ground truth and one proposal) are eligible to be matched if their intersection over union (IOU) exceeds 0.25, and no footprint may be matched more than once.” (p. 6, seção 4. Evaluation Metrics)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Evidência (leitura) — Rótulos (o ponto mais reaproveitável):**

- Polígonos de edificação com **ID único persistente**; >11 milhões de rótulos, >500.000 edifícios; 10 a ~20.000 por imagem (média 4.600); área mediana 193 m² (≈12 px²) (p. 3).
- Duas camadas por imagem: polígonos de edificação e **UDM** (máscara de dado inutilizável) para nuvem e para erro de georreferenciamento >1 px (em casos raros as cenas têm desvios de 5–10 m) (p. 3).
- Definição: estrutura estática onde uma pessoa pode se abrigar, **sem tamanho mínimo** (p. 3).
- Procedimento: anotar a primeira imagem, **copiar os rótulos para a seguinte** e editar só com confiança de que o edifício surgiu/sumiu; usar o contexto temporal para descartar sombras e estruturas efêmeras (objeto que aparece e some várias vezes não é edifício) (p. 4, 5).
- Equipe: 7 meses, 5 pessoas; cada cubo é anotado por uma pessoa, revisado por outra e validado pelo líder. Mapa de alta resolução (privado) serviu de apoio ("rotulagem onisciente"), o que faz os rótulos conterem detalhe **não visível** nos 4 m (p. 4, 5).

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 37 ocorrências (p. 1, 2, 3, 4, 5)
- **Máscara de nuvem e sombra**: 3 ocorrências (p. 2, 5)
- **Mosaicos e compostos**: 2 ocorrências (p. 1, 2)
- **Recorte em patches/tiles**: 2 ocorrências (p. 2)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 41 menções vs 3 de pares)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 10 [−] (baseline) or 100 epochs and a learning” (p. 7)
- épocas/iterações: “300 epochs” (p. 7)
- otimizador: “Adam optimizer on the 1424 images of the tra” (p. 7)
- perda: “binary cross entropy” (p. 7)
- tamanho do patch: “1024 × 1024 pixel” (p. 3)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Evidência (leitura) — Métrica SCOT:**

- Casamento de polígonos com IoU > 0,25 (problema de atribuição; desempate pela soma de IoU) (p. 5).
- Termo de rastreamento (`F_track`): penaliza trocas de ID; termo de mudança (`F_change`): só edifícios novos. `SCOT = F-beta(β=2)` entre os dois, média sobre as áreas (p. 6).
- Vantagem sobre MOTA: um modelo estático (sem dependência do tempo) tem termo de mudança 0 (p. 6).

**Detectado automaticamente (verificar):**
- **Teste externo / generalização**: 2 ocorrências (p. 6)
- métrica **F1**: 13 ocorrências (p. 6, 7, 8)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Baseline e resultados:**

- U-Net com encoder VGG16 (perda Jaccard + 4·BCE) e com EfficientNet-B5 (Focal + Dice); 60 cubos para treino (1.424 imagens), 41 para teste; Adam; 300 épocas/lr 1e-4 (VGG16) e 100 épocas/lr 2e-4 (EfficientNet); instâncias por componente e IDs por IoU ≥ 0,25 com o mês anterior (p. 7).
- Resultados (edifícios ≥ 4 px²): F1 0,45 ± 0,13 / 0,42 ± 0,12; tracking 0,40 / 0,39; **mudança 0,06 / 0,07**; SCOT 0,17 / 0,18 (p. 7).
- Empilhar 5 datas na entrada não melhorou (SCOT 0,17 ± 0,08); VGG16 ≈ EfficientNet (p. 8).
- Edifícios isolados chegam a F1 0,55 / SCOT 0,31; áreas densas ficam em SCOT 0,07 (p. 7).

**Trechos numéricos detectados automaticamente (verificar):**
- “A pair of footprints (one ground truth and one proposal) are eligible to be matched if their intersection over union (IOU) exceeds 0.25, and no footprint may be matched more than once.” (p. 6, seção 4. Evaluation Metrics)
- “We select an IOU of 0.25 to mimic Equation 5 of ImageNet ), which sets IOU < 0 .” (p. 6, seção 4. Evaluation Metrics)
- “A pair of foot- 11 3 1 3 1 Time January Time January 12 12 11 13prints (one ground truth and one proposal) are eligible to be 11 13 February 3 1 2 February 3 1 2 13 12 3 4matched if their intersection over union (IOU) exceeds 0.25, March 1 2 March 1 2 12 3 4 1” (p. 6, seção 4. Evaluation Metrics)
- “We se- April 1 April 1 12 2 14 lect an IOU of 0.25 to mimic Equation 5 of ImageNet ), May 1 12 2 14 3 11 4 15 May 1 12 2 14 3 11 4 15 which sets IOU < 0.5 for small objects.” (p. 6, seção 4. Evaluation Metrics)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites declarados:**

- O termo de mudança é o mais difícil: identificar o mês de origem de cada edifício é não trivial e propostas espúrias são penalizadas.
- Objetos de 4–5 px e adensamento; foco em construção (demolição é rara no dataset).
- Rótulos "oniscientes" podem ensinar o modelo a prever o que o sensor não resolve; cuidado ao interpretar o F1.

**Trechos detectados automaticamente (verificar contexto):**
- “The closest comparison is the xView2 challenge and dataset , which examined building damage in satellite image pairs acquired before and after natural disasters ( i.e . only two timestamps) in < 20 locations; however, this task fails to add” (p. 2, seção 2. Related Work)
- “Since understanding time-dependence is usually a primary purpose of time series data, this is a serious drawback.” (p. 7, seção 4. Evaluation Metrics)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 1)
- declaração: “This open source dataset consists of medium resolution (4.0m) satellite imagery mosaics, which includes ≈ 24 images (one per month) covering > 100 unique geographies, and comprises > 40 , 000 km of im- agery and exhaustive polygon labels of” (p. 1)
- declaração: “The MUDS dataset is open sourced under a CC-BY4.0 ShareAlike International license [‡] to encourage broad use.” (p. 2)
- hiperparâmetros **não detectados** automaticamente: batch (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo. Dataset com rótulos oniscientes; não avalia atualização contínua.

**Interpretação — O que reaproveitar:**

- **Protocolo de rotulagem temporal** para construir nossos próprios rótulos mensais: copiar → editar → revisar com a série inteira, UDM de nuvem/co-registro e regra de exclusão de efêmeros.
- **SCOT** como métrica de identidade e de mudança por objeto na etapa E10 Avaliação e incerteza.
- **Particionamento por cubo (área inteira)** em vez de patches; **U-Net com encoder fixo** como baseline de edificações.
- **Faixas de tamanho**: avaliar apenas edifícios ≥ 4 px² e reportar por faixa.

**Interpretação — Cuidados para o nosso projeto:**

- O produto é RGB visual de ~4 m; não há NIR.
- Resultados de F1 de 0,45 são o patamar de referência para 4–5 px; não esperar mais em 5 m sem super-resolução.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[PlanetProdutos|Produtos Planet (visão geral)]] — 3 ocorrências (p. 2, 5)
- emprega conjunto de dados: [[SpaceNet7_MUDS|SpaceNet 7 / MUDS]] — 24 ocorrências (p. 1, 2, 3, 4, 5)
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[SITS|Séries temporais de imagens (SITS)]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[UNet|U-Net]] — suporte vindo da leitura/título/resumo
- referencia (suporte manual da leitura): [[RotulagemTemporal|Rotulagem temporalmente consistente]] — suporte vindo da leitura/título/resumo
- referencia (suporte manual da leitura): [[MetricasMudancaSemantica|Métricas de mudança semântica (SeK, SCS, SCOT)]] — suporte vindo da leitura/título/resumo
- referencia (suporte manual da leitura): [[DivisaoEspacialBlocos|Divisão espacial por blocos e áreas]] — suporte vindo da leitura/título/resumo
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 37 ocorrências (p. 1, 2, 3, 4, 5)
- aplica etapa de preparo: [[MascaraNuvem|Máscara de nuvem e sombra]] — 3 ocorrências (p. 2, 5)
- é avaliado por: [[F1|F1]] — 13 ocorrências (p. 6, 7, 8)

**Comparações substantivas com outros artigos:**
- [[Vincent_2024_SatelliteImageTime|Vincent 2024]] emprega o conjunto de dados de este artigo — P13 usa o MUDS de P10 como segundo benchmark e gera mapas binários a partir dos polígonos (p. 6).
- [[Toker_2022_DynamicEarthNetDailyMulti|Toker 2022]] compara-se, na descrição do dataset, com este artigo — P12 cita o MUDS como o dataset temporal mais próximo: (p. 2).
- [[Etten_2021_SpaceNetMultiTemporal|Etten 2021]] descreve o desafio construído sobre o conjunto de este artigo — P11 relata o desafio SpaceNet 7 sobre o MUDS de P10; o escore de mudança do campeão foi 0,20 (tabela 2, p. 9).

## Figuras selecionadas

![[Etten_2021_MultiTemporalUrban_p3_Figure2.png|520]]
*Figure 2: Location of MUDS data cubes. (p. 3; recorte do PDF convertido)*

![[Etten_2021_MultiTemporalUrban_p3_Figure1.png|520]]
*Figure 1: A comparison between our dataset and related (p. 3; recorte do PDF convertido)*

![[Etten_2021_MultiTemporalUrban_p4_Figure3.png|520]]
*Figure 3: Time series of two data cubes. Left column ( e.g . 1a) denotes the start of the times series, the middle column ( e.g . (p. 4; recorte do PDF convertido)*


## Anotações do leitor

- 
