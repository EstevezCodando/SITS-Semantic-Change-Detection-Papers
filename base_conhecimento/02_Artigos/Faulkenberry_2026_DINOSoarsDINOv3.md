---
tipo: artigo
id_origem: P65
titulo: "DINO Soars: DINOv3 for Open-Vocabulary Semantic Segmentation of Remote Sensing Imagery"
ano: 2026
autores: ["Ryan Faulkenberry", "Saurabh Prasad"]
doi: "10.48550/arXiv.2605.03175"
arquivo_fonte: "coleta/P65_Faulkenberry2026_DINO-Soars-DINOv3-for-Open-Vocabulary-Semantic-Segmentation-.pdf"
markdown_fonte: "output/pdf/P65_Faulkenberry2026_DINO-Soars-DINOv3-for-Open-Vocabulary-Semantic-Segmentation-/document.md"
paginas: 15
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[SegmentacaoSemantica|Segmentação semântica]]"]
sensores: []
conjuntos_dados: []
metodos: ["[[ModeloFundacional|Modelos fundacionais]]", "[[TransferLearning|Aprendizado por transferência]]", "[[Transformer|Transformers]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Faulkenberry 2026 — DINO Soars: DINOv3 for Open-Vocabulary Semantic Segmentation of Remote Sensing Imagery

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Ryan Faulkenberry, Saurabh Prasad (2026). DINO Soars: DINOv3 for Open-Vocabulary Semantic Segmentation of Remote Sensing Imagery. arXiv (Cornell University). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2605.03175
- **Arquivo de origem:** `coleta/P65_Faulkenberry2026_DINO-Soars-DINOv3-for-Open-Vocabulary-Semantic-Segmentation-.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P65_Faulkenberry2026_DINO-Soars-DINOv3-for-Open-Vocabulary-Semantic-Segmentation-/document.md` — 15 páginas, 100 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** The remote sensing (RS) domain suffers from a lack of densely labeled datasets, which are costly to obtain. Thus, models that can segment RS imagery well without super- vised fine-tuning are valuable, but existing solutions fall behind supervised methods. Recently, DINOv3 sur- passed SOTA RS foundation models on the GEO-bench segmentation benchmark without pre-training on RS data. Additionally, DINO.txt has enabled open vocabu- lary semantic segmentation (OVSS) with the DINOv3 back- bone. We leverage these developments to form an OVSS model for RS imagery, free of RS-domain fine-tuning. Our model, CAFe-DINO (Cost Aggregation + Feature Upsam- pling with DINO) exploits the strong OVSS performance of DINOv3 for RS imagery via cost aggregation and training- free upsampling of text-image similarity scores. The ro- bust latent of the DINOv3 backbone eliminates the need for fine-tuning on RS im…

- “We introduce CAFe-DINO, a cost-aggregation and feature upsampling model for the DINOv3 backbone that does not require RS fine-tuning.” (p. 2, seção 1. Introduction)
- “Remote-Sensing-Targeted Natural Image Training We train CAFe-DINO on natural imagery with the goal of introducing as many relevant semantic classes as possible, noting that a key drawback of existing RS datasets is a lack of dense labeling ” (p. 5, seção 4. Experiments)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- “(a) DINOv3.txt (b) DINOv3.txt + CA + AnyUp (Ours) (c) Ground Truth Figure 2.” (p. 2, seção 1. Introduction)
- “DINOv3.txt OVRS GSNet SegEarth-OV CAFe-DINO (Ours) Ground Truth Figure 4.” (p. 5, seção 3.3. Class-Wise Upsampling)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 9 ocorrências (p. 3, 4, 7)
- **Rotulagem / anotação**: 5 ocorrências (p. 1, 3, 5, 7)
- **Textura (GLCM)**: 4 ocorrências (p. 5, 7, 8)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **Modelo fundacional**: 61 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Transfer learning**: 25 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **Transformer**: 11 ocorrências (p. 3, 4, 6)
- método/família **Semi/auto-supervisionado**: 3 ocorrências (p. 3, 7)
**Hiperparâmetros detectados automaticamente (verificar):**
- batch: “batch size of 4 for 45,000 iterations” (p. 6)
- épocas/iterações: “45,000 iterations” (p. 6)
- tamanho do patch: “512 × 512 and perform sliding window” (p. 6)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- métrica **IoU**: 8 ocorrências (p. 6, 7, 8)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “Despite its pedigree on natural imagery, DINOv3.txt struggles with OVSS on RS imagery, as we show in Fig.” (p. 2, seção 1. Introduction)
- “Despite these advances, most OVSS methods still struggle with fine-grained localization and domain shift, particularly when deployed outside natural image distributions such as RS.” (p. 3, seção 2.1. Open Vocabulary Semantic Segmentation)
- “Collectively, these methods demonstrate the promise of OVSS in RS, but are limited by the need to train with RS imagery.” (p. 3, seção 2.2. OVSS for Remote Sensing)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/rfaulk/DINOSoars (p. 1)
- URL citada: https://github.com/rfaulk/DINOSoars (p. 1)
- declaração: “Our code and data are publicly available at https://github.com/rfaulk/DINOSoars.” (p. 1)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 56 (p. 1, 2, 3, 4, 5)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza método: [[ModeloFundacional|Modelos fundacionais]] — 61 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 25 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza método: [[Transformer|Transformers]] — 11 ocorrências (p. 3, 4, 6)
- trata a tarefa: [[SegmentacaoSemantica|Segmentação semântica]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
