---
tipo: conceito
subtipo: "etapa"
titulo: "Recorte em patches/tiles"
aliases: ["Recorte em patches/tiles"]
pasta_tematica: "04_Preparo"
n_artigos: 7
tags: [conceito, etapa]
---

# Recorte em patches/tiles

**Natureza:** etapa. A base distingue algoritmo, arquitetura, ferramenta, tarefa, etapa metodológica, dado e desenho de validação por este campo.

> *Definição, pressupostos e limitações* abaixo são **interpretação/conhecimento geral da base**, salvo onde há token de página. Os fatos dos artigos estão na tabela de evidências.

## Definição

Dividir imagens grandes em blocos para treino e inferência.

## Finalidade

Caber na memória e aumentar amostras.

## Entradas

Imagem grande.

## Saídas

Patches e máscaras.

## Pressupostos

Divisão que evite sobreposição entre treino e teste.

## Limitações

Patches vizinhos entre treino/teste causam vazamento; bordas exigem sobreposição.

## Evidência nos artigos lidos

| Artigo | Relação | Ocorrências | Páginas | Status de leitura |
|---|---|---:|---|---|
| [[Wagner_2023_MappingTropicalForest\|Wagner 2023]] | aplica etapa de preparo | 26 | 4, 5, 6, 7, 8 | lido (profundo) |
| [[Carter_2024_DetectionForestDisturbance\|Carter 2024]] | aplica etapa de preparo | 24 | 1, 2, 3, 4, 5 | lido (profundo) |
| [[Febrita_2025_EvaluatingDrivenAutomated\|Febrita 2025]] | aplica etapa de preparo | 20 | 3, 4, 5, 6, 7 | lido (profundo) |
| [[GonzalezVelez_2026_TropicalDryForest\|GonzalezVelez 2026]] | aplica etapa de preparo | 13 | 2, 8, 10, 12, 15 | lido (profundo) |
| [[Wang_2025_SAMTestingReliability\|Wang 2025]] | aplica etapa de preparo | 9 | 10, 18 | lido (profundo) |
| [[ZarazaAguilera_2022_ChangeDetectionOver\|ZarazaAguilera 2022]] | referência (curado pela leitura) | — | ver nota do artigo | lido (profundo) |
| [[Crato_2025_DetectionRuralRoads\|Crato 2025]] | referência (curado pela leitura) | — | ver nota do artigo | lido (profundo) |

## Navegação

- Mapa: [[MOC_02_PreparoQualidade|Preparação e qualidade das imagens]]
