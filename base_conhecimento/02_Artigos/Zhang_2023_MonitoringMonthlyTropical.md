---
tipo: artigo
id_origem: P91
titulo: "Monitoring monthly tropical humid forest disturbances with Planet NICFI images in Cameroon"
ano: 2023
autores: ["Yihang Zhang", "Xia Wang", "Xiaodong Li", "Yun Du", "Peter M. Atkinson"]
doi: "10.1016/j.agrformet.2023.109676"
arquivo_fonte: "coleta/P91_Zhang2023_Monitoring-monthly-tropical-humid-forest-disturbances-with-P.pdf"
markdown_fonte: "output/pdf/P91_Zhang2023_Monitoring-monthly-tropical-humid-forest-disturbances-with-P/document.md"
paginas: 30
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "A"
tarefas: ["[[Desmatamento|Desmatamento]]", "[[DegradacaoFlorestal|Degradação e perturbação florestal]]"]
sensores: ["[[PlanetNICFI|Planet NICFI (basemaps)]]"]
conjuntos_dados: ["[[GlobalForestChange|Global Forest Change (Hansen)]]"]
metodos: ["[[RandomForest|Random Forest]]"]
preparo: ["[[MascaraNuvem|Máscara de nuvem e sombra]]", "[[IndicesEspectrais|Índices espectrais (NDVI etc.)]]"]
validacao: ["[[EstimativaArea|Estimativa de área com intervalo de confiança]]"]
ferramentas: ["[[GoogleEarthEngine|Google Earth Engine]]"]
tags: [artigo, leitura/profunda, relevancia/A]
---

# Zhang 2023 — Monitoring monthly tropical humid forest disturbances with Planet NICFI images in Cameroon

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **A** — NICFI mensal de 5 m para perda de dossel sem rótulos de treino (índice rHue e persistência de 3 meses); amostragem estratificada com três intérpretes.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Yihang Zhang, Xia Wang, Xiaodong Li, Yun Du et al. (2023). Monitoring monthly tropical humid forest disturbances with Planet NICFI images in Cameroon. Agricultural and Forest Meteorology. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1016/j.agrformet.2023.109676
- **Arquivo de origem:** `coleta/P91_Zhang2023_Monitoring-monthly-tropical-humid-forest-disturbances-with-P.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P91_Zhang2023_Monitoring-monthly-tropical-humid-forest-disturbances-with-P/document.md` — 30 páginas, 71 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Mapear **mensalmente** perturbações florestais de pequena escala (corte seletivo e roça de pequenos agricultores) na floresta úmida de **Camarões** (475.442 km²) em **2021**, com mosaicos mensais **Planet NICFI de 4,77 m (~5 m)**, de forma automática e **sem treinar modelo supervisionado** (p. 1–5).

- “In this paper, we develop a method to monitor monthly small-scale 20 tropical humid forest disturbances using 2021 Planet NICFI images.” (p. 1, seção 12 Chinese Academy of Sciences, Wuhan 430074, China;)
- “3, we developed a spatio-temporal filter to 12 / 30” (p. 12, seção 0 otherwise)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The entire CAM, which is a typical area 121 of selective logging and smallholder clearing in the Congo’s tropical forests (Tyukavina et al., 2018), 122 was chosen as the study site, and it is expected to use the proposed method to monitor h” (p. 5, seção 50 m Annual 2019-2022)
- “Study site and dataset 126 As shown in Fig.” (p. 5, seção 50 m Annual 2019-2022)
- “(2014) used 54 ALOS/ALOS-2 PALSAR/PALSAR-2, a dual-pole L-band Synthetic Aperture Radar (SAR), during 55 2007-2010 and 2015-2017 to estimate global forest cover maps with a spatial resolution of 25 m.” (p. 2, seção 44 Vancutsem et al., 2021; Zhu and Woodcock, 2014).)
- “(2021) 65 developed a 50 m spatial resolution near real-time forest early warning system in the tropics (JJ-FAST) 66 by using ALOS-2 PALSAR-2 mosaics during 2019-2022.” (p. 3, seção 59 disturbances (Francini et al., 2020).)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- **NICFI mensal, 4 bandas (azul, verde, vermelho, NIR), 16 bits convertidos em reflectância de superfície**, pré-processados pelo NICFI no GEE, harmonizados entre satélites Dove/SuperDove e coregistrados por pontos de controle (p. 6–7). Os mosaicos são mensais a partir de set/2020 e semestrais antes (p. 5).
- **Mapa de floresta úmida primária de 2020**, construído por fusão de cinco produtos: mapa de 2001 (Turubanova), perda do GFC 2001–2020, alertas RADD Sentinel-1 2019–2020, altura de dossel Landsat (limiar de 15 m) e cobertura Sentinel-2 de 2020 (p. 6, 10).
- Comparação com RADD (10 m), GLAD (30 m) e GFC (30 m) (p. 14, 18–20).

