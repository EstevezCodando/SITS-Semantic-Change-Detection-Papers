---
tipo: resultado
titulo: "Achados relevantes"
tags: [resultado]
---

# Achados relevantes

> Cada achado vale **dentro** do estudo citado. Não compare valores entre bases diferentes. As frases de “interpretação” estão marcadas.

## 1. Shift espacial é o que mais degrada o desempenho

**Evidência:** [[Vincent_2024_SatelliteImageTime|Vincent 2024]] (p. 9): queda média de mIoU de 31,9% (DynamicEarthNet) e 10,5% (MUDS); o shift temporal afeta principalmente a detecção de mudança.

**Conceitos:** [[Generalizacao|Generalização e domain shift]], [[DivisaoEspacialBlocos|Divisão espacial por blocos e áreas]], [[DivisaoTemporal|Divisão temporal]]

## 2. A mudança é rara

**Evidência:** [[Daudt_2019_MultitaskLearningLarge|Daudt 2019]] (p. 6) e [[Toker_2022_DynamicEarthNetDailyMulti|Toker 2022]] (p. 5).

**Conceitos:** [[Desbalanceamento|Desbalanceamento de classes]], [[AcuraciaGlobal|Acurácia global (OA)]]

## 3. Mais datas nem sempre ajudam

**Evidência:** [[Toker_2022_DynamicEarthNetDailyMulti|Toker 2022]] (p. 6): observações diárias são correlacionadas e desestabilizam o treino.

**Conceitos:** [[SITS|Séries temporais de imagens (SITS)]], [[UTAE|U-TAE (U-Net com atenção temporal)]]

## 4. Edificações de 4–5 px têm F1 em torno de 0,45

**Evidência:** [[Etten_2021_MultiTemporalUrban|Etten 2021]] (p. 8) para objetos de 4–5 px; o termo de mudança do SCOT foi 0,06–0,07.

**Conceitos:** [[SpaceNet7_MUDS|SpaceNet 7 / MUDS]], [[MetricasMudancaSemantica|Métricas de mudança semântica (SeK, SCS, SCOT)]]

## 5. Mudança direta e pós-classificação em PlanetScope

**Evidência:** [[ZarazaAguilera_2022_ChangeDetectionOver|ZarazaAguilera 2022]] (p. 8) (mudança direta), com a ressalva de uma só mina e oito datas.

**Conceitos:** [[PosClassificacao|Pós-classificação]], [[UNet|U-Net]]

## 6. NDVI não ajudou como entrada extra

**Evidência:** [[ZarazaAguilera_2022_ChangeDetectionOver|ZarazaAguilera 2022]] (p. 8): modelos de 4 bandas igualaram ou superaram os de 5.

**Conceitos:** [[IndicesEspectrais|Índices espectrais (NDVI etc.)]]

## 7. Objetos e textura compensam o espectro do Planet

**Evidência:** [[Vizzari_2022_PlanetScopeSentinelSentinel|Vizzari 2022]] (início) (66,7%); com objetos, 82,2% no mesmo dado.

**Conceitos:** [[OBIA|Análise baseada em objetos (OBIA)]], [[Textura|Textura (GLCM)]], [[RandomForest|Random Forest]]

## 8. Mais pontos de prompt não melhoram sempre o SAM

**Evidência:** [[Wang_2025_SAMTestingReliability|Wang 2025]] (p. 17): o ótimo ficou em ~20–30 pontos; contraste do alvo prevê o sucesso.

**Conceitos:** [[SAM|Segment Anything (SAM)]], [[PreAnotacaoSAM|Pré-anotação assistida (SAM e plugins QGIS)]]

## 9. Parâmetros do plugin importam tanto quanto o modelo

**Evidência:** [[Febrita_2025_EvaluatingDrivenAutomated|Febrita 2025]] (p. 8): resolução, sobreposição e remoção de segmentos levaram o F1 de 48,1% a 78,6%.

**Conceitos:** [[QGIS|QGIS]]

## 10. Métricas próprias para mudança semântica

**Evidência:** [[Yang_2021_AsymmetricSiameseNetworks|Yang 2021]] (p. 6): SeK, SCS e SCOT foram criadas para evitar que a classe “sem mudança” domine.

**Conceitos:** [[MetricasMudancaSemantica|Métricas de mudança semântica (SeK, SCS, SCOT)]]


[[00_Inicio|← Painel]]
