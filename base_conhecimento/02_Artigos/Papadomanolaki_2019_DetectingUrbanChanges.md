---
tipo: artigo
id_origem: P146
titulo: "Detecting Urban Changes with Recurrent Neural Networks from Multitemporal Sentinel-2 Data"
ano: 2019
autores: ["Maria Papadomanolaki", "Sagar Verma", "Maria Vakalopoulou", "Siddharth Gupta", "Konstantinos G. Karantzalos"]
doi: "10.1109/igarss.2019.8900330"
arquivo_fonte: "coleta/P146_Papadomanolaki2019_Detecting-Urban-Changes-with-Recurrent-Neural-Networks-from-.pdf"
markdown_fonte: "output/pdf/P146_Papadomanolaki2019_Detecting-Urban-Changes-with-Recurrent-Neural-Networks-from-/document.md"
paginas: 5
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[Edificacoes|Edificações e urbanização]]"]
sensores: ["[[Sentinel2|Sentinel-2]]"]
conjuntos_dados: ["[[OSCD|OSCD]]"]
metodos: ["[[LSTM|Redes recorrentes (LSTM)]]", "[[UNet|U-Net]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Papadomanolaki 2019 — Detecting Urban Changes with Recurrent Neural Networks from Multitemporal Sentinel-2 Data

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Maria Papadomanolaki, Sagar Verma, Maria Vakalopoulou, Siddharth Gupta et al. (2019). Detecting Urban Changes with Recurrent Neural Networks from Multitemporal Sentinel-2 Data. IEEE International Geoscience and Remote Sensing Symposium (IGARSS). Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1109/igarss.2019.8900330
- **Arquivo de origem:** `coleta/P146_Papadomanolaki2019_Detecting-Urban-Changes-with-Recurrent-Neural-Networks-from-.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P146_Papadomanolaki2019_Detecting-Urban-Changes-with-Recurrent-Neural-Networks-from-/document.md` — 5 páginas, 33 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** The advent of multitemporal high resolution data, like the Copernicus Sentinel-2, has enhanced significantly the potential of monitoring the earth’s surface and environmental dynamics. In this paper, we present a novel deep learning framework for urban change detection which combines state-ofthe-art fully convolutional networks (similar to U-Net) for feature representation and powerful recurrent networks (such as LSTMs) for temporal modeling. We report our results on the recently publicly available bi-temporal Onera Satellite Change Detection (OSCD) Sentinel-2 dataset, enhancing the temporal information with additional images of the same region on different dates. Moreover, we evaluate the performance of the recurrent networks as well as the use of the ad ditional dates on the unseen test-set using an ensemble crossvalidation strategy. All the developed models during the validation phase…

- “In this paper, we present a novel deep learning framework for urban change detection which combines state-ofthe-art fully convolutional networks (similar to U-Net) for feature representation and powerful recurrent networks (such as LSTMs) f” (p. 1, seção ABSTRACT)
- “Moreover, we evaluate the performance of the recurrent networks as well as the use of the ad ditional dates on the unseen test-set using an ensemble crossvalidation strategy.” (p. 1, seção ABSTRACT)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-2**: 5 ocorrências (p. 1, 2, 3)
- conjunto de dados **OSCD**: 11 ocorrências (p. 1, 2, 3, 4)
- “Our setup follows the submission system guidelines where the 14 image pairs are used for training and the rest for testing.” (p. 2, seção 2.1. Dataset and Implementation Details)
- “As mentioned earlier, additional Sentinel-2 images depicting the provided cities in different dates were acquired to further enrich the temporal information of the OSCD dataset.” (p. 2, seção 2.1. Dataset and Implementation Details)
- “A total of 32421 patches containing both change and non-change pixels resulted from the 14 training cities and was feedforwarded to the proposed architecture for training.” (p. 3, seção 2.1. Dataset and Implementation Details)
- “13 spectral channels are available for each image pair with ground truth information provided for 14 cities.” (p. 2, seção 2.1. Dataset and Implementation Details)
- “Red and green parts in the predictions’ visualization represent false positive and false negative areas that we have manually annotated, only for the qualitative analysis of our method, since no ground truth is available for the testing par” (p. 3, seção 13 channel volumes require much more computational power)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 8 ocorrências (p. 2, 3)
- **Rotulagem / anotação**: 3 ocorrências (p. 2, 3)
- **Aumento de dados**: 2 ocorrências (p. 3)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal e série (auto: 8 pares; 7 série)
**Métodos detectados automaticamente:**
- método/família **LSTM / recorrente**: 21 ocorrências (p. 1, 2, 3, 4)
- método/família **U-Net**: 11 ocorrências (p. 1, 2, 3, 4)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate values were equal to 64 and 0.0001 respectively” (p. 3)
- batch: “batch size and learning rate values were equal to ” (p. 3)
- otimizador: “Adam while batch size and learning rate valu” (p. 3)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Validação cruzada**: 2 ocorrências (p. 1, 3)
- métrica **Precisão/Recall**: 7 ocorrências (p. 3)
- métrica **F1**: 6 ocorrências (p. 1, 3, 4)
- métrica **Acurácia global**: 3 ocorrências (p. 1, 3)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “All the developed models during the validation phase have scored an overall accuracy of more than 95%, while the use of LSTMs and further temporal information, boost the F1 rate of the change class by an additional 1.5%.” (p. 1, seção ABSTRACT)
- “In addition, recall rates remain over 50% in all Dates-Channels combinations.” (p. 3, seção 13 channel volumes require much more computational)

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 2)
- declaração: “Our final aim is to study the behaviour and prospects of such a model when multitemporal data are available eliminating at the same time the need for any fully-connected layers.” (p. 2)
- hiperparâmetros **não detectados** automaticamente: épocas/iterações, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Sentinel2|Sentinel-2]] — 5 ocorrências (p. 1, 2, 3)
- emprega conjunto de dados: [[OSCD|OSCD]] — 11 ocorrências (p. 1, 2, 3, 4)
- utiliza método: [[LSTM|Redes recorrentes (LSTM)]] — 21 ocorrências (p. 1, 2, 3, 4)
- utiliza método: [[UNet|U-Net]] — 11 ocorrências (p. 1, 2, 3, 4)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
