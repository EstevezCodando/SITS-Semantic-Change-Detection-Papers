---
tipo: artigo
id_origem: P66
titulo: "AlphaEarth Foundations: An embedding field model for accurate and efficient global mapping from sparse label data"
ano: 2025
autores: ["Christopher F. Brown", "Kazmierski, Michal R.", "Valerie J. Pasquarella", "William J. Rucklidge", "Masha Samsikova", "Zhang, Chenhui", "Evan Shelhamer", "Lahera, Estefania"]
doi: "10.48550/arXiv.2507.22291"
arquivo_fonte: "coleta/P66_Brown2025_AlphaEarth-Foundations-An-embedding-field-model-for-accurate.pdf"
markdown_fonte: "output/pdf/P66_Brown2025_AlphaEarth-Foundations-An-embedding-field-model-for-accurate/document.md"
paginas: 63
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
tarefas: []
sensores: []
conjuntos_dados: []
metodos: ["[[Transformer|Transformers]]", "[[ModeloFundacional|Modelos fundacionais]]"]
preparo: ["[[PatchesTiles|Recorte em patches/tiles]]", "[[Rotulagem|Rotulagem e anotação]]", "[[MosaicosCompostos|Mosaicos e compostos temporais]]", "[[Reamostragem|Reamostragem]]"]
validacao: ["[[ValidacaoCruzada|Validação cruzada]]", "[[PrecisaoRecall|Precisão e recall]]", "[[EstimativaArea|Estimativa de área com intervalo de confiança]]"]
ferramentas: []
tags: [artigo, leitura/automatica]
---

# Brown 2025 — AlphaEarth Foundations: An embedding field model for accurate and efficient global mapping from sparse label data

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Christopher F. Brown, Kazmierski, Michal R., Valerie J. Pasquarella, William J. Rucklidge et al. (2025). AlphaEarth Foundations: An embedding field model for accurate and efficient global mapping from sparse label data. arXiv (Cornell University). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2507.22291
- **Arquivo de origem:** `coleta/P66_Brown2025_AlphaEarth-Foundations-An-embedding-field-model-for-accurate.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P66_Brown2025_AlphaEarth-Foundations-An-embedding-field-model-for-accurate/document.md` — 63 páginas, 35 recortes de figuras, 1 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “Here we introduce AlphaEarth Foundations, an embedding field model yielding a highly general, geospatial representation that assimilates spatial, temporal, and measurement contexts across multiple sources, enabling accurate and efficient pr” (p. 1, seção Início)
- “In this work, we introduce a foundational geospatial Corresponding author(s): cfb@deepmind.com © 2025 Google DeepMind.” (p. 1, seção Introduction)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “AlphaEarth Foundations: An embedding field model for accurate and efficient global mapping from sparse label data ### Author contributions Conceptualization: C.F.B., M.K., V.J.P., E.Sh., O.G., A.B., Methodology: C.F.B., M.K., V.J.P., W.J.R.” (p. 12, seção Acknowledgements)
- “Our evaluation datasets were derived from publicly available data including: LCMAP CONUS Reference Data Product 1984-2021 land cover, land use and change process attributes, from the United States Geological Survey, which is in the public d” (p. 12, seção Acknowledgements)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-2**: 2 ocorrências (p. 9, 11)
- sensor/produto **Landsat**: 2 ocorrências (p. 1, 11)
- resolução mencionada: 10 m (p. 9)
- “This simplifies the label collection process, allowing trained interpreters to collect larger volumes at scale at the expense of descriptive power for certain use cases.” (p. 1, seção Introduction)
- “Additionally we introduce a challenging evaluation suite composed of high-quality reference data that attempts to faithfully replicate realistic mapping scenarios.” (p. 4, seção Introduction)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 10 ocorrências (p. 6, 7, 11)
- **Rotulagem / anotação**: 8 ocorrências (p. 1, 4, 6, 11)
- **Mosaicos e compostos**: 5 ocorrências (p. 3, 6, 9)
- **Reamostragem**: 4 ocorrências (p. 4, 6)
- **Normalização / escala**: 2 ocorrências (p. 4, 5)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 15 menções vs 2 de pares)
**Métodos detectados automaticamente:**
- método/família **Transformer**: 4 ocorrências (p. 4, 6, 9)
- método/família **Modelo fundacional**: 3 ocorrências (p. 3, 6, 10)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Validação cruzada**: 3 ocorrências (p. 3, 8, 10)
- métrica **Precisão/Recall**: 7 ocorrências (p. 1, 3, 4, 5, 6)
- métrica **Estimativa de área**: 4 ocorrências (p. 3, 8, 9, 10)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Sistema operacional 1 (p. 3); Persistência / confirmação 1 (p. 6)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza método: [[Transformer|Transformers]] — 4 ocorrências (p. 4, 6, 9)
- utiliza método: [[ModeloFundacional|Modelos fundacionais]] — 3 ocorrências (p. 3, 6, 10)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 7 ocorrências (p. 1, 3, 4, 5, 6)
- é avaliado por: [[EstimativaArea|Estimativa de área com intervalo de confiança]] — 4 ocorrências (p. 3, 8, 9, 10)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 10 ocorrências (p. 6, 7, 11)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 8 ocorrências (p. 1, 4, 6, 11)
- aplica etapa de preparo: [[MosaicosCompostos|Mosaicos e compostos temporais]] — 5 ocorrências (p. 3, 6, 9)
- aplica etapa de preparo: [[Reamostragem|Reamostragem]] — 4 ocorrências (p. 4, 6)
- adota desenho de validação: [[ValidacaoCruzada|Validação cruzada]] — 3 ocorrências (p. 3, 8, 10)

## Anotações do leitor

- 
