---
tipo: artigo
id_origem: P18
titulo: "Multitask Learning for Large-scale Semantic Change Detection"
ano: 2019
autores: ["Rodrigo Caye Daudt", "Bertrand Le Saux", "Alexandre Boulch", "Yann Gousseau"]
doi: "10.48550/arXiv.1810.08452"
arquivo_fonte: "coleta/P18_Daudt2018_Multitask-Learning-for-Large-scale-Semantic-Change-Detection.pdf"
markdown_fonte: "output/pdf/P18_Daudt2018_Multitask-Learning-for-Large-scale-Semantic-Change-Detection/document.md"
paginas: 16
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "B"
tarefas: ["[[MudancaSemantica|Mudança semântica (from–to)]]"]
sensores: ["[[ImagensAereas|Imagens aéreas]]"]
conjuntos_dados: ["[[HRSCD|HRSCD]]"]
metodos: ["[[CNN|Redes convolucionais (CNN)]]"]
preparo: []
validacao: ["[[Desbalanceamento|Desbalanceamento de classes]]", "[[Kappa|Coeficiente kappa]]"]
ferramentas: []
tags: [artigo, leitura/profunda, relevancia/B]
---

# Daudt 2019 — Multitask Learning for Large-scale Semantic Change Detection

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **B** — HRSCD: estratégias de mudança semântica (aéreo bitemporal).

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Rodrigo Caye Daudt, Bertrand Le Saux, Alexandre Boulch, Yann Gousseau (2019). Multitask Learning for Large-scale Semantic Change Detection. arXiv (Cornell University). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.1810.08452
- **Arquivo de origem:** `coleta/P18_Daudt2018_Multitask-Learning-for-Large-scale-Semantic-Change-Detection.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P18_Daudt2018_Multitask-Learning-for-Large-scale-Semantic-Change-Detection/document.md` — 16 páginas, 46 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Como obter, numa mesma rede, **onde** houve mudança e **de qual classe para qual classe**, e um dataset de larga escala (HRSCD) para treinar isso de forma supervisionada. Compara quatro estratégias de mudança semântica.

**Resumo detectado automaticamente (p. 1):** Change detection is one of the main problems in remote sensing, and is essential to the accurate processing and understanding of the large scale Earth observation data available. Most of the recently proposed change detection methods bring deep learning to this context, but change detection labelled datasets which are openly available are still very scarce, which limits the methods that can be proposed and tested. In this paper we present the first large scale very high resolution semantic change detection dataset, which enables the usage of deep supervised learning methods for semantic change detection with very high resolution images. The dataset contains coregistered RGB image pairs, pixel-wise change information and land cover information. We then propose several supervised learning methods using fully convolutional neural networks to perform semantic change detection. Most notably, …

- “In this paper we present the first large scale very high resolution semantic change detection dataset, which enables the usage of deep supervised learning methods for semantic change detection with very high resolution images.” (p. 1, seção Abstract)
- “Most notably, we present a network architecture that performs change detection and land cover mapping simultaneously, while using the predicted land cover information to help to predict changes.” (p. 1, seção Abstract)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “That is the case for the images taken in 2005 and 2006.” (p. 5, seção 3. Dataset)
- “These maps were generated for the years of 2006 and 2012, and a third map is available containing the changes that took place in that period.” (p. 5, seção 3. Dataset)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Imagens aéreas**: 5 ocorrências (p. 4, 13)
- sensor/produto **Sentinel-2**: 2 ocorrências (p. 4, 10)
- conjunto de dados **HRSCD**: 16 ocorrências (p. 3, 4, 5, 7, 10)
- conjunto de dados **OSCD**: 6 ocorrências (p. 4, 5, 7, 10, 11)
- resolução mencionada: 50 cm (p. 4)
- “The FC-EF-Res architecture was compared to the previously proposed FCNN architectures on the OSCD dataset for binary change detection, which contains lowerresolution Sentinel-2 image pairs with 13 multispectral To test the methods proposed ” (p. 10, seção 5. Results)
- “Inference times of the proposed methods were under 0.04 s for 512x512 image pairs using the 10” (p. 10, seção 5. Results)
- “These rasters allow us to have ground truth information about each pixel in the dataset.” (p. 5, seção 1. This hierarchical level will henceforth be referred to as)
- “We leave it up to the users how to best interpret and deal with these differences.” (p. 5, seção 1. This hierarchical level will henceforth be referred to as)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Evidência (leitura) — Dados e rótulos (HRSCD):**

