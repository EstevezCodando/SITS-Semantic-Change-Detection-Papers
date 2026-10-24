---
tipo: artigo
id: P38
titulo: "Fully Convolutional Network for Automatic Road Extraction From Satellite Imagery"
autores: "Alexander Pavlovich Buslaev, Selim Seferbekov, Vladimir Iglovikov, Alexey A. Shvets"
ano: 2018
secao: D
categoria: "Vias, redes viárias e cartografia prévia"
tipo_publicacao: "Artigo"
papel: ["vias e cartografia"]
prioridade: baixa
doi: "10.1109/cvprw.2018.00035"
pdf: "coleta/P38_Buslaev2018_Fully-Convolutional-Network-for-Automatic-Road-Extraction-Fr.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 11
sensores: []
tarefas: ["[[Vias-estradas|Vias/estradas]]"]
metodos: ["[[U-Net]]", "[[ResNet]]", "[[FCN]]"]
datasets: ["[[DeepGlobe]]"]
metricas: ["[[IoU - mIoU|IoU / mIoU]]"]
ferramentas: []
etapas_pipeline: ["[[E09 Pós-processamento e eventos|E09]]"]
status_leitura: não lido
tags: [artigo, secao/D, prioridade/baixa, etapa/E09]
---

# P38 — Fully Convolutional Network for Automatic Road Extraction From Satellite Imagery

**Alexander Pavlovich Buslaev, Selim Seferbekov, Vladimir Iglovikov** · 2018 · Artigo · IEEE · [publicação](https://openaccess.thecvf.com/content_cvpr_2018_workshops/w4/html/Buslaev_Fully_Convolutional_Network_CVPR_2018_paper.html) · [PDF](../../coleta/P38_Buslaev2018_Fully-Convolutional-Network-for-Automatic-Road-Extraction-Fr.pdf)

Seção: **Vias, redes viárias e cartografia prévia** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Uso proposto:** baseline de máscara de vias, depois combinável entre datas.
- **Receita de treino extraída:** taxa de aprendizado — `learning rate 1e-4 and decay 1e-4 [9]`; batch size — `batch size of 8 images`; otimizador — `Adam optimizer with learning rate 1e-4 and d`; função de perda — `binary cross entropy, while for a multi-class segmen`; tamanho do patch — `1024x1024 pixel` (confirmar nos chunks).
- **Métricas usadas:** [[IoU - mIoU|IoU / mIoU]]
- **Dados/benchmarks citados:** [[DeepGlobe]]

## Método e dados (da revisão original)

- **Método:** rede da família U-Net para extração viária no DeepGlobe.

## Limites e cuidados

- pixel de via em duas datas não basta para diferenciar abertura, pavimentação e alteração de iluminação.

## Contextos de uso no projeto

- Etapas do pipeline: [[E09 Pós-processamento e eventos|E09]]
- Tarefas: [[Vias-estradas|Vias/estradas]]
- Métodos: [[U-Net]], [[ResNet]], [[FCN]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| dataset | [[DeepGlobe]] | 1 |
| metodo | [[U-Net]] | 13 |
| metodo | [[ResNet]] | 4 |
| metodo | [[FCN]] | 3 |
| metrica | [[IoU - mIoU\|IoU / mIoU]] | 3 |
| tarefa | [[Vias-estradas\|Vias/estradas]] | 15 |

## Chunks

- Arquivo de chunks: [[P38 chunks]] (11 chunks; resumo 2, introdução 2, dados 1, métodos 2, experimentos 3, conclusão 1)
- Resumo: [[P38 chunks#^P38_c001|c001]], [[P38 chunks#^P38_c002|c002]]
- Dados / área de estudo: [[P38 chunks#^P38_c005|c005]]
- Método: [[P38 chunks#^P38_c006|c006]], [[P38 chunks#^P38_c007|c007]]
- Hiperparâmetros / treino: [[P38 chunks#^P38_c005|c005]], [[P38 chunks#^P38_c009|c009]], [[P38 chunks#^P38_c010|c010]]

## Relações

- Vizinhos por entidades em comum: [[P25 Chen 2021|P25]], [[P100 Crato 2025|P100]]

## Anotações

- 
