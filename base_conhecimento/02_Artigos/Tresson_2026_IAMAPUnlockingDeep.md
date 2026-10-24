---
tipo: artigo
id_origem: P157
titulo: "IAMAP: Unlocking Deep Learning in QGIS for non-coders and limited computing resources"
ano: 2026
autores: ["Paul Tresson", "Pierre Le Coz", "Hadrien Tulet", "Anthony Malkassian", "Maxime Réjou‐Méchain"]
doi: "10.21105/joss.10329"
arquivo_fonte: "coleta/P157_Tresson2026_IAMAP-Unlocking-Deep-Learning-in-QGIS-for-non-coders-and-lim.pdf"
markdown_fonte: "output/pdf/P157_Tresson2026_IAMAP-Unlocking-Deep-Learning-in-QGIS-for-non-coders-and-lim/document.md"
paginas: 5
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
tarefas: []
sensores: []
conjuntos_dados: []
metodos: ["[[ModeloFundacional|Modelos fundacionais]]"]
preparo: []
validacao: []
ferramentas: ["[[QGIS|QGIS]]"]
tags: [artigo, leitura/profunda]
---

# Tresson 2026 — IAMAP: Unlocking Deep Learning in QGIS for non-coders and limited computing resources

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Paul Tresson, Pierre Le Coz, Hadrien Tulet, Anthony Malkassian et al. (2026). IAMAP: Unlocking Deep Learning in QGIS for non-coders and limited computing resources. The Journal of Open Source Software. Tipo no catálogo: Software.
- **DOI/URL:** https://doi.org/10.21105/joss.10329
- **Arquivo de origem:** `coleta/P157_Tresson2026_IAMAP-Unlocking-Deep-Learning-in-QGIS-for-non-coders-and-lim.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P157_Tresson2026_IAMAP-Unlocking-Deep-Learning-in-QGIS-for-non-coders-and-lim/document.md` — 5 páginas, 7 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Plugin do QGIS para **usar modelos fundacionais autossupervisionados sem GPU e sem grandes conjuntos de rótulos**: extrair características de um raster, reduzir dimensão, agrupar, medir similaridade com pixels-modelo e treinar classificadores supervisionados leves sobre essas características. Artigo JOSS (Tresson et al., publicado em 25/jun/2026).

- “Pierre, La Réunion, France - Corresponding author ## Summary We introduce IAMAP, a user-friendly plugin for the geographic information system QGIS that allows users to (1) tile raster images and feed them into pre-trained deep learning mode” (p. 1, seção Início)

## 3. Área de estudo e período analisado

