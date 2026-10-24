---
tipo: leitura_profunda
paper: "P158"
leitura: "profunda (texto integral, arXiv)"
fonte_lida: "arXiv 2504.18777 (coleta/P158_...pdf); chunks P158_c001–c015"
etapas_pipeline: ["[[E11 Operação e atualização|E11]]"]
tags: [leitura_profunda, prioridade/baixa]
---

# Leitura profunda — P158 Febrita 2025

**Evaluating AI-Driven Automated Map Digitization in QGIS**

Nota do artigo: [[P158 Febrita 2025|P158 Febrita 2025]] · Chunks: [[P158 chunks]] · Leitura: *profunda (texto integral, arXiv)*

> Leitura feita nesta coleta; valores e afirmações vêm do texto lido, com link para o chunk de origem. O que não foi verificado está marcado.

## Pergunta e escopo
Avaliar o **Deepness** (plugin QGIS) na digitalização automática de **edificações** com imagens do Google Earth, comparando com polígonos do OpenStreetMap como referência. É uma avaliação independente e pequena, útil sobretudo pela sensibilidade aos parâmetros do plugin.

## Dados e método
- Área: um bairro residencial na Cumberland Avenue, West Lafayette (Indiana, EUA); **320 edificações do OSM** como verdade; imagens do Google Earth; análise em QGIS e R ([[P158 chunks#^P158_c005|c005]], [[P158 chunks#^P158_c006|c006]]).
- Casamento: IoU > 50 % = verdadeiro positivo; IoU < 50 % ou ausente no OSM = falso positivo; sem detecção = falso negativo; F1 sobre esses contagens ([[P158 chunks#^P158_c006|c006]], [[P158 chunks#^P158_c007|c007]]).
- Parâmetros testados: **resolução** (100 e 300 cm/px), **sobreposição de tiles** (0 % e 12 %; o campo não aceita decimais) e **remover segmentos pequenos** ([[P158 chunks#^P158_c007|c007]]–[[P158 chunks#^P158_c010|c010]]).

## Resultados ([[P158 chunks#^P158_c012|c012]], [[P158 chunks#^P158_c014|c014]])
| Teste | Configuração | Detectadas | TP | FP | FN | Precisão | Recall | F1 |
|---|---|---|---|---|---|---|---|---|
| 1 | 300 cm/px, 0 % de sobreposição | 603 | 222 | 381 | 98 | 36,8 % | 69,4 % | 48,1 % |
| 2 | 300 cm/px, 12 % | 497 | 257 | 240 | 63 | 51,7 % | 80,3 % | 62,9 % |
| 3 | 300 cm/px, 12 %, remover segmentos pequenos | 398 | 282 | 116 | 38 | 70,9 % | 88,1 % | 78,6 % |

- Em 100 cm/px o plugin produziu 2.909 "edificações" contra 776 em 300 cm/px (12 %), com muitos segmentos pequenos ([[P158 chunks#^P158_c007|c007]]).
- A IA detecta mais edificações que o OSM (anexos, galpões) e às vezes divide uma edificação em várias partes ([[P158 chunks#^P158_c012|c012]]).

## Limites (incluindo observações minhas)
- **Uma só vizinhança**, referência do OSM (sem revisão) e imagens do Google Earth; o artigo é um trabalho de curso.
- Inconsistência interna: o texto diz que a remoção de segmentos pequenos deixou **611** edificações ([[P158 chunks#^P158_c009|c009]]), mas a Tabela 2 mostra **398** no teste 3; usei a tabela. As legendas das Figuras 5 e 6 também parecem trocadas.
- Os parâmetros foram escolhidos olhando o F1 na própria área: otimismo.

## O que reaproveitar
- **Lista de parâmetros que alteram muito o resultado** (resolução de processamento, sobreposição, remoção de segmentos pequenos) e a necessidade de **calibrar por área** antes de comparar modelos.
- **Protocolo de casamento por IoU > 0,5** para contagem de edificações e relatório de TP/FP/FN, em linha com o SCOT (IoU > 0,25) de [[P10 Etten 2021]].
- Reforça: **recall alto com precisão média** é adequado para triagem, e a revisão humana corrige os falsos positivos ([[E11 Operação e atualização]]).

## Cuidados
- Resolução de 1–3 m/px nos testes (Google Earth), comparável à escala de 3–5 m do projeto, mas com um modelo de zoo próprio e sem treino em Planet.
