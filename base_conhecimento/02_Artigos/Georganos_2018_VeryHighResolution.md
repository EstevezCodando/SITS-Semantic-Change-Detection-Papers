---
tipo: artigo
id_origem: P52
titulo: "Very High Resolution Object-Based Land Use-Land Cover Urban Classification Using Extreme Gradient Boosting"
ano: 2018
autores: ["Stefanos Georganos", "Taïs Grippa", "Sabine G. Vanhuysse", "Moritz Lennert", "Michal Shimoni", "Eléonore Wolff A"]
doi: "10.1109/LGRS.2018.2803259"
arquivo_fonte: "coleta/P52_Georganos2018_Very-High-Resolution-Object-Based-Land-Use-Land-Cover-Urban-.pdf"
markdown_fonte: "output/pdf/P52_Georganos2018_Very-High-Resolution-Object-Based-Land-Use-Land-Cover-Urban-/document.md"
paginas: 5
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[Edificacoes|Edificações e urbanização]]", "[[ClassificacaoCobertura|Classificação de cobertura e uso da terra]]"]
sensores: []
conjuntos_dados: []
metodos: ["[[OBIA|Análise baseada em objetos (OBIA)]]", "[[XGBoost|XGBoost]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Georganos 2018 — Very High Resolution Object-Based Land Use-Land Cover Urban Classification Using Extreme Gradient Boosting

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Stefanos Georganos, Taïs Grippa, Sabine G. Vanhuysse, Moritz Lennert et al. (2018). Very High Resolution Object-Based Land Use-Land Cover Urban Classification Using Extreme Gradient Boosting. IEEE Geoscience and Remote Sensing Letters. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1109/LGRS.2018.2803259
- **Arquivo de origem:** `coleta/P52_Georganos2018_Very-High-Resolution-Object-Based-Land-Use-Land-Cover-Urban-.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P52_Georganos2018_Very-High-Resolution-Object-Based-Land-Use-Land-Cover-Urban-/document.md` — 5 páginas, 8 recortes de figuras, 5 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “In this letter, we introduce Xgboost and evaluate its efficiency considering its sensitivity to sample size and feature selection (FS) using VHR datasets over the cities of Dakar and Ouagadougou along with the village of Vaihingen.” (p. 1, seção Início)
- “In detail, we investigated the sensitivity of Xgboost GEOBIA , .” (p. 1, seção Início)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **WorldView**: 4 ocorrências (p. 2, 5)
- sensor/produto **Imagens aéreas**: 2 ocorrências (p. 5)
- resolução mencionada: 9 cm (p. 2)
- “Critically, from 200 samples dimensionality where the accuracy of prediction can be per class, Xgboost appears to increase in accuracy when the affected by the number of predictors .” (p. 4, seção 10 randomly sampled training distributions for each class si)
- “The results of the random and stratified random sampling with strata defined Xgboost classification, both in terms of accuracy and using OpenStreetMap while the objects are validated and computational cost, are compared with traditional ben” (p. 2, seção Início)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Mosaicos e compostos**: 2 ocorrências (p. 2, 4)
- **Índices espectrais**: 2 ocorrências (p. 3)
- **Textura (GLCM)**: 2 ocorrências (p. 3)
- **Recorte em patches/tiles**: 2 ocorrências (p. 2)
- **Rotulagem / anotação**: 2 ocorrências (p. 2)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **SVM**: 30 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **OBIA**: 16 ocorrências (p. 1, 3, 4, 5)
- método/família **XGBoost**: 8 ocorrências (p. 1, 5)
- método/família **Random Forest**: 7 ocorrências (p. 1, 5)
- método/família **CNN**: 5 ocorrências (p. 1, 5)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Validação cruzada**: 2 ocorrências (p. 3)
- métrica **Acurácia global**: 7 ocorrências (p. 3, 4)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “The highest recorded accuracy (OA=82.10%) is efficiency albeit having the drawback of not capturing feature obtained when Xgboost trained with the full set of features. interaction, a phenomenon documented in CART based Nonetheless, Xgboost appears to be sligh” (p. 3, seção II. RESULTS)
- “2. a) Pleiades RGB composite of a central urban region in Dakar and b) Time (s) 0.29 0.21 1.75 0.82 4.15 1.93 LULC map of the same region using Xgboost with the largest sample size (N60).” (p. 4, seção II. RESULTS)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “The highest recorded accuracy (OA=82.10%) is efficiency albeit having the drawback of not capturing feature obtained when Xgboost trained with the full set of features. interaction, a phenomenon documented in CART based Nonetheless, Xgboost” (p. 3, seção II. RESULTS)
- “Guestrin, “XGBoost : Reliable Large-scale Tree complexity, and training data limitations.” (p. 5, seção IV. CONCLUSIONS Vision, 2010, pp. 210–223.)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/ANAGEO/XgboostFeatureSelectionOpt (p. 4)
- URL citada: https://github.com/ANAGEO/XgboostFeatureSelectionOpt (p. 4)
- URL citada: https://github.com/ANAGEO/XgboostFeatureSelectionOptimization (p. 4)
- declaração: “2 TABLE I C LASSIFICATION S CHEME AND V ALIDATION D ATA FOR D AKAR, O UAGADOUGOU AND V AIHINGEN |Dakar(Senegal)|Col2|Ouagadougou(BurkinaFaso)|Col4|Vaihingen(Germany)|Col6| |---|---|---|---|---|---| |Class name|Validation set|Class name|Vali” (p. 2)
- declaração: “Infrared false color composite image subsets of a) Vaihingen, b) a dense built-up area in Dakar, c) a sparsely built-up area in For segmentation, we use an open source, semi-automatic Ouagadougou. processing chain, recently developed in a P” (p. 2)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 8 (p. 1, 2, 3, 4, 5); Sistema operacional 2 (p. 2); Revisão humana 1 (p. 2)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza método: [[OBIA|Análise baseada em objetos (OBIA)]] — 16 ocorrências (p. 1, 3, 4, 5)
- utiliza método: [[XGBoost|XGBoost]] — 8 ocorrências (p. 1, 5)
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[ClassificacaoCobertura|Classificação de cobertura e uso da terra]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
