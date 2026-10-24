---
tipo: artigo
id_origem: P28
titulo: "ChangeMamba: Remote Sensing Change Detection With Spatiotemporal State Space Model"
ano: 2024
autores: ["Hongruixuan Chen", "Jian Hui Song", "Chengxi Han", "Junshi Xia", "Naoto Yokoya"]
doi: "10.48550/arXiv.2404.03425"
arquivo_fonte: "coleta/P28_Chen2024_ChangeMamba-Remote-Sensing-Change-Detection-With-Spatiotempo.pdf"
markdown_fonte: "output/pdf/P28_Chen2024_ChangeMamba-Remote-Sensing-Change-Detection-With-Spatiotempo/document.md"
paginas: 19
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "B"
tarefas: ["[[MudancaSemantica|Mudança semântica (from–to)]]", "[[Deteccao_Mudanca|Detecção de mudanças]]"]
sensores: []
conjuntos_dados: ["[[SECOND|SECOND]]"]
metodos: ["[[RedeSiamesa|Redes siamesas]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/profunda, relevancia/B]
---

# Chen 2024 — ChangeMamba: Remote Sensing Change Detection With Spatiotemporal State Space Model

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **B** — ChangeMamba para mudança binária, semântica e dano; encoder transferível, não testado em 3–5 m.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Hongruixuan Chen, Jian Hui Song, Chengxi Han, Junshi Xia et al. (2024). ChangeMamba: Remote Sensing Change Detection With Spatiotemporal State Space Model. IEEE Transactions on Geoscience and Remote Sensing. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2404.03425
- **Arquivo de origem:** `coleta/P28_Chen2024_ChangeMamba-Remote-Sensing-Change-Detection-With-Spatiotempo.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P28_Chen2024_ChangeMamba-Remote-Sensing-Change-Detection-With-Spatiotempo/document.md` — 19 páginas, 254 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Verificar se a arquitetura **Mamba** (modelo de espaço de estados com varredura 2D) serve para detecção de mudança em imagens ópticas de alta resolução, nas três subtarefas **BCD** (binária), **SCD** (semântica) e **BDA** (avaliação de dano em edifícios). Propõe **MambaBCD, MambaSCD e MambaBDA**, com encoder VMamba compartilhado e um decodificador de mudança com **três mecanismos de modelagem espaço-temporal** (sequencial, cruzado e paralelo) (p. 1–2, 5–8).

- “For the change decoder, which is available in all three architectures, we propose three spatio-temporal relationship modeling mechanisms, which can be naturally combined with the Mamba architecture and fully utilize its attribute to achieve” (p. 1, seção Início)
- “In this paper, we present the first attempt at introducing Mamba architecture for CD tasks and propose several spatiotemporal state space models (collectively called ChangeMamba) to realize effective and robust CD.” (p. 2, seção I. I NTRODUCTION)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “Dataset Study site Number of image pairs Size Resolution Evaluation task SYSU Hong Kong 20,000 256 × 256 0.5m BCD (category-agnostic) LEVIR-CD+ Texas of the U.S.” (p. 9, seção 1 Mamba architectures sometimes are abbreviated as the S6 mo)
- “The aerial images captured in 2012 cover an area of 20.5 km , featuring 12,796 buildings, while the image captured in 2016 shows an increase to 16,077 buildings within the same area, reflecting significant urban development over the four-ye” (p. 9, seção IV. E XPERIMENTS A ND D ISCUSSIONS)
- “Datasets 1) SYSU-CD : This dataset is a category-agnostic CD dataset, which introduces a comprehensive collection of 20,000 pairs of 0.5 meter/pixel resolution aerial images from Hong Kong, spanning 2007 to 2014.” (p. 9, seção IV. E XPERIMENTS A ND D ISCUSSIONS)
- “It comprises two aerial datasets from Christchurch, New Zealand, captured in April 2012 and 2016, with a spatial resolution of 0.3 meters/pixel.” (p. 9, seção IV. E XPERIMENTS A ND D ISCUSSIONS)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- Cinco benchmarks (tabela I, p. 9): **SYSU-CD** (Hong Kong, 20.000 pares 256², 0,5 m, categoria-agnóstico), **LEVIR-CD+** (985 pares 1024², 0,5 m, edifícios), **WHU-CD** (um par de 32.508 × 15.354 px, 0,3 m, edifícios), **SECOND** (4.662 pares 512², 0,5–3 m, SCD) e **xBD** (11.034 pares 1024², < 0,8 m, 15 países, dano em 4 níveis).
- Todos **bitemporais ópticos RGB**; nenhum em 3–5 m, nenhum Planet.

