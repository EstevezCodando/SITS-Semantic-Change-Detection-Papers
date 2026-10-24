---
tipo: artigo
id_origem: P153
titulo: "Specialized Foundation Models Struggle to Beat Supervised Baselines"
ano: 2024
autores: ["Zongzhe Xu", "Ritvik Gupta", "Cheng, Wenduo", "Shen, Alexander", "Jun-Hong Shen", "Ameet Talwalkar", "Mikhail Khodak"]
doi: "10.48550/arXiv.2411.02796"
arquivo_fonte: "coleta/P153_Xu2024_Specialized-Foundation-Models-Struggle-to-Beat-Supervised-Ba.pdf"
markdown_fonte: "output/pdf/P153_Xu2024_Specialized-Foundation-Models-Struggle-to-Beat-Supervised-Ba/document.md"
paginas: 26
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: []
sensores: []
conjuntos_dados: []
metodos: ["[[TransferLearning|Aprendizado por transferência]]", "[[ModeloFundacional|Modelos fundacionais]]", "[[CNN|Redes convolucionais (CNN)]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Xu 2024 — Specialized Foundation Models Struggle to Beat Supervised Baselines

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Zongzhe Xu, Ritvik Gupta, Cheng, Wenduo, Shen, Alexander et al. (2024). Specialized Foundation Models Struggle to Beat Supervised Baselines. arXiv (Cornell University). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2411.02796
- **Arquivo de origem:** `coleta/P153_Xu2024_Specialized-Foundation-Models-Struggle-to-Beat-Supervised-Ba.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P153_Xu2024_Specialized-Foundation-Models-Struggle-to-Beat-Supervised-Ba/document.md` — 26 páginas, 42 recortes de figuras, 1 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “While for time series we go through a traditional process of developing and tuning a supervised model, this manual approach does not scale to many domains; as a result, in Section 3.1 we develop a way to simulate it using architecture searc” (p. 3, seção 1 I NTRODUCTION)
- “Specialized baselines: Both automated supervised pipelines that we develop are heavily influenced by successful in-domain model development.” (p. 4, seção 2 R ELATED WORK)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “In IGARSS 2019 - 2019 IEEE International Geoscience and Remote Sensing Symposium .” (p. 15, seção 6 C ONCLUSION)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- “Given an input time series of length L and prediction horizon H, the zero-shot Auto-AR methods works as follows: 1. segment the input into smaller fragments using a rolling window of size W such that W < L, resulting in L − W + 1 samples of” (p. 26, seção 6 C ONCLUSION)
- “While our findings are significant according to measures set by past work, they should not be misinterpreted to address all possible scenarios where FMs may be useful; for example, genomics FMs are often used for exploratory science and not” (p. 10, seção 5.6 L IMITATIONS)
- “Skysense: A multi-modal remote sensing foundation model towards universal interpretation for earth observation imagery.” (p. 13, seção 6 C ONCLUSION)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Normalização / escala**: 2 ocorrências (p. 5, 12)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 78 menções vs 0 de pares)
**Métodos detectados automaticamente:**
- método/família **Transfer learning**: 37 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Modelo fundacional**: 31 ocorrências (p. 1, 3, 6, 7, 8)
- método/família **CNN**: 25 ocorrências (p. 2, 3, 4, 5, 6)
- método/família **Transformer**: 23 ocorrências (p. 2, 3, 4, 6, 12)
- método/família **U-Net**: 14 ocorrências (p. 1, 2, 4, 5, 6)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate, weight decay, momentum, drop rate, and random se” (p. 19)
- batch: “batch size= 128 for all datasets, and cross entrop” (p. 19)
- épocas/iterações: “20 epochs” (p. 19)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 4 ocorrências (p. 19, 21, 22)
- métrica **F1**: 6 ocorrências (p. 6, 17)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “0.75 0.70 Figure 7: Scatterplot of improvement in RMSE (averaged across time horizons) of two closed-source FMs, LLM4TS and Toto, on a subset of datasets in Table 14.” (p. 24, seção 6 C ONCLUSION)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “Published as a conference paper at ICLR 2025 Figure 1: Across genomics, satellite imaging, and time series, specialized FMs fail to significantly improve upon supervised learning despite using two-to-five orders of magnitude more data.” (p. 2, seção 1 I NTRODUCTION)
- “Our main result is negative: despite pretraining on massive data, specialized FMs struggle and often fail to outperform models trained solely on downstream task data with traditional supervised learning (c.f.” (p. 2, seção 1 I NTRODUCTION)
- “As part of our study, we introduce two automated workflows— DASHA for simulating in-domain model development of CNNs and Auto-AR for tuning linear auto-regression on GPUs—that we believe will be useful tools for evaluating future work in th” (p. 10, seção 6 C ONCLUSION)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/ritvikgupta199/DASHA (p. 2)
- URL citada: https://github.com/ritvikgupta199/DASHA (p. 2)
- URL citada: https://github.com/Zongzhe-Xu/AutoAR (p. 2)
- URL citada: https://huggingface.co/made-with-clay/Clay (p. 12)
- URL citada: https://huggingface.co/spaces/InstaDeepAI/nucleotidetransformerbenchmark (p. 19)
- declaração: “Our work demonstrates that the benefits of large-scale pretraining have yet to be realized in many specialized areas, reinforces the need to compare new FMs to strong, well-tuned baselines, and introduces two new, easy-to-use, open-source, ” (p. 1)
- declaração: “Furthermore, tuned linear auto-regression (AR) matches or outperforms every open-source time series FM on a standard suite of forecasting tasks, despite using four or more orders of magnitude fewer parameters and data.” (p. 2)
- hiperparâmetros **não detectados** automaticamente: otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 14 (p. 8, 9, 10, 24, 25)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 37 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[ModeloFundacional|Modelos fundacionais]] — 31 ocorrências (p. 1, 3, 6, 7, 8)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 25 ocorrências (p. 2, 3, 4, 5, 6)

## Anotações do leitor

- 
