---
tipo: artigo
id_origem: P40
titulo: "Road Change Detection Using Maps and Aerial Imagery for Digital Map Updating"
ano: 2026
autores: ["Juhee Lee", "Chang-Young Lee", "Inhyeok Lee", "Bui Ngoc An", "Jangwoo Cheon", "Impyeong Lee"]
doi: "10.7780/kjrs.2026.42.2.5"
arquivo_fonte: "coleta/P40_Lee2026_Road-Change-Detection-Using-Maps-and-Aerial-Imagery-for-Digi.pdf"
markdown_fonte: "output/pdf/P40_Lee2026_Road-Change-Detection-Using-Maps-and-Aerial-Imagery-for-Digi/document.md"
paginas: 18
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (parcial)"
relevancia_objetivo: "B"
tarefas: ["[[Vias|Vias e estradas]]", "[[Deteccao_Mudanca|Detecção de mudanças]]"]
sensores: ["[[ImagensAereas|Imagens aéreas]]"]
conjuntos_dados: []
metodos: ["[[TransferLearning|Aprendizado por transferência]]", "[[Transformer|Transformers]]"]
preparo: []
validacao: ["[[Desbalanceamento|Desbalanceamento de classes]]", "[[F1|F1]]", "[[IoU|IoU / mIoU]]"]
ferramentas: []
tags: [artigo, leitura/parcial, relevancia/B]
---

# Lee 2026 — Road Change Detection Using Maps and Aerial Imagery for Digital Map Updating

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (parcial). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **B** — Mapa de vias anterior como entrada do modelo; ortofoto de 12 cm.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Juhee Lee, Chang-Young Lee, Inhyeok Lee, Bui Ngoc An et al. (2026). Road Change Detection Using Maps and Aerial Imagery for Digital Map Updating. 대한원격탐사학회지. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.7780/kjrs.2026.42.2.5
- **Arquivo de origem:** `coleta/P40_Lee2026_Road-Change-Detection-Using-Maps-and-Aerial-Imagery-for-Digi.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P40_Lee2026_Road-Change-Detection-Using-Maps-and-Aerial-Imagery-for-Digi/document.md` — 18 páginas, 22 recortes de figuras, 1 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Detectar **mudança de vias** comparando um **mapa vetorial anterior** com uma **ortofoto aérea atual**, para atualizar mapas digitais, com um modelo derivado do **MapFormer** (p. 1, 5). O mapa antigo não é só linha de base: **condiciona** a interpretação da imagem nova (p. 5).

- “This study proposes a deep learning–based framework for road change detection that integrates existing maps and high-resolution aerial orthophotos to support digital map updating.” (p. 1, seção 5 Principal Researcher, Geospatial Team, InnoPAM, Seoul, Rep)
- “To address the severe class imbalance commonly observed in road change detection tasks, we introduce a dataset construction strategy that combines synthetic map modification and tile filtering to increase the proportion of informative chang” (p. 1, seção 5 Principal Researcher, Geospatial Team, InnoPAM, Seoul, Rep)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “In this study, to objectively evaluate the learning efficiency and cross-regional generalization performance of the proposed road change detection model, we divided the study area into training and evaluation regions.” (p. 3, seção 2.1. Study Area)
- “Geographical overview of the study area, displaying the training regions (Anyang-si and Jungnang-gu) and independent test areas (Gangnamgu and Gangseo-gu) alongside their corresponding aerial orthophoto. https://www.kjrs.org 231” (p. 3, seção 2.1. Study Area)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- Mapas digitais 1:5.000 do NGII (polígonos de vias) e **ortofotos aéreas de 12 cm/pixel**, rasterizados à mesma resolução (p. 4).
- **Treino/validação:** Anyang-si (2023/2024, 52,8 km²) e Jungnang-gu (2020/2022, 8,07 km²); **teste independente:** Gangnam-gu (2020/2023, 12,01 km²) e Gangseo-gu (2020/2022, 5,69 km²) (p. 4, tabela 1).
- **Rótulos automáticos** por interseção e diferença entre o raster de vias antigo e o atual: classes **nova, removida e sem mudança** (calçadas excluídas por subtração) (p. 5).
- **Divisão espacial em blocos com zonas de buffer** entre treino e validação para evitar vazamento por autocorrelação; tiles de 512 × 512 (p. 4–5).

