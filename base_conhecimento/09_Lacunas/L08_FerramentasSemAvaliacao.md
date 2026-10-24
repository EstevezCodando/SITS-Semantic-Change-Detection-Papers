---
tipo: lacuna
titulo: "Ferramentas de QGIS/GeoAI carecem de avaliação quantitativa"
tema: monitoramento
status: aberta
tags: [lacuna]
---

# Ferramentas de QGIS/GeoAI carecem de avaliação quantitativa

## Descrição

Os artigos de software (GeoAI, IAMAP) descrevem capacidades, mas não medem acurácia ou ganho de tempo; Deepness tem apenas uma avaliação independente pequena.

## Evidências nos artigos

- [[Wu_2026_GeoAIPythonPackage|Wu 2026]] (p. 1) e [[Tresson_2026_IAMAPUnlockingDeep|Tresson 2026]] (p. 4): artigos JOSS sem avaliação quantitativa.
- [[Febrita_2025_EvaluatingDrivenAutomated|Febrita 2025]] (p. 9): uma vizinhança e referência OSM.
- [[Wang_2025_SAMTestingReliability|Wang 2025]] (p. 18): seleção de máscara usa a anotação (viés otimista).

## O que isto afeta (método, dado ou resultado)

- afeta ferramenta: [[QGIS|QGIS]]
- afeta modelo fundacional: [[SAM|Segment Anything (SAM)]]
- afeta etapa: [[PreAnotacaoSAM|Pré-anotação assistida (SAM e plugins QGIS)]]

## Oportunidade (interpretação)

Medir tempo e qualidade de pré-anotação e revisão em QGIS com amostra independente.

[[00_Sintese_Lacunas|← Síntese das lacunas]]
