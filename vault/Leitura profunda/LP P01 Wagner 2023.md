---
tipo: leitura_profunda
paper: "P01"
leitura: "profunda (texto integral, arXiv)"
fonte_lida: "arXiv 2211.09806 (coleta/P01_...pdf); chunks P01_c010–c044"
etapas_pipeline: ["[[E06 Modelos-base de cobertura|E06]]"]
tags: [leitura_profunda, prioridade/alta]
---

# Leitura profunda — P01 Wagner 2023

**Mapping Tropical Forest Cover and Deforestation with Planet NICFI Satellite Images and Deep Learning in Mato Grosso State (Brazil) from 2015 to 2021**

Nota do artigo: [[P01 Wagner 2023|P01 Wagner 2023]] · Chunks: [[P01 chunks]] · Leitura: *profunda (texto integral, arXiv)*

> Leitura feita nesta coleta; valores e afirmações vêm do texto lido, com link para o chunk de origem. O que não foi verificado está marcado.

## Pergunta e escopo
Mapear cobertura arbórea e desmatamento no Mato Grosso (~1 milhão de km²) com mosaicos Planet NICFI (~4,78 m) e uma U-Net, reconstruindo a história do desmatamento 2015–2021 ao comparar a máscara de floresta de cada data. A classificação é feita **data a data**; a mudança vem da diferença entre máscaras.

## Dados
- 2.658 tiles de ~20 × 20 km, 32 datas: semestrais de 2015-12 a 2020-06 e mensais de 2020-09 a 2022-06; 85.056 imagens ([[P01 chunks#^P01_c010|c010]]).
- Bandas R, G, B, NIR em 12 bits. RGB truncado em 0–2540, NIR dividido por 3,937 e tudo reescalado para 8 bits (÷10). **Sem correção atmosférica.** Borda espelhada de 128 px no composto ([[P01 chunks#^P01_c010|c010]]) e 64 px na predição ([[P01 chunks#^P01_c017|c017]]).
- Validação independente: LiDAR aéreo do projeto EBA/INPE (141 faixas de 15 km × 0,5 km, 2016, ≥4 pontos/m²), PRODES (mín. 6,25 ha) e Global Forest Change ([[P01 chunks#^P01_c011|c011]], [[P01 chunks#^P01_c012|c012]]).

## Rótulos (como foram feitos)
1. 10 imagens aleatórias por mosaico mensal de set/2020 a set/2021 → 130; 75 sem nuvem forte; o algoritmo **k-textures** (auto-segmentação não supervisionada, 8 classes) segmentou; 23 imagens aceitas por inspeção visual, com pequenas correções manuais ([[P01 chunks#^P01_c015|c015]]).
2. Primeira U-Net treinada e aplicada às 130; depois 21 imagens com nuvem/neblina fina entram para ensinar o modelo a tratar o que não é reconhecível como não-floresta.
3. Amostra final: 6.663 patches de 256 × 256 (6.187 com floresta, 476 só fundo), 80/20 → 5.331/1.332 ([[P01 chunks#^P01_c016|c016]]).
4. A produção das amostras levou "um par de dias", com mínima supervisão humana ([[P01 chunks#^P01_c043|c043]]).

## Método
- U-Net clássica, entrada 256 × 256 × 4, saída 256 × 256 × 1 (limiar 0,5), 34,6 milhões de parâmetros; R + Keras/TensorFlow 2.8 ([[P01 chunks#^P01_c014|c014]]).
- Treino: Adam, lr 1e-4, perda BCE + Dice, batch 256, 20.000 épocas (melhor: 17.058; acurácia treino/val 99,40/97,70 %), augmentation só com flips H/V, ~12,5 h numa RTX 2080 ([[P01 chunks#^P01_c017|c017]]).
- **Filtro temporal de nuvem:** o pixel é floresta se detectado como floresta em pelo menos metade das observações da janela de ±3 datas; processamento do presente para o passado ([[P01 chunks#^P01_c018|c018]]).
- **Regras de confiança** (`trust` 1 confirmado, 2 muito provável, 3 não confirmado, só para a última data); desmatamento = pixel não-floresta na data N, confirmado quando N−1 e N coincidem ([[P01 chunks#^P01_c019|c019]]).

## Métricas e resultados
- Validação em patches: OA 98,11 %, F1 0,982 (P 0,975, R 0,988) ([[P01 chunks#^P01_c020|c020]]).
- LiDAR: 94 % dos pixels "não-árvore" abaixo de 0,55 m; ~95 % dos "árvore" acima de 5 m (mediana 16,9 m) ([[P01 chunks#^P01_c020|c020]]).
- Cobertura 556.511 km² em 2015 (58,1 % do estado); 141.598 km² perdidos até 2021; desmatamento semestral mínimo 6.632 km² (2016-12), 19.818 km² em 2021-12 ([[P01 chunks#^P01_c022|c022]]).
- Contra o PRODES: 3,39 a 7,49 vezes mais área; interseção mediana por tile 67,2 % (2020); contra o GFC 0,71 a 3,49 vezes ([[P01 chunks#^P01_c025|c025]], [[P01 chunks#^P01_c030|c030]]).

## Limites declarados
- O modelo não compara datas: não vê a "diminuição do número de árvores" e perde degradação sutil ([[P01 chunks#^P01_c038|c038]]).
- O filtro de ±3 datas **atrasa** a data do desmatamento nos anos semestrais; só fica consistente com o PRODES quando a série passa a ser mensal ([[P01 chunks#^P01_c026|c026]], [[P01 chunks#^P01_c035|c035]]).
- Rios, bordas e erros de co-registro viram "desmatamento" nos primeiros anos; floresta caducifólia pode ser detectada como perda quando a série vira mensal ([[P01 chunks#^P01_c041|c041]]).
- Regeneração não é contabilizada; a definição de floresta (FAO) não é reproduzida; o último período tem nuvens residuais ([[P01 chunks#^P01_c038|c038]], [[P01 chunks#^P01_c042|c042]]).
- Discordâncias fortes com PRODES/GFC vêm de **fogo contado como desmatamento** nesses produtos ([[P01 chunks#^P01_c033|c033]]).

## O que reaproveitar
- **Receita de treino pronta para o EXP2:** U-Net 256 × 256 × 4, BCE + Dice, Adam 1e-4, flips, escala 8 bits sem correção atmosférica, borda espelhada na inferência.
- **Cadeia de rotulagem barata:** auto-segmentação por textura + escolha de classes + correção manual, mais amostras de nuvem/neblina como "não-floresta" explícito.
- **Regra de persistência** (a classe não pode ir floresta → não-floresta → floresta) e **nível de confiança por pixel**; ambas migram para a etapa [[E09 Pós-processamento e eventos]].
- **Comparação com produtos oficiais por interseção por tile** ponderada pelo número de pixels, útil para [[E10 Avaliação e incerteza]].
- **Validação com altura LiDAR** como referência independente do próprio rótulo.

## Cuidados para o nosso projeto (mosaicos mensais de 3–5 m)
- Antes de set/2020 os mosaicos NICFI são semestrais; confirmar a cadência real dos nossos arquivos.
- A acurácia de 98 % é de **cobertura arbórea**, não de evento de mudança; medir precisão/recall dos eventos separadamente.
- A área mapeada não é a área estimada; usar amostragem probabilística ([[P46 Olofsson 2014]]).