**Detectado automaticamente (verificar):**
- sensor/produto **Imagens aéreas**: 4 ocorrências (p. 1, 2)
- resolução mencionada: 12 cm (p. 4)
- “The original dataset (OD) refers to the initial training setup where aerial orthophotos are simply partitioned into 512 × 512 tiles without additional augmentation or filtering.” (p. 5, seção 3.1. Overall Framework)
- “The OD, as the initial dataset, consists of 15,934 tiles and suffers from a severe class imbalance with an extremely low proportion of change classes, as it has not undergone any augmentation or selection processes.” (p. 9, seção 4.1. Experimental Setup)
- “To resolve this imbalance, geometric augmentation, including 90-degree rotations and horizontal/vertical flips, was applied to the 201 tiles containing changes within the OD, generating a total of 905 change tiles.” (p. 9, seção 4.1. Experimental Setup)
- “Changes are typically subjected to a primary screening process followed by secondary validation through aerial photography, which frequently requires repetitive manual interpretation.” (p. 2, seção 1. Introduction)
- “Additionally, there are practical limitations to conducting field surveys with restricted personnel.” (p. 2, seção 1. Introduction)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Recorte em patches/tiles**: 31 ocorrências (p. 1, 3, 4, 5, 7)
- **Aumento de dados**: 6 ocorrências (p. 5, 7, 9)
- **Rotulagem / anotação**: 6 ocorrências (p. 4, 5, 9, 10, 15)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Método:**

- Entrada: ortofoto + mapa anterior; saída: classes de mudança de via; **dados sintéticos** (modificação sintética do mapa) e **filtragem de tiles** para aumentar a fração de mudança; três estratégias de ajuste fino (FT1 integrada, FT2 com encoder congelado, FT3 com cabeça reinicializada) (p. 5–6, 12–13).
- Configurações de dados: OD (original), AD1 (com sintéticos), AD2 (com filtro), AD3 (filtro forte) (p. 11).

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **Transfer learning**: 12 ocorrências (p. 1, 3, 6, 12, 13)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate to 0.00006 to ensure stable convergence” (p. 9)
- batch: “batch size was configured to 6, considering GPU me” (p. 9)
- otimizador: “AdamW optimizer for weight updates, setting t” (p. 9)
- perda: “cross-entropy in Eq” (p. 9)
- tamanho do patch: “512 × 512 pixel tile” (p. 5)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- **Desbalanceamento**: 21 ocorrências (p. 1, 3, 7, 8, 9)
- **Teste externo / generalização**: 4 ocorrências (p. 3, 4, 5, 16)
- métrica **Precisão/Recall**: 98 ocorrências (p. 7, 8, 9, 10, 11)
- métrica **F1**: 30 ocorrências (p. 10, 11, 12, 13, 14)
- métrica **IoU**: 21 ocorrências (p. 10, 11, 13, 14, 15)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Resultados (texto das p. 11–13):**

- **OD:** conservador, alta precisão e baixo recall (em Gangnam-gu recall de "nova" 0,289 e "removida" 0,190) (p. 11).
- **AD1:** recall sobe para 0,725 (nova) e 0,519 (removida) em Gangnam-gu e 0,758 e 0,763 em Gangseo-gu, com **queda de precisão** (p. 11).
- AD2 e AD3 não melhoram de forma consistente; remover muito fundo atrapalha o contexto (p. 11).
- **FT1 (ajuste fino completo)** é o mais estável: F1 de "nova" 0,457 em Gangnam-gu e 0,419 em Gangseo-gu; FT2 e FT3 ficam atrás (p. 12–13).
- Sensibilidade da perda de separação: λ_sep 0 → IoU 0,267 e F1 0,422 para "nova"; λ_sep 0,2 melhora (p. 13–14).

**Trechos numéricos detectados automaticamente (verificar):**
- “Specifically, in Gangnam-gu, the recall for New and Removed classes was notably low at 0.289 and 0.190, respectively, indicating a tendency to miss change areas.” (p. 11, seção 4.2.1. Dataset Strategy Comparison)
- “In Gangnam-gu, the recall for New and Removed classes improved to 0.725 and 0.519, respectively.” (p. 11, seção 4.2.1. Dataset Strategy Comparison)
- “A similar trend was observed in Gangseo-gu, where recall increased to 0.758 and 0.763.” (p. 11, seção 4.2.1. Dataset Strategy Comparison)
- “In the Gangnam-gu results (Table 7), it recorded a recall of 0.725 and an F1-score of 0.457 for the New class.” (p. 12, seção 4.2.2. Fine-Tuning Strategy Comparison)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites e observações:**

