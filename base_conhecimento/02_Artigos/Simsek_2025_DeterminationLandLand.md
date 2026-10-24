---
tipo: artigo
id_origem: P06
titulo: "Determination of land use and land cover change using multi-temporal PlanetScope images and deep learning CNN model"
ano: 2025
autores: ["Fatih Fehmi Şimşek"]
doi: "10.1007/s10333-025-01024-9"
arquivo_fonte: "coleta/P06_Simsek2025_Determination-of-land-use-and-land-cover-change-using-multi-.pdf"
markdown_fonte: "output/pdf/P06_Simsek2025_Determination-of-land-use-and-land-cover-change-using-multi-/document.md"
paginas: 19
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "A"
tarefas: ["[[ClassificacaoCobertura|Classificação de cobertura e uso da terra]]", "[[SITS|Séries temporais de imagens (SITS)]]", "[[Deteccao_Mudanca|Detecção de mudanças]]"]
sensores: ["[[PlanetScope|PlanetScope (Dove/SuperDove)]]"]
conjuntos_dados: []
metodos: []
preparo: ["[[IndicesEspectrais|Índices espectrais (NDVI etc.)]]"]
validacao: ["[[AcuraciaGlobal|Acurácia global (OA)]]"]
ferramentas: []
tags: [artigo, leitura/profunda, relevancia/A]
---

# Simsek 2025 — Determination of land use and land cover change using multi-temporal PlanetScope images and deep learning CNN model

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **A** — PlanetScope de 3 m em nove datas; CNN de cobertura e mudança por comparação de mapas de datas diferentes; divisão por pixel (vazamento).

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Fatih Fehmi Şimşek (2025). Determination of land use and land cover change using multi-temporal PlanetScope images and deep learning CNN model. Paddy and Water Environment. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1007/s10333-025-01024-9
- **Arquivo de origem:** `coleta/P06_Simsek2025_Determination-of-land-use-and-land-cover-change-using-multi-.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P06_Simsek2025_Determination-of-land-use-and-land-cover-change-using-multi-/document.md` — 19 páginas, 13 recortes de figuras, 1 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Classificar **uso e cobertura da terra (LULC)** na planície de Gediz (Manisa, Turquia) com **PlanetScope SuperDove de 8 bandas (3 m)** em nove datas de 2023 e uma **CNN 2D**, e **comparar o mapa de 2023 com os blocos físicos do LPIS de 2015** para apontar áreas que precisam de atualização cadastral (p. 1–2, 15–17). A mudança vem da **diferença entre dois mapas de fontes diferentes**, não de um modelo de mudança.

**Resumo detectado automaticamente (p. 1):** Land use and land cover (LULC), an important component of Earth observation technology, plays a crucial role in image classification. Detailed LULC information is of great importance for monitoring agriculture and wetlands, urban and rural planning, land resource management, and the monitoring and detection of climate change-induced changes. To create a detailed LULC, high-resolution satellite imagery, ground truth data, and a model that provides high accuracy are required. For this reason, 8-band PlanetScope images with 3 m spatial resolution, Land Parcel Identification System (LPIS) physical blocks (1:5000 scale), and a convolutional neural network (CNN) model were used as ground truth data. While using the CNN model, hyperparameter optimization was performed to determine the most suitable parameters for achieving high classification accuracy. As a result of the classification, the ove…

