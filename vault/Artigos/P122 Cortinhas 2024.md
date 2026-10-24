---
tipo: artigo
id: P122
titulo: "Uncontrolled Illegal Mining and Garimpo in the Brazilian Amazon"
autores: "Luiz Cortinhas, Cesar Guerreiro Diniz, Raian Vargas Maretto, Claudio Persello"
ano: 2024
secao: L
categoria: "Desmatamento e alertas"
tipo_publicacao: "Artigo"
papel: ["desmatamento/alerta"]
prioridade: baixa
doi: "10.1038/s41467-024-54220-2"
pdf: "coleta/P122_Cortinhas2024_Uncontrolled-Illegal-Mining-and-Garimpo-in-the-Brazilian-Ama.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 49
sensores: ["[[Landsat]]"]
tarefas: ["[[Mineração]]", "[[Séries temporais de imagens]]"]
metodos: ["[[U-Net]]", "[[NDVI-índices|NDVI/índices]]"]
datasets: ["[[MapBiomas]]"]
metricas: ["[[Acurácia global]]", "[[Estimativa de área - IC|Estimativa de área / IC]]", "[[Precisão-Recall|Precisão/Recall]]"]
ferramentas: ["[[Google Earth Engine]]", "[[TensorFlow]]"]
etapas_pipeline: ["[[E06 Modelos-base de cobertura|E06]]", "[[E09 Pós-processamento e eventos|E09]]", "[[E11 Operação e atualização|E11]]"]
status_leitura: não lido
tags: [artigo, secao/L, prioridade/baixa, etapa/E06, etapa/E09, etapa/E11]
---

# P122 — Uncontrolled Illegal Mining and Garimpo in the Brazilian Amazon

**Luiz Cortinhas, Cesar Guerreiro Diniz, Raian Vargas Maretto** · 2024 · Artigo · Nature Communications · [publicação](https://doi.org/10.1038/s41467-024-54220-2) · [PDF](../../coleta/P122_Cortinhas2024_Uncontrolled-Illegal-Mining-and-Garimpo-in-the-Brazilian-Ama.pdf)

Seção: **Desmatamento e alertas** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Relevância:** Mineração ilegal (garimpo) na Amazônia brasileira; contexto de uma transição relevante ao projeto.
- **Receita de treino extraída:** tamanho do patch — `256 × 256 pixel` (confirmar nos chunks).
- **Métricas usadas:** [[Acurácia global]], [[Estimativa de área - IC|Estimativa de área / IC]], [[Precisão-Recall|Precisão/Recall]]
- **Dados/benchmarks citados:** [[MapBiomas]]

## Limites e cuidados

- Conferir resolução, bandas, região e rótulos antes de transferir resultados; síntese baseada em registro e metadados.

## Contextos de uso no projeto

- Etapas do pipeline: [[E06 Modelos-base de cobertura|E06]], [[E09 Pós-processamento e eventos|E09]], [[E11 Operação e atualização|E11]]
- Tarefas: [[Mineração]], [[Séries temporais de imagens]]
- Sensores/produtos: [[Landsat]]
- Métodos: [[U-Net]], [[NDVI-índices|NDVI/índices]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Landsat]] | 12 |
| dataset | [[MapBiomas]] | 4 |
| metodo | [[U-Net]] | 11 |
| metodo | [[NDVI-índices\|NDVI/índices]] | 4 |
| metrica | [[Acurácia global]] | 19 |
| metrica | [[Estimativa de área - IC\|Estimativa de área / IC]] | 6 |
| metrica | [[Precisão-Recall\|Precisão/Recall]] | 3 |
| tarefa | [[Mineração]] | 270 |
| tarefa | [[Séries temporais de imagens]] | 12 |
| ferramenta | [[Google Earth Engine]] | 6 |
| ferramenta | [[TensorFlow]] | 2 |

## Resultados citados pelos autores (extraídos automaticamente)

> However, without a finer spatial constraint to account for the mining class rarity, the OA metric would be statistically inflated to the point where a nonlocally constrained method would quickly yield OA levels greater than 99% wh
> 4, the per grid-per-area weighted approach demonstrated that in 2022, every grid exhibited an OA value greater than 97% throughout Brazil’s territory.

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P122 chunks]] (49 chunks; resumo 6, resultados 14, discussão 13, métodos 16)
- Resumo: [[P122 chunks#^P122_c001|c001]], [[P122 chunks#^P122_c002|c002]]
- Método: [[P122 chunks#^P122_c034|c034]], [[P122 chunks#^P122_c035|c035]], [[P122 chunks#^P122_c036|c036]]
- Hiperparâmetros / treino: [[P122 chunks#^P122_c039|c039]]
- Resultados numéricos: [[P122 chunks#^P122_c017|c017]], [[P122 chunks#^P122_c018|c018]]
- Limitações / discussão: [[P122 chunks#^P122_c021|c021]], [[P122 chunks#^P122_c022|c022]]

## Relações

- Vizinhos por entidades em comum: [[P05 Zaraza-Aguilera 2022|P05]], [[P123 Alencar 2020|P123]], [[P88 Aragon 2021|P88]], [[P96 Wang 2022|P96]]

## Anotações

- 