- 291 pares RGB de 10.000 × 10.000 px, mosaicos aéreos do IGN (BD ORTHO, 0,5 m): imagens de 2005/2006 e 2012, regiões de Rennes e Caen (p. 4).
- Rótulos vindos do **Urban Atlas** (Copernicus/EEA) de 2006 e 2012 e do mapa de mudança: rasterizados e alinhados às imagens; nível hierárquico L1 com 5 classes (artificial, agrícola, florestas, áreas úmidas, água) mais "sem informação" (p. 5).
- Rótulos não são perfeitos: precisão mínima garantida de 80–85 % por classe; um único rótulo por parcela gera **bordas imprecisas e mudanças superestimadas** (p. 5, 6).
- **Desbalanceamento extremo:** 99,232 % dos pixels sem mudança; a maior classe de mudança (agrícola → artificial) é 0,653 %; todas as outras somam 0,115 % (p. 6).
- Níveis hierárquicos mais finos que L1 foram evitados: o número de transições cresce com o quadrado das classes (p. 6).

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 14 ocorrências (p. 2, 3, 5, 6, 7)
- **Corregistro / georreferenciamento**: 2 ocorrências (p. 2, 5)
- **Recorte em patches/tiles**: 2 ocorrências (p. 4, 13)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Quatro estratégias:**

1. **Comparar mapas de cobertura** previstos em cada data (mais simples; erros dos dois mapas se somam).
2. **Mudança semântica direta**: cada par from–to vira uma classe (cresce com N²).
3. **CD e LCM separados:** uma rede de mudança binária mascara os dois mapas de cobertura.
4. **Rede integrada multitarefa:** dois ramos de cobertura com pesos compartilhados e um ramo de mudança com *difference skip connections* (p. 7, 8, 9).
   - 4.1: perda ponderada `L_CD + λ·L_LCM` (λ = 0,05), exige busca em grade.
   - **4.2: treino sequencial** — primeiro só a cobertura; depois o ramo de mudança com os pesos da cobertura congelados (p. 9, 10).

- **Estratégia temporal (detecção automática, verificar):** bitemporal e série (auto: 28 pares; 8 série)
**Métodos detectados automaticamente:**
- método/família **CNN**: 20 ocorrências (p. 1, 3, 4, 7, 10)
- método/família **LSTM / recorrente**: 5 ocorrências (p. 4, 12, 13)
- método/família **Transfer learning**: 4 ocorrências (p. 3, 12)
- método/família **Rede siamesa**: 3 ocorrências (p. 4, 9)
**Hiperparâmetros detectados automaticamente (verificar):**
- tamanho do patch: “631x602 pixel” (p. 13)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Evidência (leitura) — Treino e métricas:**

- Rede FC-EF-Res (blocos residuais em encoder–decoder, extensão do FC-EF); no OSCD melhora o Dice RGB de 48,89 (FC-EF) para 59,20 e o multiespectral de 56,91 para 60,15 (p. 7, 11).
- HRSCD: 146 pares para treino e 145 para teste (nenhum pixel de teste visto no treino); pesos de classe inversos à frequência; 3–5 h por modelo numa GTX 1080 Ti; inferência < 0,04 s por par 512² (p. 10).
- **A acurácia global é inadequada** (só reflete a classe "sem mudança"); usar kappa e Dice (p. 6).

**Detectado automaticamente (verificar):**
- **Desbalanceamento**: 10 ocorrências (p. 6, 8, 10, 11)
- **Conjuntos treino/val/teste**: 3 ocorrências (p. 10, 13)
- métrica **Kappa**: 10 ocorrências (p. 6, 9, 11, 12, 13)
- métrica **Precisão/Recall**: 3 ocorrências (p. 9, 11)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Resultados (HRSCD, kappa de mudança):**

| Estratégia | Kappa CD | Dice CD | Kappa cobertura |
|---|---|---|---|
| 1 comparar mapas | 3,99 | 5,56 | 71,92 |
| 2 direta | 21,54 | — | — |
| 3 separadas | 12,48 | 13,79 | 71,92 |
| 4.1 integrada (λ) | 19,13 | 20,23 | 67,25 |
| **4.2 sequencial** | **25,49** | **26,33** | 71,81 |

