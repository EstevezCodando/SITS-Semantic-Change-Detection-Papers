---
tipo: artigo
id_origem: P105
titulo: "Tracking Urbanization in Developing Regions with Remote Sensing Spatial-Temporal Super-Resolution"
ano: 2022
autores: ["Yutong He", "William Zhang", "Chenlin Meng", "Marshall Burke", "David B. Lobell", "Stefano Ermon"]
doi: "10.48550/arXiv.2204.01736"
arquivo_fonte: "coleta/P105_He2022_Tracking-Urbanization-in-Developing-Regions-with-Remote-Sens.pdf"
markdown_fonte: "output/pdf/P105_He2022_Tracking-Urbanization-in-Developing-Regions-with-Remote-Sens/document.md"
paginas: 7
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[SITS|Séries temporais de imagens (SITS)]]", "[[Edificacoes|Edificações e urbanização]]"]
sensores: []
conjuntos_dados: ["[[SpaceNet7_MUDS|SpaceNet 7 / MUDS]]"]
metodos: ["[[SuperResolucao|Super-resolução]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]"]
validacao: ["[[IoU|IoU / mIoU]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# He 2022 — Tracking Urbanization in Developing Regions with Remote Sensing Spatial-Temporal Super-Resolution

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Yutong He, William Zhang, Chenlin Meng, Marshall Burke et al. (2022). Tracking Urbanization in Developing Regions with Remote Sensing Spatial-Temporal Super-Resolution. arXiv (Cornell University). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2204.01736
- **Arquivo de origem:** `coleta/P105_He2022_Tracking-Urbanization-in-Developing-Regions-with-Remote-Sens.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P105_He2022_Tracking-Urbanization-in-Developing-Regions-with-Remote-Sens/document.md` — 7 páginas, 2 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Automated tracking of urban development in areas where construction information is not available became possible with recent advancements in machine learning and remote sensing. Unfortunately, these solutions perform best on high-resolution imagery, which is expensive to acquire and infrequently available, making it difficult to scale over long time spans and across large geographies. In this work, we propose a pipeline that leverages a single high-resolution image and a time series of publicly available low-resolution images to generate accurate high-resolution time series for object tracking in urban construction. Our method achieves significant improvement in comparison to baselines using single image super-resolution, and can assist in extending the accessibility and scalability of building construction tracking across the developing world. 1 Introduction Accurate measures of buildin…

- “In this work, we propose a pipeline that leverages a single high-resolution image and a time series of publicly available low-resolution images to generate accurate high-resolution time series for object tracking in urban construction.” (p. 1, seção Abstract)
- “Inspired by this success, we propose a pipeline that uses a spatial-temporal super-resolution model which uses one HR image and a times series of low-resolution (LR) images to generate the target HR time series, which is then input into an ” (p. 2, seção Abstract)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The released dataset contains images and building footprint labels between 2017 and 2020 in 60 locations across the globe, which were selected to be geographically diverse and display dramatic changes in urbanization.” (p. 3, seção Abstract)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Landsat**: 2 ocorrências (p. 2, 3)
- conjunto de dados **SpaceNet 7 (MUDS)**: 8 ocorrências (p. 2, 3, 4, 5)
- resolução mencionada: 4 m (p. 1)
- resolução mencionada: 30 m (p. 2)
- “Each location has approximately 24 images (one per month) with dimensions of 1024 × 1024 pixels, corresponding to an area of ≈ 18 km .” (p. 3, seção Abstract)
- “At inference time, we use the generating by patch technique in to generate the large 1024 × 1024 images.” (p. 4, seção Abstract)
- “The model is trained with 256 × 256 images and inference with the same generating by patch technique to create the 1024 × 1024 images.” (p. 4, seção Abstract)
- “We also compare the generated images with the ground truth HR and LR images.” (p. 4, seção Abstract)
- “We use the same ground truth building footprints for both settings.” (p. 4, seção Abstract)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 11 ocorrências (p. 1, 4, 5, 6)
- **Recorte em patches/tiles**: 3 ocorrências (p. 4)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 20 menções vs 0 de pares)
**Métodos detectados automaticamente:**
- método/família **Super-resolução**: 26 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Transfer learning**: 3 ocorrências (p. 4)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate 2 × 10 [−] , β 0 = 0 , β 1 = 0 ” (p. 4)
- otimizador: “Adam optimizer with learning rate 2 × 10 [−]” (p. 4)
- tamanho do patch: “1024 × 1024 pixel” (p. 3)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- métrica **IoU**: 4 ocorrências (p. 4, 5)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado
- hiperparâmetros **não detectados** automaticamente: batch, épocas/iterações, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 2 (p. 1, 5); Latência / frequência 1 (p. 1)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- emprega conjunto de dados: [[SpaceNet7_MUDS|SpaceNet 7 / MUDS]] — 8 ocorrências (p. 2, 3, 4, 5)
- utiliza método: [[SuperResolucao|Super-resolução]] — 26 ocorrências (p. 1, 2, 3, 4, 5)
- é avaliado por: [[IoU|IoU / mIoU]] — 4 ocorrências (p. 4, 5)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 11 ocorrências (p. 1, 4, 5, 6)
- trata a tarefa: [[SITS|Séries temporais de imagens (SITS)]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