**Detectado automaticamente (verificar):**
- sensor/produto **Planet (mosaicos e cenas)**: 87 ocorrências (p. 1, 2, 4, 5, 6)
- sensor/produto **Planet NICFI**: 56 ocorrências (p. 1, 2, 5, 6, 7)
- sensor/produto **Landsat**: 38 ocorrências (p. 1, 2, 3, 4, 5)
- sensor/produto **Sentinel-1**: 25 ocorrências (p. 1, 3, 4, 5, 6)
- conjunto de dados **Global Forest Change**: 11 ocorrências (p. 2, 5, 6, 10, 14)
- resolução mencionada: 10 m (p. 2)
- resolução mencionada: 250 m (p. 2)
- resolução mencionada: 25 m (p. 2)
- “(2021) applied Landsat 53 images to map 30 m global VCF and forest cover changes every five years.” (p. 2, seção 44 Vancutsem et al., 2021; Zhu and Woodcock, 2014).)
- “(2021) developed a 10 m forest disturbance alerting system based on 69 Sentinel-1 C-band SAR images, with the benefit of penetrating smoke, clouds and rain and a finer spatial 70 resolution compared to Landsat and PALSAR-2 images.” (p. 3, seção 59 disturbances (Francini et al., 2020).)
- “By analyzing two widely used humid tropical forest 136 disturbances based on Landsat images (Hansen et al., 2016) and Sentinel-1 images (Reiche et al., 2021), 137 we found that there were more forest disturbances during 2021 in CAM than in ” (p. 5, seção 50 m Annual 2019-2022)
- “Specifically, the time-series monthly Planet NICFI images were used 181 for the determination process based on visual interpretation.” (p. 7, seção 50 m Annual 2019-2022)
- “To decrease the uncertainty of visual interpretation, three experienced 183 interpreters interpreted visually the reference class of each sample unit with the help of time-series 184 monthly Planet NICFI images and very fine spatial resolut” (p. 7, seção 50 m Annual 2019-2022)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Máscara de nuvem e sombra**: 25 ocorrências (p. 1, 3, 8, 9, 10)
- **Mosaicos e compostos**: 16 ocorrências (p. 3, 5, 6, 7, 9)
- **Índices espectrais**: 7 ocorrências (p. 7, 26, 29, 30)
- **Recorte em patches/tiles**: 7 ocorrências (p. 6, 13, 18, 21)
- **Normalização / escala**: 2 ocorrências (p. 7, 29)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Método (sem aprendizado profundo):**

1. **Máscara de nuvem** por mês: floresta aleatória gerando mapa de probabilidade de nuvem (treinada com amostras visuais tiradas do composto de máximo anual; limiares de 20 % a 40 % por estação) e **índice HOT** (limiares 0,016–0,028) (p. 9–10).
2. **Índice rHue_forest:** índice Hue (do Francini et al., 2020) restrito à floresta primária e **referenciado à mediana local** (filtro circular de raio 300 m), com limites −0,1 e 0,3 (p. 11–12, eqs. 2–6).
3. **Detecção possível:** primeiro mês em que rHue_forest > T, com T = 0,09 (faixa sugerida 0,06–0,12) e valor anterior abaixo de T (p. 12–13, eq. 7).
4. **Filtro espaço-temporal:** a perturbação só é confirmada se persistir em ≥ 3 de 5 observações (um mês antes e três depois); remoção de manchas com < 7 pixels numa janela de 15 × 15 (p. 13, eqs. 8–10).

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 12 menções vs 1 de pares)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Amostragem estratificada**: 9 ocorrências (p. 5, 7, 14, 15, 20)
- métrica **Estimativa de área**: 12 ocorrências (p. 1, 5, 7, 14, 15)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Validação e resultados:**

