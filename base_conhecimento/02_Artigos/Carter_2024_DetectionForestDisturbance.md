---
tipo: artigo
id_origem: P03
titulo: "Detection of forest disturbance across California using deep-learning on PlanetScope imagery"
ano: 2024
autores: ["Griffin Carter", "Fabien Hubert Wagner", "Ricardo Dalagnol", "Sophia Roberts", "Alison L. Ritz", "Sassan S Saatchi"]
doi: "10.3389/frsen.2024.1409400"
arquivo_fonte: "coleta/P03_Carter2024_Detection-of-forest-disturbance-across-California-using-deep.pdf"
markdown_fonte: "output/pdf/P03_Carter2024_Detection-of-forest-disturbance-across-California-using-deep/document.md"
paginas: 15
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
tarefas: ["[[DegradacaoFlorestal|Degradação e perturbação florestal]]", "[[Edificacoes|Edificações e urbanização]]"]
sensores: ["[[PlanetScope|PlanetScope (Dove/SuperDove)]]", "[[PlanetProdutos|Produtos Planet (visão geral)]]", "[[PlanetNICFI|Planet NICFI (basemaps)]]"]
conjuntos_dados: ["[[GlobalForestChange|Global Forest Change (Hansen)]]"]
metodos: ["[[UNet|U-Net]]", "[[CNN|Redes convolucionais (CNN)]]", "[[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]]"]
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]", "[[MosaicosCompostos|Mosaicos e compostos temporais]]", "[[Textura|Textura (GLCM)]]", "[[Rotulagem|Rotulagem e anotação]]", "[[AumentoDados|Aumento de dados]]"]
validacao: ["[[AmostraIndependente|Amostra independente]]", "[[PrecisaoRecall|Precisão e recall]]", "[[F1|F1]]", "[[AcuraciaGlobal|Acurácia global (OA)]]", "[[EstimativaArea|Estimativa de área com intervalo de confiança]]"]
ferramentas: []
tags: [artigo, leitura/profunda]
---

# Carter 2024 — Detection of forest disturbance across California using deep-learning on PlanetScope imagery

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Griffin Carter, Fabien Hubert Wagner, Ricardo Dalagnol, Sophia Roberts et al. (2024). Detection of forest disturbance across California using deep-learning on PlanetScope imagery. Frontiers in Remote Sensing. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.3389/frsen.2024.1409400
- **Arquivo de origem:** `coleta/P03_Carter2024_Detection-of-forest-disturbance-across-California-using-deep.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P03_Carter2024_Detection-of-forest-disturbance-across-California-using-deep/document.md` — 15 páginas, 19 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Mapear **cobertura arbórea mensal** e **perturbação florestal anual** em toda a Califórnia (423.971 km²) com a **base visual RGB do PlanetScope (4,77 m)** e uma U-Net, no período 2020–2022 (p. 1–2). A mudança é derivada comparando mapas anuais, não por um modelo temporal.

- “We introduce a novel method of tracking California forest cover using a supervised U-Net deep learning architecture and PlanetScope’s Visual dataset which provides 3-band RGB (Red, Green, and Blue) mosaicked imagery.” (p. 1, seção Início)
- “We compared our high-resolution disturbance maps with wildfire GIS survey data from CALFIRE, and satellitebased forest cover changes and achieved an F-1 score of 54% and 88% respectively.” (p. 1, seção Início)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The highest observed forest loss rate was located at the Sierra Nevada mountains at 21.4% of the forested area being disturbed between 2020 and 2021.” (p. 1, seção Início)
- “Our study site covers the entire state boundary of California, United States (Figure 1).” (p. 2, seção 2.1 Study site)
- “From 2020 to 2021, California maintained 30,923.5 sq km of forest while 5,994.9 sq km were disturbed.” (p. 1, seção Início)
- “The highest observed forest loss rate was located at the Sierra Nevada mountains at 21.4% of the forested area being disturbed between 2020 and 2021.” (p. 1, seção Início)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- Mosaicos mensais PlanetScope **visuais (3 bandas RGB, 8 bits)**, jan/2020 a dez/2022, 1.866 tiles de 20 × 20 km (4.096 × 4.096 px), obtidos pela API da Planet; **nenhum pré-processamento** foi aplicado (p. 3–4).
- Referência independente: LiDAR aéreo (USGS e NEON, 2018–2020; 11 sítios NEON), modelos de altura de dossel de 1 m agregados para 4,77 m; 1.000 de 9.188 tiles de altura foram sorteados como referência (p. 4).
- Comparações: perímetros de incêndio e manejo do **CALFIRE** e o **Global Forest Change** (30 m) (p. 6).

