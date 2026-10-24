---
tipo: artigo
id_origem: P49
titulo: "Remote sensing image change detection using deep learning techniques: a comprehensive survey"
ano: 2026
autores: ["Tao Lei", "Shuxin Zhang", "Shaoxiong Lin", "Tongfei Liu", "Zhiyong Lv", "Tao Gao", "Maoguo Gong", "Asoke Kumar Nandi"]
doi: "10.1007/s10462-026-11501-0"
arquivo_fonte: "coleta/P49_Lei2026_Remote-sensing-image-change-detection-using-deep-learning-te.pdf"
markdown_fonte: "output/pdf/P49_Lei2026_Remote-sensing-image-change-detection-using-deep-learning-te/document.md"
paginas: 63
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]"]
sensores: ["[[SAR|Radar (SAR)]]"]
conjuntos_dados: ["[[LEVIRCD|LEVIR-CD]]", "[[WHUCD|WHU-CD]]"]
metodos: ["[[CNN|Redes convolucionais (CNN)]]", "[[Transformer|Transformers]]", "[[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Lei 2026 — Remote sensing image change detection using deep learning techniques: a comprehensive survey

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Tao Lei, Shuxin Zhang, Shaoxiong Lin, Tongfei Liu et al. (2026). Remote sensing image change detection using deep learning techniques: a comprehensive survey. Artificial Intelligence Review. Tipo no catálogo: Revisão.
- **DOI/URL:** https://doi.org/10.1007/s10462-026-11501-0
- **Arquivo de origem:** `coleta/P49_Lei2026_Remote-sensing-image-change-detection-using-deep-learning-te.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P49_Lei2026_Remote-sensing-image-change-detection-using-deep-learning-te/document.md` — 63 páginas, 71 recortes de figuras, 5 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 3):** In recent years, deep learning algorithms have been widely regarded as the preferred method for remote sensing image analysis and have been successfully applied in the field of change detection. However, currently only few comprehensive review papers on deep learning based remote sensing image change detection methods are available. To address the above issues, this study provides the current research status and development trends of remote sensing image change detection and analysis based on deep learning. Firstly, considering the 1 differences in data volume and in data characteristics between different data sources, unlike previous reviews that only focus on the change detection problem of a certain type of remote sensing data, this review outlines the various data types involved in remote sensing image change detection, mainly including very high-resolution (VHR) data, hyperspectral …

- “In section 5, we propose five promising research directions to further promote the development of remote sensing change detection technology.” (p. 7, seção 1 Introduction)
- “In section 5, we propose ﬁve promising research directions to further promote the development of remote sensing change detection technology.” (p. 7, seção 2.1 Change Detection Definition)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “45000 40000 35000 30000 25000 20000 15000 SpDL SsDL UnDL 10000 5000 0 2013-2016 2017-2020 2021-2024 Publication years Fig.” (p. 6, seção 1 Introduction)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **SAR**: 65 ocorrências (p. 4, 5, 6, 7, 9)
- conjunto de dados **LEVIR-CD**: 4 ocorrências (p. 10, 32, 34)
- conjunto de dados **WHU-CD**: 4 ocorrências (p. 10, 32, 34)
- resolução mencionada: 0.075 m (p. 10)
- resolução mencionada: 2.5 m (p. 10)
- resolução mencionada: 1 m (p. 10)
- “However, the interpretability of the original features in the second group of methods may be lost in the mapped feature space.” (p. 4, seção 1 Introduction)
- “In the field of change detection, deep learning methods can extract highlevel semantic features, including spectrum, space, and texture from multi-temporal remote sensing images , as well as explore the nonlinear relationships between diffe” (p. 5, seção 1 Introduction)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 128 ocorrências (p. 5, 6, 7, 11, 14)
- **Segmentação em objetos**: 5 ocorrências (p. 28, 29)
- **Aumento de dados**: 2 ocorrências (p. 24, 40)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 19 menções vs 9 de pares)
**Métodos detectados automaticamente:**
- método/família **CNN**: 108 ocorrências (p. 6, 7, 8, 11, 14)
- método/família **Transformer**: 93 ocorrências (p. 6, 7, 14, 15, 18)
- método/família **Semi/auto-supervisionado**: 70 ocorrências (p. 4, 5, 6, 7, 11)
- método/família **Transfer learning**: 18 ocorrências (p. 6, 20, 22, 25, 26)
- método/família **Rede siamesa**: 13 ocorrências (p. 14, 18, 19, 23, 24)
- método/família **U-Net**: 10 ocorrências (p. 12, 14, 16, 17, 21)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Teste externo / generalização**: 16 ocorrências (p. 5, 20, 22, 24, 25)
- métrica **Precisão/Recall**: 16 ocorrências (p. 4, 20, 34, 35, 36)
- métrica **Acurácia global**: 11 ocorrências (p. 32, 34, 35, 36)
- métrica **IoU**: 6 ocorrências (p. 32, 34)
- métrica **F1**: 5 ocorrências (p. 34, 35, 36)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “In the LEVIR-CD dataset, The C2F-SemiCD algorithm achieved the best performance on 5%, 10%, and 20% labeled data, with AdaSemiCD outperforming other methods in both IoU and OA metrics at 40% labeled data.” (p. 32, seção 4.1 VHR Data in Semi-Supervised Learning)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “The critical step in the third group of methods is classification, which often struggles to produce high-precision results, leading to uncertainty 2” (p. 4, seção 1 Introduction)
- “This refined multi-level classification and detailed exploration enable researchers to gain a deeper and more holistic understanding of how deep learning is applied in remote sensing image change detection, thereby addressing the limitation” (p. 6, seção 1 Introduction)
- “Traditional CNNs often struggle to capture these small objects due to the pooling operation.” (p. 8, seção 2.2.1 Very High-Resolution Data)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 41)
- declaração: “All authors reviewed the manuscript. - Data availability No datasets were generated or analysed during the current study.” (p. 41)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 8 (p. 9, 11, 19, 20, 23); Falsos alertas 1 (p. 16)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[SAR|Radar (SAR)]] — 65 ocorrências (p. 4, 5, 6, 7, 9)
- emprega conjunto de dados: [[LEVIRCD|LEVIR-CD]] — 4 ocorrências (p. 10, 32, 34)
- emprega conjunto de dados: [[WHUCD|WHU-CD]] — 4 ocorrências (p. 10, 32, 34)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 108 ocorrências (p. 6, 7, 8, 11, 14)
- utiliza método: [[Transformer|Transformers]] — 93 ocorrências (p. 6, 7, 14, 15, 18)
- utiliza método: [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 70 ocorrências (p. 4, 5, 6, 7, 11)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
