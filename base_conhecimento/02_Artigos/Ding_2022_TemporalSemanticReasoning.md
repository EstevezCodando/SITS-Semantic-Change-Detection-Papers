---
tipo: artigo
id_origem: P21
titulo: "Bi-Temporal Semantic Reasoning for the Semantic Change Detection in HR Remote Sensing Images"
ano: 2022
autores: ["Lei Ding", "Haitao Guo", "Sicong Liu", "Lichao Mou", "Jing Zhang", "Lorenzo Bruzzone"]
doi: "10.1109/tgrs.2022.3154390"
arquivo_fonte: "coleta/P21_Ding2022_Bi-Temporal-Semantic-Reasoning-for-the-Semantic-Change-Detec.pdf"
markdown_fonte: "output/pdf/P21_Ding2022_Bi-Temporal-Semantic-Reasoning-for-the-Semantic-Change-Detec/document.md"
paginas: 14
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[MudancaSemantica|Mudança semântica (from–to)]]"]
sensores: ["[[SAR|Radar (SAR)]]"]
conjuntos_dados: ["[[HRSCD|HRSCD]]"]
metodos: ["[[CNN|Redes convolucionais (CNN)]]", "[[RedeSiamesa|Redes siamesas]]", "[[LSTM|Redes recorrentes (LSTM)]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Ding 2022 — Bi-Temporal Semantic Reasoning for the Semantic Change Detection in HR Remote Sensing Images

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Lei Ding, Haitao Guo, Sicong Liu, Lichao Mou et al. (2022). Bi-Temporal Semantic Reasoning for the Semantic Change Detection in HR Remote Sensing Images. IEEE Transactions on Geoscience and Remote Sensing. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1109/tgrs.2022.3154390
- **Arquivo de origem:** `coleta/P21_Ding2022_Bi-Temporal-Semantic-Reasoning-for-the-Semantic-Change-Detec.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P21_Ding2022_Bi-Temporal-Semantic-Reasoning-for-the-Semantic-Change-Detec/document.md` — 14 páginas, 99 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “To overcome the limitations in existing methods, we propose a novel CNN architecture for the SCD, where the semantic temporal features are merged in a deep CD unit.” (p. 1, seção Início)
- “N ETWORK (B I -SRN ET ) FOR SCD In this section we introduce the Bi-SRNet for SCD.” (p. 3, seção III. P ROPOSED B I - TEMPORAL S EMANTIC R EASONING)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **SAR**: 5 ocorrências (p. 2, 3, 13)
- conjunto de dados **HRSCD**: 18 ocorrências (p. 4, 9, 10, 12)
- resolução mencionada: 0.5 m (p. 7)
- resolução mencionada: 3 m (p. 7)
- “We further split them into a training set and a test set with the numeric ratio of 4 : 1 (i.e., 2375 image pairs for training, 593 ones for testing).” (p. 7, seção IV. D ATASET D ESCRIPTION AND E XPERIMENTAL)
- “The required training labels in the SCD can be either i) two ground truth (GT) semantic change maps L 1 and L 2 , or alternatively ii) one GT binary CD map L c and two GT LCLU maps L S 1 and L S 2 .” (p. 3, seção III. P ROPOSED B I - TEMPORAL S EMANTIC R EASONING)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Aumento de dados**: 2 ocorrências (p. 7)
- **Rotulagem / anotação**: 2 ocorrências (p. 3, 7)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal e série (auto: 23 pares; 7 série)
**Métodos detectados automaticamente:**
- método/família **CNN**: 52 ocorrências (p. 1, 2, 3, 4, 7)
- método/família **Rede siamesa**: 11 ocorrências (p. 2, 3, 4, 5, 8)
- método/família **LSTM / recorrente**: 9 ocorrências (p. 2, 9, 10, 12, 13)
- método/família **U-Net**: 4 ocorrências (p. 8, 9, 10, 14)
- método/família **Semi/auto-supervisionado**: 4 ocorrências (p. 2, 3, 13)
**Hiperparâmetros detectados automaticamente (verificar):**
- batch: “batch size (8), running epochs (50) and initial le” (p. 7)
- épocas/iterações: “100 epochs” (p. 7)
- otimizador: “SGD) with Nesterov momentum” (p. 7)
- perda: “binary cross entropy loss between the predicted bina” (p. 6)
- tamanho do patch: “512 × 512 pixel” (p. 7)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- métrica **IoU**: 20 ocorrências (p. 7, 8, 9)
- métrica **Acurácia global**: 9 ocorrências (p. 7, 9)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/ggsDing/Bi-SRNet (p. 1)
- URL citada: https://github.com/ggsDing/Bi-SRNet (p. 1)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 4 (p. 7, 8, 9)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[SAR|Radar (SAR)]] — 5 ocorrências (p. 2, 3, 13)
- emprega conjunto de dados: [[HRSCD|HRSCD]] — 18 ocorrências (p. 4, 9, 10, 12)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 52 ocorrências (p. 1, 2, 3, 4, 7)
- utiliza método: [[RedeSiamesa|Redes siamesas]] — 11 ocorrências (p. 2, 3, 4, 5, 8)
- utiliza método: [[LSTM|Redes recorrentes (LSTM)]] — 9 ocorrências (p. 2, 9, 10, 12, 13)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[MudancaSemantica|Mudança semântica (from–to)]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
