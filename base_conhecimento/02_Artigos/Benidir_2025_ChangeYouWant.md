---
tipo: artigo
id_origem: P139
titulo: "The Change You Want To Detect: Semantic Change Detection In Earth Observation With Hybrid Data Generation"
ano: 2025
autores: ["Yanis Benidir", "Nicolas Gonthier", "Clément Mallet"]
doi: "10.1109/cvpr52734.2025.00211"
arquivo_fonte: "coleta/P139_Benidir2025_The-Change-You-Want-To-Detect-Semantic-Change-Detection-In-E.pdf"
markdown_fonte: "output/pdf/P139_Benidir2025_The-Change-You-Want-To-Detect-Semantic-Change-Detection-In-E/document.md"
paginas: 20
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[MudancaSemantica|Mudança semântica (from–to)]]", "[[ClassificacaoCobertura|Classificação de cobertura e uso da terra]]"]
sensores: []
conjuntos_dados: ["[[S2Looking|S2Looking]]", "[[SECOND|SECOND]]"]
metodos: ["[[TransferLearning|Aprendizado por transferência]]", "[[UNet|U-Net]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]", "[[PatchesTiles|Recorte em patches/tiles]]"]
validacao: ["[[Generalizacao|Generalização e domain shift]]", "[[IoU|IoU / mIoU]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Benidir 2025 — The Change You Want To Detect: Semantic Change Detection In Earth Observation With Hybrid Data Generation

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Yanis Benidir, Nicolas Gonthier, Clément Mallet (2025). The Change You Want To Detect: Semantic Change Detection In Earth Observation With Hybrid Data Generation. IEEE Computer Society Conference on Computer Vision and Pattern Recognition. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1109/cvpr52734.2025.00211
- **Arquivo de origem:** `coleta/P139_Benidir2025_The-Change-You-Want-To-Detect-Semantic-Change-Detection-In-E.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P139_Benidir2025_The-Change-You-Want-To-Detect-Semantic-Change-Detection-In-E/document.md` — 20 páginas, 116 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Bi-temporal change detection at scale based on Very High Resolution (VHR) images is crucial for Earth monitoring. This remains poorly addressed so far: methods either re- quire large volumes of annotated data (semantic case), or are limited to restricted datasets (binary set-ups). Most ap- proaches do not exhibit the versatility required for temporal and spatial adaptation: simplicity in architecture design and pretraining on realistic and comprehensive datasets. Synthetic datasets are the key solution but still fail to han- dle complex and diverse scenes. In this paper, we present HySCDG a generative pipeline for creating a large hybrid semantic change detection dataset that contains both real VHR images and inpainted ones, along with land cover se- mantic map at both dates and the change map. Being seman- tically and spatially guided, HySCDG generates realistic im- ages, leading to a c…

- “In this paper, we present HySCDG a generative pipeline for creating a large hybrid semantic change detection dataset that contains both real VHR images and inpainted ones, along with land cover se- mantic map at both dates and the change ma” (p. 1, seção Abstract)
- “We evaluate FSC-180k on five change de- tection cases (binary and semantic), from zero-shot to mixed and sequential training, and also under low data regime training.” (p. 1, seção Abstract)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- conjunto de dados **S2Looking**: 5 ocorrências (p. 5, 6, 7, 8)
- conjunto de dados **SECOND**: 2 ocorrências (p. 6, 7)
- resolução mencionada: 0.2 m (p. 5)
- “We keep the training strategy simple and constant to focus on data and transfer, this enhances interpretability.” (p. 6, seção 4.2.2. Model architecture)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 7 ocorrências (p. 1, 2, 3, 4)
- **Recorte em patches/tiles**: 5 ocorrências (p. 1, 2, 3, 6)
- **Textura (GLCM)**: 2 ocorrências (p. 3, 4)
- **Aumento de dados**: 2 ocorrências (p. 2, 6)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal / pares (auto: 17 menções)
**Métodos detectados automaticamente:**
- método/família **Transfer learning**: 28 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **U-Net**: 16 ocorrências (p. 3, 5, 6, 7)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 3e-4 with exponential decay (0.99 per epoch)” (p. 6)
- batch: “batch size of 32)” (p. 3)
- épocas/iterações: “30,000 iterations” (p. 3)
- perda: “Focal losses [ 31 ]: minimizing high-frequency err” (p. 3)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Teste externo / generalização**: 4 ocorrências (p. 2, 8)
- **Conjuntos treino/val/teste**: 2 ocorrências (p. 8)
- métrica **IoU**: 14 ocorrências (p. 5, 6, 7, 8)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “We evaluated how unchanged the semantic map remains by performing 15-class semantic segmentation on real and generated images, thanks to a UNet trained for this task, leading to a satisfactory error rate below 20% between both outputs.” (p. 5, seção 3.4. Structure of the FSC-180k dataset)
- “Experiments show that even for binary tasks, the Dual UNet outperforms the binary-only model, e.g., achieving an IoU of 0.83 on Levir-CD (compared to 0.80).” (p. 6, seção 4.2.2. Model architecture)
- “For HiUCDmini, our pretraining results in a SeK of 0.19 and a SCS of 0.78, representing respective increases of 11% and 7% 6” (p. 6, seção 4.3.1. Sequential training)
- “For SECOND, SyntheWorld partially narrows the gap: SeK of 0.17 and a SCS of 0.84, while the FSC-180k’s pretrained Dual UNet achieves 0.18 and 0.87.” (p. 7, seção 4.3.1. Sequential training)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “They are often limited by their size [ 6, 25, 39, 56, 63 ], geographical extent [ 6, 56, 57, 63 ], low geometrical or annotation quality [ 11 ].” (p. 2, seção 2. Related work)
- “ControlNet is the most error-prone module: it may sometimes fail to respect the semantic map.” (p. 5, seção 3.4. Structure of the FSC-180k dataset)
- “Indeed, pretraining on SyntheWorld, that focuses solely on the “ building ” class, shows limitations in multiclass tasks on HiUCD-mini and HiUCD-XL compared to the baseline.” (p. 6, seção 4.3.1. Sequential training)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: huggingface.co/stabilityai/stable-diffusion-2-inpainting (p. 3)
- URL citada: https://huggingface.co/stabilityai/stable-diffusion-2-inpainting (p. 3)
- declaração: “All codes, models, and data are available [here: https://yb23.github.io/projects/cywd/.](https://yb23.github.io/projects/cywd/)” (p. 1)
- declaração: “The primary objective of pretraining is to develop a model that can either swiftly adapt to new target datasets or perform well when only limited training data is available .” (p. 7)
- hiperparâmetros **não detectados** automaticamente: otimizador (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Sistema operacional 1 (p. 3); Custo 1 (p. 1)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- emprega conjunto de dados: [[S2Looking|S2Looking]] — 5 ocorrências (p. 5, 6, 7, 8)
- emprega conjunto de dados: [[SECOND|SECOND]] — 2 ocorrências (p. 6, 7)
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 28 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[UNet|U-Net]] — 16 ocorrências (p. 3, 5, 6, 7)
- é avaliado por: [[IoU|IoU / mIoU]] — 14 ocorrências (p. 5, 6, 7, 8)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 7 ocorrências (p. 1, 2, 3, 4)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 5 ocorrências (p. 1, 2, 3, 6)
- adota desenho de validação: [[Generalizacao|Generalização e domain shift]] — 4 ocorrências (p. 2, 8)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[MudancaSemantica|Mudança semântica (from–to)]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[ClassificacaoCobertura|Classificação de cobertura e uso da terra]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
