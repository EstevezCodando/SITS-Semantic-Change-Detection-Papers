---
tipo: artigo
id_origem: P76
titulo: "Efficient Self-Supervised Learning for Earth Observation via Dynamic Dataset Curation"
ano: 2025
autores: ["Thomas Kerdreux", "Alexandre Tuel", "Quentin Febvre", "Alexis Aurelien Mouche", "Bertrand Chapron"]
doi: "10.48550/arXiv.2504.06962"
arquivo_fonte: "coleta/P76_Kerdreux2025_Efficient-Self-Supervised-Learning-for-Earth-Observation-via.pdf"
markdown_fonte: "output/pdf/P76_Kerdreux2025_Efficient-Self-Supervised-Learning-for-Earth-Observation-via/document.md"
paginas: 11
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: []
sensores: ["[[SAR|Radar (SAR)]]", "[[Sentinel1|Sentinel-1]]"]
conjuntos_dados: []
metodos: ["[[Transformer|Transformers]]", "[[ModeloFundacional|Modelos fundacionais]]", "[[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Kerdreux 2025 — Efficient Self-Supervised Learning for Earth Observation via Dynamic Dataset Curation

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Thomas Kerdreux, Alexandre Tuel, Quentin Febvre, Alexis Aurelien Mouche et al. (2025). Efficient Self-Supervised Learning for Earth Observation via Dynamic Dataset Curation. IEEE. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2504.06962
- **Arquivo de origem:** `coleta/P76_Kerdreux2025_Efficient-Self-Supervised-Learning-for-Earth-Observation-via.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P76_Kerdreux2025_Efficient-Self-Supervised-Learning-for-Earth-Observation-via/document.md` — 11 páginas, 3 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Self-supervised learning (SSL) has enabled the development of vision foundation models for Earth Observation (EO), demonstrating strong transferability across diverse remote sensing tasks. While much research has focused on network architectures and training strategies, the role of dataset curation – particularly in balancing and diversifying pre- training datasets – remains underexplored. In EO, this chal- lenge is exacerbated by the strong redundancy and heavy- tailed distributions of satellite imagery, which can lead to biased representations and inefficient training. In this work, we introduce a dynamic dataset pruning strat- egy designed to enhance SSL pre-training efficiency by max- imizing dataset diversity and balancedness. Our method iteratively refines the training set without relying on a pre- existing feature extractor, making it well-suited for domains where curated datasets…

- “In this work, we introduce a dynamic dataset pruning strat- egy designed to enhance SSL pre-training efficiency by max- imizing dataset diversity and balancedness.” (p. 1, seção Abstract)
- “Furthermore, there is no guarantee that the resulting datasets are truly balanced, since the selection criteria, like land cover, are always reductive (diversity in land imagery is not only driven by differences in land cover, but also by s” (p. 2, seção 1. Introduction)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The ESA Sentinel-1 mission is a constellation of two polar-orbiting, sun-synchronous satellites (S-1 A and S-1 B) launched in April of 2014 and 2016, respectively.” (p. 3, seção 3.1. Sentinel-1 WV data)
- “The WV data archive we used includes about 12 million different images, covering the full 2015-2024 period (each satellite produces approximately 60,000 WV images per month).” (p. 3, seção 3.1. Sentinel-1 WV data)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **SAR**: 21 ocorrências (p. 1, 2, 3, 4, 5)
- sensor/produto **Sentinel-1**: 17 ocorrências (p. 1, 2, 3, 5, 6)
- sensor/produto **Sentinel-2**: 2 ocorrências (p. 1, 2)
- resolução mencionada: 5 m (p. 3)
- “A similar approach was taken in the Prithvi model , whereby individual Harmonized Landsat/Sentinel-2 images were selected based on average climatology and land cover 1” (p. 1, seção 1. Introduction)
- “We used a random subset of 50,000 images among those selected by O’Driscoll et al. and labeled with wind speed using ERA5 reanalysis data as ground truth.” (p. 5, seção 3.5.3. Wind speed dataset)
- “The TenGeoP dataset consists of 37,553 WV images that were manually annotated by human SAR experts into ten categories.” (p. 5, seção 3.5.1. TenGeoP dataset)
- “We used a random subset of 50,000 images among those selected by O’Driscoll et al. and labeled with wind speed using ERA5 reanalysis data as ground truth.” (p. 5, seção 3.5.3. Wind speed dataset)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 5 ocorrências (p. 5, 7)
- **Recorte em patches/tiles**: 4 ocorrências (p. 3, 7, 8)
- **Textura (GLCM)**: 3 ocorrências (p. 5, 6, 8)
- **Reamostragem**: 2 ocorrências (p. 4, 8)
- **Aumento de dados**: 2 ocorrências (p. 2, 3)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **Transformer**: 32 ocorrências (p. 4, 5, 6, 7, 8)
- método/família **Modelo fundacional**: 19 ocorrências (p. 1, 2, 4, 5, 6)
- método/família **Semi/auto-supervisionado**: 17 ocorrências (p. 2, 3, 4, 6, 7)
- método/família **Transfer learning**: 12 ocorrências (p. 7, 8)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate” (p. 5)
- batch: “batch size of 256, an AdamW optimizer, a cosine sc” (p. 5)
- épocas/iterações: “380 epochs” (p. 5)
- otimizador: “AdamW optimizer, a cosine scheduler with anne” (p. 5)
- perda: “focal loss or self-paced reweighting ” (p. 2)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Teste externo / generalização**: 5 ocorrências (p. 1, 2, 7)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “For instance, the best TenGeoP classification accuracy for a ViT-S/16 is 76% when no pruning is applied during training, and it is reached after about 145 epochs.” (p. 6, seção 3.6.1. Impact of dataset pruning)
- “By contrast, the same accuracy is reached as early as after 85 epochs under the 75% pruning scenario, a more than 40% gain in computational resources.” (p. 6, seção 3.6.1. Impact of dataset pruning)
- “Similarly, the RMSE for wave height and wind speed decreases by 0.050.2 for existing models and by 0.1-0.3 for our models.” (p. 7, seção 3.6.2. Comparison to other SAR foundation models)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “However, such approaches have important drawbacks.” (p. 2, seção 1. Introduction)
- “However, the proposed approach still requires an existing feature extractor and cannot therefore be considered fully unsupervised.” (p. 2, seção 2. Related Work)
- “Future work could investigate the relative impact of sensor versus domain shift in driving this perfor mance gap.” (p. 7, seção 3.6.2. Comparison to other SAR foundation models)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/galeio-research/OceanSAR-models/ (p. 1)
- URL citada: https://github.com/galeio-research/OceanSAR-models/ (p. 1)
- URL citada: https://huggingface.co/galeio-research/OceanSAR- (p. 8)
- URL citada: https://huggingface.co/galeio-research/OceanSAR-1 (p. 8)

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 3 (p. 5, 7)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[SAR|Radar (SAR)]] — 21 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza dado/sensor: [[Sentinel1|Sentinel-1]] — 17 ocorrências (p. 1, 2, 3, 5, 6)
- utiliza método: [[Transformer|Transformers]] — 32 ocorrências (p. 4, 5, 6, 7, 8)
- utiliza método: [[ModeloFundacional|Modelos fundacionais]] — 19 ocorrências (p. 1, 2, 4, 5, 6)
- utiliza método: [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 17 ocorrências (p. 2, 3, 4, 6, 7)

## Anotações do leitor

- 
