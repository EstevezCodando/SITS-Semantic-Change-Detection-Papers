---
tipo: artigo
id_origem: P133
titulo: "Adapting Segment Anything Model for Change Detection in VHR Remote Sensing Images"
ano: 2024
autores: ["Lei Ding", "Kun Zhu", "Daifeng Peng", "Hao Tang", "Kuiwu Yang", "Lorenzo Bruzzone"]
doi: "10.1109/tgrs.2024.3368168"
arquivo_fonte: "coleta/P133_Ding2024_Adapting-Segment-Anything-Model-for-Change-Detection-in-VHR-.pdf"
markdown_fonte: "output/pdf/P133_Ding2024_Adapting-Segment-Anything-Model-for-Change-Detection-in-VHR-/document.md"
paginas: 11
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]"]
sensores: []
conjuntos_dados: ["[[WHUCD|WHU-CD]]", "[[S2Looking|S2Looking]]"]
metodos: ["[[SAM|Segment Anything (SAM)]]", "[[CNN|Redes convolucionais (CNN)]]", "[[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Ding 2024 — Adapting Segment Anything Model for Change Detection in VHR Remote Sensing Images

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Lei Ding, Kun Zhu, Daifeng Peng, Hao Tang et al. (2024). Adapting Segment Anything Model for Change Detection in VHR Remote Sensing Images. IEEE Transactions on Geoscience and Remote Sensing. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1109/tgrs.2024.3368168
- **Arquivo de origem:** `coleta/P133_Ding2024_Adapting-Segment-Anything-Model-for-Change-Detection-in-VHR-.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P133_Ding2024_Adapting-Segment-Anything-Model-for-Change-Detection-in-VHR-/document.md` — 11 páginas, 62 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “To adapt FastSAM to focus on some specific ground objects in RS scenes, we propose a convolutional adaptor to aggregate the task-oriented change information.” (p. 1, seção Início)
- “Moreover, to utilize the semantic representations that are inherent to SAM features, we introduce a task-agnostic semantic learning branch to model the semantic latent in bi-temporal RSIs.” (p. 1, seção Início)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “It consists of Google Earth images collected in 6 cities in Texas, US between 2012 and 2016.” (p. 5, seção IV. E XPERIMENTAL R ESULTS)
- “The RSIs were collected in Christchurch, New Zealand between 2012 and 2016, covering an urban area of 20.5 km .” (p. 5, seção IV. E XPERIMENTAL R ESULTS)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- conjunto de dados **WHU-CD**: 11 ocorrências (p. 5, 7, 8, 9, 10)
- conjunto de dados **S2Looking**: 9 ocorrências (p. 5, 7, 8, 9)
- conjunto de dados **LEVIR-CD**: 2 ocorrências (p. 5)
- resolução mencionada: 0.5 m (p. 5)
- resolução mencionada: 0.2 m (p. 5)
- “The split of training, validation and test sets is 320, 120 and 120 image pairs, respectively.” (p. 5, seção IV. E XPERIMENTAL R ESULTS)
- “Therefore, we propose a temporal constraint loss L t to measure their temporal similarity, calculated as: L t ( l 1 , l 2 ) = [1 − cosine ( l 1 , l 2 )] · c, (6) where c is the ground truth (GT) change label on which unchanged areas are ann” (p. 4, seção III. P ROPOSED M ETHOD)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 10 ocorrências (p. 1, 2, 3, 4, 5)
- **Aumento de dados**: 5 ocorrências (p. 2, 4, 8)
- **Normalização / escala**: 4 ocorrências (p. 3, 4)
- **Recorte em patches/tiles**: 3 ocorrências (p. 5, 10)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal e série (auto: 9 pares; 8 série)
**Métodos detectados automaticamente:**
- método/família **SAM**: 109 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **CNN**: 22 ocorrências (p. 1, 2, 3, 5, 6)
- método/família **Semi/auto-supervisionado**: 16 ocorrências (p. 1, 2, 8, 9, 10)
- método/família **Transformer**: 14 ocorrências (p. 1, 2, 5, 7, 10)
- método/família **Rede siamesa**: 13 ocorrências (p. 1, 2, 3, 5, 6)
- método/família **Modelo fundacional**: 7 ocorrências (p. 1, 2, 3)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate to 0.1 and update it at each iteration as 0 ” (p. 4)
- épocas/iterações: “50 epochs” (p. 4)
- tamanho do patch: “1024 × 1024 pixel” (p. 5)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Teste externo / generalização**: 7 ocorrências (p. 1, 2, 3, 8, 9)
- **Conjuntos treino/val/teste**: 3 ocorrências (p. 5)
- métrica **IoU**: 18 ocorrências (p. 5, 6, 7, 8, 9)
- métrica **Acurácia global**: 13 ocorrências (p. 5, 6, 7, 8, 9)
- métrica **F1**: 5 ocorrências (p. 6, 7, 8)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/ggsDing/SAM-CD (p. 4)
- URL citada: https://github.com/ggsDing/SAM-CD (p. 4)
- declaração: “For more details, readers are encouraged to visit our codes [released at: https://github.com/ggsDing/SAM-CD.](https://github.com/ggsDing/SAM-CD)” (p. 4)
- hiperparâmetros **não detectados** automaticamente: batch, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 4 (p. 5, 7, 8); Quase tempo real 1 (p. 2); Falsos alertas 1 (p. 7)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- emprega conjunto de dados: [[WHUCD|WHU-CD]] — 11 ocorrências (p. 5, 7, 8, 9, 10)
- emprega conjunto de dados: [[S2Looking|S2Looking]] — 9 ocorrências (p. 5, 7, 8, 9)
- utiliza método: [[SAM|Segment Anything (SAM)]] — 109 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 22 ocorrências (p. 1, 2, 3, 5, 6)
- utiliza método: [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 16 ocorrências (p. 1, 2, 8, 9, 10)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
