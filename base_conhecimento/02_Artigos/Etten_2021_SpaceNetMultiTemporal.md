---
tipo: artigo
id_origem: P11
titulo: "The SpaceNet Multi-Temporal Urban Development Challenge"
ano: 2021
autores: ["A. Van Etten", "Hogan, Daniel"]
doi: "10.48550/arXiv.2102.11958"
arquivo_fonte: "coleta/P11_Etten2021_The-SpaceNet-Multi-Temporal-Urban-Development-Challenge.pdf"
markdown_fonte: "output/pdf/P11_Etten2021_The-SpaceNet-Multi-Temporal-Urban-Development-Challenge/document.md"
paginas: 15
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "A"
tarefas: ["[[Edificacoes|Edificações e urbanização]]", "[[SITS|Séries temporais de imagens (SITS)]]"]
sensores: ["[[PlanetProdutos|Produtos Planet (visão geral)]]"]
conjuntos_dados: ["[[SpaceNet7_MUDS|SpaceNet 7 / MUDS]]"]
metodos: ["[[UNet|U-Net]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]"]
validacao: ["[[Generalizacao|Generalização e domain shift]]"]
ferramentas: []
tags: [artigo, leitura/profunda, relevancia/A]
---

# Etten 2021 — The SpaceNet Multi-Temporal Urban Development Challenge

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **A** — Desafio SpaceNet 7: os cinco melhores métodos em Planet de ~4 m; escore de mudança do campeão de 0,20.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** A. Van Etten, Hogan, Daniel (2021). The SpaceNet Multi-Temporal Urban Development Challenge. arXiv (Cornell University). Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2102.11958
- **Arquivo de origem:** `coleta/P11_Etten2021_The-SpaceNet-Multi-Temporal-Urban-Development-Challenge.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P11_Etten2021_The-SpaceNet-Multi-Temporal-Urban-Development-Challenge/document.md` — 15 páginas, 18 recortes de figuras, 1 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Relatar o **SpaceNet 7 (Multi-Temporal Urban Development Challenge)**: localizar e **rastrear edificações** em séries mensais de mosaicos Planet de ~4 m sobre áreas em urbanização rápida, detectando construção e demolição (p. 1, 3, 5). Descreve os cinco melhores métodos entre mais de 300 participantes e analisa os resultados.

**Resumo detectado automaticamente (p. 1):** Building footprints provide a useful proxy for many humanitarian applications. For example, building footprints are useful for high fidelity population estimates, and quantifying population statistics is fundamental to ∼ 1 / 4 of the United Nations Sustainable Development Goals Indicators. In this paper we (the SpaceNet Partners) discuss efforts to develop techniques for precise building footprint localization, tracking, and change detection via the SpaceNet Multi-Temporal Urban Development Challenge (also known as SpaceNet 7). In this NeurIPS 2020 competition, participants were asked identify and track buildings in satellite imagery time series collected over rapidly urbanizing areas. The competition centered around a brand new open source dataset of Planet Labs satellite imagery mosaics at 4m resolution, which includes 24 images (one per month) covering ≈ 100 unique geographies. Tracki…

