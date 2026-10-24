---
tipo: artigo
id_origem: P31
titulo: "TextSCD: Leveraging Text-based Semantic Guidance for Remote Sensing Image Semantic Change Detection"
ano: 2025
autores: ["Haiyan Huang", "Qimin Cheng", "Duowang Zhu", "Xiao Huang", "Qunshan Zhao"]
doi: "10.5194/isprs-annals-x-g-2025-383-2025"
arquivo_fonte: "coleta/P31_Huang2025_TextSCD-Leveraging-Text-based-Semantic-Guidance-for-Remote-S.pdf"
markdown_fonte: "output/pdf/P31_Huang2025_TextSCD-Leveraging-Text-based-Semantic-Guidance-for-Remote-S/document.md"
paginas: 7
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[MudancaSemantica|Mudança semântica (from–to)]]"]
sensores: []
conjuntos_dados: ["[[SECOND|SECOND]]"]
metodos: ["[[Transformer|Transformers]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]"]
validacao: ["[[F1|F1]]", "[[AcuraciaGlobal|Acurácia global (OA)]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Huang 2025 — TextSCD: Leveraging Text-based Semantic Guidance for Remote Sensing Image Semantic Change Detection

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Haiyan Huang, Qimin Cheng, Duowang Zhu, Xiao Huang et al. (2025). TextSCD: Leveraging Text-based Semantic Guidance for Remote Sensing Image Semantic Change Detection. ISPRS annals of the photogrammetry, remote sensing and spatial information sciences. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.5194/isprs-annals-x-g-2025-383-2025
- **Arquivo de origem:** `coleta/P31_Huang2025_TextSCD-Leveraging-Text-based-Semantic-Guidance-for-Remote-S.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P31_Huang2025_TextSCD-Leveraging-Text-based-Semantic-Guidance-for-Remote-S/document.md` — 7 páginas, 37 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Semantic change detection (SCD) in remote sensing image aims to identify semantic alterations between bi-temporal images captured at the same geographic location. SCD is extensively applied in fields such as environmental monitoring and disaster assessment. Despite significant advancements in deep learning leading to numerous successful approaches, most existing methods primarily rely on visual representation learning, thereby overlooking the potential benefits of multimodal data. Recently, visionlanguage models have demonstrated outstanding performance across various downstream tasks. In this paper, we propose a novel framework named TextSCD that leverages text-based semantic information to guide the generation of semantic change maps. Our approach integrates Gemini to generate change descriptions between bi-temporal images and employs a multi-level semantic extraction method to capture…

- “In this paper, we propose a novel framework named TextSCD that leverages text-based semantic information to guide the generation of semantic change maps.” (p. 1, seção Abstract)
- “Furthermore, we introduce a semantic text-guided interaction module that facilitates the effective integration of visual and textual features, enhancing multimodal knowledge transfer and the extraction of discriminative features.” (p. 1, seção Abstract)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- conjunto de dados **SECOND**: 5 ocorrências (p. 1, 2, 4)
- resolução mencionada: 0.3 m (p. 4)
- resolução mencionada: 0.5 m (p. 4)
- “L bce ( Y, P ) = − N N � [ Y i log 2 P i + (1 − Y i ) log 2 (1 − P i )] , i =1 (10) where Y and P denote the ground truth and predicted change map, respectively, and N is the number of total pixels of a change map.” (p. 4, seção 3. We conduct experiments on the SECOND dataset. The)
- “L sim =  1 − cos P 1 [i,j] [, P] [ i,j] 2 , if GT [i,j] = 0 � � (11) cos P 1 [i,j] [, P] [ i,j] 2 , if GT [i,j] = 1 � � Text Features Transformer layers where P 1 [i,j] [, P] [ i,j] 2 denote the predicted maps in ( i, j ), GT [i,j] rep” (p. 4, seção 3. We conduct experiments on the SECOND dataset. The)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 4 ocorrências (p. 1, 4, 5)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal e série (auto: 12 pares; 5 série)
**Métodos detectados automaticamente:**
- método/família **Transformer**: 6 ocorrências (p. 1, 2, 4)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 0.1” (p. 4)
- batch: “batch size is set to 8, with an initial learning r” (p. 4)
- otimizador: “SGD) optimizer is utilized with a momentum ” (p. 4)
- perda: “dice loss (Milletari et al” (p. 4)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- métrica **F1**: 3 ocorrências (p. 4, 5)
- métrica **Acurácia global**: 3 ocorrências (p. 1, 4)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “In future work, we will explore the integration of multimodal information in semi-supervised or unsupervised semantic change detection tasks to overcome challenges associated with pixellevel annotations.” (p. 5, seção 3. We conduct experiments on the SECOND dataset. The)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado
- hiperparâmetros **não detectados** automaticamente: épocas/iterações (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Persistência / confirmação 1 (p. 1)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- emprega conjunto de dados: [[SECOND|SECOND]] — 5 ocorrências (p. 1, 2, 4)
- utiliza método: [[Transformer|Transformers]] — 6 ocorrências (p. 1, 2, 4)
- é avaliado por: [[F1|F1]] — 3 ocorrências (p. 4, 5)
- é avaliado por: [[AcuraciaGlobal|Acurácia global (OA)]] — 3 ocorrências (p. 1, 4)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 4 ocorrências (p. 1, 4, 5)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[MudancaSemantica|Mudança semântica (from–to)]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