Ver seção 4 (dados), que traz área e período quando informados pelo artigo.

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- “By enabling non-AI specialists to leverage the high-quality features provided by foundation models without requiring GPU capacity or extensive reference datasets, IAMAP contributes to the democratization of these [computationally efficient ” (p. 1, seção Início)
- “In most ecological and environmental science studies, constructing such a large reference dataset, through e.g., ground observations or photointerpretation, remains a major barrier to the implementation of deep learning approaches.” (p. 1, seção Início)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 4 ocorrências (p. 1)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Os cinco módulos (p. 2–p. 3):**

1. **Extração de características:** raster em tiles passa por um backbone ViT (via Timm/Hugging Face ou pesos locais) usando um fork leve do **TorchGeo**; saída em **GeoTIFF**.
2. **Redução de dimensão:** qualquer algoritmo do `sklearn.decomposition`/`cluster` com `fit`/`transform`; parâmetros em JSON.
3. **Agrupamento:** algoritmos do `sklearn.cluster` com `fit`/`predict`.
4. **Similaridade:** mapa de similaridade entre o raster e **pixels-modelo** dados por uma camada vetorial.
5. **Aprendizado supervisionado:** modelos de `sklearn.ensemble` e `neighbors`, com validação e dados rotulados definidos pelo usuário.

**Evidência (leitura) — Princípios de projeto:**

- Restrição central: usuário **sem programar, sem GPU e com internet limitada**. Desenvolvimento feito em CPU de notebook, com quantização, pausas agendadas e progresso salvo em disco (p. 3).
- Reaproveita do **Deepness** o diálogo de instalação automática de dependências (p. 3, 4).
- Argumento: modelos autossupervisionados têm bom desempenho com poucos ou nenhum rótulo; as soluções existentes em QGIS exigem ajuste fino ou inferência de modelo já treinado (p. 1, 2).
- Figura 2: Sentinel-2 de uma floresta na Tailândia processado por diferentes backbones, mostrando PCA e t-SNE das características (p. 3).

**Evidência (leitura) — Do README:**

- Exemplos de backbones autossupervisionados: DINO, DINOv2, MAE e SAM; modelos do benchmark **Pangaea** (SSL4EO MOCO, DOFA) ainda no roteiro; licença **GPL-3.0**; documentação em iamap.readthedocs.io.
- Pendências declaradas: salvar e reutilizar modelos sklearn na inferência, publicar no repositório oficial do QGIS e lidar com características de modelos **não** ViT.

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **Modelo fundacional**: 3 ocorrências (p. 1, 2)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos



## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites (verificados):**

- **Sem avaliação quantitativa.** O "impacto" descrito é uso interno, webinars e um estudo de terceiros (prévia na documentação) (p. 4).
- Não está documentado como o plugin trata **4 bandas** (RGB+NIR) em backbones que esperam 3 canais; isso precisa ser testado com mosaicos Planet.
- Backbones treinados em imagens naturais ou Sentinel-2/NAIP, não em Planet 3–5 m.
- GPL-3.0 limita incorporar o código em software proprietário.


## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/openjournals/joss-reviews/issues/10329 (p. 1)
- URL citada: https://github.com/openjournals/joss-reviews/issues/10329 (p. 1)
- URL citada: https://github.com/umr-amap/iamap (p. 1)
- URL citada: https://github.com/florianfranz (p. 1)
- URL citada: https://github.com/AMSANJEEV28 (p. 1)
- declaração: “Journal of Open Source Software, 1 11 [(122), 10329. https://doi.org/10.21105/joss.10329.](https://doi.org/10.21105/joss.10329)” (p. 1)
- declaração: “With the democratization of deep learning, some developers have already worked on the integration of deep learning models in geographic information systems such as the open source and widely used QGIS software (QGIS Development Team, 2025).” (p. 2)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 

**Interpretação — O que reaproveitar:**

- **Mapas de similaridade e agrupamento sobre embeddings** como forma barata de **buscar exemplos parecidos** e escolher amostras para rotular na etapa E04 Rotulagem e pré-anotação, sem treinar nada.
- **Classificadores leves (RF/KNN) sobre embeddings** como baseline do EXP1 com poucos rótulos.
- **Desenho de CPU primeiro** (quantização, pausas, progresso em disco) para rodar em máquinas sem GPU.
- Padrão de **diálogo de dependências** (herdado do Deepness) para distribuir o ambiente.

**Interpretação — Teste proposto (hipótese):**

Rodar o IAMAP com DINOv2 sobre um mosaico Planet de 4 bandas, comparar agrupamentos com a classe de referência e medir quantas amostras rotuladas são necessárias para igualar o baseline de atributos (EXP1).

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza método: [[ModeloFundacional|Modelos fundacionais]] — 3 ocorrências (p. 1, 2)
- usa ferramenta: [[QGIS|QGIS]] — 9 ocorrências (p. 1, 2, 3, 4)
- referencia (suporte manual da leitura): [[PreAnotacaoSAM|Pré-anotação assistida (SAM e plugins QGIS)]] — suporte vindo da leitura/título/resumo

**Comparações substantivas com outros artigos:**
- este artigo reutiliza código de [[Aszkowski_2023_DeepnessDeepNeural|Aszkowski 2023]] — IAMAP reaproveita o diálogo de instalação de dependências do Deepness (JOSS, resumo).

## Figuras selecionadas

![[Tresson_2026_IAMAPUnlockingDeep_p2_Figure1.png|520]]
*Figure 1). (p. 2; recorte do PDF convertido)*

![[Tresson_2026_IAMAPUnlockingDeep_p3_Figure2.png|520]]
*Figure 2: A Sentinel-2 image of a forested landscape in Thailand (Khao Banthat Wildlife Sanctuary; (p. 3; recorte do PDF convertido)*


## Anotações do leitor

- 
