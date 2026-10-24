---
tipo: artigo
id_origem: P120
titulo: "A near-real-time tropical deforestation monitoring algorithm based on the CuSum change detection method"
ano: 2024
autores: ["Bertrand Ygorra", "Frédéric Frappart", "Jean‐Pierre Wigneron", "Thibault Catry", "Benjamin Pillot", "Antoine Pfefer", "Jonas Courtalon", "Serge Riazanoff"]
doi: "10.3389/frsen.2024.1416550"
arquivo_fonte: "coleta/P120_Ygorra2024_A-near-real-time-tropical-deforestation-monitoring-algorithm.pdf"
markdown_fonte: "output/pdf/P120_Ygorra2024_A-near-real-time-tropical-deforestation-monitoring-algorithm/document.md"
paginas: 12
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (parcial)"
relevancia_objetivo: "B"
tarefas: ["[[Desmatamento|Desmatamento]]"]
sensores: ["[[Sentinel1|Sentinel-1]]", "[[PlanetNICFI|Planet NICFI (basemaps)]]"]
conjuntos_dados: []
metodos: []
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/parcial, relevancia/B]
---

# Ygorra 2024 — A near-real-time tropical deforestation monitoring algorithm based on the CuSum change detection method

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (parcial). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **B** — CuSum em quase tempo real com Sentinel-1; calibração de limiares e latência.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Bertrand Ygorra, Frédéric Frappart, Jean‐Pierre Wigneron, Thibault Catry et al. (2024). A near-real-time tropical deforestation monitoring algorithm based on the CuSum change detection method. Frontiers in Remote Sensing. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.3389/frsen.2024.1416550
- **Arquivo de origem:** `coleta/P120_Ygorra2024_A-near-real-time-tropical-deforestation-monitoring-algorithm.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P120_Ygorra2024_A-near-real-time-tropical-deforestation-monitoring-algorithm/document.md` — 12 páginas, 25 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Versão de **quase tempo real do CuSum** (soma cumulativa) para detectar desmatamento em séries de **Sentinel-1** com unidade mínima de mapeamento de **0,03 ha (3 pixels de 10 m)**, calibrada na Amazônia (Pará, 97,2 km²), e comparada com a versão offline ReCuSum (p. 1–2). "Quase tempo real" é definido como atraso máximo de 90 dias, o limite de confirmação do RADD (p. 2).

