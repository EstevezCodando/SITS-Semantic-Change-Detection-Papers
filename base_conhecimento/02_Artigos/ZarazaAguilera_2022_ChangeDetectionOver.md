---
tipo: artigo
id_origem: P05
titulo: "Change Detection over mining areas using Deep Neural Networks from Planetscope image time series"
ano: 2022
autores: ["Maycol Alejandro Zaraza-Aguilera", "Erika Upegui", "Oscar Javier Espejo-Valero"]
doi: "10.1109/tla.2022.9878176"
arquivo_fonte: "coleta/P05_Zaraza-Aguilera2022_Change-Detection-over-mining-areas-using-Deep-Neural-Netw.pdf"
markdown_fonte: "output/pdf/P05_Zaraza-Aguilera2022_Change-Detection-over-mining-areas-using-Deep-Neural-Netw/document.md"
paginas: 10
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "A"
tarefas: ["[[Mineracao|Mineração]]", "[[Deteccao_Mudanca|Detecção de mudanças]]"]
sensores: ["[[PlanetScope|PlanetScope (Dove/SuperDove)]]"]
conjuntos_dados: []
metodos: ["[[UNet|U-Net]]"]
preparo: ["[[IndicesEspectrais|Índices espectrais (NDVI etc.)]]"]
validacao: ["[[EstimativaArea|Estimativa de área com intervalo de confiança]]"]
ferramentas: []
tags: [artigo, leitura/profunda, relevancia/A]
---

# ZarazaAguilera 2022 — Change Detection over mining areas using Deep Neural Networks from Planetscope image time series

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **A** — PlanetScope de 3 m em mineração; mudança direta vs pós-classificação; protocolo de Olofsson.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Maycol Alejandro Zaraza-Aguilera, Erika Upegui, Oscar Javier Espejo-Valero (2022). Change Detection over mining areas using Deep Neural Networks from Planetscope image time series. IEEE Latin America Transactions. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1109/tla.2022.9878176
- **Arquivo de origem:** `coleta/P05_Zaraza-Aguilera2022_Change-Detection-over-mining-areas-using-Deep-Neural-Netw.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P05_Zaraza-Aguilera2022_Change-Detection-over-mining-areas-using-Deep-Neural-Netw/document.md` — 10 páginas, 14 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Comparar **duas estratégias de deep learning** para detectar mudança em **áreas de mineração a céu aberto** com **PlanetScope**: (1) pós-classificação com U-Net/FPN e (2) **detecção direta** com U-Net modificada sobre pares de imagens. É o único estudo do catálogo que compara as duas famílias na mesma série PlanetScope.


## 3. Área de estudo e período analisado

**Detectado automaticamente (verificar):**
- “Esta investigación tiene como objetivo principal evaluar el rendimiento de los métodos de Deep Learning para DC sobre áreas de minería a cielo abierta en STIS de imágenes Planet Scope (PS) en la mina del Cerrejón para el periodo 2017 -2019,” (p. 2, seção I. INTRODUCCION)

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- Mina do Cerrejón (La Guajira, Colômbia), 327,16 km², cinco municípios (p. 3).
- **8 imagens PlanetScope** (4 bandas B, G, R, NIR; nível 3B ortorretificado; reflectância de superfície; 3 m), de out/2017 a nov/2019, escolhidas pelo menor percentual de nuvem (p. 3).
- Vetores de mineração/não-mineração para dez/2017, dez/2018 e dez/2019 (p. 3).
- Ambiente: TensorFlow 2.1 e Google Colab (GPU Tesla K80) (p. 3).

**Detectado automaticamente (verificar):**
- sensor/produto **Sentinel-2**: 4 ocorrências (p. 2, 5)
- sensor/produto **PlanetScope**: 3 ocorrências (p. 1, 2)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Evidência (leitura) — Amostragem e partições (reaproveitável):**

