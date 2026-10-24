---
tipo: artigo
id_origem: P88
titulo: "CubeSats deliver new insights into agricultural water use at daily and 3 m resolutions"
ano: 2021
autores: ["B. Aragon", "Matteo G. Ziliani", "Rasmus Houborg", "Trenton E. Franz", "Matthew Francis McCabe"]
doi: "10.1038/s41598-021-91646-w"
arquivo_fonte: "coleta/P88_Aragon2021_CubeSats-deliver-new-insights-into-agricultural-water-use-at.pdf"
markdown_fonte: "output/pdf/P88_Aragon2021_CubeSats-deliver-new-insights-into-agricultural-water-use-at/document.md"
paginas: 12
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: []
sensores: ["[[PlanetProdutos|Produtos Planet (visão geral)]]", "[[Landsat|Landsat]]", "[[Sentinel2|Sentinel-2]]"]
conjuntos_dados: []
metodos: []
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Aragon 2021 — CubeSats deliver new insights into agricultural water use at daily and 3 m resolutions

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** B. Aragon, Matteo G. Ziliani, Rasmus Houborg, Trenton E. Franz et al. (2021). CubeSats deliver new insights into agricultural water use at daily and 3 m resolutions. Scientific Reports. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1038/s41598-021-91646-w
- **Arquivo de origem:** `coleta/P88_Aragon2021_CubeSats-deliver-new-insights-into-agricultural-water-use-at.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P88_Aragon2021_CubeSats-deliver-new-insights-into-agricultural-water-use-at/document.md` — 12 páginas, 22 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “Here we present the first daily CubeSat-based retrievals of E at 3 m resolution, using a year-long record of [Planet (www.​planet.​com) cloud-free surface reflectances to estimate crop water use over three agricultural sites](http://www.pla” (p. 2, seção Início)
- “As there is no consensus on the most effective energy closure correction ­procedure , we evaluate the modeled latent heat flux using the residual corrected LE fluxes (i.e., Scientific Reports | (2021) 11:12131 | https://doi.org/10.1038/s415” (p. 2, seção Methods)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “Focusing on three agricultural fields located in Nebraska, USA, high-resolution crop water use estimates are delivered via CubeSat-based evaporation modeling.” (p. 1, seção Início)
- “The study region is characterized by cold winters, hot summers, and overall humid ­conditions and has an extensive history of agronomic data collections and ­analysis .” (p. 2, seção Methods)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Planet (mosaicos e cenas)**: 11 ocorrências (p. 1, 2, 3, 8, 9)
- sensor/produto **Landsat**: 8 ocorrências (p. 1, 3, 4, 6, 8)
- sensor/produto **Sentinel-2**: 3 ocorrências (p. 1, 3, 9)
- resolução mencionada: 3 m (p. 1)
- resolução mencionada: 10 m (p. 1)
- resolução mencionada: 70 m (p. 1)
- “The cloud-masked mosaics are then radiometrically harmonized using HLS reference data acquired over a ‘temporal calibration window’ around the capture time of the mosaic.” (p. 3, seção Methods)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 29 ocorrências (p. 1, 2, 3, 4, 6)
- **Máscara de nuvem e sombra**: 12 ocorrências (p. 1, 2, 3, 4, 8)
- **Índices espectrais**: 12 ocorrências (p. 2, 3, 4, 6, 7)
- **Correção atmosférica / reflectância**: 8 ocorrências (p. 2, 3, 9)
- **Mosaicos e compostos**: 5 ocorrências (p. 3)
- **Preenchimento de lacunas**: 3 ocorrências (p. 3, 8)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- métrica **Precisão/Recall**: 10 ocorrências (p. 1, 2, 7, 8, 9)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “It should be noted that this underestimation was accumulated throughout the season and that the tower E cannot show the spatial variability present in the CubeSat product.” (p. 6, seção Results)
- “Interestingly, the cumulative spatial variability for both fields (Fig. b,d) highlights areas of the field with lower E that cannot be appreciated in the spatial maps (panels a and c of Fig.” (p. 6, seção Results)
- “Furthermore, while reflectance derived vegetation indices are a good indicator of vegetation health and conditions, they cannot provide the early warning signals against yield losses relative to models that incorporate ­LST or ­fluorescence” (p. 8, seção Discussion)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 9)
- declaração: “Data availability The CubeSat data that supports the findings of this study are available from Planet.” (p. 9)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 3 (p. 1, 2, 8); Sistema operacional 2 (p. 1, 8); Alertas 1 (p. 8)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[PlanetProdutos|Produtos Planet (visão geral)]] — 11 ocorrências (p. 1, 2, 3, 8, 9)
- utiliza dado/sensor: [[Landsat|Landsat]] — 8 ocorrências (p. 1, 3, 4, 6, 8)
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 3 ocorrências (p. 1, 3, 9)

## Anotações do leitor

- 
