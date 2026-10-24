---
tipo: artigo
id_origem: P179
titulo: "Advancing Earth Observation Through Machine Learning: A TorchGeo Tutorial"
ano: 2026
autores: ["Caleb Robinson", "Nils Lehmann", "Adam J. Stewart", "Burak Ekim", "Heng Fang", "Isaac Corley", "Maurício C. R. Cordeiro"]
doi: "10.48550/arXiv.2603.02386"
arquivo_fonte: "coleta/P179_Robinson2026_Advancing-Earth-Observation-Through-Machine-Learning-A-Torch.pdf"
markdown_fonte: "output/pdf/P179_Robinson2026_Advancing-Earth-Observation-Through-Machine-Learning-A-Torch/document.md"
paginas: 5
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: []
sensores: ["[[Sentinel2|Sentinel-2]]"]
conjuntos_dados: []
metodos: []
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]", "[[IndicesEspectrais|Índices espectrais (NDVI etc.)]]", "[[Normalizacao|Normalização e escala radiométrica]]"]
validacao: []
ferramentas: ["[[PyTorch|PyTorch]]"]
tags: [artigo, leitura/automatica]
---

# Robinson 2026 — Advancing Earth Observation Through Machine Learning: A TorchGeo Tutorial

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Caleb Robinson, Nils Lehmann, Adam J. Stewart, Burak Ekim et al. (2026). Advancing Earth Observation Through Machine Learning: A TorchGeo Tutorial. arXiv (Cornell University). Tipo no catálogo: Software.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2603.02386
- **Arquivo de origem:** `coleta/P179_Robinson2026_Advancing-Earth-Observation-Through-Machine-Learning-A-Torch.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P179_Robinson2026_Advancing-Earth-Observation-Through-Machine-Learning-A-Torch/document.md` — 5 páginas, 2 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “TorchGeo is a PyTorch-based domain library that provides datasets, samplers, transforms and pre-trained models with the goal of making it easy to use geospatial data in machine learning pipelines.” (p. 1, seção 6 National Water and Sanitation Agency, Brazil, Federal Dist)
- “In this paper, we introduce a tutorial that demonstrates 1.) the core TorchGeo abstractions through code examples, and 2.) an end-to-end case study on multispectral water segmentation from Sentinel-2 imagery using the Earth Surface Water da” (p. 1, seção 6 National Water and Sanitation Agency, Brazil, Federal Dist)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-2**: 9 ocorrências (p. 1, 2, 3, 4)
- resolução mencionada: 30 m (p. 2)
- “We train the model from scratch for 10 epochs with 130 samples per epoch, using an AdamW optimizer with a learning rate of 0.0001, and achieves an overall accuracy of 0.977 and IoU of 0.824 on the val set.” (p. 4, seção 3 C ASE STUDY : WATER SEGMENTATION ON E ARTH S URFACE W ATER)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 14 ocorrências (p. 1, 2, 3, 4)
- **Índices espectrais**: 8 ocorrências (p. 2, 3)
- **Normalização / escala**: 5 ocorrências (p. 2, 3)
- **Corregistro / georreferenciamento**: 3 ocorrências (p. 1)
- **Mosaicos e compostos**: 3 ocorrências (p. 2)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 0.0001, and achieves an overall accuracy of 0.97” (p. 4)
- épocas/iterações: “10 epochs” (p. 4)
- otimizador: “AdamW optimizer with a learning rate of 0” (p. 4)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 2 ocorrências (p. 1, 4)
- métrica **IoU**: 3 ocorrências (p. 4)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “We train the model from scratch for 10 epochs with 130 samples per epoch, using an AdamW optimizer with a learning rate of 0.0001, and achieves an overall accuracy of 0.977 and IoU of 0.824 on the val set.” (p. 4, seção 3 C ASE STUDY : WATER SEGMENTATION ON E ARTH S URF)

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/Lightning-AI/lightning (p. 5)
- URL citada: https://github.com/Lightning-AI/lightning (p. 5)
- URL citada: https://github.com/pytorch/vision (p. 5)
- hiperparâmetros **não detectados** automaticamente: batch, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Rastreabilidade 1 (p. 1)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 9 ocorrências (p. 1, 2, 3, 4)
- usa ferramenta: [[PyTorch|PyTorch]] — 12 ocorrências (p. 1, 2, 3, 5)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 14 ocorrências (p. 1, 2, 3, 4)
- aplica etapa de preparo: [[IndicesEspectrais|Índices espectrais (NDVI etc.)]] — 8 ocorrências (p. 2, 3)
- aplica etapa de preparo: [[Normalizacao|Normalização e escala radiométrica]] — 5 ocorrências (p. 2, 3)

## Anotações do leitor

- 
