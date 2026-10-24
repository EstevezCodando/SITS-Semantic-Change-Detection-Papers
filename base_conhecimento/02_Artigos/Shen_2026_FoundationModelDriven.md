---
tipo: artigo
id_origem: P34
titulo: "Foundation Model-Driven Semantic Change Detection in Remote Sensing Imagery"
ano: 2026
autores: ["Hengtong Shen", "Li Yan", "Hong Xie", "Yaxuan Wei", "Xinhao Li", "Wenfei Shen", "Peixian Lv", "Fei Tan"]
doi: "10.48550/arXiv.2602.13780"
arquivo_fonte: "coleta/P34_Shen2026_Foundation-Model-Driven-Semantic-Change-Detection-in-Remote-.pdf"
markdown_fonte: "output/pdf/P34_Shen2026_Foundation-Model-Driven-Semantic-Change-Detection-in-Remote-/document.md"
paginas: 19
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[MudancaSemantica|Mudança semântica (from–to)]]"]
sensores: []
conjuntos_dados: ["[[SECOND|SECOND]]", "[[HRSCD|HRSCD]]"]
metodos: ["[[ModeloFundacional|Modelos fundacionais]]", "[[Transformer|Transformers]]", "[[Mamba|Mamba / modelos de espaço de estados]]", "[[RedeSiamesa|Redes siamesas]]", "[[CNN|Redes convolucionais (CNN)]]", "[[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]", "[[CorrecaoAtmosferica|Correção atmosférica e reflectância]]", "[[PatchesTiles|Recorte em patches/tiles]]", "[[Normalizacao|Normalização e escala radiométrica]]", "[[AumentoDados|Aumento de dados]]"]
validacao: ["[[Generalizacao|Generalização e domain shift]]", "[[Desbalanceamento|Desbalanceamento de classes]]", "[[DivisaoTreinoTeste|Divisão treino/validação/teste]]", "[[IoU|IoU / mIoU]]", "[[AcuraciaGlobal|Acurácia global (OA)]]", "[[PrecisaoRecall|Precisão e recall]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Shen 2026 — Foundation Model-Driven Semantic Change Detection in Remote Sensing Imagery

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Hengtong Shen, Li Yan, Hong Xie, Yaxuan Wei et al. (2026). Foundation Model-Driven Semantic Change Detection in Remote Sensing Imagery. arXiv (Cornell University). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2602.13780
- **Arquivo de origem:** `coleta/P34_Shen2026_Foundation-Model-Driven-Semantic-Change-Detection-in-Remote-.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P34_Shen2026_Foundation-Model-Driven-Semantic-Change-Detection-in-Remote-/document.md` — 19 páginas, 16 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “Building upon this, we present PerASCD, a robust and unified SCD framework driven by the RS foundation model PerA.” (p. 1, seção Início)
- “Furthermore, we propose a Soft Semantic Consistency Loss (SSCLoss) to mitigate the numerical instability often encountered during the training of large-scale models.” (p. 1, seção Início)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The LandsatSCD is collected between the years 1990 and 2020 in Xinjiang, China.” (p. 8, seção IV. E XPERIMENTS)
- “Patel, “A TransformerBased Siamese Network for Change Detection,” in IGARSS 2022 - 2022 IEEE International Geoscience and Remote Sensing Symposium, Jul.” (p. 17, seção V. C ONCLUSION AND D ISCUSSION)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **SAR**: 2 ocorrências (p. 4, 16)
- conjunto de dados **SECOND**: 11 ocorrências (p. 8, 9, 10, 11, 13)
- conjunto de dados **HRSCD**: 5 ocorrências (p. 3, 9, 11)
- resolução mencionada: 3 m (p. 8)
- resolução mencionada: 30 m (p. 8)
- “After filtering, a total of 2,385 image pairs are retained.” (p. 8, seção IV. E XPERIMENTS)
- “Following previous work, we split the dataset into training, validation, and test sets with a ratio of 3:1:1, resulting in 1,431, 477, and 477 image pairs, respectively.” (p. 8, seção IV. E XPERIMENTS)
- “1 - JSTARS-2026-02222 < ## Foundation Model–Driven Semantic Change Detection in Remote Sensing Imagery Hengtong Shen, Li Yan, Hong Xie, Yaxuan Wei, Xinhao Li, Wenfei Shen, Peixian Lv and Fei Tan Abstract —Remote sensing (RS) change detectio” (p. 1, seção Início)
- “Extensive experiments on the SECOND and LandsatSCD benchmarks demonstrate that PerASCD achieves new state-of-the-art SeK scores (26.11% and 65.21%), surpassing the previous best method by 0.61% and 4.95%, respectively, while also exhibiting” (p. 1, seção Início)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 12 ocorrências (p. 1, 2, 5, 8, 9)
- **Correção atmosférica / reflectância**: 5 ocorrências (p. 1, 4, 9, 13, 16)
- **Recorte em patches/tiles**: 4 ocorrências (p. 4, 5, 8)
- **Normalização / escala**: 3 ocorrências (p. 7, 11, 16)
- **Aumento de dados**: 3 ocorrências (p. 8, 11)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal / pares (auto: 12 menções)
**Métodos detectados automaticamente:**
- método/família **Modelo fundacional**: 39 ocorrências (p. 1, 2, 3, 4, 6)
- método/família **Transformer**: 33 ocorrências (p. 3, 4, 5, 8, 9)
- método/família **Mamba**: 12 ocorrências (p. 3, 4, 9, 11, 12)
- método/família **Rede siamesa**: 7 ocorrências (p. 3, 17, 18)
- método/família **CNN**: 6 ocorrências (p. 3, 12)
- método/família **Semi/auto-supervisionado**: 6 ocorrências (p. 2, 3, 4, 5)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate, SSCLoss yields a 10.44% SeK improvement over the ” (p. 2)
- batch: “batch size is set to 8 and the weight decay is set” (p. 8)
- otimizador: “SGD) optimizer with momentum” (p. 8)
- tamanho do patch: “512 × 512 size and is annotated at the pixel” (p. 8)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Teste externo / generalização**: 9 ocorrências (p. 1, 2, 3, 9, 12)
- **Desbalanceamento**: 5 ocorrências (p. 2, 4, 6, 14)
- **Conjuntos treino/val/teste**: 3 ocorrências (p. 7, 8, 9)
- métrica **IoU**: 13 ocorrências (p. 8, 11, 12, 13, 14)
- métrica **Acurácia global**: 12 ocorrências (p. 8, 9, 11, 12, 13)
- métrica **Precisão/Recall**: 12 ocorrências (p. 7, 8, 11, 15, 16)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “On the challenging SECOND dataset, PerASCD improves the 𝐹 𝑠𝑐𝑑 by 2.88% and the SeK by 2.93% over the baseline SCanNet.” (p. 9, seção 4) Mamba-FCS which is recently published SCD metho)
- “Notably, the superiority in the SeK metric is even more pronounced, with improvements of 0.61% (SECOND) and 4.95% (LandsatSCD) over Mamba-FCS.” (p. 9, seção 4) Mamba-FCS which is recently published SCD metho)
- “Method 𝜏 OA 𝐹 𝑠𝑐𝑑 mIoU SeK PerASCD 0.005 88.30 66.33 74.30 26.17 PerASCD 0.01 88.70 66.41 74.33 26.11 PerASCD 0.02 88.65 66.45 74.45 26.23 PerASCD 0.1 88.34 66.36 74.32 26.21 PerASCD 0.5 88.53 66.33 74.33 26.10 PerASCD 1 88.36 66.32 74.28 26.12” (p. 16, seção 0.01 or 𝜏= 0.02. Since a relatively smaller initia)

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/SathShen/PerASCD.git (p. 1)
- URL citada: https://github.com/SathShen/PerASCD.git (p. 1)
- declaração: “The code is available at [https://github.com/SathShen/PerASCD.git.](https://github.com/SathShen/PerASCD.git) Index Terms —Foundation model, semantic change detection, modular decoder, remote sensing, deep learning.” (p. 1)
- hiperparâmetros **não detectados** automaticamente: épocas/iterações, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 5 (p. 2, 14, 15, 16); Falsos alertas 2 (p. 8, 14); Quase tempo real 1 (p. 18); Persistência / confirmação 1 (p. 7); Rastreabilidade 1 (p. 8)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- emprega conjunto de dados: [[SECOND|SECOND]] — 11 ocorrências (p. 8, 9, 10, 11, 13)
- emprega conjunto de dados: [[HRSCD|HRSCD]] — 5 ocorrências (p. 3, 9, 11)
- utiliza método: [[ModeloFundacional|Modelos fundacionais]] — 39 ocorrências (p. 1, 2, 3, 4, 6)
- utiliza método: [[Transformer|Transformers]] — 33 ocorrências (p. 3, 4, 5, 8, 9)
- utiliza método: [[Mamba|Mamba / modelos de espaço de estados]] — 12 ocorrências (p. 3, 4, 9, 11, 12)
- utiliza método: [[RedeSiamesa|Redes siamesas]] — 7 ocorrências (p. 3, 17, 18)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 6 ocorrências (p. 3, 12)
- utiliza método: [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 6 ocorrências (p. 2, 3, 4, 5)
- é avaliado por: [[IoU|IoU / mIoU]] — 13 ocorrências (p. 8, 11, 12, 13, 14)
- é avaliado por: [[AcuraciaGlobal|Acurácia global (OA)]] — 12 ocorrências (p. 8, 9, 11, 12, 13)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 12 ocorrências (p. 7, 8, 11, 15, 16)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 12 ocorrências (p. 1, 2, 5, 8, 9)
- aplica etapa de preparo: [[CorrecaoAtmosferica|Correção atmosférica e reflectância]] — 5 ocorrências (p. 1, 4, 9, 13, 16)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 4 ocorrências (p. 4, 5, 8)
- aplica etapa de preparo: [[Normalizacao|Normalização e escala radiométrica]] — 3 ocorrências (p. 7, 11, 16)
- aplica etapa de preparo: [[AumentoDados|Aumento de dados]] — 3 ocorrências (p. 8, 11)
- adota desenho de validação: [[Generalizacao|Generalização e domain shift]] — 9 ocorrências (p. 1, 2, 3, 9, 12)
- adota desenho de validação: [[Desbalanceamento|Desbalanceamento de classes]] — 5 ocorrências (p. 2, 4, 6, 14)
- adota desenho de validação: [[DivisaoTreinoTeste|Divisão treino/validação/teste]] — 3 ocorrências (p. 7, 8, 9)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[MudancaSemantica|Mudança semântica (from–to)]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
