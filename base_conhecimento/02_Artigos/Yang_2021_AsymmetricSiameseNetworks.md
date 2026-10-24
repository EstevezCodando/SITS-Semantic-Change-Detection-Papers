---
tipo: artigo
id_origem: P19
titulo: "Asymmetric Siamese Networks for Semantic Change Detection in Aerial Images"
ano: 2021
autores: ["Kunping Yang", "Gui-Song Xia", "Zicheng Liu", "Bo Du", "Yang Wen", "Marcello Pelillo", "Liangpei Zhang"]
doi: "10.48550/arXiv.2010.05687"
arquivo_fonte: "coleta/P19_Yang2020_Asymmetric-Siamese-Networks-for-Semantic-Change-Detection-in.pdf"
markdown_fonte: "output/pdf/P19_Yang2020_Asymmetric-Siamese-Networks-for-Semantic-Change-Detection-in/document.md"
paginas: 14
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "B"
tarefas: ["[[MudancaSemantica|Mudança semântica (from–to)]]"]
sensores: []
conjuntos_dados: ["[[HRSCD|HRSCD]]", "[[SECOND|SECOND]]"]
metodos: ["[[RedeSiamesa|Redes siamesas]]"]
preparo: []
validacao: ["[[Desbalanceamento|Desbalanceamento de classes]]"]
ferramentas: []
tags: [artigo, leitura/profunda, relevancia/B]
---

# Yang 2021 — Asymmetric Siamese Networks for Semantic Change Detection in Aerial Images

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **B** — SECOND e a métrica SeK para mudança semântica (aéreo bitemporal).

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Kunping Yang, Gui-Song Xia, Zicheng Liu, Bo Du et al. (2021). Asymmetric Siamese Networks for Semantic Change Detection in Aerial Images. arXiv (Cornell University). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2010.05687
- **Arquivo de origem:** `coleta/P19_Yang2020_Asymmetric-Siamese-Networks-for-Semantic-Change-Detection-in.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P19_Yang2020_Asymmetric-Siamese-Networks-for-Semantic-Change-Detection-in/document.md` — 14 páginas, 12 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Mudança semântica bitemporal (**SCD**) quando as mudanças são **assimétricas**: o que a imagem 1 mostra (área e escala) difere do que a imagem 2 mostra para o mesmo local. Propõe a **ASN** (rede siamesa assimétrica), o dataset **SECOND** e a métrica **SeK**.

- “In this paper, we present an asymmetric siamese network (ASN) to locate and identify semantic changes through feature pairs obtained from modules of widely different structures, which involve areas of various sizes and apply different quant” (p. 1, seção Início)
- “In this article, we address the asymmetric properties of SCD problem by exploiting siamese networks.” (p. 2, seção I. I NTRODUCTION)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “Townshend, “Global land change from 1982 to 2016,” Nature, vol.” (p. 14, seção VII. C ONCLUSION)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- 4.662 pares de imagens aéreas 512 × 512 de várias plataformas e sensores (Hangzhou, Chengdu, Shanghai), anotados por um grupo de especialistas em visão da Terra (p. 6).
- Formato de anotação (reaproveitável): **par de mapas de cobertura + máscara de não-mudança**. A máscara escurece pixels que não mudam no treino e permite distinguir mudança *entre pixels da mesma classe* (p. 6).
- 6 classes (superfície não vegetada, árvore, vegetação baixa, água, edificações, quadras/playgrounds) → 30 tipos de mudança incluindo não-mudança; 2.968 pares de treino e 1.694 de teste (p. 6, 9).

