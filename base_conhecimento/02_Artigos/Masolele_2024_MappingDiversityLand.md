---
tipo: artigo
id_origem: P102
titulo: "Mapping the diversity of land uses following deforestation across Africa"
ano: 2024
autores: ["Robert N. Masolele", "Diego Marcos", "Veronique De Sy", "Itohan‐Osa Abu", "Jan Verbesselt", "Johannes Reiche", "Martin Herold"]
doi: "10.1038/s41598-024-52138-9"
arquivo_fonte: "coleta/P102_Masolele2024_Mapping-the-diversity-of-land-uses-following-deforestation-a.pdf"
markdown_fonte: "output/pdf/P102_Masolele2024_Mapping-the-diversity-of-land-uses-following-deforestation-a/document.md"
paginas: 16
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "A"
tarefas: ["[[Desmatamento|Desmatamento]]", "[[Mineracao|Mineração]]", "[[Vias|Vias e estradas]]", "[[ClassificacaoCobertura|Classificação de cobertura e uso da terra]]"]
sensores: ["[[PlanetNICFI|Planet NICFI (basemaps)]]"]
conjuntos_dados: ["[[GlobalForestChange|Global Forest Change (Hansen)]]"]
metodos: ["[[UNet|U-Net]]"]
preparo: ["[[IndicesEspectrais|Índices espectrais (NDVI etc.)]]"]
validacao: ["[[Desbalanceamento|Desbalanceamento de classes]]", "[[F1|F1]]"]
ferramentas: []
tags: [artigo, leitura/profunda, relevancia/A]
---

# Masolele 2024 — Mapping the diversity of land uses following deforestation across Africa

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **A** — NICFI de 5 m; uso da terra após o desmatamento (15 classes) com aprendizado ativo, F1 de 84%.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Robert N. Masolele, Diego Marcos, Veronique De Sy, Itohan‐Osa Abu et al. (2024). Mapping the diversity of land uses following deforestation across Africa. Scientific Reports. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1038/s41598-024-52138-9
- **Arquivo de origem:** `coleta/P102_Masolele2024_Mapping-the-diversity-of-land-uses-following-deforestation-a.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P102_Masolele2024_Mapping-the-diversity-of-land-uses-following-deforestation-a/document.md` — 16 páginas, 30 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Mapear, a **5 m** e em escala continental, **o uso da terra que sucede o desmatamento** na África (30° S a 30° N): 15 classes (cultivo de pequena e grande escala, pasto, mineração, estradas, outras terras com árvores, floresta plantada, café, assentamento, chá, água, dendê, seringueira, caju, cacau) (p. 1–2, 8). A saída é **um mapa de uso em 2022** aplicado às áreas de perda do **Hansen (2001–2020)**; não é um modelo de detecção de mudança.