- **Amostragem estratificada (Stehman/Olofsson):** 14 estratos, **1.400 pontos** (50 por mês de perturbação, 400 para floresta estável e 400 para outras coberturas); unidade 5 × 5 m; **três intérpretes** com apoio de séries NICFI e Google Earth de 0,5 m, **discordância de 32,43 %**; referência por maioria (p. 7–8, tabela 2).
- **Mapa possível:** acurácia do produtor 96,85 ± 2,65 % e do usuário 21,37 ± 16,91 % (muitos falsos positivos) (p. 20–21, tabela 3).
- **Mapa ajustado:** acurácia do usuário **84,67 ± 2,89 %** e do produtor **61,46 ± 46,43 %**; área perturbada em 2021 de **1.168 ± 882 km²** (p. 20, tabela 3). O intervalo de confiança do produtor é muito largo.
- Por mês, a acurácia do usuário ajustada varia de 58 % (jul.) a 86 % (fev.) (tabela 3, p. 21).
- Em comparação visual, o método NICFI recupera estradas de extração estreitas e clareiras pequenas que RADD (suavizado, manchas < 0,2 ha) e GLAD/GFC (Landsat) perdem (p. 18).
- A vegetação rebrota em 2–4 meses nas clareiras menores, então só imagens frequentes veem a abertura (p. 17).
- Latência: o mapa "possível" alerta ao receber a imagem; o "ajustado" exige ≥ 3 meses depois do evento (p. 23–24). Processamento de Camarões em 214 células no GEE, ~1 semana com uma conta (p. 24).

**Trechos numéricos detectados automaticamente (verificar):**
- “216 We, therefore, collected cloud and non-cloud sample pixels by visual interpretation, which were used in 217 the RF model to establish the cloud cover possibility map for monthly Planet NICIF images, and 218 threshold values ranging from 20% to 40% were use” (p. 9, seção 50 m Annual 2019-2022)
- “As listed in Table 3, the possible monthly forest disturbance from January to December has the 450 best producer’s accuracy of 96.85 ± 2.65% but the least user’s accuracy of 21.37 ± 16.91%, which means 451 it has many commission errors (false positives).” (p. 20, seção 0 otherwise)
- “By contrast, the adjusted monthly forest disturbance map 452 has the best user’s accuracy of 84.67 ± 2.89% by eliminating many false positives with the spatio 453 temporal filer, but its producer’s accuracy, 61.46 ± 46.43%, is not that good, which means it has” (p. 20, seção 0 otherwise)
- “For the adjusted monthly forest disturbance map, the user’s accuracy 455 and producer’s accuracy of other land covers and stable humid forest are 88.50 ± 3.13% and 88.71 ± 456 2.72%, respectively.” (p. 20, seção 0 otherwise)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites declarados e observações:**

- Nuvens remanescentes, sombras e erros de registro geram falsos positivos; o filtro também remove perturbações reais onde há muita nuvem; florestas decíduas ou com floração forte inflam a perturbação; degradação sub-pixel não é detectada (p. 24–25).
- A incerteza do mapa de floresta primária de 2020 propaga-se ao resultado (p. 25).
- **Observações minhas:** (a) o produtor de 61 % com ±46 % mostra que **a taxa de omissão é pouco conhecida**; (b) as tabelas extraídas trocam a ordem das colunas de usuário/produtor entre o texto e a tabela 3; usei os valores do resumo e do texto, que são coerentes; (c) há **apenas um ano e um país**; (d) a taxa de 32 % de discordância entre intérpretes limita o teto da referência; (e) T e o número de confirmações foram escolhidos por inspeção visual em dois locais (p. 21–23), sem validação independente do ajuste.

**Trechos detectados automaticamente (verificar contexto):**
- “529 5.2 Limitation and uncertainty 530 To improve the mapping of small-scale forest disturbances caused by selective logging and 531 smallholder clearing, we developed a rHueforest index and spatio-temporal filter to monitor possible 532 an” (p. 24, seção 0 otherwise)
- “579 5.3 Future research 580 Compared with the forest disturbance maps based on RADD Sentinel-1 and GFC Landsat, the 581 developed Planet NICFI possible and adjusted monthly forest disturbance maps also cannot find the 582 forest loss that o” (p. 26, seção 0 otherwise)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- Método baseado em índices e GEE; o texto lido não cita repositório de código; **não informado**. Parâmetros numéricos descritos (p. 9–13).

