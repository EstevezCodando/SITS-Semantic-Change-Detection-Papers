---
tipo: artigo
id: P156
titulo: "Deepness: Deep neural remote sensing plugin for QGIS"
autores: "Przemysław Aszkowski, Bartosz Ptak, Marek Kraft, Dominik Pieczyński"
ano: 2023
secao: N
categoria: "GeoAI e QGIS"
tipo_publicacao: "Software"
papel: ["GeoAI/QGIS", "ferramenta"]
prioridade: alta
doi: "10.1016/j.softx.2023.101495"
pdf: ""
texto_integral: nao
fonte_analise: "apenas metadados e comentário (sem PDF)"
n_chunks: 0
sensores: []
tarefas: []
metodos: []
datasets: []
metricas: []
ferramentas: ["[[QGIS]]"]
etapas_pipeline: ["[[E11 Operação e atualização|E11]]"]
leitura_profunda: "[[LP P156 Aszkowski 2023]]"
status_leitura: lido (parcial)
tags: [artigo, secao/N, prioridade/alta, etapa/E11]
---

# P156 — Deepness: Deep neural remote sensing plugin for QGIS

**Przemysław Aszkowski, Bartosz Ptak, Marek Kraft** · 2023 · Software · SoftwareX · [publicação](https://doi.org/10.1016/j.softx.2023.101495) · PDF indisponível em coleta/

Seção: **GeoAI e QGIS** · Prioridade: **alta** · Análise: *apenas metadados e comentário (sem PDF)*

> [!success] Leitura parcial concluída: [[LP P156 Aszkowski 2023]]

## O que reaproveitar

- **Rota de implantação:** exportar nossa U-Net (EXP2) para **ONNX** e rodá-la no QGIS com o Deepness para a revisão humana, usando a exportação de tiles de treino como ponte. (Hipótese: precisa conferir como o plugin trata entradas de 4 bandas.)
- **Parâmetros que precisam ser reportados em qualquer experimento com plugin:** resolução de processamento, % de sobreposição e remoção de segmentos pequenos.
- **Model zoo como baseline gratuito** para estradas e edificações antes de treinar, desde que se meça o desempenho local.

### Extraído automaticamente

- **Relevância:** Deepness: plugin QGIS que executa modelos ONNX de segmentação, detecção e regressão em camadas raster.
- **Código:** https://github.com/PUTvision/qgis-plugin-deepness

## Limites e cuidados

- Conferir resolução, bandas, região e rótulos antes de transferir resultados; síntese baseada em registro e metadados.

## Contextos de uso no projeto

- Etapas do pipeline: [[E11 Operação e atualização|E11]]

## Entidades detectadas

| Categoria | Entidade | Ocorrências |
|---|---|---:|
| ferramenta | [[QGIS]] | 2 |

## Chunks

- Sem PDF em `coleta/` (acesso restrito ou bloqueado); chunking indisponível. Use o link da publicação.

## Relações


## Anotações

- 
