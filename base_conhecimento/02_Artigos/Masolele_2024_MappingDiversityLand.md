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
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Desmatamento|Desmatamento]]", "[[ClassificacaoCobertura|Classificação de cobertura e uso da terra]]"]
sensores: ["[[PlanetNICFI|Planet NICFI (basemaps)]]", "[[PlanetProdutos|Produtos Planet (visão geral)]]"]
conjuntos_dados: []
metodos: ["[[UNet|U-Net]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]", "[[PatchesTiles|Recorte em patches/tiles]]", "[[MosaicosCompostos|Mosaicos e compostos temporais]]", "[[Normalizacao|Normalização e escala radiométrica]]", "[[MascaraNuvem|Máscara de nuvem e sombra]]"]
validacao: ["[[AmostraIndependente|Amostra independente]]", "[[Desbalanceamento|Desbalanceamento de classes]]", "[[F1|F1]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Masolele 2024 — Mapping the diversity of land uses following deforestation across Africa

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Robert N. Masolele, Diego Marcos, Veronique De Sy, Itohan‐Osa Abu et al. (2024). Mapping the diversity of land uses following deforestation across Africa. Scientific Reports. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1038/s41598-024-52138-9
- **Arquivo de origem:** `coleta/P102_Masolele2024_Mapping-the-diversity-of-land-uses-following-deforestation-a.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P102_Masolele2024_Mapping-the-diversity-of-land-uses-following-deforestation-a/document.md` — 16 páginas, 30 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “Here we present the first high-resolution (5 m) and continental-scale mapping of land use following deforestation in Africa, which covers an estimated 13.85% of the global forest area, including humid and dry forests.” (p. 1, seção Início)
- “Here we present the results with and without using AL to map land-use following deforestation at a continental scale.” (p. 2, seção Results)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “Trend of land‑use following deforestation in Africa Having predicted the land-use following deforestation across Africa for the year 2001 to 2020, we attempted to estimate the trend of the land-use for the entire study area and across four ” (p. 4, seção Results)
- “The study area was defined based on the coverage of high-resolution Planet-NICFI ­data” (p. 6, seção Study area)
- “Generating land‑use map prediction at scale We present the first wall-to-wall map of land-use following deforestation across Africa covering forest loss from the year 2001 to 2020 (Fig.” (p. 2, seção Results)
- “For detailed visualisation, the predicted output map of land use following deforestation is available at this website: [https://​rober​tnag82.​users.​earth​engine.​app/​view/​afric​alu.](https://robertnag82.users.earthengine.app/view/africa” (p. 2, seção Results)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

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

**Trechos numéricos detectados automaticamente (verificar):**
- “Specifically, the macro average F1-score improved from 43% with the original data to 54% after the first 1 AL round and to 84% after the second round (Fig. ).” (p. 2, seção Results)
- “The map has a users accuracy of 85%, producers accuracy of 84%, and F1-score of 85% (Fig.” (p. 2, seção Results)
- “1), the initial model achieved a macro averaged F1-score of 43%, compared to successive models obtaining 54% and 84% after one and two rounds of addition of training data using the AL approach, respectively.” (p. 11, seção Discussion)
- “In Africa, the lowest accuracy was found in sub-Saharan Africa, with false negatives of up to 48%, indicating an underestimation of forest loss in this region, specifically in dry ­forests .” (p. 13, seção Discussion)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “Particularly in cases where the training data is limited, heterogeneous or is prone to labeling errors (i.e. shape correctness, a mix of land uses), the model using the original data is not able to generalize across regions.” (p. 11, seção Discussion)
- “www.nature.com/scientificreports/ commodity crops and small-scale/large-scale agriculture, where other studies ­struggle .” (p. 13, seção Discussion)
- “One drawback of these approaches is that they are not wall-to-wall, and they may miss out on many deforestation drivers in unsampled locations, reducing their usefulness for deriving global statistics or getting a general ­overview [,] .” (p. 13, seção Discussion)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 8)
- declaração: “Other reference data was retrieved from open source data available via online ­searching [–] .” (p. 8)
- declaração: “www.nature.com/scientificreports/ Data availability The reference data are freely available at the citations reference in this Manuscript and upon request to the cor[responding author.” (p. 14)

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Revisão humana 5 (p. 2, 8, 11); Latência / frequência 2 (p. 8, 13); Persistência / confirmação 2 (p. 2); Falsos alertas 1 (p. 13)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[PlanetNICFI|Planet NICFI (basemaps)]] — 16 ocorrências (p. 3, 6, 8, 10, 13)
- utiliza dado/sensor: [[PlanetProdutos|Produtos Planet (visão geral)]] — 9 ocorrências (p. 6, 8, 13)
- utiliza método: [[UNet|U-Net]] — 7 ocorrências (p. 3, 8, 9, 10, 12)
- é avaliado por: [[F1|F1]] — 13 ocorrências (p. 1, 2, 4, 10, 11)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 33 ocorrências (p. 1, 6, 8, 9, 10)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 29 ocorrências (p. 1, 2, 4, 8, 11)
- aplica etapa de preparo: [[MosaicosCompostos|Mosaicos e compostos temporais]] — 9 ocorrências (p. 8, 13)
- aplica etapa de preparo: [[Normalizacao|Normalização e escala radiométrica]] — 4 ocorrências (p. 8, 9)
- aplica etapa de preparo: [[MascaraNuvem|Máscara de nuvem e sombra]] — 3 ocorrências (p. 8, 13)
- adota desenho de validação: [[AmostraIndependente|Amostra independente]] — 6 ocorrências (p. 2, 8, 9, 10)
- adota desenho de validação: [[Desbalanceamento|Desbalanceamento de classes]] — 6 ocorrências (p. 9, 10, 11)
- trata a tarefa: [[Desmatamento|Desmatamento]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[ClassificacaoCobertura|Classificação de cobertura e uso da terra]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
