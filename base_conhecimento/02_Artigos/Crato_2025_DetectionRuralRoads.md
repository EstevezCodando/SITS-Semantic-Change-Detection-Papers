---
tipo: artigo
id_origem: P100
titulo: "Detection of rural roads from planet images using convolutional neural networks"
ano: 2025
autores: ["Jorgiana Kamila Teixeira do Crato", "Mário Ernesto Jijón-Palma", "Jorge Antônio Silva Centeno"]
doi: "10.1590/s1982-21702025000100004"
arquivo_fonte: "coleta/P100_Crato2025_Detection-of-rural-roads-from-planet-images-using-convolutio.pdf"
markdown_fonte: "output/pdf/P100_Crato2025_Detection-of-rural-roads-from-planet-images-using-convolutio/document.md"
paginas: 15
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "A"
tarefas: ["[[Vias|Vias e estradas]]"]
sensores: ["[[PlanetNICFI|Planet NICFI (basemaps)]]"]
conjuntos_dados: []
metodos: ["[[UNet|U-Net]]"]
preparo: ["[[Rotulagem|Rotulagem e anotação]]", "[[PatchesTiles|Recorte em patches/tiles]]"]
validacao: ["[[IoU|IoU / mIoU]]", "[[F1|F1]]"]
ferramentas: ["[[QGIS|QGIS]]"]
tags: [artigo, leitura/profunda, relevancia/A]
---

# Crato 2025 — Detection of rural roads from planet images using convolutional neural networks

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **A** — Planet de ~5 m para estradas rurais com U-Net (F1 de 69%); detecção por data, sem mudança.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Jorgiana Kamila Teixeira do Crato, Mário Ernesto Jijón-Palma, Jorge Antônio Silva Centeno (2025). Detection of rural roads from planet images using convolutional neural networks. Boletim de Ciências Geodésicas. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1590/s1982-21702025000100004
- **Arquivo de origem:** `coleta/P100_Crato2025_Detection-of-rural-roads-from-planet-images-using-convolutio.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P100_Crato2025_Detection-of-rural-roads-from-planet-images-using-convolutio/document.md` — 15 páginas, 15 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Detectar **estradas rurais** (terra compactada) na região metropolitana de Curitiba (PR) com **imagens Planet RGB de ~5 m** e uma **U-Net**, para atualizar mapas a custo menor (p. 1, 4). É **segmentação de um alvo numa data**, não detecção de mudança; a ideia de atualização é futura.

- “This study proposes to use high-resolution satellite images from Planet constellation, in conjunction with artificial intelligence, specifically UNet, to automatically identify rural roads in the metropolitan region of Curitiba, Paraná, Bra” (p. 1, seção Início)
- “Moreover, convolutional networks can be employed for the purpose of mapping roads in images.” (p. 2, seção 1. Introduction)

## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “Detection of rural roads from planet images using convolutional neural networks 4 Figure 1: Location map of the study area.” (p. 4, seção 2. Material and Method)
- “A) Presents the study area, containing the scenes used in this study in relation to the municipality of Curitiba.” (p. 4, seção 2. Material and Method)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- **12 cenas Planet** (~5.000 km²) da região rural de Curitiba; **só RGB** (NIR excluído de propósito para testar o uso futuro com RGB de VANT) (p. 4).
- Rótulos: estradas **vetorizadas à mão no QGIS 3.22.14** por inspeção visual; máscara com 3 valores: **estrada = 1, fundo = 2 e faixa de buffer de 2 pixels = 3** para tolerar imprecisão de borda (p. 5–6).
- **Treino/teste:** 10 das 12 cenas de **21/05/2022**; **validação** com as 2 cenas restantes, ou seja, **separada por cena** (p. 7).
- **Amostras:** janelas de **41 × 41 pixels (~205 m)** extraídas ao redor de pixels de estrada com passo de 41; 9.760 amostras (70 % treino e 30 % teste) e 1.783 de validação (p. 6–8).