- **Observações minhas:** (a) o F1 da classe "nova" fica em **0,4–0,5**, mesmo com ortofoto de 12 cm; a tarefa é difícil por si; (b) os rótulos vêm de **diferença de mapas oficiais**, então erros de vetorização e de alinhamento viram "mudança" (o mesmo problema que P17 relata); (c) o ganho do sintético vem **trocando precisão por recall**, não melhorando ambos; (d) as imagens aéreas de 12 cm não são comparáveis com 3–5 m; em Planet uma via tem 1–2 pixels, e o mapa prévio teria de vir de OSM ou cadastro; (e) li só parte das equações e da comparação com baselines (tabela 10).

**Trechos detectados automaticamente (verificar contexto):**
- “Moreover, the heavy reliance on aerial photography creates a temporal lag—a “blackout” period—determined by acquisition schedules and project bidding cycles, during which changes cannot be reflected in real-time.” (p. 2, seção 1. Introduction)
- “Additionally, there are practical limitations to conducting field surveys with restricted personnel.” (p. 2, seção 1. Introduction)
- “To overcome these limitations, research on deep learningbased change detection has been actively conducted in recent years.” (p. 2, seção 1. Introduction)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 17)
- declaração: “Future research will aim to improve detection performance for sparse change classes and expand the scope of the framework through validation across more diverse regions and environmental conditions. ### Author Contributions Conceptualizatio” (p. 17)
- hiperparâmetros **não detectados** automaticamente: épocas/iterações (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Persistência / confirmação 4 (p. 11, 16); Quase tempo real 1 (p. 2)

**Interpretação — O que reaproveitar:**

- **Mapa prévio como canal de entrada** (condicionamento por informação cartográfica antes/depois) para estradas e edificações.
- **Rótulos de mudança por diferença de rasters de duas datas** com pipeline automático.
- **Divisão por blocos com buffer** e **teste em regiões independentes**.
- **Dados sintéticos de mudança** (editar o mapa) para elevar a fração de positivos, avaliando o efeito sobre precisão e recall.

**Interpretação — Cuidados para o nosso projeto:**

- Resolução de 12 cm; não há evidência em 3–5 m.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- trata a tarefa: [[Vias|Vias e estradas]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- utiliza método: [[TransferLearning|Aprendizado por transferência]] — 12 ocorrências (p. 1, 3, 6, 12, 13)
- referência (curado pela leitura): [[Transformer|Transformers]] — suporte vindo da leitura/título/resumo
- utiliza dado/sensor: [[ImagensAereas|Imagens aéreas]] — 4 ocorrências (p. 1, 2)
- adota desenho de validação: [[Desbalanceamento|Desbalanceamento de classes]] — 21 ocorrências (p. 1, 3, 7, 8, 9)
- referência (curado pela leitura): [[DivisaoEspacialBlocos|Divisão espacial por blocos e áreas]] — suporte vindo da leitura/título/resumo
- é avaliado por: [[F1|F1]] — 30 ocorrências (p. 10, 11, 12, 13, 14)
- é avaliado por: [[IoU|IoU / mIoU]] — 21 ocorrências (p. 10, 11, 13, 14, 15)

**Comparações substantivas com outros artigos:**
- este artigo usa informação prévia de vias como [[Shu_2025_SCDNewBenchmark|Shu 2025]] — P40 usa o mapa anterior como entrada do modelo; P36 define 11 transições de vias a partir de imagens bitemporais.

## Figuras selecionadas

![[Lee_2026_RoadChangeDetection_p3_Fig.1.png|520]]
*Fig. 1. Geographical overview of the study area, displaying the training regions (Anyang-si and Jungnang-gu) and independent test areas (Gan (p. 3; recorte do PDF convertido)*

![[Lee_2026_RoadChangeDetection_p8_Fig.6.png|520]]
*Fig. 6. Visual comparison of synthesized and actual road changes across multiple scenarios. The figure displays three sample cases (a–c) for (p. 8; recorte do PDF convertido)*

![[Lee_2026_RoadChangeDetection_p6_Fig.4.png|520]]
*Fig. 4. Overview of the proposed map–image fusion-based road change detection framework illustrating input configuration, feature fusion, an (p. 6; recorte do PDF convertido)*


## Anotações do leitor

- 
