---
tipo: artigo
id_origem: P02
titulo: "Mapping tropical forest degradation with deep learning and Planet NICFI data"
ano: 2023
autores: ["Ricardo Dalagnol", "Fabien Hubert Wagner", "Lênio Soares Galvão", "Daniel Braga", "Fiona Osborn", "Le Bienfaiteur Sagang", "Polyanna da Conceição Bispo", "Matthew Payne"]
doi: "10.1016/j.rse.2023.113798"
arquivo_fonte: "não informado"
markdown_fonte: "não informado"
paginas: não informado
tipo_documento: "sem texto integral (resumo, documentação ou repositório)"
status_leitura: "lido (parcial)"
relevancia_objetivo: "A"
tarefas: ["[[DegradacaoFlorestal|Degradação e perturbação florestal]]", "[[Desmatamento|Desmatamento]]"]
sensores: ["[[PlanetNICFI|Planet NICFI (basemaps)]]"]
conjuntos_dados: []
metodos: ["[[UNet|U-Net]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/parcial, relevancia/A]
---

# Dalagnol 2023 — Mapping tropical forest degradation with deep learning and Planet NICFI data

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (parcial). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **A** — NICFI de 4,77 m para degradação florestal (leitura parcial do resumo).

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Ricardo Dalagnol, Fabien Hubert Wagner, Lênio Soares Galvão, Daniel Braga et al. (2023). Mapping tropical forest degradation with deep learning and Planet NICFI data. Remote Sensing of Environment. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1016/j.rse.2023.113798
- **Arquivo de origem:** `não disponível em coleta/ (acesso restrito ou bloqueado)`
- **Texto convertido (Markdown) e figuras:** `não informado`
- **Tipo de documento:** sem texto integral (resumo, documentação ou repositório).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Mapear **degradação florestal** (exploração seletiva, fogo e estradas) na Amazônia brasileira com mosaicos **Planet NICFI de 4,77 m** e uma U-Net (modelo **DL-DEGRAD**), separando degradação de remoção completa da cobertura.


## 3. Área de estudo e período analisado

Ver seção 4 (dados), que traz área e período quando informados pelo artigo.

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo



## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem



## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — O que foi verificado (resumo institucional):**

- Dados: Planet NICFI, 4,77 m, Amazônia brasileira; **73.744 amostras rotuladas** para treino.
- Classes de degradação: **corte seletivo (logging), fogo e estradas**.
- Saída: mapas **semestrais** de degradação de 2016 a 2021.
- O modelo usa **padrões espaciais** (textura/forma de perda de árvores) mais do que a reflectância pixel a pixel.
- Validação por amostragem aleatória estratificada; concordância forte com interpretação humana; detecta degradação melhor que produtos operacionais, sobretudo para corte seletivo e fogo; no Mato Grosso a degradação supera o desmatamento em alguns anos.

- **Estratégia temporal (detecção automática, verificar):** não informado

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos



## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

Páginas: não informado (leitura feita sem texto integral convertido; ver a fonte na seção 1).

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — O que não foi verificado:**

- Números de acurácia, arquitetura detalhada, hiperparâmetros, tamanho de patch, divisão treino/validação e desenho amostral (texto integral não obtido).


## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** não avaliado (sem texto). 

**Interpretação — O que reaproveitar:**

- **Taxonomia de degradação** (corte seletivo, fogo, estradas) como extensão da classe "perda parcial / mudança de estrutura" em Taxonomia from-to.
- **Ideia de rotular classes de perda por padrão espacial**, que combina com a recomendação de P01 de tratar degradação separadamente do desmatamento.
- Validação por **amostragem estratificada**, em linha com [[Olofsson_2014_GoodPracticesEstimating|Olofsson 2014]].

**Interpretação — Cuidados:**

- É leitura parcial; não citar métricas até obter o artigo.
- Contexto amazônico e rótulos próprios: transferir para outros biomas exige novos exemplos.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- referência (curado pela leitura): [[PlanetNICFI|Planet NICFI (basemaps)]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[DegradacaoFlorestal|Degradação e perturbação florestal]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[Desmatamento|Desmatamento]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[UNet|U-Net]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[AmostragemEstratificada|Amostragem estratificada]] — suporte vindo da leitura/título/resumo

**Comparações substantivas com outros artigos:**
- [[Wagner_2023_MappingTropicalForest|Wagner 2023]] tem lacuna complementada por este artigo — P01 declara: (p. 15); P02 mapeia degradação com U-Net em Planet NICFI (leitura parcial).

## Anotações do leitor

- 