**Detectado automaticamente (verificar):**
- sensor/produto **Imagens aéreas**: 6 ocorrências (p. 1, 6, 14)
- conjunto de dados **HRSCD**: 35 ocorrências (p. 4, 7, 8, 9, 10)
- conjunto de dados **SECOND**: 7 ocorrências (p. 2, 3, 6, 7, 9)
- “Moreover, as illustrated in Fig.11, samples of feature maps in ASN are more likely to contain distinguishable response values in changed regions compared with HRSCD.str4.” (p. 12, seção Methods)
- “HANGE detection in multi-temporal aerial images , # C , , , , which aims to locate and analyze the regions of land-cover variations on the earth surface, is a crucial image interpretation task related to many applications such as, precise u” (p. 1, seção I. I NTRODUCTION)
- “However, these models often fail to consider issues such as multi-scale objects or scenes of various complexities in the interpretation process.” (p. 3, seção II. R ELATED W ORK)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 17 ocorrências (p. 1, 2, 3, 5, 6)
- **Normalização / escala**: 5 ocorrências (p. 4, 5, 12)
- **Segmentação em objetos**: 3 ocorrências (p. 3, 14)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Formulação:**

- `f(p) = (0,0)` se a probabilidade de mudança é menor que τ; caso contrário `(l1, l2)` (classe antes, classe depois) (p. 3).
- A solução intuitiva (segmentar cada data e comparar) assume independência das classes entre as duas datas e **não identifica mudança dentro da mesma classe**; a HRSCD.str4 usa ramos simétricos que não se adaptam a escalas diferentes (p. 4).

**Evidência (leitura) — Arquitetura ASN:**

- Ramos siameses de segmentação + ramo de mudança; módulos **aSP** (pirâmide espacial assimétrica; dilatações {0, 6, 12}) e **aRP** (pirâmide de representação assimétrica; multiplicadores {16, 32, 64}), que combinam pares de features *assimétricos* entre as datas; **ATL** (aprendizado adaptativo de limiar) que reajusta só duas pequenas redes ψ1, ψ2 por 20 épocas com γ = 0,5 (0,4 com Xception) (p. 4, 5, 8).
- Perda: `L = α·CE(M1) + β·CE(M2) + CE(C)`, α = β = 1 (p. 5).

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 20 menções vs 4 de pares)
**Métodos detectados automaticamente:**
- método/família **Rede siamesa**: 41 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **CNN**: 4 ocorrências (p. 14)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate is set as 0.005 and ’poly’ policy is employed with” (p. 8)
- épocas/iterações: “50 epochs” (p. 8)
- tamanho do patch: “512 × 512 and is annotated at the pixel” (p. 6)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Evidência (leitura) — Métricas:**

- OA e κ são enganosos: modelos que prevêem tudo "sem mudança" recebem notas altas; o κ ainda é dominado pelos pixels de não-mudança (p. 6).
- **mIoU = (IoU1 + IoU2)/2** (IoU1: não-mudança; IoU2: regiões mudadas) e **SeK = e^(IoU2−1) · (ρ̂ − η̂)/(1 − η̂)**, calculado sem a célula `q11` da não-mudança (p. 6).
- Em notas de 11 especialistas, o erro quadrático médio contra a avaliação humana foi 0,003 para SeK, 0,028 para κ e 0,212 para OA (p. 6).

**Detectado automaticamente (verificar):**
- **Desbalanceamento**: 14 ocorrências (p. 1, 2, 3, 5, 6)
- **Teste externo / generalização**: 6 ocorrências (p. 2, 3, 10, 11, 12)
- métrica **Acurácia global**: 13 ocorrências (p. 2, 3, 6, 7)
- métrica **Kappa**: 8 ocorrências (p. 1, 2, 6)
- métrica **Matriz de confusão**: 6 ocorrências (p. 6, 10)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Treino e resultados:**

