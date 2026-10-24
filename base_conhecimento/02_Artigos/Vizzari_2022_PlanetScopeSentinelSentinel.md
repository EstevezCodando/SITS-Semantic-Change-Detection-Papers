---
tipo: artigo
id_origem: P07
titulo: "PlanetScope, Sentinel-2, and Sentinel-1 Data Integration for Object-Based Land Cover Classification in Google Earth Engine"
ano: 2022
autores: ["Marco Vizzari"]
doi: "10.3390/rs14112628"
arquivo_fonte: "HTML MDPI (sem PDF em coleta/)"
markdown_fonte: "não informado"
paginas: não informado
tipo_documento: "artigo completo (HTML aberto)"
status_leitura: "lido (profundo)"
relevancia_objetivo: "B"
tarefas: ["[[ClassificacaoCobertura|Classificação de cobertura e uso da terra]]"]
sensores: ["[[PlanetNICFI|Planet NICFI (basemaps)]]", "[[Sentinel2|Sentinel-2]]", "[[Sentinel1|Sentinel-1]]"]
conjuntos_dados: []
metodos: ["[[RandomForest|Random Forest]]", "[[OBIA|Análise baseada em objetos (OBIA)]]"]
preparo: ["[[Textura|Textura (GLCM)]]", "[[IndicesEspectrais|Índices espectrais (NDVI etc.)]]"]
validacao: ["[[Kappa|Coeficiente kappa]]"]
ferramentas: ["[[GoogleEarthEngine|Google Earth Engine]]"]
tags: [artigo, leitura/profunda, relevancia/B]
---

# Vizzari 2022 — PlanetScope, Sentinel-2, and Sentinel-1 Data Integration for Object-Based Land Cover Classification in Google Earth Engine

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **B** — NICFI em classificação de cobertura com RF e objetos; não mede mudança.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Marco Vizzari (2022). PlanetScope, Sentinel-2, and Sentinel-1 Data Integration for Object-Based Land Cover Classification in Google Earth Engine. Remote Sensing. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.3390/rs14112628
- **Arquivo de origem:** `HTML MDPI aberto (sem PDF em coleta/)`
- **Texto convertido (Markdown) e figuras:** `não informado`
- **Tipo de documento:** artigo completo (HTML aberto).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Quanto se ganha em **classificação de cobertura** com PlanetScope NICFI ao (a) trocar a abordagem por pixel (PB) por **orientada a objetos** (OB: SNIC + GLCM) e (b) integrar PlanetScope com Sentinel-2 e Sentinel-1, tudo com Random Forest no Google Earth Engine. É um estudo de **cobertura estática** (um composto de 14 meses), não de mudança; serve como baseline de ML (EXP1).


## 3. Área de estudo e período analisado

Ver seção 4 (dados), que traz área e período quando informados pelo artigo.

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Evidência (leitura):**

- Área de 69.272 km² no centro do Brasil (≈13,305°S, 46,770°O; TO/GO/BA), mosaico agrícola e natural (§ 2.1).
- **PlanetScope NICFI**: no período só havia **um composto semestral** de 4,77 m com 4 bandas; calculados NDVI e GNDVI. Sentinel-2 L2A: 547 imagens (1 ago 2018–30 set 2019) com NDVI, NDMI, GNDVI e BSI (média temporal); Sentinel-1: 212 imagens IW, VV e VH (média). S2 e S1 foram reamostrados para 4,77 m por interpolação bicúbica (§ 2.3.1, § 2.3.2).



## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Evidência (leitura) — Rótulos:**

- 2.400 pontos distribuídos de forma homogênea: ≈850 do **Brazil Data Cube** (INPE) e o restante interpretado em QGIS com o plugin **AcATaMa** sobre Bing/Google/Planet; 7 classes (§ 2.2).



## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Método:**

- **Textura:** GLCM sobre uma imagem de 8 bits (`0,3·NIR + 0,59·RED + 0,11·GREEN`; em S1 `(VH−VV)/(VH+VV)`), reescalada pelos percentis 2–98; janela de **2 px** para S2/S1 e **5 px** para PlanetScope; cinco índices de textura selecionados (§ 2.3.3).
- **Segmentação:** SNIC sobre as quatro bandas visíveis+NIR, `compactness 1`, `connectivity 8`, `neighborhood 128`, espaçamento de sementes 8 (S2) e 10 (PL); o valor de cada objeto é a média das camadas (§ 2.3.3).
- **Classificador:** Random Forest no GEE; 70 % / 30 % dos pontos para treino/validação, **os mesmos subconjuntos para os dez modelos**; `scale` de 20 m (S2/S1) e 10 m (PL) no `sampleRegion`; seleção iterativa de variáveis por importância (§ 2.3.4).