**Detectado automaticamente (verificar):**
- sensor/produto **PlanetScope**: 15 ocorrências (p. 1, 2, 3, 4, 11)
- sensor/produto **Planet (mosaicos e cenas)**: 12 ocorrências (p. 2, 4, 5, 12, 13)
- sensor/produto **Planet NICFI**: 3 ocorrências (p. 2, 12, 13)
- sensor/produto **Sentinel-2**: 3 ocorrências (p. 2, 13)
- conjunto de dados **Global Forest Change**: 3 ocorrências (p. 2, 6)
- resolução mencionada: 500 m (p. 1)
- resolução mencionada: 5 m (p. 1)
- resolução mencionada: 4.77 m (p. 1)
- “These data are organized in 1,866 tiles of 20 km × 20 km (4,096 × 4,096 pixels) covering the entirety of California, United States (Figure 1).” (p. 4, seção 2.2 PlanetScope satellite images)
- “From the total 8113.8 km of forest covered by 9188 canopy height tiles, we randomly selected 1,000 tiles to be used as our reference data which covered 895 km .” (p. 4, seção 2.3 Airborne LiDAR data)
- “After verifying the k-texture results on the 120 images, the training dataset consisted of 3930 training samples of 256 × 256 pixels extracted from 23 images where the forest segmentation was deemed accurate according to visual interpretati” (p. 4, seção 2.5 Label production and training)
- “From the total 8113.8 km of forest covered by 9188 canopy height tiles, we randomly selected 1,000 tiles to be used as our reference data which covered 895 km .” (p. 4, seção 2.3 Airborne LiDAR data)
- “After verifying the k-texture results on the 120 images, the training dataset consisted of 3930 training samples of 256 × 256 pixels extracted from 23 images where the forest segmentation was deemed accurate according to visual interpretati” (p. 4, seção 2.5 Label production and training)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Evidência (leitura) — Rótulos:**

- Processo iterativo de **aprendizado ativo**: 120 imagens sorteadas no espaço e no tempo; auto-segmentação com **k-textures** (7 classes), escolha das classes de floresta por inspeção, correção manual de pequenos erros (p. 4).
- Três iterações: base de 3.930 patches de 23 imagens; +21 imagens (água, florestas mistas, arbustos); +69 imagens (áreas queimadas, neblina leve e nuvem fina). Nuvem espessa e neblina forte foram removidas (p. 4).
- Conjunto final: **7.141 patches 256 × 256** (3.524 com floresta e não floresta; 3.617 só não floresta), 80 % treino (5.713) e 20 % validação (1.428) (p. 4).

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 24 ocorrências (p. 1, 2, 3, 4, 5)
- **Mosaicos e compostos**: 22 ocorrências (p. 1, 2, 3, 4, 5)
- **Textura (GLCM)**: 8 ocorrências (p. 3, 4, 12, 13)
- **Rotulagem / anotação**: 5 ocorrências (p. 4, 12, 13)
- **Aumento de dados**: 3 ocorrências (p. 4, 5)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Método:**

- **U-Net clássica**, entrada 256 × 256 × 3, saída binária (limiar 0,5), em R com Keras/TensorFlow 2.8 (p. 4).
- Treino: perda = entropia cruzada binária + Dice; **Adam, lr 1e-4**; **25.000 épocas, batch 256**; melhor época 22.794 (acurácia treino/validação 98,97 %/95,02 %); ~12 h numa instância AWS g5.4xlarge (GPU A10G, 24 GB). Aumento de dados: só flips H/V (p. 4–5).
- Inferência: tiles com **borda espelhada de 256 px**; ~9 s por tile; 1.866 tiles × 36 meses (p. 5).
- **Pós-processamento temporal anual:** filtro de maioria sobre os 12 meses (soma ≥ 7) ou só sobre abril–outubro (soma ≥ 4) quando a elevação passa de 1.000 m ou a face do terreno é norte (aspecto >300° ou <60°), usando SRTM, para reduzir sombra e neve (p. 5). As trajetórias dos mapas anuais dão estável, perda e ganho (p. 5).

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **U-Net**: 22 ocorrências (p. 1, 2, 3, 4, 6)
- método/família **CNN**: 7 ocorrências (p. 1, 2, 12, 13)
- método/família **Semi/auto-supervisionado**: 3 ocorrências (p. 3, 4, 13)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 0.0001” (p. 4)
- batch: “batch size of 256 images and the model with the be” (p. 4)
- épocas/iterações: “25,000 epochs” (p. 4)
- otimizador: “Adam optimizer with a learning rate of 0” (p. 4)
- perda: “binary cross-entropy and Dice coefficient-related lo” (p. 4)
- tamanho do patch: “256 × 256 pixel” (p. 3)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Evidência (leitura) — Divisão e métricas:**