- “To evaluate model performance on a time series of identifier-tagged footprints, we introduce a new evaluation metric: the SpaceNet Change and Object Tracking (SCOT) metric.” (p. 5, seção 1 https://registry.opendata.aws/spacenet/)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The SpaceNet 7 Challenge used a brand-new, open source dataset of medium-resolution ( ≈ 4 m) satellite imagery collected by Planet Labs’ Dove Satellites between 2017 and 2020.” (p. 3, seção 7 Challenge.)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- **24 mosaicos mensais consecutivos (2017–2020) de 101 locais em 6 continentes**, ≈ 40.000 km², Dove Planet de ≈ 4 m, licença CC-BY-4.0 SA, na AWS (p. 3).
- Anotações manuais: **polígonos georreferenciados das edificações com identificador que persiste** na série, e **máscaras de dado inutilizável** (nuvem). Cada imagem de 1024 × 1024 tem de 10 a ≈ 20.000 edificações (média ≈ 4.600); total ≈ 11 M de anotações, ~500.000 edificações únicas (p. 3).
- **Rótulos "oniscientes":** feitos em 7 meses com apoio de imagens de resolução maior, então a precisão do rótulo **excede o que o olho vê em 4 m** (p. 3).
- **Divisão por local:** 60 locais para treino, 20 de teste público (só imagem) e 21 de teste privado; no total o teste tem 4,4 M de edificações (p. 3).

**Detectado automaticamente (verificar):**
- sensor/produto **Planet (mosaicos e cenas)**: 6 ocorrências (p. 1, 3, 10)
- conjunto de dados **SpaceNet 7 (MUDS)**: 26 ocorrências (p. 1, 2, 3, 5, 6)
- resolução mencionada: 4 m (p. 1)
- “The competition centered around a brand new open source dataset of Planet Labs satellite imagery mosaics at 4m resolution, which includes 24 images (one per month) covering ≈ 100 unique geographies.” (p. 1, seção Abstract)
- “4 Metric For this competition we defined successful building footprint identifications as proposals which overlap ground truth ( GT ) annotations with an Intersection-over-Union ( IoU ) score above a threshold of 0.25.” (p. 5, seção 1 https://registry.opendata.aws/spacenet/)
- “(a) (b) Figure 5: (a) Visualization of temporal collapse for ground truth (top row) and predictions (bottom row).” (p. 9, seção 3. There are three scenarios for all building candidates:)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 19 ocorrências (p. 3, 4, 5, 9, 10)
- **Mosaicos e compostos**: 3 ocorrências (p. 1, 3)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 24 menções vs 2 de pares)
**Métodos detectados automaticamente:**
- método/família **U-Net**: 6 ocorrências (p. 7, 8)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Evidência (leitura) — Métrica:**

- Acerto de footprint com **IoU > 0,25** (mais baixo que o 0,5 dos desafios anteriores pelo tamanho dos objetos) (p. 5).
- **SCOT (SpaceNet Change and Object Tracking):** combina um termo de **rastreamento** (mantém o mesmo identificador mês a mês) e um de **mudança** (detecta a construção de edificações novas) (p. 5).

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 3 ocorrências (p. 3, 6, 11)
- métrica **IoU**: 7 ocorrências (p. 5, 11, 12)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Resultados (tabela 1, p. 7):**

| Posição | Equipe | Escore | Arquitetura | Velocidade (km²/min) |
|---|---|---|---|---|
| 1 | lxastro0 | 41,00 | 1 × HRNet | 346 |
| 2 | cannab | 40,63 | 6 × EfficientNet + U-Net siamesa | 49 |
| 3 | selim_sef | 39,75 | 4 × EfficientNet + U-Net | 87 |
| 4 | motokimura | 39,11 | 10 × EfficientNet-b6 + U-Net | 42 |
| 5 | MaksimovKA | 30,74 | SENet154 + U-Net siamesa | 40 |
| baseline | | 17,11 | VGG16 + U-Net | 375 |
- **Pós-processamento pesou mais que a arquitetura** (p. 7). Tendências comuns: **ampliar a imagem 3–4×** (melhorou o desempenho), **máscara de 3 canais (footprint, borda, contato)** e ensembles (menos o vencedor) (p. 7–8).
- **Colapso temporal do vencedor:** supõe que edificações não mudam depois de aparecer (existe sempre, nunca existe, ou surge no quadro k e persiste); prevê a **posição uma só vez** num mapa de probabilidade comprimido no tempo (watershed com limiar adaptativo) e depois acha o **mês de origem** da edificação pela média da probabilidade dentro do contorno (p. 8–9).
- **Vencedor vs baseline (tabela 2, p. 9):** F1 0,61 ± 0,09 vs 0,46 ± 0,13; rastreamento 0,61 vs 0,41; **mudança 0,20 ± 0,09 vs 0,06 ± 0,06**; **SCOT 0,41 ± 0,11 vs 0,17 ± 0,11**.
- **Latitude:** como a GSD é ≈ 4,8 m × cos(latitude), o desempenho cai com a latitude: correlação de **−0,65 com o escore de mudança** e **−0,70 com o SCOT**; hipótese dos autores: sazonalidade e sombras maiores em latitudes altas (exemplo: mudança 0,30 a 20° vs 0,09 a 40°) (p. 10).
- Para objetos de 100 px², o desempenho é ~5× o do SpaceNet 4 (0,5 m), atribuído aos rótulos oniscientes; o teto de pontuação é menor (p. 11).

**Trechos numéricos detectados automaticamente (verificar):**
- “4 Metric For this competition we defined successful building footprint identifications as proposals which overlap ground truth ( GT ) annotations with an Intersection-over-Union ( IoU ) score above a threshold of 0.25.” (p. 5, seção 1 https://registry.opendata.aws/spacenet/)
- “Therefore latitude (or more precisely, the absolute value of latitude) is negatively correlated with tracking (-0.39), change (-0.65) and SCOT (-0.70) score.” (p. 10, seção 3. There are three scenarios for all building cand)
- “Figure 8: Building recall as a function of area for the winning submission (IoU ≥ 0.25).” (p. 11, seção 3. There are three scenarios for all building cand)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites e observações:**

- O artigo afirma que a mudança é "muito mais difícil" que o rastreamento, e o escore de mudança domina o SCOT (p. 9).
- **Observações minhas:** (a) o escore de mudança do campeão é **0,20**, ou seja, **a construção nova foi detectada de forma limitada**, mesmo com 7 meses de rotulagem; (b) como os rótulos usam imagem melhor que a de entrada, **não é replicável sem esse apoio**; (c) o pós-processamento do vencedor depende da suposição de que a edificação **nunca muda** depois de surgir (demolição e reforma ficam de fora); (d) o resultado é por local e mês, mas não há análise de nuvem no rastreio além das máscaras UDM; (e) a hipótese da latitude não foi testada.

**Trechos detectados automaticamente (verificar contexto):**
- “The closest comparison is the xView2 challenge , which examined building damage in satellite image pairs acquired before and after natural disasters; however, this task fails to address the complexities and opportunities posed by analysis o” (p. 2, seção 7 Challenge.)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Dados abertos** (AWS Open Data) e **os cinco códigos vencedores** com licença permissiva em github.com/SpaceNetChallenge/SpaceNet7_Multi-Temporal_Solutions; baseline em github.com/CosmiQ/CosmiQ_SN7_Baseline (notas de rodapé, p. 5–6).

- **Código/dados:** declarado sem URL localizada (p. 1)
- declaração: “The competition centered around a brand new open source dataset of Planet Labs satellite imagery mosaics at 4m resolution, which includes 24 images (one per month) covering ≈ 100 unique geographies.” (p. 1)
- declaração: “SpaceNet is a nonprofit LLC dedicated to accelerating open source, artificial intelligence applied research for geospatial applications, specifically foundational mapping ( i.e. building footprint & road network detection).” (p. 1)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (benchmark). Rótulos oniscientes e avaliação por local; não mede latência operacional.

**Interpretação — O que reaproveitar:**

- **Dataset SpaceNet 7/MUDS** para treinar e comparar detectores de construção em mosaicos Planet mensais de ~4 m.
- **Colapso temporal** (localizar uma vez, datar depois) como ideia de pós-processamento, adaptável a "início de construção".
- **Ampliação da imagem 3×** e **máscara de footprint, borda e contato** para objetos de poucos pixels.
- **Métrica SCOT** (rastreio + mudança) e o aviso de que latitude e sazonalidade afetam a mudança.
- **Soluções vencedoras** como código de referência.

**Interpretação — Cuidados para o nosso projeto:**

- Os melhores modelos acham construção nova com escore 0,2; a meta de "início de construção" automático em 5 m é difícil e precisa de pós-processamento temporal.
- Rótulos oniscientes inflam o desempenho em objetos minúsculos.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[PlanetProdutos|Produtos Planet (visão geral)]] — 6 ocorrências (p. 1, 3, 10)
- emprega conjunto de dados: [[SpaceNet7_MUDS|SpaceNet 7 / MUDS]] — 26 ocorrências (p. 1, 2, 3, 5, 6)
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[SITS|Séries temporais de imagens (SITS)]] — suporte vindo da leitura/título/resumo
- utiliza método: [[UNet|U-Net]] — 6 ocorrências (p. 7, 8)
- referencia (suporte manual da leitura): [[PosProcessamentoTemporal|Pós-processamento temporal (persistência, janela e colapso)]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[MetricasMudancaSemantica|Métricas de mudança semântica (SeK, SCS, SCOT)]] — suporte vindo da leitura/título/resumo
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 19 ocorrências (p. 3, 4, 5, 9, 10)
- referência (curado pela leitura): [[Generalizacao|Generalização e domain shift]] — suporte vindo da leitura/título/resumo

**Comparações substantivas com outros artigos:**
- este artigo descreve o desafio construído sobre o conjunto de [[Etten_2021_MultiTemporalUrban|Etten 2021]] — P11 relata o desafio SpaceNet 7 sobre o MUDS de P10; o escore de mudança do campeão foi 0,20 (tabela 2, p. 9).
- [[Metzger_2023_UrbanChangeForecasting|Metzger 2023]] usa o conjunto de dados do desafio de este artigo — P17 treina a previsão de construção no SpaceNet 7 e deriva as máscaras de mudança por subtração de máscaras de edificação.
- [[Glazer_2025_TEMPOGlobalTemporal|Glazer 2025]] valida com o benchmark de este artigo — P103 valida a presença de edificação no SpaceNet 7 (F1 0,85–0,88, p. 12), sem medir a mudança.

## Figuras selecionadas

![[Etten_2021_SpaceNetMultiTemporal_p4_Figure1.png|520]]
*Figure 1: A comparison between our dataset and related datasets. A. Annotated objects (p. 4; recorte do PDF convertido)*


## Anotações do leitor

- 