**Detectado automaticamente (verificar):**
- sensor/produto **Imagens aéreas**: 5 ocorrências (p. 9, 18)
- conjunto de dados **xBD**: 11 ocorrências (p. 3, 9, 10, 12, 13)
- conjunto de dados **HRSCD**: 9 ocorrências (p. 10, 13)
- conjunto de dados **LEVIR-CD**: 6 ocorrências (p. 9, 11, 17, 18)
- conjunto de dados **WHU-CD**: 6 ocorrências (p. 9, 11, 12)
- “For effective deep learning application, the dataset is structured into training, validation, and test sets following a 6:2:2 ratio, with 20,000 patches of 256 × 256.” (p. 9, seção IV. E XPERIMENTS A ND D ISCUSSIONS)
- “It can be seen that the proposed methods accurately detect changes with varying types, scales, and numbers contained in these image pairs, very close to the change reference maps.” (p. 11, seção IV. E XPERIMENTS A ND D ISCUSSIONS)
- “Firstly, we can find that the “from-to” transition matrices obtained by our methods are very close to the ground truth, demonstrating the effectiveness of our MambaSCD architecture again.” (p. 12, seção IV. E XPERIMENTS A ND D ISCUSSIONS)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 6 ocorrências (p. 1, 2, 3, 9, 19)
- **Rotulagem / anotação**: 4 ocorrências (p. 3, 9, 12)
- **Normalização / escala**: 3 ocorrências (p. 7, 15)
- **Aumento de dados**: 2 ocorrências (p. 9, 11)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Método:**

