---
tipo: artigo
id_origem: P14
titulo: "Time-series land cover change detection using deep learning-based temporal semantic segmentation"
ano: 2024
autores: ["Haixu He", "Jining Yan", "Dong Liang", "Zhongchang Sun", "Jun Li", "Lizhe Wang"]
doi: "10.1016/j.rse.2024.114101"
arquivo_fonte: "não informado"
markdown_fonte: "não informado"
paginas: não informado
tipo_documento: "sem texto integral (resumo, documentação ou repositório)"
status_leitura: "lido (parcial)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[SITS|Séries temporais de imagens (SITS)]]", "[[ClassificacaoCobertura|Classificação de cobertura e uso da terra]]", "[[SegmentacaoSemantica|Segmentação semântica]]"]
sensores: []
conjuntos_dados: []
metodos: []
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/parcial]
---

# He 2024 — Time-series land cover change detection using deep learning-based temporal semantic segmentation

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (parcial). Fichas de leitura profunda usadas como evidência.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Haixu He, Jining Yan, Dong Liang, Zhongchang Sun et al. (2024). Time-series land cover change detection using deep learning-based temporal semantic segmentation. Remote Sensing of Environment. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1016/j.rse.2024.114101
- **Arquivo de origem:** `não disponível em coleta/ (acesso restrito ou bloqueado)`
- **Texto convertido (Markdown) e figuras:** `não informado`
- **Tipo de documento:** sem texto integral (resumo, documentação ou repositório).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Tratar a mudança de cobertura como **segmentação semântica temporal**: cada pixel é uma série 1D mensal e as **bordas dos segmentos temporais** dão *quando* e *para o quê* mudou. É o enquadramento conceitual mais próximo do objetivo do projeto (onde, quando, de-para), mas em Sentinel-2.


## 3. Área de estudo e período analisado

Ver seção 4 (dados), que traz área e período quando informados pelo artigo.

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo



## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem



## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — O que foi verificado:**

- Entrada: Sentinel-2 mensal, 10 bandas (10 e 20 m); a rede usa modelos de segmentação existentes sobre a série 1D (README).
- Dataset de apoio **"Urban monthly land dynamics Sentinel-2 benchmark dataset"**: **32.894 amostras**, cada uma com 48 meses e rótulo de cobertura por data; 6 classes (água, mata, gramínea, solo exposto, superfície impermeável, lavoura); 632,8 MB na versão 2 (2,2 GB em todas as versões); licenças CC BY 4.0 e MIT (Zenodo; o README cita figshare).
- Código sob MIT; arquivos `config.py`, `data_loader.py`, `run.py`, `demo.py`, `metrics.py`; modelos pré-treinados válidos **só para a área do artigo**; reconhece o uso de `lcmap-pyccd` e `bfast-py` como base.
- Em P13, o TSSCD pixel a pixel como baseline obteve **SCS 12,0** na DynamicEarthNet e **11,7** na MUDS, muito abaixo dos métodos espaço-temporais (SCS 26–32), o que sugere que a série **sem contexto espacial** é insuficiente em 3 m.

- **Estratégia temporal (detecção automática, verificar):** não informado

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos



## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

Páginas: não informado (leitura feita sem texto integral convertido; ver a fonte na seção 1).

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — O que não foi verificado:**

- Arquitetura exata, hiperparâmetros, número de amostras por classe, métricas e resultados do artigo (texto integral não obtido).


## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** não avaliado (sem texto). 

**Interpretação — O que reaproveitar:**

- **Formulação** (onde, quando e o quê) e **formato do dataset** (amostra = série mensal de 48 datas com rótulo por data), como modelo para o nosso `evaluation_split` e para o catálogo semântico.
- **Anotação de séries**: o artigo recomenda um método próprio na Seção 5.2 (não lido).
- Pistas de implementação: reutilizar `metrics.py` e a estrutura de `data_loader.py` como ponto de partida.

**Interpretação — Cuidados:**

- Treinar o TSSCD em 3 m com séries por pixel parece insuficiente; combinar com contexto espacial (como o modelo de P13).
- Este registro é uma **leitura parcial**; conferir o artigo antes de citar números.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[SITS|Séries temporais de imagens (SITS)]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[ClassificacaoCobertura|Classificação de cobertura e uso da terra]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[SegmentacaoSemantica|Segmentação semântica]] — suporte vindo da leitura/título/resumo

**Comparações substantivas com outros artigos:**
- [[Vincent_2024_SatelliteImageTime|Vincent 2024]] compara-se com o baseline este artigo — TSSCD (P14) é o baseline pixel a pixel de P13 (p. 7); obtém SCS 12,0 e 11,7 na Tabela 1 de P13.

## Anotações do leitor

- 