- Grade de **blocos de 1,6 × 1,6 km separados por 0,4 km** (estratégia de trabalhos anteriores) e patches aleatórios de 256 × 256 dentro dos blocos; rotação e flips (p. 3, 4).
- 57 blocos: 42 treino, 11 validação, 4 avaliação. Esquema 1: 11.050 / 2.700 / 1.050 patches; esquema 2: 8.150 / 1.950 / 800 (p. 4).



## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Esquema 1 — pós-classificação:**

- U-Net e FPN com encoder EfficientNet-B3 pré-treinado; 12 modelos variando entradas (RGB; RGB+NIR; RGB+NIR+NDVI) e épocas (50/100); perdas DiceFocal (U-Net) e Focal-Tversky (FPN); os quatro melhores foram re-treinados com as três datas (p. 3).
- Escolhido: **U-Net, DiceFocal, 4 bandas, 75 épocas** (p. 5). IoU de avaliação 0,72–0,81 (modelos iniciais) e ~0,70–0,74 após re-treino (p. 5).

**Evidência (leitura) — Esquema 2 — detecção direta:**

- U-Net modificada (pares de imagens), 5 modelos (4 ou 5 bandas, 20–50 épocas, DiceFocal); melhor: **4 bandas, 45 épocas** — IoU de treino 0,88 e de avaliação 0,73 (p. 3, 6, 8).
- Hiperparâmetros: batch 16, Adam, **taxa de aprendizado 0,1** (valor declarado no artigo, incomum) (p. 4).

- **Estratégia temporal (detecção automática, verificar):** série temporal (auto: 8 menções vs 2 de pares)
**Métodos detectados automaticamente:**
- método/família **U-Net**: 24 ocorrências (p. 1, 2, 3, 4, 5)
- método/família **CNN**: 5 ocorrências (p. 1, 2, 3)
**Hiperparâmetros detectados automaticamente (verificar):**
- batch: “batch size) de 16, como indica el trabajo de Ball,” (p. 4)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Evidência (leitura) — Avaliação:**

- Modelos: IoU e Loss por conjunto; **mapas de mudança avaliados pelo protocolo de Olofsson** (amostragem probabilística, desenho da resposta e matriz de erro) (p. 4).
- Esquema 1: exatidão de usuário de mudança 0,62–0,93 e kappa 0,70–0,95; os primeiros períodos pioram por nuvem (p. 7).
- Esquema 2: exatidão de usuário > 0,93 (exceto 0,80 no segundo período) e kappa > 0,92 (0,84 no segundo); média 0,94 (p. 7).
- Áreas de mudança: 140–228 ha por período (esq. 1), máximo de 250 ha (esq. 2) (p. 6).

**Detectado automaticamente (verificar):**
- métrica **IoU**: 19 ocorrências (p. 4, 5)
- métrica **Kappa**: 8 ocorrências (p. 1, 7)

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Conclusões do artigo:**

- A detecção direta (esq. 2) é a mais apropriada; ambas as abordagens são aceitáveis e próximas em métricas e visualmente (p. 7, 8).
- **4 bandas > 5 bandas**: incluir NDVI não melhorou a exatidão (p. 8).
- U-Net > FPN para esta imagem de resolução média (p. 8).
- Nuvem e sombra causam **superestimativa de mudança na pós-classificação**, por diferenças entre mapas (p. 7).
- Só se contou **ampliação** de mineração; recuperação não entrou na análise (p. 6).
- Conjunto de dados e códigos disponibilizados num repositório citado pelo artigo (p. 8).

