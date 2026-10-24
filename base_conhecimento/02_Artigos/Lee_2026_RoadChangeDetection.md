---
tipo: artigo
id_origem: P40
titulo: "Road Change Detection Using Maps and Aerial Imagery for Digital Map Updating"
ano: 2026
autores: ["Juhee Lee", "Chang-Young Lee", "Inhyeok Lee", "Bui Ngoc An", "Jangwoo Cheon", "Impyeong Lee"]
doi: "10.7780/kjrs.2026.42.2.5"
arquivo_fonte: "coleta/P40_Lee2026_Road-Change-Detection-Using-Maps-and-Aerial-Imagery-for-Digi.pdf"
markdown_fonte: "output/pdf/P40_Lee2026_Road-Change-Detection-Using-Maps-and-Aerial-Imagery-for-Digi/document.md"
paginas: 18
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[Vias|Vias e estradas]]"]
sensores: ["[[ImagensAereas|Imagens aéreas]]"]
conjuntos_dados: []
metodos: ["[[TransferLearning|Aprendizado por transferência]]"]
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]", "[[AumentoDados|Aumento de dados]]", "[[Rotulagem|Rotulagem e anotação]]"]
validacao: ["[[Desbalanceamento|Desbalanceamento de classes]]", "[[Generalizacao|Generalização e domain shift]]", "[[PrecisaoRecall|Precisão e recall]]", "[[F1|F1]]", "[[IoU|IoU / mIoU]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Lee 2026 — Road Change Detection Using Maps and Aerial Imagery for Digital Map Updating

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Juhee Lee, Chang-Young Lee, Inhyeok Lee, Bui Ngoc An et al. (2026). Road Change Detection Using Maps and Aerial Imagery for Digital Map Updating. 대한원격탐사학회지. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.7780/kjrs.2026.42.2.5
- **Arquivo de origem:** `coleta/P40_Lee2026_Road-Change-Detection-Using-Maps-and-Aerial-Imagery-for-Digi.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P40_Lee2026_Road-Change-Detection-Using-Maps-and-Aerial-Imagery-for-Digi/document.md` — 18 páginas, 22 recortes de figuras, 1 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “This study proposes a deep learning–based framework for road change detection that integrates existing maps and high-resolution aerial orthophotos to support digital map updating.” (p. 1, seção 5 Principal Researcher, Geospatial Team, InnoPAM, Seoul, Rep)
- “To address the severe class imbalance commonly observed in road change detection tasks, we introduce a dataset construction strategy that combines synthetic map modification and tile filtering to increase the proportion of informative chang” (p. 1, seção 5 Principal Researcher, Geospatial Team, InnoPAM, Seoul, Rep)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “In this study, to objectively evaluate the learning efficiency and cross-regional generalization performance of the proposed road change detection model, we divided the study area into training and evaluation regions.” (p. 3, seção 2.1. Study Area)
- “Geographical overview of the study area, displaying the training regions (Anyang-si and Jungnang-gu) and independent test areas (Gangnamgu and Gangseo-gu) alongside their corresponding aerial orthophoto. https://www.kjrs.org 231” (p. 3, seção 2.1. Study Area)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Imagens aéreas**: 4 ocorrências (p. 1, 2)
- resolução mencionada: 12 cm (p. 4)
- “The original dataset (OD) refers to the initial training setup where aerial orthophotos are simply partitioned into 512 × 512 tiles without additional augmentation or filtering.” (p. 5, seção 3.1. Overall Framework)
- “The OD, as the initial dataset, consists of 15,934 tiles and suffers from a severe class imbalance with an extremely low proportion of change classes, as it has not undergone any augmentation or selection processes.” (p. 9, seção 4.1. Experimental Setup)
- “To resolve this imbalance, geometric augmentation, including 90-degree rotations and horizontal/vertical flips, was applied to the 201 tiles containing changes within the OD, generating a total of 905 change tiles.” (p. 9, seção 4.1. Experimental Setup)
- “Changes are typically subjected to a primary screening process followed by secondary validation through aerial photography, which frequently requires repetitive manual interpretation.” (p. 2, seção 1. Introduction)
- “Additionally, there are practical limitations to conducting field surveys with restricted personnel.” (p. 2, seção 1. Introduction)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 31 ocorrências (p. 1, 3, 4, 5, 7)
- **Aumento de dados**: 6 ocorrências (p. 5, 7, 9)
- **Rotulagem / anotação**: 6 ocorrências (p. 4, 5, 9, 10, 15)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **Transfer learning**: 12 ocorrências (p. 1, 3, 6, 12, 13)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate to 0.00006 to ensure stable convergence” (p. 9)
- batch: “batch size was configured to 6, considering GPU me” (p. 9)
- otimizador: “AdamW optimizer for weight updates, setting t” (p. 9)
- perda: “cross-entropy in Eq” (p. 9)
- tamanho do patch: “512 × 512 pixel tile” (p. 5)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Desbalanceamento**: 21 ocorrências (p. 1, 3, 7, 8, 9)
- **Teste externo / generalização**: 4 ocorrências (p. 3, 4, 5, 16)
- métrica **Precisão/Recall**: 98 ocorrências (p. 7, 8, 9, 10, 11)
- métrica **F1**: 30 ocorrências (p. 10, 11, 12, 13, 14)
- métrica **IoU**: 21 ocorrências (p. 10, 11, 13, 14, 15)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “Specifically, in Gangnam-gu, the recall for New and Removed classes was notably low at 0.289 and 0.190, respectively, indicating a tendency to miss change areas.” (p. 11, seção 4.2.1. Dataset Strategy Comparison)
- “In Gangnam-gu, the recall for New and Removed classes improved to 0.725 and 0.519, respectively.” (p. 11, seção 4.2.1. Dataset Strategy Comparison)
- “A similar trend was observed in Gangseo-gu, where recall increased to 0.758 and 0.763.” (p. 11, seção 4.2.1. Dataset Strategy Comparison)
- “In the Gangnam-gu results (Table 7), it recorded a recall of 0.725 and an F1-score of 0.457 for the New class.” (p. 12, seção 4.2.2. Fine-Tuning Strategy Comparison)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “Moreover, the heavy reliance on aerial photography creates a temporal lag—a “blackout” period—determined by acquisition schedules and project bidding cycles, during which changes cannot be reflected in real-time.” (p. 2, seção 1. Introduction)
- “Additionally, there are practical limitations to conducting field surveys with restricted personnel.” (p. 2, seção 1. Introduction)
- “To overcome these limitations, research on deep learningbased change detection has been actively conducted in recent years.” (p. 2, seção 1. Introduction)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 17)
- declaração: “Future research will aim to improve detection performance for sparse change classes and expand the scope of the framework through validation across more diverse regions and environmental conditions. ### Author Contributions Conceptualizatio” (p. 17)
- hiperparâmetros **não detectados** automaticamente: épocas/iterações (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Persistência / confirmação 4 (p. 11, 16); Quase tempo real 1 (p. 2)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[ImagensAereas|Imagens aéreas]] — 4 ocorrências (p. 1, 2)
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 12 ocorrências (p. 1, 3, 6, 12, 13)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 98 ocorrências (p. 7, 8, 9, 10, 11)
- é avaliado por: [[F1|F1]] — 30 ocorrências (p. 10, 11, 12, 13, 14)
- é avaliado por: [[IoU|IoU / mIoU]] — 21 ocorrências (p. 10, 11, 13, 14, 15)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 31 ocorrências (p. 1, 3, 4, 5, 7)
- aplica etapa de preparo: [[AumentoDados|Aumento de dados]] — 6 ocorrências (p. 5, 7, 9)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 6 ocorrências (p. 4, 5, 9, 10, 15)
- adota desenho de validação: [[Desbalanceamento|Desbalanceamento de classes]] — 21 ocorrências (p. 1, 3, 7, 8, 9)
- adota desenho de validação: [[Generalizacao|Generalização e domain shift]] — 4 ocorrências (p. 3, 4, 5, 16)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Vias|Vias e estradas]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
