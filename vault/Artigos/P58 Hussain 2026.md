---
tipo: artigo
id: P58
titulo: "YOLOSAM: A YOLO-Guided SAM for Accurate Building Segmentation in Remote Sensing Images"
autores: "Musarat Hussain, Ji Peng Huang, Xiankui Liu, Yulin Duan"
ano: 2026
secao: G
categoria: "Pré-catalogação SAM/YOLO e representações"
tipo_publicacao: "Artigo"
papel: ["pré-anotação/representação"]
prioridade: média
doi: "10.1109/JSTARS.2025.3649081"
pdf: ""
texto_integral: nao
fonte_analise: "apenas metadados e comentário (sem PDF)"
n_chunks: 0
sensores: []
tarefas: []
metodos: ["[[SAM]]", "[[YOLO]]"]
datasets: []
metricas: []
ferramentas: []
etapas_pipeline: ["[[E04 Rotulagem e pré-anotação|E04]]", "[[E05 Atributos e representações|E05]]"]
status_leitura: não lido
tags: [artigo, secao/G, prioridade/média, etapa/E04, etapa/E05]
---

# P58 — YOLOSAM: A YOLO-Guided SAM for Accurate Building Segmentation in Remote Sensing Images

**Musarat Hussain, Ji Peng Huang, Xiankui Liu** · 2026 · Artigo · IEEE Journal of Selected Topics in Applied Earth Observations and Remo · [publicação](https://doi.org/10.1109/JSTARS.2025.3649081) · PDF indisponível em coleta/

Seção: **Pré-catalogação SAM/YOLO e representações** · Prioridade: **média** · Análise: *apenas metadados e comentário (sem PDF)*

## O que reaproveitar

- **Uso proposto:** exemplo direto da catalogação prévia sugerida: detector localiza, segmentador delimita.

## Método e dados (da revisão original)

- **Método:** gerador de prompts de caixas baseado em YOLOv8, combinado a adaptações de SAM para segmentação de edificações; avalia WHU, Vaihingen e Inria.

## Limites e cuidados

- não assumir que as resoluções dos benchmarks equivalem a 3–5 m. Um detector que omite um edifício também pode impedir que SAM o segmente.

## Contextos de uso no projeto

- Etapas do pipeline: [[E04 Rotulagem e pré-anotação|E04]], [[E05 Atributos e representações|E05]]
- Métodos: [[SAM]], [[YOLO]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| metodo | [[SAM]] | 3 |
| metodo | [[YOLO]] | 3 |

## Chunks

- Sem PDF em `coleta/` (acesso restrito ou bloqueado); chunking indisponível. Use o link da publicação.

## Relações

- Vizinhos por entidades em comum: [[P80 Feng 2025|P80]], [[P61 Wu 2025|P61]], [[P167 Wu 2023|P167]], [[P166 Jeon 2026|P166]]

## Anotações

- 
