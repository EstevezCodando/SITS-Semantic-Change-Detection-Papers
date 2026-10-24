---
tipo: artigo
id_origem: P154
titulo: "Uncertainty and Generalizability in Foundation Models for Earth Observation"
ano: 2024
autores: ["Raúl Ramos-Pollán", "Freddie Kalaitzis", "Karthick Panner Selvam"]
doi: "10.48550/arXiv.2409.08744"
arquivo_fonte: "coleta/P154_Ramos-Pollan2024_Uncertainty-and-Generalizability-in-Foundation-Models-for-Ea.pdf"
markdown_fonte: "output/pdf/P154_Ramos-Pollan2024_Uncertainty-and-Generalizability-in-Foundation-Models-for-Ea/document.md"
paginas: 9
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: []
sensores: ["[[Sentinel2|Sentinel-2]]", "[[Sentinel1|Sentinel-1]]"]
conjuntos_dados: []
metodos: ["[[Transformer|Transformers]]"]
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]", "[[Rotulagem|Rotulagem e anotação]]"]
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica]
---

# RamosPollan 2024 — Uncertainty and Generalizability in Foundation Models for Earth Observation

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Raúl Ramos-Pollán, Freddie Kalaitzis, Karthick Panner Selvam (2024). Uncertainty and Generalizability in Foundation Models for Earth Observation. arXiv (Cornell University). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2409.08744
- **Arquivo de origem:** `coleta/P154_Ramos-Pollan2024_Uncertainty-and-Generalizability-in-Foundation-Models-for-Ea.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P154_Ramos-Pollan2024_Uncertainty-and-Generalizability-in-Foundation-Models-for-Ea/document.md` — 9 páginas, 7 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** We take the perspective in which we want to design a downstream task (such as estimating vegetation coverage) on a certain area of interest (AOI) with a limited labeling budget. By leveraging an existing Foundation Model (FM) we must decide whether we train a downstream model on a different but label-rich AOI hoping it generalizes to our AOI, or we split labels in our AOI for training and validating. In either case, we face choices concerning what FM to use, how to sample our AOI for labeling, etc. which affect both the performance and uncertainty of the results. In this work, we perform a large ablative study using eight existing FMs on either Sentinel 1 or Sentinel 2 as input data, and the classes from the ESA World Cover product as downstream tasks across eleven AOIs. We do repeated sampling and training, resulting in an ablation of some 500K simple linear regression models. Our resul…

- “In this work we address the last two.” (p. 2, seção Abstract)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-2**: 6 ocorrências (p. 1, 2, 4, 6)
- sensor/produto **Sentinel-1**: 5 ocorrências (p. 1, 2, 4, 6)
- sensor/produto **SAR**: 2 ocorrências (p. 6, 8)
- resolução mencionada: 10 m (p. 3)
- “For interpretation of the results we establish a threshold of 0.7 above which we consider FM embeddings are actually picking up meaningful information on the underlying predictive task.” (p. 4, seção Abstract)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 23 ocorrências (p. 1, 2, 3, 4, 6)
- **Rotulagem / anotação**: 18 ocorrências (p. 1, 2, 3, 6, 7)
- **Reamostragem**: 2 ocorrências (p. 5, 6)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **Transformer**: 10 ocorrências (p. 2, 4)
**Hiperparâmetros detectados automaticamente (verificar):**
- tamanho do patch: “512 × 512 pixel” (p. 3)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Amostragem estratificada**: 4 ocorrências (p. 4)
- métrica **Estimativa de área**: 4 ocorrências (p. 4)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: http://github.com/rramosp/geetiles (p. 3)
- URL citada: http://github.com/rramosp/geetiles (p. 3)
- URL citada: https://github.com/Clay-foundation/model (p. 4)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 6 ocorrências (p. 1, 2, 4, 6)
- utiliza dado/sensor: [[Sentinel1|Sentinel-1]] — 5 ocorrências (p. 1, 2, 4, 6)
- utiliza método: [[Transformer|Transformers]] — 10 ocorrências (p. 2, 4)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 23 ocorrências (p. 1, 2, 3, 4, 6)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 18 ocorrências (p. 1, 2, 3, 6, 7)

## Anotações do leitor

- 
