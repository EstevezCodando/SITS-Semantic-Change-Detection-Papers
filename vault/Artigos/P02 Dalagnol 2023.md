---
tipo: artigo
id: P02
titulo: "Mapping tropical forest degradation with deep learning and Planet NICFI data"
autores: "Ricardo Dalagnol, Fabien Hubert Wagner, Lênio Soares Galvão, Daniel Braga"
ano: 2023
secao: A
categoria: "Planet: aplicações diretas"
tipo_publicacao: "Artigo"
papel: ["aplicação Planet"]
prioridade: alta
doi: "10.1016/j.rse.2023.113798"
pdf: ""
texto_integral: sim
fonte_analise: "leitura profunda do texto integral (HTML aberto) + metadados"
n_chunks: 0
sensores: ["[[Planet NICFI]]", "[[Planet (mosaicos e cenas)]]"]
tarefas: ["[[Degradação florestal]]"]
metodos: ["[[U-Net]]"]
datasets: []
metricas: []
ferramentas: []
etapas_pipeline: ["[[E06 Modelos-base de cobertura|E06]]"]
leitura_profunda: "[[LP P02 Dalagnol 2023]]"
status_leitura: lido (parcial)
tags: [artigo, secao/A, prioridade/alta, etapa/E06]
---

# P02 — Mapping tropical forest degradation with deep learning and Planet NICFI data

**Ricardo Dalagnol, Fabien Hubert Wagner, Lênio Soares Galvão** · 2023 · Artigo · Remote Sensing of Environment · [publicação](https://doi.org/10.1016/j.rse.2023.113798) · PDF indisponível em coleta/

Seção: **Planet: aplicações diretas** · Prioridade: **alta** · Análise: *leitura profunda do texto integral (HTML aberto) + metadados*

> [!success] Leitura parcial concluída: [[LP P02 Dalagnol 2023]]

## O que reaproveitar

- **Taxonomia de degradação** (corte seletivo, fogo, estradas) como extensão da classe "perda parcial / mudança de estrutura" em [[Taxonomia from-to]].
- **Ideia de rotular classes de perda por padrão espacial**, que combina com a recomendação de P01 de tratar degradação separadamente do desmatamento.
- Validação por **amostragem estratificada**, em linha com [[P46 Olofsson 2014]].

### Extraído automaticamente

- **Uso proposto:** permite formular uma classe de degradação, além da supressão completa.

## Método e dados (da revisão original)

- **Método/dados:** deep learning com U-Net e Planet NICFI para degradação; incorpora padrões de perda de árvores e textura.

## Limites e cuidados

- transferir para outros biomas e tipos de perturbação exige novos exemplos; degradação não se resume a transição floresta → não floresta.

## Contextos de uso no projeto

- Etapas do pipeline: [[E06 Modelos-base de cobertura|E06]]
- Tarefas: [[Degradação florestal]]
- Sensores/produtos: [[Planet NICFI]], [[Planet (mosaicos e cenas)]]
- Métodos: [[U-Net]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Planet NICFI]] | 2 |
| sensor | [[Planet (mosaicos e cenas)]] | 2 |
| metodo | [[U-Net]] | 1 |
| tarefa | [[Degradação florestal]] | 1 |

## Chunks

- Sem PDF em `coleta/` (acesso restrito ou bloqueado); chunking indisponível. Use o link da publicação.

## Relações

- Vizinhos por entidades em comum: [[P93 Wagner 2025|P93]], [[P03 Carter 2024|P03]], [[P08 Debus 2025|P08]], [[P01 Wagner 2023|P01]]

## Anotações

- 
