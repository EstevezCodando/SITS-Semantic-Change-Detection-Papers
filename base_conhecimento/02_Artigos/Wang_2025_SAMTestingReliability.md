---
tipo: artigo
id_origem: P165
titulo: "MO-SAM: Testing the reliability and limits of mine feature delineation using Segment Anything Model to democratize mine observation and research"
ano: 2025
autores: ["Qitong Wang", "Emmanuel Chinkaka", "Romain Richaud", "Mehrnaz Haghdadi", "Coryn Wolk", "Kopo V. Oromeng", "Kyle Frankel Davis", "Federica Bettina Bianco"]
doi: "10.1371/journal.pstr.0000182"
arquivo_fonte: "coleta/P165_Wang2025_MO-SAM-Testing-the-reliability-and-limits-of-mine-feature-de.pdf"
markdown_fonte: "output/pdf/P165_Wang2025_MO-SAM-Testing-the-reliability-and-limits-of-mine-feature-de/document.md"
paginas: 26
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "C"
tarefas: ["[[Mineracao|Mineração]]"]
sensores: []
conjuntos_dados: []
metodos: []
preparo: ["[[Rotulagem|Rotulagem e anotação]]"]
validacao: []
ferramentas: ["[[QGIS|QGIS]]"]
tags: [artigo, leitura/profunda, relevancia/C]
---

# Wang 2025 — MO-SAM: Testing the reliability and limits of mine feature delineation using Segment Anything Model to democratize mine observation and research

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **C** — MO-SAM: SAM para feições de mina.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Qitong Wang, Emmanuel Chinkaka, Romain Richaud, Mehrnaz Haghdadi et al. (2025). MO-SAM: Testing the reliability and limits of mine feature delineation using Segment Anything Model to democratize mine observation and research. PLOS Sustainability and Transformation. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1371/journal.pstr.0000182
- **Arquivo de origem:** `coleta/P165_Wang2025_MO-SAM-Testing-the-reliability-and-limits-of-mine-feature-de.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P165_Wang2025_MO-SAM-Testing-the-reliability-and-limits-of-mine-feature-de/document.md` — 26 páginas, 61 recortes de figuras, 1 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Testar a **confiabilidade e os limites do Segment Anything Model (SAM) com prompts de pontos** para delinear feições internas de minas (pilhas de rejeito seco, bota-foras e estoques, "DWS") em imagens de alta resolução. Método **MO-SAM**, feito com QGIS e SAM abertos. É a ficha mais completa sobre uso real de SAM para rotulagem assistida no QGIS.

**Resumo detectado automaticamente (p. 1):** The purpose of this paper is to leverage the growth of AI-enabled tools to support the democratization of mine observation (MO) research. Mining is essential to meet projected demand for renewable energy technologies crucial to global climate mitiga­ tion objectives, but all mining activities pose local and regional challenges to envi­ ronmental sustainability. Such challenges can be mitigated by good governance, but unequal access among stakeholders to accurately interpreted satellite imagery can weaken good governance. Using readily available software—QGIS, and Segment Anything Model (SAM)—this paper develops and tests the reliability of MO-SAM, a new method to identify and delineate features within the spatially-explicit mine extent at a high level of detail. It focuses on dry tailings, waste dumps, and stockpiles in above-ground mining areas. While we intend for MO-SAM to be used gen…

- “The purpose of this paper is to leverage the growth of AI-enabled tools to support the democratization of mine observation (MO) research.” (p. 1, seção Abstract)
- “We developed an AI-assisted method called MO-SAM using freely available software— QGIS, and Segment Anything Model (SAM)—to make it easier for diverse communities to observe and analyze changes in mining activities.” (p. 2, seção Abstract)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “As shown in Fig 4, image 3, and Table 5, MO-SAM performance increased when there was a higher contrast among pixels located inside and outside the annotated mine features.” (p. 17, seção Discussion)
- “We utilized Airbus Pléiades constellation satellite imageries gathered between 2020 and 2023, and one image for 2015 to perform an object-based segmentation with MO-SAM on large-scale industrial mining sites with varying landscape con­ diti” (p. 5, seção Materials and methods)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- 20 minas industriais de lítio, cobalto, terras raras e platina, em floresta e em áreas áridas; 8 sítios na África Subsaariana, 4 na América do Norte, 3 na América do Sul, 3 na Ásia e 2 na Austrália (p. 5).
- Imagens **Airbus Pléiades Neo** (2020–2023 e uma de 2015), resolução **0,15 a 0,75 m** (p. 5, 7).
- Rótulos: anotados no **QGIS 3.30** por cinco coautores com formação em SIG, entre fev e ago/2023, revisados por especialistas (geologia, hidrologia, engenharia de minas, visão computacional) até haver acordo (p. 6).
- Total de 269 feições (por exemplo, 95 em floresta com terras raras, 51 em lítio em área árida) (p. 11).

