---
tipo: hub
tags: [hub]
---
# 00 Início — Mudanças de cobertura com séries Planet

Vault construído a partir de **185 artigos** (97 com texto integral analisado em `coleta/`). **Autor da coleta:** Jean Michael Estevez Alvarez.

## Perguntas do piloto

1. O histórico mensal melhora a detecção em relação a pares de datas? → [[EXP5 Modelo de série temporal]]
2. Qual a menor área/largura detectável? → [[E10 Avaliação e incerteza]]
3. Diferença entre 3 m e 5 m? → [[EXP0 Piloto de verificação dos dados]]
4. Quanto os erros aumentam ao mudar de ano, produto e setor? → [[E03 Cubo espaço-temporal e partições]]
5. Benefício do NIR frente ao RGB? → [[E02 Qualidade e harmonização]]
6. Custo de revisão humana por evento? → [[EXP6 Pré-anotação assistida (SAM-YOLO-QGIS)]]

## Pipeline (do dado ao resultado)

1. [[E01 Inventário e catálogo]] — Identificar cada arquivo, período, produto, bandas, CRS e checksum; separar catálogo técnico de imag
2. [[E02 Qualidade e harmonização]] — Medir registro geométrico, nuvem/sombra/emendas, radiometria e cadência real; decidir grade comum se
3. [[E03 Cubo espaço-temporal e partições]] — Montar o cubo (tempo × bandas × espaço), definir blocos geográficos e períodos de teste sem vazament
4. [[E04 Rotulagem e pré-anotação]] — Criar rótulos de áreas estáveis e mudanças reais; pré-anotar com SAM/YOLO e revisar; priorizar por a
5. [[E05 Atributos e representações]] — Extrair bandas/índices, textura, geometria, contexto e embeddings; testar por ablação.
6. [[E06 Modelos-base de cobertura]] — Baselines: Random Forest/XGBoost/LightGBM sobre atributos e U-Net mensal; regra de persistência temp
7. [[E07 Modelos de mudança em pares]] — Aprender a mudança diretamente (FC-Siam, ChangeFormer, ChangeMamba) e mudança semântica (HRSCD, SECO
8. [[E08 Modelos de série temporal]] — Usar o histórico completo (TSSCD, U-TAE, BFAST/CCDC) para localizar quando e o que mudou.
9. [[E09 Pós-processamento e eventos]] — Persistência, ligação de identidades no tempo, taxonomia from–to, vetorização e eventos encadeados (
10. [[E10 Avaliação e incerteza]] — Métricas por tarefa, matriz from–to, estimativa de área com IC, validação espacial/temporal e custo 
11. [[E11 Operação e atualização]] — Atualização incremental, alertas com regime operacional (só passado), revisão humana em QGIS, rastre

Mapa visual: [[Pipeline.canvas]]

## Experimentos

- [[EXP0 Piloto de verificação dos dados]]
- [[EXP1 Baseline de atributos (RF-XGBoost-LightGBM)]]
- [[EXP2 U-Net mensal + persistência]]
- [[EXP3 Pares siameses (FC-Siam - ChangeFormer)]]
- [[EXP4 Modelo semântico conjunto]]
- [[EXP5 Modelo de série temporal]]
- [[EXP6 Pré-anotação assistida (SAM-YOLO-QGIS)]]
- [[Quadro de resultados]]

## Reuso

- [[Receitas de treino]] · [[Datasets e benchmarks]] · [[Código e repositórios]] · [[Taxonomia from-to]] · [[Métricas e protocolos]]

## Navegação

- [[01 Guia de uso]] · [[02 Estratégia de chunks]] · [[03 Mapa do grafo]]

## Ordem de leitura (prioridade alta)

- [[P01 Wagner 2023|P01 Wagner 2023]] — Mapping Tropical Forest Cover and Deforestation with Planet NICFI Satellite Images and Dee · leitura: [[LP P01 Wagner 2023|profunda]]
- [[P02 Dalagnol 2023|P02 Dalagnol 2023]] — Mapping tropical forest degradation with deep learning and Planet NICFI data · leitura: [[LP P02 Dalagnol 2023|parcial]]
- [[P05 Zaraza-Aguilera 2022|P05 Zaraza-Aguilera 2022]] — Change Detection over mining areas using Deep Neural Networks from Planetscope image time  · leitura: [[LP P05 Zaraza-Aguilera 2022|profunda]]
- [[P07 Vizzari 2022|P07 Vizzari 2022]] — PlanetScope, Sentinel-2, and Sentinel-1 Data Integration for Object-Based Land Cover Class · leitura: [[LP P07 Vizzari 2022|profunda]]
- [[P10 Etten 2021|P10 Etten 2021]] — The Multi-Temporal Urban Development SpaceNet Dataset · leitura: [[LP P10 Etten 2021|profunda]]
- [[P12 Toker 2022|P12 Toker 2022]] — DynamicEarthNet: Daily Multi-Spectral Satellite Dataset for Semantic Change Segmentation · leitura: [[LP P12 Toker 2022|profunda]]
- [[P13 Vincent 2024|P13 Vincent 2024]] — Satellite Image Time Series Semantic Change Detection: Novel Architecture and Analysis of  · leitura: [[LP P13 Vincent 2024|profunda]]
- [[P14 He 2024|P14 He 2024]] — Time-series land cover change detection using deep learning-based temporal semantic segmen · leitura: [[LP P14 He 2024|parcial]]
- [[P18 Daudt 2019|P18 Daudt 2019]] — Multitask Learning for Large-scale Semantic Change Detection · leitura: [[LP P18 Daudt 2019|profunda]]
- [[P19 Yang 2021|P19 Yang 2021]] — Asymmetric Siamese Networks for Semantic Change Detection in Aerial Images · leitura: [[LP P19 Yang 2021|profunda]]
- [[P46 Olofsson 2014|P46 Olofsson 2014]] — Good practices for estimating area and assessing accuracy of land change · leitura: [[LP P46 Olofsson 2014|parcial]]
- [[P155 Wu 2026|P155 Wu 2026]] — GeoAI: A Python package for integrating artificial intelligence with geospatial data analy · *leitura pendente*
- [[P156 Aszkowski 2023|P156 Aszkowski 2023]] — Deepness: Deep neural remote sensing plugin for QGIS · *leitura pendente*
- [[P157 Tresson 2026|P157 Tresson 2026]] — IAMAP: Unlocking Deep Learning in QGIS for non-coders and limited computing resources · *leitura pendente*
- [[P164 Wang 2024|P164 Wang 2024]] — Geo-Sam: Testing the Reliability and Limits of Mine Feature Delineation Using Segment Anyt · *leitura pendente*

## Sínteses da leitura profunda

- [[Síntese — decisões e hipóteses derivadas da leitura profunda]]
- [[Síntese — métricas por tarefa e armadilhas]]
- [[Síntese — partições, vazamento e domain shift]]
- [[Síntese — cuidados específicos com produtos Planet]]
- [[Síntese — receitas de treino comparadas (verificadas na leitura)]]
- [[Síntese — protocolos de rotulagem comparados]]

## Artigos por seção

- **Planet: aplicações diretas** (9): [[P01 Wagner 2023|P01]] [[P02 Dalagnol 2023|P02]] [[P03 Carter 2024|P03]] [[P04 Wang 2024|P04]] [[P05 Zaraza-Aguilera 2022|P05]] [[P06 Şimşek 2025|P06]] [[P07 Vizzari 2022|P07]] [[P08 Debus 2025|P08]] [[P09 Gonzalez-Velez 2026|P09]]
- **Séries temporais, edificações e transições semânticas** (13): [[P10 Etten 2021|P10]] [[P11 Etten 2021|P11]] [[P12 Toker 2022|P12]] [[P13 Vincent 2024|P13]] [[P14 He 2024|P14]] [[P15 Garnot 2021|P15]] [[P16 Zhao 2025|P16]] [[P17 Metzger 2023|P17]] [[P18 Daudt 2019|P18]] [[P19 Yang 2021|P19]] [[P20 Zheng 2022|P20]] [[P21 Ding 2022|P21]] [[P22 Tang 2024|P22]]
- **Detectores profundos e modelos fundacionais** (13): [[P23 Daudt 2018|P23]] [[P24 Chen 2020|P24]] [[P25 Chen 2021|P25]] [[P26 Bandara 2022|P26]] [[P27 Zheng 2021|P27]] [[P28 Chen 2024|P28]] [[P29 Zheng 2024|P29]] [[P30 Yongshuo 2025|P30]] [[P31 Huang 2025|P31]] [[P32 Szwarcman 2024|P32]] [[P33 Bou 2026|P33]] [[P34 Shen 2026|P34]] [[P35 Su 2026|P35]]
- **Vias, redes viárias e cartografia prévia** (5): [[P36 Shu 2025|P36]] [[P37 Bastani 2018|P37]] [[P38 Buslaev 2018|P38]] [[P39 Bernhard 2023|P39]] [[P40 Lee 2026|P40]]
- **Métodos temporais clássicos e avaliação** (7): [[P41 Verbesselt 2010|P41]] [[P42 Zhu 2014|P42]] [[P43 Kennedy 2010|P43]] [[P44 Pasquarella 2022|P44]] [[P45 Brown 2022|P45]] [[P46 Olofsson 2014|P46]] [[P47 Stehman 2019|P47]]
- **Revisões do documento original** (3): [[P48 Peng 2025|P48]] [[P49 Lei 2026|P49]] [[P50 Jabbarizadegan 2026|P50]]
- **XGBoost, LightGBM e atributos** (5): [[P51 Rodrigues 2025|P51]] [[P52 Georganos 2018|P52]] [[P53 Tianqi 2016|P53]] [[P54 Gündüz 2026|P54]] [[P55 Magidi 2024|P55]]
- **Pré-catalogação SAM/YOLO e representações** (12): [[P56 Osco 2023|P56]] [[P57 Ren 2024|P57]] [[P58 Hussain 2026|P58]] [[P59 Zhang 2025|P59]] [[P60 Wang 2024|P60]] [[P61 Wu 2025|P61]] [[P62 Carion 2025|P62]] [[P63 Dabaja 2026|P63]] [[P64 Siméoni 2025|P64]] [[P65 Faulkenberry 2026|P65]] [[P66 Brown 2025|P66]] [[P67 Xiong 2024|P67]]
- **Engenharia de dados** (7): [[P68 Ferreira 2020|P68]] [[P69 Ferreira 2022|P69]] [[P70 Simões 2021|P70]] [[P71 Appel 2019|P71]] [[P72 Schramm 2021|P72]] [[P73 Trujillo 2026|P73]] [[P74 Xi 2019|P74]]
- **Ciência de dados e curadoria** (6): [[P75 Roberts 2017|P75]] [[P76 Kerdreux 2025|P76]] [[P77 Shendryk 2019|P77]] [[P78 Pogorzelski 2025|P78]] [[P79 Reed 2022|P79]] [[P80 Feng 2025|P80]]
- **Planet: dados, qualidade e fusão** (10): [[P81 Frazier 2021|P81]] [[P82 Roy 2021|P82]] [[P83 Wang 2021|P83]] [[P84 Huang 2021|P84]] [[P85 Wang 2022|P85]] [[P86 Latte 2020|P86]] [[P87 Sadeh 2020|P87]] [[P88 Aragon 2021|P88]] [[P89 Kimm 2020|P89]] [[P90 Karwowska 2022|P90]]
- **Planet: aplicações adicionais** (17): [[P91 Zhang 2023|P91]] [[P92 Yang 2025|P92]] [[P93 Wagner 2025|P93]] [[P94 Pachêco 2025|P94]] [[P95 Huang 2022|P95]] [[P96 Wang 2022|P96]] [[P97 Deigele 2020|P97]] [[P98 Martins 2022|P98]] [[P99 Ossa 2023|P99]] [[P100 Crato 2025|P100]] [[P101 Winiwarter 2024|P101]] [[P102 Masolele 2024|P102]] [[P103 Glazer 2025|P103]] [[P104 McVicar 2023|P104]] [[P105 He 2022|P105]] [[P106 Rahul 2023|P106]] [[P107 Wang 2024|P107]]
- **Desmatamento e alertas** (17): [[P108 Bem 2020|P108]] [[P109 Torres 2021|P109]] [[P110 Alshehri 2024|P110]] [[P111 Andrade 2022|P111]] [[P112 Andrade 2020|P112]] [[P113 Jelas 2024|P113]] [[P114 Wang 2023|P114]] [[P115 McCallum 2023|P115]] [[P116 Doblas 2024|P116]] [[P117 Doblas 2022|P117]] [[P118 Reiche 2024|P118]] [[P119 Reiche 2021|P119]] [[P120 Ygorra 2024|P120]] [[P121 Çamalan 2022|P121]] [[P122 Cortinhas 2024|P122]] [[P123 Alencar 2020|P123]] [[P124 Hansen 2013|P124]]
- **Detecção de mudanças: métodos adicionais** (30): [[P125 Jiang 2022|P125]] [[P126 Shafique 2022|P126]] [[P127 Miller 2024|P127]] [[P128 Peng 2025|P128]] [[P129 Peng 2019|P129]] [[P130 Shen 2021|P130]] [[P131 Yang 2025|P131]] [[P132 Zhou 2025|P132]] [[P133 Ding 2024|P133]] [[P134 Mei 2024|P134]] [[P135 Wei 2025|P135]] [[P136 Zhang 2025|P136]] [[P137 Li 2024|P137]] [[P138 Zhang 2025|P138]] [[P139 Benidir 2025|P139]] [[P140 Zhao 2022|P140]] [[P141 Guo 2025|P141]] [[P142 Zhang 2026|P142]] [[P143 Xie 2026|P143]] [[P144 Peng 2024|P144]] [[P145 Zhang 2025|P145]] [[P146 Papadomanolaki 2019|P146]] [[P147 Basavaraju 2022|P147]] [[P148 Chen 2021|P148]] [[P149 Wang 2020|P149]] [[P150 Wu 2023|P150]] [[P151 Lu 2025|P151]] [[P152 Stewart 2022|P152]] [[P153 Xu 2024|P153]] [[P154 Ramos-Pollán 2024|P154]]
- **GeoAI e QGIS** (31): [[P155 Wu 2026|P155]] [[P156 Aszkowski 2023|P156]] [[P157 Tresson 2026|P157]] [[P158 Febrita 2025|P158]] [[P159 Cubillas 2024|P159]] [[P160 Guillou 2026|P160]] [[P161 Ciecholewski 2026|P161]] [[P162 Ruiz-Hurtado 2025|P162]] [[P163 Thomas 2026|P163]] [[P164 Wang 2024|P164]] [[P165 Wang 2025|P165]] [[P166 Jeon 2026|P166]] [[P167 Wu 2023|P167]] [[P168 Wu 2020|P168]] [[P169 Congedo 2021|P169]] [[P170 Zhou 2026|P170]] [[P171 Boutayeb 2024|P171]] [[P172 Mai 2025|P172]] [[P173 Mai 2024|P173]] [[P174 Carvalho 2026|P174]] [[P175 Šanca 2023|P175]] [[P176 Kleebauer 2025|P176]] [[P177 Gluski 2024|P177]] [[P178 Vardiashvili 2026|P178]] [[P179 Robinson 2026|P179]] [[P180 Muhammad 2022|P180]] [[P181 Amgoth 2023|P181]] [[P182 Baghel 2024|P182]] [[P183 Alshari 2022|P183]] [[P184 Ramadan 2022|P184]] [[P185 Kumari 2025|P185]]
