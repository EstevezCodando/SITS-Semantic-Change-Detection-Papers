---
tipo: conceito
subtipo: "dado/produto"
titulo: "Planet NICFI (basemaps)"
aliases: ["Planet NICFI (basemaps)"]
pasta_tematica: "03_Dados"
n_artigos: 6
tags: [conceito, dado]
---

# Planet NICFI (basemaps)

**Natureza:** dado/produto. A base distingue algoritmo, arquitetura, ferramenta, tarefa, etapa metodológica, dado e desenho de validação por este campo.

> *Definição, pressupostos e limitações* abaixo são **interpretação/conhecimento geral da base**, salvo onde há token de página. Os fatos dos artigos estão na tabela de evidências.

## Definição

Mosaicos Planet do programa NICFI para os trópicos, com 4 bandas (RGB+NIR) e ~4,77 m de pixel. Sobre a cadência: [[Wagner_2023_MappingTropicalForest|Wagner 2023]] (p. 3) e [[Vizzari_2022_PlanetScopeSentinelSentinel|Vizzari 2022]] (§ 1) (semestral antes de set/2020).

## Finalidade

Monitorar cobertura e perturbação florestal em alta resolução com mosaicos pouco nublados.

## Entradas

Basemaps normalizados (analíticos) ou visuais, por tile.

## Saídas

Mosaicos por período, prontos para recorte em patches.

## Pressupostos

A reflectância absoluta não é garantida entre datas e satélites; a composição mistura observações de dias diferentes.

## Limitações

Cadência não é mensal antes de set/2020; sem correção atmosférica nos estudos lidos; georreferenciamento pode variar entre datas.

## Evidência nos artigos lidos

| Artigo | Relação | Ocorrências | Páginas | Status de leitura |
|---|---|---:|---|---|
| [[Zhang_2023_MonitoringMonthlyTropical\|Zhang 2023]] | utiliza dado/sensor | 56 | 1, 2, 5, 6, 7 | extraído automaticamente (não lido) |
| [[Wagner_2023_MappingTropicalForest\|Wagner 2023]] | utiliza dado/sensor | 21 | 2, 3, 4, 5, 13 | lido (profundo) |
| [[Masolele_2024_MappingDiversityLand\|Masolele 2024]] | utiliza dado/sensor | 16 | 3, 6, 8, 10, 13 | extraído automaticamente (não lido) |
| [[Wang_2024_ValidationDeforestationHigh\|Wang 2024]] | utiliza dado/sensor | 4 | 2, 3, 4, 6 | extraído automaticamente (não lido) |
| [[Carter_2024_DetectionForestDisturbance\|Carter 2024]] | utiliza dado/sensor | 3 | 2, 12, 13 | lido (profundo) |
| [[Vizzari_2022_PlanetScopeSentinelSentinel\|Vizzari 2022]] | utiliza dado/sensor | — | ver nota do artigo | lido (profundo) |

## Navegação

- Mapa: [[MOC_01_AquisicaoDados|Aquisição e seleção de dados]]
- Lacuna que afeta este conceito: [[L02_CadenciaPlanet|A cadência real dos mosaicos Planet nem sempre é mensal]]