- Acurácia e F1 sobre os 20 % de validação do **próprio conjunto rotulado**; validação independente por altura LiDAR com limiar de 5 m (definição IGBP); F1 contra CALFIRE e interseção ponderada contra o GFC (p. 6).

**Detectado automaticamente (verificar):**
- **Amostra independente**: 3 ocorrências (p. 1, 6, 13)
- métrica **Precisão/Recall**: 8 ocorrências (p. 1, 6, 7)
- métrica **F1**: 3 ocorrências (p. 6, 7)
- métrica **Acurácia global**: 3 ocorrências (p. 1, 6, 13)
- métrica **Estimativa de área**: 3 ocorrências (p. 6, 12)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Resultados:**

- Validação interna: acurácia de treino 98,97 %, validação 95,5 %, precisão 82 %, recall 74 %, F1 0,778 (p. 6).
- LiDAR (mapas mensais de jun/2019): acurácia global **77,77 %**; diferença de altura média entre floresta e não floresta de 29,87 m (p. 6). Composto anual: 77,30 % (p. 7).
- Perda vs CALFIRE: **F1 54,5 %** em geral e 71,8 % na região do Creek Fire; 30 % da área do perímetro já era não floresta antes do incêndio (p. 7).
- Interseção ponderada com a perda do GFC: **88,0 %** (p. 11).
- Área florestal da Califórnia: 17.042.654 ha (2020), 14.283.221 ha (2021) e 16.547.832 ha (2022); perda de 2020–2021 de 2.756.433 ha e ganho de 2.264.611 ha em 2021–2022 (p. 7–9, 11, 13).
- O modelo encontra em média ~55 % mais área florestal que o GFC, atribuído à resolução (p. 11, 12).

