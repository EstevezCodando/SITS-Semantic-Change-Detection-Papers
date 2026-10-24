---
tipo: artigo
id_origem: P39
titulo: "MapFormer: Boosting Change Detection by Using Pre-change Information"
ano: 2023
autores: ["Maximilian Bernhard", "Niklas Strauß", "Matthias Schubert"]
doi: "10.48550/arXiv.2303.17859"
arquivo_fonte: "coleta/P39_Bernhard2023_MapFormer-Boosting-Change-Detection-by-Using-Pre-change-Info.pdf"
markdown_fonte: "output/pdf/P39_Bernhard2023_MapFormer-Boosting-Change-Detection-by-Using-Pre-change-Info/document.md"
paginas: 10
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[Edificacoes|Edificações e urbanização]]"]
sensores: []
conjuntos_dados: ["[[DynamicEarthNet|DynamicEarthNet]]", "[[HRSCD|HRSCD]]", "[[LEVIRCD|LEVIR-CD]]"]
metodos: ["[[Transformer|Transformers]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Bernhard 2023 — MapFormer: Boosting Change Detection by Using Pre-change Information

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Maximilian Bernhard, Niklas Strauß, Matthias Schubert (2023). MapFormer: Boosting Change Detection by Using Pre-change Information. IEEE. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2303.17859
- **Arquivo de origem:** `coleta/P39_Bernhard2023_MapFormer-Boosting-Change-Detection-by-Using-Pre-change-Info.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P39_Bernhard2023_MapFormer-Boosting-Change-Detection-by-Using-Pre-change-Info/document.md` — 10 páginas, 38 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Change detection in remote sensing imagery is essential for a variety of applications such as urban planning, disas- ter management, and climate research. However, existing methods for identifying semantically changed areas over- look the availability of semantic information in the form of existing maps describing features of the earth’s surface. In this paper, we leverage this information for change de- tection in bi-temporal images. We show that the simple integration of the additional information via concatena- tion of latent representations suffices to significantly out- perform state-of-the-art change detection methods. Mo- tivated by this observation, we propose the new task of Conditional Change Detection , where pre-change seman- tic information is used as input next to bi-temporal im- ages. To fully exploit the extra information, we propose MapFormer , a novel architecture based…

- “Mo- tivated by this observation, we propose the new task of Conditional Change Detection , where pre-change seman- tic information is used as input next to bi-temporal im- ages.” (p. 1, seção Abstract)
- “To fully exploit the extra information, we propose MapFormer , a novel architecture based on a multi-modal feature fusion module that allows for feature processing conditioned on the available semantic information.” (p. 1, seção Abstract)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- conjunto de dados **DynamicEarthNet**: 12 ocorrências (p. 1, 2, 5, 6, 7)
- conjunto de dados **HRSCD**: 10 ocorrências (p. 1, 2, 5, 6, 7)
- conjunto de dados **LEVIR-CD**: 2 ocorrências (p. 2, 5)
- conjunto de dados **S2Looking**: 2 ocorrências (p. 2, 5)
- “These K joint representations ( h k ( i,j ) ) k =1 ...K can be interpreted as views, encoding different aspects of the same spatial location.” (p. 4, seção 4.2. Multi-modal Feature Fusion)
- “For MapFormer, the feature space is much less entangled, and the semantic classes of the pixels and the binary change ground truth can be separated from other pixels relatively well.” (p. 7, seção 5.6. Qualitative Results)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 5 ocorrências (p. 1, 5, 7, 8)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal / pares (auto: 35 menções)
**Métodos detectados automaticamente:**
- método/família **Transformer**: 8 ocorrências (p. 2, 5, 6, 7)
**Hiperparâmetros detectados automaticamente (verificar):**
- perda: “cross-entropy loss for the binary change map (as well” (p. 5)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- métrica **IoU**: 20 ocorrências (p. 1, 3, 6, 7)
- métrica **F1**: 4 ocorrências (p. 6, 7)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “MapFormer further pushes the performance on both datasets to 23.5% and 48.0% IoU, respectively.” (p. 6, seção 5.3. Binary Change Detection)
- “Remarkably, when MapFormer is applied without the true map m [(1)], but only predicted segmentation maps ˆ m [(1)] (w/o m [(1)] ), the performance is still highly competitive, even achieving by far the best performance among the bi-temporal methods on DynamicE” (p. 6, seção 5.3. Binary Change Detection)
- “However, we observe a significant performance drop on DynamicEarthNet (5.9% IoU), while the performance only degrades marginally on HRSCD (0.2% IoU).” (p. 6, seção 5.3. Binary Change Detection)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “We can see that SegFormer suffers from many false positive predictions, while the other stateof-the-art methods struggle to detect the changed areas.” (p. 7, seção 5.6. Qualitative Results)
- “A limitation of our approach is the requirement of semantic pre-change information.” (p. 8, seção 6. Conclusion)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/mxbh/mapformer (p. 1)
- URL citada: https://github.com/mxbh/mapformer (p. 1)
- declaração: “The code is available at [https://github.com/mxbh/mapformer.](https://github.com/mxbh/mapformer)” (p. 1)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 2 (p. 4)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- emprega conjunto de dados: [[DynamicEarthNet|DynamicEarthNet]] — 12 ocorrências (p. 1, 2, 5, 6, 7)
- emprega conjunto de dados: [[HRSCD|HRSCD]] — 10 ocorrências (p. 1, 2, 5, 6, 7)
- emprega conjunto de dados: [[LEVIRCD|LEVIR-CD]] — 2 ocorrências (p. 2, 5)
- utiliza método: [[Transformer|Transformers]] — 8 ocorrências (p. 2, 5, 6, 7)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
