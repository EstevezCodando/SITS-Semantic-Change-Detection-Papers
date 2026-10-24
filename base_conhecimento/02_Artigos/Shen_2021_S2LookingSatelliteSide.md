---
tipo: artigo
id_origem: P130
titulo: "S2Looking: A Satellite Side-Looking Dataset for Building Change Detection"
ano: 2021
autores: ["Li Shen", "Yao Lu", "Hao Chen", "Hao Wei", "Donghai Xie", "Jiabao Yue", "Rui Chen", "Shouye Lv"]
doi: "10.3390/rs13245094"
arquivo_fonte: "coleta/P130_Shen2021_S2Looking-A-Satellite-Side-Looking-Dataset-for-Building-Chan.pdf"
markdown_fonte: "output/pdf/P130_Shen2021_S2Looking-A-Satellite-Side-Looking-Dataset-for-Building-Chan/document.md"
paginas: 23
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[Edificacoes|Edificações e urbanização]]"]
sensores: ["[[ImagensAereas|Imagens aéreas]]"]
conjuntos_dados: ["[[S2Looking|S2Looking]]", "[[LEVIRCD|LEVIR-CD]]", "[[OSCD|OSCD]]"]
metodos: ["[[RedeSiamesa|Redes siamesas]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Shen 2021 — S2Looking: A Satellite Side-Looking Dataset for Building Change Detection

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Li Shen, Yao Lu, Hao Chen, Hao Wei et al. (2021). S2Looking: A Satellite Side-Looking Dataset for Building Change Detection. Remote Sensing. Tipo no catálogo: Dataset.
- **DOI/URL:** https://doi.org/10.3390/rs13245094
- **Arquivo de origem:** `coleta/P130_Shen2021_S2Looking-A-Satellite-Side-Looking-Dataset-for-Building-Chan.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P130_Shen2021_S2Looking-A-Satellite-Side-Looking-Dataset-for-Building-Chan/document.md` — 23 páginas, 130 recortes de figuras, 1 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Abstract: Building-change detection underpins many important applications, especially in the military and crisis-management domains. Recent methods used for change detection have shifted towards deep learning, which depends on the quality of its training data. The assembly of large-scale annotated satellite imagery datasets is therefore essential for global building-change surveillance. Existing datasets almost exclusively offer near-nadir viewing angles. This limits the range of changes that can be detected. By offering larger observation ranges, the scroll imaging mode of optical satellites presents an opportunity to overcome this restriction. This paper therefore introduces S2Looking, a building-change-detection dataset that contains large-scale side-looking satellite images captured at various off-nadir angles.…

- “In Table 1, we present the statistics relating to existing change-detection datasets, together with those for our S2Looking dataset.” (p. 6, seção 1. Introduction)
- “We evaluated the performance of four classic (FC-EF, FC-Siam-Conc, FC-Siam-Diff, and DTCDSCN) and five state-of-the-art (STANet-Base, STANetBAM, STANet-PAM, CDNet, and BiT) deep-learning methods on both the LEVIR-CD+ dataset and S2Looking d” (p. 14, seção 3. Results)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “These bitemporal images are from 20 different regions located in several cities in the state of Texas in the USA.” (p. 7, seção 2. Materials and Methods)
- “The dataset consists of 5000 bitemporal pairs of very-high-resolution (VHR) registered images collected from the GaoFen (GF), SuperView (SV) and BeiJing-2 (BJ-2) satellites from 2017 to 2020.” (p. 3, seção 1. Introduction)
- “The capture times of the image data vary from 2002 to 2020.” (p. 7, seção 2. Materials and Methods)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Imagens aéreas**: 8 ocorrências (p. 6, 8, 9)
- sensor/produto **UAV**: 3 ocorrências (p. 6)
- conjunto de dados **S2Looking**: 96 ocorrências (p. 1, 3, 4, 6, 7)
- conjunto de dados **LEVIR-CD**: 47 ocorrências (p. 1, 2, 3, 6, 7)
- conjunto de dados **OSCD**: 4 ocorrências (p. 2, 6)
- conjunto de dados **WHU-CD**: 3 ocorrências (p. 2, 6)
- resolução mencionada: 0.8 m (p. 3)
- resolução mencionada: 0.5 m (p. 7)
- resolução mencionada: 20 m (p. 11)
- “Unlike other datasets, AICD [ 22 ] is a synthetic change-detection dataset containing 500 image pairs.” (p. 6, seção 1. Introduction)
- “This subset contained 3597 image pairs.” (p. 16, seção 3. Results)
- “This subset contained 3597 image pairs.” (p. 16, seção 3.2. Benchmark Results)
- “To avoid misaligned image pairs and guarantee the registration accuracy, all the bitemporal images in the S2Looking dataset were manually screened by remote sensing imageinterpretation experts to ensure that the maximum registration deviati” (p. 11, seção 2. Materials and Methods)
- “The bitemporal images were also annotated by the remote sensing image-interpretation experts.” (p. 12, seção 2. Materials and Methods)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 34 ocorrências (p. 1, 3, 4, 6, 9)
- **Recorte em patches/tiles**: 9 ocorrências (p. 6, 7, 11, 13, 14)
- **Textura (GLCM)**: 2 ocorrências (p. 2)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal e série (auto: 67 pares; 12 série)
**Métodos detectados automaticamente:**
- método/família **Rede siamesa**: 12 ocorrências (p. 2, 5, 18, 19)
- método/família **Transformer**: 6 ocorrências (p. 5, 18, 19)
- método/família **CNN**: 4 ocorrências (p. 5, 18)
**Hiperparâmetros detectados automaticamente (verificar):**
- perda: “cross-entropy loss for the fused features” (p. 5)
- tamanho do patch: “1024 × 1024 pixel” (p. 7)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 7 ocorrências (p. 14, 18)
- métrica **Precisão/Recall**: 24 ocorrências (p. 11, 15, 16, 17, 18)
- métrica **F1**: 17 ocorrências (p. 13, 15, 16, 17, 18)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “Many methods have achieved satisfactory results on the LEVIR-CD dataset (F1-score > 0.85) [ 23, 34 ], but the S2Looking dataset presents a whole new set of challenges that changedetection algorithms will need to be able to address.” (p. 13, seção 2. Materials and Methods)
- “The F1-scores of the evaluated methods for the S2Looking dataset were at least 25% lower than the scores for LEVIR-CD+.” (p. 16, seção 3. Results)
- “The F1-scores of the evaluated methods were about 46.4% greater than their average scores for the overall dataset.” (p. 16, seção 3. Results)
- “The F1-scores of the evaluated methods for the S2Looking dataset were at least 25% lower than the scores for LEVIR-CD+.” (p. 16, seção 3.2. Benchmark Results)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “Overall, deep learning approaches are very robust when it comes to variability in the data, but one of their key drawbacks is that they are only as good as the datasets that they use for training [ 35 – 37 ].” (p. 5, seção 1. Introduction)
- “2021, 1, 0 7 of 23 common drawback in that most of the images they contain have been captured at near-nadir viewing angles.” (p. 7, seção 1. Introduction)
- “Due to memory limitations, we kept the size of the original input images to 1024 × 1024 for the classic methods (FC-EF, FC-Siam-Conc, FC-Siam-Diff, and DTCDSCN) and cropped the images to 256 × 256 for the state-of-the-art methods (STANet-Ba” (p. 15, seção 3. Results)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/S2Looking/ (p. 7)
- URL citada: https://github.com/S2Looking/ (p. 7)
- declaração: “Data Availability Statement: Publicly available datasets were analyzed in this study.” (p. 20)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Latência / frequência 5 (p. 3, 8); Sistema operacional 1 (p. 14); Persistência / confirmação 1 (p. 14)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[ImagensAereas|Imagens aéreas]] — 8 ocorrências (p. 6, 8, 9)
- emprega conjunto de dados: [[S2Looking|S2Looking]] — 96 ocorrências (p. 1, 3, 4, 6, 7)
- emprega conjunto de dados: [[LEVIRCD|LEVIR-CD]] — 47 ocorrências (p. 1, 2, 3, 6, 7)
- emprega conjunto de dados: [[OSCD|OSCD]] — 4 ocorrências (p. 2, 6)
- utiliza método: [[RedeSiamesa|Redes siamesas]] — 12 ocorrências (p. 2, 5, 18, 19)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