**Detectado automaticamente (verificar):**
- sensor/produto **Planet (mosaicos e cenas)**: 10 ocorrências (p. 1, 3, 4, 13)
- sensor/produto **Planet NICFI**: 2 ocorrências (p. 3)
- resolução mencionada: 4.7 m (p. 3)
- resolução mencionada: 5 m (p. 13)
- “The training set was obtained from 10 scenes out of 12 scenes acquired on May 21, 2022.” (p. 7, seção 2.1.1 Preprocessing)
- “The training set consists of 9760 samples, where 70% of the samples were used to adjust the parameters of the net and the remaining samples (30%) were used as test samples.” (p. 8, seção 2.1.2 Processing)
- “The validation of the net was performed with a new set of 1783 samples not used during training.” (p. 8, seção 2.1.2 Processing)
- “The Google Colab platform was used with the python language interpreter to develop the necessary programs.” (p. 4, seção 2. Material and Method)
- “The initial stage of the process entails a visual examination of the image, with the purpose of generating a ground truth map, which will be utilized in the subsequent stages.” (p. 5, seção 2.1.1 Preprocessing)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 20 ocorrências (p. 5, 6, 8, 10, 12)
- **Índices espectrais**: 2 ocorrências (p. 13, 14)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Método:**

- U-Net com 13 camadas convolucionais (7 na codificação e 6 na decodificação), **16 ou 32 neurônios** iniciais, lote 32, 50 épocas, Keras/TensorFlow com a biblioteca Segmentation Models, no **Google Colab (GPU T4 gratuita)** (p. 4, 7–8).

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **U-Net**: 30 ocorrências (p. 1, 2, 3, 5, 6)
- método/família **CNN**: 15 ocorrências (p. 1, 2, 4, 6, 8)
**Hiperparâmetros detectados automaticamente (verificar):**
- batch: “batch size, Epochs), the number of neurons influen” (p. 9)
- épocas/iterações: “50 epochs” (p. 7)
- tamanho do patch: “41x41 pixel” (p. 6)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Detectado automaticamente (verificar):**
- métrica **Precisão/Recall**: 15 ocorrências (p. 1, 2, 3, 8, 9)
- métrica **IoU**: 10 ocorrências (p. 8, 9, 10, 13)
- métrica **F1**: 9 ocorrências (p. 1, 8, 9, 10, 12)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Resultados (tabela 1, p. 9):**

| | Teste 1 (16) | Teste 2 (32) |
|---|---|---|
| Acurácia | 91,85 % | 91,95 % |
| Precisão | 75,80 % | 75,83 % |
| Recall | 63,71 % | 65,92 % |
| F1 | 68,99 % | 69,07 % |
| mIoU | 53,94 % | 55,01 % |
| Tempo | 4 h 53 | 6 h 08 |
- Dobrar os neurônios deu ganho pequeno (+0,08 de F1) e quase 1 h 15 min a mais; 16 neurônios deu mais continuidade da rede, 32 deu resultado mais conservador (p. 9–11).
- Falhas: vegetação densa sobre a via, **falta de contraste com o entorno**, bordas da imagem, sombra e urbano de cor parecida (p. 10–12).

**Trechos numéricos detectados automaticamente (verificar):**
- “Parameters Test 1 Test 2 Epochs 50 50 Batch Size 32 32 Neurons 16 32 Accuracy 91.85% 91.95% Precision 75.80% 75.83% Recall 63.71% 65.92% F1-Score 68.99% 69.07% mIoU 53.94% 55.01% Time 04h:53min 06:08min Boletim de Ciências Geodésicas, 31: e2025004, 2025” (p. 9, seção 3. Results and Discussion)
- “Detection of rural roads from planet images using convolutional neural networks 10 The benefits were notably limited: a gain of only 0.10% in accuracy, 0.03% in precision, and 0.08% in F1-Score.” (p. 10, seção 3. Results and Discussion)
- “Even for metrics where the improvement was a little more significant, such as Recall, which showed an increase of 2.21%, and mIoU, with an improvement of 1.07%, the gain is still considered low.” (p. 10, seção 3. Results and Discussion)
- “Considering the quality metrics, the accuracy lies above 90%, which is relatively high.” (p. 10, seção 3. Results and Discussion)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites e observações:**