**Trechos numéricos detectados automaticamente (verificar):**
- “The network was trained for 25,000 epochs with a batch size of 256 images and the model with the best weighted accuracy was kept for prediction (epoch 22,794 and training/validation accuracy of 98.97% and 95.02%, respectively, and training/validation loss of 0” (p. 4, seção 21 more images to increase the robustness of the a)
- “Our U-net model has a training accuracy of 98.97%, validation accuracy of 95.5%, a precision of 82%, a recall of 74%, and an F-1 score of 0.778.” (p. 6, seção 3.1 Training validation)
- “The validation accuracy is conducted over the 20% of the training dataset that is not included in the training of the U-net to ensure independence.” (p. 6, seção 3.1 Training validation)
- “Setting the height threshold at 5 m, according to the International Geosphere-Biosphere Program (IGBP) definition for forest cover, we saw an overall accuracy of 77.77%, an 82% precision of pixels predicted as forest cover and 74% precision of pixels predicted” (p. 6, seção 3.2 Validation of individual predictions using)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites declarados e observações:**

- Sombra diferencial em encostas e neve em alta altitude geram erro; a face norte e as altitudes são tratadas por regra, não por modelo (p. 5, 13).
- Chaparral e vegetação baixa (< 5 m) são difíceis; o limiar de 5 m pode excluí-los (p. 12).
- Rebrota e verdejamento após incêndio aparecem como "ganho": parte da oscilação perda/ganho é artefato (p. 9, 12).
- Só RGB: a ausência do NIR pode piorar a separação; deixam o teste 3 vs 4 bandas para o futuro (p. 13).
- **Observações minhas (inconsistências internas):** a acurácia de validação aparece como 95,5 % (p. 6) e 95,02 % (p. 4, 12); a cobertura de 2020 é 40,1 % (p. 7) e 44,7 % (p. 12); a conclusão diz "acurácia global de 82 %" para o composto anual (p. 13), enquanto o valor reportado na seção de resultados é 77,30 % (p. 7), e 82 % é a precisão da classe floresta. A perda foi validada só contra perímetros do CALFIRE (que o próprio artigo diz serem superestimados) e contra o GFC; não há amostra probabilística de eventos.

**Trechos detectados automaticamente (verificar contexto):**
- “These limitations can be circumvented by using AI and cloud computing optimization techniques.” (p. 2, seção 1 Introduction)
- “The CALFIRE dataset is the most up to date data on fire and logging available in California but presents limitations such as areas which may be shown as undisturbed forest within the disturbed polygons perimeter, or disturbed forests outsid” (p. 6, seção 2.8 Validation and comparison with)
- “A limitation for our model comes from the topography and seasonality of California.” (p. 13, seção 4.5 Topography and seasonality of data)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- Código: não informado; os dados "estarão disponíveis mediante solicitação razoável" (p. 13). Hiperparâmetros e arquitetura estão descritos; o código do k-textures é citado (Wagner et al., 2022).

- **Código/dados:** declarado sem URL localizada (p. 13)
- declaração: “The creation of such accurate, high resolution forest cover maps at a wide range of scales can help track and monitor forest changes across various biomes. ## Data availability statement The raw data supporting the conclusion of this articl” (p. 13)

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo. Mapas mensais e anuais de 2020–2022 processados depois; sem medição de latência.
- menções de termos de monitoramento (contagem, não avaliação): Latência / frequência 1 (p. 2); Revisão humana 1 (p. 4)

**Interpretação — O que reaproveitar:**

- **Mesma receita de P01 sobre produto RGB visual**, com rótulos gerados por k-textures e três ciclos de aprendizado ativo, bom para o caso em que os mosaicos do projeto não tenham NIR.
- **Filtro temporal condicionado por elevação e aspecto** para neve e sombra.
- **Validação por altura LiDAR** como referência independente do rótulo.
- **Perda e ganho como trajetória de mapas anuais** e a ressalva de que "ganho" após incêndio pode ser rebrota.

**Interpretação — Cuidados para o nosso projeto:**

- Os números de acurácia medem **cobertura**, não evento; a perda tem F1 de 54,5 % contra uma referência frágil.
- O modelo é por data e anual; não mede data da mudança nem latência (retrospectivo).

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[PlanetScope|PlanetScope (Dove/SuperDove)]] — 15 ocorrências (p. 1, 2, 3, 4, 11)
- utiliza dado/sensor: [[PlanetProdutos|Produtos Planet (visão geral)]] — 12 ocorrências (p. 2, 4, 5, 12, 13)
- utiliza dado/sensor: [[PlanetNICFI|Planet NICFI (basemaps)]] — 3 ocorrências (p. 2, 12, 13)
- emprega conjunto de dados: [[GlobalForestChange|Global Forest Change (Hansen)]] — 3 ocorrências (p. 2, 6)
- utiliza método: [[UNet|U-Net]] — 22 ocorrências (p. 1, 2, 3, 4, 6)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 7 ocorrências (p. 1, 2, 12, 13)
- utiliza método: [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 3 ocorrências (p. 3, 4, 13)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 8 ocorrências (p. 1, 6, 7)
- é avaliado por: [[F1|F1]] — 3 ocorrências (p. 6, 7)
- é avaliado por: [[AcuraciaGlobal|Acurácia global (OA)]] — 3 ocorrências (p. 1, 6, 13)
- é avaliado por: [[EstimativaArea|Estimativa de área com intervalo de confiança]] — 3 ocorrências (p. 6, 12)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 24 ocorrências (p. 1, 2, 3, 4, 5)
- aplica etapa de preparo: [[MosaicosCompostos|Mosaicos e compostos temporais]] — 22 ocorrências (p. 1, 2, 3, 4, 5)
- aplica etapa de preparo: [[Textura|Textura (GLCM)]] — 8 ocorrências (p. 3, 4, 12, 13)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 5 ocorrências (p. 4, 12, 13)
- aplica etapa de preparo: [[AumentoDados|Aumento de dados]] — 3 ocorrências (p. 4, 5)
- adota desenho de validação: [[AmostraIndependente|Amostra independente]] — 3 ocorrências (p. 1, 6, 13)
- trata a tarefa: [[DegradacaoFlorestal|Degradação e perturbação florestal]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo

## Figuras selecionadas

![[Carter_2024_DetectionForestDisturbance_p3_FIGURE1.png|520]]
*FIGURE 1 (p. 3; recorte do PDF convertido)*

![[Carter_2024_DetectionForestDisturbance_p3_FIGURE2.png|520]]
*FIGURE 2 (p. 3; recorte do PDF convertido)*


## Anotações do leitor

- 
