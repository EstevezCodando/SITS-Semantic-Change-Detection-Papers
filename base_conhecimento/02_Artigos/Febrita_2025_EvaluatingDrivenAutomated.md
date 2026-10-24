---
tipo: artigo
id_origem: P158
titulo: "Evaluating AI-Driven Automated Map Digitization in QGIS"
ano: 2025
autores: ["Diana Febrita"]
doi: "10.48550/arXiv.2504.18777"
arquivo_fonte: "coleta/P158_Febrita2025_Evaluating-AI-Driven-Automated-Map-Digitization-in-QGIS.pdf"
markdown_fonte: "output/pdf/P158_Febrita2025_Evaluating-AI-Driven-Automated-Map-Digitization-in-QGIS/document.md"
paginas: 13
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
tarefas: []
sensores: []
conjuntos_dados: ["[[OpenStreetMap|OpenStreetMap]]"]
metodos: []
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]", "[[Rotulagem|Rotulagem e anotação]]"]
validacao: ["[[PrecisaoRecall|Precisão e recall]]", "[[F1|F1]]", "[[IoU|IoU / mIoU]]"]
ferramentas: ["[[QGIS|QGIS]]"]
tags: [artigo, leitura/profunda]
---

# Febrita 2025 — Evaluating AI-Driven Automated Map Digitization in QGIS

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Diana Febrita (2025). Evaluating AI-Driven Automated Map Digitization in QGIS. arXiv (Cornell University). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2504.18777
- **Arquivo de origem:** `coleta/P158_Febrita2025_Evaluating-AI-Driven-Automated-Map-Digitization-in-QGIS.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P158_Febrita2025_Evaluating-AI-Driven-Automated-Map-Digitization-in-QGIS/document.md` — 13 páginas, 11 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Avaliar o **Deepness** (plugin QGIS) na digitalização automática de **edificações** com imagens do Google Earth, comparando com polígonos do OpenStreetMap como referência. É uma avaliação independente e pequena, útil sobretudo pela sensibilidade aos parâmetros do plugin.

**Resumo detectado automaticamente (p. 1):** Map digitization is an important process that converts maps into digital formats that can be used for further analysis. This process typically requires a deep human involvement because of the need for interpretation and decision-making when translating complex features. With the advancement of artificial intelligence, there is an alternative to conducting map digitization with the help of machine learning techniques. Deepness, or Deep Neural Remote Sensing, is an advanced AI-driven tool designed and integrated as a plugin in the QGIS application. This research focuses on assessing the effectiveness of Deepness in automated digitization. This study analyses AI-generated digitization results from Google Earth imagery and compares them with digitized outputs from OpenStreetMap (OSM) to evaluate performance. Keywords: GeoAI, Deep Neural Remote Sensing, Deepness, QGIS, F1-score…

- “This research evaluates the performance of Deepness, a QGIS plugin for automated digitization by comparing its results with manually digitized data from human contributors in a location in the United States.” (p. 2, seção Introduction)
- “This study compares AI-based digitization using Deepness, a QGIS plugin, with human digitized data extracted from OpenStreetMap (OSM) as the ground truth.” (p. 2, seção Methods)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The study area is a residential neighborhood along Cumberland Avenue in West Lafayette, Indiana, United States.” (p. 2, seção Methods)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- conjunto de dados **OpenStreetMap**: 24 ocorrências (p. 1, 2, 3, 8, 9)
- resolução mencionada: 100 cm (p. 4)
- resolução mencionada: 300 cm (p. 4)
- “This process typically requires a deep human involvement because of the need for interpretation and decision-making when translating complex features.” (p. 1, seção Abstract)
- “This research evaluates the performance of Deepness, a QGIS plugin for automated digitization by comparing its results with manually digitized data from human contributors in a location in the United States.” (p. 2, seção Introduction)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 20 ocorrências (p. 3, 4, 5, 6, 7)
- **Rotulagem / anotação**: 7 ocorrências (p. 2, 3, 9)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Dados e método:**

