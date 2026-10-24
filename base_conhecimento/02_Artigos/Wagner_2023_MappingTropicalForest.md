---
tipo: artigo
id_origem: P01
titulo: "Mapping Tropical Forest Cover and Deforestation with Planet NICFI Satellite Images and Deep Learning in Mato Grosso State (Brazil) from 2015 to 2021"
ano: 2023
autores: ["Fabien Hubert Wagner", "Ricardo Dalagnol", "Celso H. L. Silva", "Griffin Carter", "Alison L. Ritz", "Mayumi C. M. Hirye", "Jean Pierre Ometto", "Sassan S Saatchi"]
doi: "10.3390/rs15020521"
arquivo_fonte: "coleta/P01_Wagner2023_Mapping-Tropical-Forest-Cover-and-Deforestation-with-Planet-.pdf"
markdown_fonte: "output/pdf/P01_Wagner2023_Mapping-Tropical-Forest-Cover-and-Deforestation-with-Planet-/document.md"
paginas: 20
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "A"
tarefas: ["[[Desmatamento|Desmatamento]]"]
sensores: ["[[PlanetNICFI|Planet NICFI (basemaps)]]"]
conjuntos_dados: ["[[PRODES|PRODES (INPE)]]", "[[GlobalForestChange|Global Forest Change (Hansen)]]"]
metodos: ["[[UNet|U-Net]]", "[[CNN|Redes convolucionais (CNN)]]"]
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]", "[[MascaraNuvem|Máscara de nuvem e sombra]]", "[[Normalizacao|Normalização e escala radiométrica]]", "[[Rotulagem|Rotulagem e anotação]]"]
validacao: ["[[AmostraIndependente|Amostra independente]]", "[[F1|F1]]", "[[AcuraciaGlobal|Acurácia global (OA)]]"]
ferramentas: []
tags: [artigo, leitura/profunda, relevancia/A]
---

# Wagner 2023 — Mapping Tropical Forest Cover and Deforestation with Planet NICFI Satellite Images and Deep Learning in Mato Grosso State (Brazil) from 2015 to 2021

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **A** — NICFI mensal de 4,77 m com U-Net para cobertura arbórea e desmatamento por diferença; validado com LiDAR, PRODES e GFC.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Fabien Hubert Wagner, Ricardo Dalagnol, Celso H. L. Silva, Griffin Carter et al. (2023). Mapping Tropical Forest Cover and Deforestation with Planet NICFI Satellite Images and Deep Learning in Mato Grosso State (Brazil) from 2015 to 2021. Remote Sensing. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.3390/rs15020521
- **Arquivo de origem:** `coleta/P01_Wagner2023_Mapping-Tropical-Forest-Cover-and-Deforestation-with-Planet-.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P01_Wagner2023_Mapping-Tropical-Forest-Cover-and-Deforestation-with-Planet-/document.md` — 20 páginas, 40 recortes de figuras, 2 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Mapear cobertura arbórea e desmatamento no Mato Grosso (~1 milhão de km²) com mosaicos Planet NICFI (~4,78 m) e uma U-Net, reconstruindo a história do desmatamento 2015–2021 ao comparar a máscara de floresta de cada data. A classificação é feita **data a data**; a mudança vem da diferença entre máscaras.

- “2.2 LiDAR tree cover dataset To validate our tree cover map, we compared our results to the LiDAR height data that were acquired in the scope of the Amazon Biomass Estimate project (EBA/INPE) which covers mainly Amazonian forests.” (p. 4, seção Início)
- “To test if our tree cover and deforestation products were consistent with independent datasets over the region, we compared our results to two existing products.” (p. 5, seção 2.3 Deforestation history datasets)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The region located in the south of the Amazon Forest was chosen because it has overcome large amounts of deforestation the past.” (p. 4, seção Início)
- “This study region cover represents ∼ 1 millions of km .” (p. 4, seção Início)
- “arXiv Template A P REPRINT ## M APPING T ROPICAL F OREST C OVER AND D EFORESTATION WITH P LANET NICFI S ATELLITE I MAGES AND D EEP L EARNING IN M ATO G ROSSO S TATE (B RAZIL ) FROM 2015 TO 2021 A P REPRINT Fabien H.” (p. 2, seção Início)
- “Here, we map tropical tree cover and deforestation between 2015 and 2022 using 5 m spatial resolution Planet NICFI satellite images over the state of Mato Grosso (MT) in Brazil and a U-net deep learning model.” (p. 3, seção Início)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- 2.658 tiles de ~20 × 20 km, 32 datas: semestrais de 2015-12 a 2020-06 e mensais de 2020-09 a 2022-06; 85.056 imagens (p. 4).
- Bandas R, G, B, NIR em 12 bits. RGB truncado em 0–2540, NIR dividido por 3,937 e tudo reescalado para 8 bits (÷10). **Sem correção atmosférica.** Borda espelhada de 128 px no composto (p. 4) e 64 px na predição (p. 7).
- Validação independente: LiDAR aéreo do projeto EBA/INPE (141 faixas de 15 km × 0,5 km, 2016, ≥4 pontos/m²), PRODES (mín. 6,25 ha) e Global Forest Change (p. 5).