- “Here we present the first high-resolution (5 m) and continental-scale mapping of land use following deforestation in Africa, which covers an estimated 13.85% of the global forest area, including humid and dry forests.” (p. 1, seção Início)
- “Here we present the results with and without using AL to map land-use following deforestation at a continental scale.” (p. 2, seção Results)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “Trend of land‑use following deforestation in Africa Having predicted the land-use following deforestation across Africa for the year 2001 to 2020, we attempted to estimate the trend of the land-use for the entire study area and across four ” (p. 4, seção Results)
- “The study area was defined based on the coverage of high-resolution Planet-NICFI ­data” (p. 6, seção Study area)
- “Generating land‑use map prediction at scale We present the first wall-to-wall map of land-use following deforestation across Africa covering forest loss from the year 2001 to 2020 (Fig.” (p. 2, seção Results)
- “For detailed visualisation, the predicted output map of land use following deforestation is available at this website: [https://​rober​tnag82.​users.​earth​engine.​app/​view/​afric​alu.](https://robertnag82.users.earthengine.app/view/africa” (p. 2, seção Results)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- **Mosaicos NICFI anuais de 4,77 m**, 4 bandas normalizadas para 0–1, mais **NDVI, SAVI e NDMI**, que os autores dizem terem melhorado o desempenho em testes (p. 8).
- **2.357 imagens** de toda a África: 895 com anotação (80 % treino e 20 % teste independente) e 1.462 sem anotação, usadas no aprendizado ativo; patches com perda ≥ 3,8 ha (n = 1.821) (p. 8).
- **Rótulos de referência heterogêneos:** ciência cidadã, anotações de projetos por país e amostragem sistemática 10 × 10 km da FAO; a maior parte em **pontos ou polígonos com mistura de classes**, o que impede o uso direto em segmentação (p. 6–8).
- A imagem de **2022** serve de proxy para o uso que seguiu a perda de 2001–2020 (p. 8).

**Detectado automaticamente (verificar):**
- sensor/produto **Planet NICFI**: 16 ocorrências (p. 3, 6, 8, 10, 13)
- sensor/produto **Planet (mosaicos e cenas)**: 9 ocorrências (p. 6, 8, 13)
- sensor/produto **SAR**: 7 ocorrências (p. 13)
- resolução mencionada: 5 m (p. 1)
- “In total, we had 2357 images acquired from all across Africa (refer Sect. "Data", of which only 895 images were having annotations.” (p. 8, seção Data)
- “80% of the 895 images were placed in a pool of training data, while 20% was left out as independent test data.” (p. 8, seção Data)
- “The remaining 1462 images were placed in a pool of unannotated training data.” (p. 8, seção Data)
- “We use reference data for 15 different land-use types from 30 countries and implement an active learning framework to train a deep learning model for predicting land-use following deforestation with an F1-score of 84 ± 0.7 for the whole of ” (p. 1, seção Início)
- “Many efforts to map drivers of forest loss rely on expert-based visual interpretation from samples of high-resolution satellite ­images [,] .” (p. 2, seção Início)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 33 ocorrências (p. 1, 6, 8, 9, 10)
- **Recorte em patches/tiles**: 29 ocorrências (p. 1, 2, 4, 8, 11)
- **Mosaicos e compostos**: 9 ocorrências (p. 8, 13)
- **Índices espectrais**: 9 ocorrências (p. 8)
- **Normalização / escala**: 4 ocorrências (p. 8, 9)
- **Máscara de nuvem e sombra**: 3 ocorrências (p. 8, 13)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Método:**

- **U-Net com atenção** (Attention U-Net de um estudo prévio na Etiópia, estendida de 9 para 15 classes), 200 épocas, lote 64, **Adam 1e-4**, **Focal Loss** para desbalanceamento, dropout 0,1, Keras/TensorFlow na plataforma SEPAL (p. 9–10).
- **Aprendizado ativo** em ciclos: o modelo é treinado, escolhe entre as imagens não anotadas as de **entropia > 0,6**, uma pessoa anota, e elas voltam ao treino. Foram 716 imagens no treino inicial, +372 no 2º ciclo e +554 no 3º (p. 10).
- Inferência só nas áreas de perda do Hansen; avaliação independente com 179 imagens por ciclo (p. 10).

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **Aprendizado ativo**: 11 ocorrências (p. 1, 2, 3, 7, 8)
- método/família **U-Net**: 7 ocorrências (p. 3, 8, 9, 10, 12)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 10 [−] ” (p. 9)
- batch: “batch size of 64, using Adam optimization with a l” (p. 9)
- épocas/iterações: “200 epochs” (p. 9)
- otimizador: “Adam optimization with a learning rate of 10” (p. 9)
- perda: “focal loss has shown to perform well on data with ” (p. 9)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Amostra independente**: 6 ocorrências (p. 2, 8, 9, 10)
- **Desbalanceamento**: 6 ocorrências (p. 9, 10, 11)
- **Teste externo / generalização**: 2 ocorrências (p. 2, 9)
- métrica **F1**: 13 ocorrências (p. 1, 2, 4, 10, 11)
- métrica **Precisão/Recall**: 4 ocorrências (p. 10)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Resultados:**

- **F1 macro:** 43 % com os dados originais → 54 % após o 1º ciclo → **84 % após o 2º** (84 ± 0,7 no continente) (p. 2).
- Antes do aprendizado ativo, o F1 era de 0,05 (mineração), 0,10 (estradas), 0,41 (assentamento), 0,25 (seringueira) e 0,14 (caju) (p. 10); o **cacau** ficou alto em todos os ciclos, atribuído à homogeneidade regional dos rótulos (p. 11).
- **Mapa completo:** acurácia do usuário 85 %, do produtor 84 %, F1 85 % (p. 2, figura 3); amostragem estratificada por quinquênio (2001–2020) para estimar área e acurácia (p. 10).
- Resultado temático: **roça de pequena escala responde por 64 % da perda de floresta na África**, com picos em Madagascar (88 %) e RDC (85 %); outras terras com árvores 10 %; grandes cultivos 9 %; "arco de culturas comerciais" (cacau, dendê, seringueira) no oeste e centro; caju em expansão nas florestas secas (p. 2–3).

**Trechos numéricos detectados automaticamente (verificar):**
- “Specifically, the macro average F1-score improved from 43% with the original data to 54% after the first 1 AL round and to 84% after the second round (Fig. ).” (p. 2, seção Results)
- “The map has a users accuracy of 85%, producers accuracy of 84%, and F1-score of 85% (Fig.” (p. 2, seção Results)
- “1), the initial model achieved a macro averaged F1-score of 43%, compared to successive models obtaining 54% and 84% after one and two rounds of addition of training data using the AL approach, respectively.” (p. 11, seção Discussion)
- “In Africa, the lowest accuracy was found in sub-Saharan Africa, with false negatives of up to 48%, indicating an underestimation of forest loss in this region, specifically in dry ­forests .” (p. 13, seção Discussion)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites declarados e observações:**

- A imagem de 2022 **pode mostrar um uso secundário ou rebrota**, e não a causa original da perda de 2001–2015 (p. 11).
- O Hansen tem erros conhecidos, sobretudo em perdas pequenas (p. 11).
- **Observações minhas:** (a) o F1 de 84 % vem de uma avaliação com 179 imagens independentes, mas os rótulos de teste também surgem dos ciclos de anotação; o texto não detalha a separação espacial entre o conjunto de teste e as áreas anotadas depois; (b) o ganho de 54 % para 84 % mostra que o **aprendizado ativo vale mais que a mudança de arquitetura** neste problema; (c) o produto é de **uso após perda**, com uma só data de imagem; **não mede a data da mudança**; (d) para mineração, estrada e assentamento, o F1 inicial era muito baixo, o que mostra a dificuldade das classes pequenas e lineares.

**Trechos detectados automaticamente (verificar contexto):**
- “Particularly in cases where the training data is limited, heterogeneous or is prone to labeling errors (i.e. shape correctness, a mix of land uses), the model using the original data is not able to generalize across regions.” (p. 11, seção Discussion)
- “www.nature.com/scientificreports/ commodity crops and small-scale/large-scale agriculture, where other studies ­struggle .” (p. 13, seção Discussion)
- “One drawback of these approaches is that they are not wall-to-wall, and they may miss out on many deforestation drivers in unsampled locations, reducing their usefulness for deriving global statistics or getting a general ­overview [,] .” (p. 13, seção Discussion)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- Mapa visualizável em app do Earth Engine (URL no artigo); modelo e dados de treino não confirmados como abertos no trecho lido; **código não informado**.

- **Código/dados:** declarado sem URL localizada (p. 8)
- declaração: “Other reference data was retrieved from open source data available via online ­searching [–] .” (p. 8)
- declaração: “www.nature.com/scientificreports/ Data availability The reference data are freely available at the citations reference in this Manuscript and upon request to the cor[responding author.” (p. 14)

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Revisão humana 5 (p. 2, 8, 11); Latência / frequência 2 (p. 8, 13); Persistência / confirmação 2 (p. 2); Falsos alertas 1 (p. 13)

**Interpretação — O que reaproveitar:**

- **Aprendizado ativo por entropia** para construir rótulos de segmentação onde só há pontos ou polígonos misturados (ganho de 43 % para 84 % de F1 em dois ciclos).
- **Focal Loss + Attention U-Net** como linha de base para classes raras, incluindo estradas, mineração e assentamento.
- **Índices NDVI, SAVI e NDMI** como canais extras sobre as 4 bandas do NICFI.
- **Seleção de patches pela perda do Hansen** (≥ 3,8 ha) para focar o treino e a inferência onde há mudança.
- **Estimativa de acurácia e área estratificada por período**.

**Interpretação — Cuidados para o nosso projeto:**

- Mosaico anual, não mensal: serve para classificar o destino do solo, não para datar o início da obra.
- Depende do Hansen para saber onde houve perda, então herda a sua omissão de perdas pequenas.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[PlanetNICFI|Planet NICFI (basemaps)]] — 16 ocorrências (p. 3, 6, 8, 10, 13)
- referência (curado pela leitura): [[GlobalForestChange|Global Forest Change (Hansen)]] — suporte vindo da leitura/título/resumo
- utiliza método: [[UNet|U-Net]] — 7 ocorrências (p. 3, 8, 9, 10, 12)
- trata a tarefa: [[Desmatamento|Desmatamento]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[Mineracao|Mineração]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[Vias|Vias e estradas]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[ClassificacaoCobertura|Classificação de cobertura e uso da terra]] — suporte vindo da leitura/título/resumo
- referencia (suporte manual da leitura): [[AprendizadoAtivo|Aprendizado ativo para rotulagem]] — suporte vindo da leitura/título/resumo
- referencia (suporte manual da leitura): [[AmostragemEstratificada|Amostragem estratificada]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[IndicesEspectrais|Índices espectrais (NDVI etc.)]] — suporte vindo da leitura/título/resumo
- adota desenho de validação: [[Desbalanceamento|Desbalanceamento de classes]] — 6 ocorrências (p. 9, 10, 11)
- é avaliado por: [[F1|F1]] — 13 ocorrências (p. 1, 2, 4, 10, 11)

**Comparações substantivas com outros artigos:**
- este artigo usa o mesmo mosaico NICFI de 4,77 m de [[Wagner_2023_MappingTropicalForest|Wagner 2023]] — P102 classifica o uso após a perda do Hansen e P01 classifica a floresta por data; ambos usam as quatro bandas do NICFI.
- este artigo complementa [[Zhang_2023_MonitoringMonthlyTropical|Zhang 2023]] — P91 detecta a perda de dossel mensal e P102 classifica o uso da terra que sucede a perda; juntos cobrem onde e o que veio depois com NICFI de 5 m (interpretação).

## Figuras selecionadas

![[Masolele_2024_MappingDiversityLand_p7_Figure7.png|520]]
*Figure 7. Map showing study location in the African continent along 30 [◦] south and 30 [◦] north. ( A ) is the study (p. 7; recorte do PDF convertido)*

![[Masolele_2024_MappingDiversityLand_p3_Figure1.png|520]]
*Figure 1. The bar chart shows the performance of the attention U-Net model in classifying land-use following (p. 3; recorte do PDF convertido)*

![[Masolele_2024_MappingDiversityLand_p3_Figure2.png|520]]
*Figure 2. A 5 m resolution land-use following deforestation map in Africa (30 [◦] south and 30 [◦] north) (p. 3; recorte do PDF convertido)*


## Anotações do leitor

- 
