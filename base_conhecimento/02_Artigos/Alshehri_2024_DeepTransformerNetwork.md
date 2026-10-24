---
tipo: artigo
id_origem: P110
titulo: "Deep Transformer-Based Network Deforestation Detection in the Brazilian Amazon Using Sentinel-2 Imagery"
ano: 2024
autores: ["Mariam Alshehri", "Anes Ouadou", "Grant J. Scott"]
doi: "10.1109/lgrs.2024.3355104"
arquivo_fonte: "coleta/P110_Alshehri2024_Deep-Transformer-Based-Network-Deforestation-Detection-in-th.pdf"
markdown_fonte: "output/pdf/P110_Alshehri2024_Deep-Transformer-Based-Network-Deforestation-Detection-in-th/document.md"
paginas: 5
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[Desmatamento|Desmatamento]]"]
sensores: ["[[Sentinel2|Sentinel-2]]", "[[Landsat|Landsat]]"]
conjuntos_dados: ["[[PRODES|PRODES (INPE)]]"]
metodos: ["[[Transformer|Transformers]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Alshehri 2024 — Deep Transformer-Based Network Deforestation Detection in the Brazilian Amazon Using Sentinel-2 Imagery

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Mariam Alshehri, Anes Ouadou, Grant J. Scott (2024). Deep Transformer-Based Network Deforestation Detection in the Brazilian Amazon Using Sentinel-2 Imagery. IEEE Geoscience and Remote Sensing Letters. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1109/lgrs.2024.3355104
- **Arquivo de origem:** `coleta/P110_Alshehri2024_Deep-Transformer-Based-Network-Deforestation-Detection-in-th.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P110_Alshehri2024_Deep-Transformer-Based-Network-Deforestation-Detection-in-th/document.md` — 5 páginas, 10 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “This study aims to investigate the application of the transformer-based network, ChangeFormer , originally designed for change detection in urban areas, in the context of deforestation, with the objective of demonstrating its effectiveness ” (p. 2, seção I. I NTRODUCTION)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “To assess the model’s effectiveness, we employed a robust approach to create a deforestation detection dataset, utilizing Sentinel-2 imagery from select conservation areas in the Brazilian Amazon throughout 2020 and 2021.” (p. 1, seção Início)
- “We targeted the years 2020 and 2021, as they provide the most recent and complete yearly deforestation data.” (p. 2, seção II. M ETHODS)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-2**: 12 ocorrências (p. 1, 2, 5)
- sensor/produto **Landsat**: 5 ocorrências (p. 1, 5)
- conjunto de dados **PRODES**: 5 ocorrências (p. 2, 5)
- resolução mencionada: 250 m (p. 1)
- resolução mencionada: 10 m (p. 1)
- resolução mencionada: 60 m (p. 1)
- “Band Combinations Sentinel-2 images are composed of 13 bands at varying resolutions of 10 m, 20 m, and 60 m.” (p. 2, seção II. M ETHODS)
- “Almeida, “Deforestation Detection with Fully Convolutional Networks in the Amazon Forest from Landsat-8 and Sentinel-2 Images,” Remote Sensing, vol.” (p. 5, seção V. C ONCLUSION AND F UTURE W ORK)
- “This makes conventional methods, such as map interpretation, field surveys, and ancillary data analysis, impractical due to their time-consuming and labor-intensive nature.” (p. 1, seção I. I NTRODUCTION)
- “2) Ground truth source: To generate ground truth polygons for our study, we utilized the PRODES project datasets developed by the Brazilian National Space Agency (INPE). - Copernicus portal: https://scihub.copernicus.eu/dhus/ 2 Since 1988, ” (p. 2, seção II. M ETHODS)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 26 ocorrências (p. 1, 2, 3, 4, 5)
- **Rotulagem / anotação**: 9 ocorrências (p. 2, 4, 5)
- **Índices espectrais**: 3 ocorrências (p. 3, 4)
- **Máscara de nuvem e sombra**: 2 ocorrências (p. 2)
- **Mosaicos e compostos**: 2 ocorrências (p. 4, 5)
- **Normalização / escala**: 2 ocorrências (p. 3)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal / pares (auto: 7 menções)
**Métodos detectados automaticamente:**
- método/família **Transformer**: 25 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **CNN**: 6 ocorrências (p. 2, 5)
- método/família **Rede siamesa**: 3 ocorrências (p. 2, 4, 5)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rates|0.01 - 0.0001| |Loss functions|Cross-Entropy (CE),” (p. 4)
- épocas/iterações: “200 epochs” (p. 4)
- otimizador: “SGD, Adam, AdamW| |learning rates|0” (p. 4)
- perda: “cross-entropy loss with AdamW optimizer resulted in t” (p. 5)
- tamanho do patch: “256 × 256 pixel” (p. 1)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Desbalanceamento**: 3 ocorrências (p. 1, 3, 4)
- **Teste externo / generalização**: 2 ocorrências (p. 3, 4)
- métrica **IoU**: 13 ocorrências (p. 1, 4, 5)
- métrica **F1**: 8 ocorrências (p. 1, 4, 5)
- métrica **Precisão/Recall**: 8 ocorrências (p. 4, 5)
- métrica **Acurácia global**: 6 ocorrências (p. 1, 4, 5)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado
- hiperparâmetros **não detectados** automaticamente: batch (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Latência / frequência 3 (p. 1); Custo 2 (p. 1, 2); Quase tempo real 1 (p. 5); Rastreabilidade 1 (p. 1)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 12 ocorrências (p. 1, 2, 5)
- utiliza dado/sensor: [[Landsat|Landsat]] — 5 ocorrências (p. 1, 5)
- emprega conjunto de dados: [[PRODES|PRODES (INPE)]] — 5 ocorrências (p. 2, 5)
- utiliza método: [[Transformer|Transformers]] — 25 ocorrências (p. 1, 2, 3, 4, 5)
- trata a tarefa: [[Desmatamento|Desmatamento]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
