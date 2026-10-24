---
tipo: mapa
titulo: "Síntese das lacunas"
tags: [lacuna, mapa]
---

# Síntese das lacunas

Cada lacuna tem evidências com página e uma oportunidade (interpretação).

| Lacuna | Tema | Resumo |
|---|---|---|
| [[L01_ValidacaoOperacional\|Quase nenhum estudo avalia monitoramento contínuo]] | monitoramento | Os estudos lidos são retrospectivos. Nenhum dos artigos aprofundados reporta latência de alerta, falsos alertas por km²/mês, custo de revisão humana ou drift em operação … |
| [[L02_CadenciaPlanet\|A cadência real dos mosaicos Planet nem sempre é mensal]] | dados | O NICFI foi semestral até ago/2020. Estudos como Vizzari 2022 usam um único composto de seis meses; Wagner 2023 mistura datas semestrais e mensais.… |
| [[L03_MudancaRara\|Mudança rara: métricas e perdas ainda penalizam eventos]] | validacao | A fração de pixels que mudam é pequena (≈5% mensal no DynamicEarthNet, 1,28% e 0,03% em P13; 0,115% de transições raras em HRSCD).… |
| [[L04_DomainShift\|Domain shift espacial e temporal degrada mudança e segmentação]] | validacao | O desempenho cai quando se muda de área e, para a detecção de mudança, quando se muda de ano.… |
| [[L05_RotulosTemporais\|Rótulos temporais são caros e subjetivos]] | preparo | A rotulagem sequencial de P10 levou 7 meses com 5 pessoas; P165 reconhece anotações subjetivas e ambíguas; P18 tem rótulos de 80–85% de precisão.… |
| [[L06_MetricasIncomparaveis\|Métricas e benchmarks não são comparáveis entre estudos]] | validacao | F1, IoU, kappa, SeK, SCS e SCOT medem coisas diferentes, em bases, classes e resoluções diferentes.… |
| [[L07_ResolucaoObjetosPequenos\|Objetos de poucos pixels limitam edificações e vias em 3–5 m]] | dados | Em Planet de ~4 m, edificações têm ≈4–5 px de extensão, com F1 de ~0,45 e mudança <0,1.… |
| [[L08_FerramentasSemAvaliacao\|Ferramentas de QGIS/GeoAI carecem de avaliação quantitativa]] | monitoramento | Os artigos de software (GeoAI, IAMAP) descrevem capacidades, mas não medem acurácia ou ganho de tempo; Deepness tem apenas uma avaliação independente pequena.… |
| [[L09_ReprodutibilidadeCodigo\|Disponibilidade de código e dados é desigual]] | monitoramento | Parte dos artigos lidos publica código; outros não informam. Ver a tabela de reprodutibilidade em [[Matriz_Comparativa]].… |
| [[L10_TaxonomiaTransicoes\|Transições (from–to) são pouco padronizadas]] | dados | DynamicEarthNet usa 7 classes, SECOND 6 (30 transições) e HRSCD 5 no nível L1; causa e legalidade não são observáveis em imagem.… |

[[00_Inicio|← Painel]]