**Detectado automaticamente (verificar):**
- sensor/produto **Planet (mosaicos e cenas)**: 62 ocorrências (p. 3, 4, 5, 6, 7)
- sensor/produto **Planet NICFI**: 21 ocorrências (p. 2, 3, 4, 5, 13)
- sensor/produto **Landsat**: 7 ocorrências (p. 3, 4, 5, 11, 15)
- conjunto de dados **PRODES**: 14 ocorrências (p. 3, 4, 5, 6, 11)
- conjunto de dados **Global Forest Change**: 6 ocorrências (p. 3, 5, 15, 16)
- resolução mencionada: 5 m (p. 3)
- resolução mencionada: 30 m (p. 3)
- “The model was tested in the Mato Grosso States in Brazil with the complete the Planet dataset from December 2015 to March 2022, corresponding to a total of 85056 images.” (p. 4, seção Início)
- “2.5 Training To produce the training sample of evergreen forest cover for the U-net model, 10 Planet images where randomly selected over Mato Grosso for each monthly Planet mosaic dates from September 2020 to September 2021 included, to con” (p. 6, seção 2.3 Deforestation history datasets)
- “We kept only 23 images where the forest segmentation was deemed accurate according to the visual interpretation of the forest and non-forest areas.” (p. 6, seção 2.3 Deforestation history datasets)
- “It is produced based on the visual interpretation of satellite imagery and manual mapping of deforestation by trained specialists over the course of the PRODES-year, which starts at August 1 [st] and ends on July 31 [st] de Almeida et al. .” (p. 3, seção Início)
- “These two products, PRODES and GFC tree loss year product, are reference datasets to monitor deforestation; however, they are delivered annually and at 30 m of spatial resolution.” (p. 3, seção Início)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Evidência (leitura) — Rótulos (como foram feitos):**

1. 10 imagens aleatórias por mosaico mensal de set/2020 a set/2021 → 130; 75 sem nuvem forte; o algoritmo **k-textures** (auto-segmentação não supervisionada, 8 classes) segmentou; 23 imagens aceitas por inspeção visual, com pequenas correções manuais (p. 6).
2. Primeira U-Net treinada e aplicada às 130; depois 21 imagens com nuvem/neblina fina entram para ensinar o modelo a tratar o que não é reconhecível como não-floresta.
3. Amostra final: 6.663 patches de 256 × 256 (6.187 com floresta, 476 só fundo), 80/20 → 5.331/1.332 (p. 6).
4. A produção das amostras levou "um par de dias", com mínima supervisão humana (p. 16).

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 26 ocorrências (p. 4, 5, 6, 7, 8)
- **Máscara de nuvem e sombra**: 12 ocorrências (p. 3, 6, 7, 8, 11)
- **Textura (GLCM)**: 12 ocorrências (p. 6, 14, 15, 16)
- **Mosaicos e compostos**: 10 ocorrências (p. 3, 4, 5, 6, 7)
- **Aumento de dados**: 6 ocorrências (p. 4, 6, 15)
- **Correção atmosférica / reflectância**: 3 ocorrências (p. 4)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Método:**

- U-Net clássica, entrada 256 × 256 × 4, saída 256 × 256 × 1 (limiar 0,5), 34,6 milhões de parâmetros; R + Keras/TensorFlow 2.8 (p. 6).
- Treino: Adam, lr 1e-4, perda BCE + Dice, batch 256, 20.000 épocas (melhor: 17.058; acurácia treino/val 99,40/97,70 %), augmentation só com flips H/V, ~12,5 h numa RTX 2080 (p. 7).
- **Filtro temporal de nuvem:** o pixel é floresta se detectado como floresta em pelo menos metade das observações da janela de ±3 datas; processamento do presente para o passado (p. 7).
- **Regras de confiança** (`trust` 1 confirmado, 2 muito provável, 3 não confirmado, só para a última data); desmatamento = pixel não-floresta na data N, confirmado quando N−1 e N coincidem (p. 7).

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 15 menções vs 3 de pares)
**Métodos detectados automaticamente:**
- método/família **U-Net**: 25 ocorrências (p. 3, 4, 6, 7, 8)
- método/família **CNN**: 4 ocorrências (p. 4, 16)
**Hiperparâmetros detectados automaticamente (verificar):**
- batch: “batch size of 256 images and the model with the be” (p. 7)
- épocas/iterações: “20000 epochs” (p. 7)
- perda: “binary cross-entropy and Dice coefficient-related lo” (p. 6)
- tamanho do patch: “256 × 256 pixel” (p. 6)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Amostra independente**: 2 ocorrências (p. 7, 15)
- **Teste externo / generalização**: 2 ocorrências (p. 15)
- métrica **F1**: 3 ocorrências (p. 7, 14, 17)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Métricas e resultados:**

