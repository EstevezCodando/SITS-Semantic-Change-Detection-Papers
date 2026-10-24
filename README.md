# Detecção e Classificação de Mudanças da Cobertura Terrestre com Séries Planet — Coletânea de Artigos

**Idioma:** Português (Brasil)

Lista curada de **185 trabalhos** sobre detecção semântica de mudanças em séries temporais de imagens de satélite (SITS-SCD), orientada a **mosaicos mensais Planet de 3–5 m (2020–2026)**: supressão vegetal, novas construções, abertura de vias e outras transições de cobertura. Cada entrada informa **onde**, **entre quais datas** e **de qual cobertura para qual cobertura** o estudo trata, com comentário de método, aplicação e limite. A coletânea inclui ainda artigos sobre **GeoAI e plugins de QGIS**, bibliotecas verificadas e um guia metodológico para o experimento do projeto.

> Os resultados citados são **os relatados pelos autores**, não reproduções. Ao comentar um artigo, as limitações indicam o que **não** se pode concluir sobre mosaicos Planet de 3–5 m. Esta é uma busca dirigida, **não** uma revisão sistemática PRISMA nem um censo da literatura. Os artigos não foram lidos integralmente.

## Sobre esta coleta

**Autor da coleta:** Jean Michael Estevez Alvarez

- **Data da coleta e verificação:** 24/10/2026.
- **Fontes:** OpenAlex, Crossref, arXiv, Semantic Scholar, páginas de editoras, GitHub e PyPI. Sem consulta autenticada a Scopus ou Web of Science.
- **Origem dos registros:** 80 do documento de revisão original (P01–P80) e 105 acrescentados nesta coleta (P81 em diante).
- **Pasta `coleta/`:** 96 PDFs de acesso aberto, com nomes `ID_Autor-Ano_titulo.pdf`. Veja também [`coleta/_manifesto.csv`](coleta/_manifesto.csv). Os demais são de acesso restrito, sem versão aberta localizada ou bloqueados contra download automático (parte do MDPI e do ScienceDirect, onde o 403 persistiu mesmo com o fallback); use o link da publicação na tabela.
- **Scripts** em [`scripts/`](scripts/) reproduzem a coleta: `build_catalog.py`, `download_pdfs.py`, `download_fallback.py`, `check_tools.py`, `make_readme.py`. Quando uma editora bloqueou o download simples, o fallback usou o `curl_cffi` (a mesma base do Scrapling de `C:\Desenvolvimento\WebScrapping`).
- **Direitos autorais:** os PDFs são de acesso aberto (arXiv, MDPI, Frontiers e repositórios institucionais), baixados para estudo pessoal. Respeite as licenças de cada artigo ao redistribuir.

**Legenda:** ✓ = título, ano e DOI/identificador conferidos em base bibliográfica em 24/10/2026; ○ = não localizado automaticamente (conferir manualmente). A marca não atesta a qualidade metodológica do estudo. Em PDF, `—` indica que não há cópia aberta em `coleta/`.

## Conteúdo

