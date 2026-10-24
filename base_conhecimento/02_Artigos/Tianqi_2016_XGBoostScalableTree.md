---
tipo: artigo
id_origem: P53
titulo: "XGBoost: A Scalable Tree Boosting System"
ano: 2016
autores: ["Chen, Tianqi", "Carlos Guestrin"]
doi: "10.48550/arXiv.1603.02754"
arquivo_fonte: "coleta/P53_Tianqi2016_XGBoost-A-Scalable-Tree-Boosting-System.pdf"
markdown_fonte: "output/pdf/P53_Tianqi2016_XGBoost-A-Scalable-Tree-Boosting-System/document.md"
paginas: 13
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: []
sensores: []
conjuntos_dados: []
metodos: ["[[XGBoost|XGBoost]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Tianqi 2016 — XGBoost: A Scalable Tree Boosting System

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Chen, Tianqi, Carlos Guestrin (2016). XGBoost: A Scalable Tree Boosting System. arXiv (Cornell University). Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.48550/arXiv.1603.02754
- **Arquivo de origem:** `coleta/P53_Tianqi2016_XGBoost-A-Scalable-Tree-Boosting-System.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P53_Tianqi2016_XGBoost-A-Scalable-Tree-Boosting-System/document.md` — 13 páginas, 18 recortes de figuras, 2 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Tree boosting is a highly effective and widely used machine learning method. In this paper, we describe a scalable endto-end tree boosting system called XGBoost, which is used widely by data scientists to achieve state-of-the-art results on many machine learning challenges. We propose a novel sparsity-aware algorithm for sparse data and weighted quantile sketch for approximate tree learning. More importantly, we provide insights on cache access patterns, data compression and sharding to build a scalable tree boosting system. By combining these insights, XGBoost scales beyond billions of examples using far fewer resources than existing systems. Keywords Large-scale Machine Learning 1. INTRODUCTION Machine learning and data-driven approaches are becoming very important in many areas.…

- “We propose a novel sparsity-aware algorithm for sparse data and weighted quantile sketch for approximate tree learning.” (p. 1, seção ABSTRACT)
- “The major contributions of this paper is listed as follows: • We design and build a highly scalable end-to-end tree boosting system. • We propose a theoretically justified weighted quantile sketch for efficient proposal calculation. • We in” (p. 2, seção 1 Gradient tree boosting is also known as gradient boosting)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

Não informado (nada detectado automaticamente).

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

Não informado (nada detectado automaticamente).

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **XGBoost**: 56 ocorrências (p. 1, 3, 5, 7, 8)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate in tochastic optimization, shrinkage reduces the ” (p. 3)
- épocas/iterações: “10 iterations” (p. 9)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

Não informado (nada detectado automaticamente).

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “(2) includes functions as parameters and cannot be optimized using traditional optimization methods in Euclidean space.” (p. 2, seção 1 Gradient tree boosting is also known as gradient boosting)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/dmlc/xgboost (p. 1)
- URL citada: https://github.com/dmlc/xgboost (p. 1)
- declaração: “The system is available as an open source package .” (p. 1)
- declaração: “END TO END EVALUATIONS 6.1 System Implementation We implemented XGBoost as an open source package .” (p. 7)
- hiperparâmetros **não detectados** automaticamente: batch, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 14 (p. 5, 6, 7, 8, 9); Persistência / confirmação 3 (p. 7, 9)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza método: [[XGBoost|XGBoost]] — 56 ocorrências (p. 1, 3, 5, 7, 8)

## Anotações do leitor

- 
