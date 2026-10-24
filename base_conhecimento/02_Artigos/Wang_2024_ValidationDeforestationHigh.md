---
tipo: artigo
id_origem: P04
titulo: "AI-based Validation of Deforestation Using High-Resolution Satellite Imagery in the Brazilian Amazon"
ano: 2024
autores: ["Zhihao Wang", "Zhili Li", "Yiqun Xie", "Carlos Eduardo A. Souza", "Jailson Soares Souza Filho", "Stefany P. Costa"]
doi: "10.5194/isprs-archives-XLVIII-3-2024-583-2024"
arquivo_fonte: "coleta/P04_Wang2024_AI-based-Validation-of-Deforestation-Using-High-Resolution-S.pdf"
markdown_fonte: "output/pdf/P04_Wang2024_AI-based-Validation-of-Deforestation-Using-High-Resolution-S/document.md"
paginas: 6
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "A"
tarefas: ["[[Desmatamento|Desmatamento]]"]
sensores: ["[[PlanetNICFI|Planet NICFI (basemaps)]]"]
conjuntos_dados: ["[[DETER|DETER (INPE)]]"]
metodos: ["[[UNet|U-Net]]"]
preparo: []
validacao: ["[[Desbalanceamento|Desbalanceamento de classes]]"]
ferramentas: []
tags: [artigo, leitura/profunda, relevancia/A]
---

# Wang 2024 — AI-based Validation of Deforestation Using High-Resolution Satellite Imagery in the Brazilian Amazon

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **A** — Par NICFI antes e depois com U-Net bitemporal de supressão (F1 0,83), mas divisão aleatória e amostra pequena.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Zhihao Wang, Zhili Li, Yiqun Xie, Carlos Eduardo A. Souza et al. (2024). AI-based Validation of Deforestation Using High-Resolution Satellite Imagery in the Brazilian Amazon. The international archives of the photogrammetry, remote sensing and spatial information sciences. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.5194/isprs-archives-XLVIII-3-2024-583-2024
- **Arquivo de origem:** `coleta/P04_Wang2024_AI-based-Validation-of-Deforestation-Using-High-Resolution-S.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P04_Wang2024_AI-based-Validation-of-Deforestation-Using-High-Resolution-S/document.md` — 6 páginas, 51 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

**Confirmar automaticamente alertas de desmatamento** da Amazônia brasileira com **um par de imagens Planet NICFI (antes e depois)** em cada local sugerido por produtos de baixa resolução (DETER, SAD, GLAD, SIRAD-X via MapBiomas Alerta), distinguindo **desmatamento novo** do já existente. O objetivo é substituir a validação manual do Imazon (p. 1–2).

**Resumo detectado automaticamente (p. 1):** Forests play an important role in the Earth systems for carbon sequestration and climate change mitigation, yet they have been increasingly disturbed by deforestation and forest degradation at an unprecedented pace. The Brazilian Amazon, for instance, experienced a 140% rise in deforestation from 2012 to 2020, with a record loss of 13,200 km² between August 2020 and July 2021. Alarmingly, 87% of 2019 deforestation alerts occurred on private properties, with 61% in legally restricted areas. Existing deforestation monitoring systems, such as PRODES and the Global Forest Change dataset, use about 30m resolution satellite imagery, which is insufficient for operational validation at fine scales. The Deforestation Alert System by Imazon leverages highresolution PlanetScope data (3-4m) but faces challenges due to fewer spectral bands and variations in reflectance values across different satelli…