- **Encoder:** VMamba de quatro estágios, blocos VSS com módulo SS2D e *cross-scan* em quatro direções, complexidade linear no número de tokens (p. 5–6).
- **Decodificador de mudança:** três mecanismos de interação espaço-temporal combinados (p. 7–8); MambaSCD acrescenta dois decodificadores semânticos de cobertura do solo e deriva o "de-para" mascarando os mapas de cobertura com o mapa binário (p. 5–6). MambaBDA usa um decodificador de localização e um de classificação de dano (p. 6).
- Três tamanhos (Tiny, Small, Base). Treino em PyTorch, **AdamW**, batch 16, recortes **256 × 256**, 20.000 iterações em SYSU e 50.000 nos demais, flips e rotação; inferência no tamanho original (p. 9). O valor numérico da taxa de aprendizado e do weight decay está ilegível na extração; **conferir no PDF**.

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 33 menções vs 10 de pares)
**Métodos detectados automaticamente:**
- método/família **Transformer**: 73 ocorrências (p. 1, 2, 3, 4, 6)
- método/família **Mamba**: 49 ocorrências (p. 1, 2, 4, 5, 6)
- método/família **CNN**: 32 ocorrências (p. 1, 2, 3, 4, 10)
- método/família **Rede siamesa**: 20 ocorrências (p. 2, 3, 5, 10, 14)
- método/família **U-Net**: 12 ocorrências (p. 3, 10, 14, 15, 17)
- método/família **Transfer learning**: 4 ocorrências (p. 2, 18, 19)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 1 e [−] and a weight decay of 5 e [−] ” (p. 9)
- batch: “batch size is set to 16” (p. 9)
- otimizador: “AdamW optimizer with a learning rate of 1 e [” (p. 9)
- perda: “focal loss , deep supervision , multi-scale traini” (p. 8)
- tamanho do patch: “1024 × 1024 pixel” (p. 9)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Conjuntos treino/val/teste**: 8 ocorrências (p. 9, 11, 12, 13, 14)
- **Desbalanceamento**: 3 ocorrências (p. 8)
- métrica **F1**: 25 ocorrências (p. 10, 11, 12, 13, 16)
- métrica **IoU**: 12 ocorrências (p. 10, 11, 12, 13, 16)
- métrica **Acurácia global**: 12 ocorrências (p. 10, 11, 12, 13, 16)
- métrica **Precisão/Recall**: 3 ocorrências (p. 5, 10)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Métricas e resultados:**

- BCD: Rec, Pre, OA, F1, IoU, KC; SCD: OA, F1, mIoU, **SeK**; BDA: F1 de localização, F1 por nível de dano, **F1_overall = 0,3·F1_loc + 0,7·F1_clf** (p. 10).
- **SYSU-CD** (tabela III, p. 10): MambaBCD-Base F1 83,11 e IoU 71,10; Small F1 82,83; melhor CNN/Transformer da lista SwinSUNet F1 81,58.
- **SECOND** (tabela VII, p. 13): MambaSCD-Base SeK **22,92**, F1 55,32 e mIoU 73,68; Small SeK 22,83; Tiny 22,08; SCanNet 21,57; BiSRNet 21,18. O treino é no conjunto de treino e o teste no de teste (nota da tabela).
- **xBD:** MambaBDA supera o DamFormer em +2,64, +4,12 e +4,39 de F1_overall, com ganho vindo da classificação de dano e não da localização (p. 12). "Minor damage" é a classe mais confundida (p. 13).
- **Mecanismos espaço-temporais** (tabela XI, p. 16): sobre a linha de base, SYSU F1 81,11 → 82,83; SECOND SeK 21,15 → 22,83; xBD F1_overall 77,77 → 81,14. Sobre o Transformer: +0,77 de F1, +0,52 de SeK e +1,10 de F1_overall (p. 16). Cada mecanismo isolado dá quase o mesmo (F1 82,17–82,24) e juntos 82,83 (tabela XII).
- **Backbones** (tabela XIII, p. 17): VMamba-Small F1 82,83 vs Swin-Small 82,22 e EfficientNet-B5 82,26.
- **Custo:** MambaBCD-Tiny 17,13 M de parâmetros e 45,74 GFLOPs; Base 84,70 M e 179,32 GFLOPs (tabela VI, p. 13).
- **Robustez a degradação** (LEVIR-CD+, p. 17): com desfoque gaussiano σ de 0 a 2 o F1 do MambaBCD cai 8,73 % contra ~60 % de SiamCRNN-101 e DSIFN; com ruído (σ = 20) cai 8,26 %; mudança de escala para 0,5 cai 12,03 % contra 14,99–16,41 %.


## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites declarados e observações:**

- Trabalho futuro citado: Mamba mais adequado a dados de sensoriamento remoto, **dados multimodais e séries temporais**, modelos fundacionais (p. 18).
- **Observações minhas:** (a) no SECOND o MambaSCD-Tiny e o Base têm OA 90,44 e 90,36 enquanto o Small tem 86,48, com F1 e SeK próximos; é uma discrepância na tabela VII (p. 13) que o texto não explica; (b) os ganhos sobre SCanNet no SECOND são de ~1,3 ponto de SeK e vêm de uma execução por configuração, sem desvio; (c) no SECOND os números de SeK deste artigo (22,9) não são comparáveis a P34 (26,1) sem checar protocolo e divisão; P34 relata SCanNet em 23,18 e 23,84 em lugares diferentes; (d) a avaliação de robustez é só em LEVIR-CD+ e com degradações sintéticas, não com variação real de sensor ou fenologia; (e) o "Mamba é linear" vale em FLOPs/memória; o tempo real de treino não é comparado.


## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- Código aberto: github.com/ChenHongruixuan/MambaCD (p. 1, 9); hiperparâmetros quase completos.

- **Código/dados:** sim: github.com/ChenHongruixuan/MambaCD (p. 1)
- URL citada: https://github.com/ChenHongruixuan/MambaCD (p. 1)
- declaração: “The source code is available in [https://github.com/ChenHongruixuan/MambaCD.](https://github.com/ChenHongruixuan/MambaCD) Index Terms —State space model, Mamba, binary change de- tection, semantic change detection, building damage assessmen” (p. 1)
- declaração: “Type Method Rec Pre OA F1 IoU KC C T FC-EF 71.77 69.12 97.54 70.42 54.34 69.14 FC-Siam-Diff 74.02 81.49 98.26 77.57 63.36 76.67 FC-Siam-Conc 78.49 78.39 98.24 78.44 64.53 77.52 SiamCRNN-18 84.25 81.22 98.56 82.71 70.52 81.96 SiamCRNN-34 83.” (p. 11)
- hiperparâmetros **não detectados** automaticamente: épocas/iterações (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 6 (p. 2, 3, 13, 15, 17)

**Interpretação — O que reaproveitar:**

- **Encoder VMamba** como alternativa de custo linear ao Transformer para tiles grandes ou mosaicos extensos; a família já aparece como backbone em P34 (VMamba-B, SeK 25,31 no SECOND).
- **Derivar o "de-para" de dois mapas de cobertura mascarados pelo mapa binário** (MambaSCD): bom desenho quando há rótulos de cobertura por data.
- **Teste de robustez com desfoque, ruído e escala** como protocolo barato para simular diferenças entre mosaicos Planet (resolução efetiva, ruído).
- **F1_overall 0,3/0,7** como exemplo de métrica composta localização + classificação.

**Interpretação — Cuidados para o nosso projeto:**

- Imagem RGB de 0,3–3 m e pares bitemporais; as bandas NIR e a resolução de 3–5 m não foram testadas.
- Dano em edifícios (xBD) é evento discreto; floresta e estradas têm limites difusos.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- referência (curado pela leitura): [[MudancaSemantica|Mudança semântica (from–to)]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- emprega conjunto de dados: [[SECOND|SECOND]] — 5 ocorrências (p. 9, 12, 13, 14)
- referência (curado pela leitura): [[MetricasMudancaSemantica|Métricas de mudança semântica (SeK, SCS, SCOT)]] — suporte vindo da leitura/título/resumo
- utiliza método: [[RedeSiamesa|Redes siamesas]] — 20 ocorrências (p. 2, 3, 5, 10, 14)

**Comparações substantivas com outros artigos:**
- [[Shen_2026_FoundationModelDriven|Shen 2026]] usa a mesma família de encoder de este artigo — P34 integra o VMamba-B ao seu decodificador (SeK 25,31 no SECOND), a mesma família Mamba de P28 (SeK 22,92 no SECOND).
- este artigo adota a métrica de [[Yang_2021_AsymmetricSiameseNetworks|Yang 2021]] — P28 relata SeK no SECOND, métrica proposta por P19.

## Figuras selecionadas

![[Chen_2024_ChangeMambaRemoteSensing_p6_Fig.2.png|520]]
*Fig. 2: The specific structure of the encoder network is based on the visual state space model used in our three architectures. (p. 6; recorte do PDF convertido)*


## Anotações do leitor

- 
