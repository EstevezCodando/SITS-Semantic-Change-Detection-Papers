---
tipo: mapa
titulo: "Deep Learning (arquiteturas e estratégias)"
n_conceitos: 15
tags: [mapa]
---

# Deep Learning (arquiteturas e estratégias)

> Mapa de conteúdo: aponta para conceitos (que carregam a relação com os artigos) e para as lacunas. Não liga diretamente todos os artigos.

## Síntese com evidências

- A U-Net é a base dos estudos Planet lidos ([[Wagner_2023_MappingTropicalForest|Wagner 2023]], [[ZarazaAguilera_2022_ChangeDetectionOver|ZarazaAguilera 2022]], [[Etten_2021_MultiTemporalUrban|Etten 2021]]). Arquiteturas temporais (U-TAE) são comparadas em [[Toker_2022_DynamicEarthNetDailyMulti|Toker 2022]] e estendidas em [[Vincent_2024_SatelliteImageTime|Vincent 2024]].
- Os resultados de modelos fundacionais devem ser lidos com cautela: ver o lembrete de comparabilidade em [[L06_MetricasIncomparaveis]].

## Conceitos deste mapa

**Arquitetura/família**
- [[CNN|Redes convolucionais (CNN)]] — 41 artigos

**Arquitetura**
- [[UNet|U-Net]] — 33 artigos
- [[RedeSiamesa|Redes siamesas]] — 21 artigos
- [[Transformer|Transformers]] — 34 artigos
- [[Mamba|Mamba / modelos de espaço de estados]] — 2 artigos
- [[UTAE|U-TAE (U-Net com atenção temporal)]] — 3 artigos
- [[LSTM|Redes recorrentes (LSTM)]] — 11 artigos

**Família de modelos**
- [[ModeloFundacional|Modelos fundacionais]] — 18 artigos

**Modelo fundacional**
- [[SAM|Segment Anything (SAM)]] — 13 artigos

**Estratégia**
- [[TransferLearning|Aprendizado por transferência]] — 25 artigos
- [[SemiAutoSupervisionado|Aprendizado semi/auto-supervisionado]] — 20 artigos
- [[SupervisaoFraca|Supervisão fraca]] — 3 artigos
- [[SuperResolucao|Super-resolução]] — 4 artigos

**Ferramenta**
- [[PyTorch|PyTorch]] — 3 artigos
- [[TensorFlow|TensorFlow / Keras]] — 2 artigos

## Lacunas relacionadas

- [[L04_DomainShift|Domain shift espacial e temporal degrada mudança e segmentação]]
- [[L06_MetricasIncomparaveis|Métricas e benchmarks não são comparáveis entre estudos]]

[[00_Inicio|← Painel]]