- Os autores concluem que o modelo "precisa de melhora", que 9.760 amostras são poucas, que trechos sinuosos e oclusos falham mais, e que o Colab limita redes maiores (p. 13).
- **Observações minhas:** (a) a **acurácia de 91,9 %** é calculada de um modo que o texto descreve como "só verdadeiros positivos sobre os pixels marcados" (p. 9), o que **não é a acurácia convencional**; o F1 de 69 % e o mIoU de 55 % são as métricas confiáveis; (b) o conjunto de **uma só data** e uma região limita a generalização; (c) as amostras de 41 × 41 **são centradas em estradas**, então a avaliação quase não tem janelas só de fundo, e a taxa de falso positivo em áreas sem estrada fica desconhecida; (d) a comparação com valores de outros trabalhos (F1 0,53 e 0,80) mistura dados e métricas diferentes (p. 12); (e) a largura da estrada em 5 m é de 0,6 a 1 pixel, e o texto atribui a queda de mIoU ao "traçado de largura constante" do rótulo, não à resolução.

**Trechos detectados automaticamente (verificar contexto):**
- “The deployment of the UNet in conjunction with these images facilitates the automated identification and mapping of roads in rural areas with high precision, offering an efficient alternative to traditional manual delimitation methods.” (p. 3, seção 1. Introduction)
- “Despite the limitations of using the GPU in the Colab environment, it has great applicability in the field of machine learning, as it includes many machine-learning libraries in Python.” (p. 4, seção 2. Material and Method)
- “It is a commercial platform designed to offer a programming environment, but with limitations for free use.” (p. 12, seção 3. Results and Discussion)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- Código e dados não informados; ambiente (Colab T4) e hiperparâmetros descritos.

- **Código/dados:** declarado sem URL localizada (p. 3)
- declaração: “Additionally, the data are available at a monthly temporal resolution.” (p. 3)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 3 (p. 1, 9)

**Interpretação — O que reaproveitar:**

- **Rótulo com buffer** (corpo, fundo, faixa de tolerância de 2 pixels) para alvos lineares estreitos.
- **Amostragem por janelas de 41 × 41** ao redor do alvo, com passo igual à janela para evitar redundância.
- **Divisão por cena** entre treino e validação.
- Estimativa realista de custo: U-Net pequena treina em horas numa GPU gratuita.

**Interpretação — Cuidados para o nosso projeto:**

- Detecta via existente, não via nova; a mudança teria de vir da diferença de duas datas.
- Em 5 m uma estrada rural tem 1–2 pixels; contraste e cobertura arbórea dominam o erro.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- referência (curado pela leitura): [[PlanetNICFI|Planet NICFI (basemaps)]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Vias|Vias e estradas]] — suporte vindo da leitura/título/resumo
- utiliza método: [[UNet|U-Net]] — 30 ocorrências (p. 1, 2, 3, 5, 6)
- aplica etapa de preparo: [[Rotulagem|Rotulagem e anotação]] — 20 ocorrências (p. 5, 6, 8, 10, 12)
- referência (curado pela leitura): [[PatchesTiles|Recorte em patches/tiles]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[QGIS|QGIS]] — suporte vindo da leitura/título/resumo
- é avaliado por: [[IoU|IoU / mIoU]] — 10 ocorrências (p. 8, 9, 10, 13)
- é avaliado por: [[F1|F1]] — 9 ocorrências (p. 1, 8, 9, 10, 12)

**Comparações substantivas com outros artigos:**
- este artigo trata de vias, como [[Shu_2025_SCDNewBenchmark|Shu 2025]] — P100 detecta estradas rurais em Planet de ~5 m por data (F1 69%) e P36 define transições de vias em imagem de 0,59 m.

## Figuras selecionadas

![[Crato_2025_DetectionRuralRoads_p4_Figure1.png|520]]
*Figure 1: Location map of the study area. A) Presents the study area, containing the scenes used in this study in (p. 4; recorte do PDF convertido)*

![[Crato_2025_DetectionRuralRoads_p6_Figure3.png|520]]
*Figure 3: The following examples illustrate the creation of cutouts in PLANET images and their respective visual (p. 6; recorte do PDF convertido)*

![[Crato_2025_DetectionRuralRoads_p5_Figure2.png|520]]
*Figure 2: The following flowchart illustrates the methodology employed to develop this research project. It (p. 5; recorte do PDF convertido)*


## Anotações do leitor

- 
