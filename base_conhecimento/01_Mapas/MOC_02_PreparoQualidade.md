---
tipo: mapa
titulo: "Preparação e qualidade das imagens"
n_conceitos: 9
tags: [mapa]
---

# Preparação e qualidade das imagens

> Mapa de conteúdo: aponta para conceitos (que carregam a relação com os artigos) e para as lacunas. Não liga diretamente todos os artigos.

## Síntese com evidências

- [[Wagner_2023_MappingTropicalForest|Wagner 2023]] (p. 4): o estudo converteu para 8 bits e confiou na variabilidade natural para generalizar.
- Desalinhamento é tratado explicitamente em [[Etten_2021_MultiTemporalUrban|Etten 2021]] (p. 3), que cria uma máscara de dado inutilizável (UDM).
- Nuvem e sombra produzem falsa mudança na pós-classificação ([[ZarazaAguilera_2022_ChangeDetectionOver|ZarazaAguilera 2022]] (p. 4)), motivo pelo qual a máscara de observação válida é prioridade.

## Conceitos deste mapa

**Etapa**
- [[MascaraNuvem|Máscara de nuvem e sombra]] — 15 artigos
- [[Corregistro|Corregistro e georreferenciamento]] — 3 artigos
- [[CorrecaoAtmosferica|Correção atmosférica e reflectância]] — 4 artigos
- [[Reamostragem|Reamostragem]] — 3 artigos
- [[MosaicosCompostos|Mosaicos e compostos temporais]] — 13 artigos
- [[Normalizacao|Normalização e escala radiométrica]] — 22 artigos
- [[PatchesTiles|Recorte em patches/tiles]] — 57 artigos
- [[AumentoDados|Aumento de dados]] — 16 artigos

**Ferramenta**
- [[GDAL|GDAL / rasterio]] — 3 artigos

## Lacunas relacionadas

- [[L02_CadenciaPlanet|A cadência real dos mosaicos Planet nem sempre é mensal]]

[[00_Inicio|← Painel]]
