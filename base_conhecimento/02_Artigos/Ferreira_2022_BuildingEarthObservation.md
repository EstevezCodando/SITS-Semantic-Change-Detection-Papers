---
tipo: artigo
id_origem: P69
titulo: "Building Earth Observation Data Cubes on AWS"
ano: 2022
autores: ["Karine Reis Ferreira", "G. R. Queiroz", "Rennan F. B. Marujo", "Ricardo Costa"]
doi: "10.5194/isprs-archives-XLIII-B3-2022-597-2022"
arquivo_fonte: "coleta/P69_Ferreira2022_Building-Earth-Observation-Data-Cubes-on-AWS.pdf"
markdown_fonte: "output/pdf/P69_Ferreira2022_Building-Earth-Observation-Data-Cubes-on-AWS/document.md"
paginas: 6
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[Edificacoes|Edificações e urbanização]]"]
sensores: ["[[Sentinel2|Sentinel-2]]", "[[Landsat|Landsat]]"]
conjuntos_dados: ["[[BrazilDataCube|Brazil Data Cube]]"]
metodos: []
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Ferreira 2022 — Building Earth Observation Data Cubes on AWS

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Karine Reis Ferreira, G. R. Queiroz, Rennan F. B. Marujo, Ricardo Costa (2022). Building Earth Observation Data Cubes on AWS. The international archives of the photogrammetry, remote sensing and spatial information sciences. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.5194/isprs-archives-XLIII-B3-2022-597-2022
- **Arquivo de origem:** `coleta/P69_Ferreira2022_Building-Earth-Observation-Data-Cubes-on-AWS.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P69_Ferreira2022_Building-Earth-Observation-Data-Cubes-on-AWS/document.md` — 6 páginas, 8 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.

- “In this work, we present the architecture of this application and its use to produce EO data cubes for Brazil from big data of remote sensing images.” (p. 1, seção 1 National Institute for Space Research (INPE))

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “To build EO data cubes for the entire country from 2015 to 2023, the Brazil Data Cube project has to process around 734 Terabytes (TB) of Sentinel-2 surface reflectance (SR) images, 108 TB of Landsat-8 SR images and 108 TB of CBERS-4 (MUX a” (p. 2, seção 16 days or monthly, trying to eliminate pixels contaminated)
- “We used this application to produce two years (2017 and 2018) of 16-days temporal-composed EO data cubes of Sentinel-2 (A and B) images for the entire Brazilian territory, based on the grid with 544 tiles of 1.5 by 1 degree each, shown in F” (p. 3, seção XXIV ISPRS Congress (2022 edition), 6–11 June 2022, Nice, Fr)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-2**: 10 ocorrências (p. 1, 2, 3)
- sensor/produto **Landsat**: 4 ocorrências (p. 1, 2)
- conjunto de dados **Brazil Data Cube**: 10 ocorrências (p. 1, 2, 4)
- “Figure 1 shows the BDC ~~S~~ M (small) grid that has 544 tiles of 1 .” (p. 1, seção 4 https://registry.opendata.aws/cbers/)
- “In the Brazil Data cube project, we are using the AWS to produce part of the 16-days temporal-composed data cubes of Sentinel2 images for Brazil.” (p. 2, seção 16 days or monthly, trying to eliminate pixels contaminated)
- “We used this application to produce two years (2017 and 2018) of 16-days temporal-composed EO data cubes of Sentinel-2 (A and B) images for the entire Brazilian territory, based on the grid with 544 tiles of 1.5 by 1 degree each, shown in F” (p. 3, seção XXIV ISPRS Congress (2022 edition), 6–11 June 2022, Nice, Fr)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 9 ocorrências (p. 1, 2, 3)
- **Máscara de nuvem e sombra**: 2 ocorrências (p. 2)
- **Correção atmosférica / reflectância**: 2 ocorrências (p. 2, 3)
- **Índices espectrais**: 2 ocorrências (p. 2)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 21 menções vs 1 de pares)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

Não informado (nada detectado automaticamente).

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 1)
- declaração: “This application is open source and is under development by the Brazil Data Cube project team to produce EO data cubes from open data sets of satellite imagery under the Earth on AWS program.” (p. 1)
- declaração: “These environments do not impose any API for data processing, allowing the development of open source technologies in non-proprietary scripting languages.” (p. 2)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 5 (p. 1, 2, 3); Latência / frequência 1 (p. 2)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 10 ocorrências (p. 1, 2, 3)
- utiliza dado/sensor: [[Landsat|Landsat]] — 4 ocorrências (p. 1, 2)
- emprega conjunto de dados: [[BrazilDataCube|Brazil Data Cube]] — 10 ocorrências (p. 1, 2, 4)
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
