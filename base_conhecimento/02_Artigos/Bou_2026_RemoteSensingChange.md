---
tipo: artigo
id_origem: P33
titulo: "Remote Sensing Change Detection via Weak Temporal Supervision"
ano: 2026
autores: ["Xavier Bou", "Elliot Vincent", "Gabriele Facciolo", "Rafael Grompone von Gioi", "Jean‐Michel Morel", "Thibaud Ehret"]
doi: "10.48550/arXiv.2601.02126"
arquivo_fonte: "coleta/P33_Bou2026_Remote-Sensing-Change-Detection-via-Weak-Temporal-Supervisio.pdf"
markdown_fonte: "output/pdf/P33_Bou2026_Remote-Sensing-Change-Detection-via-Weak-Temporal-Supervisio/document.md"
paginas: 23
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[MudancaSemantica|Mudança semântica (from–to)]]", "[[ClassificacaoCobertura|Classificação de cobertura e uso da terra]]"]
sensores: ["[[ImagensAereas|Imagens aéreas]]"]
conjuntos_dados: ["[[S2Looking|S2Looking]]", "[[LEVIRCD|LEVIR-CD]]", "[[WHUCD|WHU-CD]]"]
metodos: ["[[UNet|U-Net]]", "[[SupervisaoFraca|Supervisão fraca]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Bou 2026 — Remote Sensing Change Detection via Weak Temporal Supervision

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Xavier Bou, Elliot Vincent, Gabriele Facciolo, Rafael Grompone von Gioi et al. (2026). Remote Sensing Change Detection via Weak Temporal Supervision. arXiv (Cornell University). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2601.02126
- **Arquivo de origem:** `coleta/P33_Bou2026_Remote-Sensing-Change-Detection-via-Weak-Temporal-Supervisio.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P33_Bou2026_Remote-Sensing-Change-Detection-via-Weak-Temporal-Supervisio/document.md` — 23 páginas, 326 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Semantic change detection in remote sensing aims to iden- tify land cover changes between bi-temporal image pairs. Progress in this area has been limited by the scarcity of annotated datasets, as pixel-level annotation is costly and time-consuming. To address this, recent methods leverage synthetic data or generate artificial change pairs, but out-of- domain generalization remains limited. In this work, we in- troduce a weak temporal supervision strategy that leverages additional temporal observations of existing single-temporal - These authors contributed equally datasets, without requiring any new annotations. Specifi- cally, we extend single-date remote sensing datasets with new observations acquired at different times and train a change detection model by assuming that real bi-temporal pairs mostly contain no change, while pairing images from different locations to generate change ex…

- “To avoid this problem, we propose a novel weak temporal supervision strategy that leverages additional temporal observations of existing single-date annotated data.” (p. 1, seção 3 Lingnan University, Hong Kong 4 AMIAD, Pole Recherche, Fra)
- “In this paper, we propose to expand single-date semantic segmentation datasets into bi-temporal collections, leveraging easily accessible imagery.” (p. 2, seção 1. Introduction)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The added images have acquisition dates spanning 2022 to 2024, while IAILD’s original images were acquired before 2017.” (p. 3, seção 19 land cover classes. BD ORTHO is renewed on average)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Imagens aéreas**: 7 ocorrências (p. 2, 3)
- conjunto de dados **S2Looking**: 8 ocorrências (p. 4, 5, 7)
- conjunto de dados **LEVIR-CD**: 6 ocorrências (p. 4, 5, 7)
- conjunto de dados **WHU-CD**: 4 ocorrências (p. 4, 5, 7)
- resolução mencionada: 0.3 m (p. 3)
- resolução mencionada: 1.5 m (p. 4)
- resolução mencionada: 1.6 m (p. 4)
- “It consists of 180 patches of size 5000 × 5000 at a resolution of 0.3 m/px, annotated with binary building footprint masks.” (p. 3, seção 19 land cover classes. BD ORTHO is renewed on average)
- “For each bi-temporal pair, we downloaded the corresponding SPOT-6/7 images from IGN’s ORTHOSAT database [ 31 ] for the same acquisition year and location.” (p. 4, seção 19 land cover classes. BD ORTHO is renewed on average)
- “The images have a spatial resolution of 1.5 m/px, which we resampled to 1.6 m/px to obtain 64 × 64 patches.” (p. 4, seção 19 land cover classes. BD ORTHO is renewed on average)
- “[https://xavibou.github.io/CDviaWTS/](https://xavibou.github.io/CDviaWTS/) Ground truth Ours FSC-180k |2018 2021|Col2| |---|---| |2021<br>2018|2021<br>2018| Figure 1.” (p. 1, seção 3 Lingnan University, Hong Kong 4 AMIAD, Pole Recherche, Fra)
- “Over the past few years, SCD in remote sensing images has gained significant interest, leading to a large number of publications on the topic and several field surveys [ 2, 16, 38, 53 ].” (p. 2, seção 2. Related Works)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 54 ocorrências (p. 1, 2, 3, 4, 5)
- **Recorte em patches/tiles**: 4 ocorrências (p. 3, 4)
- **Aumento de dados**: 4 ocorrências (p. 3, 6)
- **Reamostragem**: 3 ocorrências (p. 4)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal e série (auto: 52 pares; 8 série)
**Métodos detectados automaticamente:**
- método/família **U-Net**: 23 ocorrências (p. 1, 5, 6, 7, 8)
- método/família **Supervisão fraca**: 9 ocorrências (p. 2, 3, 5, 6, 8)
- método/família **Transfer learning**: 3 ocorrências (p. 7, 8)
- método/família **Pós-classificação**: 3 ocorrências (p. 3, 6)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 1e-4” (p. 6)
- épocas/iterações: “100 epochs” (p. 6)
- otimizador: “AdamW optimizer [ 44 ] with a 1e-2 weight dec” (p. 6)
- perda: “focal losses” (p. 6)
- tamanho do patch: “512 × 512 FLAIR image patch” (p. 3)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 3 ocorrências (p. 2, 3, 8)
- **Teste externo / generalização**: 2 ocorrências (p. 1, 8)
- métrica **IoU**: 19 ocorrências (p. 5, 6, 7, 8)
- métrica **F1**: 15 ocorrências (p. 5, 6, 8)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “IoU scores on LEVIR-CD and S2Looking datasets when fine-tuning a Dual UNet on limited target data (1%, 10% and 30%).” (p. 7, seção 4. Experiments)
- “Scores reported on b-FLAIR-test. p real F1 IoU 0.00 72.3 56.6 0.10 76.1 61.4 0.25 77.0 62.6 0.35 73.8 58.5 0.50 73.6 58.2 XOR sIoU τ F1 IoU ✓ — 76.0 61.3 ✓ 0.75 74.8 59.7 ✓ 0.50 73.1 57.8 ✓ 0.25 77.0 62.6 Table 5.” (p. 8, seção 4. Experiments)

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 8)
- declaração: “Our approach achieves substantial improvements over the state of the art when only minimal annotations are available (e.g., 1%), while performance converges as more data is available.” (p. 8)
- hiperparâmetros **não detectados** automaticamente: batch (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Falsos alertas 5 (p. 6, 7); Custo 4 (p. 2, 3)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[ImagensAereas|Imagens aéreas]] — 7 ocorrências (p. 2, 3)
- emprega conjunto de dados: [[S2Looking|S2Looking]] — 8 ocorrências (p. 4, 5, 7)
- emprega conjunto de dados: [[LEVIRCD|LEVIR-CD]] — 6 ocorrências (p. 4, 5, 7)
- emprega conjunto de dados: [[WHUCD|WHU-CD]] — 4 ocorrências (p. 4, 5, 7)
- utiliza método: [[UNet|U-Net]] — 23 ocorrências (p. 1, 5, 6, 7, 8)
- utiliza método: [[SupervisaoFraca|Supervisão fraca]] — 9 ocorrências (p. 2, 3, 5, 6, 8)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[MudancaSemantica|Mudança semântica (from–to)]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[ClassificacaoCobertura|Classificação de cobertura e uso da terra]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
