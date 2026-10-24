---
tipo: artigo
id_origem: P122
titulo: "Uncontrolled Illegal Mining and Garimpo in the Brazilian Amazon"
ano: 2024
autores: ["Luiz Cortinhas", "Cesar Guerreiro Diniz", "Raian Vargas Maretto", "Claudio Persello", "Maria Luize Pinheiro", "Márcia C. Castro", "Luis Waldyr Rodrigues Sadeck", "Alexandre Fernandes Filho"]
doi: "10.1038/s41467-024-54220-2"
arquivo_fonte: "coleta/P122_Cortinhas2024_Uncontrolled-Illegal-Mining-and-Garimpo-in-the-Brazilian-Ama.pdf"
markdown_fonte: "output/pdf/P122_Cortinhas2024_Uncontrolled-Illegal-Mining-and-Garimpo-in-the-Brazilian-Ama/document.md"
paginas: 15
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[Mineracao|Mineração]]"]
sensores: ["[[Landsat|Landsat]]"]
conjuntos_dados: ["[[MapBiomas|MapBiomas]]"]
metodos: ["[[UNet|U-Net]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Cortinhas 2024 — Uncontrolled Illegal Mining and Garimpo in the Brazilian Amazon

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Luiz Cortinhas, Cesar Guerreiro Diniz, Raian Vargas Maretto, Claudio Persello et al. (2024). Uncontrolled Illegal Mining and Garimpo in the Brazilian Amazon. Nature Communications. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1038/s41467-024-54220-2
- **Arquivo de origem:** `coleta/P122_Cortinhas2024_Uncontrolled-Illegal-Mining-and-Garimpo-in-the-Brazilian-Ama.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P122_Cortinhas2024_Uncontrolled-Illegal-Mining-and-Garimpo-in-the-Brazilian-Ama/document.md` — 15 páginas, 16 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

Resumo: não localizado no texto convertido.


## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “Reference data and study area Brazil, especially the Brazilian Amazon, is associated with many publicly available datasets, ranging from geological surveys and change detection platforms to deforestation early warning systems.” (p. 9, seção Methods)
- “Therefore, using a deep learning-based classifier and cloud computing infrastructure, we mapped the evolution of mineral extraction in Brazil from 1985 to 2022.” (p. 2, seção Início)
- “Mining area Evolution: industrial mining and Garimpo The extent of Brazilian surface mining was monitored systematically and continuously, producing maps and annual statistics from 1985 to 2022.” (p. 2, seção Results)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Landsat**: 11 ocorrências (p. 2, 8, 9, 12, 13)
- conjunto de dados **MapBiomas**: 6 ocorrências (p. 2, 9, 14, 15)
- resolução mencionada: 30 m (p. 2)
- “Error assessment analysis In this study, a two-stage stratified random sampling approach was used to assess the accuracy of the artificial intelligence (AI)-based model, categorizing 52,320 samples based on a human/visual interpretation as ” (p. 4, seção Results)
- “In this way, 52,320 samples were distributed throughout the Brazilian territory, S.1 Supplementary Material.” (p. 12, seção Methods)
- “Error assessment analysis In this study, a two-stage stratified random sampling approach was used to assess the accuracy of the artificial intelligence (AI)-based model, categorizing 52,320 samples based on a human/visual interpretation as ” (p. 4, seção Results)
- “Reference data and study area Brazil, especially the Brazilian Amazon, is associated with many publicly available datasets, ranging from geological surveys and change detection platforms to deforestation early warning systems.” (p. 9, seção Methods)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Mosaicos e compostos**: 7 ocorrências (p. 8, 9, 10)
- **Rotulagem / anotação**: 4 ocorrências (p. 9, 12)
- **Máscara de nuvem e sombra**: 2 ocorrências (p. 9, 10)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 10 menções vs 0 de pares)
**Métodos detectados automaticamente:**
- método/família **U-Net**: 9 ocorrências (p. 9, 10, 12, 14)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Amostragem estratificada**: 4 ocorrências (p. 4, 12)
- **Validação cruzada**: 2 ocorrências (p. 1, 2)
- métrica **Acurácia global**: 14 ocorrências (p. 5, 6, 7, 9, 12)
- métrica **Estimativa de área**: 6 ocorrências (p. 4, 6, 12)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “However, without a finer spatial constraint to account for the mining class rarity, the OA metric would be statistically inflated to the point where a nonlocally constrained method would quickly yield OA levels greater than 99% while statistically inflating th” (p. 5, seção Results)
- “4, the per grid-per-area weighted approach demonstrated that in 2022, every grid exhibited an OA value greater than 97% throughout Brazil’s territory.” (p. 5, seção Results)
- “The metrics for 2022 revealed an OA value of 99% (A), a CA(Mi) value of 91% (B), and a PA(Mi) value of 91% (C).” (p. 7, seção Discussion)
- “There were more than 52 thousand human-validated samples, distributed over nine different years of the time series (from 1985 to 2022), in which reasonably favorable error metrics, considering the rare characteristic of the class of interest, were systematical” (p. 9, seção Discussion)

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “The Amazon biome delimitation is represented by a light green boundary in maps A and B.” (p. 3, seção Results)
- “Thus, the small-scale concept no longer applies since such lengths and areas cannot represent small-scale measures.” (p. 6, seção Discussion)
- “In turn, error metrics cannot serve as quality guarantees.” (p. 9, seção Discussion)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: gitlab.com/luizcf14/brazil-mining (p. 12)
- URL citada: https://gitlab.com/luizcf14/brazil-mining (p. 12)
- declaração: “Thus, data availability is highly diverse in scale, type, and timeframe.” (p. 9)
- declaração: “Data availability The classifier outputs, high resolution figures and other ancillary files [are all available in the informed GitLab repository.” (p. 12)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Persistência / confirmação 6 (p. 2, 4, 5, 7, 8); Revisão humana 5 (p. 4, 9, 12); Sistema operacional 1 (p. 11); Alertas 1 (p. 9); Custo 1 (p. 12)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Landsat|Landsat]] — 11 ocorrências (p. 2, 8, 9, 12, 13)
- emprega conjunto de dados: [[MapBiomas|MapBiomas]] — 6 ocorrências (p. 2, 9, 14, 15)
- utiliza método: [[UNet|U-Net]] — 9 ocorrências (p. 9, 10, 12, 14)
- trata a tarefa: [[Mineracao|Mineração]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
