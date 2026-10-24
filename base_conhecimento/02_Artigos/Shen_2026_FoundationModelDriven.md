---
tipo: artigo
id_origem: P34
titulo: "Foundation Model-Driven Semantic Change Detection in Remote Sensing Imagery"
ano: 2026
autores: ["Hengtong Shen", "Li Yan", "Hong Xie", "Yaxuan Wei", "Xinhao Li", "Wenfei Shen", "Peixian Lv", "Fei Tan"]
doi: "10.48550/arXiv.2602.13780"
arquivo_fonte: "coleta/P34_Shen2026_Foundation-Model-Driven-Semantic-Change-Detection-in-Remote-.pdf"
markdown_fonte: "output/pdf/P34_Shen2026_Foundation-Model-Driven-Semantic-Change-Detection-in-Remote-/document.md"
paginas: 19
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "B"
tarefas: ["[[MudancaSemantica|Mudança semântica (from–to)]]", "[[Deteccao_Mudanca|Detecção de mudanças]]"]
sensores: []
conjuntos_dados: ["[[SECOND|SECOND]]"]
metodos: ["[[ModeloFundacional|Modelos fundacionais]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/profunda, relevancia/B]
---

# Shen 2026 — Foundation Model-Driven Semantic Change Detection in Remote Sensing Imagery

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **B** — Mudança semântica com modelo fundacional (SECOND, LandsatSCD); arquitetura transferível, não testada em 3–5 m.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Hengtong Shen, Li Yan, Hong Xie, Yaxuan Wei et al. (2026). Foundation Model-Driven Semantic Change Detection in Remote Sensing Imagery. arXiv (Cornell University). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2602.13780
- **Arquivo de origem:** `coleta/P34_Shen2026_Foundation-Model-Driven-Semantic-Change-Detection-in-Remote-.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P34_Shen2026_Foundation-Model-Driven-Semantic-Change-Detection-in-Remote-/document.md` — 19 páginas, 16 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Como acoplar **modelos fundacionais de sensoriamento remoto** à detecção de mudança semântica (SCD, "de-para") sem decodificadores rígidos presos a um backbone, e como estabilizar o treino. Propõe o **PerASCD**: encoder ViT pré-treinado com PerA + ViT-Adapter, o **Cascaded Gated Decoder (CG-Decoder)** com o **Change-Aware Gating Module (CAGM)** e a **Soft Semantic Consistency Loss (SSCLoss)** (p. 1–2, 4–7).

- “Building upon this, we present PerASCD, a robust and unified SCD framework driven by the RS foundation model PerA.” (p. 1, seção Início)
- “Furthermore, we propose a Soft Semantic Consistency Loss (SSCLoss) to mitigate the numerical instability often encountered during the training of large-scale models.” (p. 1, seção Início)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The LandsatSCD is collected between the years 1990 and 2020 in Xinjiang, China.” (p. 8, seção IV. E XPERIMENTS)
- “Patel, “A TransformerBased Siamese Network for Change Detection,” in IGARSS 2022 - 2022 IEEE International Geoscience and Remote Sensing Symposium, Jul.” (p. 17, seção V. C ONCLUSION AND D ISCUSSION)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- **SECOND:** 4.662 pares aéreos 512 × 512, resolução de 0,5 a 3 m, 7 classes (sem mudança, solo não vegetado, árvore, vegetação baixa, água, edifício, quadras); divisão padrão 2.968 treino / 1.694 teste (p. 8).
- **LandsatSCD:** Xinjiang, 1990–2020, **30 m**, 8.468 pares gerados em grande parte por aumento de dados, 2.385 mantidos após filtro; divisão 3:1:1 = 1.431 / 477 / 477; quatro classes (terra agrícola, deserto, edifícios, água) (p. 8).
- Nenhum Planet; nenhum dado de 3–5 m em série temporal. Os dois são bitemporais.

**Detectado automaticamente (verificar):**
- sensor/produto **SAR**: 2 ocorrências (p. 4, 16)
- conjunto de dados **SECOND**: 11 ocorrências (p. 8, 9, 10, 11, 13)
- conjunto de dados **HRSCD**: 5 ocorrências (p. 3, 9, 11)
- resolução mencionada: 3 m (p. 8)
- resolução mencionada: 30 m (p. 8)
- “After filtering, a total of 2,385 image pairs are retained.” (p. 8, seção IV. E XPERIMENTS)
- “Following previous work, we split the dataset into training, validation, and test sets with a ratio of 3:1:1, resulting in 1,431, 477, and 477 image pairs, respectively.” (p. 8, seção IV. E XPERIMENTS)
- “1 - JSTARS-2026-02222 < ## Foundation Model–Driven Semantic Change Detection in Remote Sensing Imagery Hengtong Shen, Li Yan, Hong Xie, Yaxuan Wei, Xinhao Li, Wenfei Shen, Peixian Lv and Fei Tan Abstract —Remote sensing (RS) change detectio” (p. 1, seção Início)
- “Extensive experiments on the SECOND and LandsatSCD benchmarks demonstrate that PerASCD achieves new state-of-the-art SeK scores (26.11% and 65.21%), surpassing the previous best method by 0.61% and 4.95%, respectively, while also exhibiting” (p. 1, seção Início)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 12 ocorrências (p. 1, 2, 5, 8, 9)
- **Correção atmosférica / reflectância**: 5 ocorrências (p. 1, 4, 9, 13, 16)
- **Recorte em patches/tiles**: 4 ocorrências (p. 4, 5, 8)
- **Normalização / escala**: 3 ocorrências (p. 7, 11, 16)
- **Aumento de dados**: 3 ocorrências (p. 8, 11)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Método:**

- **PerA** (pré-treino autossupervisionado que une contraste e MIM) em RSRSD-5M; o backbone é o **ViT-G/16-1024** com pesos oficiais; ViT-Adapter gera 4 escalas (p. 4–5, 8).
- **CG-Decoder:** blocos em cascata, de grosso a fino, processando três fluxos (pré, pós e mudança); compressão de características com CBAM + convolução; fusão de característica rasa e profunda pelo **CAGM** (pesos global × local, sigmoide, fator (1 + W_global) ⊙ W_local) (p. 5–6, eqs. 1–12).
- **SSCLoss:** substitui o hinge de margem da SCLoss por **softplus com temperatura τ**; a hipótese é que o gradiente que liga e desliga na margem causa quedas "em penhasco" com precisão mista (p. 7, eqs. 13–15).
- Treino: PyTorch, RTX 4090, **SGD** momentum 0,9, batch 8, weight decay 1e-5, AMP; lr inicial 0,1 em SECOND e **1,0** (mín. 0,5) em LandsatSCD, decaimento polinomial com aquecimento de 10 %; DropPath 0,3; flips e color jitter; mesmas perdas do SCanNet exceto a SSCLoss (p. 8, 11).

- **Estratégia temporal (detecção automática, verificar):** bitemporal / pares (auto: 12 menções)
**Métodos detectados automaticamente:**
- método/família **Modelo fundacional**: 39 ocorrências (p. 1, 2, 3, 4, 6)
- método/família **Transformer**: 33 ocorrências (p. 3, 4, 5, 8, 9)
- método/família **Mamba**: 12 ocorrências (p. 3, 4, 9, 11, 12)
- método/família **Rede siamesa**: 7 ocorrências (p. 3, 17, 18)
- método/família **CNN**: 6 ocorrências (p. 3, 12)
- método/família **Semi/auto-supervisionado**: 6 ocorrências (p. 2, 3, 4, 5)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate, SSCLoss yields a 10.44% SeK improvement over the ” (p. 2)
- batch: “batch size is set to 8 and the weight decay is set” (p. 8)
- otimizador: “SGD) optimizer with momentum” (p. 8)
- tamanho do patch: “512 × 512 size and is annotated at the pixel” (p. 8)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Teste externo / generalização**: 9 ocorrências (p. 1, 2, 3, 9, 12)
- **Desbalanceamento**: 5 ocorrências (p. 2, 4, 6, 14)
- **Conjuntos treino/val/teste**: 3 ocorrências (p. 7, 8, 9)
- métrica **IoU**: 13 ocorrências (p. 8, 11, 12, 13, 14)
- métrica **Acurácia global**: 12 ocorrências (p. 8, 9, 11, 12, 13)
- métrica **Precisão/Recall**: 12 ocorrências (p. 7, 8, 11, 15, 16)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Métricas e resultados:**