- “This study presents a novel approach by integrating high-resolution, multi-temporal PlanetScope imagery with LPIS data and employing a CNN-based deep learning model optimized for LULC classification.” (p. 3, seção 1 TÜBİTAK Space Technologies Research Institute,)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The study area (27° 43′–28° 50′ E, 38° 39′–38° 30′ N) is situated within the Gediz Plain in the city of Manisa, western Turkey (Fig.” (p. 3, seção Study area)
- “The north-western part of the study area (520 ­km ) features Çal Mountain, with an elevation of 1034 m, and the Gediz River flows through the southern part of the area.” (p. 3, seção Study area)
- “(2023) analyzed six PlanetScope (PS) monthly mosaics from the 2021/2022 season to identify double-cropping areas in Goiatuba, Goiás State, Brazil.” (p. 3, seção 1 TÜBİTAK Space Technologies Research Institute,)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- **PlanetScope PSB.SD, Ortho Analytic 8B SR (nível 3B), reflectância de superfície**, com a ferramenta de **normalização e harmonização** da Planet (alinha cada cena a uma referência sazonal do Sentinel-2) (p. 4, 6–7).
- **Nove datas de 2023** (22/fev, 24/mar, 1/mai, 6/jun, 5/jul, 3/ago, 8/set, 5/out, 11/nov) (p. 5, tabela 2).
- **Referência:** blocos físicos do LPIS de 2015/2016, digitalizados de ortofotos de 30 cm e imagens de ≥ 50 cm; 24 subclasses agrupadas em 7 (arável, gramado, floresta, superfície artificial, arbustos/vinhedo, culturas arbóreas, água) (p. 6, 9, tabelas 3–4).
- Índices NDVI, SAVI (L = 0,5) e NDWI; composto de **99 bandas** (8 bandas × 9 datas + 3 índices × 9 datas) (p. 7–8).

**Detectado automaticamente (verificar):**
- sensor/produto **PlanetScope**: 34 ocorrências (p. 1, 2, 3, 4, 5)
- sensor/produto **Sentinel-2**: 19 ocorrências (p. 2, 3, 4, 5, 6)
- sensor/produto **Planet (mosaicos e cenas)**: 13 ocorrências (p. 2, 3, 4, 5, 6)
- sensor/produto **Sentinel-1**: 5 ocorrências (p. 3, 16, 17)
- resolução mencionada: 3 m (p. 1)
- resolução mencionada: 10 m (p. 2)
- “(2022) conducted an LULC study (grassland, arable land, tree crops, vineyard, wetland, artificial surface, and forest) in Greece (Fthiotida Prefecture and Central Greece District) using four different Sentinel-2 images from 2018, LPIS physi” (p. 2, seção 1 TÜBİTAK Space Technologies Research Institute,)
- “To create a detailed LULC, high-resolution satellite imagery, ground truth data, and a model that provides high accuracy are required.” (p. 1, seção Abstract)
- “For this reason, 8-band PlanetScope images with 3 m spatial resolution, Land Parcel Identification System (LPIS) physical blocks (1:5000 scale), and a convolutional neural network (CNN) model were used as ground truth data.” (p. 1, seção Abstract)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 25 ocorrências (p. 2, 3, 4, 6, 9)
- **Índices espectrais**: 20 ocorrências (p. 2, 3, 6, 7, 9)
- **Rotulagem / anotação**: 10 ocorrências (p. 1, 3, 6, 12, 17)
- **Mosaicos e compostos**: 8 ocorrências (p. 2, 3, 7, 8, 15)
- **Normalização / escala**: 5 ocorrências (p. 6, 7, 11)
- **Correção atmosférica / reflectância**: 4 ocorrências (p. 1, 6)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Preparo:**

- Polígonos < 1.000 m² excluídos; **erosão de 6 m** em cada classe para tirar bordas; **70 % dos pixels de referência para treino e 30 % para teste** (p. 6). A divisão é por pixel, não por bloco ou área.

**Evidência (leitura) — Método:**

- **CNN 2D** com 2 camadas de batch normalization, 5 de dropout (3 de 0,2 e 2 de 0,5), flatten e densas de 64 e 128 neurônios; Adam, lr 1e-4, lote 32, 200 épocas, entropia cruzada categórica (p. 11–12, tabela 7). Classificação por pixel na vizinhança, sem decodificador espacial.
- Otimização de hiperparâmetros citada (p. 11); busca usada não detalhada no trecho lido.

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 16 menções vs 0 de pares)
**Métodos detectados automaticamente:**
- método/família **CNN**: 43 ocorrências (p. 1, 2, 3, 6, 8)
- método/família **Random Forest**: 8 ocorrências (p. 2, 3, 16, 17)
- método/família **SVM**: 5 ocorrências (p. 2, 3)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate, etc” (p. 12)
- batch: “batch size, loss function, learning rate, etc” (p. 12)
- otimizador: “Adam optimizer was used to reduce the traini” (p. 12)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- métrica **Precisão/Recall**: 32 ocorrências (p. 12, 14)
- métrica **F1**: 9 ocorrências (p. 12, 14)
- métrica **Acurácia global**: 9 ocorrências (p. 1, 2, 3, 12, 15)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Métricas e resultados:**

- **Acurácia global 93,14 %**; por classe ~90 %; água 96,3 % e floresta 93,4 % no topo, gramado 89 % e culturas arbóreas 89,8 % no fim (p. 1, 15).
- **Comparação 2015 × 2023 (tabela 9, p. 15):** arável 100.867 → 109.329 ha; água 6.667 → 427 ha (secagem do Lago Marmara); superfície artificial 6.075 → 6.270 ha; vinhedo 4.303 → 3.219 ha; culturas arbóreas 5.628 → 6.254 ha; floresta e gramado quase iguais.
- Exemplos qualitativos: lago convertido em lavoura, estrada nova, vinhedo → arável e **painéis solares** classificados como superfície artificial (p. 12).

