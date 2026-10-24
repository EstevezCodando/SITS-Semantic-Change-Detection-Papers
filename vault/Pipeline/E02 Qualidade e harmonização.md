---
tipo: pipeline
etapa: E02
tags: [pipeline, etapa/E02]
---
# E02 — Qualidade e harmonização

**Objetivo:** Medir registro geométrico, nuvem/sombra/emendas, radiometria e cadência real; decidir grade comum sem criar detalhe artificial.

**Entradas:** Assets catalogados  
**Saídas:** Máscara de observação válida; relatório de QA; grade comum documentada

**Anterior:** [[E01 Inventário e catálogo]] · **Próxima:** [[E03 Cubo espaço-temporal e partições]]

## Como fazer (decisões da literatura e do documento original)

- Medir desalinhamento em alvos estáveis; mascarar nuvem, sombra e emendas; manter classe de observação inválida.
- Verificar bandas (RGB visual não gera NDVI) e cadência real (NICFI anterior a set/2020 é semestral).
- 3 m e 5 m não são intercambiáveis: preservar originais e testar grade comum; reamostrar não cria detalhe.

**Risco principal:** Aprender diferenças de produto e processamento como se fossem mudanças no terreno.

## Conceitos relacionados

[[Nuvem-sombra-QA|Nuvem/sombra/QA]], [[Fusão de dados]], [[Super-resolução]]

## Artigos de apoio (13)

| Prioridade | Artigo | Título | O que aproveitar |
|---|---|---|---|
| média | [[P77 Shendryk 2019\|P77 Shendryk 2019]] | Deep learning for multi-modal classification of cloud, shado | uma camada explícita de qualidade antes de detectar mudanças. |
| média | [[P81 Frazier 2021\|P81 Frazier 2021]] | A Technical Review of Planet Smallsat Data: Practical Consid | Revisão técnica dos produtos Planet: processamento, radiometria e cuidados de uso. Leitura obrigatória antes d |
| média | [[P82 Roy 2021\|P82 Roy 2021]] | A global analysis of the temporal availability of PlanetScop | Análise global da disponibilidade temporal de PlanetScope; mede quantas observações úteis realmente existem po |
| média | [[P83 Wang 2021\|P83 Wang 2021]] | Automatic cloud and cloud shadow detection in tropical areas | Detecção automática de nuvem e sombra em PlanetScope tropical; camada de qualidade antes da detecção de mudanç |
| baixa | [[P84 Huang 2021\|P84 Huang 2021]] | Characterization of Planetscope-0 Planetscope-1 surface refl | Caracterização de reflectância e NDVI entre PlanetScope-0 e PlanetScope-1; alerta para inconsistências entre g |
| baixa | [[P85 Wang 2022\|P85 Wang 2022]] | A new object-class based gap-filling method for PlanetScope  | Preenchimento de lacunas em séries PlanetScope por classe de objeto; útil para meses com nuvem. |
| baixa | [[P86 Latte 2020\|P86 Latte 2020]] | PlanetScope Radiometric Normalization and Sentinel-2 Super-R | Normalização radiométrica de PlanetScope usando Sentinel-2 e super-resolução a 2,5 m. |
| baixa | [[P87 Sadeh 2020\|P87 Sadeh 2020]] | Fusion of Sentinel-2 and PlanetScope time-series data into d | Fusão Sentinel-2 e PlanetScope em reflectância diária de 3 m; referência para harmonização multissensor. |
| baixa | [[P88 Aragon 2021\|P88 Aragon 2021]] | CubeSats deliver new insights into agricultural water use at | Planet Fusion: dados diários de 3 m por fusão de CubeSats e satélites públicos. |
| baixa | [[P89 Kimm 2020\|P89 Kimm 2020]] | Deriving high-spatiotemporal-resolution leaf area index for  | Índice de área foliar de alta resolução espaço-temporal combinando CubeSats Planet e fusão STARFM no Corn Belt |
| baixa | [[P90 Karwowska 2022\|P90 Karwowska 2022]] | Using Super-Resolution Algorithms for Small Satellite Imager | Revisão de super-resolução para imagens de pequenos satélites; limite do que a super-resolução realmente recup |
| baixa | [[P91 Zhang 2023\|P91 Zhang 2023]] | Monitoring monthly tropical humid forest disturbances with P | Perturbações florestais mensais com mosaicos Planet NICFI em Camarões; próximo da cadência mensal do projeto. |
| baixa | [[P105 He 2022\|P105 He 2022]] | Tracking Urbanization in Developing Regions with Remote Sens | Acompanhamento da urbanização com super-resolução espaço-temporal (SpaceNet 7). |

## Experimentos ligados