- Métricas: OA, mIoU (média de "sem mudança" e "mudança agregada"), **SeK** e **F_scd** (p. 8, eqs. 16–25).
- **SECOND** (tabela I, p. 11): PerASCD OA 88,70, F_scd 66,41, mIoU 74,33, **SeK 26,11**, contra Mamba-FCS 88,62/65,78/74,07/25,50 e SCanNet 87,57/63,53/73,03/23,18.
- **LandsatSCD:** PerASCD OA 96,84, F_scd 90,90, mIoU 90,54, **SeK 65,21**, contra Mamba-FCS 60,26 e SCanNet 54,77 (p. 11).
- **Troca de backbone** com o CG-Decoder (tabela II, p. 12): ResNet50 SeK 24,63; VMamba-B 25,31; Swin-L 25,40; ViT-L SatMAE 24,51; ViT-L ScaleMAE 24,56; **ResNet50 pré-treinado em SeCo 22,79 (abaixo do SCanNet 23,84)**. O artigo diz que o pré-treino em RS não supera sempre o de ImageNet (p. 12).
- **Custo** (tabela III, p. 13): com ResNet50 o CG-Decoder reduz FLOPs de 263,54 G para 159,34 G; com PerA os parâmetros ficam em ~548 M e 2.853 G de FLOPs; 182,67 ms por par.
- **Ablação** (tabela IV, p. 13): PerASCD com decodificador do SCanNet SeK 25,72; sem CAGM 25,46; **com a SCLoss original 26,07**; PerASCD 26,11. O texto admite que a SSCLoss "não traz melhora substancial" no SECOND; o benefício é estabilidade (p. 13).
- **Eficiência de dados** (tabela V, p. 14): com 50 % dos dados SeK 24,21 e F_scd 64,79, acima do SCanNet com 100 % (23,84 e 64,30). Com 10 %: 19,29 (PerA+CG) vs 18,94 (PerA+SCanNet) vs 15,72 (SCanNet).
- **Instabilidade numérica** (tabela VI, p. 15): com SCLoss em FP16 há quedas independentemente do clipping de gradiente; com SSCLoss (τ = 0,5) e clipping 1,5 o F_scd é 90,90 sem instabilidade, mas sem clipping a instabilidade volta; FP32 não a mostra.
- **Temperatura τ:** LandsatSCD melhor em τ = 0,5 (SeK 65,21); SECOND praticamente plano de 0,005 a 1 (SeK 26,10–26,23; tabelas VII–VIII, p. 15–16).

