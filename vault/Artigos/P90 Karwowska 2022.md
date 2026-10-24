---
tipo: artigo
id: P90
titulo: "Using Super-Resolution Algorithms for Small Satellite Imagery: A Systematic Review"
autores: "Kinga Karwowska, Damian Wierzbicki"
ano: 2022
secao: J
categoria: "Planet: dados, qualidade e fusão"
tipo_publicacao: "Revisão"
papel: ["dados e qualidade Planet", "revisão"]
prioridade: baixa
doi: "10.1109/jstars.2022.3167646"
pdf: "coleta/P90_Karwowska2022_Using-Super-Resolution-Algorithms-for-Small-Satellite-Imager.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 59
sensores: ["[[SkySat]]"]
tarefas: ["[[Edificações]]"]
metodos: ["[[GAN-difusão|GAN/difusão]]", "[[Super-resolução]]", "[[SAM]]"]
datasets: []
metricas: ["[[RMSE-MAE|RMSE/MAE]]"]
ferramentas: []
etapas_pipeline: ["[[E02 Qualidade e harmonização|E02]]"]
status_leitura: não lido
tags: [artigo, secao/J, prioridade/baixa, etapa/E02]
---

# P90 — Using Super-Resolution Algorithms for Small Satellite Imagery: A Systematic Review

**Kinga Karwowska, Damian Wierzbicki** · 2022 · Revisão · IEEE Journal of Selected Topics in Applied Earth Observations and Remo · [publicação](https://doi.org/10.1109/jstars.2022.3167646) · [PDF](../../coleta/P90_Karwowska2022_Using-Super-Resolution-Algorithms-for-Small-Satellite-Imager.pdf)

Seção: **Planet: dados, qualidade e fusão** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Relevância:** Revisão de super-resolução para imagens de pequenos satélites; limite do que a super-resolução realmente recupera.
- **Revisão:** usar para expandir a bibliografia por rastreamento de referências (família de arquitetura, tipo de mudança).
- **Receita de treino extraída:** tamanho do patch — `1280 × 720 pixel` (confirmar nos chunks).
- **Métricas usadas:** [[RMSE-MAE|RMSE/MAE]]

## Limites e cuidados

- Conferir resolução, bandas, região e rótulos antes de transferir resultados; síntese baseada em registro e metadados.

## Contextos de uso no projeto

- Etapas do pipeline: [[E02 Qualidade e harmonização|E02]]
- Tarefas: [[Edificações]]
- Sensores/produtos: [[SkySat]]
- Métodos: [[GAN-difusão|GAN/difusão]], [[Super-resolução]], [[SAM]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[SkySat]] | 7 |
| metodo | [[GAN-difusão\|GAN/difusão]] | 25 |
| metodo | [[Super-resolução]] | 16 |
| metodo | [[SAM]] | 4 |
| metrica | [[RMSE-MAE\|RMSE/MAE]] | 10 |
| tarefa | [[Edificações]] | 11 |

## Chunks

- Arquivo de chunks: [[P90 chunks]] (59 chunks; resumo 2, introdução 9, trabalhos relacionados 27, métodos 15, discussão 5, conclusão 1)
- Resumo: [[P90 chunks#^P90_c001|c001]], [[P90 chunks#^P90_c002|c002]]
- Método: [[P90 chunks#^P90_c039|c039]], [[P90 chunks#^P90_c040|c040]], [[P90 chunks#^P90_c041|c041]]
- Hiperparâmetros / treino: [[P90 chunks#^P90_c046|c046]], [[P90 chunks#^P90_c047|c047]]
- Limitações / discussão: [[P90 chunks#^P90_c054|c054]], [[P90 chunks#^P90_c055|c055]]

## Relações

- Vizinhos por entidades em comum: [[P105 He 2022|P105]], [[P60 Wang 2024|P60]], [[P59 Zhang 2025|P59]]

## Anotações

- 
