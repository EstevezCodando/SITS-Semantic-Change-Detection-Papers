---
tipo: artigo
id_origem: P116
titulo: "DETER-RT: The new INPE-TropiSCO deforestation monitoring system in the Amazon biome"
ano: 2024
autores: ["Juan Doblas", "Mariane Souza Reis", "Stéphane Mermoz", "Claudio Aparecido Almeida", "Thierry Koleck", "Cassiano Gustavo Messias", "Luciana de Souza Soler", "Alexandre Bouvet"]
doi: "10.5194/isprs-archives-xlviii-3-2024-127-2024"
arquivo_fonte: "coleta/P116_Doblas2024_DETER-RT-The-new-INPE-TropiSCO-deforestation-monitoring-syst.pdf"
markdown_fonte: "output/pdf/P116_Doblas2024_DETER-RT-The-new-INPE-TropiSCO-deforestation-monitoring-syst/document.md"
paginas: 7
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[Desmatamento|Desmatamento]]", "[[DegradacaoFlorestal|Degradação e perturbação florestal]]", "[[Edificacoes|Edificações e urbanização]]"]
sensores: ["[[SAR|Radar (SAR)]]"]
conjuntos_dados: ["[[DETER|DETER (INPE)]]"]
metodos: []
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Doblas 2024 — DETER-RT: The new INPE-TropiSCO deforestation monitoring system in the Amazon biome

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Juan Doblas, Mariane Souza Reis, Stéphane Mermoz, Claudio Aparecido Almeida et al. (2024). DETER-RT: The new INPE-TropiSCO deforestation monitoring system in the Amazon biome. The international archives of the photogrammetry, remote sensing and spatial information sciences. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.5194/isprs-archives-xlviii-3-2024-127-2024
- **Arquivo de origem:** `coleta/P116_Doblas2024_DETER-RT-The-new-INPE-TropiSCO-deforestation-monitoring-syst.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P116_Doblas2024_DETER-RT-The-new-INPE-TropiSCO-deforestation-monitoring-syst/document.md` — 7 páginas, 8 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** The Amazon biome, undergoing significant deforestation, requires robust monitoring systems for effective management and conservation. This study introduces DETER-RT, a novel deforestation detection system that combines the Synthetic Aperture Radar (SAR)-based DETER-R and the TropiSCO systems to enhance detection capabilities using Sentinel-1 satellite data. DETER-RT utilizes a double-threshold technique to optimize the detection of deforestation by balancing detection accuracy and minimizing false positives across different forest types and conditions in the Amazon. The new system modulates detection thresholds based on the proximity of new disturbances to previously detected deforestation, incorporating a dynamic, regionalized threshold adjustment to cater to the variable characteristics of the Amazon’s diverse forest cover. Initial results indicate that DETER-RT provides more timely an…

- “As such, this research presents the proposal for merging these systems into the hereinpresented DETER-RT framework.” (p. 2, seção Abstract)
- “2.5 Initial comparison with other systems First, we investigated if adjusting the original thresholds used in TropiSCO could improve the accuracy of detection.” (p. 3, seção 5. Freely divulges the results on its dedicated website.)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “2.8 Preliminary timeliness assessment We also evaluated the DETER-RT temporal performance by computing the date of detection of all the deforestation warning polygons detected by its optical counterpart (DETER-B) over three Brazilian munici” (p. 3, seção 0.05 step. A threshold correction factor > 1 would lead to)
- “In order to determine the exact delay attributed to the DETER-RT system, we ran the prototype DETERRT algorithm over the full DETER-B warnings (n=17,033) detected in three municipalities (Feliz Natal, L´abrea and S˜ao F´elix do Xingu) in th” (p. 4, seção 0.85) to maximize global accuracy, whereas v´arzea forests)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-1**: 4 ocorrências (p. 1)
- sensor/produto **SAR**: 3 ocorrências (p. 1, 4)
- conjunto de dados **DETER**: 67 ocorrências (p. 1, 2, 3, 4, 5)
- “This system is also based on the automatic processing of Sentinel-1 time series, with the advantage of flagging areas of deforestation in two steps: 1) first by detecting radar shadows caused by deforestation events, and then 2) delineating” (p. 1, seção Abstract)
- “The three systems are based on the same collection of S1 images, detailed in Section 2.1.” (p. 2, seção Abstract)
- “Furthermore, DETER-R is based on the S1 images loaded and processed by the Google Earth Engine (GEE), in the Ground Range Detected (GRD) format.” (p. 2, seção Abstract)
- “Created as a single system based on the visual interpretation of medium spatial-resolution optical remote sensing, DETER has evolved into a family of systems that encompasses different remote sensing data and detection methodologies (Soler ” (p. 1, seção Abstract)
- “DETER-B operates based on the visual interpretation of optical images.” (p. 1, seção Abstract)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 3 ocorrências (p. 2, 5)
- **Normalização / escala**: 2 ocorrências (p. 2, 4)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 8 menções vs 0 de pares)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

Não informado (nada detectado automaticamente).

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/CNES/ (p. 2)
- URL citada: https://github.com/CNES/ (p. 2)
- declaração: “2.3 TropiSCO Differently from DETER-R, which uses Google’s proprietary technology, TropiSCO uses the open-source PANGEO paradigm and the computational capabilities of the Centre National d’ Etudes Spatiales [´] High-Performance Computing (C” (p. 2)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** candidato a sistema operacional (verificar no texto). menções: operacional 8, alertas 1, quase tempo real 6
- menções de termos de monitoramento (contagem, não avaliação): Sistema operacional 8 (p. 3, 4, 5); Quase tempo real 6 (p. 1, 3, 4); Revisão humana 3 (p. 1, 2); Falsos alertas 2 (p. 1, 3); Alertas 1 (p. 3)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[SAR|Radar (SAR)]] — 3 ocorrências (p. 1, 4)
- emprega conjunto de dados: [[DETER|DETER (INPE)]] — 67 ocorrências (p. 1, 2, 3, 4, 5)
- trata a tarefa: [[Desmatamento|Desmatamento]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[DegradacaoFlorestal|Degradação e perturbação florestal]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
