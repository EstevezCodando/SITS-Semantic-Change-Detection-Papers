---
tipo: artigo
id: P09
titulo: "Tropical dry forest land use/land cover change detection using semi-supervised deep learning algorithms and remote sensing"
autores: "Juan Carlos Gonzalez-Velez, Maria Constanza Torres-Madronero, Juan D. Martinez-Vargas, Paula Rodríguez-Marín"
ano: 2026
secao: A
categoria: "Planet: aplicações diretas"
tipo_publicacao: "Artigo"
papel: ["aplicação Planet"]
prioridade: baixa
doi: "10.1007/s10661-025-14897-4"
pdf: "coleta/P09_Gonzalez-Velez2026_Tropical-dry-forest-land-use-land-cover-change-detection-usi.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 56
sensores: ["[[Sentinel-1-SAR|Sentinel-1/SAR]]", "[[PlanetScope]]", "[[Sentinel-2]]"]
tarefas: ["[[Classificação de cobertura]]", "[[Detecção de mudança (binária)]]", "[[Anotação-rotulagem|Anotação/rotulagem]]"]
metodos: ["[[U-Net]]", "[[Semi-auto-supervisionado|Semi/auto-supervisionado]]", "[[ResNet]]", "[[NDVI-índices|NDVI/índices]]", "[[Fusão de dados]]"]
datasets: []
metricas: ["[[IoU - mIoU|IoU / mIoU]]", "[[F1]]", "[[Acurácia global]]"]
ferramentas: ["[[Google Earth Engine]]", "[[PyTorch]]"]
etapas_pipeline: ["[[E04 Rotulagem e pré-anotação|E04]]", "[[E06 Modelos-base de cobertura|E06]]"]
status_leitura: não lido
tags: [artigo, secao/A, prioridade/baixa, etapa/E04, etapa/E06]
---

# P09 — Tropical dry forest land use/land cover change detection using semi-supervised deep learning algorithms and remote sensing

**Juan Carlos Gonzalez-Velez, Maria Constanza Torres-Madronero, Juan D. Martinez-Vargas** · 2026 · Artigo · Environmental Monitoring and Assessment · [publicação](https://doi.org/10.1007/s10661-025-14897-4) · [PDF](../../coleta/P09_Gonzalez-Velez2026_Tropical-dry-forest-land-use-land-cover-change-detection-usi.pdf)

Seção: **Planet: aplicações diretas** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Uso proposto:** escassez de rótulos e confusão entre formações vegetais, áreas abertas e regeneração.
- **Receita de treino extraída:** taxa de aprendizado — `learning rate of 1.58 × 10−4 that was modulated each step by a O`; batch size — `batch size of 10 images, using the AdamW optimizer`; épocas — `300 epochs`; otimizador — `AdamW optimizer with a weight decay of 5 × 10`; tamanho do patch — `288 × 288 pixel` (confirmar nos chunks).
- **Métricas usadas:** [[IoU - mIoU|IoU / mIoU]], [[F1]], [[Acurácia global]]

## Método e dados (da revisão original)

- **Método/dados:** pseudorrótulos, Y-Net, óptico/radar, PlanetScope e composições para floresta tropical seca na Colômbia.

## Limites e cuidados

- composições anuais/semestrais reduzem a informação intranual; não replicar esse passo se o objetivo central for datar eventos mensais.

## Contextos de uso no projeto

- Etapas do pipeline: [[E04 Rotulagem e pré-anotação|E04]], [[E06 Modelos-base de cobertura|E06]]
- Tarefas: [[Classificação de cobertura]], [[Detecção de mudança (binária)]], [[Anotação-rotulagem|Anotação/rotulagem]]
- Sensores/produtos: [[Sentinel-1-SAR|Sentinel-1/SAR]], [[PlanetScope]], [[Sentinel-2]]
- Métodos: [[U-Net]], [[Semi-auto-supervisionado|Semi/auto-supervisionado]], [[ResNet]], [[NDVI-índices|NDVI/índices]], [[Fusão de dados]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Sentinel-1-SAR\|Sentinel-1/SAR]] | 60 |
| sensor | [[PlanetScope]] | 15 |
| sensor | [[Sentinel-2]] | 13 |
| metodo | [[U-Net]] | 53 |
| metodo | [[Semi-auto-supervisionado\|Semi/auto-supervisionado]] | 34 |
| metodo | [[ResNet]] | 31 |
| metodo | [[NDVI-índices\|NDVI/índices]] | 5 |
| metodo | [[Fusão de dados]] | 4 |
| metrica | [[IoU - mIoU\|IoU / mIoU]] | 58 |
| metrica | [[F1]] | 18 |
| metrica | [[Acurácia global]] | 14 |
| tarefa | [[Classificação de cobertura]] | 63 |
| tarefa | [[Detecção de mudança (binária)]] | 14 |
| tarefa | [[Anotação-rotulagem\|Anotação/rotulagem]] | 11 |
| ferramenta | [[Google Earth Engine]] | 8 |
| ferramenta | [[PyTorch]] | 3 |

## Resultados citados pelos autores (extraídos automaticamente)

> The framework achieves state-of-the-art results, with a mean overall accuracy of 95.3% and a mean Intersection over Union (mIoU) of 88.1%, outperforming established models like standard U-Net and PSPNet.
> Even in scenarios where only 60% of the dataset is labeled, the semi-supervised method maintains accuracy above 90%, demonstrating its robustness in limited-data conditions.
> Even in scenarios where only 60% of the dataset is labeled, the semi-supervised method maintains accuracy above 90%, demonstrating its robustness in limited-data conditions.

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P09 chunks]] (56 chunks; resumo 2, introdução 28, resultados 9, discussão 14, conclusão 3)
- Resumo: [[P09 chunks#^P09_c001|c001]], [[P09 chunks#^P09_c002|c002]]
- Hiperparâmetros / treino: [[P09 chunks#^P09_c021|c021]], [[P09 chunks#^P09_c027|c027]], [[P09 chunks#^P09_c050|c050]]
- Resultados numéricos: [[P09 chunks#^P09_c031|c031]], [[P09 chunks#^P09_c032|c032]], [[P09 chunks#^P09_c033|c033]]
- Limitações / discussão: [[P09 chunks#^P09_c040|c040]], [[P09 chunks#^P09_c041|c041]]

## Relações

- Vizinhos por entidades em comum: [[P127 Miller 2024|P127]], [[P151 Lu 2025|P151]], [[P32 Szwarcman 2024|P32]], [[P96 Wang 2022|P96]]

## Anotações

- 