- Validação em patches: OA 98,11 %, F1 0,982 (P 0,975, R 0,988) (p. 7).
- LiDAR: 94 % dos pixels "não-árvore" abaixo de 0,55 m; ~95 % dos "árvore" acima de 5 m (mediana 16,9 m) (p. 7).
- Cobertura 556.511 km² em 2015 (58,1 % do estado); 141.598 km² perdidos até 2021; desmatamento semestral mínimo 6.632 km² (2016-12), 19.818 km² em 2021-12 (p. 8).
- Contra o PRODES: 3,39 a 7,49 vezes mais área; interseção mediana por tile 67,2 % (2020); contra o GFC 0,71 a 3,49 vezes (p. 10, 11).

**Trechos numéricos detectados automaticamente (verificar):**
- “The network was trained for 20000 epochs with a batch size of 256 images and the model with the best weighted accuracy was kept for prediction (epoch 17058 and training/validation accuracy of 99.40 and 97.70% respectively and training/validation loss of 0.0088” (p. 7, seção 2.3 Deforestation history datasets)
- “3 Results 3.1 Tree cover validation with independent validation sample The tree cover algorithm presented a high level of segmentation accuracy, with an overall accuracy of 98.11% and an F1-Score of 0.982 (precision = 0.975, recall = 0.988) on the 1332 images ” (p. 7, seção 2.3 Deforestation history datasets)
- “arXiv Template A P REPRINT segment trees with a very high accuracy, that is, 98% non forest pixels have height below 5 m, and around 95 % of the tree cover pixels have height above 5 m.” (p. 8, seção 2.3 Deforestation history datasets)
- “For the tiles with similar results with our deforestation map, that is with more than 90% of intersections between our deforestation mapping and the Prodes or GFC tree loss year data, Fig.” (p. 12, seção 2.3 Deforestation history datasets)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites declarados:**

- O modelo não compara datas: não vê a "diminuição do número de árvores" e perde degradação sutil (p. 15).
- O filtro de ±3 datas **atrasa** a data do desmatamento nos anos semestrais; só fica consistente com o PRODES quando a série passa a ser mensal (p. 11, 14).
- Rios, bordas e erros de co-registro viram "desmatamento" nos primeiros anos; floresta caducifólia pode ser detectada como perda quando a série vira mensal (p. 16).
- Regeneração não é contabilizada; a definição de floresta (FAO) não é reproduzida; o último período tem nuvens residuais (p. 15, 16).
- Discordâncias fortes com PRODES/GFC vêm de **fogo contado como desmatamento** nesses produtos (p. 13).

**Trechos detectados automaticamente (verificar contexto):**
- “For example, with a simple rule, i.e., the forest attribution cannot change from forest to non-forest and to forest again.” (p. 15, seção 2.3 Deforestation history datasets)
- “In future work, the deep learning model with Planet NICFI images could be adapted to work with the times series, such as works made to detect deforestation with Landsat Matosak et al. , Maretto et al. , and to account for more subtle change” (p. 15, seção 2.3 Deforestation history datasets)
- “In future work, we will also include regrowing forest, as there is a significant amount of regrowing forests and they are very interesting for carbon sequestration, with the potential of contributing 5.5% to Brazil’s 2030 net emissions redu” (p. 16, seção 2.3 Deforestation history datasets)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 11)
- declaração: “Because of the ± 3 dates aggregation for cloud filtering, our deforestation data start to be consistent in time with PRODES only when monthly Planet data are available.” (p. 11)
- declaração: “7 funding This research received no external funding 8 Data availability The TensorFlow 2 U-net model with trained weights is available on Zenodo [https://doi.org/10.5281/zenodo.](https://doi.org/10.5281/zenodo.7324753) (https://doi.org/10.” (p. 17)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, otimizador (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo. Série 2015–2021 processada depois; o próprio artigo indica que, para detecção rápida, o autor aponta o radar (p. 16).
- menções de termos de monitoramento (contagem, não avaliação): Persistência / confirmação 5 (p. 7); Revisão humana 3 (p. 3, 6, 14); Alertas 1 (p. 16); Latência / frequência 1 (p. 3)

**Interpretação — O que reaproveitar:**

- **Receita de treino pronta para o EXP2:** U-Net 256 × 256 × 4, BCE + Dice, Adam 1e-4, flips, escala 8 bits sem correção atmosférica, borda espelhada na inferência.
- **Cadeia de rotulagem barata:** auto-segmentação por textura + escolha de classes + correção manual, mais amostras de nuvem/neblina como "não-floresta" explícito.
- **Regra de persistência** (a classe não pode ir floresta → não-floresta → floresta) e **nível de confiança por pixel**; ambas migram para a etapa E09 Pós-processamento e eventos.
- **Comparação com produtos oficiais por interseção por tile** ponderada pelo número de pixels, útil para E10 Avaliação e incerteza.
- **Validação com altura LiDAR** como referência independente do próprio rótulo.

**Interpretação — Cuidados para o nosso projeto (mosaicos mensais de 3–5 m):**

- Antes de set/2020 os mosaicos NICFI são semestrais; confirmar a cadência real dos nossos arquivos.
- A acurácia de 98 % é de **cobertura arbórea**, não de evento de mudança; medir precisão/recall dos eventos separadamente.
- A área mapeada não é a área estimada; usar amostragem probabilística ([[Olofsson_2014_GoodPracticesEstimating|Olofsson 2014]]).

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[PlanetNICFI|Planet NICFI (basemaps)]] — 21 ocorrências (p. 2, 3, 4, 5, 13)
- emprega conjunto de dados: [[PRODES|PRODES (INPE)]] — 14 ocorrências (p. 3, 4, 5, 6, 11)
- emprega conjunto de dados: [[GlobalForestChange|Global Forest Change (Hansen)]] — 6 ocorrências (p. 3, 5, 15, 16)
- utiliza método: [[UNet|U-Net]] — 25 ocorrências (p. 3, 4, 6, 7, 8)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 4 ocorrências (p. 4, 16)
- trata a tarefa: [[Desmatamento|Desmatamento]] — suporte vindo da leitura/título/resumo
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 26 ocorrências (p. 4, 5, 6, 7, 8)
- aplica etapa de preparo: [[MascaraNuvem|Máscara de nuvem e sombra]] — 12 ocorrências (p. 3, 6, 7, 8, 11)
- referência (curado pela leitura): [[Normalizacao|Normalização e escala radiométrica]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[Rotulagem|Rotulagem e anotação]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[AmostraIndependente|Amostra independente]] — suporte vindo da leitura/título/resumo
- é avaliado por: [[F1|F1]] — 3 ocorrências (p. 7, 14, 17)
- referência (curado pela leitura): [[AcuraciaGlobal|Acurácia global (OA)]] — suporte vindo da leitura/título/resumo

