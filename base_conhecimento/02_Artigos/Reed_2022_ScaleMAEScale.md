---
tipo: artigo
id_origem: P79
titulo: "Scale-MAE: A Scale-Aware Masked Autoencoder for Multiscale Geospatial Representation Learning"
ano: 2022
autores: ["Colorado Reed", "Ritwik Gupta", "Shufan Li", "Sarah Brockman", "Christopher Funk", "Brian Clipp", "Kurt Keutzer", "Salvatore Candido"]
doi: "10.48550/arXiv.2212.14532"
arquivo_fonte: "coleta/P79_Reed2023_Scale-MAE-A-Scale-Aware-Masked-Autoencoder-for-Multiscale-Ge.pdf"
markdown_fonte: "output/pdf/P79_Reed2023_Scale-MAE-A-Scale-Aware-Masked-Autoencoder-for-Multiscale-Ge/document.md"
paginas: 16
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[Mineracao|Mineração]]"]
sensores: []
conjuntos_dados: []
metodos: ["[[Transformer|Transformers]]", "[[TransferLearning|Aprendizado por transferência]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Reed 2022 — Scale-MAE: A Scale-Aware Masked Autoencoder for Multiscale Geospatial Representation Learning

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Colorado Reed, Ritwik Gupta, Shufan Li, Sarah Brockman et al. (2022). Scale-MAE: A Scale-Aware Masked Autoencoder for Multiscale Geospatial Representation Learning. IEEE. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2212.14532
- **Arquivo de origem:** `coleta/P79_Reed2023_Scale-MAE-A-Scale-Aware-Masked-Autoencoder-for-Multiscale-Ge.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P79_Reed2023_Scale-MAE-A-Scale-Aware-Masked-Autoencoder-for-Multiscale-Ge/document.md` — 16 páginas, 70 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Large, pretrained models are commonly finetuned with imagery that is heavily augmented to mimic different condi- tions and scales, with the resulting models used for various tasks with imagery from a range of spatial scales. Such models overlook scale-specific information in the data for scale-dependent domains, such as remote sensing. In this paper, we present Scale-MAE , a pretraining method that ex- plicitly learns relationships between data at different, known scales throughout the pretraining process. Scale-MAE pre- trains a network by masking an input image at a known input scale, where the area of the Earth covered by the image deter- mines the scale of the ViT positional encoding, not the image resolution. Scale-MAE encodes the masked image with a standard ViT backbone, and then decodes the masked image through a bandpass filter to reconstruct low/high frequency images at lower/h…

- “In this paper, we present Scale-MAE , a pretraining method that ex- plicitly learns relationships between data at different, known scales throughout the pretraining process.” (p. 1, seção Abstract)
- “In this paper we present Scale-MAE, a masked reconstruction model that explicitly learns relationships between data at different, known scales throughout the pretraining process.” (p. 2, seção 1. Introduction)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **SAR**: 2 ocorrências (p. 8)
- resolução mencionada: 0.3 m (p. 1)
- resolução mencionada: 900 m (p. 1)
- resolução mencionada: 3 m (p. 2)
- “We train on 224x224 images and evaluate 256x256 images because we found evaluating at a higher scale improves the performance of all models.” (p. 7, seção 4.1. Representation Quality)
- “(Columns 2-4) The following columns show a ground truth building segmentation, Scale-MAE segmentation from a finetuned UperNet, and segmentation from an analogously finetuned UperNet from a vanilla MAE, respectively.” (p. 1, seção 1. Introduction)
- “Nevertheless, the remote sensing vision community has increasingly used large, pretrained models , where such applications finetune a pretrained model for a single source of Input Image Ground Truth Scale-MAE Vanilla MAE” (p. 1, seção 1. Introduction)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 21 ocorrências (p. 2, 3, 4, 5, 6)
- **Rotulagem / anotação**: 6 ocorrências (p. 1, 2, 4, 6)
- **Aumento de dados**: 3 ocorrências (p. 2, 4, 7)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **Transformer**: 37 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Transfer learning**: 14 ocorrências (p. 1, 2, 6, 7)
- método/família **Super-resolução**: 7 ocorrências (p. 3, 4)
- método/família **Semi/auto-supervisionado**: 5 ocorrências (p. 2, 3)
- método/família **CNN**: 4 ocorrências (p. 3, 9)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 5 × 10 [−] , a weight decay of 5 × 10 [−] ” (p. 7)
- batch: “batch size of 256 across 2 GPUs” (p. 7)
- épocas/iterações: “800 epochs” (p. 5)
- tamanho do patch: “100x100 pixel” (p. 1)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 5 ocorrências (p. 6)
- métrica **IoU**: 11 ocorrências (p. 1, 2, 7, 8)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “Compared to the next-best-performing method at the input GSD, Scale-MAE is 0.9 mIoU higher, at 75% GSD Scale-MAE is 1.2 mIoU higher, and at 50% Scale-MAE is 1.7 mIoU higher.” (p. 7, seção 4.1. Representation Quality)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “Existing MAE-based pretraining approaches fail to generalize across domains with images at multiple scales.” (p. 2, seção 1. Introduction)
- “MAEs fail to leverage scale information in scale-dependent domains as they are often reliant on absolute or relative positional encodings.” (p. 2, seção 2. Related Work)
- “Since we cannot synthesize data at a finer GSD than the provided ground truth, we only downsample the full resolution validation set to coarser GSDs at fixed percentages: X val [G] [%] [, G][ ∈{] [.] [,] [ 25] [,] [ 50] [,] [ 100] [}] [.] O” (p. 6, seção 4.1. Representation Quality)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado
- hiperparâmetros **não detectados** automaticamente: otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Sistema operacional 1 (p. 1)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza método: [[Transformer|Transformers]] — 37 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 14 ocorrências (p. 1, 2, 6, 7)
- trata a tarefa: [[Mineracao|Mineração]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