**Detectado automaticamente (verificar):**
- “More specifically, for the same mine feature visualizations (3 images), the pixel intervals of grids are 50, 35, and 20, respectively, expressed below as PI50, PI35, and PI20.” (p. 21, seção Conclusion)
- “Such challenges can be mitigated by good governance, but unequal access among stakeholders to accurately interpreted satellite imagery can weaken good governance.” (p. 1, seção Abstract)
- “unequal access to accurately interpreted satellite imagery among mine-adjacent communities, researchers, policy-­ makers, and mining actors can weaken the information basis of environmentally and socially sustainable mine governance .” (p. 3, seção Introduction)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 72 ocorrências (p. 6, 7, 8, 9, 10)
- **Recorte em patches/tiles**: 9 ocorrências (p. 10, 18)
- **Textura (GLCM)**: 3 ocorrências (p. 15, 20, 23)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Método:**

- As imagens são capturadas como **capturas de tela RGB** do QGIS e entram no SAM (632 M de parâmetros no encoder, 4 M no decoder). A captura **perde geotags**, muda a resolução e o balanço de cor (p. 9).
- **Prompts simulados:** dentro do retângulo envolvente do polígono anotado, pontos positivos (dentro) e negativos (fora). Três esquemas: **Random** (5 a 50 pontos; positivos com distribuição gaussiana em torno do centro), **Grid** (intervalos de 50, 35 e 20 px) e **Grid Random** (aleatório sobre os cruzamentos da grade) (p. 7, 8).
- Métrica: **mIoU** entre máscara prevista e anotação; contraste de Weber entre feição e fundo (p. 10, 11).

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **SAM**: 167 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Transformer**: 10 ocorrências (p. 10)
- método/família **CNN**: 4 ocorrências (p. 3, 10)
- método/família **Transfer learning**: 4 ocorrências (p. 19)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- métrica **IoU**: 68 ocorrências (p. 9, 10, 11, 12, 13)
- métrica **Precisão/Recall**: 5 ocorrências (p. 1, 3, 4, 11, 19)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Resultados:**

- mIoU médio global 67,6 ± 0,6 %: Random 67,04 ± 1,21; Grid 66,61; **Grid Random 69,16 ± 0,59** (p. 9, 14).
- **Mais pontos não é melhor:** o desempenho sobe até ~20–30 pontos e **cai com 50**; o melhor intervalo de grade foi 35 px (p. 11, 15, 17).
- Por commodity/paisagem: PGE chega a 84–86 % em floresta e ~61–73 % em áridas; terras raras em floresta ~46–59 %; cobalto ~59–65 % (p. 13).
- **Contraste entre feição e fundo** explica a variação: IoU de 15,4 % em cenário de baixo contraste contra 81,7 % em alto contraste; correlações de Pearson com o contraste de até 0,68 (lítio em floresta, esquema Grid) (p. 13, 15).
- O SAM às vezes ignora pontos positivos e inclui pontos negativos na máscara (p. 17).