- [Resultado principal e ordem de leitura](#resultado-principal-e-ordem-de-leitura)
- [Revisões](#revisões)
- [Artigos e códigos](#artigos-e-códigos)
  - [A. Planet: aplicações diretas](#a-planet-aplicações-diretas)
  - [B. Séries temporais, edificações e transições semânticas](#b-séries-temporais-edificações-e-transições-semânticas)
  - [C. Detectores profundos e modelos fundacionais](#c-detectores-profundos-e-modelos-fundacionais)
  - [D. Vias, redes viárias e informação cartográfica prévia](#d-vias-redes-viárias-e-informação-cartográfica-prévia)
  - [E. Métodos temporais clássicos e avaliação científica](#e-métodos-temporais-clássicos-e-avaliação-científica)
  - [F. XGBoost, LightGBM e classificação baseada em atributos](#f-xgboost-lightgbm-e-classificação-baseada-em-atributos)
  - [G. Pré-catalogação com SAM, YOLO e representações fundacionais](#g-pré-catalogação-com-sam-yolo-e-representações-fundacionais)
  - [H. Engenharia de dados: do arquivo ao acervo analítico](#h-engenharia-de-dados-do-arquivo-ao-acervo-analítico)
  - [I. Ciência de dados: amostragem, curadoria, qualidade e representação](#i-ciência-de-dados-amostragem-curadoria-qualidade-e-representação)
  - [J. Planet: dados, qualidade, radiometria e fusão](#j-planet-dados-qualidade-radiometria-e-fusão)
  - [K. Planet: aplicações adicionais (florestas, mineração, vias, edificações)](#k-planet-aplicações-adicionais-florestas-mineração-vias-edificações)
  - [L. Desmatamento, degradação e sistemas de alerta](#l-desmatamento-degradação-e-sistemas-de-alerta)
  - [M. Detecção de mudanças: métodos, datasets e revisões adicionais](#m-detecção-de-mudanças-métodos-datasets-e-revisões-adicionais)
  - [N. GeoAI e QGIS: pacotes, plugins e fluxos de trabalho](#n-geoai-e-qgis-pacotes-plugins-e-fluxos-de-trabalho)
- [GeoAI e QGIS: artigos que citam o GeoAI](#geoai-e-qgis-artigos-que-citam-o-geoai)
- [Comentário por artigo](#comentário-por-artigo)
- [Bibliotecas e ferramentas verificadas](#bibliotecas-e-ferramentas-verificadas)
- [Verificação dos links](#verificação-dos-links)
- [Tendências 2024–2026](#tendências-20242026)
- [Guia metodológico do projeto](#guia-metodológico-do-projeto)
- [Estrutura do repositório](#estrutura-do-repositório)

## Resultado principal e ordem de leitura

Para este projeto, o enquadramento mais preciso é **detecção semântica de mudanças em séries temporais de imagens de satélite — SITS-SCD**. Detectar uma diferença de pixels não basta: é necessário distinguir a transição de cobertura, sua persistência e sua incerteza temporal.

| Ordem | Referência | Motivo para começar por ela |
|---|---|---|
| 1 | P01 — Wagner et al. | Aplicação brasileira com Planet NICFI e U-Net para cobertura arbórea e desmatamento |
| 2 | P10 — SpaceNet 7/MUDS | Edificações acompanhadas em mosaicos mensais Planet de aproximadamente 4 m |
| 3 | P12 — DynamicEarthNet | Planet e rótulos semânticos mensais; aproxima-se diretamente da classificação de transições |
| 4 | P13 — Vincent et al. | Séries longas e avaliação explícita da transferência entre locais e períodos |
| 5 | P14 — TSSCD | Formulação conjunta de onde, quando e o que mudou |
| 6 | P02 — Dalagnol et al. | Separa degradação florestal de remoção completa da cobertura |
| 7 | P05 — Zaraza-Aguilera et al. | Compara mudança direta e pós-classificação em séries Planet |
| 8 | P18/P19 — HRSCD e SECOND | Fundamentos para obter classes antes/depois da alteração |
| 9 | P07 — Vizzari | Baseline de machine learning com objetos, texturas e Random Forest |
| 10 | P46 — Olofsson et al. | Como estimar áreas alteradas e avaliar a confiabilidade do mapa |

**Síntese técnica desta revisão:** comparar um baseline de classificação mensal com consistência temporal contra um modelo que aprenda explicitamente a sequência. Para edificações, usar SpaceNet 7 como referência; para mudanças multiclasse, DynamicEarthNet e TSSCD. Essa combinação é uma proposta para o projeto, não uma conclusão experimental já demonstrada nos seus arquivos.

## Revisões

- 2026, [Remote sensing image change detection using deep learning techniques: a comprehensive survey](https://doi.org/10.1007/s10462-026-11501-0) (Lei et al.), Artificial Intelligence Review ✓ · P49 · [PDF](coleta/P49_Lei2026_Remote-sensing-image-change-detection-using-deep-learning-te.pdf)
- 2026, [Change Detection in Remote Sensing Imagery: A Systematic Review of Statistical, Machine Learning, and Deep Learning Methods](https://doi.org/10.3390/rs18152573) (Jabbarizadegan e Fraternali), Remote Sensing ✓ · P50 · —
- 2026, [Measuring the spatial explicitness of GeoAI and geospatial foundation models: A systematic review and future roadmap](https://doi.org/10.1016/j.isprsjprs.2026.08.001) (Zhou et al.), ISPRS Journal of Photogrammetry and Remo… ✓ · P170 · —
- 2025, [Deep learning change detection techniques for optical remote sensing imagery: Status, perspectives and challenges](https://www.sciencedirect.com/science/article/pii/S1569843224006381) (Peng et al.), International Journal of Applied Earth O… ✓ · P48 · —
- 2025, [Toward Label‐Efficient Deep Learning Change Detection for Remote Sensing Imagery: A Comprehensive Review](https://doi.org/10.1111/phor.70021) (Peng et al.), The Photogrammetric Record ✓ · P128 · —
- 2025, [Vision Foundation Models in Remote Sensing: A survey](https://doi.org/10.1109/mgrs.2025.3541952) (Lu et al.), IEEE Geoscience and Remote Sensing Magaz… ✓ · P151 · [PDF](coleta/P151_Lu2025_Vision-Foundation-Models-in-Remote-Sensing-A-survey.pdf)
- 2025, [Towards the next generation of Geospatial Artificial Intelligence](https://doi.org/10.1016/j.jag.2025.104368) (Mai et al.), International Journal of Applied Earth O… ✓ · P172 · [PDF](coleta/P172_Mai2025_Towards-the-next-generation-of-Geospatial-Artificial-Intelli.pdf)
- 2024, [Deforestation detection using deep learning-based semantic segmentation techniques: a systematic review](https://doi.org/10.3389/ffgc.2024.1300060) (Jelas et al.), Frontiers in Forests and Global Change ✓ · P113 · [PDF](coleta/P113_Jelas2024_Deforestation-detection-using-deep-learning-based-semantic-s.pdf)
- 2024, [Deep Learning for Satellite Image Time-Series Analysis: A review](https://doi.org/10.1109/mgrs.2024.3393010) (Miller et al.), IEEE Geoscience and Remote Sensing Magaz… ✓ · P127 · [PDF](coleta/P127_Miller2024_Deep-Learning-for-Satellite-Image-Time-Series-Analysis-A-rev.pdf)
- 2024, [A comprehensive GeoAI review: Progress, Challenges and Outlooks](https://doi.org/10.48550/arXiv.2412.11643) (Boutayeb et al.), arXiv ✓ · P171 · [PDF](coleta/P171_Boutayeb2024_A-comprehensive-GeoAI-review-Progress-Challenges-and-Outlook.pdf)
- 2022, [Using Super-Resolution Algorithms for Small Satellite Imagery: A Systematic Review](https://doi.org/10.1109/jstars.2022.3167646) (Karwowska e Wierzbicki), IEEE Journal of Selected Topics in Appli… ✓ · P90 · [PDF](coleta/P90_Karwowska2022_Using-Super-Resolution-Algorithms-for-Small-Satellite-Imager.pdf)
- 2022, [A Survey on Deep Learning-Based Change Detection from High-Resolution Remote Sensing Images](https://doi.org/10.3390/rs14071552) (Jiang et al.), Remote Sensing ✓ · P125 · —
- 2022, [Deep Learning-Based Change Detection in Remote Sensing Images: A Review](https://doi.org/10.3390/rs14040871) (Shafique et al.), Remote Sensing ✓ · P126 · [PDF](coleta/P126_Shafique2022_Deep-Learning-Based-Change-Detection-in-Remote-Sensing-Image.pdf)
- 2021, [A Technical Review of Planet Smallsat Data: Practical Considerations for Processing and Using PlanetScope Imagery](https://doi.org/10.3390/rs13193930) (Frazier e Hemingway), Remote Sensing ✓ · P81 · —

## Artigos e códigos

### A. Planet: aplicações diretas

Estudos que usam Planet/PlanetScope/NICFI diretamente. Ponto de partida para supressão vegetal, degradação e mudanças de cobertura.

| ID | Ano | Título | Tipo | Publicação | Código | PDF |
|----|-----|--------|------|------------|--------|-----|
| P01 | 2023 | Mapping Tropical Forest Cover and Deforestation with Planet NICFI Satellite Images and Deep Learning in Mato Grosso State (Brazil) from 2015 to 2021 ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs15020521) | — | [PDF](coleta/P01_Wagner2023_Mapping-Tropical-Forest-Cover-and-Deforestation-with-Planet-.pdf) |
| P02 | 2023 | Mapping tropical forest degradation with deep learning and Planet NICFI data ✓ | Artigo | [Remote Sensing of Environment](https://doi.org/10.1016/j.rse.2023.113798) | — | — |
| P03 | 2024 | Detection of forest disturbance across California using deep-learning on PlanetScope imagery ✓ | Artigo | [Frontiers in Remote Sensing](https://doi.org/10.3389/frsen.2024.1409400) | — | [PDF](coleta/P03_Carter2024_Detection-of-forest-disturbance-across-California-using-deep.pdf) |
| P04 | 2024 | AI-based Validation of Deforestation Using High-Resolution Satellite Imagery in the Brazilian Amazon ✓ | Artigo | [The international archives of the phot…](https://doi.org/10.5194/isprs-archives-XLVIII-3-2024-583-2024) | — | [PDF](coleta/P04_Wang2024_AI-based-Validation-of-Deforestation-Using-High-Resolution-S.pdf) |
| P05 | 2022 | Change Detection over mining areas using Deep Neural Networks from Planetscope image time series ✓ | Artigo | [IEEE Latin America Transactions](https://latamt.ieeer9.org/index.php/transactions/article/view/6556) | — | — |
| P06 | 2025 | Determination of land use and land cover change using multi-temporal PlanetScope images and deep learning CNN model ✓ | Artigo | [Paddy and Water Environment](https://doi.org/10.1007/s10333-025-01024-9) | — | [PDF](coleta/P06_Simsek2025_Determination-of-land-use-and-land-cover-change-using-multi-.pdf) |
| P07 | 2022 | PlanetScope, Sentinel-2, and Sentinel-1 Data Integration for Object-Based Land Cover Classification in Google Earth Engine ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs14112628) | — | — |
| P08 | 2025 | Evaluating satellite data and deep learning for identifying direct deforestation drivers in Cameroon ✓ | Artigo | [Remote Sensing Applications Society and …](https://doi.org/10.1016/j.rsase.2025.101653) | — | — |
| P09 | 2026 | Tropical dry forest land use/land cover change detection using semi-supervised deep learning algorithms and remote sensing ✓ | Artigo | [Environmental Monitoring and Assessment](https://doi.org/10.1007/s10661-025-14897-4) | — | [PDF](coleta/P09_Gonzalez-Velez2026_Tropical-dry-forest-land-use-land-cover-change-detection-usi.pdf) |

### B. Séries temporais, edificações e transições semânticas

Datasets e métodos para séries temporais e mudança semântica (SpaceNet 7, DynamicEarthNet, TSSCD, HRSCD, SECOND).

| ID | Ano | Título | Tipo | Publicação | Código | PDF |
|----|-----|--------|------|------------|--------|-----|
| P10 | 2021 | The Multi-Temporal Urban Development SpaceNet Dataset ✓ | Dataset | [arXiv](https://arxiv.org/abs/2102.04420) | — | [PDF](coleta/P10_Etten2021_The-Multi-Temporal-Urban-Development-SpaceNet-Dataset.pdf) |
| P11 | 2021 | The SpaceNet Multi-Temporal Urban Development Challenge ✓ | Artigo | [arXiv](https://proceedings.mlr.press/v133/etten21a.html) | [github/SpaceNet7_Multi-Temporal_Solutions](https://github.com/SpaceNetChallenge/SpaceNet7_Multi-Temporal_Solutions) | [PDF](coleta/P11_Etten2021_The-SpaceNet-Multi-Temporal-Urban-Development-Challenge.pdf) |
| P12 | 2022 | DynamicEarthNet: Daily Multi-Spectral Satellite Dataset for Semantic Change Segmentation ✓ | Dataset | [arXiv](https://arxiv.org/abs/2203.12560) | — | [PDF](coleta/P12_Toker2022_DynamicEarthNet-Daily-Multi-Spectral-Satellite-Dataset-for-S.pdf) |
| P13 | 2024 | Satellite Image Time Series Semantic Change Detection: Novel Architecture and Analysis of Domain Shift ✓ | Preprint | [arXiv](https://arxiv.org/abs/2407.07616) | — | [PDF](coleta/P13_Vincent2024_Satellite-Image-Time-Series-Semantic-Change-Detection-Novel-.pdf) |
| P14 | 2024 | Time-series land cover change detection using deep learning-based temporal semantic segmentation ✓ | Artigo | [Remote Sensing of Environment](https://doi.org/10.1016/j.rse.2024.114101) | [github/TSSCD](https://github.com/CUG-BEODL/TSSCD) [link](https://zenodo.org/records/10846539) | — |
| P15 | 2021 | Panoptic Segmentation of Satellite Image Time Series With Convolutional Temporal Attention Networks ✓ | Artigo | [IEEE/CVF International Conference on Com…](https://openaccess.thecvf.com/content/ICCV2021/papers/Garnot_Panoptic_Segmentation_of_Satellite_Image_Time_Series_With_Convolutional_Temporal_ICCV_2021_paper.pdf) | [github/utae-paps](https://github.com/VSainteuf/utae-paps) | [PDF](coleta/P15_Garnot2021_Panoptic-Segmentation-of-Satellite-Image-Time-Series-With-Co.pdf) |
| P16 | 2025 | HiSTENet: History-Integrated Spatial–Temporal Information Extraction Network for Time Series Remote Sensing Image Change Detection ✓ | Artigo | [Remote Sensing](https://www.mdpi.com/2072-4292/17/5/792) | — | — |
| P17 | 2023 | Urban Change Forecasting from Satellite Images ✓ | Artigo | [PFG – Journal of Photogrammetry Remote S…](https://doi.org/10.1007/s41064-023-00258-8) | — | [PDF](coleta/P17_Metzger2023_Urban-Change-Forecasting-from-Satellite-Images.pdf) |
| P18 | 2019 | Multitask Learning for Large-scale Semantic Change Detection ✓ | Preprint | [arXiv](https://arxiv.org/abs/1810.08452) | — | [PDF](coleta/P18_Daudt2018_Multitask-Learning-for-Large-scale-Semantic-Change-Detection.pdf) |
| P19 | 2021 | Asymmetric Siamese Networks for Semantic Change Detection in Aerial Images ✓ | Preprint | [arXiv](https://ieeexplore.ieee.org/document/9555824/) | [captain-whu/](https://captain-whu.github.io/SCD/) | [PDF](coleta/P19_Yang2020_Asymmetric-Siamese-Networks-for-Semantic-Change-Detection-in.pdf) |
| P20 | 2022 | ChangeMask: Deep multi-task encoder-transformer-decoder architecture for semantic change detection ✓ | Artigo | [ISPRS Journal of Photogrammetry and Remo…](https://www.sciencedirect.com/science/article/pii/S0924271621002835) | — | — |
| P21 | 2022 | Bi-Temporal Semantic Reasoning for the Semantic Change Detection in HR Remote Sensing Images ✓ | Artigo | [IEEE Transactions on Geoscience and Remo…](https://iris.unitn.it/handle/11572/400193) | — | [PDF](coleta/P21_Ding2022_Bi-Temporal-Semantic-Reasoning-for-the-Semantic-Change-Detec.pdf) |
| P22 | 2024 | The ClearSCD model: Comprehensively leveraging semantics and change relationships for semantic change detection in high spatial resolution remote sensing imagery ✓ | Artigo | [ISPRS Journal of Photogrammetry and Remo…](https://www.sciencedirect.com/science/article/pii/S0924271624001734) | — | — |

### C. Detectores profundos e modelos fundacionais

Baselines siameses, transformers, Mamba e modelos fundacionais para detecção de mudanças.

| ID | Ano | Título | Tipo | Publicação | Código | PDF |
|----|-----|--------|------|------------|--------|-----|
| P23 | 2018 | Fully Convolutional Siamese Networks for Change Detection ✓ | Artigo | [arXiv](https://arxiv.org/abs/1810.08462) | [github/fully_convolutional_change_detection](https://github.com/rcdaudt/fully_convolutional_change_detection) | [PDF](coleta/P23_Daudt2018_Fully-Convolutional-Siamese-Networks-for-Change-Detection.pdf) |
| P24 | 2020 | A Spatial-Temporal Attention-Based Method and a New Dataset for Remote Sensing Image Change Detection ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs12101662) | [github/STANet](https://github.com/justchenhao/STANet) | — |
| P25 | 2021 | Remote Sensing Image Change Detection With Transformers ✓ | Artigo | [IEEE Transactions on Geoscience and Remo…](https://doi.org/10.1109/TGRS.2021.3095166) | — | [PDF](coleta/P25_Chen2021_Remote-Sensing-Image-Change-Detection-With-Transformers.pdf) |
| P26 | 2022 | A Transformer-Based Siamese Network for Change Detection ✓ | Artigo | [arXiv](https://arxiv.org/abs/2201.01293) | [github/ChangeFormer](https://github.com/wgcban/ChangeFormer) | [PDF](coleta/P26_Bandara2022_A-Transformer-Based-Siamese-Network-for-Change-Detection.pdf) |
| P27 | 2021 | Change Is Everywhere: Single-Temporal Supervised Object Change Detection in Remote Sensing Imagery ✓ | Artigo | [IEEE/CVF International Conference on Com…](https://openaccess.thecvf.com/content/ICCV2021/html/Zheng_Change_Is_Everywhere_Single-Temporal_Supervised_Object_Change_Detection_in_Remote_ICCV_2021_paper.html) | — | [PDF](coleta/P27_Zheng2021_Change-Is-Everywhere-Single-Temporal-Supervised-Object-Chang.pdf) |
| P28 | 2024 | ChangeMamba: Remote Sensing Change Detection With Spatiotemporal State Space Model ✓ | Artigo | [arXiv](https://arxiv.org/abs/2404.03425) | [github/MambaCD](https://github.com/ChenHongruixuan/MambaCD) | [PDF](coleta/P28_Chen2024_ChangeMamba-Remote-Sensing-Change-Detection-With-Spatiotempo.pdf) |
| P29 | 2024 | Segment Any Change ✓ | Artigo | [arXiv](https://arxiv.org/abs/2402.01188) | [github/pytorch-change-models](https://github.com/Z-Zheng/pytorch-change-models) | [PDF](coleta/P29_Zheng2024_Segment-Any-Change.pdf) |
| P30 | 2025 | Semantic-CD: Remote Sensing Image Semantic Change Detection towards Open-vocabulary Setting ✓ | Preprint | [arXiv](https://arxiv.org/abs/2501.06808) | — | [PDF](coleta/P30_Yongshuo2025_Semantic-CD-Remote-Sensing-Image-Semantic-Change-Detection-t.pdf) |
| P31 | 2025 | TextSCD: Leveraging Text-based Semantic Guidance for Remote Sensing Image Semantic Change Detection ✓ | Artigo | [ISPRS annals of the photogrammetry, remo…](https://isprs-annals.copernicus.org/articles/X-G-2025/383/2025/index.html) | — | [PDF](coleta/P31_Huang2025_TextSCD-Leveraging-Text-based-Semantic-Guidance-for-Remote-S.pdf) |
| P32 | 2024 | Prithvi-EO-2.0: A Versatile Multitemporal Foundation Model for Earth Observation Applications ✓ | Preprint | [arXiv](https://arxiv.org/abs/2412.02732) | — | [PDF](coleta/P32_Szwarcman2025_Prithvi-EO-2-0-A-Versatile-Multitemporal-Foundation-Model-fo.pdf) |
| P33 | 2026 | Remote Sensing Change Detection via Weak Temporal Supervision ✓ | Preprint | [arXiv](https://arxiv.org/abs/2601.02126) | — | [PDF](coleta/P33_Bou2026_Remote-Sensing-Change-Detection-via-Weak-Temporal-Supervisio.pdf) |
| P34 | 2026 | Foundation Model-Driven Semantic Change Detection in Remote Sensing Imagery ✓ | Preprint | [arXiv](https://arxiv.org/abs/2602.13780) | [github/PerASCD](https://github.com/SathShen/PerASCD) | [PDF](coleta/P34_Shen2026_Foundation-Model-Driven-Semantic-Change-Detection-in-Remote-.pdf) |
| P35 | 2026 | Seg2Change: Adapting Open-Vocabulary Semantic Segmentation Model for Remote Sensing Change Detection ✓ | Preprint | [arXiv](https://arxiv.org/abs/2604.11231) | [github/Seg2Change](https://github.com/yogurts-sy/Seg2Change) | [PDF](coleta/P35_Su2026_Seg2Change-Adapting-Open-Vocabulary-Semantic-Segmentation-Mo.pdf) |

### D. Vias, redes viárias e informação cartográfica prévia

Mudança em vias e pontes, extração de rede viária e uso de mapas anteriores como informação auxiliar.

| ID | Ano | Título | Tipo | Publicação | Código | PDF |
|----|-----|--------|------|------------|--------|-----|
| P36 | 2025 | RB-SCD: A New Benchmark for Semantic Change Detection of Roads and Bridges in Traffic Scenes ✓ | Preprint | [arXiv](https://arxiv.org/abs/2505.13212) | — | [PDF](coleta/P36_Shu2026_RB-SCD-A-New-Benchmark-for-Semantic-Change-Detection-of-Road.pdf) |
| P37 | 2018 | RoadTracer: Automatic Extraction of Road Networks From Aerial Images ✓ | Artigo | [IEEE Computer Society Conference on Comp…](https://openaccess.thecvf.com/content_cvpr_2018/html/Bastani_RoadTracer_Automatic_Extraction_CVPR_2018_paper.html) | [link](https://roadmaps.csail.mit.edu/roadtracer/) | [PDF](coleta/P37_Bastani2018_RoadTracer-Automatic-Extraction-of-Road-Networks-From-Aerial.pdf) |
| P38 | 2018 | Fully Convolutional Network for Automatic Road Extraction From Satellite Imagery ✓ | Artigo | [IEEE/CVF Conference on Computer Vision a…](https://openaccess.thecvf.com/content_cvpr_2018_workshops/w4/html/Buslaev_Fully_Convolutional_Network_CVPR_2018_paper.html) | — | [PDF](coleta/P38_Buslaev2018_Fully-Convolutional-Network-for-Automatic-Road-Extraction-Fr.pdf) |
| P39 | 2023 | MapFormer: Boosting Change Detection by Using Pre-change Information ✓ | Artigo | [arXiv](https://arxiv.org/abs/2303.17859) | [github/mapformer](https://github.com/mxbh/mapformer) | [PDF](coleta/P39_Bernhard2023_MapFormer-Boosting-Change-Detection-by-Using-Pre-change-Info.pdf) |
| P40 | 2026 | Road Change Detection Using Maps and Aerial Imagery for Digital Map Updating ✓ | Artigo | [대한원격탐사학회지](https://www.kjrs.org/journal/view.html?doi=10.7780%2Fkjrs.2026.42.2.5) | — | [PDF](coleta/P40_Lee2026_Road-Change-Detection-Using-Maps-and-Aerial-Imagery-for-Digi.pdf) |

### E. Métodos temporais clássicos e avaliação científica

BFAST, CCDC, LandTrendr e as práticas de estimativa de área e avaliação de acurácia.

| ID | Ano | Título | Tipo | Publicação | Código | PDF |
|----|-----|--------|------|------------|--------|-----|
| P41 | 2010 | Detecting trend and seasonal changes in satellite image time series ✓ | Artigo | [Remote Sensing of Environment](https://doi.org/10.1016/j.rse.2009.08.014) | — | — |
| P42 | 2014 | Continuous change detection and classification of land cover using all available Landsat data ✓ | Artigo | [Remote Sensing of Environment](https://doi.org/10.1016/j.rse.2014.01.011) | [github/CCDC](https://github.com/GERSL/CCDC) | — |
| P43 | 2010 | Detecting trends in forest disturbance and recovery using yearly Landsat time series: 1. LandTrendr — Temporal segmentation algorithms ✓ | Artigo | [Remote Sensing of Environment](https://doi.org/10.1016/j.rse.2010.07.008) | — | — |
| P44 | 2022 | Demystifying LandTrendr and CCDC temporal segmentation ✓ | Artigo | [International Journal of Applied Earth O…](https://www.sciencedirect.com/science/article/pii/S1569843222000085) | — | — |
| P45 | 2022 | Dynamic World, Near real-time global 10 m land use land cover mapping ✓ | Artigo | [Scientific Data](https://doi.org/10.1038/s41597-022-01307-4) | — | [PDF](coleta/P45_Brown2022_Dynamic-World-Near-real-time-global-10-m-land-use-land-cover.pdf) |
| P46 | 2014 | Good practices for estimating area and assessing accuracy of land change ✓ | Artigo | [Remote Sensing of Environment](https://doi.org/10.1016/j.rse.2014.02.015) | — | — |
| P47 | 2019 | Key issues in rigorous accuracy assessment of land cover products ✓ | Artigo | [Remote Sensing of Environment](https://www.sciencedirect.com/science/article/pii/S0034425719302111) | — | — |

### F. XGBoost, LightGBM e classificação baseada em atributos

Classificadores sobre vetores de atributos (bandas, índices, textura, geometria, contexto, embeddings).

| ID | Ano | Título | Tipo | Publicação | Código | PDF |
|----|-----|--------|------|------------|--------|-----|
| P51 | 2025 | Machine Learning-Based Cerrado Land Cover Classification Using PlanetScope Imagery ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs17030480) | — | — |
| P52 | 2018 | Very High Resolution Object-Based Land Use-Land Cover Urban Classification Using Extreme Gradient Boosting ✓ | Artigo | [IEEE Geoscience and Remote Sensing Lette…](https://doi.org/10.1109/LGRS.2018.2803259) | — | [PDF](coleta/P52_Georganos2018_Very-High-Resolution-Object-Based-Land-Use-Land-Cover-Urban-.pdf) |
| P53 | 2016 | XGBoost: A Scalable Tree Boosting System ✓ | Artigo | [arXiv](https://arxiv.org/abs/1603.02754) | — | [PDF](coleta/P53_Tianqi2016_XGBoost-A-Scalable-Tree-Boosting-System.pdf) |
| P54 | 2026 | An Explainable and Optimized Machine Learning Framework for Multisensor Remote Sensing-Based Land Use and Land Cover Classification ✓ | Artigo | [Transactions in GIS](https://doi.org/10.1111/tgis.70293) | — | — |
| P55 | 2024 | Land use and land cover changes in Notwane watershed, Botswana, using extreme gradient boost (XGBoost) machine learning algorithm ✓ | Artigo | [African Geographical Review](https://doi.org/10.1080/19376812.2024.2424378) | — | — |

### G. Pré-catalogação com SAM, YOLO e representações fundacionais

SAM, Grounded SAM, YOLO e embeddings para gerar um catálogo preliminar de objetos. Segmentar, classificar e ligar identidades no tempo são tarefas distintas.

| ID | Ano | Título | Tipo | Publicação | Código | PDF |
|----|-----|--------|------|------------|--------|-----|
| P56 | 2023 | The Segment Anything Model (SAM) for remote sensing applications: From zero to one shot ✓ | Artigo | [International Journal of Applied Earth O…](https://doi.org/10.1016/j.jag.2023.103540) | — | [PDF](coleta/P56_Osco2023_The-Segment-Anything-Model-SAM-for-remote-sensing-applicatio.pdf) |
| P57 | 2024 | Grounded SAM: Assembling Open-World Models for Diverse Visual Tasks ✓ | Preprint | [arXiv](https://arxiv.org/abs/2401.14159) | — | [PDF](coleta/P57_Ren2024_Grounded-SAM-Assembling-Open-World-Models-for-Diverse-Visual.pdf) |
| P58 | 2026 | YOLOSAM: A YOLO-Guided SAM for Accurate Building Segmentation in Remote Sensing Images ✓ | Artigo | [IEEE Journal of Selected Topics in Appli…](https://doi.org/10.1109/JSTARS.2025.3649081) | — | — |
| P59 | 2025 | Toward unsupervised building extraction from very high-resolution remote sensing images using SAM and CLIP ✓ | Artigo | [GIScience & Remote Sensing](https://doi.org/10.1080/15481603.2025.2543102) | — | — |
| P60 | 2024 | SAMPolyBuild: Adapting the Segment Anything Model for polygonal building extraction ✓ | Artigo | [ISPRS Journal of Photogrammetry and Remo…](https://www.sciencedirect.com/science/article/pii/S0924271624003563) | [github/SAMPolyBuild](https://github.com/wchh-2000/SAMPolyBuild) | — |
| P61 | 2025 | Remote Sensing Extraction of Damaged Buildings in the Shigatse Earthquake, 2025: A Hybrid YOLO-E and SAM2 Approach ✓ | Artigo | [Sensors](https://pubmed.ncbi.nlm.nih.gov/40732502/) | — | — |
| P62 | 2025 | SAM 3: Segment Anything with Concepts ✓ | Preprint | [arXiv](https://arxiv.org/abs/2511.16719) | — | [PDF](coleta/P62_Carion2025_SAM-3-Segment-Anything-with-Concepts.pdf) |
| P63 | 2026 | Promptable Concept Segmentation from Above: Evaluating SAM 3’s Zero-Shot and One-Shot Capabilities in Remote Sensing ✓ | Preprint | [arXiv](https://arxiv.org/html/2607.09583v1) | — | [PDF](coleta/P63_Dabaja2026_Promptable-Concept-Segmentation-from-Above-Evaluating-SAM-3s.pdf) |
| P64 | 2025 | DINOv3 ✓ | Artigo | [arXiv](https://arxiv.org/abs/2508.10104) | — | [PDF](coleta/P64_Simeoni2025_DINOv3.pdf) |
| P65 | 2026 | DINO Soars: DINOv3 for Open-Vocabulary Semantic Segmentation of Remote Sensing Imagery ✓ | Preprint | [arXiv](https://arxiv.org/abs/2605.03175) | [github/DINO_Soars](https://github.com/rfaulk/DINO_Soars) | [PDF](coleta/P65_Faulkenberry2026_DINO-Soars-DINOv3-for-Open-Vocabulary-Semantic-Segmentation-.pdf) |
| P66 | 2025 | AlphaEarth Foundations: An embedding field model for accurate and efficient global mapping from sparse label data ✓ | Preprint | [arXiv](https://arxiv.org/abs/2507.22291) | — | [PDF](coleta/P66_Brown2025_AlphaEarth-Foundations-An-embedding-field-model-for-accurate.pdf) |
| P67 | 2024 | Neural Plasticity-Inspired Multimodal Foundation Model for Earth Observation ✓ | Artigo | [arXiv](https://arxiv.org/abs/2403.15356) | — | [PDF](coleta/P67_Xiong2024_Neural-Plasticity-Inspired-Multimodal-Foundation-Model-for-E.pdf) |

### H. Engenharia de dados: do arquivo ao acervo analítico

Cubos de dados, STAC e processamento sob demanda: grade, tempo, qualidade e rastreabilidade corretos.

| ID | Ano | Título | Tipo | Publicação | Código | PDF |
|----|-----|--------|------|------------|--------|-----|
| P68 | 2020 | Earth Observation Data Cubes for Brazil: Requirements, Methodology and Products ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs12244033) | — | — |
| P69 | 2022 | Building Earth Observation Data Cubes on AWS ✓ | Artigo | [The international archives of the phot…](https://doi.org/10.5194/isprs-archives-XLIII-B3-2022-597-2022) | — | [PDF](coleta/P69_Ferreira2022_Building-Earth-Observation-Data-Cubes-on-AWS.pdf) |
| P70 | 2021 | Satellite Image Time Series Analysis for Big Earth Observation Data ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs13132428) | — | [PDF](coleta/P70_Simoes2021_Satellite-Image-Time-Series-Analysis-for-Big-Earth-Observati.pdf) |
| P71 | 2019 | On-Demand Processing of Data Cubes from Satellite Image Collections with the gdalcubes Library ✓ | Artigo | [Data](https://doi.org/10.3390/data4030092) | — | — |
| P72 | 2021 | The openEO API–Harmonising the Use of Earth Observation Cloud Services Using Virtual Data Cube Functionalities ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs13061125) | — | — |
| P73 | 2026 | Incremental Data Cube Architecture for Sentinel-2 Time Series: Multi-Cube Approaches to Dynamic Baseline Construction ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs18020260) | — | — |
| P74 | 2019 | A spatiotemporal cube model for analyzing satellite image time series: Application to land-cover mapping and change detection ✓ | Artigo | [Remote Sensing of Environment](https://www.sciencedirect.com/science/article/abs/pii/S0034425719302251) | — | — |

### I. Ciência de dados: amostragem, curadoria, qualidade e representação

Validação espacial/temporal, curadoria, aprendizado ativo e controle de qualidade.

| ID | Ano | Título | Tipo | Publicação | Código | PDF |
|----|-----|--------|------|------------|--------|-----|
| P75 | 2017 | Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure ✓ | Artigo | [Ecography](https://doi.org/10.1111/ecog.02881) | — | — |
| P76 | 2025 | Efficient Self-Supervised Learning for Earth Observation via Dynamic Dataset Curation ✓ | Artigo | [arXiv](https://arxiv.org/html/2504.06962v1) | — | [PDF](coleta/P76_Kerdreux2025_Efficient-Self-Supervised-Learning-for-Earth-Observation-via.pdf) |
| P77 | 2019 | Deep learning for multi-modal classification of cloud, shadow and land cover scenes in PlanetScope and Sentinel-2 imagery ✓ | Artigo | [ISPRS Journal of Photogrammetry and Remo…](https://www.sciencedirect.com/science/article/pii/S0924271619302023) | — | — |
| P78 | 2025 | Comparing Active Learning for Satellite Imagery: Contrastive Learning, Diversity, Confidence Sampling, and Cold Start Strategies ✓ | Artigo | [IEEE Journal of Selected Topics in Appli…](https://doi.org/10.1109/JSTARS.2025.3597196) | — | — |
| P79 | 2022 | Scale-MAE: A Scale-Aware Masked Autoencoder for Multiscale Geospatial Representation Learning ✓ | Artigo | [arXiv](https://arxiv.org/abs/2212.14532) | — | [PDF](coleta/P79_Reed2023_Scale-MAE-A-Scale-Aware-Masked-Autoencoder-for-Multiscale-Ge.pdf) |
| P80 | 2025 | BuildingSAM: A Dual-Branch Feature-Augmented Segment Anything Model for Remote Sensing Building Extraction ✓ | Artigo | [IEEE Geoscience and Remote Sensing Lette…](https://doi.org/10.1109/LGRS.2025.3568386) | — | — |

### J. Planet: dados, qualidade, radiometria e fusão

Produtos Planet, disponibilidade temporal, nuvem/sombra, reflectância e fusão com Sentinel-2.

| ID | Ano | Título | Tipo | Publicação | Código | PDF |
|----|-----|--------|------|------------|--------|-----|
| P81 | 2021 | A Technical Review of Planet Smallsat Data: Practical Considerations for Processing and Using PlanetScope Imagery ✓ | Revisão | [Remote Sensing](https://doi.org/10.3390/rs13193930) | — | — |
| P82 | 2021 | A global analysis of the temporal availability of PlanetScope high spatial resolution multi-spectral imagery ✓ | Artigo | [Remote Sensing of Environment](https://doi.org/10.1016/j.rse.2021.112586) | — | — |
| P83 | 2021 | Automatic cloud and cloud shadow detection in tropical areas for PlanetScope satellite images ✓ | Artigo | [Remote Sensing of Environment](https://doi.org/10.1016/j.rse.2021.112604) | — | — |
| P84 | 2021 | Characterization of Planetscope-0 Planetscope-1 surface reflectance and normalized difference vegetation index continuity ✓ | Artigo | [Science of Remote Sensing](https://doi.org/10.1016/j.srs.2021.100014) | — | — |
| P85 | 2022 | A new object-class based gap-filling method for PlanetScope satellite image time series ✓ | Artigo | [Remote Sensing of Environment](https://doi.org/10.1016/j.rse.2022.113136) | — | — |
| P86 | 2020 | PlanetScope Radiometric Normalization and Sentinel-2 Super-Resolution (2.5 m): A Straightforward Spectral-Spatial Fusion of Multi-Satellite Multi-Sensor Images Using Residual Convolutional Neural Networks ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs12152366) | — | — |
| P87 | 2020 | Fusion of Sentinel-2 and PlanetScope time-series data into daily 3 m surface reflectance and wheat LAI monitoring ✓ | Artigo | [International Journal of Applied Earth O…](https://doi.org/10.1016/j.jag.2020.102260) | — | — |
| P88 | 2021 | CubeSats deliver new insights into agricultural water use at daily and 3 m resolutions ✓ | Artigo | [Scientific Reports](https://doi.org/10.1038/s41598-021-91646-w) | — | [PDF](coleta/P88_Aragon2021_CubeSats-deliver-new-insights-into-agricultural-water-use-at.pdf) |
| P89 | 2020 | Deriving high-spatiotemporal-resolution leaf area index for agroecosystems in the U.S. Corn Belt using Planet Labs CubeSat and STAIR fusion data ✓ | Artigo | [Remote Sensing of Environment](https://doi.org/10.1016/j.rse.2019.111615) | — | — |
| P90 | 2022 | Using Super-Resolution Algorithms for Small Satellite Imagery: A Systematic Review ✓ | Revisão | [IEEE Journal of Selected Topics in Appli…](https://doi.org/10.1109/jstars.2022.3167646) | — | [PDF](coleta/P90_Karwowska2022_Using-Super-Resolution-Algorithms-for-Small-Satellite-Imager.pdf) |

### K. Planet: aplicações adicionais (florestas, mineração, vias, edificações)

Estudos aplicados adicionais com Planet e CubeSats em florestas, mineração, vias e edificações.

| ID | Ano | Título | Tipo | Publicação | Código | PDF |
|----|-----|--------|------|------------|--------|-----|
| P91 | 2023 | Monitoring monthly tropical humid forest disturbances with Planet NICFI images in Cameroon ✓ | Artigo | [Agricultural and Forest Meteorology](https://doi.org/10.1016/j.agrformet.2023.109676) | — | [PDF](coleta/P91_Zhang2023_Monitoring-monthly-tropical-humid-forest-disturbances-with-P.pdf) |
| P92 | 2025 | Mapping forest-agroforest frontiers in the Peruvian Amazon with deep learning and PlanetScope satellite data ✓ | Artigo | [Ecological Informatics](https://doi.org/10.1016/j.ecoinf.2025.103034) | — | — |
| P93 | 2025 | Wall‐to‐wall Amazon forest height mapping with Planet NICFI , Aerial LiDAR , and a U‐Net regression model ✓ | Artigo | [Remote Sensing in Ecology and Conservati…](https://doi.org/10.1002/rse2.70041) | — | — |
| P94 | 2025 | Land Cover Transformations in Mining-Influenced Areas Using PlanetScope Imagery, Spectral Indices, and Machine Learning: A Case Study in the Hinterlands de Pernambuco, Brazil ✓ | Artigo | [Land](https://doi.org/10.3390/land14020325) | — | — |
| P95 | 2022 | An evaluation of PlanetScope images for 3D reconstruction and change detection – experimental validations with case studies ✓ | Artigo | [GIScience & Remote Sensing](https://doi.org/10.1080/15481603.2022.2060595) | — | — |
| P96 | 2022 | An MLC and U-Net Integrated Method for Land Use/Land Cover Change Detection Based on Time Series NDVI-Composed Image from PlanetScope Satellite ✓ | Artigo | [Water](https://doi.org/10.3390/w14213363) | — | — |
| P97 | 2020 | A Hierarchical Deep-Learning Approach for Rapid Windthrow Detection on PlanetScope and High-Resolution Aerial Image Data ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs12132121) | — | — |
| P98 | 2022 | Deep learning high resolution burned area mapping by transfer learning from Landsat-8 to PlanetScope ✓ | Artigo | [Remote Sensing of Environment](https://doi.org/10.1016/j.rse.2022.113203) | — | — |
| P99 | 2023 | Land Cover Classification in the Antioquia Region of the Tropical Andes Using NICFI Satellite Data Program Imagery and Semantic Segmentation Techniques ✓ | Dataset | [Data](https://doi.org/10.3390/data8120185) | — | — |
| P100 | 2025 | Detection of rural roads from planet images using convolutional neural networks ✓ | Artigo | [Boletim de Ciências Geodésicas](https://doi.org/10.1590/s1982-21702025000100004) | — | [PDF](coleta/P100_Crato2025_Detection-of-rural-roads-from-planet-images-using-convolutio.pdf) |
| P101 | 2024 | Extraction of Forest Road Information from CubeSat Imagery Using Convolutional Neural Networks ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs16061083) | — | — |
| P102 | 2024 | Mapping the diversity of land uses following deforestation across Africa ✓ | Artigo | [Scientific Reports](https://doi.org/10.1038/s41598-024-52138-9) | — | [PDF](coleta/P102_Masolele2024_Mapping-the-diversity-of-land-uses-following-deforestation-a.pdf) |
| P103 | 2025 | TEMPO: Global Temporal Building Density and Height Estimation from Satellite Imagery ✓ | Preprint | [arXiv](https://doi.org/10.48550/arXiv.2511.12104) | — | [PDF](coleta/P103_Glazer2025_TEMPO-Global-Temporal-Building-Density-and-Height-Estimation.pdf) |
| P104 | 2023 | Smartflow: Enabling Scalable Spatiotemporal Geospatial Research ✓ | Preprint | [arXiv](https://doi.org/10.48550/arXiv.2506.03022) | — | [PDF](coleta/P104_McVicar2023_Smartflow-Enabling-Scalable-Spatiotemporal-Geospatial-Resear.pdf) |
| P105 | 2022 | Tracking Urbanization in Developing Regions with Remote Sensing Spatial-Temporal Super-Resolution ✓ | Preprint | [arXiv](https://doi.org/10.48550/arXiv.2204.01736) | — | [PDF](coleta/P105_He2022_Tracking-Urbanization-in-Developing-Regions-with-Remote-Sens.pdf) |
| P106 | 2023 | An Aligned Multi-Temporal Multi-Resolution Satellite Image Dataset for Change Detection Research ✓ | Dataset | [arXiv](https://doi.org/10.48550/arXiv.2302.12301) | — | [PDF](coleta/P106_Rahul2023_An-Aligned-Multi-Temporal-Multi-Resolution-Satellite-Image-D.pdf) |
| P107 | 2024 | BuildMon: Building Extraction and Change Monitoring in Time Series Remote Sensing Images ✓ | Artigo | [IEEE Journal of Selected Topics in Appli…](https://doi.org/10.1109/jstars.2024.3404781) | — | — |

### L. Desmatamento, degradação e sistemas de alerta

Deep learning para desmatamento (PRODES/DETER), alertas operacionais e mineração ilegal.

| ID | Ano | Título | Tipo | Publicação | Código | PDF |
|----|-----|--------|------|------------|--------|-----|
| P108 | 2020 | Change Detection of Deforestation in the Brazilian Amazon Using Landsat Data and Convolutional Neural Networks ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs12060901) | — | — |
| P109 | 2021 | Deforestation Detection with Fully Convolutional Networks in the Amazon Forest from Landsat-8 and Sentinel-2 Images ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs13245084) | — | — |
| P110 | 2024 | Deep Transformer-Based Network Deforestation Detection in the Brazilian Amazon Using Sentinel-2 Imagery ✓ | Artigo | [IEEE Geoscience and Remote Sensing Lette…](https://doi.org/10.1109/lgrs.2024.3355104) | — | [PDF](coleta/P110_Alshehri2024_Deep-Transformer-Based-Network-Deforestation-Detection-in-th.pdf) |
| P111 | 2022 | Deforestation Detection in the Amazon Using DeepLabv3+ Semantic Segmentation Model Variants ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs14194694) | — | — |
| P112 | 2020 | EVALUATION OF SEMANTIC SEGMENTATION METHODS FOR DEFORESTATION DETECTION IN THE AMAZON ✓ | Artigo | [The international archives of the phot…](https://doi.org/10.5194/isprs-archives-xliii-b3-2020-1497-2020) | — | [PDF](coleta/P112_Andrade2020_EVALUATION-OF-SEMANTIC-SEGMENTATION-METHODS-FOR-DEFORESTATIO.pdf) |
| P113 | 2024 | Deforestation detection using deep learning-based semantic segmentation techniques: a systematic review ✓ | Revisão | [Frontiers in Forests and Global Change](https://doi.org/10.3389/ffgc.2024.1300060) | — | [PDF](coleta/P113_Jelas2024_Deforestation-detection-using-deep-learning-based-semantic-s.pdf) |
| P114 | 2023 | SiamHRnet-OCR: A Novel Deforestation Detection Model with High-Resolution Imagery and Deep Learning ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs15020463) | — | — |
| P115 | 2023 | Crowd-Driven Deep Learning Tracks Amazon Deforestation ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs15215204) | — | [PDF](coleta/P115_McCallum2023_Crowd-Driven-Deep-Learning-Tracks-Amazon-Deforestation.pdf) |
| P116 | 2024 | DETER-RT: The new INPE-TropiSCO deforestation monitoring system in the Amazon biome ✓ | Artigo | [The international archives of the phot…](https://doi.org/10.5194/isprs-archives-xlviii-3-2024-127-2024) | — | [PDF](coleta/P116_Doblas2024_DETER-RT-The-new-INPE-TropiSCO-deforestation-monitoring-syst.pdf) |
| P117 | 2022 | DETER-R: An Operational Near-Real Time Tropical Forest Disturbance Warning System Based on Sentinel-1 Time Series Analysis ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs14153658) | — | [PDF](coleta/P117_Doblas2022_DETER-R-An-Operational-Near-Real-Time-Tropical-Forest-Distur.pdf) |
| P118 | 2024 | Integrating satellite-based forest disturbance alerts improves detection timeliness and confidence ✓ | Artigo | [Environmental Research Letters](https://doi.org/10.1088/1748-9326/ad2d82) | — | [PDF](coleta/P118_Reiche2024_Integrating-satellite-based-forest-disturbance-alerts-improv.pdf) |
| P119 | 2021 | Forest disturbance alerts for the Congo Basin using Sentinel-1 ✓ | Artigo | [Environmental Research Letters](https://doi.org/10.1088/1748-9326/abd0a8) | — | [PDF](coleta/P119_Reiche2021_Forest-disturbance-alerts-for-the-Congo-Basin-using-Sentinel.pdf) |
| P120 | 2024 | A near-real-time tropical deforestation monitoring algorithm based on the CuSum change detection method ✓ | Artigo | [Frontiers in Remote Sensing](https://doi.org/10.3389/frsen.2024.1416550) | — | [PDF](coleta/P120_Ygorra2024_A-near-real-time-tropical-deforestation-monitoring-algorithm.pdf) |
| P121 | 2022 | Change Detection of Amazonian Alluvial Gold Mining Using Deep Learning and Sentinel-2 Imagery ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs14071746) | — | — |
| P122 | 2024 | Uncontrolled Illegal Mining and Garimpo in the Brazilian Amazon ✓ | Artigo | [Nature Communications](https://doi.org/10.1038/s41467-024-54220-2) | — | [PDF](coleta/P122_Cortinhas2024_Uncontrolled-Illegal-Mining-and-Garimpo-in-the-Brazilian-Ama.pdf) |
| P123 | 2020 | Mapping Three Decades of Changes in the Brazilian Savanna Native Vegetation Using Landsat Data Processed in the Google Earth Engine Platform ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs12060924) | — | — |
| P124 | 2013 | High-Resolution Global Maps of 21st-Century Forest Cover Change ✓ | Artigo | [Science](https://doi.org/10.1126/science.1244693) | — | — |

### M. Detecção de mudanças: métodos, datasets e revisões adicionais

Revisões, datasets e arquiteturas adicionais (SAM, modelos fundacionais, supervisão fraca, séries de satélite).

| ID | Ano | Título | Tipo | Publicação | Código | PDF |
|----|-----|--------|------|------------|--------|-----|
| P125 | 2022 | A Survey on Deep Learning-Based Change Detection from High-Resolution Remote Sensing Images ✓ | Revisão | [Remote Sensing](https://doi.org/10.3390/rs14071552) | — | — |
| P126 | 2022 | Deep Learning-Based Change Detection in Remote Sensing Images: A Review ✓ | Revisão | [Remote Sensing](https://doi.org/10.3390/rs14040871) | — | [PDF](coleta/P126_Shafique2022_Deep-Learning-Based-Change-Detection-in-Remote-Sensing-Image.pdf) |
| P127 | 2024 | Deep Learning for Satellite Image Time-Series Analysis: A review ✓ | Revisão | [IEEE Geoscience and Remote Sensing Magaz…](https://doi.org/10.1109/mgrs.2024.3393010) | — | [PDF](coleta/P127_Miller2024_Deep-Learning-for-Satellite-Image-Time-Series-Analysis-A-rev.pdf) |
| P128 | 2025 | Toward Label‐Efficient Deep Learning Change Detection for Remote Sensing Imagery: A Comprehensive Review ✓ | Revisão | [The Photogrammetric Record](https://doi.org/10.1111/phor.70021) | — | — |
| P129 | 2019 | End-to-End Change Detection for High Resolution Satellite Images Using Improved UNet++ ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs11111382) | — | — |
| P130 | 2021 | S2Looking: A Satellite Side-Looking Dataset for Building Change Detection ✓ | Dataset | [Remote Sensing](https://doi.org/10.3390/rs13245094) | — | [PDF](coleta/P130_Shen2021_S2Looking-A-Satellite-Side-Looking-Dataset-for-Building-Chan.pdf) |
| P131 | 2025 | ConvFormer-CD: Hybrid CNN–Transformer With Temporal Attention for Detecting Changes in Remote Sensing Imagery ✓ | Artigo | [IEEE Transactions on Geoscience and Remo…](https://doi.org/10.1109/tgrs.2025.3544651) | — | — |
| P132 | 2025 | SChanger: Change Detection From a Semantic Change and Spatial Consistency Perspective ✓ | Artigo | [IEEE Journal of Selected Topics in Appli…](https://doi.org/10.1109/jstars.2025.3555849) | — | [PDF](coleta/P132_Zhou2025_SChanger-Change-Detection-From-a-Semantic-Change-and-Spatial.pdf) |
| P133 | 2024 | Adapting Segment Anything Model for Change Detection in VHR Remote Sensing Images ✓ | Artigo | [IEEE Transactions on Geoscience and Remo…](https://doi.org/10.1109/tgrs.2024.3368168) | — | [PDF](coleta/P133_Ding2024_Adapting-Segment-Anything-Model-for-Change-Detection-in-VHR-.pdf) |
| P134 | 2024 | SCD-SAM: Adapting Segment Anything Model for Semantic Change Detection in Remote Sensing Imagery ✓ | Artigo | [IEEE Transactions on Geoscience and Remo…](https://doi.org/10.1109/tgrs.2024.3407884) | — | — |
| P135 | 2025 | ASS-CD: Adapting Segment Anything Model and Swin-Transformer for Change Detection in Remote Sensing Images ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs17030369) | — | — |
| P136 | 2025 | BCTDNet: Building Change-Type Detection Networks with the Segment Anything Model in Remote Sensing Images ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs17152742) | — | — |
| P137 | 2024 | A New Learning Paradigm for Foundation Model-Based Remote-Sensing Change Detection ✓ | Artigo | [IEEE Transactions on Geoscience and Remo…](https://doi.org/10.1109/tgrs.2024.3365825) | — | [PDF](coleta/P137_Li2024_A-New-Learning-Paradigm-for-Foundation-Model-Based-Remote-Se.pdf) |
| P138 | 2025 | Recurrent Semantic Change Detection in VHR Remote Sensing Images Using Visual Foundation Models ✓ | Artigo | [IEEE Transactions on Geoscience and Remo…](https://doi.org/10.1109/tgrs.2025.3546808) | — | [PDF](coleta/P138_Zhang2025_Recurrent-Semantic-Change-Detection-in-VHR-Remote-Sensing-Im.pdf) |
| P139 | 2025 | The Change You Want To Detect: Semantic Change Detection In Earth Observation With Hybrid Data Generation ✓ | Artigo | [IEEE Computer Society Conference on Comp…](https://doi.org/10.1109/cvpr52734.2025.00211) | — | [PDF](coleta/P139_Benidir2025_The-Change-You-Want-To-Detect-Semantic-Change-Detection-In-E.pdf) |
| P140 | 2022 | Spatially and Semantically Enhanced Siamese Network for Semantic Change Detection in High-Resolution Remote Sensing Images ✓ | Artigo | [IEEE Journal of Selected Topics in Appli…](https://doi.org/10.1109/jstars.2022.3159528) | — | — |
| P141 | 2025 | HRMS-SCD:A High-Resolution Multi-Scene Satellite Imagery Dataset for Comprehensive Land-Cover Semantic Change Detection ✓ | Dataset | [ISPRS annals of the photogrammetry, remo…](https://doi.org/10.5194/isprs-annals-x-g-2025-323-2025) | — | [PDF](coleta/P141_Guo2025_HRMS-SCD-A-High-Resolution-Multi-Scene-Satellite-Imagery-Dat.pdf) |
| P142 | 2026 | Source-Only Cross-Dataset Building Change Detection with Frozen DINOv3 and Hierarchical Evidence Fusion ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs18162789) | — | — |
| P143 | 2026 | Spatial–Temporal Collaborative Network for Satellite Image Time Series Semantic Change Detection ✓ | Artigo | [IEEE Transactions on Geoscience and Remo…](https://doi.org/10.1109/tgrs.2026.3713303) | — | — |
| P144 | 2024 | Change Captioning for Satellite Images Time Series ✓ | Artigo | [IEEE Geoscience and Remote Sensing Lette…](https://doi.org/10.1109/lgrs.2024.3383163) | — | — |
| P145 | 2025 | UniChange: Unifying Change Detection with Multimodal Large Language Model ✓ | Preprint | [arXiv](https://doi.org/10.48550/arXiv.2511.02607) | — | [PDF](coleta/P145_Zhang2025_UniChange-Unifying-Change-Detection-with-Multimodal-Large-La.pdf) |
| P146 | 2019 | Detecting Urban Changes with Recurrent Neural Networks from Multitemporal Sentinel-2 Data ✓ | Artigo | [IEEE International Geoscience and Remote…](https://doi.org/10.1109/igarss.2019.8900330) | — | [PDF](coleta/P146_Papadomanolaki2019_Detecting-Urban-Changes-with-Recurrent-Neural-Networks-from-.pdf) |
| P147 | 2022 | UCDNet: A Deep Learning Model for Urban Change Detection From Bi-Temporal Multispectral Sentinel-2 Satellite Images ✓ | Artigo | [IEEE Transactions on Geoscience and Remo…](https://doi.org/10.1109/tgrs.2022.3161337) | — | — |
| P148 | 2021 | Self-Supervised Change Detection in Multiview Remote Sensing Images ✓ | Artigo | [IEEE Transactions on Geoscience and Remo…](https://doi.org/10.1109/tgrs.2021.3089453) | — | [PDF](coleta/P148_Chen2021_Self-Supervised-Change-Detection-in-Multiview-Remote-Sensing.pdf) |
| P149 | 2020 | Weakly Supervised Deep Learning for Segmentation of Remote Sensing Imagery ✓ | Artigo | [Remote Sensing](https://doi.org/10.3390/rs12020207) | — | — |
| P150 | 2023 | Fully Convolutional Change Detection Framework With Generative Adversarial Network for Unsupervised, Weakly Supervised and Regional Supervised Change Detection ✓ | Artigo | [IEEE Transactions on Pattern Analysis an…](https://doi.org/10.1109/tpami.2023.3237896) | — | [PDF](coleta/P150_Wu2023_Fully-Convolutional-Change-Detection-Framework-With-Generati.pdf) |
| P151 | 2025 | Vision Foundation Models in Remote Sensing: A survey ✓ | Revisão | [IEEE Geoscience and Remote Sensing Magaz…](https://doi.org/10.1109/mgrs.2025.3541952) | — | [PDF](coleta/P151_Lu2025_Vision-Foundation-Models-in-Remote-Sensing-A-survey.pdf) |
| P152 | 2022 | TorchGeo ✓ | Artigo | [ACM SIGSPATIAL International Conference …](https://doi.org/10.1145/3557915.3560953) | [github/torchgeo](https://github.com/torchgeo/torchgeo) | — |
| P153 | 2024 | Specialized Foundation Models Struggle to Beat Supervised Baselines ✓ | Preprint | [arXiv](https://doi.org/10.48550/arXiv.2411.02796) | — | [PDF](coleta/P153_Xu2024_Specialized-Foundation-Models-Struggle-to-Beat-Supervised-Ba.pdf) |
| P154 | 2024 | Uncertainty and Generalizability in Foundation Models for Earth Observation ✓ | Preprint | [arXiv](https://doi.org/10.48550/arXiv.2409.08744) | — | [PDF](coleta/P154_Ramos-Pollan2024_Uncertainty-and-Generalizability-in-Foundation-Models-for-Ea.pdf) |

### N. GeoAI e QGIS: pacotes, plugins e fluxos de trabalho

Pacote GeoAI (opengeos), plugins QGIS de deep learning (Deepness, IAMAP, Geo-SAM), MOLUSCE e revisões de GeoAI.

| ID | Ano | Título | Tipo | Publicação | Código | PDF |
|----|-----|--------|------|------------|--------|-----|
| P155 | 2026 | GeoAI: A Python package for integrating artificial intelligence with geospatial data analysis and visualization ✓ | Software | [The Journal of Open Source Software](https://doi.org/10.21105/joss.09605) | [github/geoai](https://github.com/opengeos/geoai) | [PDF](coleta/P155_Wu2026_GeoAI-A-Python-package-for-integrating-artificial-intelligen.pdf) |
| P156 | 2023 | Deepness: Deep neural remote sensing plugin for QGIS ✓ | Software | [SoftwareX](https://doi.org/10.1016/j.softx.2023.101495) | [github/qgis-plugin-deepness](https://github.com/PUTvision/qgis-plugin-deepness) | — |
| P157 | 2026 | IAMAP: Unlocking Deep Learning in QGIS for non-coders and limited computing resources ✓ | Software | [The Journal of Open Source Software](https://doi.org/10.21105/joss.10329) | [github/iamap](https://github.com/umr-lops/iamap) | [PDF](coleta/P157_Tresson2026_IAMAP-Unlocking-Deep-Learning-in-QGIS-for-non-coders-and-lim.pdf) |
| P158 | 2025 | Evaluating AI-Driven Automated Map Digitization in QGIS ✓ | Preprint | [arXiv](https://doi.org/10.48550/arXiv.2504.18777) | — | [PDF](coleta/P158_Febrita2025_Evaluating-AI-Driven-Automated-Map-Digitization-in-QGIS.pdf) |
| P159 | 2024 | Land Classification Plugin for QGIS Using Pix2Pix ✓ | Software | [ISPRS annals of the photogrammetry, remo…](https://doi.org/10.5194/isprs-annals-x-5-2024-33-2024) | — | [PDF](coleta/P159_Cubillas2024_Land-Classification-Plugin-for-QGIS-Using-Pix2Pix.pdf) |
| P160 | 2026 | SemanticSeg4EO: An open-source unified framework and QGIS plugin for semantic segmentation in Earth Observation ✓ | Software | [SoftwareX](https://doi.org/10.1016/j.softx.2026.102741) | — | — |
| P161 | 2026 | YOLO-MOD: YOLO-based multi-category object detection plugin for maritime, aviation, and infrastructure objects in optical remote sensing images in QGIS ✓ | Software | [SoftwareX](https://doi.org/10.1016/j.softx.2026.102721) | — | — |
| P162 | 2025 | TreeEyed: A QGIS plugin for tree monitoring in silvopastoral systems using state of the art AI models ✓ | Software | [SoftwareX](https://doi.org/10.1016/j.softx.2025.102071) | — | — |
| P163 | 2026 | Spectral Imaging Deep Learning Mapper - SpecDeepMap: An open-source EnMAP-Box semantic segmentation application for hyper- and multispectral mapping ✓ | Software | [SoftwareX](https://doi.org/10.1016/j.softx.2025.102481) | — | — |
| P164 | 2024 | Geo-Sam: Testing the Reliability and Limits of Mine Feature Delineation Using Segment Anything Model ✓ | Preprint | [SSRN Electronic Journal](https://doi.org/10.2139/ssrn.4786825) | [github/Geo-SAM](https://github.com/coolzhao/Geo-SAM) | — |
| P165 | 2025 | MO-SAM: Testing the reliability and limits of mine feature delineation using Segment Anything Model to democratize mine observation and research ✓ | Artigo | [PLOS Sustainability and Transformation](https://doi.org/10.1371/journal.pstr.0000182) | — | [PDF](coleta/P165_Wang2025_MO-SAM-Testing-the-reliability-and-limits-of-mine-feature-de.pdf) |
| P166 | 2026 | Systematic evaluation of SAM prompting strategies for agricultural land extraction with GeoSAM ✓ | Artigo | [Geocarto International](https://doi.org/10.1080/10106049.2026.2717446) | — | — |
| P167 | 2023 | samgeo: A Python package for segmenting geospatial data with the Segment Anything Model (SAM) ✓ | Software | [The Journal of Open Source Software](https://doi.org/10.21105/joss.05663) | [github/segment-geospatial](https://github.com/opengeos/segment-geospatial) | [PDF](coleta/P167_Wu2023_samgeo-A-Python-package-for-segmenting-geospatial-data-with-.pdf) |
| P168 | 2020 | geemap: A Python package for interactive mapping with Google Earth Engine ✓ | Software | [The Journal of Open Source Software](https://doi.org/10.21105/joss.02305) | [github/geemap](https://github.com/gee-community/geemap) | [PDF](coleta/P168_Wu2020_geemap-A-Python-package-for-interactive-mapping-with-Google-.pdf) |
| P169 | 2021 | Semi-Automatic Classification Plugin: A Python tool for the download and processing of remote sensing images in QGIS ✓ | Software | [The Journal of Open Source Software](https://doi.org/10.21105/joss.03172) | [github/SemiAutomaticClassificationPlugin](https://github.com/semiautomaticgit/SemiAutomaticClassificationPlugin) | [PDF](coleta/P169_Congedo2021_Semi-Automatic-Classification-Plugin-A-Python-tool-for-the-d.pdf) |
| P170 | 2026 | Measuring the spatial explicitness of GeoAI and geospatial foundation models: A systematic review and future roadmap ✓ | Revisão | [ISPRS Journal of Photogrammetry and Remo…](https://doi.org/10.1016/j.isprsjprs.2026.08.001) | — | — |
| P171 | 2024 | A comprehensive GeoAI review: Progress, Challenges and Outlooks ✓ | Revisão | [arXiv](https://doi.org/10.48550/arXiv.2412.11643) | — | [PDF](coleta/P171_Boutayeb2024_A-comprehensive-GeoAI-review-Progress-Challenges-and-Outlook.pdf) |
| P172 | 2025 | Towards the next generation of Geospatial Artificial Intelligence ✓ | Revisão | [International Journal of Applied Earth O…](https://doi.org/10.1016/j.jag.2025.104368) | — | [PDF](coleta/P172_Mai2025_Towards-the-next-generation-of-Geospatial-Artificial-Intelli.pdf) |
| P173 | 2024 | On the Opportunities and Challenges of Foundation Models for GeoAI (Vision Paper) ✓ | Artigo | [ACM Transactions on Spatial Algorithms a…](https://doi.org/10.1145/3653070) | — | — |
| P174 | 2026 | Remote SAMsing: From segment anything to segment everything ✓ | Artigo | [International Journal of Applied Earth O…](https://doi.org/10.1016/j.jag.2026.105528) | — | — |
| P175 | 2023 | AN END-TO-END DEEP LEARNING WORKFLOW FOR BUILDING SEGMENTATION, BOUNDARY REGULARIZATION AND VECTORIZATION OF BUILDING FOOTPRINTS ✓ | Artigo | [The international archives of the phot…](https://doi.org/10.5194/isprs-archives-xlviii-4-w7-2023-169-2023) | — | [PDF](coleta/P175_Sanca2023_AN-END-TO-END-DEEP-LEARNING-WORKFLOW-FOR-BUILDING-SEGMENTATI.pdf) |
| P176 | 2025 | Globally Scalable, QGIS-Integrated Workflow for Solar Photovoltaic System Segmentation and Capacity Estimation: A Case Study in Algeria ✓ | Artigo | [IEEE International Geoscience and Remote…](https://doi.org/10.1109/igarss55030.2025.11242710) | — | — |
| P177 | 2024 | Remote detection of asbestos-cement roofs: Evaluating a QGIS plugin in a low- and middle-income country ✓ | Artigo | [Remote Sensing Applications Society and …](https://doi.org/10.1016/j.rsase.2024.101351) | — | — |
| P178 | 2026 | GSIP: A Model-Agnostic Framework for Scalable Geospatial Inference ✓ | Artigo | [Lecture notes in networks and systems](https://doi.org/10.1007/978-3-032-32729-1_47) | — | — |
| P179 | 2026 | Advancing Earth Observation Through Machine Learning: A TorchGeo Tutorial ✓ | Software | [arXiv](https://doi.org/10.48550/arXiv.2603.02386) | [github/torchgeo](https://github.com/torchgeo/torchgeo) | [PDF](coleta/P179_Robinson2026_Advancing-Earth-Observation-Through-Machine-Learning-A-Torch.pdf) |
| P180 | 2022 | Spatiotemporal Change Analysis and Prediction of Future Land Use and Land Cover Changes Using QGIS MOLUSCE Plugin and Remote Sensing Big Data: A Case Study of Linyi, China ✓ | Artigo | [Land](https://doi.org/10.3390/land11030419) | — | — |
| P181 | 2023 | Exploring LULC changes in Pakhal Lake area, Telangana, India using QGIS MOLUSCE plugin ✓ | Artigo | [Spatial Information Research](https://doi.org/10.1007/s41324-023-00509-1) | — | — |
| P182 | 2024 | Spatiotemporal LULC change detection and future prediction for the Mand catchment using MOLUSCE tool ✓ | Artigo | [Environmental Earth Sciences](https://doi.org/10.1007/s12665-023-11381-5) | — | — |
| P183 | 2022 | Modeling Land Use Change in Sana’a City of Yemen with MOLUSCE ✓ | Artigo | [Journal of Sensors](https://doi.org/10.1155/2022/7419031) | — | — |
| P184 | 2022 | Prediction and Simulation of Land Use and Land Cover Changes Using Open Source QGIS. A Case Study of Purwokerto, Central Java, Indonesia ✓ | Artigo | [Indonesian Journal of Geography](https://doi.org/10.22146/ijg.68702) | — | [PDF](coleta/P184_Ramadan2022_Prediction-and-Simulation-of-Land-Use-and-Land-Cover-Changes.pdf) |
| P185 | 2025 | Simulation of Land Use and Land Cover Using the MOLUSCE Plugin Integrated with QGIS for the Western Himalayan Region of India ✓ | Artigo | [The international archives of the phot…](https://doi.org/10.5194/isprs-archives-xlviii-m-5-2024-81-2025) | — | [PDF](coleta/P185_Kumari2025_Simulation-of-Land-Use-and-Land-Cover-Using-the-MOLUSCE-Plug.pdf) |

## GeoAI e QGIS: artigos que citam o GeoAI

Consulta feita em 24/10/2026 no OpenAlex (citações indexadas) e nas páginas oficiais do projeto:

- **Existe um artigo citável do pacote:** Wu, Q. (2026). *GeoAI: A Python package for integrating artificial intelligence with geospatial data analysis and visualization*. Journal of Open Source Software, 11(118), 9605. https://doi.org/10.21105/joss.09605 (**P155**).
- **O plugin QGIS faz parte do pacote.** O README do repositório [opengeos/geoai](https://github.com/opengeos/geoai) lista a "integração com o QGIS por um plugin dedicado" (código na pasta `qgis_plugin`; documentação em https://opengeoai.org/qgis_plugin/). **Não localizei um artigo separado só do plugin.** O trabalho a citar é o do JOSS.
- **Pacote:** PyPI `geoai-py` 0.43.1, licença MIT, Python >=3.12.
- **Trabalhos que citam o JOSS do GeoAI (OpenAlex, 24/10/2026):** o índice mostrou apenas 4, o que reflete a publicação recente (fev/2026) e o atraso de indexação:
  1. Zhou, Huang, Wang e Mai (2026). *Measuring the spatial explicitness of GeoAI and geospatial foundation models: a systematic review and future roadmap*. ISPRS J. Photogramm. Remote Sens. https://doi.org/10.1016/j.isprsjprs.2026.08.001 (**P170**).
  2. Le Guillou, A. (2026). *SemanticSeg4EO: an open-source unified framework and QGIS plugin for semantic segmentation in Earth Observation*. SoftwareX. https://doi.org/10.1016/j.softx.2026.102741 (**P160**).
  3. Polanco et al. (2026). *Dry forest wood and fiber provision for traditional crafts and its potential impact on woody cactus (Leptocereus paniculatus) populations in the Dominican Republic*. Conservation, 6(4), 127. https://doi.org/10.3390/conservation6040127 (aplicação ecológica; fora do escopo de mudança de cobertura).
  4. Fraser et al. (2026). *A multi-year assessment of oak response to spongy moth using uncrewed aerial vehicles*. J. Earth Obs. Geospat. Appl. https://doi.org/10.65372/ptapac10 (aplicação com UAV; fora do escopo).
- **Outros plugins QGIS de deep learning com artigo:** Deepness (**P156**, SoftwareX 2023), IAMAP (**P157**), Geo-SAM e MO-SAM, Land Classification Plugin com Pix2Pix, SemanticSeg4EO, YOLO-MOD, TreeEyed e SpecDeepMap, todos na seção N. O Deepness acumula citações de plugins posteriores (YOLO-MOD, SemanticSeg4EO, TreeEyed, GSIP).
- **Mudança de cobertura no QGIS:** o plugin MOLUSCE (previsão de uso/cobertura por autômatos celulares e redes neurais) tem vários estudos aplicados, listados na seção N. Nenhum deles usa mosaicos Planet mensais nem substitui um modelo temporal.
- **Limite:** nenhum artigo localizado combina GeoAI/QGIS com mosaicos Planet mensais para eventos de mudança. A integração é uma oportunidade de implementação (pré-anotar no QGIS, rodar o modelo e revisar o resultado), não um fluxo validado.

## Comentário por artigo

Os registros P01–P80 reproduzem a revisão original; os de P81 em diante trazem a relevância para o projeto, e o resumo do artigo não foi lido integralmente.

### A. Planet: aplicações diretas

**[P01] Wagner et al. 2023 — Mapping Tropical Forest Cover and Deforestation with Planet NICFI Satellite Images and Deep Learning in Mato Grosso State (Brazil) from 2015 to 2021.** ✓ _Referência:_ Wagner, F. H. et al., 2023. Remote Sensing, 15(2), 521. Artigo aplicado. _Método/dados:_ U-Net para cobertura arbórea e acompanhamento de perda usando Planet NICFI, aproximadamente 5 m. _Aplicação:_ principal ponto de partida para a frente de supressão vegetal no Brasil. _Limite:_ cobertura arbórea/não arbórea não distingue automaticamente construções, ruas e todas as formações vegetais; observar a mudança histórica da cadência NICFI.

**[P02] Dalagnol et al. 2023 — Mapping tropical forest degradation with deep learning and Planet NICFI data.** ✓ _Referência:_ Dalagnol, R. et al., 2023. Remote Sensing of Environment. Artigo aplicado. _Método/dados:_ deep learning com U-Net e Planet NICFI para degradação; incorpora padrões de perda de árvores e textura. _Aplicação:_ permite formular uma classe de degradação, além da supressão completa. _Limite:_ transferir para outros biomas e tipos de perturbação exige novos exemplos; degradação não se resume a transição floresta → não floresta.

**[P03] Carter et al. 2024 — Detection of forest disturbance across California using deep-learning on PlanetScope imagery.** ✓ _Referência:_ Carter, G.; Wagner, F. H.; Dalagnol, R.; Roberts, S.; Ritz, A. L.; Saatchi, S., 2024. Frontiers in Remote Sensing. _Método/dados:_ U-Net, mosaicos visuais RGB a 4,77 m, mapas mensais de 2020–2022 e pós-processamento temporal. _Aplicação:_ especialmente relevante se seus mosaicos forem RGB, sem NIR. _Limite:_ contexto florestal e climático diferente. O artigo apresenta avaliações distintas de cobertura e perturbação; não confundir a acurácia da cobertura com a precisão de eventos de mudança.

**[P04] Wang et al. 2024 — AI-based Validation of Deforestation Using High-Resolution Satellite Imagery in the Brazilian Amazon.** ✓ _Referência:_ Wang, Z.; Li, Z.; Xie, Y.; Souza Jr., C.; Souza Filho, J. S.; Pinheiro, S., 2024. ISPRS Archives. _Método/dados:_ pares PlanetScope antes/depois para confirmar desmatamento candidato indicado por produtos de menor resolução. _Aplicação:_ arquitetura em duas etapas: gerar candidatos e verificar mudanças em alta resolução. _Limite:_ confirmar alertas não demonstra capacidade de encontrar todas as mudanças fora das áreas candidatas.

**[P05] Zaraza-Aguilera et al. 2022 — Change Detection over mining areas using Deep Neural Networks from Planetscope image time series.** ✓ _Referência:_ Zaraza-Aguilera, M. A.; Upegui, E. S.; Espejo-Valero, O. J., 2022. IEEE Latin America Transactions, 20(9), 2196–2205. _Método/dados:_ mina de Cerrejón, Colômbia; compara pós-classificação com U-Net/FPN a detecção direta por U-Net modificada em pares da série. _Aplicação:_ evidência para comparar duas estratégias no seu piloto, incluindo solo exposto e alteração de grandes superfícies. _Limite:_ desempenho em mineração não garante distinção entre obra, terraplenagem, via e solo naturalmente exposto. A página disponibiliza links de PDF e código.

**[P06] Şimşek 2025 — Determination of land use and land cover change using multi-temporal PlanetScope images and deep learning CNN model.** ✓ _Referência:_ Şimşek, F. F., 2025. Paddy and Water Environment, 23, 405–423. _Método/dados:_ PlanetScope de 3 m, oito bandas, múltiplas datas e CNN; comparação com blocos cadastrais LPIS. _Aplicação:_ classificação multitemporal e localização de áreas que exigem atualização cartográfica. _Limite:_ não é equivalente a datar mensalmente cada mudança. Disponibilidade de oito bandas e qualidade temporal do cadastro precisam ser verificadas; o texto apresenta referências distintas ao ano de base do LPIS.

**[P07] Vizzari 2022 — PlanetScope, Sentinel-2, and Sentinel-1 Data Integration for Object-Based Land Cover Classification in Google Earth Engine.** ✓ _Referência:_ Vizzari, M., 2022. Remote Sensing, 14(11), 2628. _Método/dados:_ Random Forest, segmentação em objetos, textura e integração de sensores; classificação de cobertura no Brasil. _Aplicação:_ baseline de ML para testar se o custo adicional do deep learning produz benefício real. _Limite:_ classificar cobertura em uma composição não equivale a validar transições mensais; o estudo é complementar à detecção de mudanças.

**[P08] Debus et al. 2025 — Evaluating satellite data and deep learning for identifying direct deforestation drivers in Cameroon.** ✓ _Referência:_ 2025. Remote Sensing Applications: Society and Environment. Registro editorial localizado; autoria completa deve ser importada do artigo. _Método/dados:_ comparação de dados de satélite e deep learning para categorias associadas ao desmatamento, incluindo composições Planet NICFI. _Aplicação:_ investigar a ocupação posterior à perda vegetal, indo além do mapa binário. _Limite:_ inferência de atividade associada à mudança não determina, por si, sua causa ou responsabilidade. Síntese baseada no registro/resumo indexado; abertura integral não obtida nesta busca.

**[P09] Gonzalez-Velez et al. 2026 — Tropical dry forest land use/land cover change detection using semi-supervised deep learning algorithms and remote sensing.** ✓ _Referência:_ González-Vélez, J. C. et al., 2026. Environmental Monitoring and Assessment, 198, 197. Publicado em 2/2/2026, apesar do DOI conter 2025. _Método/dados:_ pseudorrótulos, Y-Net, óptico/radar, PlanetScope e composições para floresta tropical seca na Colômbia. _Aplicação:_ escassez de rótulos e confusão entre formações vegetais, áreas abertas e regeneração. _Limite:_ composições anuais/semestrais reduzem a informação intranual; não replicar esse passo se o objetivo central for datar eventos mensais.

### B. Séries temporais, edificações e transições semânticas

**[P10] Etten et al. 2021 — The Multi-Temporal Urban Development SpaceNet Dataset.** ✓ _Referência:_ Van Etten, A. et al., 2021. CVPR. Artigo de dataset — MUDS/SpaceNet 7. _Método/dados:_ mosaicos Planet de aproximadamente 4 m, cerca de 24 observações mensais por local e polígonos de edificações com identidade temporal. _Aplicação:_ referência prioritária para novas construções e acompanhamento de objetos em resolução próxima à sua. _Limite:_ o desempenho depende do tamanho e separabilidade dos edifícios; não valida automaticamente contornos cadastrais precisos.

**[P11] Etten e Daniel 2021 — The SpaceNet Multi-Temporal Urban Development Challenge.** ✓ _Referência:_ Van Etten, A.; Hogan, D., 2021. PMLR, 133, 216–232. Resultados da competição. _Método/dados:_ comparação de soluções para localizar e rastrear edificações na série SpaceNet 7. _Aplicação:_ consultar desenho da avaliação, associação entre meses e soluções reproduzíveis. _Limite:_ compartilha o benchmark de P10; não é uma validação independente em outro sensor ou município.

**[P12] Toker et al. 2022 — DynamicEarthNet: Daily Multi-Spectral Satellite Dataset for Semantic Change Segmentation.** ✓ _Referência:_ Toker, A. et al., 2022. CVPR. Dataset e benchmarks. _Método/dados:_ observações Planet de 75 áreas, imagens diárias e rótulos mensais de sete classes; inclui métrica SCS para mudança semântica temporal. _Aplicação:_ benchmark central para mudanças multiclasse, e não apenas edifícios. _Limite:_ imagens diárias/Planet Fusion e mosaicos mensais convencionais não são o mesmo produto. Não presumir equivalência radiométrica ou temporal.

**[P13] Vincent et al. 2024 — Satellite Image Time Series Semantic Change Detection: Novel Architecture and Analysis of Domain Shift.** ✓ _Referência:_ Vincent, E.; Ponce, J.; Aubry, M., 2024. Preprint consultado. _Método/dados:_ arquitetura temporal avaliada em DynamicEarthNet e MUDS, com separação de mudanças de domínio espacial e temporal. _Aplicação:_ fundamenta avaliar anos e áreas inéditos, em vez de apenas sortear patches da mesma paisagem. _Limite:_ o artigo evidencia dificuldades com mudanças raras e transferência; usar uma série longa não elimina a necessidade de rótulos representativos.

**[P14] He et al. 2024 — Time-series land cover change detection using deep learning-based temporal semantic segmentation.** ✓ _Referência:_ He, H.; Yan, J.; Liang, D.; Sun, Z.; Li, J.; Wang, L., 2024. Remote Sensing of Environment, 305, 114101. _Método/dados:_ TSSCD; composições mensais Sentinel-2 de 10/20 m para estimar localização, momento e tipo de alteração. _Aplicação:_ correspondência conceitual muito alta com o projeto. _Limite:_ arquitetura temporal relevante, mas resolução e bandas diferentes das suas.

**[P15] Garnot e Landrieu 2021 — Panoptic Segmentation of Satellite Image Time Series With Convolutional Temporal Attention Networks.** ✓ _Referência:_ Sainte Fare Garnot, V.; Landrieu, L., 2021. ICCV. _Método/dados:_ U-TAE, PaPs e PASTIS; atenção temporal em séries Sentinel-2. _Aplicação:_ referência de encoder espaço-temporal para aproveitar várias observações. _Limite:_ segmentação agrícola/panóptica não é um detector pronto de supressão e construção; exige adaptação da tarefa e dos rótulos.

**[P16] Zhao et al. 2025 — HiSTENet: History-Integrated Spatial–Temporal Information Extraction Network for Time Series Remote Sensing Image Change Detection.** ✓ _Referência:_ 2025. Remote Sensing, 17(5), 792. _Método:_ detecção temporal com integração do histórico espacial e temporal. _Aplicação:_ candidato adicional para comparar histórico multitemporal com pares isolados. _Limite:_ confirmar no texto integral quantidade de entradas, datasets e recursos de reprodução antes de selecionar para implementação; inclusão baseada na página editorial indexada.

**[P17] Metzger et al. 2023 — Urban Change Forecasting from Satellite Images.** ✓ _Referência:_ 2023. PFG — Journal of Photogrammetry, Remote Sensing and Geoinformation Science. _Método/dados:_ previsão de mudança urbana usando SpaceNet 7 e aprendizado com arquitetura siamesa/U-Net. _Aplicação:_ extensão futura para previsão de expansão, depois de validar mudanças observadas. _Limite:_ **forecasting é previsão**, não evidência de que uma nova construção já existe.

**[P18] Daudt et al. 2019 — Multitask Learning for Large-scale Semantic Change Detection.** ✓ _Referência:_ Daudt, R. C.; Le Saux, B.; Boulch, A.; Gousseau, Y., 2019. Computer Vision and Image Understanding; preprint de 2018. _Método/dados:_ HRSCD e aprendizado conjunto de classificação de cobertura e mudança. _Aplicação:_ base para dois mapas semânticos e uma máscara de mudança coerentes entre si. _Limite:_ imagens aéreas RGB e condições diferentes de Planet; não transferir números de desempenho diretamente.

**[P19] Yang et al. 2021 — Asymmetric Siamese Networks for Semantic Change Detection in Aerial Images.** ✓ _Referência:_ Yang, K. et al., 2021. IEEE TGRS; preprint de 2020 com título ligeiramente diferente. _Método/dados:_ ASN, dataset SECOND e métrica SeK; modelagem de classes antes/depois. _Aplicação:_ organizar avaliação de transições semânticas. _Limite:_ benchmark bitemporal não resolve sozinho a cronologia de uma série de vários anos.

**[P20] Zheng et al. 2022 — ChangeMask: Deep multi-task encoder-transformer-decoder architecture for semantic change detection.** ✓ _Referência:_ 2022. ISPRS Journal of Photogrammetry and Remote Sensing. _Método:_ arquitetura multitarefa que conecta segmentação semântica e mudança. _Aplicação:_ candidato a modelo conjunto para evitar divergência entre “mudou” e classes previstas. _Limite:_ testar consistência e transferência local; não representa automaticamente séries mensais inteiras.

**[P21] Ding et al. 2022 — Bi-Temporal Semantic Reasoning for the Semantic Change Detection in HR Remote Sensing Images.** ✓ _Referência:_ Ding, L.; Guo, H.; Liu, S.; Mou, L.; Zhang, J.; Bruzzone, L., 2022. IEEE TGRS. _Método:_ raciocínio semântico bitemporal para localizar mudanças e categorizar coberturas anteriores e posteriores. _Aplicação:_ reduzir inconsistências na interpretação das transições. _Limite:_ necessita exemplos das classes e condições do local; pares de datas continuam exigindo consolidação temporal.

**[P22] Tang et al. 2024 — The ClearSCD model: Comprehensively leveraging semantics and change relationships for semantic change detection in high spatial resolution remote sensing imagery.** ✓ _Referência:_ 2024. ISPRS Journal of Photogrammetry and Remote Sensing. _Método:_ relações semânticas entre datas e comparação no espaço de probabilidades de classificação. _Aplicação:_ avaliar transições com probabilidades, não apenas subtrair rótulos rígidos. _Limite:_ probabilidades do modelo precisam ser avaliadas/calibradas para uso como confiança operacional.

### C. Detectores profundos e modelos fundacionais

**[P23] Daudt et al. 2018 — Fully Convolutional Siamese Networks for Change Detection.** ✓ _Referência:_ Daudt, R. C.; Le Saux, B.; Boulch, A., 2018. ICIP. _Método:_ FC-EF, FC-Siam-conc e FC-Siam-diff, comparando imagens corregistradas. _Aplicação:_ baseline profundo simples, importante para comparar com redes mais complexas. _Limite:_ normalmente produz mudança binária; requer outra saída para dizer o que mudou.

**[P24] Chen e Shi 2020 — A Spatial-Temporal Attention-Based Method and a New Dataset for Remote Sensing Image Change Detection.** ✓ _Referência:_ Chen, H.; Shi, Z., 2020. Remote Sensing, 12(10), 1662. _Método/dados:_ STANet e LEVIR-CD, referência de mudanças em edificações. _Aplicação:_ atenção espacial/temporal e avaliação de construção. _Limite:_ LEVIR-CD não tem a mesma resolução dos mosaicos Planet de 3–5 m.

**[P25] Chen et al. 2021 — Remote Sensing Image Change Detection With Transformers.** ✓ _Referência:_ Chen, H.; Qi, Z.; Shi, Z. Publicação online em 2021, volume 60 de IEEE TGRS, 2022. _Método:_ BIT, transformer bitemporal para incorporar contexto de longo alcance. _Aplicação:_ baseline de transformer para mudança binária. _Limite:_ contexto amplo não recupera objetos que a resolução da imagem não representa adequadamente.

**[P26] Bandara e Patel 2022 — A Transformer-Based Siamese Network for Change Detection.** ✓ _Referência:_ Bandara, W. G. C.; Patel, V. M., 2022. IGARSS — ChangeFormer. _Método:_ rede siamesa com transformers para pares corregistrados. _Aplicação:_ comparar com U-Net/FC-Siam sob os mesmos dados, rótulos e orçamento. _Limite:_ adaptação para bandas adicionais e saída semântica deve ser explícita.

**[P27] Zheng et al. 2021 — Change Is Everywhere: Single-Temporal Supervised Object Change Detection in Remote Sensing Imagery.** ✓ _Referência:_ Zheng, Z.; Ma, A.; Zhang, L.; Zhong, Y., 2021. ICCV — ChangeStar/STAR. _Método:_ aprendizado de mudança a partir de supervisão de uma única data. _Aplicação:_ aproveitar mapas e polígonos disponíveis quando faltam pares anotados. _Limite:_ supervisão construída não substitui teste independente em mudanças reais.

**[P28] Chen et al. 2024 — ChangeMamba: Remote Sensing Change Detection With Spatiotemporal State Space Model.** ✓ _Referência:_ Chen, H.; Song, J.; Han, C.; Xia, J.; Yokoya, N., 2024. Versão consultada no arXiv. _Método:_ variantes MambaBCD, MambaSCD e MambaBDA para mudança binária, semântica e danos. _Aplicação:_ candidato moderno para comparar eficiência e desempenho semântico. _Limite:_ o nome espaço-temporal não implica aceitar qualquer comprimento de série sem modificação.

**[P29] Zheng et al. 2024 — Segment Any Change.** ✓ _Referência:_ Zheng, Z.; Zhong, Y.; Zhang, L.; Ermon, S., 2024. NeurIPS. _Método:_ AnyChange; adaptação sem treinamento do SAM por correspondência latente bitemporal. _Aplicação:_ gerar candidatos e apoiar exploração/anotação com pouca supervisão. _Limite:_ capacidade zero-shot não garante taxa aceitável de falsos positivos em mosaicos Planet; testar deslocamentos, textura e sombras.

**[P30] Yongshuo et al. 2025 — Semantic-CD: Remote Sensing Image Semantic Change Detection towards Open-vocabulary Setting.** ✓ _Referência:_ 2025. Preprint consultado. _Método:_ CLIP, prompts semânticos e decodificação de mudança binária/semântica. _Aplicação:_ investigar categorias descritas por texto e assistência à classificação. _Limite:_ vocabulário aberto não equivale a reconhecer com confiabilidade toda classe territorial local.

**[P31] Huang et al. 2025 — TextSCD: Leveraging Text-based Semantic Guidance for Remote Sensing Image Semantic Change Detection.** ✓ _Referência:_ 2025. ISPRS Annals, X-G-2025, 383. _Método:_ orientação textual para predição de alterações semânticas. _Aplicação:_ avaliar se descrições de classes ajudam na separação das transições. _Limite:_ textos não fornecem, sozinhos, comprovação física da mudança.

**[P32] Szwarcman et al. 2024 — Prithvi-EO-2.0: A Versatile Multitemporal Foundation Model for Earth Observation Applications.** ✓ _Referência:_ Szwarcman, D. et al.; preprint de 2024 e publicação em IEEE TGRS, volume 64, 2026. _Método:_ modelo fundacional multitemporal para observação da Terra. _Aplicação:_ backbone candidato, principalmente em experimentos que integrem outras fontes. _Limite:_ não é detector Planet pronto. Conferir bandas, normalização, resolução e requisitos do checkpoint antes de ajustar.

**[P33] Bou et al. 2026 — Remote Sensing Change Detection via Weak Temporal Supervision.** ✓ _Referência:_ Bou, X.; Vincent, E.; Facciolo, G.; Grompone von Gioi, R.; Morel, J.-M.; Ehret, T., 2026. Preprint. _Método:_ observações temporais adicionais e supervisão fraca para reduzir novas anotações. _Aplicação:_ aproveitar seu acervo longo com rótulos limitados. _Limite:_ a hipótese de predominância de não mudança cria rótulos ruidosos; avaliar separadamente bairros/áreas em rápida transformação.

**[P34] Shen et al. 2026 — Foundation Model-Driven Semantic Change Detection in Remote Sensing Imagery.** ✓ _Referência:_ Shen, H. et al., 2026. Preprint — PerASCD. _Método:_ modelo fundacional, decoder com gates e consistência semântica. _Aplicação:_ candidato recente para fine-tuning semântico. _Limite:_ resultados em benchmarks não comprovam operação em seus mosaicos mensais.

**[P35] Su et al. 2026 — Seg2Change: Adapting Open-Vocabulary Semantic Segmentation Model for Remote Sensing Change Detection.** ✓ _Referência:_ Su, Y.; Song, Y.; Chen, J.; Wen, Z., 2026. Preprint. _Método:_ adaptação de segmentação de vocabulário aberto à detecção de mudanças; dataset CA-CDD. _Aplicação:_ linha exploratória para novas categorias sem refazer toda a taxonomia de treinamento. _Limite:_ tratar como pesquisa a avaliar, não como substituição imediata de modelos supervisionados localmente.

### D. Vias, redes viárias e informação cartográfica prévia

**[P36] Shu et al. 2025 — RB-SCD: A New Benchmark for Semantic Change Detection of Roads and Bridges in Traffic Scenes.** ✓ _Referência:_ Shu, Q.; Chen, S.; You, Z.; Lu, W.; Tang, J.; Luo, B., 2025. Preprint consultado. _Método/dados:_ 260 pares de imagens de alta resolução, 11 categorias de mudança em vias/pontes e modelo MFDCD. _Aplicação:_ taxonomia e detecção de construção, reforma e remoção de infraestrutura viária. _Limite:_ categorias finas podem ser incompatíveis com 3–5 m. Confirmar tamanho dos alvos e resolução do benchmark antes de transferir.

**[P37] Bastani et al. 2018 — RoadTracer: Automatic Extraction of Road Networks From Aerial Images.** ✓ _Referência:_ Bastani, F. et al., 2018. CVPR. _Método:_ extração da rede viária como estrutura conectada. _Aplicação:_ fundamentar avaliação de conectividade, além de sobreposição de pixels. _Limite:_ extração em uma data não é detecção temporal; imagens e escalas distintas de Planet.

**[P38] Buslaev et al. 2018 — Fully Convolutional Network for Automatic Road Extraction From Satellite Imagery.** ✓ _Referência:_ Buslaev, A. et al., 2018. CVPR Workshops. _Método:_ rede da família U-Net para extração viária no DeepGlobe. _Aplicação:_ baseline de máscara de vias, depois combinável entre datas. _Limite:_ pixel de via em duas datas não basta para diferenciar abertura, pavimentação e alteração de iluminação.

**[P39] Bernhard et al. 2023 — MapFormer: Boosting Change Detection by Using Pre-change Information.** ✓ _Referência:_ Bernhard, M.; Strauß, N.; Schubert, M., 2023. ICCV. _Método:_ detecção condicionada por mapas semânticos prévios. _Aplicação:_ usar cartografia existente como informação adicional para localizar atualizações. _Limite:_ mapa anterior desatualizado ou mal alinhado pode induzir erros. Avaliar qualidade e data da referência.

**[P40] Lee et al. 2026 — Road Change Detection Using Maps and Aerial Imagery for Digital Map Updating.** ✓ _Referência:_ Lee, J. et al., 2026. Korean Journal of Remote Sensing, 42(2). _Método:_ adaptação do MapFormer para atualização viária, mapas e ortofotos; tratamento do desbalanceamento. _Aplicação:_ caso específico de mudança em ruas, complementar a P39. _Limite:_ ortofotos de alta resolução e contexto sul-coreano; não tratar a transferência para Planet como demonstrada.

### E. Métodos temporais clássicos e avaliação científica

**[P41] Verbesselt et al. 2010 — Detecting trend and seasonal changes in satellite image time series.** ✓ _Referência:_ Verbesselt, J.; Hyndman, R.; Newnham, G.; Culvenor, D., 2010. Remote Sensing of Environment, 114(1), 106–115. _Método:_ BFAST, decomposição de tendência e sazonalidade com detecção de rupturas. _Aplicação:_ baseline temporal para distinguir sazonalidade de mudança persistente. _Limite:_ ruptura espectral não fornece automaticamente a classe posterior. Método estatístico, não deep learning.

**[P42] Zhu e Woodcock 2014 — Continuous change detection and classification of land cover using all available Landsat data.** ✓ _Referência:_ Zhu, Z.; Woodcock, C. E., 2014. Remote Sensing of Environment. _Método:_ CCDC, modelagem contínua, detecção de rupturas e classificação. _Aplicação:_ referência para separar detecção do evento e atribuição da cobertura. _Limite:_ entrada Landsat, bandas e densidade observacional diferentes. Não aplicar parâmetros originais a Planet sem calibração.

**[P43] Kennedy et al. 2010 — Detecting trends in forest disturbance and recovery using yearly Landsat time series: 1. LandTrendr — Temporal segmentation algorithms.** ✓ _Referência:_ Kennedy, R. E.; Yang, Z.; Cohen, W. B., 2010. Remote Sensing of Environment, 114, 2897–2910. _Método:_ segmentação temporal de trajetórias anuais de perturbação e recuperação. _Aplicação:_ produto anual complementar e interpretação de regeneração. _Limite:_ não é a primeira escolha para localizar meses de mudança em uma série de apenas sete anos.

**[P44] Pasquarella et al. 2022 — Demystifying LandTrendr and CCDC temporal segmentation.** ✓ _Referência:_ 2022. International Journal of Applied Earth Observation and Geoinformation. _Método/contribuição:_ explica diferenças entre segmentações LandTrendr e CCDC. _Aplicação:_ orientar escolha de frequência temporal e interpretação dos segmentos. _Limite:_ referência metodológica complementar; não constitui validação direta com Planet.

**[P45] Brown et al. 2022 — Dynamic World, Near real-time global 10 m land use land cover mapping.** ✓ _Referência:_ Brown, C. F. et al., 2022. Scientific Data, 9, 251. _Método/dados:_ deep learning para cobertura Sentinel-2 com probabilidades por classe. _Aplicação:_ fonte auxiliar de contexto, comparação e eventual pré-rotulagem. _Limite:_ não usar como verdade de campo independente se seus rótulos ou modelo derivarem do próprio produto; 10 m não resolve detalhamento de edificações em 3–5 m.

**[P46] Olofsson et al. 2014 — Good practices for estimating area and assessing accuracy of land change.** ✓ _Referência:_ Olofsson, P.; Foody, G. M.; Herold, M.; Stehman, S. V.; Woodcock, C. E.; Wulder, M. A., 2014. Remote Sensing of Environment, 148, 42–57. _Contribuição:_ amostragem probabilística, matriz de erro, estimativas de área e intervalos de confiança. _Aplicação:_ essencial para sustentar quantos hectares mudaram e a incerteza associada. _Limite:_ contar pixels classificados fornece área mapeada; não equivale, por si, a uma estimativa de área corrigida pelos erros.

**[P47] Stehman e Foody 2019 — Key issues in rigorous accuracy assessment of land cover products.** ✓ _Referência:_ 2019. Remote Sensing of Environment. Artigo metodológico/revisão de avaliação. _Contribuição:_ desenho e documentação rigorosos de validação de mapas. _Aplicação:_ auditar independência da amostra, referência e inferência das métricas. _Limite:_ não substitui um protocolo local para datas incertas, alvos pequenos e mudanças raras.

### F. XGBoost, LightGBM e classificação baseada em atributos

**[P51] Rodrigues et al. 2025 — Machine Learning-Based Cerrado Land Cover Classification Using PlanetScope Imagery.** ✓ _Referência:_ Rodrigues, T.; Takahashi, F.; Dias, A.; Lima, T.; Alcântara, E., 2025. Remote Sensing, 17(3), 480. _Evidência direta:_ compara **XGBoost, Random Forest e SVM em PlanetScope de 4,77 m** para classes de cobertura do Cerrado. _Resultado contextualizado:_ tabela 5 apresenta F1 ponderado de 0,97 para XGBoost. Os testes entre classificadores apresentados não indicam diferenças significativas; não há suporte para afirmar superioridade geral do XGBoost. _Aplicação:_ baseline prioritário de cobertura vegetal. É classificação, não validação de todas as transições mensais ou de edifícios. Não transportar a acurácia publicada para outra região.

**[P52] Georganos et al. 2018 — Very High Resolution Object-Based Land Use-Land Cover Urban Classification Using Extreme Gradient Boosting.** ✓ _Referência:_ Georganos, S.; Grippa, T.; Vanhuysse, S.; Lennert, M.; Shimoni, M.; Wolff, E., 2018. IEEE Geoscience and Remote Sensing Letters, 15(4), 607–611. _Método:_ XGBoost por objetos, seleção de atributos e parametrização bayesiana; comparação com RF/SVM em ambientes urbanos. _Aplicação:_ fundamento para classificar segmentos por espectro, textura e forma. _Limite:_ classificação urbana VHR, sem demonstração de catálogo temporal Planet. Substituir a segmentação original por SAM constitui um novo experimento.

**[P53] Tianqi e Guestrin 2016 — XGBoost: A Scalable Tree Boosting System.** ✓ _Referência:_ Chen, T.; Guestrin, C., 2016. ACM SIGKDD. _Contribuição:_ artigo do sistema de gradient boosting escalável. _Aplicação:_ fundamentar implementação e processamento de uma tabela de atributos por pixel, objeto ou trajetória. _Limite:_ referência geral de ML; não é um estudo de sensoriamento remoto e não comprova qualidade de classificação Planet.

**[P54] Gündüz et al. 2026 — An Explainable and Optimized Machine Learning Framework for Multisensor Remote Sensing-Based Land Use and Land Cover Classification.** ✓ _Referência:_ Gündüz et al., 2026. Transactions in GIS. _Método:_ RF, XGBoost e LightGBM; cinco estratégias de seleção de atributos; Optuna, validação espacial e SHAP. Usa Sentinel-1/2 e fontes auxiliares. _Aplicação:_ referência especialmente útil de **ciência de dados aplicada**: seleção, otimização e interpretação. No experimento relatado, a combinação de melhor desempenho foi HSIC-Lasso + LightGBM, não XGBoost. _Limite:_ não é série mensal Planet; SHAP explica associações do modelo, não causas físicas da mudança. Seleção e ajuste devem ficar dentro dos dados de treinamento de cada partição.

**[P55] Magidi et al. 2024 — Land use and land cover changes in Notwane watershed, Botswana, using extreme gradient boost (XGBoost) machine learning algorithm.** ✓ _Referência:_ Magidi, J. et al. African Geographical Review. Registro com DOI de 2024 e publicação em volume de 2025; conferir versão bibliográfica final ao importar a citação. _Método/dados:_ classificação Landsat com XGBoost e análise das mudanças em diferentes anos, incluindo vegetação, água, agricultura e áreas construídas. _Aplicação:_ exemplo concreto de XGBoost dentro de um fluxo de mudança por pós-classificação. _Limite:_ Landsat e intervalos longos não demonstram identificação mensal de pequenas obras.

### G. Pré-catalogação com SAM, YOLO e representações fundacionais

**[P56] Osco et al. 2023 — The Segment Anything Model (SAM) for remote sensing applications: From zero to one shot.** ✓ _Referência:_ Osco, L. P. et al., 2023. International Journal of Applied Earth Observation and Geoinformation. _Método:_ explora adaptação e aplicação de SAM no sensoriamento remoto, incluindo segmentação orientada por texto e exemplos. _Aplicação:_ leitura prioritária para gerar máscaras preliminares e reduzir delineamento manual. _Limite:_ máscaras não equivalem a rótulos de referência. Erros devem ser revisados antes de treinamento e quantificados em teste independente.

**[P57] Ren et al. 2024 — Grounded SAM: Assembling Open-World Models for Diverse Visual Tasks.** ✓ _Referência:_ Ren, T. et al., 2024. Preprint consultado. _Método:_ Grounding DINO para detecção de vocabulário aberto combinado ao SAM para segmentação; discute pipelines de anotação automática. _Aplicação:_ texto → caixas candidatas → máscaras → revisão. _Limite:_ artigo de visão geral, não validação específica em mosaicos Planet. O detector pode perder alvos pequenos ou apresentar viés de imagens ao nível do solo.

**[P58] Hussain et al. 2026 — YOLOSAM: A YOLO-Guided SAM for Accurate Building Segmentation in Remote Sensing Images.** ✓ _Referência:_ Hussain, M. et al. IEEE JSTARS, 19, 4403–4417, 2026; DOI/publicação online de 2025. _Método:_ gerador de prompts de caixas baseado em YOLOv8, combinado a adaptações de SAM para segmentação de edificações; avalia WHU, Vaihingen e Inria. _Aplicação:_ exemplo direto da catalogação prévia sugerida: detector localiza, segmentador delimita. _Limite:_ não assumir que as resoluções dos benchmarks equivalem a 3–5 m. Um detector que omite um edifício também pode impedir que SAM o segmente.

**[P59] Zhang e Yue 2025 — Toward unsupervised building extraction from very high-resolution remote sensing images using SAM and CLIP.** ✓ _Referência:_ 2025. GIScience & Remote Sensing. _Método:_ SAM segmenta objetos; modelo visão-linguagem ajuda a separar edifício/não edifício e construir pseudorrótulos; uma etapa posterior aprende o extrator. _Aplicação:_ referência muito próxima da ideia de criar previamente um catálogo de objetos para treinamento. _Limite:_ supervisão automática continua sujeita a erros sistemáticos. Não avaliar o resultado apenas contra os próprios pseudorrótulos. Síntese baseada no registro editorial indexado.

**[P60] Wang et al. 2024 — SAMPolyBuild: Adapting the Segment Anything Model for polygonal building extraction.** ✓ _Referência:_ Wang, C. et al., 2024. ISPRS Journal of Photogrammetry and Remote Sensing, 218, 707–720. _Método:_ adapta SAM à extração de polígonos de edificações. _Aplicação:_ aproxima a saída do modelo de objetos GIS utilizáveis no catálogo. _Limite:_ um polígono regular não prova contorno correto. Em Planet de 5 m, a qualidade geométrica precisa ser reportada por tamanho de objeto e referência independente.

**[P61] Wu et al. 2025 — Remote Sensing Extraction of Damaged Buildings in the Shigatse Earthquake, 2025: A Hybrid YOLO-E and SAM2 Approach.** ✓ _Referência:_ 2025. Artigo aplicado. _Método/dados:_ YOLO-E e SAM2 em imagens de aproximadamente 0,15–0,80 m para edificações danificadas. _Aplicação:_ demonstra integração detector–segmentador em sensoriamento remoto. _Limite:_ dano de construção e resolução submétrica são diferentes de surgimento de construções em 3–5 m. Não reutilizar desempenho como expectativa para seus mosaicos.

**[P62] Carion et al. 2025 — SAM 3: Segment Anything with Concepts.** ✓ _Referência:_ Carion, N. et al., 2025. Preprint/artigo dos autores consultado. _Método:_ detecção, segmentação e rastreamento com prompts conceituais textuais ou exemplos visuais. _Aplicação:_ candidato recente para catalogação orientada por conceitos e seleção assistida de objetos. _Limite:_ rastreamento em vídeo não equivale à associação de objetos entre mosaicos mensais com mudanças radiométricas e grandes intervalos. A transferência exige avaliação própria.

**[P63] Dabaja e Çelik 2026 — Promptable Concept Segmentation from Above: Evaluating SAM 3’s Zero-Shot and One-Shot Capabilities in Remote Sensing.** ✓ _Referência:_ Dabaja, M.; Celik, T., julho de 2026. Preprint. _Método:_ avaliação de SAM 3 em classificação de cenas, detecção e segmentação de instâncias no domínio remoto. _Aplicação:_ ajuda a avaliar objetivamente quando texto ou exemplo visual são úteis para pré-catalogar. _Limite:_ os autores relatam dificuldades de transferência e interferência entre modalidades de prompt. É evidência contra presumir confiabilidade zero-shot universal, não uma validação Planet local.

**[P64] Siméoni et al. 2025 — DINOv3.** ✓ _Referência:_ 2025. Artigo dos autores sobre aprendizado autossupervisionado. _Modelo satelital oficial:_ https://huggingface.co/facebook/dinov3-vit7b16-pretrain-sat493m _Método:_ extração de representações densas; inclui treinamento e avaliação em dados geoespaciais. _Aplicação proposta:_ embeddings de patches/objetos para busca por similaridade, agrupamento, seleção de amostras e classificadores supervisionados. _Limite:_ embedding não é classe; agrupamentos não são uma taxonomia validada. O checkpoint indicado é grande, e não uma indicação automática de melhor custo-benefício.

**[P65] Faulkenberry e Prasad 2026 — DINO Soars: DINOv3 for Open-Vocabulary Semantic Segmentation of Remote Sensing Imagery.** ✓ _Referência:_ Faulkenberry, R.; Prasad, S., maio de 2026. Preprint. _Método:_ CAFe-DINO, agregação e aumento de resolução de similaridades texto–imagem para segmentação aberta. _Aplicação:_ candidato de pré-classificação de cenas e cobertura. _Limite:_ ausência de fine-tuning em imagens remotas não significa ausência total de treinamento; o resumo descreve ajuste em subconjunto de COCO-Stuff. Ainda requer teste em Planet.

**[P66] Brown et al. 2025 — AlphaEarth Foundations: An embedding field model for accurate and efficient global mapping from sparse label data.** ✓ _Referência:_ Brown, C. F. et al., 2025. Preprint/relatório dos autores. _Documentação do lançamento:_ https://deepmind.google/blog/alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail/ _Método:_ representações geoespaciais multifuente e lançamento de embeddings anuais. _Aplicação:_ contexto e classificação auxiliar quando há poucos rótulos. _Limite:_ um produto anual não informa diretamente o mês da mudança. Não tratar os embeddings disponibilizados como um encoder público pronto para processar qualquer raster Planet local; são coisas diferentes.

**[P67] Xiong et al. 2024 — Neural Plasticity-Inspired Multimodal Foundation Model for Earth Observation.** ✓ _Referência:_ Xiong, Z. et al., 2024. Versão consultada no arXiv — DOFA. _Método:_ modelo multimodal condicionado por comprimentos de onda, com diferentes sensores. _Aplicação:_ alternativa para investigar entrada multiespectral heterogênea. _Limite:_ flexibilidade de bandas não elimina necessidade de reflectância consistente, normalização, ajuste e avaliação local. Não é solução automática para misturar produtos visuais e analíticos.

### H. Engenharia de dados: do arquivo ao acervo analítico

**[P68] Ferreira et al. 2020 — Earth Observation Data Cubes for Brazil: Requirements, Methodology and Products.** ✓ _Referência:_ Ferreira, K. R. et al., 2020. Remote Sensing, 12(24), 4033 — INPE/Brazil Data Cube. _Página do projeto:_ https://data.inpe.br/bdc/earth-observation-data-cubes-for-brazil-requirements-methodology-and-products/ _Contribuição:_ requisitos, dados prontos para análise, cubos multidimensionais, infraestrutura e serviços. _Aplicação:_ principal referência brasileira para estruturar seu acervo espaço-temporal. _Limite:_ os produtos originais não são Planet; aproveitar princípios de arquitetura, sem presumir parâmetros ou custos equivalentes.

**[P69] Ferreira et al. 2022 — Building Earth Observation Data Cubes on AWS.** ✓ _Referência:_ Ferreira, K. R.; Queiroz, G. R.; Marujo, R. F. B.; Costa, R. W., 2022. ISPRS Archives. _Contribuição:_ construção de cubos de observação da Terra com arquitetura serverless e imagens em armazenamento de objetos. _Aplicação:_ execução por tarefas, paralelismo e processamento de grandes coleções. _Limite:_ referência arquitetural, não recomendação obrigatória de AWS. A escolha entre local, nuvem e processamento distribuído depende do volume e recursos reais.

**[P70] Simões et al. 2021 — Satellite Image Time Series Analysis for Big Earth Observation Data.** ✓ _Referência:_ Simoes, R.; Camara, G.; Queiroz, G.; Souza, F.; Andrade, P. R.; Santos, L.; Carvalho, A.; Ferreira, K., 2021. Remote Sensing, 13(13), 2428. _Contribuição:_ pacote `sits`, integrando cubos temporais e classificação por ML/DL. _Aplicação:_ referência de fluxo completo entre dados e classificação de séries, e não apenas escolha de modelo. _Limite:_ implementação de referência em R. É possível adotar os princípios em Python, mas isso constitui implementação distinta a verificar.

**[P71] Appel e Pebesma 2019 — On-Demand Processing of Data Cubes from Satellite Image Collections with the gdalcubes Library.** ✓ _Referência:_ Appel, M.; Pebesma, E., 2019. Data, 4(3), 92. _Contribuição:_ processamento sob demanda de coleções como cubos, com definição explícita da grade e tempo. _Aplicação:_ evitar materializar combinações completas quando apenas recortes e operações específicas são necessários. _Limite:_ computação sob demanda muda o perfil de I/O e repetição de operações; medir desempenho em vez de pressupor economia.

**[P72] Schramm et al. 2021 — The openEO API–Harmonising the Use of Earth Observation Cloud Services Using Virtual Data Cube Functionalities.** ✓ _Referência:_ Schramm, M. et al., 2021. Remote Sensing. _Fonte institucional:_ https://publications.jrc.ec.europa.eu/repository/handle/JRC122714 _Contribuição:_ interface comum para processamento de dados de observação da Terra com funcionalidades de cubos virtuais. _Aplicação:_ desacoplar especificação analítica e infraestrutura de execução. _Limite:_ suporte efetivo depende do backend e das operações implementadas; interoperabilidade não garante igualdade numérica entre ambientes.

**[P73] Trujillo e Solar 2026 — Incremental Data Cube Architecture for Sentinel-2 Time Series: Multi-Cube Approaches to Dynamic Baseline Construction.** ✓ _Referência:_ 2026. Remote Sensing, 18(2), 260. _Contribuição:_ arquitetura incremental para séries Sentinel-2 e atualização de referências temporais. _Aplicação:_ incorporar o próximo mês sem recomputar indiscriminadamente toda a série 2020–2026. _Limite:_ algoritmo retrospectivo pode exigir reprocessar uma janela maior; definir explicitamente quais produtos são invalidados quando um mosaico histórico é corrigido.

**[P74] Xi et al. 2019 — A spatiotemporal cube model for analyzing satellite image time series: Application to land-cover mapping and change detection.** ✓ _Referência:_ 2019. Remote Sensing of Environment. _Contribuição:_ modelagem espaço-temporal para análise de séries, cobertura e mudança. _Aplicação:_ fundamenta a organização conjunta de espaço, tempo e atributos. _Limite:_ um cubo físico ou virtual não garante homogeneidade semântica dos produtos que contém; manter metadados de origem e qualidade.

### I. Ciência de dados: amostragem, curadoria, qualidade e representação

**[P75] Roberts et al. 2017 — Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure.** ✓ _Referência:_ Roberts, D. R. et al., 2017. Ecography. _Contribuição:_ validação que respeita dependências entre observações. _Aplicação:_ separar bairros/blocos e períodos, evitando a falsa independência de pixels e patches próximos. _Limite:_ estudo metodológico geral; o tamanho do bloco e o teste temporal devem refletir a aplicação. Não há uma distância de separação universal.

**[P76] Kerdreux et al. 2025 — Efficient Self-Supervised Learning for Earth Observation via Dynamic Dataset Curation.** ✓ _Referência:_ Kerdreux, T.; Tuel, A.; Febvre, Q.; Mouche, A.; Chapron, B., 2025. Versão arXiv consultada. _Contribuição:_ seleção dinâmica para reduzir redundância e melhorar diversidade no pré-treinamento. _Aplicação:_ inspira seleção de amostras informativas em vez de treinar com todos os patches repetidos de meses estáveis. _Limite:_ experimentos em Sentinel-1 Wave Mode, predominantemente oceânico. É referência de curadoria, não evidência direta em cobertura terrestre Planet.

**[P77] Shendryk et al. 2019 — Deep learning for multi-modal classification of cloud, shadow and land cover scenes in PlanetScope and Sentinel-2 imagery.** ✓ _Referência:_ 2019. ISPRS Journal of Photogrammetry and Remote Sensing. _Método:_ classificação de nuvens, sombras e cenas, incluindo avaliação de generalização e aplicação a séries densas. _Aplicação:_ uma camada explícita de qualidade antes de detectar mudanças. _Limite:_ nuvem/sombra não são as únicas anomalias: registro geométrico, emendas e diferenças radiométricas também precisam de controle.

**[P78] Pogorzelski et al. 2025 — Comparing Active Learning for Satellite Imagery: Contrastive Learning, Diversity, Confidence Sampling, and Cold Start Strategies.** ✓ _Referência:_ Pogorzelski, D.; Arlinghaus, P. P.; Zhang, W., 2025. IEEE JSTARS, 18, 20678–20689. _Contribuição:_ comparação de estratégias de seleção de amostras para aprendizado ativo. _Aplicação:_ priorizar revisão humana por diversidade, incerteza e representatividade, comparando com seleção aleatória. _Limite:_ não usar apenas baixa confiança: amostras raras que o modelo classifica incorretamente com alta confiança também precisam de auditoria.

**[P79] Reed et al. 2022 — Scale-MAE: A Scale-Aware Masked Autoencoder for Multiscale Geospatial Representation Learning.** ✓ _Referência:_ Reed, C. J. et al. Versão arXiv inicial de 2022. _Contribuição:_ pré-treinamento com representação explícita de escala geográfica e reconstrução multiescala. _Aplicação:_ estudar representações quando o acervo mistura resoluções e tamanhos físicos de objetos. _Limite:_ tratar escalas não recupera detalhes ausentes. Super-resolução e aumento de resolução de features não criam evidência de um telhado que não foi resolvido pelo sensor.

**[P80] Feng et al. 2025 — BuildingSAM: A Dual-Branch Feature-Augmented Segment Anything Model for Remote Sensing Building Extraction.** ✓ _Referência:_ 2025. IEEE Geoscience and Remote Sensing Letters. _Método:_ adaptação de SAM voltada à extração de edificações. _Aplicação:_ candidato especializado para comparar com SAM genérico e YOLO-seg. _Limite:_ inclusão pelo registro editorial; arquitetura, custo de anotação, pesos e compatibilidade Planet devem ser verificados integralmente antes de implementar.

### J. Planet: dados, qualidade, radiometria e fusão

**[P81] Frazier e Hemingway 2021 — A Technical Review of Planet Smallsat Data: Practical Considerations for Processing and Using PlanetScope Imagery.** ✓ _Tipo:_ Revisão. _Relevância:_ Revisão técnica dos produtos Planet: processamento, radiometria e cuidados de uso. Leitura obrigatória antes de comparar meses.

**[P82] Roy et al. 2021 — A global analysis of the temporal availability of PlanetScope high spatial resolution multi-spectral imagery.** ✓ _Tipo:_ Artigo. _Relevância:_ Análise global da disponibilidade temporal de PlanetScope; mede quantas observações úteis realmente existem por local e período.

**[P83] Wang et al. 2021 — Automatic cloud and cloud shadow detection in tropical areas for PlanetScope satellite images.** ✓ _Tipo:_ Artigo. _Relevância:_ Detecção automática de nuvem e sombra em PlanetScope tropical; camada de qualidade antes da detecção de mudança.

**[P84] Huang e Roy 2021 — Characterization of Planetscope-0 Planetscope-1 surface reflectance and normalized difference vegetation index continuity.** ✓ _Tipo:_ Artigo. _Relevância:_ Caracterização de reflectância e NDVI entre PlanetScope-0 e PlanetScope-1; alerta para inconsistências entre gerações de sensores.

**[P85] Wang et al. 2022 — A new object-class based gap-filling method for PlanetScope satellite image time series.** ✓ _Tipo:_ Artigo. _Relevância:_ Preenchimento de lacunas em séries PlanetScope por classe de objeto; útil para meses com nuvem.

**[P86] Latte e Lejeune 2020 — PlanetScope Radiometric Normalization and Sentinel-2 Super-Resolution (2.5 m): A Straightforward Spectral-Spatial Fusion of Multi-Satellite Multi-Sensor Images Using Residual Convolutional Neural Networks.** ✓ _Tipo:_ Artigo. _Relevância:_ Normalização radiométrica de PlanetScope usando Sentinel-2 e super-resolução a 2,5 m.

**[P87] Sadeh et al. 2020 — Fusion of Sentinel-2 and PlanetScope time-series data into daily 3 m surface reflectance and wheat LAI monitoring.** ✓ _Tipo:_ Artigo. _Relevância:_ Fusão Sentinel-2 e PlanetScope em reflectância diária de 3 m; referência para harmonização multissensor.

**[P88] Aragon et al. 2021 — CubeSats deliver new insights into agricultural water use at daily and 3 m resolutions.** ✓ _Tipo:_ Artigo. _Relevância:_ Planet Fusion: dados diários de 3 m por fusão de CubeSats e satélites públicos.

**[P89] Kimm et al. 2020 — Deriving high-spatiotemporal-resolution leaf area index for agroecosystems in the U.S. Corn Belt using Planet Labs CubeSat and STAIR fusion data.** ✓ _Tipo:_ Artigo. _Relevância:_ Índice de área foliar de alta resolução espaço-temporal combinando CubeSats Planet e fusão STARFM no Corn Belt (EUA).

**[P90] Karwowska e Wierzbicki 2022 — Using Super-Resolution Algorithms for Small Satellite Imagery: A Systematic Review.** ✓ _Tipo:_ Revisão. _Relevância:_ Revisão de super-resolução para imagens de pequenos satélites; limite do que a super-resolução realmente recupera.

### K. Planet: aplicações adicionais (florestas, mineração, vias, edificações)

**[P91] Zhang et al. 2023 — Monitoring monthly tropical humid forest disturbances with Planet NICFI images in Cameroon.** ✓ _Tipo:_ Artigo. _Relevância:_ Perturbações florestais mensais com mosaicos Planet NICFI em Camarões; próximo da cadência mensal do projeto.

**[P92] Yang et al. 2025 — Mapping forest-agroforest frontiers in the Peruvian Amazon with deep learning and PlanetScope satellite data.** ✓ _Tipo:_ Artigo. _Relevância:_ Fronteiras floresta–agrofloresta na Amazônia peruana com deep learning e PlanetScope.

**[P93] Wagner et al. 2025 — Wall‐to‐wall Amazon forest height mapping with Planet NICFI , Aerial LiDAR , and a U‐Net regression model.** ✓ _Tipo:_ Artigo. _Relevância:_ Altura de floresta amazônica com Planet NICFI, LiDAR e U-Net; exemplo de uso estrutural dos mosaicos.

**[P94] Pachêco et al. 2025 — Land Cover Transformations in Mining-Influenced Areas Using PlanetScope Imagery, Spectral Indices, and Machine Learning: A Case Study in the Hinterlands de Pernambuco, Brazil.** ✓ _Tipo:_ Artigo. _Relevância:_ Transformações de cobertura em áreas de mineração com PlanetScope, índices espectrais e aprendizado de máquina.

**[P95] Huang et al. 2022 — An evaluation of PlanetScope images for 3D reconstruction and change detection – experimental validations with case studies.** ✓ _Tipo:_ Artigo. _Relevância:_ Avaliação de PlanetScope para reconstrução 3D e detecção de mudanças; limites geométricos das imagens.

**[P96] Wang et al. 2022 — An MLC and U-Net Integrated Method for Land Use/Land Cover Change Detection Based on Time Series NDVI-Composed Image from PlanetScope Satellite.** ✓ _Tipo:_ Artigo. _Relevância:_ MLC e U-Net para mudança de uso/cobertura com série temporal de NDVI.

**[P97] Deigele et al. 2020 — A Hierarchical Deep-Learning Approach for Rapid Windthrow Detection on PlanetScope and High-Resolution Aerial Image Data.** ✓ _Tipo:_ Artigo. _Relevância:_ Detecção hierárquica de áreas de vendaval em PlanetScope e imagens de alta resolução.

**[P98] Martins et al. 2022 — Deep learning high resolution burned area mapping by transfer learning from Landsat-8 to PlanetScope.** ✓ _Tipo:_ Artigo. _Relevância:_ Mapeamento de área queimada em PlanetScope por transferência de aprendizado de Landsat-8.

**[P99] Ossa et al. 2023 — Land Cover Classification in the Antioquia Region of the Tropical Andes Using NICFI Satellite Data Program Imagery and Semantic Segmentation Techniques.** ✓ _Tipo:_ Dataset. _Relevância:_ Classificação de cobertura em Antioquia (Andes) com dados NICFI e rótulos; referência regional de dados.

**[P100] Crato et al. 2025 — Detection of rural roads from planet images using convolutional neural networks.** ✓ _Tipo:_ Artigo. _Relevância:_ Detecção de estradas rurais em imagens Planet com redes convolucionais (autores brasileiros).

**[P101] Winiwarter et al. 2024 — Extraction of Forest Road Information from CubeSat Imagery Using Convolutional Neural Networks.** ✓ _Tipo:_ Artigo. _Relevância:_ Extração de estradas florestais em imagens CubeSat com CNN; escala comparável a 3–5 m.

**[P102] Masolele et al. 2024 — Mapping the diversity of land uses following deforestation across Africa.** ✓ _Tipo:_ Artigo. _Relevância:_ Usos do solo após o desmatamento na África; útil para pensar a classe posterior à perda de floresta.

**[P103] Glazer et al. 2025 — TEMPO: Global Temporal Building Density and Height Estimation from Satellite Imagery.** ✓ _Tipo:_ Preprint. _Relevância:_ TEMPO: densidade e altura de edificações com basemaps PlanetScope trimestrais (2018–2025).

**[P104] McVicar et al. 2023 — Smartflow: Enabling Scalable Spatiotemporal Geospatial Research.** ✓ _Tipo:_ Preprint. _Relevância:_ Smartflow: aprendizado profundo para construção pesada em grandes áreas, incluindo imagens Planet.

**[P105] He et al. 2022 — Tracking Urbanization in Developing Regions with Remote Sensing Spatial-Temporal Super-Resolution.** ✓ _Tipo:_ Preprint. _Relevância:_ Acompanhamento da urbanização com super-resolução espaço-temporal (SpaceNet 7).

**[P106] Rahul et al. 2023 — An Aligned Multi-Temporal Multi-Resolution Satellite Image Dataset for Change Detection Research.** ✓ _Tipo:_ Dataset. _Relevância:_ Dataset multitemporal e multirresolução alinhado para pesquisa em detecção de mudanças.

**[P107] Wang et al. 2024 — BuildMon: Building Extraction and Change Monitoring in Time Series Remote Sensing Images.** ✓ _Tipo:_ Artigo. _Relevância:_ BuildMon: extração e monitoramento de edificações em séries temporais de sensoriamento remoto.

### L. Desmatamento, degradação e sistemas de alerta

**[P108] Bem et al. 2020 — Change Detection of Deforestation in the Brazilian Amazon Using Landsat Data and Convolutional Neural Networks.** ✓ _Tipo:_ Artigo. _Relevância:_ Detecção de desmatamento na Amazônia brasileira com Landsat e CNN; referência clássica de DL para PRODES.

**[P109] Torres et al. 2021 — Deforestation Detection with Fully Convolutional Networks in the Amazon Forest from Landsat-8 and Sentinel-2 Images.** ✓ _Tipo:_ Artigo. _Relevância:_ Redes totalmente convolucionais para desmatamento na Amazônia com Landsat-8 e Sentinel-2.

**[P110] Alshehri et al. 2024 — Deep Transformer-Based Network Deforestation Detection in the Brazilian Amazon Using Sentinel-2 Imagery.** ✓ _Tipo:_ Artigo. _Relevância:_ Rede baseada em transformers para desmatamento na Amazônia com Sentinel-2.

**[P111] Andrade et al. 2022 — Deforestation Detection in the Amazon Using DeepLabv3+ Semantic Segmentation Model Variants.** ✓ _Tipo:_ Artigo. _Relevância:_ Variantes do DeepLabv3+ para desmatamento na Amazônia.

**[P112] Andrade et al. 2020 — EVALUATION OF SEMANTIC SEGMENTATION METHODS FOR DEFORESTATION DETECTION IN THE AMAZON.** ✓ _Tipo:_ Artigo. _Relevância:_ Avaliação de métodos de segmentação semântica para desmatamento na Amazônia.

**[P113] Jelas et al. 2024 — Deforestation detection using deep learning-based semantic segmentation techniques: a systematic review.** ✓ _Tipo:_ Revisão. _Relevância:_ Revisão sistemática de segmentação semântica por deep learning para desmatamento.

**[P114] Wang et al. 2023 — SiamHRnet-OCR: A Novel Deforestation Detection Model with High-Resolution Imagery and Deep Learning.** ✓ _Tipo:_ Artigo. _Relevância:_ SiamHRnet-OCR: modelo siamês para desmatamento em imagens de alta resolução.

**[P115] McCallum et al. 2023 — Crowd-Driven Deep Learning Tracks Amazon Deforestation.** ✓ _Tipo:_ Artigo. _Relevância:_ Deep learning com participação coletiva (crowd) para rastrear desmatamento na Amazônia.

**[P116] Doblas et al. 2024 — DETER-RT: The new INPE-TropiSCO deforestation monitoring system in the Amazon biome.** ✓ _Tipo:_ Artigo. _Relevância:_ DETER-RT: novo sistema de monitoramento de desmatamento do INPE.

**[P117] Doblas et al. 2022 — DETER-R: An Operational Near-Real Time Tropical Forest Disturbance Warning System Based on Sentinel-1 Time Series Analysis.** ✓ _Tipo:_ Artigo. _Relevância:_ DETER-R: sistema operacional de alerta de perturbação florestal baseado em Sentinel-1.

**[P118] Reiche et al. 2024 — Integrating satellite-based forest disturbance alerts improves detection timeliness and confidence.** ✓ _Tipo:_ Artigo. _Relevância:_ Integração de alertas de distúrbio florestal baseados em satélite para melhorar prazo e confiança.

**[P119] Reiche et al. 2021 — Forest disturbance alerts for the Congo Basin using Sentinel-1.** ✓ _Tipo:_ Artigo. _Relevância:_ Alertas de distúrbio florestal na Bacia do Congo com Sentinel-1.

**[P120] Ygorra et al. 2024 — A near-real-time tropical deforestation monitoring algorithm based on the CuSum change detection method.** ✓ _Tipo:_ Artigo. _Relevância:_ Algoritmo quase em tempo real para desmatamento tropical baseado em CuSum.

**[P121] Çamalan et al. 2022 — Change Detection of Amazonian Alluvial Gold Mining Using Deep Learning and Sentinel-2 Imagery.** ✓ _Tipo:_ Artigo. _Relevância:_ Mudança por garimpo aluvial na Amazônia com aprendizado profundo e Sentinel-2.

**[P122] Cortinhas et al. 2024 — Uncontrolled Illegal Mining and Garimpo in the Brazilian Amazon.** ✓ _Tipo:_ Artigo. _Relevância:_ Mineração ilegal (garimpo) na Amazônia brasileira; contexto de uma transição relevante ao projeto.

**[P123] Alencar et al. 2020 — Mapping Three Decades of Changes in the Brazilian Savanna Native Vegetation Using Landsat Data Processed in the Google Earth Engine Platform.** ✓ _Tipo:_ Artigo. _Relevância:_ Três décadas de mudança na vegetação nativa do Cerrado (Landsat/MapBiomas).

**[P124] Hansen et al. 2013 — High-Resolution Global Maps of 21st-Century Forest Cover Change.** ✓ _Tipo:_ Artigo. _Relevância:_ Hansen et al. (2013): mapas globais de mudança da cobertura florestal; base de comparação histórica.

### M. Detecção de mudanças: métodos, datasets e revisões adicionais

**[P125] Jiang et al. 2022 — A Survey on Deep Learning-Based Change Detection from High-Resolution Remote Sensing Images.** ✓ _Tipo:_ Revisão. _Relevância:_ Levantamento de detecção de mudanças por DL em imagens de alta resolução.

**[P126] Shafique et al. 2022 — Deep Learning-Based Change Detection in Remote Sensing Images: A Review.** ✓ _Tipo:_ Revisão. _Relevância:_ Revisão de detecção de mudanças por DL em sensoriamento remoto.

**[P127] Miller et al. 2024 — Deep Learning for Satellite Image Time-Series Analysis: A review.** ✓ _Tipo:_ Revisão. _Relevância:_ Revisão de deep learning para séries temporais de imagens de satélite.

**[P128] Peng et al. 2025 — Toward Label‐Efficient Deep Learning Change Detection for Remote Sensing Imagery: A Comprehensive Review.** ✓ _Tipo:_ Revisão. _Relevância:_ Detecção de mudanças com poucos rótulos: revisão abrangente.

**[P129] Peng et al. 2019 — End-to-End Change Detection for High Resolution Satellite Images Using Improved UNet++.** ✓ _Tipo:_ Artigo. _Relevância:_ UNet++ aprimorada para detecção de mudanças de ponta a ponta.

**[P130] Shen et al. 2021 — S2Looking: A Satellite Side-Looking Dataset for Building Change Detection.** ✓ _Tipo:_ Dataset. _Relevância:_ S2Looking: dataset de edificações com visão lateral para detecção de mudanças.

**[P131] Yang et al. 2025 — ConvFormer-CD: Hybrid CNN–Transformer With Temporal Attention for Detecting Changes in Remote Sensing Imagery.** ✓ _Tipo:_ Artigo. _Relevância:_ ConvFormer-CD: CNN–transformer com atenção temporal para mudanças.

**[P132] Zhou et al. 2025 — SChanger: Change Detection From a Semantic Change and Spatial Consistency Perspective.** ✓ _Tipo:_ Artigo. _Relevância:_ SChanger: detecção de mudanças sob perspectiva de consistência semântica e espacial.

**[P133] Ding et al. 2024 — Adapting Segment Anything Model for Change Detection in VHR Remote Sensing Images.** ✓ _Tipo:_ Artigo. _Relevância:_ Adaptação do SAM para detecção de mudanças em imagens VHR.

**[P134] Mei et al. 2024 — SCD-SAM: Adapting Segment Anything Model for Semantic Change Detection in Remote Sensing Imagery.** ✓ _Tipo:_ Artigo. _Relevância:_ SCD-SAM: SAM adaptado à detecção de mudança semântica.

**[P135] Wei et al. 2025 — ASS-CD: Adapting Segment Anything Model and Swin-Transformer for Change Detection in Remote Sensing Images.** ✓ _Tipo:_ Artigo. _Relevância:_ ASS-CD: SAM e Swin-Transformer para detecção de mudanças.

**[P136] Zhang et al. 2025 — BCTDNet: Building Change-Type Detection Networks with the Segment Anything Model in Remote Sensing Images.** ✓ _Tipo:_ Artigo. _Relevância:_ BCTDNet: tipos de mudança em edificações com SAM.

**[P137] Li et al. 2024 — A New Learning Paradigm for Foundation Model-Based Remote-Sensing Change Detection.** ✓ _Tipo:_ Artigo. _Relevância:_ Novo paradigma de aprendizado para detecção de mudanças com modelo fundacional.

**[P138] Zhang et al. 2025 — Recurrent Semantic Change Detection in VHR Remote Sensing Images Using Visual Foundation Models.** ✓ _Tipo:_ Artigo. _Relevância:_ Mudança semântica recorrente em imagens VHR com modelos visuais fundacionais.

**[P139] Benidir et al. 2025 — The Change You Want To Detect: Semantic Change Detection In Earth Observation With Hybrid Data Generation.** ✓ _Tipo:_ Artigo. _Relevância:_ Detecção de mudança semântica com geração híbrida de dados (CVPR 2025).

**[P140] Zhao et al. 2022 — Spatially and Semantically Enhanced Siamese Network for Semantic Change Detection in High-Resolution Remote Sensing Images.** ✓ _Tipo:_ Artigo. _Relevância:_ Rede siamesa melhorada semântica e espacialmente para mudança semântica em alta resolução.

**[P141] Guo et al. 2025 — HRMS-SCD:A High-Resolution Multi-Scene Satellite Imagery Dataset for Comprehensive Land-Cover Semantic Change Detection.** ✓ _Tipo:_ Dataset. _Relevância:_ HRMS-SCD: dataset multicena de alta resolução para mudança semântica de cobertura.

**[P142] Zhang et al. 2026 — Source-Only Cross-Dataset Building Change Detection with Frozen DINOv3 and Hierarchical Evidence Fusion.** ✓ _Tipo:_ Artigo. _Relevância:_ Detecção de mudança em edificações entre datasets com DINOv3 congelado.

**[P143] Xie et al. 2026 — Spatial–Temporal Collaborative Network for Satellite Image Time Series Semantic Change Detection.** ✓ _Tipo:_ Artigo. _Relevância:_ Rede colaborativa espaço-temporal para mudança semântica em séries de imagens de satélite.

**[P144] Peng et al. 2024 — Change Captioning for Satellite Images Time Series.** ✓ _Tipo:_ Artigo. _Relevância:_ Legendagem de mudanças (change captioning) em séries temporais de satélite.

**[P145] Zhang et al. 2025 — UniChange: Unifying Change Detection with Multimodal Large Language Model.** ✓ _Tipo:_ Preprint. _Relevância:_ UniChange: detecção de mudanças unificada com modelo de linguagem multimodal.

**[P146] Papadomanolaki et al. 2019 — Detecting Urban Changes with Recurrent Neural Networks from Multitemporal Sentinel-2 Data.** ✓ _Tipo:_ Artigo. _Relevância:_ Mudança urbana com redes recorrentes em séries Sentinel-2 (OSCD).

**[P147] Basavaraju et al. 2022 — UCDNet: A Deep Learning Model for Urban Change Detection From Bi-Temporal Multispectral Sentinel-2 Satellite Images.** ✓ _Tipo:_ Artigo. _Relevância:_ UCDNet: mudança urbana em pares Sentinel-2 multiespectrais.

**[P148] Chen e Bruzzone 2021 — Self-Supervised Change Detection in Multiview Remote Sensing Images.** ✓ _Tipo:_ Artigo. _Relevância:_ Detecção de mudanças autossupervisionada em imagens de múltiplas visadas.

**[P149] Wang et al. 2020 — Weakly Supervised Deep Learning for Segmentation of Remote Sensing Imagery.** ✓ _Tipo:_ Artigo. _Relevância:_ Segmentação profunda fracamente supervisionada em sensoriamento remoto.

**[P150] Wu et al. 2023 — Fully Convolutional Change Detection Framework With Generative Adversarial Network for Unsupervised, Weakly Supervised and Regional Supervised Change Detection.** ✓ _Tipo:_ Artigo. _Relevância:_ Detecção de mudanças não supervisionada com GAN e rede totalmente convolucional.

**[P151] Lu et al. 2025 — Vision Foundation Models in Remote Sensing: A survey.** ✓ _Tipo:_ Revisão. _Relevância:_ Levantamento sobre modelos fundacionais de visão em sensoriamento remoto.

**[P152] Stewart et al. 2022 — TorchGeo.** ✓ _Tipo:_ Artigo. _Relevância:_ TorchGeo (SIGSPATIAL 2022): biblioteca de deep learning para dados geoespaciais.

**[P153] Xu et al. 2024 — Specialized Foundation Models Struggle to Beat Supervised Baselines.** ✓ _Tipo:_ Preprint. _Relevância:_ Modelos fundacionais especializados têm dificuldade em superar baselines supervisionados; cautela para P32/P64.

**[P154] Ramos-Pollán et al. 2024 — Uncertainty and Generalizability in Foundation Models for Earth Observation.** ✓ _Tipo:_ Preprint. _Relevância:_ Incerteza e generalização em modelos fundacionais para observação da Terra.

### N. GeoAI e QGIS: pacotes, plugins e fluxos de trabalho

**[P155] Wu 2026 — GeoAI: A Python package for integrating artificial intelligence with geospatial data analysis and visualization.** ✓ _Tipo:_ Software. _Relevância:_ Artigo do pacote GeoAI (opengeos/geoai, PyPI geoai-py), que inclui plugin para QGIS: busca/baixa dados, prepara datasets, treina e infere modelos.

**[P156] Aszkowski et al. 2023 — Deepness: Deep neural remote sensing plugin for QGIS.** ✓ _Tipo:_ Software. _Relevância:_ Deepness: plugin QGIS que executa modelos ONNX de segmentação, detecção e regressão em camadas raster.

**[P157] Tresson et al. 2026 — IAMAP: Unlocking Deep Learning in QGIS for non-coders and limited computing resources.** ✓ _Tipo:_ Software. _Relevância:_ IAMAP: plugin QGIS para extração de características com modelos fundacionais autossupervisionados, agrupamento e mapas de similaridade.

**[P158] Febrita 2025 — Evaluating AI-Driven Automated Map Digitization in QGIS.** ✓ _Tipo:_ Preprint. _Relevância:_ Avaliação do Deepness para digitalização automática de mapas, comparada ao OpenStreetMap (F1).

**[P159] Cubillas et al. 2024 — Land Classification Plugin for QGIS Using Pix2Pix.** ✓ _Tipo:_ Software. _Relevância:_ Plugin QGIS de classificação de cobertura com Pix2Pix (aplicado principalmente a Landsat).

**[P160] Guillou 2026 — SemanticSeg4EO: An open-source unified framework and QGIS plugin for semantic segmentation in Earth Observation.** ✓ _Tipo:_ Software. _Relevância:_ SemanticSeg4EO: framework e plugin QGIS para segmentação semântica em observação da Terra; cita o GeoAI.

**[P161] Ciecholewski et al. 2026 — YOLO-MOD: YOLO-based multi-category object detection plugin for maritime, aviation, and infrastructure objects in optical remote sensing images in QGIS.** ✓ _Tipo:_ Software. _Relevância:_ YOLO-MOD: plugin QGIS de detecção de objetos baseado em YOLO.

**[P162] Ruiz-Hurtado et al. 2025 — TreeEyed: A QGIS plugin for tree monitoring in silvopastoral systems using state of the art AI models.** ✓ _Tipo:_ Software. _Relevância:_ TreeEyed: plugin QGIS para monitoramento de árvores com modelos de IA.

**[P163] Thomas et al. 2026 — Spectral Imaging Deep Learning Mapper - SpecDeepMap: An open-source EnMAP-Box semantic segmentation application for hyper- and multispectral mapping.** ✓ _Tipo:_ Software. _Relevância:_ SpecDeepMap: aplicação de segmentação semântica para o EnMAP-Box (QGIS).

**[P164] Wang et al. 2024 — Geo-Sam: Testing the Reliability and Limits of Mine Feature Delineation Using Segment Anything Model.** ✓ _Tipo:_ Preprint. _Relevância:_ Geo-SAM (plugin QGIS com SAM): teste de confiabilidade e limites na delineação de feições de mineração.

**[P165] Wang et al. 2025 — MO-SAM: Testing the reliability and limits of mine feature delineation using Segment Anything Model to democratize mine observation and research.** ✓ _Tipo:_ Artigo. _Relevância:_ MO-SAM: confiabilidade do Geo-SAM na delineação de feições de mineração.

**[P166] Jeon et al. 2026 — Systematic evaluation of SAM prompting strategies for agricultural land extraction with GeoSAM.** ✓ _Tipo:_ Artigo. _Relevância:_ Avaliação sistemática de estratégias de prompt do SAM com GeoSAM para extração de áreas agrícolas.

**[P167] Wu e Osco 2023 — samgeo: A Python package for segmenting geospatial data with the Segment Anything Model (SAM).** ✓ _Tipo:_ Software. _Relevância:_ samgeo (segment-geospatial): SAM para dados geoespaciais; integra-se ao ecossistema opengeos/geoai.

**[P168] Wu 2020 — geemap: A Python package for interactive mapping with Google Earth Engine.** ✓ _Tipo:_ Software. _Relevância:_ geemap: mapeamento interativo com Google Earth Engine, do mesmo autor do GeoAI.

**[P169] Congedo 2021 — Semi-Automatic Classification Plugin: A Python tool for the download and processing of remote sensing images in QGIS.** ✓ _Tipo:_ Software. _Relevância:_ Semi-Automatic Classification Plugin (SCP): download e classificação de imagens de satélite no QGIS.

**[P170] Zhou et al. 2026 — Measuring the spatial explicitness of GeoAI and geospatial foundation models: A systematic review and future roadmap.** ✓ _Tipo:_ Revisão. _Relevância:_ Revisão sistemática sobre explicitação espacial em GeoAI e modelos fundacionais geoespaciais; cita o GeoAI.

**[P171] Boutayeb et al. 2024 — A comprehensive GeoAI review: Progress, Challenges and Outlooks.** ✓ _Tipo:_ Revisão. _Relevância:_ Revisão abrangente de GeoAI: progresso, desafios e perspectivas.

**[P172] Mai et al. 2025 — Towards the next generation of Geospatial Artificial Intelligence.** ✓ _Tipo:_ Revisão. _Relevância:_ Rumo à próxima geração de inteligência artificial geoespacial.

**[P173] Mai et al. 2024 — On the Opportunities and Challenges of Foundation Models for GeoAI (Vision Paper).** ✓ _Tipo:_ Artigo. _Relevância:_ Oportunidades e desafios dos modelos fundacionais para GeoAI.

**[P174] Carvalho et al. 2026 — Remote SAMsing: From segment anything to segment everything.** ✓ _Tipo:_ Artigo. _Relevância:_ Remote SAMsing: do segment anything ao segment everything em sensoriamento remoto.

**[P175] Šanca et al. 2023 — AN END-TO-END DEEP LEARNING WORKFLOW FOR BUILDING SEGMENTATION, BOUNDARY REGULARIZATION AND VECTORIZATION OF BUILDING FOOTPRINTS.** ✓ _Tipo:_ Artigo. _Relevância:_ Fluxo de aprendizado profundo para segmentação, regularização de bordas e vetorização de edificações.

**[P176] Kleebauer et al. 2025 — Globally Scalable, QGIS-Integrated Workflow for Solar Photovoltaic System Segmentation and Capacity Estimation: A Case Study in Algeria.** ✓ _Tipo:_ Artigo. _Relevância:_ Fluxo integrado ao QGIS para segmentação de usinas fotovoltaicas em escala global.

**[P177] Gluski et al. 2024 — Remote detection of asbestos-cement roofs: Evaluating a QGIS plugin in a low- and middle-income country.** ✓ _Tipo:_ Artigo. _Relevância:_ Avaliação de plugin QGIS para detecção remota de telhados de amianto.

**[P178] Vardiashvili et al. 2026 — GSIP: A Model-Agnostic Framework for Scalable Geospatial Inference.** ✓ _Tipo:_ Artigo. _Relevância:_ GSIP: framework agnóstico de modelo para inferência geoespacial escalável; cita Deepness.

**[P179] Robinson et al. 2026 — Advancing Earth Observation Through Machine Learning: A TorchGeo Tutorial.** ✓ _Tipo:_ Software. _Relevância:_ Tutorial de TorchGeo para observação da Terra com aprendizado de máquina.

**[P180] Muhammad et al. 2022 — Spatiotemporal Change Analysis and Prediction of Future Land Use and Land Cover Changes Using QGIS MOLUSCE Plugin and Remote Sensing Big Data: A Case Study of Linyi, China.** ✓ _Tipo:_ Artigo. _Relevância:_ Análise e previsão de mudanças de uso/cobertura com o plugin MOLUSCE do QGIS.

**[P181] Amgoth et al. 2023 — Exploring LULC changes in Pakhal Lake area, Telangana, India using QGIS MOLUSCE plugin.** ✓ _Tipo:_ Artigo. _Relevância:_ Mudanças de uso/cobertura em Telangana com o plugin MOLUSCE.

**[P182] Baghel et al. 2024 — Spatiotemporal LULC change detection and future prediction for the Mand catchment using MOLUSCE tool.** ✓ _Tipo:_ Artigo. _Relevância:_ Detecção e previsão de mudança de uso/cobertura na bacia Mand com MOLUSCE.

**[P183] Alshari e Gawali 2022 — Modeling Land Use Change in Sana’a City of Yemen with MOLUSCE.** ✓ _Tipo:_ Artigo. _Relevância:_ Modelagem de mudança de uso do solo em Sana'a (Iêmen) com MOLUSCE.

**[P184] Ramadan e Hidayati 2022 — Prediction and Simulation of Land Use and Land Cover Changes Using Open Source QGIS. A Case Study of Purwokerto, Central Java, Indonesia.** ✓ _Tipo:_ Artigo. _Relevância:_ Previsão e simulação de mudança de uso/cobertura com QGIS de código aberto.

**[P185] Kumari e Roy 2025 — Simulation of Land Use and Land Cover Using the MOLUSCE Plugin Integrated with QGIS for the Western Himalayan Region of India.** ✓ _Tipo:_ Artigo. _Relevância:_ Simulação de uso/cobertura com MOLUSCE integrado ao QGIS.

### Revisões do documento original (P48–P50)

**[P48] Peng et al. 2025 — Deep learning change detection techniques for optical remote sensing imagery: Status, perspectives and challenges.** ✓ _Referência:_ Peng, D. et al., 2025. International Journal of Applied Earth Observation and Geoinformation. _Contribuição:_ panorama de datasets, métodos e desafios de mudança em imagens ópticas. _Uso:_ buscar referências adicionais por família de arquitetura e tipo de mudança. _Limite:_ revisão oferece mapa da área; consultar os estudos originais antes de reutilizar resultados quantitativos.

**[P49] Lei et al. 2026 — Remote sensing image change detection using deep learning techniques: a comprehensive survey.** ✓ _Referência:_ Lei, T. et al., 2026. Artificial Intelligence Review. _Contribuição:_ revisão de aprendizado supervisionado, semissupervisionado e não supervisionado, com diferentes modalidades de sensoriamento. _Uso:_ atualizar o panorama e identificar estratégias para poucos rótulos. _Limite:_ técnicas SAR/hiperespectrais não são diretamente compatíveis com RGB ou quatro bandas Planet.

**[P50] Jabbarizadegan e Fraternali 2026 — Change Detection in Remote Sensing Imagery: A Systematic Review of Statistical, Machine Learning, and Deep Learning Methods.** ✓ _Referência:_ Jabbarizadegan, M. et al., 2026. Remote Sensing, 18(15), 2573. _Contribuição:_ revisão que declara analisar 144 estudos primários, abrangendo métodos estatísticos, ML e DL. _Uso:_ principal trilha para expandir este catálogo por rastreamento de referências. _Limite:_ os 144 trabalhos da revisão **não foram todos individualmente verificados nem incorporados** aqui. O total deste documento ampliado é de 80 registros; não se deve somar os trabalhos citados por uma revisão como se fossem novas referências verificadas.

## Bibliotecas e ferramentas verificadas

Repositórios consultados na API do GitHub e pacotes no PyPI em 24/10/2026. Um repositório existente não garante que o ambiente rode sem adaptação, e as licenças devem ser conferidas antes do uso.

| Ferramenta | Repositório | Estrelas | Licença | Último push | Status |
|------------|-------------|---------:|---------|-------------|--------|
| TorchGeo | [torchgeo/torchgeo](https://github.com/torchgeo/torchgeo) | 4211 | MIT | 2026-10-23 | ativo |
| Open-CD | [likyoo/open-cd](https://github.com/likyoo/open-cd) | 896 | Apache-2.0 | 2026-06-15 | ativo |
| PyTorch Change Models / AnyChange | [Z-Zheng/pytorch-change-models](https://github.com/Z-Zheng/pytorch-change-models) | 269 | Apache-2.0 | 2026-08-03 | ativo |
| SpaceNet 7 solutions | [SpaceNetChallenge/SpaceNet7_Multi-Temporal_Solutions](https://github.com/SpaceNetChallenge/SpaceNet7_Multi-Temporal_Solutions) | 66 | Apache-2.0 | 2021-01-29 | estável/sem atividade recente |
| TSSCD | [CUG-BEODL/TSSCD](https://github.com/CUG-BEODL/TSSCD) | 52 | MIT | 2024-12-17 | estável/sem atividade recente |
| U-TAE / PaPs | [VSainteuf/utae-paps](https://github.com/VSainteuf/utae-paps) | 226 | MIT | 2024-08-20 | estável/sem atividade recente |
| ChangeFormer | [wgcban/ChangeFormer](https://github.com/wgcban/ChangeFormer) | 627 | MIT | 2024-01-31 | estável/sem atividade recente |
| ChangeMamba (MambaCD) | [ChenHongruixuan/MambaCD](https://github.com/ChenHongruixuan/MambaCD) | 656 | Apache-2.0 | 2026-04-24 | ativo |
| MapFormer | [mxbh/mapformer](https://github.com/mxbh/mapformer) | 43 | — | 2023-10-05 | estável/sem atividade recente |
| CCDC | [GERSL/CCDC](https://github.com/GERSL/CCDC) | 108 | MIT | 2024-10-30 | estável/sem atividade recente |
| FC-Siam (Daudt) | [rcdaudt/fully_convolutional_change_detection](https://github.com/rcdaudt/fully_convolutional_change_detection) | 234 | — | 2020-06-23 | estável/sem atividade recente |
| STANet | [justchenhao/STANet](https://github.com/justchenhao/STANet) | 477 | BSD-2-Clause | 2023-03-11 | estável/sem atividade recente |
| PerASCD | [SathShen/PerASCD](https://github.com/SathShen/PerASCD) | 7 | MIT | 2026-06-01 | ativo |
| Seg2Change | [yogurts-sy/Seg2Change](https://github.com/yogurts-sy/Seg2Change) | 38 | — | 2026-09-09 | ativo |
| SAMPolyBuild | [wchh-2000/SAMPolyBuild](https://github.com/wchh-2000/SAMPolyBuild) | 84 | Apache-2.0 | 2025-07-20 | estável/sem atividade recente |
| DINO Soars | [rfaulk/DINO_Soars](https://github.com/rfaulk/DINO_Soars) | 28 | — | 2026-08-06 | ativo |
| GeoAI (geoai-py + plugin QGIS) | opengeos/geoai | — | — | — | **não encontrado (403)** |
| segment-geospatial (samgeo) | opengeos/segment-geospatial | — | — | — | **não encontrado (403)** |
| geemap | gee-community/geemap | — | — | — | **não encontrado (403)** |
| Deepness (plugin QGIS) | PUTvision/qgis-plugin-deepness | — | — | — | **não encontrado (403)** |
| IAMAP (plugin QGIS) | [umr-amap/iamap](https://github.com/umr-amap/iamap) | 4 | — | — | ativo |
| Geo-SAM (plugin QGIS) | coolzhao/Geo-SAM | — | — | — | **não encontrado (403)** |
| Semi-Automatic Classification Plugin | semiautomaticgit/SemiAutomaticClassificationPlugin | — | — | — | **não encontrado (403)** |
| MOLUSCE (plugin QGIS) | [nextgis/qgis_molusce](https://github.com/nextgis/qgis_molusce) | 59 | — | — | ativo |
| sits (R) | e-sensing/sits | — | — | — | **não encontrado (403)** |
| gdalcubes | appelmar/gdalcubes | — | — | — | **não encontrado (403)** |
| openEO Python client | Open-EO/openeo-python-client | — | — | — | **não encontrado (403)** |
| XGBoost | dmlc/xgboost | — | — | — | **não encontrado (403)** |
| LightGBM | microsoft/LightGBM | — | — | — | **não encontrado (403)** |
| Ultralytics (YOLO) | ultralytics/ultralytics | — | — | — | **não encontrado (403)** |
| Segment Anything (SAM) | facebookresearch/segment-anything | — | — | — | **não encontrado (403)** |
| SAM 3 | facebookresearch/sam3 | — | — | — | **não encontrado (403)** |
| Grounded-SAM | IDEA-Research/Grounded-Segment-Anything | — | — | — | **não encontrado (403)** |
| DINOv3 | facebookresearch/dinov3 | — | — | — | **não encontrado (403)** |
| Prithvi-EO-2.0 | NASA-IMPACT/Prithvi-EO-2.0 | — | — | — | **não encontrado (403)** |
| Scale-MAE | bair-climate-initiative/scale-mae | — | — | — | **não encontrado (403)** |
| DOFA | zhu-xlab/DOFA | — | — | — | **não encontrado (403)** |
| STAC spec | radiantearth/stac-spec | — | — | — | **não encontrado (403)** |
| RoadTracer | mitroadmaps/roadtracer | — | — | — | **não encontrado (403)** |

**Pacotes PyPI:**

| Pacote | Versão | Python | Licença |
|--------|--------|--------|---------|
| `torchgeo` | 0.10.1 | >=3.12 | — |
| `geoai-py` | 0.43.1 | >=3.12 | MIT License |
| `segment-geospatial` | 1.4.2 | >=3.10 | MIT license |
| `geemap` | 0.38.9 | >=3.12 | MIT |
| `xgboost` | 3.4.1 | >=3.12 | — |
| `lightgbm` | 4.7.0 | >=3.10 | — |
| `ultralytics` | 8.4.184 | >=3.8 | AGPL-3.0 |
| `openeo` | 0.53.0 | >=3.9 | Apache-2.0 |
| `pystac` | 1.15.2 | >=3.10 | Apache-2.0 |
| `rasterio` | 1.5.2 | >=3.12 | — |
| `optuna` | 5.0.0 | >=3.9 | — |
| `shap` | 0.54.1 | >=3.12 | MIT License |
| `open-cd` | **não publicado no PyPI** | — | — |
| `leafmap` | 0.63.1 | >=3.9 | MIT license |

Notas: BFAST (R, https://bfast.r-forge.r-project.org/) respondeu 503 na checagem automática. O Open-CD não está no PyPI e deve ser instalado do GitHub. O Ultralytics usa AGPL-3.0, o que importa para uso comercial.

## Verificação dos links

Todos os 117 URLs do documento original foram testados em 24/10/2026: **92** responderam normalmente (incluindo redirecionamentos para IEEE e PubMed), **24** devolveram 403 (bloqueio de robôs por editoras como MDPI, ScienceDirect, Taylor & Francis e Wiley; os DOIs correspondentes foram confirmados no OpenAlex) e **1** indisponível (503 transitório no site do BFAST). Nenhum retornou 404. Detalhes em [`dados/links_original.json`](dados/links_original.json).

Registros não conferidos automaticamente: **0**.

## Tendências 2024–2026

Observadas nesta coleta; são leituras do conjunto de títulos e resumos, não resultados medidos:

1. **Modelos fundacionais (SAM, DINOv3, Prithvi) adaptados à detecção de mudanças**, com muitos trabalhos novos em 2025–2026 (seções C, G e M). Há também avisos de que modelos especializados podem não superar baselines supervisionados (P153).
2. **Mudança semântica em séries temporais**, e não só em pares de datas: TSSCD, DynamicEarthNet, MUDS e redes espaço-temporais (P10–P16, P143).
3. **Supervisão fraca e poucos rótulos**: supervisão temporal fraca, pseudorrótulos, aprendizado ativo e pré-anotação com SAM/YOLO (P33, P59, P78, P128).
4. **Planet NICFI como base operacional para floresta**: cobertura arbórea, degradação, perturbações mensais e validação de alertas (P01–P04, P91).
5. **IA geoespacial dentro do QGIS**: plugins de inferência (Deepness, IAMAP, Geo-SAM, GeoAI) reduzem a barreira de uso, mas ainda não há validação publicada com mosaicos Planet mensais (seção N).
6. **Engenharia de dados antes do modelo**: cubos, STAC e controle de qualidade são pré-requisitos para não aprender diferenças de produto como mudança no terreno (seção H).

## Guia metodológico do projeto

Seções do documento original, mantidas sem alteração de conteúdo: verificações dos mosaicos, taxonomia, experimento, passos para uma revisão sistemática, limitações e arquitetura. Os IDs P01–P80 referem-se às tabelas acima.

### 3. O que conferir nos mosaicos antes de escolher o método

Os arquivos não foram inspecionados nesta revisão. Portanto, as seguintes verificações são requisitos, não diagnósticos sobre seus dados.

1. **Produto e bandas:** distinguir mosaico visual RGB de produto analítico de reflectância. NDVI exige vermelho e infravermelho próximo; não deve ser calculado a partir de um RGB renderizado. Bandas adicionais de SuperDove não podem ser presumidas em toda a série.
2. **Cadência real:** se forem NICFI, o arquivo histórico anterior a setembro de 2020 contém mosaicos semestrais. Um arquivo nomeado por mês não prova uma observação mensal independente. Verificar `cadence`, início/fim do período e cenas contribuintes quando disponíveis. Isso não invalida a possibilidade de seus arquivos serem de outro produto Planet.
3. **Data de composição:** um mosaico mensal pode reunir observações de dias distintos. Registrar um intervalo de ocorrência, não um dia exato inferido do nome do arquivo.
4. **2026 parcial:** considerar apenas meses efetivamente disponíveis; não tratar janeiro–dezembro de 2026 como série já completa.
5. **Resolução e grade:** 3 m e 5 m não são intercambiáveis. Reamostrar 5 m para 3 m não cria detalhe. Preservar os originais e testar uma grade comum, além de resultados separados por produto/resolução.
6. **Registro geométrico:** medir deslocamentos em alvos estáveis. Bordas de telhados, vias e vegetação podem gerar mudanças falsas quando imagens estão desalinhadas.
7. **Qualidade:** identificar nuvens, sombras, névoa, áreas sem dado, diferenças de iluminação, emendas do mosaico e mudanças de processamento. Mascarar e manter uma classe de observação inválida.
8. **Limite de identificação:** em 5 m, uma via de 5 m de largura ocupa aproximadamente um pixel; um telhado de 10 × 10 m ocupa nominalmente quatro pixels. Isso não garante sua detecção ou seu contorno. Definir área e largura mínimas por validação local.

Documentação: [especificação Planet NICFI](https://assets.planet.com/docs/NICFI_Basemap_Spec_Addendum.pdf), [metadados NICFI no catálogo Earth Engine](https://developers.google.com/earth-engine/datasets/catalog/projects_planet-nicfi_assets_basemaps_americas), [coleção visual e início da cadência mensal](https://planetarycomputer.microsoft.com/dataset/planet-nicfi-visual).

### 11. Taxonomia inicial proposta para as alterações

As classes abaixo são uma proposta a validar por interpretação de amostras locais. **Cobertura física, uso do solo e processo de transformação são conceitos diferentes.** Uma imagem pode mostrar solo exposto sem determinar se é terraplenagem, mineração ou outra atividade.

| Transição observável | Evento candidato | O que precisa ser confirmado |
|---|---|---|
| Vegetação arbórea → solo exposto | Supressão de cobertura arbórea | Persistência, exclusão de sombra/nuvem e sazonalidade |
| Vegetação arbórea → vegetação baixa | Perda parcial ou mudança de estrutura | Separar degradação, manejo e erro de classificação |
| Vegetação baixa → solo exposto | Remoção de cobertura rasteira | Separar cultivo, seca e preparo do terreno |
| Solo exposto → cobertura edificada | Nova construção | Tamanho detectável e estabilidade em observações seguintes |
| Vegetação → cobertura edificada | Conversão direta aparente | Pode haver etapa de solo exposto não observada |
| Solo/vegetação → estrutura linear viária | Nova via ou acesso | Continuidade, largura e conexão com a rede |
| Via não pavimentada → superfície pavimentada | Pavimentação candidata | Pode ser espectralmente ambígua em 3–5 m |
| Edificação → solo exposto | Remoção/demolição candidata | Excluir sombra, cobertura por nuvem e desalinhamento |
| Solo exposto → vegetação persistente | Revegetação/regeneração candidata | Distinguir crescimento sazonal e recuperação duradoura |
| Água → solo/vegetação, ou inverso | Mudança hídrica/inundação/retração | Sazonalidade, maré e contexto hidrológico |
| Qualquer classe → observação inválida | Sem conclusão | Não registrar como alteração territorial |

**Saída mínima por evento:** identificador, geometria, classe anterior, classe posterior, intervalo temporal, área, resolução/produto, número de observações válidas, confiança avaliada, referências às imagens e estado de revisão humana.

Supressão, construção e abertura de via podem ser etapas do mesmo processo. Guardar eventos encadeados e evitar contabilizar repetidamente a mesma área como nova conversão independente. Legalidade, finalidade e responsabilidade não são classes diretamente observáveis no mosaico.

### 12. Experimento recomendado a partir da literatura

#### 12.1 Perguntas que o piloto deve responder

1. O histórico mensal melhora a detecção em relação a pares de datas?
2. Qual a menor área de supressão, edificação e largura de via detectável com precisão aceitável?
3. Qual é a diferença de desempenho entre produtos de 3 m e de 5 m?
4. Quanto os erros aumentam ao mudar de ano, sensor/produto e setor geográfico?
5. Qual benefício se obtém de NIR, quando disponível, frente ao RGB?
6. Qual o custo de revisão humana por evento verdadeiro confirmado?

#### 12.2 Comparações mínimas

| Experimento | Base bibliográfica | Hipótese testada |
|---|---|---|
| Random Forest com atributos espectrais/texturais + comparação temporal | P07, P42 | Baseline de ML pode ser competitivo com poucos rótulos |
| U-Net mensal + regra de persistência | P01–P03, P05 | Segmentação consistente pode ser suficiente para parte dos eventos |
| FC-Siam ou ChangeFormer em pares | P23, P26 | Aprender a mudança diretamente reduz erros da pós-classificação |
| Modelo semântico conjunto | P18–P22 | Coerência entre classes e mudança melhora as transições |
| Modelo de série, inspirado em TSSCD/P13 | P13–P15 | Histórico reduz sazonalidade e melhora localização temporal |
| AnyChange como candidato/assistente | P29 | Pré-anotação pode reduzir esforço, mantendo revisão independente |

Começar pelos três primeiros e pelo teste temporal prioritário, conforme volume de rótulos e recursos. Não é necessário implementar todas as arquiteturas do catálogo. Preservar os mesmos conjuntos de teste e critérios para comparar os modelos.

#### 12.3 Rótulos e separação dos dados

- Rotular **áreas estáveis e mudanças reais**, com exemplos difíceis: sombras, variação hídrica, mosaicos desalinhados, solo arenoso, telhados claros e vegetação sazonal.
- Separar treino/validação/teste por blocos geográficos; evitar patches vizinhos ou sobrepostos entre os conjuntos.
- Reservar períodos posteriores para teste temporal, além do teste espacial. Documentar se o teste envolve simultaneamente outro produto ou resolução.
- Rotular a transição com imagem anterior e posterior válidas; incluir intervalo de incerteza quando houver nuvens ou composição temporal ampla.
- Distinguir avaliação retrospectiva, que pode usar meses futuros, de alerta operacional, que só pode usar o passado disponível. Comparar os dois regimes separadamente.
- Se usar pseudorrótulos de outro mapa/modelo, construir amostra final independente com interpretação especializada e, quando possível, imagens de maior resolução ou campo.

#### 12.4 Métricas mínimas

| Dimensão | Avaliação recomendada |
|---|---|
| Mudança/não mudança | Precisão, recall, F1, IoU e curva precisão–recall |
| Tipo de transição | Matriz de confusão from–to, F1 por transição e macro-F1 |
| Cobertura em cada mês | IoU/F1 por classe, separadas das métricas de mudança |
| Edificações | Precisão/recall por objeto e faixa de tamanho; associação temporal de identidades |
| Vias | Sobreposição, continuidade/conectividade e erros de rede; não apenas área de pixels |
| Data | Erro ou compatibilidade com intervalo de ocorrência; atraso do alerta operacional |
| Área alterada | Área mapeada e estimativa amostral com intervalo de confiança, sem confundi-las |
| Transferência | Resultados por ano, região, resolução, produto e qualidade da observação |
| Uso operacional | Falsos alertas por km²/mês, tempo de revisão e tempo de processamento |

Não comparar F1 publicado de LEVIR-CD, SECOND, SpaceNet 7 e desmatamento como se fossem medidos na mesma tarefa. Classes, resoluções, prevalência de mudança, referência e divisão dos dados são diferentes. Acurácia global alta pode esconder baixa detecção de eventos raros.

### 13. Como continuar até uma revisão sistemática publicável

1. Fixar a pergunta de pesquisa, as classes de mudança e critérios de inclusão antes de expandir a busca.
2. Executar buscas estruturadas em bases bibliográficas, exportando resultados e datas de execução.
3. Deduplicar por DOI, título e relação preprint–publicação; manter versões vinculadas.
4. Fazer triagem de título/resumo e depois texto integral, registrando motivo de exclusão.
5. Extrair: sensor/produto, bandas, resolução, frequência, área, período, classes, rótulos, arquitetura, entradas temporais, divisão espacial/temporal, métricas, código, licença e limitações.
6. Rastrear as referências de P48–P50 e as citações posteriores de P01, P10, P12–P14.
7. Classificar risco de vazamento espacial/temporal e independência da validação.
8. Não agregar métricas incompatíveis; organizar síntese por tarefa e condição de aquisição.
9. Fazer atualização final antes da escrita do trabalho, especialmente para preprints de 2026.

**Campos sugeridos para a planilha de extração:**

```text
id;titulo;autores;ano;veiculo;doi_url;status_publicacao;
nivel_leitura;produto_sensor;bandas;resolucao_m;cadencia;
periodo;regiao;tipo_tarefa;classes;numero_datas_entrada;
rotulos_origem;split_espacial;split_temporal;metodo;
metricas;codigo_url;pesos_disponiveis;licenca;
limitacoes;aplicabilidade_planet;prioridade;decisao_inclusao
```

### 14. Limitações deste levantamento

- O catálogo é dirigido ao seu objetivo; não representa um censo de toda a produção científica.
- A qualidade metodológica de cada estudo ainda precisa de avaliação integral. Inclusão não significa endosso de todos os procedimentos ou resultados.
- Nos registros acessados apenas por resumo/indexação, detalhes não confirmados foram omitidos ou marcados para conferência.
- Preprints não foram tratados automaticamente como artigos revisados por pares. Quando a versão consultada é preprint, isso foi indicado.
- Código localizado não foi instalado/testado; disponibilidade de pesos e licença deve ser confirmada na execução.
- Não houve inspeção dos seus rasters: produto, bandas, qualidade, abrangência espacial e número real de meses permanecem a verificar.
- A recomendação central é testar **classificação semântica temporal com validação local**, mantendo trilhas específicas para vegetação, edificações e vias. Não há evidência suficiente nesta revisão para prometer que um único modelo classifique todas as alterações em 3–5 m.

### 19. Arquitetura revisada: acervo → catálogo preliminar → eventos de mudança

#### 19.1 O papel de cada tecnologia

| Camada | Responsabilidade | Candidatos e referências | Produto verificável |
|---|---|---|---|
| Inventário | Identificar exatamente cada arquivo e período | STAC; P68–P74 | Catálogo de assets e manifestos |
| Qualidade e harmonização | Grade, bandas, observações válidas e registro | P68–P71, P77 | Cubo/coleção pronta para análise e relatório de QA |
| Pré-segmentação | Delimitar regiões/objetos candidatos | SAM, SAMPolyBuild, YOLOSAM; P56–P63, P80 | Máscaras e polígonos provisórios |
| Representação | Extrair espectro, textura, geometria e embeddings | XGBoost/OBIA, DINOv3, DOFA, Scale-MAE | Tabela de atributos versionada |
| Pré-classificação | Atribuir categorias e abstinência | XGBoost, LightGBM, modelos abertos | Classe proposta e confiança avaliada |
| Curadoria | Corrigir rótulos e selecionar exemplos úteis | P75–P78 | Conjunto anotado com origem e revisão |
| Análise temporal | Associar observações e detectar transições | P10–P14, P18–P29 | Histórico de objetos e eventos |
| Avaliação | Medir cobertura, omissões, geometria, tempo e custo | P46–P47, P75 | Métricas independentes e limitações |

**Esta integração é uma proposta de engenharia baseada nas referências, não um pipeline integral já validado por um único artigo.**

#### 19.2 Dois catálogos diferentes

**Catálogo técnico de imagens:** registra arquivos, footprints, CRS, tamanho de pixel, bandas, datas de composição, produto, máscaras, checksum e relação entre originais e derivados. STAC é apropriado para organizar a descoberta desses assets; não reconhece construções nem vegetação.

**Catálogo semântico de observações:** registra máscara/polígono, mês/intervalo, classe sugerida, atributos, modelo, prompt, confiança e revisão. Um registro observado em um mês não deve receber automaticamente a mesma identidade de um registro no mês seguinte.

Documentação oficial de STAC: https://www.ogc.org/standards/stac/ e https://stacspec.org/. São especificações técnicas, não artigos adicionais ao total de 80.

#### 19.3 Estrutura de dados proposta

| Entidade | Campos essenciais |
|---|---|
| `image_asset` | `asset_id`, produto, intervalo de composição, CRS, resolução, bandas, URI, checksum |
| `processing_run` | `run_id`, versão do código, configuração, ambiente, entradas, saídas, logs |
| `object_observation` | `observation_id`, `asset_id`, geometria, classe proposta, modelo/prompt, qualidade, revisão |
| `feature_record` | `observation_id`, versão do extrator, bandas/índices/textura/forma, embedding e procedência |
| `annotation` | geometria/classe revisada, origem humana ou automática, revisor, status, versão |
| `entity_link` | observações associadas, hipótese de identidade, confiança, relações de divisão/fusão |
| `change_event` | cobertura anterior/posterior, intervalo do evento, geometria, evidências, status |
| `evaluation_split` | versão da amostra, blocos geográficos, período, treino/validação/teste |

Não confundir o identificador gerado por SAM/YOLO em uma imagem com uma identidade persistente no mundo real. Árvores podem ocultar telhados; máscaras podem dividir ou unir objetos; ruas formam redes. A associação temporal precisa modelar esses casos.

#### 19.4 Engenharia de atributos para XGBoost/LightGBM

- Bandas e índices compatíveis com o produto; NIR apenas quando realmente disponível.
- Estatísticas por segmento: média, dispersão, quantis e proporção de pixels inválidos.
- Texturas em janelas definidas em metros; manter escala física comparável.
- Geometria: área, perímetro, alongamento e compactação, reconhecendo que dependem da qualidade da segmentação.
- Contexto: vizinhança e distâncias a elementos cartográficos disponíveis à época analisada.
- Tempo: diferença para a observação anterior válida, variação sazonal, persistência e tendência.
- Embeddings: representações de patches/objetos, registrando modelo, checkpoint, resolução e normalização.

Testar grupos de atributos por ablação. Ajustar seletores, normalizadores e hiperparâmetros apenas no treino; não selecionar features olhando o teste. Se mapas atuais forem usados para explicar eventos antigos, marcar o experimento como retrospectivo e controlar vazamento de informação futura.

#### 19.5 Como testar se a pré-catalogação realmente economiza trabalho

Comparar três condições na mesma amostra independente: anotação manual; pré-anotação SAM/YOLO com correção; pré-anotação sem correção, usada apenas como baseline de erro.

Medir tempo total, incluindo falsos positivos removidos e objetos omitidos acrescentados; qualidade das máscaras; acurácia das classes; cobertura de alvos pequenos; e desempenho do modelo final treinado com esses rótulos. Uma máscara visualmente convincente pode estar sistematicamente errada.

Para reduzir viés de confirmação, parte da avaliação deve começar diretamente da imagem sem mostrar a sugestão do modelo. Manter uma amostra probabilística independente para avaliação, separada do conjunto escolhido por active learning.

#### 19.6 Ordem prática de implementação revisada

1. Inventariar os produtos e medir qualidade/registro; preservar os arquivos originais.
2. Criar amostra espacial e temporal representativa, com mudanças e áreas estáveis.
3. Treinar baseline XGBoost/LightGBM e baseline U-Net para cobertura.
4. Comparar pré-anotação por SAM, YOLO→SAM e um modelo semântico recente em um subconjunto; medir correção humana e omissões.
5. Aproveitar embeddings para busca de similares e seleção de amostras se houver ganho comprovado.
6. Construir catálogo semântico revisável e associação temporal, com incerteza e proveniência.
7. Comparar pós-classificação e modelos temporais em teste independente.
8. Automatizar atualização incremental só depois de estabilizar entradas, rótulos e critérios de avaliação.

**Ponto de decisão:** se o gargalo for falta de rótulos, priorizar pré-anotação e curadoria. Se for falso alerta, priorizar qualidade e consistência temporal. Se for volume de dados, priorizar acesso por blocos, processamento incremental e medição de I/O. Escolher o modelo apenas pela novidade não resolve esses três problemas.

#### 19.7 Complemento do registro de busca

```text
PlanetScope XGBoost land cover classification change detection paper
Very High Resolution Object-Based Land Use-Land Cover Urban Classification Using Extreme Gradient Boosting
remote sensing SAM YOLO automatic annotation building dataset satellite paper
YOLOSAM building segmentation
SAM CLIP unsupervised building extraction
SAMPolyBuild
SAM 3 Concept segmentation arxiv
DINOv3 satellite imagery arxiv
satellite image time series data cube STAC cloud native geospatial machine learning paper
Earth Observation Data Cubes for Brazil
Satellite Image Time Series Analysis for Big Earth Observation Data
gdalcubes on demand processing data cubes
Cross-validation strategies for data with temporal spatial hierarchical structure
Comparing Active Learning for Satellite Imagery
```

Foram verificados registros de fontes primárias e textos/trechos disponíveis. As extensões continuam sendo uma revisão dirigida, não leitura integral nem reprodução dos 80 estudos. Datas de publicação online e de volume são distinguidas quando identificadas; metadados completos devem ser importados antes de normalização bibliográfica final.

## Estrutura do repositório

```text
README.md                 este arquivo
coleta/                   PDFs de acesso aberto + _manifesto.csv
dados/catalog.json        metadados verificados de cada registro
dados/tools.json          repositórios GitHub e pacotes PyPI verificados
dados/links_original.json resultado da checagem dos URLs do documento original
dados/analysis.json       entidades, hiperparametros e frases de resultado extraidos dos PDFs
dados/chunks/             chunks por secao em JSONL (para RAG; fora do git)
vault/                    vault Obsidian: artigos, conceitos, pipeline, experimentos, reuso (abra esta pasta no Obsidian)
fonte_original/           documento de revisão que originou a coleta (inalterado)
scripts/                  scripts de coleta, verificação e geração do README
```

## Referências de formato

Estrutura inspirada no repositório [ML-for-Location-and-Routing-Optimization-Papers](https://github.com/EstevezCodando/ML-for-Location-and-Routing-Optimization-Papers).
