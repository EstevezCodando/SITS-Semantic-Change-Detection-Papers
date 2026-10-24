---
tipo: leitura_profunda
paper: "P19"
leitura: "profunda (texto integral, arXiv)"
fonte_lida: "arXiv 2010.05687 (coleta/P19_...pdf); chunks P19_c014–c045"
etapas_pipeline: ["[[E07 Modelos de mudança em pares|E07]]", "[[E08 Modelos de série temporal|E08]]", "[[E10 Avaliação e incerteza|E10]]"]
tags: [leitura_profunda, prioridade/alta]
---

# Leitura profunda — P19 Yang 2021

**Asymmetric Siamese Networks for Semantic Change Detection in Aerial Images**

Nota do artigo: [[P19 Yang 2021|P19 Yang 2021]] · Chunks: [[P19 chunks]] · Leitura: *profunda (texto integral, arXiv)*

> Leitura feita nesta coleta; valores e afirmações vêm do texto lido, com link para o chunk de origem. O que não foi verificado está marcado.

## Pergunta e escopo
Mudança semântica bitemporal (**SCD**) quando as mudanças são **assimétricas**: o que a imagem 1 mostra (área e escala) difere do que a imagem 2 mostra para o mesmo local. Propõe a **ASN** (rede siamesa assimétrica), o dataset **SECOND** e a métrica **SeK**.

## Formulação
- `f(p) = (0,0)` se a probabilidade de mudança é menor que τ; caso contrário `(l1, l2)` (classe antes, classe depois) ([[P19 chunks#^P19_c014|c014]]).
- A solução intuitiva (segmentar cada data e comparar) assume independência das classes entre as duas datas e **não identifica mudança dentro da mesma classe**; a HRSCD.str4 usa ramos simétricos que não se adaptam a escalas diferentes ([[P19 chunks#^P19_c015|c015]], [[P19 chunks#^P19_c016|c016]]).

## Arquitetura ASN
- Ramos siameses de segmentação + ramo de mudança; módulos **aSP** (pirâmide espacial assimétrica; dilatações {0, 6, 12}) e **aRP** (pirâmide de representação assimétrica; multiplicadores {16, 32, 64}), que combinam pares de features *assimétricos* entre as datas; **ATL** (aprendizado adaptativo de limiar) que reajusta só duas pequenas redes ψ1, ψ2 por 20 épocas com γ = 0,5 (0,4 com Xception) ([[P19 chunks#^P19_c017|c017]], [[P19 chunks#^P19_c018|c018]], [[P19 chunks#^P19_c021|c021]], [[P19 chunks#^P19_c024|c024]], [[P19 chunks#^P19_c034|c034]]).
- Perda: `L = α·CE(M1) + β·CE(M2) + CE(C)`, α = β = 1 ([[P19 chunks#^P19_c023|c023]]).

## Dataset SECOND
- 4.662 pares de imagens aéreas 512 × 512 de várias plataformas e sensores (Hangzhou, Chengdu, Shanghai), anotados por um grupo de especialistas em visão da Terra ([[P19 chunks#^P19_c025|c025]]).
- Formato de anotação (reaproveitável): **par de mapas de cobertura + máscara de não-mudança**. A máscara escurece pixels que não mudam no treino e permite distinguir mudança *entre pixels da mesma classe* ([[P19 chunks#^P19_c026|c026]]).
- 6 classes (superfície não vegetada, árvore, vegetação baixa, água, edificações, quadras/playgrounds) → 30 tipos de mudança incluindo não-mudança; 2.968 pares de treino e 1.694 de teste ([[P19 chunks#^P19_c026|c026]], [[P19 chunks#^P19_c036|c036]]).

## Métricas
- OA e κ são enganosos: modelos que prevêem tudo "sem mudança" recebem notas altas; o κ ainda é dominado pelos pixels de não-mudança ([[P19 chunks#^P19_c027|c027]], [[P19 chunks#^P19_c028|c028]]).
- **mIoU = (IoU1 + IoU2)/2** (IoU1: não-mudança; IoU2: regiões mudadas) e **SeK = e^(IoU2−1) · (ρ̂ − η̂)/(1 − η̂)**, calculado sem a célula `q11` da não-mudança ([[P19 chunks#^P19_c028|c028]], [[P19 chunks#^P19_c029|c029]]).
- Em notas de 11 especialistas, o erro quadrático médio contra a avaliação humana foi 0,003 para SeK, 0,028 para κ e 0,212 para OA ([[P19 chunks#^P19_c029|c029]]).

## Treino e resultados
- SGD, 50 épocas, lr 0,005 com política *poly* (potência 0,9), momentum 0,9, weight decay 1e-4, batch 4, flip + escala aleatória 0,5–2; teste com 6 escalas e flip; 4 GPUs V100; sem pré-treino ([[P19 chunks#^P19_c033|c033]], [[P19 chunks#^P19_c034|c034]]).
- Encoder residual: HRSCD.str4 mIoU 67,5 / SeK 13,7; ASN 69,0 / 15,2; ASN-ATL 69,1 / 15,5 sem TTA e **70,0 / 16,8** com escalas + flip. FC-EF: 59,3 / 5,7; HRSCD.str1: 29,3 / 4,6 ([[P19 chunks#^P19_c033|c033]], [[P19 chunks#^P19_c038|c038]]).
- Ganhos de ASN-ATL sobre HRSCD.str4: +2,1 mIoU e +2,3 SeK; o ganho se repete com Xception e Squeeze-and-Excitation ([[P19 chunks#^P19_c038|c038]], [[P19 chunks#^P19_c041|c041]]).
- Ablação: aSP e aRP contribuem de forma cumulativa; sem os pares assimétricos o desempenho cai (mIoU 68,3 vs 69,7) ([[P19 chunks#^P19_c040|c040]], [[P19 chunks#^P19_c043|c043]], [[P19 chunks#^P19_c044|c044]]).

## O que reaproveitar
- **Formato de anotação** `mapa antes + mapa depois + máscara de não-mudança`, usado diretamente no `change_event` e no `annotation` da arquitetura de dados.
- **SeK + mIoU** para avaliar transições semânticas em [[E10 Avaliação e incerteza]]; nunca OA ou κ isolados.
- **ATL** como remédio barato para limiar descalibrado por desbalanceamento (pode ser reproduzido em qualquer modelo de saída softmax).
- **Taxonomia enxuta** (6 classes → 30 tipos) como teto razoável para as transições.

## Limites e cuidados
- Bitemporal e aéreo (RGB, muito mais fino que Planet). SeK de ~16 mostra que a tarefa continua difícil até em alta resolução.
- Arquitetura pesada (aSP/aRP) e sem pré-treino; o ganho sobre HRSCD.str4 é de ~2 pontos.
