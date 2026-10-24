---
tipo: artigo
id_origem: P36
titulo: "RB-SCD: A New Benchmark for Semantic Change Detection of Roads and Bridges in Traffic Scenes"
ano: 2025
autores: ["Qinji Shu", "Si-Bao Chen", "Xiao Wang", "Zhihui You", "Wei Lu", "Jin Long Tang", "Bin Luo"]
doi: "10.48550/arXiv.2505.13212"
arquivo_fonte: "coleta/P36_Shu2026_RB-SCD-A-New-Benchmark-for-Semantic-Change-Detection-of-Road.pdf"
markdown_fonte: "output/pdf/P36_Shu2026_RB-SCD-A-New-Benchmark-for-Semantic-Change-Detection-of-Road/document.md"
paginas: 35
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[MudancaSemantica|Mudança semântica (from–to)]]", "[[Edificacoes|Edificações e urbanização]]", "[[Vias|Vias e estradas]]"]
sensores: ["[[Landsat|Landsat]]"]
conjuntos_dados: ["[[LEVIRCD|LEVIR-CD]]", "[[WHUCD|WHU-CD]]", "[[HRSCD|HRSCD]]"]
metodos: ["[[CNN|Redes convolucionais (CNN)]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]", "[[PatchesTiles|Recorte em patches/tiles]]", "[[AumentoDados|Aumento de dados]]"]
validacao: ["[[Desbalanceamento|Desbalanceamento de classes]]", "[[Generalizacao|Generalização e domain shift]]", "[[DivisaoTreinoTeste|Divisão treino/validação/teste]]", "[[IoU|IoU / mIoU]]", "[[F1|F1]]", "[[PrecisaoRecall|Precisão e recall]]"]
ferramentas: []
tags: [artigo, leitura/profunda]
---

# Shu 2025 — RB-SCD: A New Benchmark for Semantic Change Detection of Roads and Bridges in Traffic Scenes

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Qinji Shu, Si-Bao Chen, Xiao Wang, Zhihui You et al. (2025). RB-SCD: A New Benchmark for Semantic Change Detection of Roads and Bridges in Traffic Scenes. Pattern Recognition. Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2505.13212
- **Arquivo de origem:** `coleta/P36_Shu2026_RB-SCD-A-New-Benchmark-for-Semantic-Change-Detection-of-Road.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P36_Shu2026_RB-SCD-A-New-Benchmark-for-Semantic-Change-Detection-of-Road/document.md` — 35 páginas, 214 recortes de figuras, 1 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Detectar **mudança semântica de estradas e pontes** (estruturas lineares, continuidade, confusão entre "estrada nova" e "solo exposto"), com dois aportes: o dataset **RB-SCD** (11 categorias de mudança semântica de/para) e o detector **MFDCD** (*Multimodal Frequency-Driven Change Detector*), que opera no **domínio da frequência** com características visuais (wavelet) e textuais (CLIP + Fourier) (p. 1–5).

**Resumo detectado automaticamente (p. 1):** Accurate detection of road and bridge changes is crucial for urban planning and trans portation management, yet presents unique challenges for general change detection (CD). Key difficulties arise from maintaining the continuity of roads and bridges as lin ear structures and disambiguating visually similar land covers (e.g., road construction vs. bare land). Existing spatial-domain models struggle with these issues, further hin dered by the lack of specialized, semantically rich datasets. To fill these gaps, we intro duce the Road and Bridge Semantic Change Detection (RB-SCD) dataset. As the first benchmark to systematically target semantic change detection of roads and bridges, RB-SCD offers comprehensive fine-grained annotations for 11 semantic change cat egories. This enables a detailed analysis of traffic infrastructure evolution. Building on this, we propose a novel framework, the M…