- “Our contributions are summarized as follows: • We introduce a novel deep learning model to automate the validation of deforestation sites, leveraging the high spatial resolution of PlanetScope imagery to enhance detection ac curacy. • We co” (p. 2, seção Abstract)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “3 shows the study area ranging from 55° to 52.5°W and 2.5°S to 0°, near the Amazon River, where deforestation is more likely to occur and be transported across the river.” (p. 3, seção Abstract)
- “After data collection, we have a total of 1,912 images in the study area.” (p. 3, seção Abstract)
- “The Brazilian Amazon, for instance, experienced a 140% rise in deforestation from 2012 to 2020, with a record loss of 13,200 km² between August 2020 and July 2021.” (p. 1, seção Abstract)
- “Taking the Brazilian Amazon as an example, deforestation has been rapidly growing by 140% from 2012 to 2020, and between August 2020 and July 2021 alone, this region experienced a huge forest loss of 13,200 km², marking the highest deforest” (p. 1, seção Abstract)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- Locais de desmatamento do **MapBiomas Alerta** (2022) como verdade; para cada um, **um par de imagens NICFI** (R, G, B, NIR) por GEE, antes e depois (p. 3).
- **1.912 imagens** na área de 55°–52,5° O e 2,5° S–0° (perto do Rio Amazonas) (p. 3).
- Divisão **aleatória 80/10/10** (treino, validação, teste) (p. 3).

