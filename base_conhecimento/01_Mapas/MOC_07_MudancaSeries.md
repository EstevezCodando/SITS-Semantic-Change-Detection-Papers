---
tipo: mapa
titulo: "Detecção de mudanças e séries temporais"
n_conceitos: 11
tags: [mapa]
---

# Detecção de mudanças e séries temporais

> Mapa de conteúdo: aponta para conceitos (que carregam a relação com os artigos) e para as lacunas. Não liga diretamente todos os artigos.

## Síntese com evidências

- Comparação direta entre as duas famílias na mesma série PlanetScope: [[ZarazaAguilera_2022_ChangeDetectionOver|ZarazaAguilera 2022]] (p. 8) (mudança direta supera pós-classificação, com ressalvas).
- Quatro estratégias de mudança semântica em [[Daudt_2019_MultitaskLearningLarge|Daudt 2019]]; a estratégia sequencial teve o maior kappa de mudança no HRSCD. Em séries diárias, nem sempre mais datas ajudam: [[Toker_2022_DynamicEarthNetDailyMulti|Toker 2022]] (p. 6).
- Segmentar uma imagem isolada **não** é evidência de detecção temporal; as notas só tratam como mudança o que compara datas.

## Conceitos deste mapa

**Tarefa**
- [[Deteccao_Mudanca|Detecção de mudanças]] — 33 artigos
- [[MudancaSemantica|Mudança semântica (from–to)]] — 16 artigos
- [[SITS|Séries temporais de imagens (SITS)]] — 12 artigos

**Arquitetura**
- [[UTAE|U-TAE (U-Net com atenção temporal)]] — 3 artigos
- [[RedeSiamesa|Redes siamesas]] — 12 artigos

**Métrica**
- [[MetricasMudancaSemantica|Métricas de mudança semântica (SeK, SCS, SCOT)]] — 7 artigos

**Conjunto de dados**
- [[DynamicEarthNet|DynamicEarthNet]] — 3 artigos
- [[SpaceNet7_MUDS|SpaceNet 7 / MUDS]] — 6 artigos
- [[HRSCD|HRSCD]] — 8 artigos
- [[SECOND|SECOND]] — 10 artigos

**Método**
- [[PosProcessamentoTemporal|Pós-processamento temporal (persistência, janela e colapso)]] — 6 artigos

## Lacunas relacionadas

- [[L03_MudancaRara|Mudança rara: métricas e perdas ainda penalizam eventos]]
- [[L04_DomainShift|Domain shift espacial e temporal degrada mudança e segmentação]]
- [[L10_TaxonomiaTransicoes|Transições (from–to) são pouco padronizadas]]

[[00_Inicio|← Painel]]
