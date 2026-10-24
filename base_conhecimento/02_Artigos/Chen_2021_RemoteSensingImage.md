---
tipo: artigo
id_origem: P25
titulo: "Remote Sensing Image Change Detection With Transformers"
ano: 2021
autores: ["Hao Chen", "Zipeng Qi", "Zhenwei Shi"]
doi: "10.1109/TGRS.2021.3095166"
arquivo_fonte: "coleta/P25_Chen2021_Remote-Sensing-Image-Change-Detection-With-Transformers.pdf"
markdown_fonte: "output/pdf/P25_Chen2021_Remote-Sensing-Image-Change-Detection-With-Transformers/document.md"
paginas: 14
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]"]
sensores: ["[[ImagensAereas|Imagens aéreas]]"]
conjuntos_dados: ["[[LEVIRCD|LEVIR-CD]]", "[[WHUCD|WHU-CD]]"]
metodos: ["[[Transformer|Transformers]]", "[[CNN|Redes convolucionais (CNN)]]", "[[RedeSiamesa|Redes siamesas]]", "[[UNet|U-Net]]"]
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]", "[[Normalizacao|Normalização e escala radiométrica]]"]
validacao: ["[[DivisaoTreinoTeste|Divisão treino/validação/teste]]", "[[F1|F1]]", "[[IoU|IoU / mIoU]]", "[[PrecisaoRecall|Precisão e recall]]", "[[AcuraciaGlobal|Acurácia global (OA)]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Chen 2021 — Remote Sensing Image Change Detection With Transformers

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Hao Chen, Zipeng Qi, Zhenwei Shi (2021). Remote Sensing Image Change Detection With Transformers. IEEE Transactions on Geoscience and Remote Sensing. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1109/TGRS.2021.3095166
- **Arquivo de origem:** `coleta/P25_Chen2021_Remote-Sensing-Image-Change-Detection-With-Transformers.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P25_Chen2021_Remote-Sensing-Image-Change-Detection-With-Transformers/document.md` — 14 páginas, 118 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “Here, we propose a bitemporal image transformer (BIT) to efficiently and effectively model contexts within the spatial-temporal domain.” (p. 1, seção Início)
- “The goal of CD is to assign binary labels (i.e., change or no change) to every pixel in a region by comparing co-registered images of the same region taken at different times .” (p. 1, seção I. I NTRODUCTION)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Imagens aéreas**: 4 ocorrências (p. 6, 13)
- conjunto de dados **LEVIR-CD**: 21 ocorrências (p. 6, 7, 8, 9, 10)
- conjunto de dados **WHU-CD**: 18 ocorrências (p. 6, 7, 8, 9, 10)
- resolução mencionada: 0.5 m (p. 6)
- resolução mencionada: 0.075 m (p. 6)
- resolução mencionada: 2 m (p. 6)
- “We have 3600/340/48 samples for training/validation/test respectively.” (p. 6, seção IV. E XPERIMENTAL R ESULTS AND A NALYSIS)
- “Information extraction based on RS images still mainly relies on manual visual interpretation.” (p. 1, seção I. I NTRODUCTION)
- “8 (a) (b) Image 1 Image 2 Ground Truth FC-EF FC-Siam-Conc FC-Siam-Di DTCDSCN STANet IFNet SNUNet Base BIT (d) LEVIR-CD (e) (f) (g) (h) WHU-CD (i) (j) (k) (l) DSIFN-CD Fig.” (p. 8, seção II reports the number of parameters (Params.), floating-poin)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 12 ocorrências (p. 3, 4, 6, 13, 14)
- **Normalização / escala**: 5 ocorrências (p. 5, 6, 12, 14)
- **Aumento de dados**: 2 ocorrências (p. 6, 13)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal e série (auto: 45 pares; 7 série)
**Métodos detectados automaticamente:**
- método/família **Transformer**: 83 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **CNN**: 35 ocorrências (p. 1, 2, 3, 4, 6)
- método/família **Rede siamesa**: 21 ocorrências (p. 2, 4, 5, 7, 12)
- método/família **U-Net**: 5 ocorrências (p. 1, 2, 7, 12, 14)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate is initially set to 0.01 and linearly decay to 0 u” (p. 6)
- épocas/iterações: “200 epochs” (p. 6)
- otimizador: “SGD) with momentum to optimize the model” (p. 6)
- perda: “crossentropy loss to optimize the network parameters” (p. 6)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 17 ocorrências (p. 6, 7, 8, 9, 11)
- métrica **F1**: 33 ocorrências (p. 7, 9, 10, 11, 12)
- métrica **IoU**: 17 ocorrências (p. 7, 9, 10, 11)
- métrica **Precisão/Recall**: 10 ocorrências (p. 7, 11, 12)
- métrica **Acurácia global**: 6 ocorrências (p. 7, 9)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/justchenhao/BIT (p. 1)
- URL citada: https://github.com/justchenhao/BIT (p. 1)
- declaração: “Our code is available at https://github.com/justchenhao/BIT CD.” (p. 1)
- hiperparâmetros **não detectados** automaticamente: batch (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 4 (p. 1, 2, 9); Falsos alertas 1 (p. 12); Revisão humana 1 (p. 1)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[ImagensAereas|Imagens aéreas]] — 4 ocorrências (p. 6, 13)
- emprega conjunto de dados: [[LEVIRCD|LEVIR-CD]] — 21 ocorrências (p. 6, 7, 8, 9, 10)
- emprega conjunto de dados: [[WHUCD|WHU-CD]] — 18 ocorrências (p. 6, 7, 8, 9, 10)
- utiliza método: [[Transformer|Transformers]] — 83 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 35 ocorrências (p. 1, 2, 3, 4, 6)
- utiliza método: [[RedeSiamesa|Redes siamesas]] — 21 ocorrências (p. 2, 4, 5, 7, 12)
- utiliza método: [[UNet|U-Net]] — 5 ocorrências (p. 1, 2, 7, 12, 14)
- é avaliado por: [[F1|F1]] — 33 ocorrências (p. 7, 9, 10, 11, 12)
- é avaliado por: [[IoU|IoU / mIoU]] — 17 ocorrências (p. 7, 9, 10, 11)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 10 ocorrências (p. 7, 11, 12)
- é avaliado por: [[AcuraciaGlobal|Acurácia global (OA)]] — 6 ocorrências (p. 7, 9)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 12 ocorrências (p. 3, 4, 6, 13, 14)
- aplica etapa de preparo: [[Normalizacao|Normalização e escala radiométrica]] — 5 ocorrências (p. 5, 6, 12, 14)
- adota desenho de validação: [[DivisaoTreinoTeste|Divisão treino/validação/teste]] — 17 ocorrências (p. 6, 7, 8, 9, 11)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
