---
tipo: leitura_profunda
paper: "P02"
leitura: "parcial (resumo e página institucional; artigo da RSE sem texto integral aberto)"
fonte_lida: "restoration.elti.yale.edu/node/89512 (resumo condensado)"
etapas_pipeline: ["[[E06 Modelos-base de cobertura|E06]]"]
tags: [leitura_profunda, prioridade/alta]
---

# Leitura profunda — P02 Dalagnol 2023

**Mapping tropical forest degradation with deep learning and Planet NICFI data**

Nota do artigo: [[P02 Dalagnol 2023|P02 Dalagnol 2023]] · Leitura: *parcial (resumo e página institucional; artigo da RSE sem texto integral aberto)*

> Leitura feita nesta coleta; valores e afirmações vêm do texto lido, com link para o chunk de origem. O que não foi verificado está marcado.

## Pergunta e escopo
Mapear **degradação florestal** (exploração seletiva, fogo e estradas) na Amazônia brasileira com mosaicos **Planet NICFI de 4,77 m** e uma U-Net (modelo **DL-DEGRAD**), separando degradação de remoção completa da cobertura.

## O que foi verificado (resumo institucional)
- Dados: Planet NICFI, 4,77 m, Amazônia brasileira; **73.744 amostras rotuladas** para treino.
- Classes de degradação: **corte seletivo (logging), fogo e estradas**.
- Saída: mapas **semestrais** de degradação de 2016 a 2021.
- O modelo usa **padrões espaciais** (textura/forma de perda de árvores) mais do que a reflectância pixel a pixel.
- Validação por amostragem aleatória estratificada; concordância forte com interpretação humana; detecta degradação melhor que produtos operacionais, sobretudo para corte seletivo e fogo; no Mato Grosso a degradação supera o desmatamento em alguns anos.

## O que não foi verificado
- Números de acurácia, arquitetura detalhada, hiperparâmetros, tamanho de patch, divisão treino/validação e desenho amostral (texto integral não obtido).

## O que reaproveitar
- **Taxonomia de degradação** (corte seletivo, fogo, estradas) como extensão da classe "perda parcial / mudança de estrutura" em [[Taxonomia from-to]].
- **Ideia de rotular classes de perda por padrão espacial**, que combina com a recomendação de P01 de tratar degradação separadamente do desmatamento.
- Validação por **amostragem estratificada**, em linha com [[P46 Olofsson 2014]].

## Cuidados
- É leitura parcial; não citar métricas até obter o artigo.
- Contexto amazônico e rótulos próprios: transferir para outros biomas exige novos exemplos.