**Trechos numéricos detectados automaticamente (verificar):**
- “As a result of the classification, the overall accuracy value was 93.14%, while the accuracy value for each class (arable land, artificial surface, forest, grassland, shrubland, tree crops, and water) was around 90%.” (p. 1, seção Abstract)
- “In the study, the overall accuracy value was 92.2%, with the highest accuracy observed for arable land and water (97%), while the lowest accuracy was found for grassland (88%) and tree crops (73%).” (p. 2, seção 1 TÜBİTAK Space Technologies Research Institute,)
- “As a result of this study using the random forest algorithm, the overall accuracy was 83.3%.” (p. 2, seção 1 TÜBİTAK Space Technologies Research Institute,)
- “When the LULC map and LPIS physical blocks were compared, it was found that there was a 31.5% increase in arable areas.” (p. 2, seção 1 TÜBİTAK Space Technologies Research Institute,)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites e observações:**

- O texto atribui a confusão entre vinhedo/arbustos e arável, e entre mata e artificial, à fenologia e à semelhança espectral (p. 12, 17).
- **Observações minhas:** (a) a **divisão 70/30 por pixel** de blocos com buffer de 6 m provoca **vazamento espacial**: pixels vizinhos do mesmo bloco aparecem no treino e no teste, o que **infla** os 93,14 %; (b) o gabarito é o próprio LPIS de 2015 filtrado ("blocos sem mudança de classe"), então a mudança é avaliada contra uma referência que exclui as mudanças; (c) a verificação das mudanças é visual e por exemplos, **sem amostra independente nem acurácia de mudança**; (d) a diferença de fonte entre mapas (ortofoto 30 cm vs Planet 3 m) gera artefatos de escala (blocos mínimos e bordas); (e) **não há comparação** com Random Forest ou outro baseline com os mesmos dados, apesar da afirmação de superioridade da CNN (p. 17); (f) o título fala em "mudança", mas só há uma data de Planet.

**Trechos detectados automaticamente (verificar contexto):**
- “Despite the promising results, this study has some limitations.” (p. 17, seção Discussion)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- Código e dados não informados no trecho lido; LPIS é dado oficial turco.

- **Código/dados:** declarado sem URL localizada (p. 2)
- declaração: “Notably, DL-based LULC classification methods have outperformed traditional and ML methods, particularly 2017). when sufficient training data is available (Zhu et al.” (p. 2)
- hiperparâmetros **não detectados** automaticamente: épocas/iterações, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 3 (p. 10, 12, 17)

**Interpretação — O que reaproveitar:**

- **Harmonização radiométrica da Planet com referência Sentinel-2** antes de empilhar datas (p. 6–7).
- **Pilha multitemporal de 9 datas com índices** como entrada de pixel para classificação de transições sazonais.
- **Erosão da referência (buffer negativo)** para remover pixels de borda.
- **Mapa de cobertura vs mapa cadastral** como fluxo para listar polígonos candidatos à revisão humana.

**Interpretação — Cuidados para o nosso projeto:**

- Não usar a acurácia de 93,14 % como estimativa de generalização (vazamento espacial).
- Cobertura agrícola e sazonal; não trata de edificações novas nem de supressão de vegetação nativa.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[PlanetScope|PlanetScope (Dove/SuperDove)]] — 34 ocorrências (p. 1, 2, 3, 4, 5)
- trata a tarefa: [[ClassificacaoCobertura|Classificação de cobertura e uso da terra]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[SITS|Séries temporais de imagens (SITS)]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- aplica etapa de preparo: [[IndicesEspectrais|Índices espectrais (NDVI etc.)]] — 20 ocorrências (p. 2, 3, 6, 7, 9)
- é avaliado por: [[AcuraciaGlobal|Acurácia global (OA)]] — 9 ocorrências (p. 1, 2, 3, 12, 15)

**Comparações substantivas com outros artigos:**
- este artigo compartilha o problema de fontes diferentes com [[GonzalezVelez_2026_TropicalDryForest|GonzalezVelez 2026]] — P06 compara o mapa de 2023 com o cadastro de 2015, e P09 compara o mapa de 2019 com o de 2017 de outra fonte; ambos herdam diferenças de fonte.

## Figuras selecionadas

![[Simsek_2025_DeterminationLandLand_p4_Fig.1.png|520]]
*Fig. 1 Study area (Gediz Plain, Manisa, Turkey) is shown as terrain with labels (p. 4; recorte do PDF convertido)*


## Anotações do leitor

- 