- “Building on this, we propose a novel framework, the Multimodal Frequency-Driven Change Detector (MFDCD).” (p. 1, seção Abstract)
- “Second, we propose a novel M ultimodal F requency- D riven C hange D etector ( MFDCD ).” (p. 5, seção 1. INTRODUCTION)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “The image pairs are sourced from Google Earth, with a temporal coverage spanning from 2007 to 2022.” (p. 10, seção 8. fl->road)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- **260 pares** de imagens do **Google Earth**, 2007–2022, 0,59 m/pixel, de 270 × 534 a 7.215 × 4.366 px, recortados em **5.016 pares de 256 × 256**: **4.015 treino e 1.001 teste** (p. 10–11, tabela 1 na p. 3).
- Cobertura geográfica ampla (Hefei, Xi'an, Chongqing, Guangzhou, Japão, Singapura, Nigéria, Itália, EUA, Indonésia) (p. 10–11).
- **8 classes de cobertura** (estrada, ponte, solo exposto, grama, água, terra agrícola, vegetação, edifício) combinadas em **11 mudanças** (p. 8–9, tabela 2, figura 4); algumas transições raras têm peso zero no treino (p. 10).
- Anotação por equipe profissional com controle de qualidade (p. 9–10). Sem Planet; imagem de 0,59 m, muito mais fina que 3–5 m.

**Detectado automaticamente (verificar):**
- sensor/produto **Landsat**: 3 ocorrências (p. 2, 3, 6)
- sensor/produto **Imagens aéreas**: 2 ocorrências (p. 18)
- conjunto de dados **LEVIR-CD**: 12 ocorrências (p. 3, 18, 21, 22, 24)
- conjunto de dados **WHU-CD**: 9 ocorrências (p. 18, 21, 22, 24, 25)
- conjunto de dados **HRSCD**: 3 ocorrências (p. 2, 3, 6)
- resolução mencionada: 0.59 m (p. 10)
- resolução mencionada: 0.5 m (p. 18)
- “pairs of 256 × 256 patches, including 4,015 pairs for the training set and 1,001 pairs for the testing set.” (p. 11, seção 8. fl->road)
- “The Label row shows the ground truth. critical spatial information.” (p. 8, seção 2. Related Work)
- “This indicates that MFDCD demonstrates the best performance in terms of overlap between the predicted and ground truth change regions, enabling more precise localization of change areas.” (p. 21, seção 5. Experiments and Results)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 9 ocorrências (p. 1, 5, 6, 8, 21)
- **Recorte em patches/tiles**: 6 ocorrências (p. 3, 9, 10, 11, 18)
- **Aumento de dados**: 3 ocorrências (p. 11, 14, 19)
- **Textura (GLCM)**: 2 ocorrências (p. 20, 23)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Método:**

- **Backbone ResNet50** (compartilhado) → dois ramos: **Dynamic Frequency Coupler (DFC)** e **Textual Frequency Filter (TFF)** (p. 11–12).
- **DFC:** DWT separa baixa frequência (estrutura, continuidade) de alta (bordas); **ASFF** mistura alta frequência com características de baixo nível usando uma máscara de esparsidade que **decai com as iterações** (λ(p) = λ0·e^(−δp)); **BTFF** injeta a baixa frequência de uma data nas características de alto nível da outra data, nos dois sentidos (p. 12–15, eqs. 1–7).
- **TFF:** o CLIP faz inferência zero-shot nas imagens e gera descrições do tipo "imagem no tempo T1 tem probabilidade X de ser a classe Y" (top 5); o texto vira embedding, passa por **DFT** ao longo da sequência e por um **banco de filtros em grafo totalmente conectado** (l = 5); um decodificador de contexto alinha o resultado com os tokens visuais (p. 15–18, eqs. 8–14).
- Treino: uma RTX 3090, **AdamW lr 1e-4, weight decay 0,01, 40.000 iterações**, flips e distorção fotométrica; **entropia cruzada ponderada** com peso 1,5 para classes raras e 1,0 para as comuns (p. 19).

- **Estratégia temporal (detecção automática, verificar):** bitemporal / pares (auto: 9 menções)
**Métodos detectados automaticamente:**
- método/família **CNN**: 4 ocorrências (p. 7, 17, 26)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate of 0.0001 and a weight decay parameter of 0.01” (p. 19)
- batch: “batch size, N is the sequence length (number of to” (p. 16)
- otimizador: “AdamW is employed, with a learning rate of 0” (p. 19)
- perda: “cross-entropy loss to mitigate the class imbalance is” (p. 11)
- tamanho do patch: “256 × 256 patch” (p. 11)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Desbalanceamento**: 5 ocorrências (p. 6, 11, 19)
- **Teste externo / generalização**: 4 ocorrências (p. 6, 7, 21, 29)
- **Conjuntos treino/val/teste**: 3 ocorrências (p. 9, 18)
- métrica **IoU**: 22 ocorrências (p. 19, 20, 21, 22, 24)
- métrica **F1**: 18 ocorrências (p. 19, 20, 21, 22)
- métrica **Precisão/Recall**: 4 ocorrências (p. 19, 23, 28)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Métricas e resultados:**

- IoU e F1 (principais), Rec e Pre (auxiliares) (p. 19).
- **RB-SCD, mudança semântica** (tabela 3, p. 19): **mIoU 57,52** contra ChangeCLIP 54,95, DEFO 54,63, CdSC 52,75 e HGINet 48,65. IoU por classe do MFDCD: water→bridge 86,83; bridge→water 83,58; water→road 71,68; farmland→road 68,40. As mais difíceis ficam abaixo de 50 (p. ex., road→vegetation, road→grass e bare land→road em ~20–50).
- **LWGANet** (modelo fundacional de RS), tabela 4 (p. 20): mIoU 55,12 (L1) e 55,71 (L2), abaixo do MFDCD; os autores usam isso para dizer que o dataset é difícil.
- **RB-SCD, mudança binária** (tabela 5, p. 20): IoU 65,83 e F1 79,39 contra ELGC-Net 65,53/79,18.
- **Públicos** (tabela 6, p. 21): LEVIR-CD IoU 84,69, SYSU-CD 72,63 e WHU-CD 90,43, com ganhos de +1,06, +4,43 e +2,69 de IoU sobre o segundo; métodos reproduzidos com código público e parâmetros padrão (p. 21–22).
- **Ablação** (tabelas 7–10, p. 25–26): sem DFC e sem TFF mIoU 50,45; só DFC 55,89; só TFF 55,23; ambos 57,52. A troca do grafo por MLP, CNN 1D ou GAT fica entre 56,31 e 56,67; concatenar embeddings CLIP fica em 56,38. l = 5 filtros é o melhor.
- **Backbone** (tabela 11, p. 27): ResNet18 55,53, ResNet34 56,31, ResNet50 57,52, com 13,75 M / 22,80 M / 103,78 M de parâmetros.

**Trechos numéricos detectados automaticamente (verificar):**
- “Specifically, for the easily de tectable categories like water- - bridge, bridge- - water, water- - road and farmland- - road, our model attains IoU scores of 86.83%, 83.58%, 71.68%, and 68.40%, respec 19” (p. 19, seção 5. Experiments and Results)
- “In terms of the IoU metric, our model ranks first with a score of 65.83%, slightly outperforming ELGC-Net , which achieves 65.53%.” (p. 21, seção 5. Experiments and Results)
- “Regarding the F1, our MFDCD model also leads with a score of 79.39%, followed closely by ELGC-Net at 79.18%.” (p. 21, seção 5. Experiments and Results)
- “Specifically, on the WHU-CD dataset, our approach outperforms the second-best method by 2.69% and 1.5% in IoU and F1, respectively.” (p. 22, seção 5. Experiments and Results)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites declarados e observações:**

- Os autores listam: desbalanceamento (transições raras, como reparo e demolição, com poucas amostras) e pretendem coletar mais amostras (p. 11).
- **Observações minhas:** (a) o mIoU de 57,52 inclui a classe de fundo (~98 de IoU) e classes que os próprios autores zeram; a média é sensível a isso (p. 10, 19); (b) os ganhos sobre ChangeCLIP e DEFO são de ~2,6–2,9 pontos de mIoU em um único treino, sem desvio; (c) 5.016 recortes vêm de **260 pares**, e a divisão 4.015/1.001 é por recortes: o texto não diz que a divisão é por par/cena, então pode haver **vazamento espacial entre treino e teste**; (d) as imagens são do Google Earth, com datas e sensores heterogêneos, e o artigo não discute pseudomudança por sombra ou por diferença de aquisição, apenas mostra exemplos (p. 23–24); (e) o TFF depende do CLIP zero-shot para gerar as descrições, de modo que o "texto" é derivado da própria imagem e não de conhecimento externo; (f) as tabelas 3 e 4 foram extraídas com formatação ruim; usei apenas valores consistentes com o texto.

**Trechos detectados automaticamente (verificar contexto):**
- “Although existing road extraction datasets , mainly focus on binary pixel segmentation of roads, they cannot be used to focus on road changes.” (p. 2, seção 1. INTRODUCTION)
- “The limitations of existing spatial-domain methods highlight the need for a new ap proach that operates in a more suitable domain.” (p. 4, seção 1. INTRODUCTION)
- “This frequency domain representation naturally filters out minor textual variations, providing a stable basis for a cleaner alignment with visual features and overcoming the core limitations of spatial-level fusion.” (p. 4, seção 1. INTRODUCTION)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- Código prometido em github.com/DaGuangDaGuang/RB-SCD (p. 2, "will be available"); a disponibilidade do dataset não foi verificada. Hiperparâmetros listados (p. 19, figura 12 de sensibilidade na p. 28).

- **Código/dados:** sim: github.com/DaGuangDaGuang/RB-SCD (p. 2)
- URL citada: https://github.com/DaGuangDaGuang/RB-SCD (p. 2)
- declaração: “The code will be available at https://github.com/DaGuangDaGuang/RB-SCD.” (p. 2)
- hiperparâmetros **não detectados** automaticamente: épocas/iterações (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Quase tempo real 1 (p. 29); Custo 1 (p. 27)

**Interpretação — O que reaproveitar:**

- **Taxonomia de mudanças de estrada de/para** (11 categorias, incluindo água→ponte e estrada→solo) como ponto de partida para o esquema de classes de infraestrutura viária.
- **Decomposição por wavelet** para separar estrutura contínua e borda em alvos lineares; **BTFF** para manter a continuidade entre datas.
- **Esparsidade com decaimento** de componentes de alta frequência (estabiliza o início do treino).
- **Peso 1,5 para classes raras** como linha de base simples contra desbalanceamento.

**Interpretação — Cuidados para o nosso projeto:**

- Resolução de 0,59 m e imagem RGB do Google Earth: em 3–5 m uma estrada tem poucos pixels de largura, e a decomposição wavelet pode não se comportar da mesma forma.
- O benchmark mede acerto de classe de/para em recortes, não a data da obra.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[Landsat|Landsat]] — 3 ocorrências (p. 2, 3, 6)
- emprega conjunto de dados: [[LEVIRCD|LEVIR-CD]] — 12 ocorrências (p. 3, 18, 21, 22, 24)
- emprega conjunto de dados: [[WHUCD|WHU-CD]] — 9 ocorrências (p. 18, 21, 22, 24, 25)
- emprega conjunto de dados: [[HRSCD|HRSCD]] — 3 ocorrências (p. 2, 3, 6)
- utiliza método: [[CNN|Redes convolucionais (CNN)]] — 4 ocorrências (p. 7, 17, 26)
- é avaliado por: [[IoU|IoU / mIoU]] — 22 ocorrências (p. 19, 20, 21, 22, 24)
- é avaliado por: [[F1|F1]] — 18 ocorrências (p. 19, 20, 21, 22)
- é avaliado por: [[PrecisaoRecall|Precisão e recall]] — 4 ocorrências (p. 19, 23, 28)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 9 ocorrências (p. 1, 5, 6, 8, 21)
- aplica etapa de preparo: [[PatchesTiles|Recorte em patches/tiles]] — 6 ocorrências (p. 3, 9, 10, 11, 18)
- aplica etapa de preparo: [[AumentoDados|Aumento de dados]] — 3 ocorrências (p. 11, 14, 19)
- adota desenho de validação: [[Desbalanceamento|Desbalanceamento de classes]] — 5 ocorrências (p. 6, 11, 19)
- adota desenho de validação: [[Generalizacao|Generalização e domain shift]] — 4 ocorrências (p. 6, 7, 21, 29)
- adota desenho de validação: [[DivisaoTreinoTeste|Divisão treino/validação/teste]] — 3 ocorrências (p. 9, 18)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[MudancaSemantica|Mudança semântica (from–to)]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Edificacoes|Edificações e urbanização]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Vias|Vias e estradas]] — suporte vindo da leitura/título/resumo

## Figuras selecionadas

![[Shu_2025_SCDNewBenchmark_p12_Figure7.png|520]]
*Figure 7: Overview of our proposed Multimodal Frequency-Driven Change Detector (MFDCD). The frame (p. 12; recorte do PDF convertido)*

![[Shu_2025_SCDNewBenchmark_p8_Figure3.png|520]]
*Figure 3: Annotation examples on RB-SCD dataset. T 1 and T 2 represent the pre- and post-change images, (p. 8; recorte do PDF convertido)*

![[Shu_2025_SCDNewBenchmark_p4_Figure2.png|520]]
*Figure 2: Frequency-domain transformation of visual and textual data. (a) The DWT separates a visual (p. 4; recorte do PDF convertido)*


## Anotações do leitor

- 
