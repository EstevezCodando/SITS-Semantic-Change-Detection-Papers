---
tipo: artigo
id: P179
titulo: "Advancing Earth Observation Through Machine Learning: A TorchGeo Tutorial"
autores: "Caleb Robinson, Nils Lehmann, Adam J. Stewart, Burak Ekim"
ano: 2026
secao: N
categoria: "GeoAI e QGIS"
tipo_publicacao: "Software"
papel: ["GeoAI/QGIS", "ferramenta"]
prioridade: baixa
doi: "10.48550/arXiv.2603.02386"
pdf: "coleta/P179_Robinson2026_Advancing-Earth-Observation-Through-Machine-Learning-A-Torch.pdf"
texto_integral: sim
fonte_analise: "texto integral (PDF) + metadados"
n_chunks: 11
sensores: ["[[Sentinel-2]]"]
tarefas: []
metodos: []
datasets: []
metricas: ["[[IoU - mIoU|IoU / mIoU]]"]
ferramentas: ["[[TorchGeo]]", "[[PyTorch]]"]
etapas_pipeline: ["[[E11 Operação e atualização|E11]]"]
status_leitura: não lido
tags: [artigo, secao/N, prioridade/baixa, etapa/E11]
---

# P179 — Advancing Earth Observation Through Machine Learning: A TorchGeo Tutorial

**Caleb Robinson, Nils Lehmann, Adam J. Stewart** · 2026 · Software · arXiv (Cornell University) · [publicação](https://doi.org/10.48550/arXiv.2603.02386) · [PDF](../../coleta/P179_Robinson2026_Advancing-Earth-Observation-Through-Machine-Learning-A-Torch.pdf)

Seção: **GeoAI e QGIS** · Prioridade: **baixa** · Análise: *texto integral (PDF) + metadados*

## O que reaproveitar

- **Relevância:** Tutorial de TorchGeo para observação da Terra com aprendizado de máquina.
- **Código:** https://github.com/torchgeo/torchgeo · https://github.com/pytorch/vision.
- **Receita de treino extraída:** taxa de aprendizado — `learning rate of 0.0001, and achieves an overall accuracy of 0.97`; épocas — `10 epochs`; otimizador — `AdamW optimizer with a learning rate of 0` (confirmar nos chunks).
- **Métricas usadas:** [[IoU - mIoU|IoU / mIoU]]

## Limites e cuidados

- Conferir resolução, bandas, região e rótulos antes de transferir resultados; síntese baseada em registro e metadados.

## Contextos de uso no projeto

- Etapas do pipeline: [[E11 Operação e atualização|E11]]
- Sensores/produtos: [[Sentinel-2]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| sensor | [[Sentinel-2]] | 10 |
| metrica | [[IoU - mIoU\|IoU / mIoU]] | 4 |
| ferramenta | [[TorchGeo]] | 18 |
| ferramenta | [[PyTorch]] | 10 |

## Chunks

- Arquivo de chunks: [[P179 chunks]] (11 chunks; resumo 11)
- Resumo: [[P179 chunks#^P179_c001|c001]], [[P179 chunks#^P179_c002|c002]]
- Hiperparâmetros / treino: [[P179 chunks#^P179_c010|c010]], [[P179 chunks#^P179_c011|c011]]

## Relações

- Vizinhos por entidades em comum: [[P73 Trujillo 2026|P73]], [[P147 Basavaraju 2022|P147]], [[P86 Latte 2020|P86]], [[P121 Çamalan 2022|P121]]

## Anotações

- 
