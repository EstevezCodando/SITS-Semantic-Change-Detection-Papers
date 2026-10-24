---
tipo: artigo
id_origem: P90
titulo: "Using Super-Resolution Algorithms for Small Satellite Imagery: A Systematic Review"
ano: 2022
autores: ["Kinga Karwowska", "Damian Wierzbicki"]
doi: "10.1109/jstars.2022.3167646"
arquivo_fonte: "coleta/P90_Karwowska2022_Using-Super-Resolution-Algorithms-for-Small-Satellite-Imager.pdf"
markdown_fonte: "output/pdf/P90_Karwowska2022_Using-Super-Resolution-Algorithms-for-Small-Satellite-Imager/document.md"
paginas: 21
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: []
sensores: ["[[SAR|Radar (SAR)]]"]
conjuntos_dados: []
metodos: ["[[SuperResolucao|Super-resolução]]", "[[CNN|Redes convolucionais (CNN)]]", "[[SAM|Segment Anything (SAM)]]"]
preparo: ["[[Reamostragem|Reamostragem]]", "[[Normalizacao|Normalização e escala radiométrica]]", "[[Textura|Textura (GLCM)]]", "[[PatchesTiles|Recorte em patches/tiles]]", "[[CorrecaoAtmosferica|Correção atmosférica e reflectância]]"]
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Karwowska 2022 — Using Super-Resolution Algorithms for Small Satellite Imagery: A Systematic Review

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Kinga Karwowska, Damian Wierzbicki (2022). Using Super-Resolution Algorithms for Small Satellite Imagery: A Systematic Review. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing. Tipo no catálogo: Revisão.
- **DOI/URL:** https://doi.org/10.1109/jstars.2022.3167646
- **Arquivo de origem:** `coleta/P90_Karwowska2022_Using-Super-Resolution-Algorithms-for-Small-Satellite-Imager.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P90_Karwowska2022_Using-Super-Resolution-Algorithms-for-Small-Satellite-Imager/document.md` — 21 páginas, 59 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “The objective of linear interpolation methods is to find u function that will meet the condition specified in the following and will then be used for sampling the input image I n,m [LR] [of the] dimensions n × m, being integers I n,m [LR] [” (p. 3, seção II. R ELATED W ORKS)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “Subsets from the study area in true color combination of (a) LMS image (GSD MS = 1.24 m), (b) PAN image (GSD PAN = 0.31 m), (c) PCA fused image, (d) AWPC fused image, (e) IPCA fused image (one iteration), and (f) IPCA fused image (four iter” (p. 6, seção 1 if an edge occurs, and 0 in other cases)
- “This number is more than 4.5 × higher than in 2011–2015.” (p. 1, seção I technology, which, in turn, has contributed to a significa)
- “1947–1955, doi: 10.1109/Com-](https://dx.doi.org/10.1109/CompComm.2017.8322878) [pComm.2017.8322878.](https://dx.doi.org/10.1109/CompComm.2017.8322878) J.Zhang,H.Zhao,andJ.Li,“TRS:Transformersforremotesensingscene classification,” Remote Se” (p. 17, seção IV. C ONCLUSION)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **SAR**: 7 ocorrências (p. 8, 17, 18, 19, 20)
- sensor/produto **SkySat**: 5 ocorrências (p. 1, 2, 13)
- sensor/produto **Planet (mosaicos e cenas)**: 2 ocorrências (p. 21)
- sensor/produto **Sentinel-2**: 2 ocorrências (p. 20, 21)
- resolução mencionada: 32 m (p. 1)
- resolução mencionada: 1 m (p. 5)
- “Due to the highest spectral distortions, the worst results were achieved by the PCA method, which is confirmed by the tested metrics, e.g., very high RMSE value (for WV-2 images RMSE = 97.1180) or low SSIM value (for WV-3 images SSIM = 0.44” (p. 7, seção I MAGES (M EAN V ALUES ))
- “Xu, “Change detection of land use and land cover in an urban region with SPOT-5 images and partial Lanczos extreme learning machine,” J.” (p. 19, seção IV. C ONCLUSION)
- “Akay, “High resolution mapping of urban areas using SPOT-5 images and ancillary data,” Int.” (p. 19, seção IV. C ONCLUSION)
- “Unfortunately, the simplicity of calculations significantly affects the interpretation possibilities of the generated images.” (p. 2, seção I technology, which, in turn, has contributed to a significa)
- “The application of this algorithm enables to enhance the spatial resolution of the image, which, in turn, improves the level of detail, and, as a consequence, the interpretation ability of the image, which was ultimately reflected in numero” (p. 8, seção I MAGES (M EAN V ALUES ))

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Reamostragem**: 19 ocorrências (p. 3, 4, 5, 11, 14)
- **Normalização / escala**: 9 ocorrências (p. 4, 5, 6, 11, 12)
- **Textura (GLCM)**: 7 ocorrências (p. 8, 11, 12, 13, 16)
- **Recorte em patches/tiles**: 6 ocorrências (p. 9, 10, 19)
- **Correção atmosférica / reflectância**: 4 ocorrências (p. 4, 8, 20)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **Super-resolução**: 63 ocorrências (p. 1, 2, 3, 4, 8)
- método/família **CNN**: 20 ocorrências (p. 2, 9, 10, 11, 12)
- método/família **SAM**: 5 ocorrências (p. 7, 15, 16, 21)
**Hiperparâmetros detectados automaticamente (verificar):**
- perda: “focal loss,” IEEE Trans” (p. 17)
- tamanho do patch: “3840 × 2160 pixel” (p. 13)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

Não informado (nada detectado automaticamente).

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Persistência / confirmação 4 (p. 7, 11, 16); Sistema operacional 2 (p. 1)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[SAR|Radar (SAR)]] — 7 ocorrências (p. 8, 17, 18, 19, 20)
- utiliza método: [[SuperResolucao|Super-resolução]] — 63 ocorrências (p. 1, 2, 3, 4, 8)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 20 ocorrências (p. 2, 9, 10, 11, 12)
- utiliza método: [[SAM|Segment Anything (SAM)]] — 5 ocorrências (p. 7, 15, 16, 21)
- aplica etapa de preparo: [[Reamostragem|Reamostragem]] — 19 ocorrências (p. 3, 4, 5, 11, 14)
- aplica etapa de preparo: [[Normalizacao|Normalização e escala radiométrica]] — 9 ocorrências (p. 4, 5, 6, 11, 12)
- aplica etapa de preparo: [[Textura|Textura (GLCM)]] — 7 ocorrências (p. 8, 11, 12, 13, 16)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 6 ocorrências (p. 9, 10, 19)
- aplica etapa de preparo: [[CorrecaoAtmosferica|Correção atmosférica e reflectância]] — 4 ocorrências (p. 4, 8, 20)

## Anotações do leitor

- 
