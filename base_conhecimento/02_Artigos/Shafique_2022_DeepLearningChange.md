---
tipo: artigo
id_origem: P126
titulo: "Deep Learning-Based Change Detection in Remote Sensing Images: A Review"
ano: 2022
autores: ["Ayesha Shafique", "Guo Cao", "Zia Uddin Khan", "Muhammad Asad", "Muhammad Aslam"]
doi: "10.3390/rs14040871"
arquivo_fonte: "coleta/P126_Shafique2022_Deep-Learning-Based-Change-Detection-in-Remote-Sensing-Image.pdf"
markdown_fonte: "output/pdf/P126_Shafique2022_Deep-Learning-Based-Change-Detection-in-Remote-Sensing-Image/document.md"
paginas: 40
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[Edificacoes|Edificações e urbanização]]", "[[ClassificacaoCobertura|Classificação de cobertura e uso da terra]]"]
sensores: ["[[SAR|Radar (SAR)]]", "[[WorldView|WorldView]]", "[[Landsat|Landsat]]"]
conjuntos_dados: ["[[OSCD|OSCD]]"]
metodos: ["[[CNN|Redes convolucionais (CNN)]]", "[[UNet|U-Net]]", "[[RedeSiamesa|Redes siamesas]]", "[[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]]", "[[LSTM|Redes recorrentes (LSTM)]]", "[[SVM|SVM]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]", "[[PatchesTiles|Recorte em patches/tiles]]", "[[CorrecaoAtmosferica|Correção atmosférica e reflectância]]", "[[AumentoDados|Aumento de dados]]", "[[Corregistro|Corregistro e georreferenciamento]]"]
validacao: ["[[Generalizacao|Generalização e domain shift]]", "[[PrecisaoRecall|Precisão e recall]]", "[[Kappa|Coeficiente kappa]]", "[[AcuraciaGlobal|Acurácia global (OA)]]", "[[F1|F1]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Shafique 2022 — Deep Learning-Based Change Detection in Remote Sensing Images: A Review

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Ayesha Shafique, Guo Cao, Zia Uddin Khan, Muhammad Asad et al. (2022). Deep Learning-Based Change Detection in Remote Sensing Images: A Review. Remote Sensing. Tipo no catálogo: Revisão.
- **DOI/URL:** https://doi.org/10.3390/rs14040871
- **Arquivo de origem:** `coleta/P126_Shafique2022_Deep-Learning-Based-Change-Detection-in-Remote-Sensing-Image.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P126_Shafique2022_Deep-Learning-Based-Change-Detection-in-Remote-Sensing-Image/document.md` — 40 páginas, 39 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Abstract: Images gathered from different satellites are vastly available these days due to the fast development of remote sensing (RS) technology. These images significantly enhance the data sources of change detection (CD). CD is a technique of recognizing the dissimilarities in the images acquired at distinct intervals and are used for numerous applications, such as urban area development, disaster management, land cover object identification, etc. In recent years, deep learning (DL) techniques have been used tremendously in change detection processes, where it has achieved great success because of their practical applications. Some researchers have even claimed that DL approaches outperform traditional approaches and enhance change detection accuracy. Therefore, this review focuses on deep learning techniques, such as supervised, unsupervised, and semi-supervised for different change …

- “We present the data from different sensors used for CD in detail, mainly including SAR, multispectral, hyperspectral, VHR, and heterogeneous images.” (p. 4, seção 1. Introduction and Background)
- “The purpose of CD in HS is to detect changes associated with significant spectral fluctuations and those associated with minor spectral variations using comprehensive spectral sampling of HS sensors (which are usually not detectable in MS i” (p. 9, seção 3.2.5. Hyperspectral Images)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “We reviewed the significant research papers in the field published during 2015–2021, mainly from the years of 2019 and 2020, with some papers from 2021.” (p. 4, seção 2. Research Inclusion/Exclusion Criteria)
- “Year-wise publications in journals from 2015 to 2021.” (p. 4, seção 2. Research Inclusion/Exclusion Criteria)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **SAR**: 65 ocorrências (p. 1, 2, 3, 4, 5)
- sensor/produto **WorldView**: 10 ocorrências (p. 5, 6, 8, 10)
- sensor/produto **Landsat**: 8 ocorrências (p. 5, 7, 8, 11, 13)
- sensor/produto **Sentinel-2**: 2 ocorrências (p. 6, 8)
- conjunto de dados **HRSCD**: 3 ocorrências (p. 8)
- conjunto de dados **OSCD**: 3 ocorrências (p. 8, 18)
- resolução mencionada: 15 m (p. 5)
- resolução mencionada: 500 m (p. 5)
- resolução mencionada: 1.5 m (p. 5)
- “High spectral variability within geographic objects increases within-class variance, resulting in the uncertainty of spectral-based image interpretation methods.” (p. 11, seção 3.3.2. Spectral Variability)
- “The method significantly enhances the interpretability and accuracy of remote sensing data.” (p. 13, seção 4. Change Detection Architecture)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 29 ocorrências (p. 10, 14, 15, 16, 17)
- **Recorte em patches/tiles**: 12 ocorrências (p. 15, 16, 22, 25, 27)
- **Correção atmosférica / reflectância**: 9 ocorrências (p. 2, 5, 13, 15, 22)
- **Aumento de dados**: 5 ocorrências (p. 18, 19, 21, 23, 31)
- **Corregistro / georreferenciamento**: 3 ocorrências (p. 2, 26, 32)
- **Normalização / escala**: 3 ocorrências (p. 12, 13)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal e série (auto: 22 pares; 30 série)
**Métodos detectados automaticamente:**
- método/família **CNN**: 29 ocorrências (p. 15, 16, 17, 18, 19)
- método/família **U-Net**: 23 ocorrências (p. 15, 16, 18, 19, 20)
- método/família **Rede siamesa**: 18 ocorrências (p. 15, 16, 17, 22, 23)
- método/família **Semi/auto-supervisionado**: 17 ocorrências (p. 1, 4, 14, 16, 18)
- método/família **LSTM / recorrente**: 16 ocorrências (p. 15, 16, 17, 20, 21)
- método/família **SVM**: 7 ocorrências (p. 15, 22, 29)
**Hiperparâmetros detectados automaticamente (verificar):**
- perda: “cross-entropy loss function, which allows using prior” (p. 19)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Teste externo / generalização**: 6 ocorrências (p. 18, 19, 21, 23)
- **Desbalanceamento**: 2 ocorrências (p. 22, 27)
- métrica **Precisão/Recall**: 25 ocorrências (p. 19, 27, 28, 30, 31)
- métrica **Kappa**: 11 ocorrências (p. 16, 17, 21, 27)
- métrica **Acurácia global**: 10 ocorrências (p. 19, 23, 28, 30, 31)
- métrica **F1**: 9 ocorrências (p. 23, 27, 28, 30, 31)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “Their proposed method exhibits excellent performance on PCC and kappa (0.98, 0.86).” (p. 16, seção 5.1.3. Deep Learning-Based Semi-Supervised Methods)
- “Similarly, it achieved better performance of PCC (0.98, 0.99, 0.99) and kappa (0.91, 0.90).” (p. 16, seção 5.1.3. Deep Learning-Based Semi-Supervised Methods)
- “In [ 125 ], the novel idea of unsupervised method saliency-guided deep neural networks achieved good performance (PCC 0.99 and kappa 0.92) but lacked annotation data.” (p. 17, seção 5.1.3. Deep Learning-Based Semi-Supervised Methods)
- “In reference [ 118 ], the authors achieved the highest PCC and kappa results: 0.99, 0.96.” (p. 17, seção 5.1.3. Deep Learning-Based Semi-Supervised Methods)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “PBCD is the conventional approach and identifies changes by comparing pixels, and as a result, it cannot overcome the limits of radiometric variations and misregistration across various dates or sensors.” (p. 2, seção 1. Introduction and Background)
- “Because of the increased variability among image objects, PBCD approaches, which are generally appropriate for middle- and low-resolution RS images, frequently fail to operate in VHR imagery.” (p. 2, seção 1. Introduction and Background)
- “However, those methods cannot incorporate specific and dependable statistical features for many datasets and, hence, do not produce high detection performance for new datasets.” (p. 3, seção 1. Introduction and Background)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/yolalala/RS-source (p. 6)
- URL citada: https://github.com/yolalala/RS-source (p. 6)
- declaração: “However, MS RS is advantageous in terms of data availability.” (p. 5)
- declaração: “The links of the datasets are as follows: 1. [Bern dataset open source: https://github.com/yolalala/RS-source (accessed on 22](https://github.com/yolalala/RS-source) December 2021).” (p. 6)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 7 (p. 7, 16, 17, 26); Falsos alertas 3 (p. 20, 24); Quase tempo real 1 (p. 13); Sistema operacional 1 (p. 5)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[SAR|Radar (SAR)]] — 65 ocorrências (p. 1, 2, 3, 4, 5)
- utiliza dado/sensor: [[WorldView|WorldView]] — 10 ocorrências (p. 5, 6, 8, 10)
- utiliza dado/sensor: [[Landsat|Landsat]] — 8 ocorrências (p. 5, 7, 8, 11, 13)
- emprega conjunto de dados: [[OSCD|OSCD]] — 3 ocorrências (p. 8, 18)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 29 ocorrências (p. 15, 16, 17, 18, 19)
- utiliza método: [[UNet|U-Net]] — 23 ocorrências (p. 15, 16, 18, 19, 20)
- utiliza método: [[RedeSiamesa|Redes siamesas]] — 18 ocorrências (p. 15, 16, 17, 22, 23)
- utiliza método: [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 17 ocorrências (p. 1, 4, 14, 16, 18)
- utiliza método: [[LSTM|Redes recorrentes (LSTM)]] — 16 ocorrências (p. 15, 16, 17, 20, 21)
- utiliza método: [[SVM|SVM]] — 7 ocorrências (p. 15, 22, 29)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 25 ocorrências (p. 19, 27, 28, 30, 31)
- é avaliado por: [[Kappa|Coeficiente kappa]] — 11 ocorrências (p. 16, 17, 21, 27)
- é avaliado por: [[AcuraciaGlobal|Acurácia global (OA)]] — 10 ocorrências (p. 19, 23, 28, 30, 31)
- é avaliado por: [[F1|F1]] — 9 ocorrências (p. 23, 27, 28, 30, 31)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 29 ocorrências (p. 10, 14, 15, 16, 17)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 12 ocorrências (p. 15, 16, 22, 25, 27)
- aplica etapa de preparo: [[CorrecaoAtmosferica|Correção atmosférica e reflectância]] — 9 ocorrências (p. 2, 5, 13, 15, 22)
- aplica etapa de preparo: [[AumentoDados|Aumento de dados]] — 5 ocorrências (p. 18, 19, 21, 23, 31)
- aplica etapa de preparo: [[Corregistro|Corregistro e georreferenciamento]] — 3 ocorrências (p. 2, 26, 32)
- adota desenho de validação: [[Generalizacao|Generalização e domain shift]] — 6 ocorrências (p. 18, 19, 21, 23)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[ClassificacaoCobertura|Classificação de cobertura e uso da terra]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
