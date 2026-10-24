---
tipo: artigo
id_origem: P56
titulo: "The Segment Anything Model (SAM) for remote sensing applications: From zero to one shot"
ano: 2023
autores: ["Lucas Prado Osco", "Qiusheng Wu", "Eduardo Lopes de Lemos", "Wesley Nunes Gonçalves", "Ana Paula Marques Ramos", "Jonathan Li", "José Marcato"]
doi: "10.1016/j.jag.2023.103540"
arquivo_fonte: "coleta/P56_Osco2023_The-Segment-Anything-Model-SAM-for-remote-sensing-applicatio.pdf"
markdown_fonte: "output/pdf/P56_Osco2023_The-Segment-Anything-Model-SAM-for-remote-sensing-applicatio/document.md"
paginas: 21
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: []
sensores: ["[[UAV|UAV / drones]]"]
conjuntos_dados: []
metodos: ["[[SAM|Segment Anything (SAM)]]", "[[Transformer|Transformers]]", "[[TransferLearning|Aprendizado por transferência]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Osco 2023 — The Segment Anything Model (SAM) for remote sensing applications: From zero to one shot

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Lucas Prado Osco, Qiusheng Wu, Eduardo Lopes de Lemos, Wesley Nunes Gonçalves et al. (2023). The Segment Anything Model (SAM) for remote sensing applications: From zero to one shot. International Journal of Applied Earth Observation and Geoinformation. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1016/j.jag.2023.103540
- **Arquivo de origem:** `coleta/P56_Osco2023_The-Segment-Anything-Model-SAM-for-remote-sensing-applicatio.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P56_Osco2023_The-Segment-Anything-Model-SAM-for-remote-sensing-applicatio/document.md` — 21 páginas, 9 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “This study aims to advance the application of the Segment Anything Model (SAM), an innovative image segmentation model by Meta AI, in the field of remote sensing image analysis.” (p. 1, seção Início)
- “In this context, we present a first-of-its-kind evaluation of SAM, developing both its zero and one-shot learning performance on segmenting remote sensing imagery.” (p. 2, seção 1 Introduction)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **UAV**: 9 ocorrências (p. 4, 5, 9, 18)
- sensor/produto **SkySat**: 2 ocorrências (p. 4, 5)
- resolução mencionada: 0.01 m (p. 9)
- resolução mencionada: 0.04 m (p. 9)
- resolução mencionada: 0.20 m (p. 9)
- “The total quantifiable size of these datasets surpasses 90 Gigabytes and comprises more than 10,000 images and image patches.” (p. 4, seção 3 Materials and Methods)
- “In contrast, one-shot learning denotes a model’s ability to interpret and make accurate inferences from just a single example of a new class [ 70 ].” (p. 1, seção 1 Introduction)
- “This permitted an evaluation of these models’ capabilities to understand, interpret, and transform textual inputs into precise segmentation outputs.” (p. 4, seção 3 Materials and Methods)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 27 ocorrências (p. 1, 2, 3, 8, 9)
- **Recorte em patches/tiles**: 8 ocorrências (p. 4, 8, 9)
- **Mosaicos e compostos**: 5 ocorrências (p. 5, 6, 8)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **SAM**: 177 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Transformer**: 14 ocorrências (p. 2, 3, 5, 8, 17)
- método/família **Transfer learning**: 12 ocorrências (p. 1, 3, 7, 15)
- método/família **CNN**: 6 ocorrências (p. 3, 18)
- método/família **OBIA**: 3 ocorrências (p. 2, 7)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate is scheduled using the Cosine Annealing method [ ” (p. 8)
- épocas/iterações: “1000 epochs” (p. 8)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Teste externo / generalização**: 6 ocorrências (p. 1, 15, 17, 18)
- métrica **IoU**: 8 ocorrências (p. 8, 9, 11, 15)
- métrica **Precisão/Recall**: 7 ocorrências (p. 2, 4, 6)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “To overcome this limitation, SAM can be modified by a relearning approach [ 70 ], feeding it with a single example of a new class or object for better results.” (p. 1, seção 1 Introduction)
- “In this study, we also discuss the implications, limitations, and potential future directions of our findings.” (p. 2, seção 1 Introduction)
- “In our study, we aim to evaluate the performance of SAM across these sources to understand its applicability and limitations in diverse contexts.” (p. 4, seção 3 Materials and Methods)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/LucasOsco/AI-RemoteSensing (p. 18)
- URL citada: https://github.com/LucasOsco/AI-RemoteSensing (p. 18)
- URL citada: https://github.com/opengeos/segment-geospatial (p. 18)
- declaração: “Furthermore, we provide the open-source code of our modifications on online repositories, encouraging further and broader adaptations of SAM to the remote sensing domain.” (p. 1)
- hiperparâmetros **não detectados** automaticamente: batch, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Quase tempo real 3 (p. 15, 18); Custo 3 (p. 8, 18); Sistema operacional 1 (p. 18)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[UAV|UAV / drones]] — 9 ocorrências (p. 4, 5, 9, 18)
- utiliza método: [[SAM|Segment Anything (SAM)]] — 177 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[Transformer|Transformers]] — 14 ocorrências (p. 2, 3, 5, 8, 17)
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 12 ocorrências (p. 1, 3, 7, 15)

## Anotações do leitor

- 
