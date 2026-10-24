---
tipo: artigo
id_origem: P159
titulo: "Land Classification Plugin for QGIS Using Pix2Pix"
ano: 2024
autores: ["James Earl Cubillas", "Reynard Torculas", "Jessie Mayol", "Paul Justine Bajao"]
doi: "10.5194/isprs-annals-x-5-2024-33-2024"
arquivo_fonte: "coleta/P159_Cubillas2024_Land-Classification-Plugin-for-QGIS-Using-Pix2Pix.pdf"
markdown_fonte: "output/pdf/P159_Cubillas2024_Land-Classification-Plugin-for-QGIS-Using-Pix2Pix/document.md"
paginas: 7
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: ["[[Edificacoes|Edificações e urbanização]]", "[[ClassificacaoCobertura|Classificação de cobertura e uso da terra]]"]
sensores: []
conjuntos_dados: []
metodos: []
preparo: ["[[Corregistro|Corregistro e georreferenciamento]]"]
validacao: ["[[AcuraciaGlobal|Acurácia global (OA)]]"]
ferramentas: ["[[QGIS|QGIS]]", "[[PyTorch|PyTorch]]", "[[GDAL|GDAL / rasterio]]"]
tags: [artigo, leitura/automatica]
---

# Cubillas 2024 — Land Classification Plugin for QGIS Using Pix2Pix

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** James Earl Cubillas, Reynard Torculas, Jessie Mayol, Paul Justine Bajao (2024). Land Classification Plugin for QGIS Using Pix2Pix. ISPRS annals of the photogrammetry, remote sensing and spatial information sciences. Tipo no catálogo: Software.
- **DOI/URL:** https://doi.org/10.5194/isprs-annals-x-5-2024-33-2024
- **Arquivo de origem:** `coleta/P159_Cubillas2024_Land-Classification-Plugin-for-QGIS-Using-Pix2Pix.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P159_Cubillas2024_Land-Classification-Plugin-for-QGIS-Using-Pix2Pix/document.md` — 7 páginas, 18 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** Land cover classification is critical in various fields, including environmental monitoring, urban planning, and ecological assessment, facilitating informed decision-making processes. Traditional land cover classification methods often involve laborintensive and time-consuming processes, relying on manual intervention and predefined algorithms. The emergence of deep learning techniques, particularly convolutional neural networks (CNNs), offers a promising solution to automate this process, albeit with complexities in implementation. This study addresses the limitations of existing Geographic Information System (GIS) software and plugins by proposing a novel approach utilizing the Pix2Pix architecture, a type of CNN, for automated land cover classification. The proposed Land Classification Plugin (LCP) integrates seamlessly with QGIS, offering an end-to-end solution for generating classi…


## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- conjunto de dados **OpenStreetMap**: 2 ocorrências (p. 2)
- “A comprehensive evaluation was conducted using a curated set of 10 images, each class comprising 10 points, resulting in 50 points per image.” (p. 6, seção 1.75.1 as the integrated development environment (IDE),)
- “Herein, users manually delineate and extract the desired area, submitting it as input to a trained Pix2Pix model embedded within the plugin.” (p. 2, seção Abstract)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Corregistro / georreferenciamento**: 7 ocorrências (p. 1, 2, 3, 5)
- **Mosaicos e compostos**: 2 ocorrências (p. 1)
- **Normalização / escala**: 2 ocorrências (p. 4)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **CNN**: 6 ocorrências (p. 1)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- métrica **Acurácia global**: 4 ocorrências (p. 1, 5, 6, 7)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “The accuracy assessment of the LCP demonstrated an overall accuracy of 83.40% across diverse land cover classes, indicating its efficacy in classification tasks.” (p. 1, seção Abstract)
- “As depicted in Table 1, the overall accuracy attained by our pre-trained model stands at 83.40%.” (p. 6, seção 1.75.1 as the integrated development environment ()
- “This result implies that our pre-trained model demonstrates a commendable accuracy in classifying pixels across diverse land cover classes compared to SCP with 69.20%.” (p. 6, seção 1.75.1 as the integrated development environment ()
- “As delineated in Tables 3 and 4, the outcomes derived from our pre-trained model exhibit notable Producer accuracy rates across various classes: LCP: Water (86%), Buildings (67%), Vegetation (83%), Road (87%), and Land (94%).” (p. 6, seção 1.75.1 as the integrated development environment ()

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “By harnessing the power of deep learning techniques, particularly the Pix2Pix architecture, the LCP offers an automated solution that streamlines the classification process, overcoming the limitations of traditional methods.” (p. 7, seção 1.75.1 as the integrated development environment (IDE),)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 1)
- declaração: “The emergence of the Semi-Automatic Classification Plugin (SCP), a product of Luca Congedo, has garnered significant attention within the GIS and remote sensing communities due to its open-source nature and comprehensive toolset tailored fo” (p. 1)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 1 (p. 1)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- é avaliado por: [[AcuraciaGlobal|Acurácia global (OA)]] — 4 ocorrências (p. 1, 5, 6, 7)
- usa ferramenta: [[QGIS|QGIS]] — 27 ocorrências (p. 1, 2, 3, 4, 5)
- usa ferramenta: [[PyTorch|PyTorch]] — 4 ocorrências (p. 1, 2, 7)
- usa ferramenta: [[GDAL|GDAL / rasterio]] — 4 ocorrências (p. 1, 2, 5, 7)
- aplica etapa de preparo: [[Corregistro|Corregistro e georreferenciamento]] — 7 ocorrências (p. 1, 2, 3, 5)
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[ClassificacaoCobertura|Classificação de cobertura e uso da terra]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
