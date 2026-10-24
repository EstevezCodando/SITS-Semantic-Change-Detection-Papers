---
tipo: artigo
id: P05
titulo: "Change Detection over mining areas using Deep Neural Networks from Planetscope image time series"
autores: "Maycol Alejandro Zaraza-Aguilera, Erika Upegui, Oscar Javier Espejo-Valero"
ano: 2022
secao: A
categoria: "Planet: aplicações diretas"
tipo_publicacao: "Artigo"
papel: ["aplicação Planet"]
prioridade: alta
doi: "10.1109/tla.2022.9878176"
pdf: "coleta/P05_Zaraza-Aguilera2022_Change-Detection-over-mining-areas-using-Deep-Neural-Netw.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 32
sensores: ["[[Sentinel-2]]", "[[PlanetScope]]"]
tarefas: ["[[Séries temporais de imagens]]", "[[Mineração]]"]
metodos: ["[[U-Net]]"]
datasets: []
metricas: ["[[IoU - mIoU|IoU / mIoU]]", "[[Kappa]]"]
ferramentas: []
etapas_pipeline: ["[[E06 Modelos-base de cobertura|E06]]"]
leitura_profunda: "[[LP P05 Zaraza-Aguilera 2022]]"
status_leitura: lido (profundo)
tags: [artigo, secao/A, prioridade/alta, etapa/E06]
---

# P05 — Change Detection over mining areas using Deep Neural Networks from Planetscope image time series

**Maycol Alejandro Zaraza-Aguilera, Erika Upegui, Oscar Javier Espejo-Valero** · 2022 · Artigo · IEEE Latin America Transactions · [publicação](https://latamt.ieeer9.org/index.php/transactions/article/view/6556) · [PDF](../../coleta/P05_Zaraza-Aguilera2022_Change-Detection-over-mining-areas-using-Deep-Neural-Netw.pdf)

Seção: **Planet: aplicações diretas** · Prioridade: **alta** · Análise: *texto integral (PDF) + metadados*

> [!success] Leitura profunda concluída: [[LP P05 Zaraza-Aguilera 2022]]

## O que reaproveitar

- **Comparação pareada EXP2 vs EXP3** com os mesmos blocos e métricas (pós-classificação vs mudança direta).
- **Desenho de blocos** (1,6 km com folga de 0,4 km) como política de partição espacial contra vazamento.
- **Tratamento de nuvem** como prioridade: a pós-classificação exige máscara de observação válida.
- **Não gastar tempo com NDVI** como entrada extra no primeiro ciclo (resultado negativo relatado).
- **Loss DiceFocal** como padrão para classes raras.

### Extraído automaticamente

- **Uso proposto:** evidência para comparar duas estratégias no seu piloto, incluindo solo exposto e alteração de grandes superfícies.
- **Receita de treino extraída:** batch size — `batch size) de 16, como indica el trabajo de Ball,` (confirmar nos chunks).
- **Métricas usadas:** [[IoU - mIoU|IoU / mIoU]], [[Kappa]]

## Método e dados (da revisão original)

- **Método/dados:** mina de Cerrejón, Colômbia; compara pós-classificação com U-Net/FPN a detecção direta por U-Net modificada em pares da série.

## Limites e cuidados

- desempenho em mineração não garante distinção entre obra, terraplenagem, via e solo naturalmente exposto. A página disponibiliza links de PDF e código.

## Contextos de uso no projeto

- Etapas do pipeline: [[E06 Modelos-base de cobertura|E06]]
- Tarefas: [[Séries temporais de imagens]], [[Mineração]]
- Sensores/produtos: [[Sentinel-2]], [[PlanetScope]]
- Métodos: [[U-Net]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Sentinel-2]] | 6 |
| sensor | [[PlanetScope]] | 3 |
| metodo | [[U-Net]] | 32 |
| metrica | [[IoU - mIoU\|IoU / mIoU]] | 20 |
| metrica | [[Kappa]] | 12 |
| tarefa | [[Séries temporais de imagens]] | 1 |
| tarefa | [[Mineração]] | 1 |

## Resultados citados pelos autores (extraídos automaticamente)

> A nivel general los 12 modelos bajo el esquema 1 en el entrenamiento poseen métricas de exactitud (IoU) superiores a 0.98 (TABLA I) mientras que con los datos de validación los modelos disminuyen su exactitud levemente rodeando va
> Con los datos de evaluación los valores en general son buenos los cuales se encuentran entre 0.75 y 0.81 a excepción del modelo 6 el cual obtuvo un IoU de 0.72 esto puede indicar que un modelo con dicha configuración requiere de m
> Id Modelo Entrenamiento Validación Evaluación Loss IoU Loss IoU Loss IoU FPN_3b_100e 0.12 0.99 0.29 0.91 0.46 0.75 FPN_3b_50e 0.14 0.99 0.30 0.90 0.45 0.76 FPN_4b_100e 0.12 0.99 0.32 0.88 0.48 0.75 FPN_4b_50e 0.14 0.99 0.30 0.89 0

*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*

## Chunks

- Arquivo de chunks: [[P05 chunks]] (32 chunks; resumo 15, resultados 17)
- Resumo: [[P05 chunks#^P05_c001|c001]], [[P05 chunks#^P05_c002|c002]]
- Hiperparâmetros / treino: [[P05 chunks#^P05_c014|c014]]
- Resultados numéricos: [[P05 chunks#^P05_c017|c017]], [[P05 chunks#^P05_c018|c018]], [[P05 chunks#^P05_c021|c021]]

## Relações

- Vizinhos por entidades em comum: [[P87 Sadeh 2020|P87]], [[P86 Latte 2020|P86]], [[P85 Wang 2022|P85]], [[P121 Çamalan 2022|P121]]

## Anotações

- 
