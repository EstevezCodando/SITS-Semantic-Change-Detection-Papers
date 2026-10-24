---
tipo: painel
titulo: "Guia do grafo"
tags: [painel, grafo]
---

# Guia do grafo

O arquivo `.obsidian/graph.json` já traz os filtros e as cores abaixo. O Obsidian reescreve esse arquivo quando você mexe nos controles, e a interface pode variar conforme a versão instalada: se algum controle não existir na sua versão, aplique os valores manualmente em *Grafo → Configurações*.

## Cores por pasta (grupos)

| Pasta | Cor | Consulta do grupo |
|---|---|---|
| 02_Artigos | azul `#3B82F6` | `path:"02_Artigos"` |
| 03_Dados | ciano `#06B6D4` | `path:"03_Dados"` |
| 04_Preparo | laranja `#F97316` | `path:"04_Preparo"` |
| 05_Metodos | roxo `#8B5CF6` | `path:"05_Metodos"` |
| 06_Validacao | amarelo `#EAB308` | `path:"06_Validacao"` |
| 07_Resultados | verde `#22C55E` | `path:"07_Resultados"` |
| 08_Monitoramento | turquesa `#14B8A6` | `path:"08_Monitoramento"` |
| 09_Lacunas | vermelho `#EF4444` | `path:"09_Lacunas"` |

Ciano e turquesa são próximos por pedido de paleta; se confundirem, aumente a saturação de um deles.

## Filtros

- Campo de busca do grafo: `-path:"90_Anexos" -path:"99_Templates" -file:README` (esconde anexos, templates e README).
- Desmarque “Anexos” e “Tags”; mantenha “Existentes apenas” ligado para ocultar links não resolvidos.
- Para investigar, abra **Grafo local** (ícone no painel da nota) com **profundidade 1** (vizinhos diretos) ou **2** (vizinhos dos vizinhos). Em um conceito, a profundidade 1 mostra os artigos que o utilizam.

## Forças (ponto de partida, não valores fixos)

| Controle | Valor inicial | Como ajustar |
|---|---|---|
| Força central | 0,35 | aumente se os nós se espalham demais; diminua se tudo se aglomera |
| Repulsão | 12 | suba (14–18) com mais de ~300 notas; desça (8–10) com poucas |
| Força dos links | 1 | reduza (0,6–0,8) se os mapas puxam clusters demais |
| Distância dos links | 220 | aumente (300+) com muitos nós para reduzir sobreposição |
| Tamanho dos nós | 1 | opcional |

O grafo de forças é dinâmico: as posições mudam a cada abertura e **não há garantia** de distância exata nem de ausência de sobreposição. Para uma disposição fixa use os Canvas (`01_Mapas/*.canvas`).

[[00_Inicio|← Painel]]