- **Estratégia temporal (detecção automática, verificar):** não informado

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

**Evidência (leitura) — Métricas:**

- OA, exatidão do produtor (PA = recall), do usuário (UA = precisão) e F-score; **teste de McNemar** (sem correção de continuidade; p < 0,05) para comparar modelos. **Kappa não calculado**, porque os dados de teste não são independentes entre as abordagens, e por críticas gerais ao kappa (§ 2.3.5).



## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Resultados (OA):**

| Abordagem | OA % |
|---|---|
| PB só S2 | 74,4 |
| OB só S2 | 81,6 |
| PB S2 + S1 | 81,2 |
| OB S2 + S1 | 83,5 |
| OB S2 + S1 + textura S1 | 86,2 |
| **PB só PlanetScope** | **66,7** |
| **OB só PlanetScope** | **82,2** |
| PB S2 + S1 + PL | 81,6 |
| OB (S2 + S1 espectral, PL textura/objeto) | 88,3 |
| **OB (PL espectral + S2 + S1)** | **90,6** |

- OB só com PL iguala OB só com S2 (82,2 vs 81,6; p = 0,892) com o dobro da resolução. A passagem de PB para OB com PL é significativa (82,2 vs 66,7; p = 0,000). Classes mais difíceis: arbustos, pastagens, solo exposto e edificado (§ 3).


Páginas: não informado (leitura feita sem texto integral convertido; ver a fonte na seção 1).

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Limites declarados:**

- A integração é feita só na composição de bandas, sem técnicas de fusão; a janela de 14 meses mistura mudanças reais no composto (§ 4.2).
- Geometria dos objetos (tamanho/forma) e precisão geométrica não foram avaliadas; vetorização no GEE travou; seleção de variáveis e redução de dimensionalidade limitadas pelo GEE (§ 4.5).
- Código só por e-mail ao autor.


## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** não avaliado (sem texto). 

**Interpretação — O que reaproveitar:**

- **Pipeline OB (SNIC + GLCM + RF)** como baseline barato do EXP1, inclusive em Python (scikit-image `slic`/`skimage.feature.graycomatrix` + scikit-learn), definindo janelas em **metros** (não px) para 3 m e 5 m.
- **Fluxo de rotulagem no QGIS** com AcATaMa e pontos de um cubo de dados oficial (Brazil Data Cube) para ampliar a amostra.
- **McNemar** para comparar classificadores no mesmo conjunto de teste; ao relatar, usar PA/UA/F por classe.
- Regra de que **objetos + textura do PlanetScope** trazem o ganho espacial, enquanto S2/S1 acrescentam espectro/estrutura.

**Interpretação — Cuidados para o nosso projeto:**

- Um composto único não valida transições mensais; este baseline mede cobertura, não evento.
- A OA de 67 % em PB com PlanetScope puro mostra que o espectro de 4 bandas do Planet é pobre sem contexto espacial.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza dado/sensor: [[PlanetNICFI|Planet NICFI (basemaps)]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[Sentinel2|Sentinel-2]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[Sentinel1|Sentinel-1]] — suporte vindo da leitura/título/resumo
- trata a tarefa: [[ClassificacaoCobertura|Classificação de cobertura e uso da terra]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[RandomForest|Random Forest]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[OBIA|Análise baseada em objetos (OBIA)]] — suporte vindo da leitura/título/resumo
- aplica etapa de preparo: [[Textura|Textura (GLCM)]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[IndicesEspectrais|Índices espectrais (NDVI etc.)]] — suporte vindo da leitura/título/resumo
- usa ferramenta: [[GoogleEarthEngine|Google Earth Engine]] — suporte vindo da leitura/título/resumo
- referência (curado pela leitura): [[Kappa|Coeficiente kappa]] — suporte vindo da leitura/título/resumo

**Comparações substantivas com outros artigos:**
- este artigo complementa com classificação estática [[ZarazaAguilera_2022_ChangeDetectionOver|ZarazaAguilera 2022]] — P07 classifica cobertura (RF/OBIA) e P05 detecta mudança em PlanetScope; juntos separam classificação estática de mudança temporal.
- [[Wagner_2023_MappingTropicalForest|Wagner 2023]] convergem na cadência do NICFI este artigo — Ambos descrevem a cadência do NICFI: (p. 3); (§ 1).

## Anotações do leitor

- 