**Trechos numéricos detectados automaticamente (verificar):**
- “On the challenging SECOND dataset, PerASCD improves the 𝐹 𝑠𝑐𝑑 by 2.88% and the SeK by 2.93% over the baseline SCanNet.” (p. 9, seção 4) Mamba-FCS which is recently published SCD metho)
- “Notably, the superiority in the SeK metric is even more pronounced, with improvements of 0.61% (SECOND) and 4.95% (LandsatSCD) over Mamba-FCS.” (p. 9, seção 4) Mamba-FCS which is recently published SCD metho)
- “Method 𝜏 OA 𝐹 𝑠𝑐𝑑 mIoU SeK PerASCD 0.005 88.30 66.33 74.30 26.17 PerASCD 0.01 88.70 66.41 74.33 26.11 PerASCD 0.02 88.65 66.45 74.45 26.23 PerASCD 0.1 88.34 66.36 74.32 26.21 PerASCD 0.5 88.53 66.33 74.33 26.10 PerASCD 1 88.36 66.32 74.28 26.12” (p. 16, seção 0.01 or 𝜏= 0.02. Since a relatively smaller initia)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites declarados e observações:**

- Os autores listam: τ exige ajuste; custo computacional alto (548 M parâmetros) dificulta borda; **sem teste com SAR–óptico ou LLM** (p. 16).
- **Observações minhas:** (a) o ganho de +0,61 em SECOND sobre o Mamba-FCS é pequeno e vem de **uma só execução com semente fixa** (p. 8), sem desvio ou intervalo; (b) o +4,95 em LandsatSCD ocorre num conjunto em que a maioria dos pares veio de aumento de dados e a divisão 3:1:1 é feita depois dele, com risco de vazamento entre treino e teste que o artigo não discute; (c) a lr de 1,0 e a variação entre 90,48 e 90,90 na tabela VI são do mesmo tamanho do ganho atribuído à SSCLoss; (d) o título de "interpretabilidade" se apoia em mapas de calor do CAGM e numa hipótese dos autores sobre faixas de peso 0,3–0,7 (p. 14), não em teste causal; (e) o texto extraído tem tabelas II, III e V embaralhadas; usei só valores que aparecem de forma consistente em mais de um trecho.
- Os rótulos "-" na tabela I (resultados reproduzidos dos artigos) misturam números copiados e reexecutados (p. 11).


## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- Código: github.com/SathShen/PerASCD (p. 1). Pesos oficiais do PerA citados; hiperparâmetros completos (p. 8, 11).

- **Código/dados:** sim: github.com/SathShen/PerASCD.git (p. 1)
- URL citada: https://github.com/SathShen/PerASCD.git (p. 1)
- declaração: “The code is available at [https://github.com/SathShen/PerASCD.git.](https://github.com/SathShen/PerASCD.git) Index Terms —Foundation model, semantic change detection, modular decoder, remote sensing, deep learning.” (p. 1)
- hiperparâmetros **não detectados** automaticamente: épocas/iterações, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 5 (p. 2, 14, 15, 16); Falsos alertas 2 (p. 8, 14); Quase tempo real 1 (p. 18); Persistência / confirmação 1 (p. 7); Rastreabilidade 1 (p. 8)

**Interpretação — O que reaproveitar:**

- **Troca de backbone sem trocar o decodificador:** o CG-Decoder aceita CNN, Swin, ViT e VMamba; útil para testar encoders pré-treinados sem reescrever a cabeça.
- **Receita de treino estável:** FP32 ou clipping de gradiente quando se usa perda com margem; monitorar quedas em "penhasco" na curva de validação.
- **Métrica F_scd e SeK** com mIoU (já em uso em P36/P28) e a definição de IoU de "mudança agregada".
- **Curva de eficiência de dados (10/50/100 %)** como protocolo para medir quanto rótulo o pré-treino economiza.

**Interpretação — Cuidados para o nosso projeto:**

- Benchmarks de 0,5–3 m e 30 m, **bitemporais**; nenhum teste em 3–5 m nem em séries.
- Backbone de 548 M de parâmetros inviável para treino local sem GPU grande; as variantes ResNet50 ou VMamba-B são o ponto de partida realista (SeK 24,6–25,3 no SECOND).

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- emprega conjunto de dados: [[SECOND|SECOND]] — 11 ocorrências (p. 8, 9, 10, 11, 13)
- utiliza método: [[ModeloFundacional|Modelos fundacionais]] — 39 ocorrências (p. 1, 2, 3, 4, 6)
- trata a tarefa: [[MudancaSemantica|Mudança semântica (from–to)]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[MetricasMudancaSemantica|Métricas de mudança semântica (SeK, SCS, SCOT)]] — suporte vindo da leitura/título/resumo

**Comparações substantivas com outros artigos:**
- este artigo usa a mesma família de encoder de [[Chen_2024_ChangeMambaRemoteSensing|Chen 2024]] — P34 integra o VMamba-B ao seu decodificador (SeK 25,31 no SECOND), a mesma família Mamba de P28 (SeK 22,92 no SECOND).
- [[Li_2024_NewLearningParadigm|Li 2024]] compartilha a abordagem de modelo fundacional com este artigo — P137 congela um modelo fundacional (CLIP) e P34 usa o PerA com decodificador modular; ambos em benchmarks bitemporais.
- [[Szwarcman_2024_PrithviVersatileMultitemporal|Szwarcman 2024]] é modelo fundacional afim a este artigo — P34 testa SatMAE, ScaleMAE e SeCo como encoders; P32 é um encoder multitemporal em HLS de 30 m (interpretação: candidato a encoder, sem teste em mudança).

## Figuras selecionadas

![[Shen_2026_FoundationModelDriven_p4_Fig.2.png|520]]
*Fig. 2. Overall pipeline: (a) PerA Pre-training: A selfsupervised paradigm combining contrastive learning and (p. 4; recorte do PDF convertido)*


## Anotações do leitor

- 