- **Código/dados:** não informado
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo. Um ano de NICFI mensal processado depois; o mapa "possível" alerta ao receber o mosaico, e o "ajustado" exige 3 meses de confirmação (p. 23–24).
- menções de termos de monitoramento (contagem, não avaliação): Alertas 10 (p. 3, 18, 19, 26, 28); Quase tempo real 9 (p. 2, 3, 4, 5, 11); Latência / frequência 5 (p. 3, 4, 24, 27); Revisão humana 3 (p. 7, 9); Persistência / confirmação 2 (p. 23, 29)

**Interpretação — O que reaproveitar:**

- **Receita de monitoramento mensal com NICFI sem rótulos:** máscara de nuvem (RF + HOT), índice Hue referenciado à vizinhança, limiar T ≈ 0,09 e **persistência de ≥ 3 meses**, como linha de base interpretável contra a qual comparar um modelo profundo.
- **Pareamento de dois mapas (possível e ajustado)** para tratar a troca entre latência e precisão.
- **Protocolo de validação** com amostragem estratificada por mês, três intérpretes e estimativa de área com intervalo.
- **Máscara prévia de floresta** para restringir a detecção e reduzir falsos positivos.

**Interpretação — Cuidados para o nosso projeto:**

- Alvo é perda de dossel em floresta úmida; para edificações e estradas, o índice Hue não se aplica diretamente.
- Hue depende de RGB e é sensível a fenologia; em biomas secos haverá mais falsos positivos (ver P09, floresta seca).

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[PlanetNICFI|Planet NICFI (basemaps)]] — 56 ocorrências (p. 1, 2, 5, 6, 7)
- emprega conjunto de dados: [[GlobalForestChange|Global Forest Change (Hansen)]] — 11 ocorrências (p. 2, 5, 6, 10, 14)
- usa ferramenta: [[GoogleEarthEngine|Google Earth Engine]] — 5 ocorrências (p. 6, 24, 26)
- aplica etapa de preparo: [[MascaraNuvem|Máscara de nuvem e sombra]] — 25 ocorrências (p. 1, 3, 8, 9, 10)
- aplica etapa de preparo: [[IndicesEspectrais|Índices espectrais (NDVI etc.)]] — 7 ocorrências (p. 7, 26, 29, 30)
- referência (curado pela leitura): [[RandomForest|Random Forest]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[Desmatamento|Desmatamento]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[DegradacaoFlorestal|Degradação e perturbação florestal]] — suporte vindo da leitura/título/resumo
- referencia (suporte manual da leitura): [[PosProcessamentoTemporal|Pós-processamento temporal (persistência, janela e colapso)]] — suporte vindo da leitura/título/resumo
- referencia (suporte manual da leitura): [[AmostragemEstratificada|Amostragem estratificada]] — suporte vindo da leitura/título/resumo
- referencia (suporte manual da leitura): [[ReferenciaVisual|Referência por interpretação visual]] — suporte vindo da leitura/título/resumo
- discute aspecto de monitoramento: [[Alertas|Alertas de mudança]] — 10 ocorrências (p. 3, 18, 19, 26, 28)
- referência (curado pela leitura): [[PersistenciaConfirmacao|Persistência e confirmação]] — suporte vindo da leitura/título/resumo
- é avaliado por: [[EstimativaArea|Estimativa de área com intervalo de confiança]] — 12 ocorrências (p. 1, 5, 7, 14, 15)

**Comparações substantivas com outros artigos:**
- este artigo é alternativa sem rótulos a [[Wagner_2023_MappingTropicalForest|Wagner 2023]] — Ambos usam NICFI de ~5 m para a supressão de dossel: P91 usa o índice rHue e a persistência de 3 meses sem treinar modelo; P01 treina uma U-Net e deriva o desmatamento por diferença de mapas.
- este artigo compara-se com o alerta de [[Reiche_2021_ForestDisturbanceAlerts|Reiche 2021]] — P91 compara seu mapa NICFI mensal com RADD (P119), GLAD e GFC; o RADD suaviza manchas pequenas (< 0,2 ha), que o NICFI recupera (p. 18).
- [[Masolele_2024_MappingDiversityLand|Masolele 2024]] complementa este artigo — P91 detecta a perda de dossel mensal e P102 classifica o uso da terra que sucede a perda; juntos cobrem onde e o que veio depois com NICFI de 5 m (interpretação).

## Anotações do leitor

- 