**Detectado automaticamente (verificar):**
- sensor/produto **PlanetScope**: 8 ocorrências (p. 1, 2, 3, 5)
- sensor/produto **Planet NICFI**: 4 ocorrências (p. 2, 3, 4, 6)
- sensor/produto **Planet (mosaicos e cenas)**: 4 ocorrências (p. 2, 3, 4, 6)
- conjunto de dados **Global Forest Change**: 6 ocorrências (p. 1, 2)
- conjunto de dados **MapBiomas**: 4 ocorrências (p. 1, 3)
- conjunto de dados **PRODES**: 2 ocorrências (p. 1)
- resolução mencionada: 30 m (p. 1)
- resolução mencionada: 4 m (p. 1)
- “After data collection, we have a total of 1,912 images in the study area.” (p. 3, seção Abstract)
- “PRODES, the widely-used product of deforestation monitoring from the National Institute of Space Research of Brazil, generates clear-cut deforestation maps based on visual interpretation of satellite imagery and manual mapping (de Almeida e” (p. 1, seção Abstract)
- “Specifically, Dice loss measures the overlap between the predicted regions and the ground truth out of the union of both regions.” (p. 2, seção Abstract)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Textura (GLCM)**: 7 ocorrências (p. 1, 2, 5, 6)
- **Rotulagem / anotação**: 3 ocorrências (p. 2, 3)
- **Índices espectrais**: 2 ocorrências (p. 5)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Método:**

- **U-Net bitemporal** (4 blocos de encoder e 4 de decoder; convoluções 3 × 3 com stride 2 para reduzir; camada de projeção final em mapa de probabilidade de desmatado e não desmatado); perda **Dice** (p. 2–3).
- Linhas de base: **Random Forest** de 50 árvores por pixel e **rede densa** de 5 camadas de 512 neurônios, ambas sobre pixel isolado (p. 3).
- Adam, lr 1e-4, 50 épocas; aumento por rotações e flips; melhor modelo escolhido pelo maior F1 de validação (p. 3–4).

- **Estratégia temporal (detecção automática, verificar):** bitemporal / pares (auto: 7 menções)
**Métodos detectados automaticamente:**
- método/família **U-Net**: 17 ocorrências (p. 2, 3, 4, 5)
- método/família **Random Forest**: 5 ocorrências (p. 2, 3, 4)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 0.0001” (p. 3)
- épocas/iterações: “50 epochs” (p. 5)
- otimizador: “Adam optimizer with a learning rate of 0” (p. 3)
- perda: “Dice loss, which is a widely used loss function f” (p. 2)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Desbalanceamento**: 4 ocorrências (p. 2, 3, 5)
- métrica **Precisão/Recall**: 24 ocorrências (p. 3, 5)
- métrica **F1**: 12 ocorrências (p. 3, 5)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Resultados (tabela 1, p. 5):**

| Modelo | F1 | Precisão | Recall | Acurácia |
|---|---|---|---|---|
| Random Forest | 0,5505 | 0,6712 | 0,4665 | 0,9456 |
| Rede densa | 0,5833 | 0,4729 | 0,7608 | 0,9223 |
| **U-Net** | **0,8251** | 0,7462 | 0,9226 | 0,9720 |
- A U-Net delimita melhor as bordas e preenche as clareiras com árvores esparsas; o RF tem ruído "sal e pimenta" (p. 5). Um limiar global de NDVI não separa bem desmatado de não desmatado (p. 5).

**Trechos numéricos detectados automaticamente (verificar):**
- “Moreover, a recent study indicates that 87% of the deforestation alerts in 2019 occurred on private properties, with 61% overlapping with legal restricted areas for forest removal, and only 0.1% were licensed forest suppression (MapBiomas, 2020).” (p. 1, seção Abstract)
- “It can be seen that the removal of trees usually leads to lower NDVI values |Model|F1 Precision Recall Accuracy| |---|---| |RF<br>FCN|0.5505<br>0.6712<br>0.4665<br>0.9456<br>0.5833<br>0.4729<br>0.7608<br>0.9223| |U-Net|0.8251<br>0.7462<br>0.9226<br>0.9720| Tab” (p. 5, seção Abstract)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites e observações:**

- O artigo não traz seção de limitações; a conclusão fala em **mais amostras e outras florestas** como trabalho futuro (p. 6).
- **Observações minhas:** (a) a divisão é **aleatória**, sem separar por local ou região, e os sítios vêm de uma só janela de ~280 km, então há risco de vazamento espacial e a generalização não foi testada; (b) a "verdade" vem de alertas de outros sistemas (MapBiomas), então o modelo reproduz o que esses sistemas já viram e **não mede desmatamento perdido por eles**; (c) a acurácia de 97 % é pouco informativa com classe rara; o F1 de 0,83 é a métrica que importa; (d) as linhas de base usam **pixel isolado**, sem contexto, enquanto a U-Net vê vizinhança; a comparação não separa a influência do contexto da do aprendizado profundo; (e) não há análise de nuvem, de diferença de data entre os pares nem de falsos positivos por rebrota ou queimada.


## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- Código e dados não informados; hiperparâmetros básicos descritos.

- **Código/dados:** não informado
- hiperparâmetros **não detectados** automaticamente: batch (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Alertas 4 (p. 1, 3); Revisão humana 3 (p. 1, 2); Sistema operacional 2 (p. 1); Falsos alertas 1 (p. 3)

**Interpretação — O que reaproveitar:**

- **Formulação "validar candidatos"**: um modelo bitemporal que confirma ou descarta locais apontados por um detector grosseiro (reduz custo de inspeção).
- **Entrada de dois mosaicos NICFI concatenados** (8 canais) numa U-Net pequena como baseline de mudança binária.
- **Perda Dice** e escolha do ponto de parada pelo F1 de validação.

**Interpretação — Cuidados para o nosso projeto:**

- O resultado depende de a localização candidata já existir; **não procura áreas novas** sozinho.
- Comparações com divisão aleatória devem ser refeitas por região antes de se confiar no F1.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[PlanetNICFI|Planet NICFI (basemaps)]] — 4 ocorrências (p. 2, 3, 4, 6)
- utiliza método: [[UNet|U-Net]] — 17 ocorrências (p. 2, 3, 4, 5)
- trata a tarefa: [[Desmatamento|Desmatamento]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[DETER|DETER (INPE)]] — suporte vindo da leitura/título/resumo
- adota desenho de validação: [[Desbalanceamento|Desbalanceamento de classes]] — 4 ocorrências (p. 2, 3, 5)
- referência (curado pela leitura): [[Alertas|Alertas de mudança]] — suporte vindo da leitura/título/resumo

**Comparações substantivas com outros artigos:**
- este artigo compartilha o produto NICFI e o alvo de [[Wagner_2023_MappingTropicalForest|Wagner 2023]] — P04 valida alertas de desmatamento com par NICFI e U-Net bitemporal (F1 0,83), enquanto P01 classifica por data.

## Figuras selecionadas

![[Wang_2024_ValidationDeforestationHigh_p4_Figure3.png|520]]
*Figure 3. Deforestation sites collected in the study area (left), and the overall location within the Amazon Forest region (right). (p. 4; recorte do PDF convertido)*


## Anotações do leitor

- 
