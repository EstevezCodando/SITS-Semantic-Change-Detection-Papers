---
tipo: conceito
subtipo: "arquitetura"
titulo: "U-TAE (U-Net com atenção temporal)"
aliases: ["U-TAE (U-Net com atenção temporal)"]
pasta_tematica: "05_Metodos"
n_artigos: 3
tags: [conceito, arquitetura]
---

# U-TAE (U-Net com atenção temporal)

**Natureza:** arquitetura. A base distingue algoritmo, arquitetura, ferramenta, tarefa, etapa metodológica, dado e desenho de validação por este campo.

> *Definição, pressupostos e limitações* abaixo são **interpretação/conhecimento geral da base**, salvo onde há token de página. Os fatos dos artigos estão na tabela de evidências.

## Definição

U-Net com codificador temporal de atenção para séries de imagens.

## Finalidade

Segmentar séries temporais.

## Entradas

Série (T×H×W×C).

## Saídas

Mapa agregado ou por data.

## Pressupostos

Séries regulares.

## Limitações

Agrega o tempo, a menos de modificação.

## Evidência nos artigos lidos

| Artigo | Relação | Ocorrências | Páginas | Status de leitura |
|---|---|---:|---|---|
| [[Vincent_2024_SatelliteImageTime\|Vincent 2024]] | utiliza método | 16 | 2, 3, 6, 7, 8 | lido (profundo) |
| [[Garnot_2021_PanopticSegmentationSatellite\|Garnot 2021]] | utiliza método | 9 | 2, 6, 7, 8 | extraído automaticamente (não lido) |
| [[Toker_2022_DynamicEarthNetDailyMulti\|Toker 2022]] | utiliza método | 5 | 6, 7 | lido (profundo) |

## Navegação

- Mapa: [[MOC_06_DeepLearning|Deep Learning (arquiteturas e estratégias)]]
- Mapa: [[MOC_07_MudancaSeries|Detecção de mudanças e séries temporais]]
