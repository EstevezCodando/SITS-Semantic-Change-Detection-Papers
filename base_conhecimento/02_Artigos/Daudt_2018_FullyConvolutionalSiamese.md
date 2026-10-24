---
tipo: artigo
id_origem: P23
titulo: "Fully Convolutional Siamese Networks for Change Detection"
ano: 2018
autores: ["Rodrigo Caye Daudt", "Bertrand Le Saux", "Alexandre Boulch"]
doi: "10.48550/arXiv.1810.08462"
arquivo_fonte: "coleta/P23_Daudt2018_Fully-Convolutional-Siamese-Networks-for-Change-Detection.pdf"
markdown_fonte: "output/pdf/P23_Daudt2018_Fully-Convolutional-Siamese-Networks-for-Change-Detection/document.md"
paginas: 5
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]"]
sensores: ["[[ImagensAereas|Imagens aéreas]]", "[[Landsat|Landsat]]", "[[SAR|Radar (SAR)]]"]
conjuntos_dados: ["[[OSCD|OSCD]]"]
metodos: ["[[RedeSiamesa|Redes siamesas]]", "[[UNet|U-Net]]", "[[CNN|Redes convolucionais (CNN)]]"]
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]"]
validacao: ["[[F1|F1]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Daudt 2018 — Fully Convolutional Siamese Networks for Change Detection

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Rodrigo Caye Daudt, Bertrand Le Saux, Alexandre Boulch (2018). Fully Convolutional Siamese Networks for Change Detection. arXiv (Cornell University). Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.48550/arXiv.1810.08462
- **Arquivo de origem:** `coleta/P23_Daudt2018_Fully-Convolutional-Siamese-Networks-for-Change-Detection.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P23_Daudt2018_Fully-Convolutional-Siamese-Networks-for-Change-Detection/document.md` — 5 páginas, 20 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** This paper presents three fully convolutional neural network architectures which perform change detection using a pair of coregistered images. Most notably, we propose two Siamese extensions of fully convolutional networks which use heuristics about the current problem to achieve the best results in our tests on two open change detection datasets, using both RGB and multispectral images. We show that our system is able to learn from scratch using annotated change detection images. Our architectures achieve better performance than previously proposed methods, while being at least 500 times faster than related systems. This work is a step towards efficient processing of data from large scale Earth observation systems such as Copernicus or Landsat. Index Terms — Change detection, supervised machine learning, fully convolutional networks, Earth observation. Change Detection (CD) is one of th…

- “This paper presents three fully convolutional neural network architectures which perform change detection using a pair of coregistered images.” (p. 1, seção ABSTRACT)
- “Most notably, we propose two Siamese extensions of fully convolutional networks which use heuristics about the current problem to achieve the best results in our tests on two open change detection datasets, using both RGB and multispectral ” (p. 1, seção ABSTRACT)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Imagens aéreas**: 5 ocorrências (p. 1, 3, 5)
- sensor/produto **Landsat**: 3 ocorrências (p. 1, 4)
- sensor/produto **SAR**: 3 ocorrências (p. 2, 4, 5)
- conjunto de dados **OSCD**: 13 ocorrências (p. 1, 3, 4)
- “Szada-1 and Tiszadob-3 images were extracted for testing, and the rest of the data for each location (another 6 and 4 images, respectively) was used for training.” (p. 3, seção 90 degrees to the training patches. Dropout was used to help)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 9 ocorrências (p. 2, 3, 4, 5)
- **Rotulagem / anotação**: 3 ocorrências (p. 1)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal / pares (auto: 10 menções)
**Métodos detectados automaticamente:**
- método/família **Rede siamesa**: 16 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **U-Net**: 6 ocorrências (p. 2, 3, 5)
- método/família **CNN**: 5 ocorrências (p. 1, 2, 5)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- métrica **F1**: 6 ocorrências (p. 3, 4)
- métrica **Precisão/Recall**: 6 ocorrências (p. 3)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “For example, most of the networks have been trained on RGB images, and cannot be transfered for SAR or multispectral images, which is the case of the dataset presented in .” (p. 2, seção 2. RELATED WORK)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Latência / frequência 1 (p. 4); Custo 1 (p. 4)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[ImagensAereas|Imagens aéreas]] — 5 ocorrências (p. 1, 3, 5)
- utiliza dado/sensor: [[Landsat|Landsat]] — 3 ocorrências (p. 1, 4)
- utiliza dado/sensor: [[SAR|Radar (SAR)]] — 3 ocorrências (p. 2, 4, 5)
- emprega conjunto de dados: [[OSCD|OSCD]] — 13 ocorrências (p. 1, 3, 4)
- utiliza método: [[RedeSiamesa|Redes siamesas]] — 16 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[UNet|U-Net]] — 6 ocorrências (p. 2, 3, 5)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 5 ocorrências (p. 1, 2, 5)
- é avaliado por: [[F1|F1]] — 6 ocorrências (p. 3, 4)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 9 ocorrências (p. 2, 3, 4, 5)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