**Trechos numéricos detectados automaticamente (verificar):**
- “A nivel general los 12 modelos bajo el esquema 1 en el entrenamiento poseen métricas de exactitud (IoU) superiores a 0.98 (TABLA I) mientras que con los datos de validación los modelos disminuyen su exactitud levemente rodeando valores alrededor de 0.9.” (p. 4, seção V. RESULTADOS Y DISCUSION)
- “Con los datos de evaluación los valores en general son buenos los cuales se encuentran entre 0.75 y 0.81 a excepción del modelo 6 el cual obtuvo un IoU de 0.72 esto puede indicar que un modelo con dicha configuración requiere de más de 50 épocas para tener una” (p. 4, seção V. RESULTADOS Y DISCUSION)
- “Sin embargo, en comparación a lo obtenido en este trabajo se evidencio que esta función de perdida permite dar un ajuste adecuado al modelo evitando el sobreajuste del mismo, a su vez el IoU obtenido es un poco más alto (0.88) por lo tanto el modelo aquí estru” (p. 5, seção V. RESULTADOS Y DISCUSION)
- “Id Modelo Entrenamiento Validación Evaluación Loss IoU Loss IoU Loss IoU 1 UNET4b40e 0.14 0.88 0.60 0.48 0.21 0.74 2 UNET4b45e 0.16 0.88 0.59 0.46 0.22 0.73 3 UNET5b20e 0.18 0.78 0.73 0.33 0.35 0.61 4 UNET5b25e 0.17 0.82 0.65 0.40 0.36 0.59 5 UNET5b50eb32 0.24” (p. 5, seção V. RESULTADOS Y DISCUSION)

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites e cuidados:**

- Apenas 8 datas, uma mina e uma classe; as avaliações de mudança são por período e não por evento datado.
- O kappa é alto numa amostra por pares; **não substitui** estimativa de área com IC (ver [[Olofsson_2014_GoodPracticesEstimating|Olofsson 2014]]).
- Taxa de aprendizado de 0,1 deve ser confirmada no código antes de replicar.


## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo. Oito datas de 2017 a 2019; avaliação por período.

**Interpretação — O que reaproveitar:**

- **Comparação pareada EXP2 vs EXP3** com os mesmos blocos e métricas (pós-classificação vs mudança direta).
- **Desenho de blocos** (1,6 km com folga de 0,4 km) como política de partição espacial contra vazamento.
- **Tratamento de nuvem** como prioridade: a pós-classificação exige máscara de observação válida.
- **Não gastar tempo com NDVI** como entrada extra no primeiro ciclo (resultado negativo relatado).
- **Loss DiceFocal** como padrão para classes raras.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[PlanetScope|PlanetScope (Dove/SuperDove)]] — 3 ocorrências (p. 1, 2)
- trata a tarefa: [[Mineracao|Mineração]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[Deteccao_Mudanca|Detecção de mudanças]] — suporte vindo da leitura/título/resumo
- utiliza método: [[UNet|U-Net]] — 24 ocorrências (p. 1, 2, 3, 4, 5)
- referencia (suporte manual da leitura): [[DivisaoEspacialBlocos|Divisão espacial por blocos e áreas]] — suporte vindo da leitura/título/resumo
- referencia (suporte manual da leitura): [[AmostragemEstratificada|Amostragem estratificada]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[EstimativaArea|Estimativa de área com intervalo de confiança]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[IndicesEspectrais|Índices espectrais (NDVI etc.)]] — suporte vindo da leitura/título/resumo

**Comparações substantivas com outros artigos:**
- este artigo aplica o protocolo de avaliação de [[Olofsson_2014_GoodPracticesEstimating|Olofsson 2014]] — P05 valida os mapas de mudança pelo método de Olofsson: (p. 4).
- [[Vizzari_2022_PlanetScopeSentinelSentinel|Vizzari 2022]] complementa com classificação estática este artigo — P07 classifica cobertura (RF/OBIA) e P05 detecta mudança em PlanetScope; juntos separam classificação estática de mudança temporal.

## Figuras selecionadas

![[ZarazaAguilera_2022_ChangeDetectionOver_p3_Fig.1.png|520]]
*Fig. 1. Área de estudio Mina el Cerrejón. (p. 3; recorte do PDF convertido)*


## Anotações do leitor

- 