- SGD, 50 épocas, lr 0,005 com política *poly* (potência 0,9), momentum 0,9, weight decay 1e-4, batch 4, flip + escala aleatória 0,5–2; teste com 6 escalas e flip; 4 GPUs V100; sem pré-treino (p. 8).
- Encoder residual: HRSCD.str4 mIoU 67,5 / SeK 13,7; ASN 69,0 / 15,2; ASN-ATL 69,1 / 15,5 sem TTA e **70,0 / 16,8** com escalas + flip. FC-EF: 59,3 / 5,7; HRSCD.str1: 29,3 / 4,6 (p. 8, 10).
- Ganhos de ASN-ATL sobre HRSCD.str4: +2,1 mIoU e +2,3 SeK; o ganho se repete com Xception e Squeeze-and-Excitation (p. 10, 12).
- Ablação: aSP e aRP contribuem de forma cumulativa; sem os pares assimétricos o desempenho cai (mIoU 68,3 vs 69,7) (p. 12, 13).

**Trechos numéricos detectados automaticamente (verificar):**
- “Moreover, the Mean Square Error (MSE) between SeK and human scores is 0.003.” (p. 6, seção 0.23 in κ, which is too high compared with human s)
- “OA and κ are 0.212 and 0.028 respectively, which further validates the rationality of SeK.” (p. 6, seção 0.23 in κ, which is too high compared with human s)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites e cuidados:**

- Bitemporal e aéreo (RGB, muito mais fino que Planet). SeK de ~16 mostra que a tarefa continua difícil até em alta resolução.
- Arquitetura pesada (aSP/aRP) e sem pré-treino; o ganho sobre HRSCD.str4 é de ~2 pontos.


## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado
- hiperparâmetros **não detectados** automaticamente: batch, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 

**Interpretação — O que reaproveitar:**

- **Formato de anotação** `mapa antes + mapa depois + máscara de não-mudança`, usado diretamente no `change_event` e no `annotation` da arquitetura de dados.
- **SeK + mIoU** para avaliar transições semânticas em E10 Avaliação e incerteza; nunca OA ou κ isolados.
- **ATL** como remédio barato para limiar descalibrado por desbalanceamento (pode ser reproduzido em qualquer modelo de saída softmax).
- **Taxonomia enxuta** (6 classes → 30 tipos) como teto razoável para as transições.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- emprega conjunto de dados: [[HRSCD|HRSCD]] — 35 ocorrências (p. 4, 7, 8, 9, 10)
- emprega conjunto de dados: [[SECOND|SECOND]] — 7 ocorrências (p. 2, 3, 6, 7, 9)
- trata a tarefa: [[MudancaSemantica|Mudança semântica (from–to)]] — suporte vindo da leitura/título/resumo
- utiliza método: [[RedeSiamesa|Redes siamesas]] — 41 ocorrências (p. 1, 2, 3, 4, 5)
- referencia (suporte manual da leitura): [[MetricasMudancaSemantica|Métricas de mudança semântica (SeK, SCS, SCOT)]] — suporte vindo da leitura/título/resumo
- adota desenho de validação: [[Desbalanceamento|Desbalanceamento de classes]] — 14 ocorrências (p. 1, 2, 3, 5, 6)

**Comparações substantivas com outros artigos:**
- este artigo compara-se com e critica [[Daudt_2019_MultitaskLearningLarge|Daudt 2019]] — P19 supera HRSCD.str4 (P18): (p. 10); e critica a simetria: (p. 4).
- [[Daudt_2019_MultitaskLearningLarge|Daudt 2019]] têm datasets complementares este artigo — HRSCD (aéreo, Urban Atlas) e SECOND (aéreo, anotação por especialistas) são benchmarks bitemporais de mudança semântica.
- [[Chen_2024_ChangeMambaRemoteSensing|Chen 2024]] adota a métrica de este artigo — P28 relata SeK no SECOND, métrica proposta por P19.

## Figuras selecionadas

![[Yang_2021_AsymmetricSiameseNetworks_p7_Fig.6.png|520]]
*Fig. 6. Comparison between SeK and other metrics. SeK alleviates the influence of label imbalance caused by non-change pixels and shows most (p. 7; recorte do PDF convertido)*


## Anotações do leitor

- 
