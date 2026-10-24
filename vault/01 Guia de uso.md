---
tipo: guia
tags: [guia]
---
# Guia de uso do vault

## Como abrir
Abra a pasta `vault/` como vault no Obsidian. O grafo (Ctrl+G) já vem com cores por tipo de nota e esconde os arquivos de chunks.

## Tipos de nota
| Pasta | Conteúdo | Grafo |
|---|---|---|
| `Artigos/` | uma nota por artigo, com propriedades, reaproveitamento, limites e contextos | nós azuis |
| `Conceitos/` | sensores, datasets, métodos, métricas, tarefas e ferramentas (hubs) | nós coloridos por categoria |
| `Pipeline/` | 11 etapas do dado ao resultado | nós vermelhos |
| `Experimentos/` | EXP0–EXP6 com base bibliográfica e registro de execução | nós roxos |
| `Reuso/` | receitas de treino, datasets, código, taxonomia, métricas | nós verdes |
| `Chunks/` | texto do PDF dividido por seção, com âncoras `^ID` | oculto no grafo |

## Fluxo de trabalho sugerido
1. Comece por [[00 Início]] e pela lista de prioridade alta.
2. Ao ler um artigo, mude `status_leitura` (não lido → lendo → lido → aplicado) e escreva em **Anotações**.
3. Ao decidir algo (ex.: grade comum), registre na nota da etapa e linke os artigos que sustentam.
4. Execute um experimento: copie `Templates/Execução de experimento`, preencha e atualize o [[Quadro de resultados]].
5. Para citar um trecho: `![[P01 chunks#^P01_c017]]` incorpora o chunk.

## Consultas Dataview (opcional)
```dataview
TABLE ano, papel, prioridade FROM "Artigos" WHERE contains(etapas_pipeline, "E08") SORT prioridade ASC
```
```dataview
TABLE rows.file.link AS Artigos FROM "Artigos" FLATTEN datasets AS d GROUP BY d
```
```dataview
LIST FROM "Artigos" WHERE texto_integral = "nao" AND prioridade = "alta"
```

## Regras de confiança
- `fonte_analise` indica se a extração veio do texto integral ou só de metadados e comentário.
- Entidades, hiperparâmetros e frases de resultado são **extraídos por regra**; confirme no chunk antes de reutilizar.
- Nada aqui substitui a leitura integral dos artigos de prioridade alta.