**Comparações substantivas com outros artigos:**
- este artigo tem lacuna complementada por [[Dalagnol_2023_MappingTropicalForest|Dalagnol 2023]] — P01 declara: (p. 15); P02 mapeia degradação com U-Net em Planet NICFI (leitura parcial).
- este artigo convergem na cadência do NICFI [[Vizzari_2022_PlanetScopeSentinelSentinel|Vizzari 2022]] — Ambos descrevem a cadência do NICFI: (p. 3); (§ 1).
- [[Zhang_2023_MonitoringMonthlyTropical|Zhang 2023]] é alternativa sem rótulos a este artigo — Ambos usam NICFI de ~5 m para a supressão de dossel: P91 usa o índice rHue e a persistência de 3 meses sem treinar modelo; P01 treina uma U-Net e deriva o desmatamento por diferença de mapas.
- [[Masolele_2024_MappingDiversityLand|Masolele 2024]] usa o mesmo mosaico NICFI de 4,77 m de este artigo — P102 classifica o uso após a perda do Hansen e P01 classifica a floresta por data; ambos usam as quatro bandas do NICFI.
- [[Wang_2024_ValidationDeforestationHigh|Wang 2024]] compartilha o produto NICFI e o alvo de este artigo — P04 valida alertas de desmatamento com par NICFI e U-Net bitemporal (F1 0,83), enquanto P01 classifica por data.
- [[Carter_2024_DetectionForestDisturbance|Carter 2024]] replica a receita de este artigo — P03 aplica a ideia de P01 (U-Net por data e perda por diferença anual) ao produto visual RGB do PlanetScope e valida a perda contra LiDAR e CALFIRE.

## Figuras selecionadas

![[Wagner_2023_MappingTropicalForest_p5_Figure1.png|520]]
*Figure 1: Planet NICFI mosaic of September 2021 constituted of the 2658 Planet image tiles covering the Mato Grosso (p. 5; recorte do PDF convertido)*

![[Wagner_2023_MappingTropicalForest_p9_Figure4.png|520]]
*Figure 4: Tree cover and tree cover loss per year for the 2658 Planet tiles covering the Mato Grosso State - Brazil, with (p. 9; recorte do PDF convertido)*


## Anotações do leitor

- 