- A estratégia 2 acerta *onde* mas prevê sempre o mesmo tipo de mudança (sem semântica) (p. 11).
- Métodos clássicos (PCA + k-means, diferença de features VGG) ficam abaixo de kappa 3,3 (p. 13).
- Reduzir os dados de treino para ½ e ¼ baixa o kappa de 25,49 para 23,34 e 22,18 (p. 12).
- Crítica ao teste com pixels aleatórios (lago Eppalock): vizinhos redundantes causam overfitting (p. 13).

**Trechos numéricos detectados automaticamente (verificar):**
- “Furthermore, EEA only guarantees a minimum label accuracy of 80-85% depending on the consid 5” (p. 5, seção 1. This hierarchical level will henceforth be refe)
- “It is likely that overfitting takes place, since an accuracy of over 98% is achieved by using only 1000 labelled pixels to train a network with 67500 parameters (for their long short-term memory (LSTM) architecture, which performed the best).” (p. 13, seção 5. Results)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites e cuidados:**

- Aéreo RGB de 0,5 m e rótulos de mapas vetoriais, longe de Planet 3–5 m; **não transferir os números**.
- Ruído de rótulo, paralaxe e datas de aquisição incertas.

**Trechos detectados automaticamente (verificar contexto):**
- “The methods used to create this dataset, as well as the limitations of the available data, will be described later on.” (p. 2, seção 1. Introduction)
- “It may nevertheless affect future works done with the data.” (p. 5, seção 1. This hierarchical level will henceforth be referred to as)
- “Dataset analysis Despite its unprecedented size and qualities, we acknowledge in this section the dataset’s limitations and challenges.” (p. 5, seção 1. This hierarchical level will henceforth be referred to as)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 

**Interpretação — O que reaproveitar:**

- **Estratégia 4.2** como desenho de referência para o EXP4 (modelo semântico conjunto), sem busca de λ.
- **Pesos de classe inversos à frequência** e **kappa/Dice** (nunca OA) para mudança rara.
- **Rotular `mudança` como parcela inteira gera superestimação de borda**: avaliar sempre com tolerância espacial.
- **Hierarquia de classes** (comece em 5–6 classes) e controle do crescimento quadrático de transições.
- **Partição por pares/áreas**, nunca por pixels.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- emprega conjunto de dados: [[HRSCD|HRSCD]] — 16 ocorrências (p. 3, 4, 5, 7, 10)
- trata a tarefa: [[MudancaSemantica|Mudança semântica (from–to)]] — suporte vindo da leitura/título/resumo
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 20 ocorrências (p. 1, 3, 4, 7, 10)
- utiliza dado/sensor: [[ImagensAereas|Imagens aéreas]] — 5 ocorrências (p. 4, 13)
- adota desenho de validação: [[Desbalanceamento|Desbalanceamento de classes]] — 10 ocorrências (p. 6, 8, 10, 11)
- é avaliado por: [[Kappa|Coeficiente kappa]] — 10 ocorrências (p. 6, 9, 11, 12, 13)
- referencia (suporte manual da leitura): [[DivisaoEspacialBlocos|Divisão espacial por blocos e áreas]] — suporte vindo da leitura/título/resumo

**Comparações substantivas com outros artigos:**
- [[Yang_2021_AsymmetricSiameseNetworks|Yang 2021]] compara-se com e critica este artigo — P19 supera HRSCD.str4 (P18): (p. 10); e critica a simetria: (p. 4).
- este artigo têm datasets complementares [[Yang_2021_AsymmetricSiameseNetworks|Yang 2021]] — HRSCD (aéreo, Urban Atlas) e SECOND (aéreo, anotação por especialistas) são benchmarks bitemporais de mudança semântica.

## Figuras selecionadas

![[Daudt_2019_MultitaskLearningLarge_p10_Figure5.png|520]]
*Figure 5: Detailed schematics for the integrated change detection and land cover mapping network (Strategy 4). The encoder-decoder architect (p. 10; recorte do PDF convertido)*

![[Daudt_2019_MultitaskLearningLarge_p10_Fig.6.png|520]]
*Fig. 6. (p. 10; recorte do PDF convertido)*


## Anotações do leitor

- 