- Área: um bairro residencial na Cumberland Avenue, West Lafayette (Indiana, EUA); **320 edificações do OSM** como verdade; imagens do Google Earth; análise em QGIS e R (p. 2, 3).
- Casamento: IoU > 50 % = verdadeiro positivo; IoU < 50 % ou ausente no OSM = falso positivo; sem detecção = falso negativo; F1 sobre esses contagens (p. 3).
- Parâmetros testados: **resolução** (100 e 300 cm/px), **sobreposição de tiles** (0 % e 12 %; o campo não aceita decimais) e **remover segmentos pequenos** (p. 3–p. 8).

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- métrica **Precisão/Recall**: 12 ocorrências (p. 2, 3, 11, 12)
- métrica **F1**: 8 ocorrências (p. 1, 3, 8, 11, 12)
- métrica **IoU**: 7 ocorrências (p. 3, 9)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Resultados (p. 10, 12):**

| Teste | Configuração | Detectadas | TP | FP | FN | Precisão | Recall | F1 |
|---|---|---|---|---|---|---|---|---|
| 1 | 300 cm/px, 0 % de sobreposição | 603 | 222 | 381 | 98 | 36,8 % | 69,4 % | 48,1 % |
| 2 | 300 cm/px, 12 % | 497 | 257 | 240 | 63 | 51,7 % | 80,3 % | 62,9 % |
| 3 | 300 cm/px, 12 %, remover segmentos pequenos | 398 | 282 | 116 | 38 | 70,9 % | 88,1 % | 78,6 % |

- Em 100 cm/px o plugin produziu 2.909 "edificações" contra 776 em 300 cm/px (12 %), com muitos segmentos pequenos (p. 3).
- A IA detecta mais edificações que o OSM (anexos, galpões) e às vezes divide uma edificação em várias partes (p. 10).


## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites (incluindo observações minhas):**

- **Uma só vizinhança**, referência do OSM (sem revisão) e imagens do Google Earth; o artigo é um trabalho de curso.
- Inconsistência interna: o texto diz que a remoção de segmentos pequenos deixou **611** edificações (p. 6), mas a Tabela 2 mostra **398** no teste 3; usei a tabela. As legendas das Figuras 5 e 6 também parecem trocadas.
- Os parâmetros foram escolhidos olhando o F1 na própria área: otimismo.


## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 

**Interpretação — O que reaproveitar:**

- **Lista de parâmetros que alteram muito o resultado** (resolução de processamento, sobreposição, remoção de segmentos pequenos) e a necessidade de **calibrar por área** antes de comparar modelos.
- **Protocolo de casamento por IoU > 0,5** para contagem de edificações e relatório de TP/FP/FN, em linha com o SCOT (IoU > 0,25) de [[Etten_2021_MultiTemporalUrban|Etten 2021]].
- Reforça: **recall alto com precisão média** é adequado para triagem, e a revisão humana corrige os falsos positivos (E11 Operação e atualização).

**Interpretação — Cuidados:**

- Resolução de 1–3 m/px nos testes (Google Earth), comparável à escala de 3–5 m do projeto, mas com um modelo de zoo próprio e sem treino em Planet.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- emprega conjunto de dados: [[OpenStreetMap|OpenStreetMap]] — 24 ocorrências (p. 1, 2, 3, 8, 9)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 12 ocorrências (p. 2, 3, 11, 12)
- é avaliado por: [[F1|F1]] — 8 ocorrências (p. 1, 3, 8, 11, 12)
- é avaliado por: [[IoU|IoU / mIoU]] — 7 ocorrências (p. 3, 9)
- usa ferramenta: [[QGIS|QGIS]] — 11 ocorrências (p. 1, 2, 9)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 20 ocorrências (p. 3, 4, 5, 6, 7)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 7 ocorrências (p. 2, 3, 9)

**Comparações substantivas com outros artigos:**
- este artigo avalia [[Aszkowski_2023_DeepnessDeepNeural|Aszkowski 2023]] — P158 avalia o Deepness em edificações e mostra a dependência dos parâmetros (F1 48,1 → 78,6%).

## Figuras selecionadas

![[Febrita_2025_EvaluatingDrivenAutomated_p4_Figure1.png|520]]
*Figure 1. AI-based digitization results with a 100 cm/px resolution (p. 4; recorte do PDF convertido)*

![[Febrita_2025_EvaluatingDrivenAutomated_p4_Figure2.png|520]]
*Figure 2. AI-based digitization results with a 300 cm/px resolution (p. 4; recorte do PDF convertido)*

![[Febrita_2025_EvaluatingDrivenAutomated_p5_Figure3.png|520]]
*Figure 3. AI digitization results in a 300 cm/px resolution & 0% of tiles overlap (p. 5; recorte do PDF convertido)*


## Anotações do leitor

- 
