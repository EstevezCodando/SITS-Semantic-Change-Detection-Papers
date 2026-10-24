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
status_leitura: "lido (parcial)"
relevancia_objetivo: "C"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]"]
sensores: ["[[Sentinel1|Sentinel-1]]"]
conjuntos_dados: []
metodos: ["[[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]]"]
preparo: []
validacao: ["[[Desbalanceamento|Desbalanceamento de classes]]"]
ferramentas: []
tags: [artigo, leitura/parcial, relevancia/C]
---

# Shafique 2022 — Deep Learning-Based Change Detection in Remote Sensing Images: A Review

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (parcial). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **C** — Revisão de detecção de mudança até 2021 (leitura parcial).

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Ayesha Shafique, Guo Cao, Zia Uddin Khan, Muhammad Asad et al. (2022). Deep Learning-Based Change Detection in Remote Sensing Images: A Review. Remote Sensing. Tipo no catálogo: Revisão.
- **DOI/URL:** https://doi.org/10.3390/rs14040871
- **Arquivo de origem:** `coleta/P126_Shafique2022_Deep-Learning-Based-Change-Detection-in-Remote-Sensing-Image.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P126_Shafique2022_Deep-Learning-Based-Change-Detection-in-Remote-Sensing-Image/document.md` — 40 páginas, 39 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Revisão da **detecção de mudança com aprendizado profundo** organizada **por tipo de dado** (SAR, multiespectral, hiperespectral, VHR e imagens heterogêneas) e por paradigma (supervisionado, não supervisionado, semissupervisionado) (p. 1, 3–4).

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

**Evidência (leitura) — Método da revisão:**

- Artigos de 2015 a 2021 (foco em 2019–2020, alguns de 2021), de editoras como Elsevier, IEEE e Remote Sensing e de conferências como IGARSS e ISPRS; **68 artigos** de aprendizado profundo para CD (p. 4). A busca é descrita em três fases (título, resumo, leitura integral), sem cadeia de busca nem bases declaradas no trecho lido.
- Estrutura: seção 3 datasets por tipo de sensor (tabelas 2–8); seção 4 arquiteturas; seção 5 literatura por tipo de dado (tabelas 9–12); seção 6 métricas; seção 7 discussão (p. 4).

**Evidência (leitura) — Principais conteúdos lidos:**

- **Sensores** (tabela 2, p. 5): lista de satélites com revisita e resolução; não inclui Planet/PlanetScope entre os exemplos (conferido no trecho lido).
- **Métricas** (p. 27): precisão, revocação, especificidade, F1, acurácia, kappa, IoU e PCC; a revisão destaca que os dados de CD são **extremamente desbalanceados** (p. 27).
- **Resultados de exemplo** (tabelas 14–18, p. 27–31): comparam métodos em conjuntos diferentes, **cada tabela com métricas distintas**: SAR (K de 34,95 a 91,66), VHR (F1 0,68 de CDNet a 0,8756 de U-Net++, OA 0,9673), hiperespectral (Att R2U-Net F1 0,952), multiespectral (F1 de 13,15 de CVA a 80,99 do método proposto) e heterogêneas (OA 95,86 a 98,05). São "exemplos" de trabalhos anteriores, não um benchmark unificado (p. 27).

**Evidência (leitura) — Desafios apontados (seção 7, p. 31–33):**

1. **Amostras de treino** escassas; alternativas: transfer learning, aumento de dados, GAN, autocodificadores (p. 31).
2. **Conhecimento prévio**: o mapa de mudança tende a ser maior que a área alterada; abordagens fracas e semissupervisionadas precisam melhorar (p. 31).
3. **Registro de imagens**: faltam conjuntos públicos; erros de co-registro e imagens fora do nadir seguem sem solução (p. 31–32).
4. **Complexidade da imagem de SR**: objetos de cores, tamanhos e rotações diversos; o problema é "fundamentalmente mal posto" (p. 32).
5. **Mapas de mudança múltiplos**: a maioria dos estudos é binária; poucos fazem mudança multiclasse (p. 32).
- Conclusão: faltam estudos com dados heterogêneos, multirresolução e informação global de imagens grandes (p. 33).

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

**Evidência (leitura) — Limites e observações:**

- **Observações minhas:** (a) a revisão cobre até 2021, portanto não inclui Transformers de CD (BIT, ChangeFormer só entram se citados), modelos Mamba, modelos fundacionais nem NICFI; (b) a seleção dos 68 artigos não é sistemática (sem bases, strings nem critérios de exclusão numerados no trecho lido); (c) comparar métricas de tabelas 14–18 entre si não faz sentido; (d) a equação do kappa/PRE nas equações 6–8 aparece com termos repetidos na extração (p. 27), então conferir no PDF antes de citar.
- Por ter lido só parte, **não cito** conclusões das seções 4 e 5.

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

**Interpretação — O que reaproveitar:**

- **Taxonomia por tipo de dado e por supervisão** para organizar a literatura e justificar o recorte "óptico de resolução média/alta, pares ou séries".
- **Lista de desafios** (poucos rótulos, registro, desbalanceamento, mudança multiclasse) como referência para a seção de lacunas.
- **Ressalva sobre métricas em dados desbalanceados**: F1/IoU da classe de mudança e kappa, não acurácia global.

**Interpretação — Cuidados para o nosso projeto:**

- Defasada para 2022–2026; usar apenas como contexto histórico.
- Não trata de séries temporais nem de mosaicos Planet.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[Sentinel1|Sentinel-1]] — suporte vindo da leitura/título/resumo
- utiliza método: [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 17 ocorrências (p. 1, 4, 14, 16, 18)
- referência (curado pela leitura): [[Desbalanceamento|Desbalanceamento de classes]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
