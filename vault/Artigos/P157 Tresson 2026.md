---
tipo: artigo
id: P157
titulo: "IAMAP: Unlocking Deep Learning in QGIS for non-coders and limited computing resources"
autores: "Paul Tresson, Pierre Le Coz, Hadrien Tulet, Anthony Malkassian"
ano: 2026
secao: N
categoria: "GeoAI e QGIS"
tipo_publicacao: "Software"
papel: ["GeoAI/QGIS", "ferramenta"]
prioridade: alta
doi: "10.21105/joss.10329"
pdf: "coleta/P157_Tresson2026_IAMAP-Unlocking-Deep-Learning-in-QGIS-for-non-coders-and-lim.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 7
sensores: []
tarefas: []
metodos: ["[[Modelo fundacional]]"]
datasets: []
metricas: []
ferramentas: ["[[QGIS]]", "[[TorchGeo]]", "[[Hugging Face]]"]
etapas_pipeline: ["[[E11 Operação e atualização|E11]]"]
leitura_profunda: "[[LP P157 Tresson 2026]]"
status_leitura: lido (profundo)
tags: [artigo, secao/N, prioridade/alta, etapa/E11]
---

# P157 — IAMAP: Unlocking Deep Learning in QGIS for non-coders and limited computing resources

**Paul Tresson, Pierre Le Coz, Hadrien Tulet** · 2026 · Software · The Journal of Open Source Software · [publicação](https://doi.org/10.21105/joss.10329) · [PDF](../../coleta/P157_Tresson2026_IAMAP-Unlocking-Deep-Learning-in-QGIS-for-non-coders-and-lim.pdf)

Seção: **GeoAI e QGIS** · Prioridade: **alta** · Análise: *texto integral (PDF) + metadados*

> [!success] Leitura profunda concluída: [[LP P157 Tresson 2026]]

## O que reaproveitar

- **Mapas de similaridade e agrupamento sobre embeddings** como forma barata de **buscar exemplos parecidos** e escolher amostras para rotular na etapa [[E04 Rotulagem e pré-anotação]], sem treinar nada.
- **Classificadores leves (RF/KNN) sobre embeddings** como baseline do EXP1 com poucos rótulos.
- **Desenho de CPU primeiro** (quantização, pausas, progresso em disco) para rodar em máquinas sem GPU.
- Padrão de **diálogo de dependências** (herdado do Deepness) para distribuir o ambiente.

### Extraído automaticamente

- **Relevância:** IAMAP: plugin QGIS para extração de características com modelos fundacionais autossupervisionados, agrupamento e mapas de similaridade.
- **Código:** https://github.com/umr-lops/iamap

## Limites e cuidados

- Conferir resolução, bandas, região e rótulos antes de transferir resultados; síntese baseada em registro e metadados.

## Contextos de uso no projeto

- Etapas do pipeline: [[E11 Operação e atualização|E11]]
- Métodos: [[Modelo fundacional]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| metodo | [[Modelo fundacional]] | 3 |
| ferramenta | [[QGIS]] | 9 |
| ferramenta | [[TorchGeo]] | 2 |
| ferramenta | [[Hugging Face]] | 2 |

## Chunks

- Arquivo de chunks: [[P157 chunks]] (7 chunks; resumo 7)
- Resumo: [[P157 chunks#^P157_c001|c001]], [[P157 chunks#^P157_c002|c002]]

## Relações

- Vizinhos por entidades em comum: [[P170 Zhou 2026|P170]], [[P66 Brown 2025|P66]]

## Anotações

- 
