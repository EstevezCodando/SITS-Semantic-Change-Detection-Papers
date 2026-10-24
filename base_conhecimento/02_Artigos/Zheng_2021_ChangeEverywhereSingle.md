---
tipo: artigo
id_origem: P27
titulo: "Change Is Everywhere: Single-Temporal Supervised Object Change Detection in Remote Sensing Imagery"
ano: 2021
autores: ["Zhuo Zheng", "Ailong Ma", "Liangpei Zhang", "Yanfei Zhong"]
doi: "10.1109/iccv48922.2021.01491"
arquivo_fonte: "coleta/P27_Zheng2021_Change-Is-Everywhere-Single-Temporal-Supervised-Object-Chang.pdf"
markdown_fonte: "output/pdf/P27_Zheng2021_Change-Is-Everywhere-Single-Temporal-Supervised-Object-Chang/document.md"
paginas: 10
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: ["[[Deteccao_Mudanca|Detecção de mudanças]]", "[[SegmentacaoSemantica|Segmentação semântica]]"]
sensores: []
conjuntos_dados: ["[[LEVIRCD|LEVIR-CD]]"]
metodos: []
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Zheng 2021 — Change Is Everywhere: Single-Temporal Supervised Object Change Detection in Remote Sensing Imagery

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Zhuo Zheng, Ailong Ma, Liangpei Zhang, Yanfei Zhong (2021). Change Is Everywhere: Single-Temporal Supervised Object Change Detection in Remote Sensing Imagery. IEEE. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1109/iccv48922.2021.01491
- **Arquivo de origem:** `coleta/P27_Zheng2021_Change-Is-Everywhere-Single-Temporal-Supervised-Object-Chang.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P27_Zheng2021_Change-Is-Everywhere-Single-Temporal-Supervised-Object-Chang/document.md` — 10 páginas, 42 recortes de figuras, 1 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** For high spatial resolution (HSR) remote sensing im- ages, bitemporal supervised learning always dominates change detection using many pairwise labeled bitemporal images. However, it is very expensive and time-consuming to pairwise label large-scale bitemporal HSR remote sens- ing images. In this paper, we propose single-temporal su- pervised learning (STAR) for change detection from a new perspective of exploiting object changes in unpaired im- ages as supervisory signals. STAR enables us to train a high-accuracy change detector only using unpaired la- beled images and generalize to real-world bitemporal im- ages. To evaluate the effectiveness of STAR, we design a simple yet effective change detector called ChangeStar, which can reuse any deep semantic segmentation architec- ture by the ChangeMixin module. The comprehensive ex- perimental results show that ChangeStar outperforms the bas…

- “In this paper, we propose single-temporal su- pervised learning (STAR) for change detection from a new perspective of exploiting object changes in unpaired im- ages as supervisory signals.” (p. 1, seção Abstract)
- “In this paper, we propose a single-temporal supervised object change detection approach to bypass the problem of collecting paired labeled images by exploiting object change between unpaired images as supervisory signals, as shown in Fig.” (p. 2, seção 1 The bitemporal pixels should be at the same geographical p)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “This dataset consists of two aerial images obtained in 2012 and 2016 at same area of 20.5 km , which contains 12,796 and 16,077 building instances respectively.” (p. 5, seção 4.1. Experimental Setting)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- conjunto de dados **LEVIR-CD**: 16 ocorrências (p. 5, 6, 7, 8)
- resolução mencionada: 0.3 m (p. 5)
- resolução mencionada: 0.2 m (p. 5)
- resolução mencionada: 0.5 m (p. 5)
- “We used SGD] as the optimizer on single Titan RTX GPU with a minibatch of 16 images, weight decay of 0.0001 and momentum of 0.9.” (p. 6, seção 2 https://www.digitalglobe.com/ecosystem/open-data)
- “(a) t 1 Image (b) t 2 Image (c) Ground Truth (d) Bitemporal Sup.” (p. 8, seção 4.3. Ablation Study)
- “A extração direta abaixo preserva o conteúdo disponível e pode repetir trechos, rótulos ou camadas do PDF. text (a) t1 Image (b) t2 Image (c) Ground Truth (d) Bitemporal Sup.” (p. 8, seção 5. Conclusion)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 30 ocorrências (p. 1, 2, 3, 4, 5)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** bitemporal e série (auto: 72 pares; 7 série)
**Métodos detectados automaticamente:**
- método/família **Pós-classificação**: 3 ocorrências (p. 2, 6)
**Hiperparâmetros detectados automaticamente (verificar):**
- taxa de aprendizado: “learning rate was set to 0.03 and multiplied by (1 − maxstepstep” (p. 6)
- otimizador: “SGD] as the optimizer on single Titan RTX G” (p. 6)
- perda: “binary cross-entropy loss L binary as L seg to provi” (p. 4)
- tamanho do patch: “1024 × 1024 pixel” (p. 5)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- métrica **IoU**: 30 ocorrências (p. 6, 7, 8)
- métrica **F1**: 13 ocorrências (p. 6, 7, 8)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Trechos numéricos detectados automaticamente (verificar):**
- “Quantitatively, semantic supervision improves the baseline by 0.57% IoU and 0.43% F 1 and improves the baseline with temporal symmetry by 1.61% IoU and 1.19% F 1 .” (p. 7, seção 4.3. Ablation Study)
- “Table 2 (a)/(d) and (c)/(e) shows that using temporal symmetry gives a 2.25% IoU and 1.69% F 1 gains over the baseline and gives a 3.29% IoU and 2.45% F 1 over the baseline with semantic supervision.” (p. 7, seção 4.3. Ablation Study)
- “Table 3 presents that using or achieves 43.84% IoU, while using xor achieves 65.71% IoU.” (p. 7, seção 4.3. Ablation Study)

## 9. Limitações e condições de aplicabilidade

Não informado (nenhum trecho de limitação detectado).

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** declarado sem URL localizada (p. 1)
- declaração: “Code is available at https://github. com/Z-Zheng/ChangeStar.” (p. 1)
- hiperparâmetros **não detectados** automaticamente: batch, épocas/iterações (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 2 (p. 3, 6)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- emprega conjunto de dados: [[LEVIRCD|LEVIR-CD]] — 16 ocorrências (p. 5, 6, 7, 8)
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[SegmentacaoSemantica|Segmentação semântica]] — suporte vindo da leitura/título/resumo

## Anotações do leitor

- 