**Trechos numéricos detectados automaticamente (verificar):**
- “All four images of the “Co” commodity are forested. “STDev” denotes standard deviation. [https://doi.org/10.1371/journal.pstr.0000182.t004](https://doi.org/10.1371/journal.pstr.0000182.t004) of 15.42%, and on the right, a high-contrast landscape with an IoU of” (p. 13, seção Results)
- “Left, a low contrast landscape (IoU 15.42%).” (p. 14, seção Discussion)
- “Right, a high contrast landscape (IoU 81.68%).” (p. 14, seção Discussion)
- “Overall, MO-SAM’s mean perfor­ mance in segmenting DWS is < mIoU>=67.60 + /- 0.60% (where the uncertainty is represented by the standard devia­ tion).” (p. 14, seção Discussion)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites declarados e observações minhas:**

- Só aceita **RGB**; sem bandas multiespectrais nem geotags (p. 18).
- Anotações subjetivas: o limite entre pilha, estrada e erosão é ambíguo (p. 18).
- **Viés otimista (observação minha):** os prompts são gerados a partir do polígono anotado (retângulo envolvente e classificação positiva/negativa pela anotação), e quando a máscara tem várias partes o artigo **mantém só a máscara de maior mIoU** (p. 18), o que usa a verdade de campo. Os números são um teto, não o desempenho de um usuário real.
- Resolução submétrica; não testado em 3–5 m.
- Código: repositório GitHub `Critical-Minerals-Metals/MO-SAM` citado no artigo (p. 2).

**Trechos detectados automaticamente (verificar contexto):**
- “This demon­ strates a limitation in MO-SAM interpretation of features within the spatially explicit mine extent, and suggests potential limitations to MO-SAM performance on other complex and low-contrast images.” (p. 13, seção Results)
- “The results for forested PGE cannot be calculated because it has only one image that includes more than one mine feature, and there are only two mine features in that image.” (p. 13, seção Results)
- “We further discuss the potential limitations of mIoU as an evaluation metric, the necessary role of subjective human judgment, the incidence of human error in annotation, and the prediction noise from MO-SAM.” (p. 16, seção Discussion)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/Critical-Minerals-Metals/MO-SAM (p. 2)
- URL citada: https://github.com/Critical-Minerals-Metals/MO-SAM (p. 2)
- declaração: “Data availability statement: The github repository is available here: [https://github.com/](https://github.com/Critical-Minerals-Metals/MO-SAM) [Critical-Minerals-Metals/MO-SAM.](https://github.com/Critical-Minerals-Metals/MO-SAM) Funding: ” (p. 2)
- declaração: “Quan­ tum GIS (QGIS) software was utilized due to its functionality as an open-source platform for earth observation analysis (QGIS ).” (p. 5)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Persistência / confirmação 1 (p. 11)

**Interpretação — O que reaproveitar:**

- **Protocolo do EXP6 (pré-anotação com SAM no QGIS):** variar o esquema e o número de pontos (5 a 50), repetir a geração três vezes, medir mIoU e **tempo por objeto**.
- **Regra prática de 20–30 pontos** como ponto de partida, mas **validada na nossa resolução**: um telhado de 10 × 10 m tem ~4 px em 5 m, bem diferente de Pléiades a 0,3 m.
- **Contraste de Weber** como diagnóstico para prever onde a pré-anotação vai falhar e onde exigir revisão humana.
- **Seleção da máscara sem usar a anotação:** escolher a maior componente conexa ou a de maior pontuação do SAM, e não a de maior IoU.
- Ideia de **acompanhar a mesma feição no tempo** (pilhas que crescem ou mudam de lugar) como caso de mudança *dentro* de uma área já mapeada.

**Interpretação — Cuidados:**

- O artigo é sobre delineação, não sobre detecção de mudança.
- O nome do plugin Geo-SAM (ficha LP P164 Wang 2024) é anterior e diferente do método MO-SAM, que roda o SAM fora do plugin.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- usa ferramenta: [[QGIS|QGIS]] — 11 ocorrências (p. 1, 2, 3, 5, 6)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 72 ocorrências (p. 6, 7, 8, 9, 10)
- trata a tarefa: [[Mineracao|Mineração]] — suporte vindo da leitura/título/resumo
- referencia (suporte manual da leitura): [[PreAnotacaoSAM|Pré-anotação assistida (SAM e plugins QGIS)]] — suporte vindo da leitura/título/resumo

**Comparações substantivas com outros artigos:**
- este artigo tem versão anterior possivelmente em [[Wang_2024_GeoSamTesting|Wang 2024]] — O registro SSRN P164 parece ser o preprint do estudo MO-SAM; equivalência não confirmada.
- [[Wu_2026_GeoAIPythonPackage|Wu 2026]] integra a mesma família de ferramentas de este artigo — O plugin GeoAI inclui SamGeo (SAM); MO-SAM usa o SAM fora do plugin, com capturas de tela.

## Anotações do leitor

- 
