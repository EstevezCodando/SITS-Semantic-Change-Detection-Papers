---
tipo: conceito
subtipo: "etapa"
titulo: "Aprendizado ativo para rotulagem"
aliases: ["Aprendizado ativo para rotulagem"]
pasta_tematica: "04_Preparo"
n_artigos: 2
tags: [conceito, etapa]
---

# Aprendizado ativo para rotulagem

**Natureza:** etapa. A base distingue algoritmo, arquitetura, ferramenta, tarefa, etapa metodológica, dado e desenho de validação por este campo.

> *Definição, pressupostos e limitações* abaixo são **interpretação/conhecimento geral da base**, salvo onde há token de página. Os fatos dos artigos estão na tabela de evidências.

## Definição

Treinar o modelo, escolher entre as imagens sem rótulo as de maior incerteza (por exemplo, entropia acima de 0,6), anotá-las e devolvê-las ao treino em ciclos.

## Finalidade

Obter rótulos de segmentação onde só há pontos, polígonos misturados ou poucos exemplos de classes raras.

## Entradas

Modelo treinado e conjunto de imagens sem rótulo.

## Saídas

Novas anotações focadas nas imagens mais informativas.

## Pressupostos

Anotador disponível a cada ciclo; incerteza do modelo correlacionada com o erro.

## Limitações

Exige ciclos de anotação; o teste independente precisa ficar separado das áreas anotadas depois.

## Evidência nos artigos lidos

| Artigo | Relação | Ocorrências | Páginas | Status de leitura |
|---|---|---:|---|---|
| [[Carter_2024_DetectionForestDisturbance\|Carter 2024]] | referencia (suporte manual da leitura) | — | ver nota do artigo | lido (profundo) |
| [[Masolele_2024_MappingDiversityLand\|Masolele 2024]] | referencia (suporte manual da leitura) | — | ver nota do artigo | lido (profundo) |

## Navegação

