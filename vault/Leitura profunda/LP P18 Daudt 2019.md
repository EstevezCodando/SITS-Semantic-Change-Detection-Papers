---
tipo: leitura_profunda
paper: "P18"
leitura: "profunda (texto integral, arXiv)"
fonte_lida: "arXiv 1810.08452 (coleta/P18_...pdf); chunks P18_c014–c047"
etapas_pipeline: ["[[E07 Modelos de mudança em pares|E07]]", "[[E08 Modelos de série temporal|E08]]"]
tags: [leitura_profunda, prioridade/alta]
---

# Leitura profunda — P18 Daudt 2019

**Multitask Learning for Large-scale Semantic Change Detection**

Nota do artigo: [[P18 Daudt 2019|P18 Daudt 2019]] · Chunks: [[P18 chunks]] · Leitura: *profunda (texto integral, arXiv)*

> Leitura feita nesta coleta; valores e afirmações vêm do texto lido, com link para o chunk de origem. O que não foi verificado está marcado.

## Pergunta e escopo
Como obter, numa mesma rede, **onde** houve mudança e **de qual classe para qual classe**, e um dataset de larga escala (HRSCD) para treinar isso de forma supervisionada. Compara quatro estratégias de mudança semântica.

## Dados e rótulos (HRSCD)
- 291 pares RGB de 10.000 × 10.000 px, mosaicos aéreos do IGN (BD ORTHO, 0,5 m): imagens de 2005/2006 e 2012, regiões de Rennes e Caen ([[P18 chunks#^P18_c016|c016]]).
- Rótulos vindos do **Urban Atlas** (Copernicus/EEA) de 2006 e 2012 e do mapa de mudança: rasterizados e alinhados às imagens; nível hierárquico L1 com 5 classes (artificial, agrícola, florestas, áreas úmidas, água) mais "sem informação" ([[P18 chunks#^P18_c018|c018]], [[P18 chunks#^P18_c019|c019]]).
- Rótulos não são perfeitos: precisão mínima garantida de 80–85 % por classe; um único rótulo por parcela gera **bordas imprecisas e mudanças superestimadas** ([[P18 chunks#^P18_c020|c020]], [[P18 chunks#^P18_c021|c021]]).
- **Desbalanceamento extremo:** 99,232 % dos pixels sem mudança; a maior classe de mudança (agrícola → artificial) é 0,653 %; todas as outras somam 0,115 % ([[P18 chunks#^P18_c021|c021]]).
- Níveis hierárquicos mais finos que L1 foram evitados: o número de transições cresce com o quadrado das classes ([[P18 chunks#^P18_c023|c023]]).

## Quatro estratégias
1. **Comparar mapas de cobertura** previstos em cada data (mais simples; erros dos dois mapas se somam).
2. **Mudança semântica direta**: cada par from–to vira uma classe (cresce com N²).
3. **CD e LCM separados:** uma rede de mudança binária mascara os dois mapas de cobertura.
4. **Rede integrada multitarefa:** dois ramos de cobertura com pesos compartilhados e um ramo de mudança com *difference skip connections* ([[P18 chunks#^P18_c026|c026]], [[P18 chunks#^P18_c030|c030]], [[P18 chunks#^P18_c032|c032]]).
   - 4.1: perda ponderada `L_CD + λ·L_LCM` (λ = 0,05), exige busca em grade.
   - **4.2: treino sequencial** — primeiro só a cobertura; depois o ramo de mudança com os pesos da cobertura congelados ([[P18 chunks#^P18_c034|c034]], [[P18 chunks#^P18_c035|c035]]).

## Treino e métricas
- Rede FC-EF-Res (blocos residuais em encoder–decoder, extensão do FC-EF); no OSCD melhora o Dice RGB de 48,89 (FC-EF) para 59,20 e o multiespectral de 56,91 para 60,15 ([[P18 chunks#^P18_c024|c024]], [[P18 chunks#^P18_c038|c038]]).
- HRSCD: 146 pares para treino e 145 para teste (nenhum pixel de teste visto no treino); pesos de classe inversos à frequência; 3–5 h por modelo numa GTX 1080 Ti; inferência < 0,04 s por par 512² ([[P18 chunks#^P18_c037|c037]]).
- **A acurácia global é inadequada** (só reflete a classe "sem mudança"); usar kappa e Dice ([[P18 chunks#^P18_c022|c022]]).

## Resultados (HRSCD, kappa de mudança)
| Estratégia | Kappa CD | Dice CD | Kappa cobertura |
|---|---|---|---|
| 1 comparar mapas | 3,99 | 5,56 | 71,92 |
| 2 direta | 21,54 | — | — |
| 3 separadas | 12,48 | 13,79 | 71,92 |
| 4.1 integrada (λ) | 19,13 | 20,23 | 67,25 |
| **4.2 sequencial** | **25,49** | **26,33** | 71,81 |

- A estratégia 2 acerta *onde* mas prevê sempre o mesmo tipo de mudança (sem semântica) ([[P18 chunks#^P18_c039|c039]]).
- Métodos clássicos (PCA + k-means, diferença de features VGG) ficam abaixo de kappa 3,3 ([[P18 chunks#^P18_c045|c045]]).
- Reduzir os dados de treino para ½ e ¼ baixa o kappa de 25,49 para 23,34 e 22,18 ([[P18 chunks#^P18_c044|c044]]).
- Crítica ao teste com pixels aleatórios (lago Eppalock): vizinhos redundantes causam overfitting ([[P18 chunks#^P18_c045|c045]], [[P18 chunks#^P18_c046|c046]]).

## O que reaproveitar
- **Estratégia 4.2** como desenho de referência para o EXP4 (modelo semântico conjunto), sem busca de λ.
- **Pesos de classe inversos à frequência** e **kappa/Dice** (nunca OA) para mudança rara.
- **Rotular `mudança` como parcela inteira gera superestimação de borda**: avaliar sempre com tolerância espacial.
- **Hierarquia de classes** (comece em 5–6 classes) e controle do crescimento quadrático de transições.
- **Partição por pares/áreas**, nunca por pixels.

## Limites e cuidados
- Aéreo RGB de 0,5 m e rótulos de mapas vetoriais, longe de Planet 3–5 m; **não transferir os números**.
- Ruído de rótulo, paralaxe e datas de aquisição incertas.