- “Here, we present the development of a NRT version of CuSum with a MMU of 0.03 ha.” (p. 1, seção Início)
- “However, the CuSum may not fit the purpose of rapid alerts of deforestation as it was not developed yet as an NRT monitoring system.” (p. 2, seção 6.13 Mha in 2016, according to the Global Forest Review publ)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “In the first part, the small test-study region located in the Brazilian Amazon and the different datasets used here are presented.” (p. 2, seção 6.13 Mha in 2016, according to the Global Forest Review publ)
- “Ygorra et al. [10.3389/frsen.2024.1416550](https://doi.org/10.3389/frsen.2024.1416550) FIGURE 1 The study area is located in the Parà State, Brazil [(A), orange polygon].” (p. 3, seção 90 days) as the “maximum delay limit.”)
- “In the Brazilian semiarid region (BSAR), a 26.96% loss was observed (60,769.39 km ) between 2000 and 2018 (Santos et al., 2020).” (p. 2, seção 6.13 Mha in 2016, according to the Global Forest Review publ)
- “The Sentinel-1 mission is composed of two satellites (S1A and S1B), launched in 2014 and 2016, respectively.” (p. 3, seção 3.2.1 Sentinel-1)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- Sentinel-1 em VV e VH; área de estudo do Pará com grandes cortes rasos e perturbações menores; **referência por inspeção visual de mudanças entre 01/08/2017 e 01/07/2019** (p. 3), com apoio de **mosaico mensal PlanetScope do NICFI** e Sentinel-2 (seção 3.2.2, p. 5).

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-1**: 14 ocorrências (p. 1, 2, 3, 4, 5)
- sensor/produto **SAR**: 13 ocorrências (p. 1, 2, 3, 5, 6)
- sensor/produto **PlanetScope**: 4 ocorrências (p. 4, 6)
- sensor/produto **Sentinel-2**: 2 ocorrências (p. 4, 6)
- conjunto de dados **DETER**: 6 ocorrências (p. 1, 2, 10)
- conjunto de dados **Global Forest Change**: 3 ocorrências (p. 1, 2)
- resolução mencionada: 9.55 m (p. 3)
- resolução mencionada: 4.77 m (p. 4)
- resolução mencionada: 10 m (p. 10)
- “Recently, the Cumulative sum change detection (CuSum) method has been developed for the monitoring of forest disturbances from long time series of Sentinel-1 images.” (p. 1, seção Início)
- “Sentinel-1 images are now being also used by Brazil’s National Institute for Space Research (INPE) in a new version of the Real Time Deforestation Detection System (DETER) system called DETER-R, to identify changes in forest cover (Doblas e” (p. 2, seção 6.13 Mha in 2016, according to the Global Forest Review publ)
- “In the study area, 82 images were used between 2016/09/29 and 2019/07/01.” (p. 3, seção 5 m by 20 m resolution. The images are available from the Eu)
- “Maps of changes were then analysed for all possible parameter configurations (Table 1) using the reference map.” (p. 6, seção 4.1.4.2 CuSum NRT sensitivity analysis)
- “Due to the large cloud cover over the study area, only one Sentinel-2 image and one PlanetScope mosaic were found to be cloud-free to perform the visual interpretation of changes in forest cover.” (p. 6, seção 4.2.1 Reference map composition)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Máscara de nuvem e sombra**: 6 ocorrências (p. 2, 4, 6, 10)
- **Mosaicos e compostos**: 3 ocorrências (p. 4, 6)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Método:**

- CuSum com limiares cruzados (cross-Tc: **Low Tc** e **High Tc**) sobre polarizações VV, VH e **VV ∩ VH**; parâmetros otimizados por **F1** em varredura: nº de imagens antes e depois da data monitorada (p. 7–8).
- Melhor configuração: **High Tc = 100 %, Low Tc = 92 %, 11 imagens antes e 3 depois** (atraso de ~36 dias com Sentinel-1) (p. 8, 10).

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 43 menções vs 5 de pares)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Desbalanceamento**: 3 ocorrências (p. 2, 6, 7)
- métrica **F1**: 32 ocorrências (p. 1, 2, 6, 7, 8)
- métrica **Precisão/Recall**: 16 ocorrências (p. 1, 2, 7, 8, 9)
- métrica **Kappa**: 5 ocorrências (p. 7, 8, 9)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Resultados:**

- **CuSum NRT:** precisão 68 %, recall 72 %, acurácia 93 %, **F1 0,71**, kappa 0,67; **ReCuSum:** precisão 81 %, recall 68 %, acurácia 95 %, F1 0,74, kappa 0,72 (tabela 3, p. 9).
- NRT detecta mais mudança real (737 vs 701 ha) e tem menos falso negativo (284 vs 320 ha), mas **mais falso positivo (335 vs 156 ha)**, sobretudo nas bordas de áreas perturbadas e por eventos no fim do período (p. 8–9).
- Mais de 3 imagens depois reduzem o F1 (rebrota) (p. 10).

**Trechos numéricos detectados automaticamente (verificar):**
- “This method is particularly customizable and has a very small Minimum Mapping Unit (MMU) of 0.03 ha.” (p. 2, seção 6.13 Mha in 2016, according to the Global Forest R)
- “The higher F1-score value of 0.71 was obtained for the VV ∩ VH configuration.” (p. 8, seção 5.1.1 Low T c and high T c combination analysis)
- “For instance, choosing a Low T c value higher than 92% results in a lower F1-score value (0.69 for Low T c = 93%, 0.68 for 94% and 0.67 for 95%).” (p. 8, seção 5.1.1 Low T c and high T c combination analysis)
- “The highest F1-score of each Low T c value is obtained using a High T c value of 100%.” (p. 8, seção 5.1.1 Low T c and high T c combination analysis)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites e observações:**

- Os autores avisam que os parâmetros foram calibrados em uma área pequena e **não valem para todas as florestas**; sazonalidade não foi corrigida e não houve comparação com RADD, GLAD, DETER ou JJ-FAST por falta de área de validação maior (p. 10).
- **Observações minhas:** (a) uma única janela de ~97 km² e um período; os parâmetros são ajustados e avaliados **na mesma área**, o que **inflaciona o F1**; (b) a referência vem da própria equipe, sem análise de concordância entre intérpretes; (c) o trabalho é de radar C-band; serve como referência de lógica (limiar duplo, confirmação com N imagens depois), não de método óptico.

**Trechos detectados automaticamente (verificar contexto):**
- “They are based on the use of optical images which suffer from drawbacks caused by the cloud cover over the Brazilian Amazon regions (Weisse et al., 2019).” (p. 2, seção 6.13 Mha in 2016, according to the Global Forest Review publ)
- “CuSum cross-T c was created to detect forest cover changes based on the changes in backscatter in time series Sentinel-1 SAR images, even during extended periods of cloud cover in tropical forests, which is the fundamental limitation of opt” (p. 10, seção 7 Conclusion)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/Pfefer/ (p. 10)
- URL citada: https://github.com/Pfefer/ (p. 10)
- URL citada: https://github.com/Pfefer/cusum (p. 10)
- declaração: “Implementing a Bayesian updating system after the first detection with an increasing probability of being a real change would be a substantial upgrade to CuSum NRT. ## Data availability statement The datasets presented in this study can be ” (p. 10)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** protótipo de quase tempo real. Define quase tempo real como até 90 dias e obtém ~36 dias de atraso; calibrado em uma só área.
- menções de termos de monitoramento (contagem, não avaliação): Quase tempo real 84 (p. 1, 2, 3, 4, 5); Alertas 6 (p. 1, 2, 5); Sistema operacional 5 (p. 1, 2, 4, 6, 10); Falsos alertas 3 (p. 5, 8, 10); Revisão humana 1 (p. 6)

**Interpretação — O que reaproveitar:**

- **Limiar duplo (alto e baixo) com recombinação espacial** para fechar polígonos de mudança.
- **Varredura de F1 sobre nº de datas antes e depois** como forma de calibrar a persistência exigida (o análogo da regra "≥ 3 meses" de P91).
- **Definição operacional de quase tempo real** por atraso máximo aceitável.

**Interpretação — Cuidados para o nosso projeto:**

- Parâmetros ajustados numa só área; refazer em outra região antes de qualquer uso.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Sentinel1|Sentinel-1]] — 14 ocorrências (p. 1, 2, 3, 4, 5)
- referência (curado pela leitura): [[PlanetNICFI|Planet NICFI (basemaps)]] — suporte vindo da leitura/título/resumo
- discute aspecto de monitoramento: [[QuaseTempoReal|Quase tempo real e latência]] — 84 ocorrências (p. 1, 2, 3, 4, 5)
- discute aspecto de monitoramento: [[Alertas|Alertas de mudança]] — 6 ocorrências (p. 1, 2, 5)
- referência (curado pela leitura): [[PersistenciaConfirmacao|Persistência e confirmação]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Desmatamento|Desmatamento]] — suporte vindo da leitura/título/resumo
- referencia (suporte manual da leitura): [[ReferenciaVisual|Referência por interpretação visual]] — suporte vindo da leitura/título/resumo
- referencia (suporte manual da leitura): [[PosProcessamentoTemporal|Pós-processamento temporal (persistência, janela e colapso)]] — suporte vindo da leitura/título/resumo

**Comparações substantivas com outros artigos:**
- este artigo adota o limite de confirmação de [[Reiche_2021_ForestDisturbanceAlerts|Reiche 2021]] — P120 define quase tempo real como até 90 dias, o limite de confirmação do RADD (P119).

## Figuras selecionadas

![[Ygorra_2024_NearRealTime_p3_FIGURE1.png|520]]
*FIGURE 1 (p. 3; recorte do PDF convertido)*


## Anotações do leitor

- 
