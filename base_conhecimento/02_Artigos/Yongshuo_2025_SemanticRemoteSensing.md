---
tipo: artigo
id_origem: P30
titulo: "Semantic-CD: Remote Sensing Image Semantic Change Detection towards Open-vocabulary Setting"
ano: 2025
autores: ["Zhu, Yongshuo", "Li, Lu", "Keyan Chen", "Liu, Chenyang", "Zhou, Fugen", "Shi, Zhenwei"]
doi: "10.48550/arXiv.2501.06808"
arquivo_fonte: "coleta/P30_Yongshuo2025_Semantic-CD-Remote-Sensing-Image-Semantic-Change-Detection-t.pdf"
markdown_fonte: "output/pdf/P30_Yongshuo2025_Semantic-CD-Remote-Sensing-Image-Semantic-Change-Detection-t/document.md"
paginas: 5
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[MudancaSemantica|Mudança semântica (from–to)]]"]
sensores: []
conjuntos_dados: ["[[SECOND|SECOND]]", "[[HRSCD|HRSCD]]"]
metodos: ["[[ModeloFundacional|Modelos fundacionais]]", "[[RedeSiamesa|Redes siamesas]]", "[[Transformer|Transformers]]"]
preparo: []
validacao: ["[[Generalizacao|Generalização e domain shift]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Yongshuo 2025 — Semantic-CD: Remote Sensing Image Semantic Change Detection towards Open-vocabulary Setting

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Zhu, Yongshuo, Li, Lu, Keyan Chen, Liu, Chenyang et al. (2025). Semantic-CD: Remote Sensing Image Semantic Change Detection towards Open-vocabulary Setting. arXiv (Cornell University). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2501.06808
- **Arquivo de origem:** `coleta/P30_Yongshuo2025_Semantic-CD-Remote-Sensing-Image-Semantic-Change-Detection-t.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P30_Yongshuo2025_Semantic-CD-Remote-Sensing-Image-Semantic-Change-Detection-t/document.md` — 5 páginas, 44 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “To address this issue, we introduce a novel approach called Semantic-CD, specifically designed for semantic change detection in remote sensing images.” (p. 1, seção Início)
- “We propose Semantic-CD, a method that decouples change detection into BCD and SCD tasks.” (p. 1, seção I. I NTRODUCTION)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- conjunto de dados **SECOND**: 5 ocorrências (p. 1, 3, 4)
- conjunto de dados **HRSCD**: 2 ocorrências (p. 3, 4)
- “The BCD task utilizes the general visual semantic understanding capabilities of the vision-language foundation model CLIP for binary segmentation, while the SCD task leverages CLIP’s open vocabulary capabilities to interpret semantic change” (p. 1, seção I. I NTRODUCTION)
- “The symbols ˆ y i and y i denote the predicted and ground truth values of a single pixel, respectively.” (p. 3, seção II. M ETHODOLOGY)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

Não informado (nada detectado automaticamente).

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal / pares (auto: 17 menções)
**Métodos detectados automaticamente:**
- método/família **Modelo fundacional**: 9 ocorrências (p. 1, 2, 4, 5)
- método/família **Rede siamesa**: 6 ocorrências (p. 4, 5)
- método/família **Transformer**: 5 ocorrências (p. 3, 5)
**Hiperparâmetros detectados automaticamente (verificar):**
- batch: “batch size of 1 and trained for 300 epochs” (p. 3)
- épocas/iterações: “300 epochs” (p. 3)
- perda: “cross-entropy loss for supervised training, as detail” (p. 3)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Teste externo / generalização**: 4 ocorrências (p. 1, 4, 5)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 4)
- declaração: “In the future, we hope the release of more open-source datasets featuring diverse and granular categories in semantic change detection.” (p. 4)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, otimizador (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 8 (p. 1, 2, 3)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- emprega conjunto de dados: [[SECOND|SECOND]] — 5 ocorrências (p. 1, 3, 4)
- emprega conjunto de dados: [[HRSCD|HRSCD]] — 2 ocorrências (p. 3, 4)
- utiliza método: [[ModeloFundacional|Modelos fundacionais]] — 9 ocorrências (p. 1, 2, 4, 5)
- utiliza método: [[RedeSiamesa|Redes siamesas]] — 6 ocorrências (p. 4, 5)
- utiliza método: [[Transformer|Transformers]] — 5 ocorrências (p. 3, 5)
- adota desenho de validação: [[Generalizacao|Generalização e domain shift]] — 4 ocorrências (p. 1, 4, 5)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[MudancaSemantica|Mudança semântica (from–to)]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
