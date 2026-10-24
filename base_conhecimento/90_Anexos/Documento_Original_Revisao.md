---
tipo: anexo
titulo: "Documento original da revisão"
tags: [anexo, original]
---

> Cópia inalterada do documento que originou a coleta (fonte: `fonte_original/REVISAO_ORIGINAL.md`).

# Detecção e classificação de mudanças da cobertura terrestre com séries Planet

## Revisão bibliográfica orientada a mosaicos mensais de 3–5 m, 2020–2026

**Data da pesquisa:** 23 de outubro de 2026.  
**Objetivo:** fundamentar a identificação de supressão vegetal, novas construções, abertura de vias e outras transições, informando **onde ocorreu, entre quais datas e de qual cobertura para qual cobertura**.  
**Conteúdo:** 80 trabalhos catalogados, além de repositórios, documentação e proposta de avaliação. Os artigos de revisão, descritores de datasets, estudos aplicados, métodos e preprints são identificados separadamente.

**Atualização de escopo:** as seções 15–19 acrescentam 30 referências sobre XGBoost/LightGBM, pré-catalogação com SAM/YOLO, representações fundacionais, engenharia de dados e ciência de dados. A primeira seleção sub-representava essas frentes. Para desenhar o sistema completo, leia também as novas seções, especialmente P51, P54, P56–P60 e P68–P78.

> Esta é uma busca bibliográfica ampla e dirigida, não uma garantia de reunir literalmente todos os artigos existentes nem uma revisão sistemática concluída segundo PRISMA. A literatura é muito extensa. Foram priorizadas fontes primárias e referências transferíveis ao problema. A pesquisa verificou páginas editoriais, resumos, registros dos autores e trechos de texto completo quando disponíveis; não realizou leitura integral dos 80 trabalhos. Algumas páginas editoriais bloquearam a abertura, embora seus registros e resumos estivessem indexados. Não foram baixados todos os PDFs nem executados os modelos.

## 1. Resultado principal e ordem de leitura

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

## 2. Escopo e estratégia da busca

### 2.1 Critérios

- Inclusão: uso de Planet/PlanetScope/NICFI; mudanças florestais, urbanas, viárias ou de cobertura; séries temporais; mudança semântica; ML/DL; modelos fundacionais; datasets, avaliações e revisões diretamente úteis.
- Complementares: Landsat, Sentinel e imagens aéreas quando oferecem métodos de temporalidade, amostragem, topologia ou transferência. Não são apresentados como evidência direta de desempenho em Planet.
- Exclusão da bibliografia principal: páginas comerciais sem estudo científico, duplicatas entre preprint e publicação do mesmo trabalho, mudança de faixa de veículos e outros problemas sem relação com cobertura terrestre.
- Um artigo de dataset e o artigo de resultados de uma competição podem aparecer separadamente: são publicações diferentes, mas **não equivalem a duas validações independentes**.
- Fontes consultadas: páginas de periódicos e editoras, CVF, PMLR, arXiv, ISPRS, repositórios institucionais, documentação dos provedores e GitHub dos autores. Não houve consulta autenticada/exaustiva a Scopus ou Web of Science.
- Metadados: título e URL identificam cada trabalho. Autores são apresentados quando recuperados com segurança; listas completas e DOI ausentes devem ser importados da página primária antes de uma bibliografia ABNT final. O ano do DOI não foi usado automaticamente como ano de publicação.

### 2.2 Consultas efetivamente utilizadas, entre outras

```text
PlanetScope monthly mosaics land cover change detection deep learning deforestation time series paper
SpaceNet 7 multi temporal urban development challenge satellite 4m buildings paper
semantic change detection remote sensing SECOND HRSCD review deep learning
Planet NICFI deep learning tree cover loss Wagner 2023 deforestation U net
remote sensing road change detection deep learning dataset road construction multi temporal
Fully convolutional siamese networks change detection 2018 HRSCD semantic change detection 2019
SECOND semantic change detection asymmetric siamese network 2021
remote sensing change detection ChangeFormer BIT ChangeStar ChangeMamba papers
remote sensing semantic change detection ChangeMask Bi temporal semantic reasoning TSSCD paper
satellite time series change detection BFAST CCDC LandTrendr random forest papers
SAM change detection remote sensing AnyChange ChangeSAM foundation model Prithvi Clay 2025
PlanetScope land cover classification random forest object based Vizzari 2022
Good practices estimating area assessing accuracy land change Olofsson 2014
remote sensing semantic change detection Planet time series 2026 deep learning
DynamicEarthNet Daily 2022 Planet
Satellite Image Time Series Semantic Change Detection 2024
```

Foram feitas também buscas por títulos exatos e verificações de publicações de 2025–2026. A busca por modelos recentes não estabelece um ranking universal de desempenho.

## 3. O que conferir nos mosaicos antes de escolher o método

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

## 4. Catálogo comentado — trabalhos diretamente próximos de Planet

### P01 — Mapping Tropical Forest Cover and Deforestation with Planet NICFI Satellite Images and Deep Learning in Mato Grosso State (Brazil) from 2015 to 2021

- **Referência:** Wagner, F. H. et al., 2023. *Remote Sensing*, 15(2), 521. Artigo aplicado.
- **Fonte:** https://doi.org/10.3390/rs15020521 — [cópia institucional](https://vtechworks.lib.vt.edu/items/66fe4bdd-a06f-4f37-94f5-1da276f1ccb7).
- **Método/dados:** U-Net para cobertura arbórea e acompanhamento de perda usando Planet NICFI, aproximadamente 5 m.
- **Aplicação:** principal ponto de partida para a frente de supressão vegetal no Brasil.
- **Limite:** cobertura arbórea/não arbórea não distingue automaticamente construções, ruas e todas as formações vegetais; observar a mudança histórica da cadência NICFI.

### P02 — Mapping tropical forest degradation with deep learning and Planet NICFI data

- **Referência:** Dalagnol, R. et al., 2023. *Remote Sensing of Environment*. Artigo aplicado.
- **Fonte:** https://doi.org/10.1016/j.rse.2023.113798
- **Método/dados:** deep learning com U-Net e Planet NICFI para degradação; incorpora padrões de perda de árvores e textura.
- **Aplicação:** permite formular uma classe de degradação, além da supressão completa.
- **Limite:** transferir para outros biomas e tipos de perturbação exige novos exemplos; degradação não se resume a transição floresta → não floresta.

### P03 — Detection of forest disturbance across California using deep-learning on PlanetScope imagery

- **Referência:** Carter, G.; Wagner, F. H.; Dalagnol, R.; Roberts, S.; Ritz, A. L.; Saatchi, S., 2024. *Frontiers in Remote Sensing*.
- **Fonte:** https://doi.org/10.3389/frsen.2024.1409400
- **Método/dados:** U-Net, mosaicos visuais RGB a 4,77 m, mapas mensais de 2020–2022 e pós-processamento temporal.
- **Aplicação:** especialmente relevante se seus mosaicos forem RGB, sem NIR.
- **Limite:** contexto florestal e climático diferente. O artigo apresenta avaliações distintas de cobertura e perturbação; não confundir a acurácia da cobertura com a precisão de eventos de mudança.

### P04 — AI-based Validation of Deforestation Using High-Resolution Satellite Imagery in the Brazilian Amazon

- **Referência:** Wang, Z.; Li, Z.; Xie, Y.; Souza Jr., C.; Souza Filho, J. S.; Pinheiro, S., 2024. *ISPRS Archives*.
- **Fonte:** https://doi.org/10.5194/isprs-archives-XLVIII-3-2024-583-2024
- **Método/dados:** pares PlanetScope antes/depois para confirmar desmatamento candidato indicado por produtos de menor resolução.
- **Aplicação:** arquitetura em duas etapas: gerar candidatos e verificar mudanças em alta resolução.
- **Limite:** confirmar alertas não demonstra capacidade de encontrar todas as mudanças fora das áreas candidatas.

### P05 — Change Detection over mining areas using Deep Neural Networks from Planetscope image time series

- **Referência:** Zaraza-Aguilera, M. A.; Upegui, E. S.; Espejo-Valero, O. J., 2022. *IEEE Latin America Transactions*, 20(9), 2196–2205.
- **Fonte:** https://latamt.ieeer9.org/index.php/transactions/article/view/6556
- **Método/dados:** mina de Cerrejón, Colômbia; compara pós-classificação com U-Net/FPN a detecção direta por U-Net modificada em pares da série.
- **Aplicação:** evidência para comparar duas estratégias no seu piloto, incluindo solo exposto e alteração de grandes superfícies.
- **Limite:** desempenho em mineração não garante distinção entre obra, terraplenagem, via e solo naturalmente exposto. A página disponibiliza links de PDF e código.

### P06 — Determination of land use and land cover change using multi-temporal PlanetScope images and deep learning CNN model

- **Referência:** Şimşek, F. F., 2025. *Paddy and Water Environment*, 23, 405–423.
- **Fonte:** https://doi.org/10.1007/s10333-025-01024-9
- **Método/dados:** PlanetScope de 3 m, oito bandas, múltiplas datas e CNN; comparação com blocos cadastrais LPIS.
- **Aplicação:** classificação multitemporal e localização de áreas que exigem atualização cartográfica.
- **Limite:** não é equivalente a datar mensalmente cada mudança. Disponibilidade de oito bandas e qualidade temporal do cadastro precisam ser verificadas; o texto apresenta referências distintas ao ano de base do LPIS.

### P07 — PlanetScope, Sentinel-2, and Sentinel-1 Data Integration for Object-Based Land Cover Classification in Google Earth Engine

- **Referência:** Vizzari, M., 2022. *Remote Sensing*, 14(11), 2628.
- **Fonte:** https://doi.org/10.3390/rs14112628
- **Método/dados:** Random Forest, segmentação em objetos, textura e integração de sensores; classificação de cobertura no Brasil.
- **Aplicação:** baseline de ML para testar se o custo adicional do deep learning produz benefício real.
- **Limite:** classificar cobertura em uma composição não equivale a validar transições mensais; o estudo é complementar à detecção de mudanças.

### P08 — Evaluating satellite data and deep learning for identifying direct deforestation drivers in Cameroon

- **Referência:** 2025. *Remote Sensing Applications: Society and Environment*. Registro editorial localizado; autoria completa deve ser importada do artigo.
- **Fonte:** https://doi.org/10.1016/j.rsase.2025.101653
- **Método/dados:** comparação de dados de satélite e deep learning para categorias associadas ao desmatamento, incluindo composições Planet NICFI.
- **Aplicação:** investigar a ocupação posterior à perda vegetal, indo além do mapa binário.
- **Limite:** inferência de atividade associada à mudança não determina, por si, sua causa ou responsabilidade. Síntese baseada no registro/resumo indexado; abertura integral não obtida nesta busca.

### P09 — Tropical dry forest land use/land cover change detection using semi-supervised deep learning algorithms and remote sensing

- **Referência:** González-Vélez, J. C. et al., **2026**. *Environmental Monitoring and Assessment*, 198, 197. Publicado em 2/2/2026, apesar do DOI conter 2025.
- **Fonte:** https://doi.org/10.1007/s10661-025-14897-4
- **Método/dados:** pseudorrótulos, Y-Net, óptico/radar, PlanetScope e composições para floresta tropical seca na Colômbia.
- **Aplicação:** escassez de rótulos e confusão entre formações vegetais, áreas abertas e regeneração.
- **Limite:** composições anuais/semestrais reduzem a informação intranual; não replicar esse passo se o objetivo central for datar eventos mensais.

## 5. Séries temporais, edificações e transições semânticas

### P10 — The Multi-Temporal Urban Development SpaceNet Dataset

- **Referência:** Van Etten, A. et al., 2021. *CVPR*. Artigo de dataset — MUDS/SpaceNet 7.
- **Fonte:** https://arxiv.org/abs/2102.04420
- **Método/dados:** mosaicos Planet de aproximadamente 4 m, cerca de 24 observações mensais por local e polígonos de edificações com identidade temporal.
- **Aplicação:** referência prioritária para novas construções e acompanhamento de objetos em resolução próxima à sua.
- **Limite:** o desempenho depende do tamanho e separabilidade dos edifícios; não valida automaticamente contornos cadastrais precisos.

### P11 — The SpaceNet Multi-Temporal Urban Development Challenge

- **Referência:** Van Etten, A.; Hogan, D., 2021. *PMLR*, 133, 216–232. Resultados da competição.
- **Fonte:** https://proceedings.mlr.press/v133/etten21a.html
- **Método/dados:** comparação de soluções para localizar e rastrear edificações na série SpaceNet 7.
- **Aplicação:** consultar desenho da avaliação, associação entre meses e soluções reproduzíveis.
- **Código:** https://github.com/SpaceNetChallenge/SpaceNet7_Multi-Temporal_Solutions
- **Limite:** compartilha o benchmark de P10; não é uma validação independente em outro sensor ou município.

### P12 — DynamicEarthNet: Daily Multi-Spectral Satellite Dataset for Semantic Change Segmentation

- **Referência:** Toker, A. et al., 2022. *CVPR*. Dataset e benchmarks.
- **Fonte:** https://arxiv.org/abs/2203.12560
- **Método/dados:** observações Planet de 75 áreas, imagens diárias e rótulos mensais de sete classes; inclui métrica SCS para mudança semântica temporal.
- **Aplicação:** benchmark central para mudanças multiclasse, e não apenas edifícios.
- **Limite:** imagens diárias/Planet Fusion e mosaicos mensais convencionais não são o mesmo produto. Não presumir equivalência radiométrica ou temporal.

### P13 — Satellite Image Time Series Semantic Change Detection: Novel Architecture and Analysis of Domain Shift

- **Referência:** Vincent, E.; Ponce, J.; Aubry, M., 2024. Preprint consultado.
- **Fonte:** https://arxiv.org/abs/2407.07616
- **Método/dados:** arquitetura temporal avaliada em DynamicEarthNet e MUDS, com separação de mudanças de domínio espacial e temporal.
- **Aplicação:** fundamenta avaliar anos e áreas inéditos, em vez de apenas sortear patches da mesma paisagem.
- **Limite:** o artigo evidencia dificuldades com mudanças raras e transferência; usar uma série longa não elimina a necessidade de rótulos representativos.

### P14 — Time-series land cover change detection using deep learning-based temporal semantic segmentation

- **Referência:** He, H.; Yan, J.; Liang, D.; Sun, Z.; Li, J.; Wang, L., 2024. *Remote Sensing of Environment*, 305, 114101.
- **Fonte:** https://doi.org/10.1016/j.rse.2024.114101
- **Método/dados:** TSSCD; composições mensais Sentinel-2 de 10/20 m para estimar localização, momento e tipo de alteração.
- **Aplicação:** correspondência conceitual muito alta com o projeto.
- **Código/dados:** https://github.com/CUG-BEODL/TSSCD ; https://zenodo.org/records/10846539
- **Limite:** arquitetura temporal relevante, mas resolução e bandas diferentes das suas.

### P15 — Panoptic Segmentation of Satellite Image Time Series With Convolutional Temporal Attention Networks

- **Referência:** Sainte Fare Garnot, V.; Landrieu, L., 2021. *ICCV*.
- **Fonte:** https://openaccess.thecvf.com/content/ICCV2021/papers/Garnot_Panoptic_Segmentation_of_Satellite_Image_Time_Series_With_Convolutional_Temporal_ICCV_2021_paper.pdf
- **Método/dados:** U-TAE, PaPs e PASTIS; atenção temporal em séries Sentinel-2.
- **Aplicação:** referência de encoder espaço-temporal para aproveitar várias observações.
- **Código:** https://github.com/VSainteuf/utae-paps
- **Limite:** segmentação agrícola/panóptica não é um detector pronto de supressão e construção; exige adaptação da tarefa e dos rótulos.

### P16 — HiSTENet: History-Integrated Spatial–Temporal Information Extraction Network for Time Series Remote Sensing Image Change Detection

- **Referência:** 2025. *Remote Sensing*, 17(5), 792.
- **Fonte:** https://www.mdpi.com/2072-4292/17/5/792
- **Método:** detecção temporal com integração do histórico espacial e temporal.
- **Aplicação:** candidato adicional para comparar histórico multitemporal com pares isolados.
- **Limite:** confirmar no texto integral quantidade de entradas, datasets e recursos de reprodução antes de selecionar para implementação; inclusão baseada na página editorial indexada.

### P17 — Urban Change Forecasting from Satellite Images

- **Referência:** 2023. *PFG — Journal of Photogrammetry, Remote Sensing and Geoinformation Science*.
- **Fonte:** https://doi.org/10.1007/s41064-023-00258-8
- **Método/dados:** previsão de mudança urbana usando SpaceNet 7 e aprendizado com arquitetura siamesa/U-Net.
- **Aplicação:** extensão futura para previsão de expansão, depois de validar mudanças observadas.
- **Limite:** **forecasting é previsão**, não evidência de que uma nova construção já existe.

### P18 — Multitask Learning for Large-scale Semantic Change Detection

- **Referência:** Daudt, R. C.; Le Saux, B.; Boulch, A.; Gousseau, Y., 2019. *Computer Vision and Image Understanding*; preprint de 2018.
- **Fonte:** https://arxiv.org/abs/1810.08452
- **Método/dados:** HRSCD e aprendizado conjunto de classificação de cobertura e mudança.
- **Aplicação:** base para dois mapas semânticos e uma máscara de mudança coerentes entre si.
- **Limite:** imagens aéreas RGB e condições diferentes de Planet; não transferir números de desempenho diretamente.

### P19 — Asymmetric Siamese Networks for Semantic Change Detection in Aerial Images

- **Referência:** Yang, K. et al., 2021. *IEEE TGRS*; preprint de 2020 com título ligeiramente diferente.
- **Fonte:** https://ieeexplore.ieee.org/document/9555824/ — https://arxiv.org/abs/2010.05687
- **Método/dados:** ASN, dataset SECOND e métrica SeK; modelagem de classes antes/depois.
- **Aplicação:** organizar avaliação de transições semânticas.
- **Projeto:** https://captain-whu.github.io/SCD/
- **Limite:** benchmark bitemporal não resolve sozinho a cronologia de uma série de vários anos.

### P20 — ChangeMask: Deep multi-task encoder-transformer-decoder architecture for semantic change detection

- **Referência:** 2022. *ISPRS Journal of Photogrammetry and Remote Sensing*.
- **Fonte:** https://www.sciencedirect.com/science/article/pii/S0924271621002835
- **Método:** arquitetura multitarefa que conecta segmentação semântica e mudança.
- **Aplicação:** candidato a modelo conjunto para evitar divergência entre “mudou” e classes previstas.
- **Limite:** testar consistência e transferência local; não representa automaticamente séries mensais inteiras.

### P21 — Bi-Temporal Semantic Reasoning for the Semantic Change Detection in HR Remote Sensing Images

- **Referência:** Ding, L.; Guo, H.; Liu, S.; Mou, L.; Zhang, J.; Bruzzone, L., 2022. *IEEE TGRS*.
- **Fonte:** https://iris.unitn.it/handle/11572/400193
- **Método:** raciocínio semântico bitemporal para localizar mudanças e categorizar coberturas anteriores e posteriores.
- **Aplicação:** reduzir inconsistências na interpretação das transições.
- **Limite:** necessita exemplos das classes e condições do local; pares de datas continuam exigindo consolidação temporal.

### P22 — The ClearSCD model: Comprehensively leveraging semantics and change relationships for semantic change detection in high spatial resolution remote sensing imagery

- **Referência:** 2024. *ISPRS Journal of Photogrammetry and Remote Sensing*.
- **Fonte:** https://www.sciencedirect.com/science/article/pii/S0924271624001734
- **Método:** relações semânticas entre datas e comparação no espaço de probabilidades de classificação.
- **Aplicação:** avaliar transições com probabilidades, não apenas subtrair rótulos rígidos.
- **Limite:** probabilidades do modelo precisam ser avaliadas/calibradas para uso como confiança operacional.

## 6. Detectores profundos e modelos fundacionais

### P23 — Fully Convolutional Siamese Networks for Change Detection

- **Referência:** Daudt, R. C.; Le Saux, B.; Boulch, A., 2018. *ICIP*.
- **Fonte:** https://arxiv.org/abs/1810.08462
- **Método:** FC-EF, FC-Siam-conc e FC-Siam-diff, comparando imagens corregistradas.
- **Aplicação:** baseline profundo simples, importante para comparar com redes mais complexas.
- **Código:** https://github.com/rcdaudt/fully_convolutional_change_detection
- **Limite:** normalmente produz mudança binária; requer outra saída para dizer o que mudou.

### P24 — A Spatial-Temporal Attention-Based Method and a New Dataset for Remote Sensing Image Change Detection

- **Referência:** Chen, H.; Shi, Z., 2020. *Remote Sensing*, 12(10), 1662.
- **Fonte:** https://doi.org/10.3390/rs12101662
- **Método/dados:** STANet e LEVIR-CD, referência de mudanças em edificações.
- **Código:** https://github.com/justchenhao/STANet
- **Aplicação:** atenção espacial/temporal e avaliação de construção.
- **Limite:** LEVIR-CD não tem a mesma resolução dos mosaicos Planet de 3–5 m.

### P25 — Remote Sensing Image Change Detection With Transformers

- **Referência:** Chen, H.; Qi, Z.; Shi, Z. Publicação online em 2021, volume 60 de *IEEE TGRS*, 2022.
- **Fonte:** https://doi.org/10.1109/TGRS.2021.3095166 — https://arxiv.org/abs/2103.00208
- **Método:** BIT, transformer bitemporal para incorporar contexto de longo alcance.
- **Aplicação:** baseline de transformer para mudança binária.
- **Limite:** contexto amplo não recupera objetos que a resolução da imagem não representa adequadamente.

### P26 — A Transformer-Based Siamese Network for Change Detection

- **Referência:** Bandara, W. G. C.; Patel, V. M., 2022. *IGARSS* — ChangeFormer.
- **Fonte:** https://arxiv.org/abs/2201.01293
- **Código:** https://github.com/wgcban/ChangeFormer
- **Método:** rede siamesa com transformers para pares corregistrados.
- **Aplicação:** comparar com U-Net/FC-Siam sob os mesmos dados, rótulos e orçamento.
- **Limite:** adaptação para bandas adicionais e saída semântica deve ser explícita.

### P27 — Change Is Everywhere: Single-Temporal Supervised Object Change Detection in Remote Sensing Imagery

- **Referência:** Zheng, Z.; Ma, A.; Zhang, L.; Zhong, Y., 2021. *ICCV* — ChangeStar/STAR.
- **Fonte:** https://openaccess.thecvf.com/content/ICCV2021/html/Zheng_Change_Is_Everywhere_Single-Temporal_Supervised_Object_Change_Detection_in_Remote_ICCV_2021_paper.html
- **Método:** aprendizado de mudança a partir de supervisão de uma única data.
- **Aplicação:** aproveitar mapas e polígonos disponíveis quando faltam pares anotados.
- **Limite:** supervisão construída não substitui teste independente em mudanças reais.

### P28 — ChangeMamba: Remote Sensing Change Detection With Spatiotemporal State Space Model

- **Referência:** Chen, H.; Song, J.; Han, C.; Xia, J.; Yokoya, N., 2024. Versão consultada no arXiv.
- **Fonte:** https://arxiv.org/abs/2404.03425
- **Método:** variantes MambaBCD, MambaSCD e MambaBDA para mudança binária, semântica e danos.
- **Código:** https://github.com/ChenHongruixuan/MambaCD
- **Aplicação:** candidato moderno para comparar eficiência e desempenho semântico.
- **Limite:** o nome espaço-temporal não implica aceitar qualquer comprimento de série sem modificação.

### P29 — Segment Any Change

- **Referência:** Zheng, Z.; Zhong, Y.; Zhang, L.; Ermon, S., 2024. *NeurIPS*.
- **Fonte:** https://arxiv.org/abs/2402.01188
- **Método:** AnyChange; adaptação sem treinamento do SAM por correspondência latente bitemporal.
- **Código:** https://github.com/Z-Zheng/pytorch-change-models
- **Aplicação:** gerar candidatos e apoiar exploração/anotação com pouca supervisão.
- **Limite:** capacidade zero-shot não garante taxa aceitável de falsos positivos em mosaicos Planet; testar deslocamentos, textura e sombras.

### P30 — Semantic-CD: Remote Sensing Image Semantic Change Detection towards Open-vocabulary Setting

- **Referência:** 2025. Preprint consultado.
- **Fonte:** https://arxiv.org/abs/2501.06808
- **Método:** CLIP, prompts semânticos e decodificação de mudança binária/semântica.
- **Aplicação:** investigar categorias descritas por texto e assistência à classificação.
- **Limite:** vocabulário aberto não equivale a reconhecer com confiabilidade toda classe territorial local.

### P31 — TextSCD: Leveraging Text-based Semantic Guidance for Remote Sensing Image Semantic Change Detection

- **Referência:** 2025. *ISPRS Annals*, X-G-2025, 383.
- **Fonte:** https://isprs-annals.copernicus.org/articles/X-G-2025/383/2025/index.html
- **Método:** orientação textual para predição de alterações semânticas.
- **Aplicação:** avaliar se descrições de classes ajudam na separação das transições.
- **Limite:** textos não fornecem, sozinhos, comprovação física da mudança.

### P32 — Prithvi-EO-2.0: A Versatile Multitemporal Foundation Model for Earth Observation Applications

- **Referência:** Szwarcman, D. et al.; preprint de 2024 e publicação em *IEEE TGRS*, volume 64, 2026.
- **Fonte:** https://arxiv.org/abs/2412.02732 — https://doi.org/10.1109/TGRS.2025.3642610
- **Método:** modelo fundacional multitemporal para observação da Terra.
- **Aplicação:** backbone candidato, principalmente em experimentos que integrem outras fontes.
- **Limite:** não é detector Planet pronto. Conferir bandas, normalização, resolução e requisitos do checkpoint antes de ajustar.

### P33 — Remote Sensing Change Detection via Weak Temporal Supervision

- **Referência:** Bou, X.; Vincent, E.; Facciolo, G.; Grompone von Gioi, R.; Morel, J.-M.; Ehret, T., 2026. Preprint.
- **Fonte:** https://arxiv.org/abs/2601.02126
- **Método:** observações temporais adicionais e supervisão fraca para reduzir novas anotações.
- **Aplicação:** aproveitar seu acervo longo com rótulos limitados.
- **Limite:** a hipótese de predominância de não mudança cria rótulos ruidosos; avaliar separadamente bairros/áreas em rápida transformação.

### P34 — Foundation Model-Driven Semantic Change Detection in Remote Sensing Imagery

- **Referência:** Shen, H. et al., 2026. Preprint — PerASCD.
- **Fonte:** https://arxiv.org/abs/2602.13780
- **Método:** modelo fundacional, decoder com gates e consistência semântica.
- **Código:** https://github.com/SathShen/PerASCD
- **Aplicação:** candidato recente para fine-tuning semântico.
- **Limite:** resultados em benchmarks não comprovam operação em seus mosaicos mensais.

### P35 — Seg2Change: Adapting Open-Vocabulary Semantic Segmentation Model for Remote Sensing Change Detection

- **Referência:** Su, Y.; Song, Y.; Chen, J.; Wen, Z., 2026. Preprint.
- **Fonte:** https://arxiv.org/abs/2604.11231
- **Método:** adaptação de segmentação de vocabulário aberto à detecção de mudanças; dataset CA-CDD.
- **Código:** https://github.com/yogurts-sy/Seg2Change
- **Aplicação:** linha exploratória para novas categorias sem refazer toda a taxonomia de treinamento.
- **Limite:** tratar como pesquisa a avaliar, não como substituição imediata de modelos supervisionados localmente.

## 7. Ruas, redes viárias e informação cartográfica prévia

### P36 — RB-SCD: A New Benchmark for Semantic Change Detection of Roads and Bridges in Traffic Scenes

- **Referência:** Shu, Q.; Chen, S.; You, Z.; Lu, W.; Tang, J.; Luo, B., 2025. Preprint consultado.
- **Fonte:** https://arxiv.org/abs/2505.13212
- **Método/dados:** 260 pares de imagens de alta resolução, 11 categorias de mudança em vias/pontes e modelo MFDCD.
- **Aplicação:** taxonomia e detecção de construção, reforma e remoção de infraestrutura viária.
- **Limite:** categorias finas podem ser incompatíveis com 3–5 m. Confirmar tamanho dos alvos e resolução do benchmark antes de transferir.

### P37 — RoadTracer: Automatic Extraction of Road Networks From Aerial Images

- **Referência:** Bastani, F. et al., 2018. *CVPR*.
- **Fonte:** https://openaccess.thecvf.com/content_cvpr_2018/html/Bastani_RoadTracer_Automatic_Extraction_CVPR_2018_paper.html
- **Projeto:** https://roadmaps.csail.mit.edu/roadtracer/
- **Método:** extração da rede viária como estrutura conectada.
- **Aplicação:** fundamentar avaliação de conectividade, além de sobreposição de pixels.
- **Limite:** extração em uma data não é detecção temporal; imagens e escalas distintas de Planet.

### P38 — Fully Convolutional Network for Automatic Road Extraction From Satellite Imagery

- **Referência:** Buslaev, A. et al., 2018. *CVPR Workshops*.
- **Fonte:** https://openaccess.thecvf.com/content_cvpr_2018_workshops/w4/html/Buslaev_Fully_Convolutional_Network_CVPR_2018_paper.html
- **Método:** rede da família U-Net para extração viária no DeepGlobe.
- **Aplicação:** baseline de máscara de vias, depois combinável entre datas.
- **Limite:** pixel de via em duas datas não basta para diferenciar abertura, pavimentação e alteração de iluminação.

### P39 — MapFormer: Boosting Change Detection by Using Pre-change Information

- **Referência:** Bernhard, M.; Strauß, N.; Schubert, M., 2023. *ICCV*.
- **Fonte:** https://arxiv.org/abs/2303.17859
- **Método:** detecção condicionada por mapas semânticos prévios.
- **Código:** https://github.com/mxbh/mapformer
- **Aplicação:** usar cartografia existente como informação adicional para localizar atualizações.
- **Limite:** mapa anterior desatualizado ou mal alinhado pode induzir erros. Avaliar qualidade e data da referência.

### P40 — Road Change Detection Using Maps and Aerial Imagery for Digital Map Updating

- **Referência:** Lee, J. et al., 2026. *Korean Journal of Remote Sensing*, 42(2).
- **Fonte:** https://www.kjrs.org/journal/view.html?doi=10.7780%2Fkjrs.2026.42.2.5
- **Método:** adaptação do MapFormer para atualização viária, mapas e ortofotos; tratamento do desbalanceamento.
- **Aplicação:** caso específico de mudança em ruas, complementar a P39.
- **Limite:** ortofotos de alta resolução e contexto sul-coreano; não tratar a transferência para Planet como demonstrada.

## 8. Métodos temporais clássicos e avaliação científica

### P41 — Detecting trend and seasonal changes in satellite image time series

- **Referência:** Verbesselt, J.; Hyndman, R.; Newnham, G.; Culvenor, D., 2010. *Remote Sensing of Environment*, 114(1), 106–115.
- **Fonte:** https://doi.org/10.1016/j.rse.2009.08.014 — [PDF do autor](https://robjhyndman.com/papers/bfast1.pdf).
- **Método:** BFAST, decomposição de tendência e sazonalidade com detecção de rupturas.
- **Aplicação:** baseline temporal para distinguir sazonalidade de mudança persistente.
- **Limite:** ruptura espectral não fornece automaticamente a classe posterior. Método estatístico, não deep learning.

### P42 — Continuous change detection and classification of land cover using all available Landsat data

- **Referência:** Zhu, Z.; Woodcock, C. E., 2014. *Remote Sensing of Environment*.
- **Fonte:** https://doi.org/10.1016/j.rse.2014.01.011
- **Método:** CCDC, modelagem contínua, detecção de rupturas e classificação.
- **Código:** https://github.com/GERSL/CCDC
- **Aplicação:** referência para separar detecção do evento e atribuição da cobertura.
- **Limite:** entrada Landsat, bandas e densidade observacional diferentes. Não aplicar parâmetros originais a Planet sem calibração.

### P43 — Detecting trends in forest disturbance and recovery using yearly Landsat time series: 1. LandTrendr — Temporal segmentation algorithms

- **Referência:** Kennedy, R. E.; Yang, Z.; Cohen, W. B., 2010. *Remote Sensing of Environment*, 114, 2897–2910.
- **Fonte:** https://doi.org/10.1016/j.rse.2010.07.008 — https://research.fs.usda.gov/treesearch/54160
- **Método:** segmentação temporal de trajetórias anuais de perturbação e recuperação.
- **Aplicação:** produto anual complementar e interpretação de regeneração.
- **Limite:** não é a primeira escolha para localizar meses de mudança em uma série de apenas sete anos.

### P44 — Demystifying LandTrendr and CCDC temporal segmentation

- **Referência:** 2022. *International Journal of Applied Earth Observation and Geoinformation*.
- **Fonte:** https://www.sciencedirect.com/science/article/pii/S1569843222000085
- **Método/contribuição:** explica diferenças entre segmentações LandTrendr e CCDC.
- **Aplicação:** orientar escolha de frequência temporal e interpretação dos segmentos.
- **Limite:** referência metodológica complementar; não constitui validação direta com Planet.

### P45 — Dynamic World, Near real-time global 10 m land use land cover mapping

- **Referência:** Brown, C. F. et al., 2022. *Scientific Data*, 9, 251.
- **Fonte:** https://doi.org/10.1038/s41597-022-01307-4
- **Método/dados:** deep learning para cobertura Sentinel-2 com probabilidades por classe.
- **Aplicação:** fonte auxiliar de contexto, comparação e eventual pré-rotulagem.
- **Limite:** não usar como verdade de campo independente se seus rótulos ou modelo derivarem do próprio produto; 10 m não resolve detalhamento de edificações em 3–5 m.

### P46 — Good practices for estimating area and assessing accuracy of land change

- **Referência:** Olofsson, P.; Foody, G. M.; Herold, M.; Stehman, S. V.; Woodcock, C. E.; Wulder, M. A., 2014. *Remote Sensing of Environment*, 148, 42–57.
- **Fonte:** https://doi.org/10.1016/j.rse.2014.02.015
- **Contribuição:** amostragem probabilística, matriz de erro, estimativas de área e intervalos de confiança.
- **Aplicação:** essencial para sustentar quantos hectares mudaram e a incerteza associada.
- **Limite:** contar pixels classificados fornece área mapeada; não equivale, por si, a uma estimativa de área corrigida pelos erros.

### P47 — Key issues in rigorous accuracy assessment of land cover products

- **Referência:** 2019. *Remote Sensing of Environment*. Artigo metodológico/revisão de avaliação.
- **Fonte:** https://www.sciencedirect.com/science/article/pii/S0034425719302111
- **Contribuição:** desenho e documentação rigorosos de validação de mapas.
- **Aplicação:** auditar independência da amostra, referência e inferência das métricas.
- **Limite:** não substitui um protocolo local para datas incertas, alvos pequenos e mudanças raras.

## 9. Revisões para ampliar a bibliografia

### P48 — Deep learning change detection techniques for optical remote sensing imagery: Status, perspectives and challenges

- **Referência:** Peng, D. et al., 2025. *International Journal of Applied Earth Observation and Geoinformation*.
- **Fonte:** https://www.sciencedirect.com/science/article/pii/S1569843224006381
- **Contribuição:** panorama de datasets, métodos e desafios de mudança em imagens ópticas.
- **Uso:** buscar referências adicionais por família de arquitetura e tipo de mudança.
- **Limite:** revisão oferece mapa da área; consultar os estudos originais antes de reutilizar resultados quantitativos.

### P49 — Remote sensing image change detection using deep learning techniques: a comprehensive survey

- **Referência:** Lei, T. et al., 2026. *Artificial Intelligence Review*.
- **Fonte:** https://doi.org/10.1007/s10462-026-11501-0
- **Contribuição:** revisão de aprendizado supervisionado, semissupervisionado e não supervisionado, com diferentes modalidades de sensoriamento.
- **Uso:** atualizar o panorama e identificar estratégias para poucos rótulos.
- **Limite:** técnicas SAR/hiperespectrais não são diretamente compatíveis com RGB ou quatro bandas Planet.

### P50 — Change Detection in Remote Sensing Imagery: A Systematic Review of Statistical, Machine Learning, and Deep Learning Methods

- **Referência:** Jabbarizadegan, M. et al., 2026. *Remote Sensing*, 18(15), 2573.
- **Fonte:** https://doi.org/10.3390/rs18152573
- **Contribuição:** revisão que declara analisar 144 estudos primários, abrangendo métodos estatísticos, ML e DL.
- **Uso:** principal trilha para expandir este catálogo por rastreamento de referências.
- **Limite:** os 144 trabalhos da revisão **não foram todos individualmente verificados nem incorporados** aqui. O total deste documento ampliado é de 80 registros; não se deve somar os trabalhos citados por uma revisão como se fossem novas referências verificadas.

## 10. Ferramentas e código para transformar a revisão em experimento

Esta seção contém software e documentação, não artigos adicionais. A presença de um repositório não garante que o ambiente execute sem adaptação; versões e licenças devem ser registradas na implementação.

| Recurso | Papel no projeto | Fonte oficial/autores |
|---|---|---|
| TorchGeo | Datasets, amostragem geográfica, treinamento e tutoriais de mudança | https://github.com/torchgeo/torchgeo |
| Tutorial de mudança TorchGeo | Exemplo de treinamento bitemporal | https://docs.torchgeo.org/en/v0.10.1/tutorials/change_detection.html |
| Open-CD | Comparar arquiteturas sob uma infraestrutura comum | https://github.com/likyoo/open-cd |
| PyTorch Change Models / AnyChange | Exploração de ChangeStar e detecção com SAM | https://github.com/Z-Zheng/pytorch-change-models |
| SpaceNet 7 solutions | Soluções de rastreamento de edifícios | https://github.com/SpaceNetChallenge/SpaceNet7_Multi-Temporal_Solutions |
| TSSCD | Referência de segmentação temporal | https://github.com/CUG-BEODL/TSSCD |
| U-TAE | Encoder temporal e segmentação | https://github.com/VSainteuf/utae-paps |
| ChangeFormer | Baseline transformer bitemporal | https://github.com/wgcban/ChangeFormer |
| ChangeMamba | Variantes binárias e semânticas com Mamba | https://github.com/ChenHongruixuan/MambaCD |
| MapFormer | Incorporação de cartografia anterior | https://github.com/mxbh/mapformer |
| CCDC | Referência clássica de modelagem temporal | https://github.com/GERSL/CCDC |
| BFAST | Rupturas e sazonalidade; implementação de referência em R | https://bfast.r-forge.r-project.org/ |

Para um pipeline Python, organizar leitura e alinhamento raster, cubo temporal, treinamento, inferência em blocos e saída vetorial em etapas separadas. O fato de parte das referências usar GEE, R ou MATLAB não obriga a adotá-los no produto final. Evitar apresentar implementações Python de terceiros como reprodução exata sem comparar seus resultados à referência.

## 11. Taxonomia inicial proposta para as alterações

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

## 12. Experimento recomendado a partir da literatura

### 12.1 Perguntas que o piloto deve responder

1. O histórico mensal melhora a detecção em relação a pares de datas?
2. Qual a menor área de supressão, edificação e largura de via detectável com precisão aceitável?
3. Qual é a diferença de desempenho entre produtos de 3 m e de 5 m?
4. Quanto os erros aumentam ao mudar de ano, sensor/produto e setor geográfico?
5. Qual benefício se obtém de NIR, quando disponível, frente ao RGB?
6. Qual o custo de revisão humana por evento verdadeiro confirmado?

### 12.2 Comparações mínimas

| Experimento | Base bibliográfica | Hipótese testada |
|---|---|---|
| Random Forest com atributos espectrais/texturais + comparação temporal | P07, P42 | Baseline de ML pode ser competitivo com poucos rótulos |
| U-Net mensal + regra de persistência | P01–P03, P05 | Segmentação consistente pode ser suficiente para parte dos eventos |
| FC-Siam ou ChangeFormer em pares | P23, P26 | Aprender a mudança diretamente reduz erros da pós-classificação |
| Modelo semântico conjunto | P18–P22 | Coerência entre classes e mudança melhora as transições |
| Modelo de série, inspirado em TSSCD/P13 | P13–P15 | Histórico reduz sazonalidade e melhora localização temporal |
| AnyChange como candidato/assistente | P29 | Pré-anotação pode reduzir esforço, mantendo revisão independente |

Começar pelos três primeiros e pelo teste temporal prioritário, conforme volume de rótulos e recursos. Não é necessário implementar todas as arquiteturas do catálogo. Preservar os mesmos conjuntos de teste e critérios para comparar os modelos.

### 12.3 Rótulos e separação dos dados

- Rotular **áreas estáveis e mudanças reais**, com exemplos difíceis: sombras, variação hídrica, mosaicos desalinhados, solo arenoso, telhados claros e vegetação sazonal.
- Separar treino/validação/teste por blocos geográficos; evitar patches vizinhos ou sobrepostos entre os conjuntos.
- Reservar períodos posteriores para teste temporal, além do teste espacial. Documentar se o teste envolve simultaneamente outro produto ou resolução.
- Rotular a transição com imagem anterior e posterior válidas; incluir intervalo de incerteza quando houver nuvens ou composição temporal ampla.
- Distinguir avaliação retrospectiva, que pode usar meses futuros, de alerta operacional, que só pode usar o passado disponível. Comparar os dois regimes separadamente.
- Se usar pseudorrótulos de outro mapa/modelo, construir amostra final independente com interpretação especializada e, quando possível, imagens de maior resolução ou campo.

### 12.4 Métricas mínimas

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

## 13. Como continuar até uma revisão sistemática publicável

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

## 14. Limitações deste levantamento

- O catálogo é dirigido ao seu objetivo; não representa um censo de toda a produção científica.
- A qualidade metodológica de cada estudo ainda precisa de avaliação integral. Inclusão não significa endosso de todos os procedimentos ou resultados.
- Nos registros acessados apenas por resumo/indexação, detalhes não confirmados foram omitidos ou marcados para conferência.
- Preprints não foram tratados automaticamente como artigos revisados por pares. Quando a versão consultada é preprint, isso foi indicado.
- Código localizado não foi instalado/testado; disponibilidade de pesos e licença deve ser confirmada na execução.
- Não houve inspeção dos seus rasters: produto, bandas, qualidade, abrangência espacial e número real de meses permanecem a verificar.
- A recomendação central é testar **classificação semântica temporal com validação local**, mantendo trilhas específicas para vegetação, edificações e vias. Não há evidência suficiente nesta revisão para prometer que um único modelo classifique todas as alterações em 3–5 m.

## 15. XGBoost, LightGBM e classificação baseada em atributos

XGBoost não é substituído automaticamente por arquiteturas mais recentes. Ele atua sobre vetores de atributos: bandas, índices, textura, geometria, contexto, estatísticas temporais ou embeddings. SAM pode ajudar a delimitar objetos; um classificador pode atribuir suas classes; a análise temporal pode identificar transições. A integração precisa ser validada, pois erros de segmentação propagam-se para as etapas seguintes.

### P51 — Machine Learning-Based Cerrado Land Cover Classification Using PlanetScope Imagery

- **Referência:** Rodrigues, T.; Takahashi, F.; Dias, A.; Lima, T.; Alcântara, E., 2025. *Remote Sensing*, 17(3), 480.
- **Fonte:** https://doi.org/10.3390/rs17030480
- **Evidência direta:** compara **XGBoost, Random Forest e SVM em PlanetScope de 4,77 m** para classes de cobertura do Cerrado.
- **Resultado contextualizado:** tabela 5 apresenta F1 ponderado de 0,97 para XGBoost. Os testes entre classificadores apresentados não indicam diferenças significativas; não há suporte para afirmar superioridade geral do XGBoost.
- **Aplicação:** baseline prioritário de cobertura vegetal. É classificação, não validação de todas as transições mensais ou de edifícios. Não transportar a acurácia publicada para outra região.

### P52 — Very High Resolution Object-Based Land Use-Land Cover Urban Classification Using Extreme Gradient Boosting

- **Referência:** Georganos, S.; Grippa, T.; Vanhuysse, S.; Lennert, M.; Shimoni, M.; Wolff, E., 2018. *IEEE Geoscience and Remote Sensing Letters*, 15(4), 607–611.
- **Fonte:** https://doi.org/10.1109/LGRS.2018.2803259
- **Método:** XGBoost por objetos, seleção de atributos e parametrização bayesiana; comparação com RF/SVM em ambientes urbanos.
- **Aplicação:** fundamento para classificar segmentos por espectro, textura e forma.
- **Limite:** classificação urbana VHR, sem demonstração de catálogo temporal Planet. Substituir a segmentação original por SAM constitui um novo experimento.

### P53 — XGBoost: A Scalable Tree Boosting System

- **Referência:** Chen, T.; Guestrin, C., 2016. *ACM SIGKDD*.
- **Fonte:** https://arxiv.org/abs/1603.02754
- **Contribuição:** artigo do sistema de gradient boosting escalável.
- **Aplicação:** fundamentar implementação e processamento de uma tabela de atributos por pixel, objeto ou trajetória.
- **Limite:** referência geral de ML; não é um estudo de sensoriamento remoto e não comprova qualidade de classificação Planet.

### P54 — An Explainable and Optimized Machine Learning Framework for Multisensor Remote Sensing-Based Land Use and Land Cover Classification

- **Referência:** Gündüz et al., 2026. *Transactions in GIS*.
- **Fonte:** https://doi.org/10.1111/tgis.70293
- **Método:** RF, XGBoost e LightGBM; cinco estratégias de seleção de atributos; Optuna, validação espacial e SHAP. Usa Sentinel-1/2 e fontes auxiliares.
- **Aplicação:** referência especialmente útil de **ciência de dados aplicada**: seleção, otimização e interpretação. No experimento relatado, a combinação de melhor desempenho foi HSIC-Lasso + LightGBM, não XGBoost.
- **Limite:** não é série mensal Planet; SHAP explica associações do modelo, não causas físicas da mudança. Seleção e ajuste devem ficar dentro dos dados de treinamento de cada partição.

### P55 — Land use and land cover changes in Notwane watershed, Botswana, using extreme gradient boost (XGBoost) machine learning algorithm

- **Referência:** Magidi, J. et al. *African Geographical Review*. Registro com DOI de 2024 e publicação em volume de 2025; conferir versão bibliográfica final ao importar a citação.
- **Fonte:** https://doi.org/10.1080/19376812.2024.2424378
- **Método/dados:** classificação Landsat com XGBoost e análise das mudanças em diferentes anos, incluindo vegetação, água, agricultura e áreas construídas.
- **Aplicação:** exemplo concreto de XGBoost dentro de um fluxo de mudança por pós-classificação.
- **Limite:** Landsat e intervalos longos não demonstram identificação mensal de pequenas obras.

## 16. Pré-catalogação e pré-anotação com SAM, YOLO e modelos recentes

**Três conceitos que precisam permanecer separados:**

- **Segmentação:** delimitar regiões ou objetos.
- **Classificação semântica:** atribuir categorias às regiões.
- **Identidade temporal:** decidir se objetos em meses distintos representam a mesma entidade, uma alteração, um desaparecimento ou uma nova entidade.

SAM original produz máscaras orientadas por prompts, sem fornecer por si uma taxonomia territorial. Grounded SAM combina detecção aberta com segmentação; YOLO pode fornecer classes/caixas após treinamento adequado; SAM 3 acrescenta prompts conceituais. Nenhuma dessas capacidades dispensa medir erros no domínio Planet.

### P56 — The Segment Anything Model (SAM) for remote sensing applications: From zero to one shot

- **Referência:** Osco, L. P. et al., 2023. *International Journal of Applied Earth Observation and Geoinformation*.
- **Fonte:** https://doi.org/10.1016/j.jag.2023.103540 — https://arxiv.org/abs/2306.16623
- **Método:** explora adaptação e aplicação de SAM no sensoriamento remoto, incluindo segmentação orientada por texto e exemplos.
- **Aplicação:** leitura prioritária para gerar máscaras preliminares e reduzir delineamento manual.
- **Limite:** máscaras não equivalem a rótulos de referência. Erros devem ser revisados antes de treinamento e quantificados em teste independente.

### P57 — Grounded SAM: Assembling Open-World Models for Diverse Visual Tasks

- **Referência:** Ren, T. et al., 2024. Preprint consultado.
- **Fonte:** https://arxiv.org/abs/2401.14159
- **Método:** Grounding DINO para detecção de vocabulário aberto combinado ao SAM para segmentação; discute pipelines de anotação automática.
- **Aplicação:** texto → caixas candidatas → máscaras → revisão.
- **Limite:** artigo de visão geral, não validação específica em mosaicos Planet. O detector pode perder alvos pequenos ou apresentar viés de imagens ao nível do solo.

### P58 — YOLOSAM: A YOLO-Guided SAM for Accurate Building Segmentation in Remote Sensing Images

- **Referência:** Hussain, M. et al. *IEEE JSTARS*, 19, 4403–4417, 2026; DOI/publicação online de 2025.
- **Fonte:** https://doi.org/10.1109/JSTARS.2025.3649081
- **Método:** gerador de prompts de caixas baseado em YOLOv8, combinado a adaptações de SAM para segmentação de edificações; avalia WHU, Vaihingen e Inria.
- **Aplicação:** exemplo direto da catalogação prévia sugerida: detector localiza, segmentador delimita.
- **Limite:** não assumir que as resoluções dos benchmarks equivalem a 3–5 m. Um detector que omite um edifício também pode impedir que SAM o segmente.

### P59 — Toward unsupervised building extraction from very high-resolution remote sensing images using SAM and CLIP

- **Referência:** 2025. *GIScience & Remote Sensing*.
- **Fonte:** https://doi.org/10.1080/15481603.2025.2543102
- **Método:** SAM segmenta objetos; modelo visão-linguagem ajuda a separar edifício/não edifício e construir pseudorrótulos; uma etapa posterior aprende o extrator.
- **Aplicação:** referência muito próxima da ideia de criar previamente um catálogo de objetos para treinamento.
- **Limite:** supervisão automática continua sujeita a erros sistemáticos. Não avaliar o resultado apenas contra os próprios pseudorrótulos. Síntese baseada no registro editorial indexado.

### P60 — SAMPolyBuild: Adapting the Segment Anything Model for polygonal building extraction

- **Referência:** Wang, C. et al., 2024. *ISPRS Journal of Photogrammetry and Remote Sensing*, 218, 707–720.
- **Fonte:** https://www.sciencedirect.com/science/article/pii/S0924271624003563
- **Código dos autores:** https://github.com/wchh-2000/SAMPolyBuild
- **Método:** adapta SAM à extração de polígonos de edificações.
- **Aplicação:** aproxima a saída do modelo de objetos GIS utilizáveis no catálogo.
- **Limite:** um polígono regular não prova contorno correto. Em Planet de 5 m, a qualidade geométrica precisa ser reportada por tamanho de objeto e referência independente.

### P61 — Remote Sensing Extraction of Damaged Buildings in the Shigatse Earthquake, 2025: A Hybrid YOLO-E and SAM2 Approach

- **Referência:** 2025. Artigo aplicado.
- **Fonte:** https://pubmed.ncbi.nlm.nih.gov/40732502/ — https://pmc.ncbi.nlm.nih.gov/articles/PMC12299807/
- **Método/dados:** YOLO-E e SAM2 em imagens de aproximadamente 0,15–0,80 m para edificações danificadas.
- **Aplicação:** demonstra integração detector–segmentador em sensoriamento remoto.
- **Limite:** dano de construção e resolução submétrica são diferentes de surgimento de construções em 3–5 m. Não reutilizar desempenho como expectativa para seus mosaicos.

### P62 — SAM 3: Segment Anything with Concepts

- **Referência:** Carion, N. et al., 2025. Preprint/artigo dos autores consultado.
- **Fonte:** https://arxiv.org/abs/2511.16719
- **Método:** detecção, segmentação e rastreamento com prompts conceituais textuais ou exemplos visuais.
- **Aplicação:** candidato recente para catalogação orientada por conceitos e seleção assistida de objetos.
- **Limite:** rastreamento em vídeo não equivale à associação de objetos entre mosaicos mensais com mudanças radiométricas e grandes intervalos. A transferência exige avaliação própria.

### P63 — Promptable Concept Segmentation from Above: Evaluating SAM 3’s Zero-Shot and One-Shot Capabilities in Remote Sensing

- **Referência:** Dabaja, M.; Celik, T., julho de 2026. Preprint.
- **Fonte:** https://arxiv.org/html/2607.09583v1
- **Método:** avaliação de SAM 3 em classificação de cenas, detecção e segmentação de instâncias no domínio remoto.
- **Aplicação:** ajuda a avaliar objetivamente quando texto ou exemplo visual são úteis para pré-catalogar.
- **Limite:** os autores relatam dificuldades de transferência e interferência entre modalidades de prompt. É evidência contra presumir confiabilidade zero-shot universal, não uma validação Planet local.

### P64 — DINOv3

- **Referência:** 2025. Artigo dos autores sobre aprendizado autossupervisionado.
- **Fonte:** https://arxiv.org/abs/2508.10104
- **Modelo satelital oficial:** https://huggingface.co/facebook/dinov3-vit7b16-pretrain-sat493m
- **Método:** extração de representações densas; inclui treinamento e avaliação em dados geoespaciais.
- **Aplicação proposta:** embeddings de patches/objetos para busca por similaridade, agrupamento, seleção de amostras e classificadores supervisionados.
- **Limite:** embedding não é classe; agrupamentos não são uma taxonomia validada. O checkpoint indicado é grande, e não uma indicação automática de melhor custo-benefício.

### P65 — DINO Soars: DINOv3 for Open-Vocabulary Semantic Segmentation of Remote Sensing Imagery

- **Referência:** Faulkenberry, R.; Prasad, S., maio de 2026. Preprint.
- **Fonte:** https://arxiv.org/abs/2605.03175
- **Código:** https://github.com/rfaulk/DINO_Soars
- **Método:** CAFe-DINO, agregação e aumento de resolução de similaridades texto–imagem para segmentação aberta.
- **Aplicação:** candidato de pré-classificação de cenas e cobertura.
- **Limite:** ausência de fine-tuning em imagens remotas não significa ausência total de treinamento; o resumo descreve ajuste em subconjunto de COCO-Stuff. Ainda requer teste em Planet.

### P66 — AlphaEarth Foundations: An embedding field model for accurate and efficient global mapping from sparse label data

- **Referência:** Brown, C. F. et al., 2025. Preprint/relatório dos autores.
- **Fonte:** https://arxiv.org/abs/2507.22291
- **Documentação do lançamento:** https://deepmind.google/blog/alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail/
- **Método:** representações geoespaciais multifuente e lançamento de embeddings anuais.
- **Aplicação:** contexto e classificação auxiliar quando há poucos rótulos.
- **Limite:** um produto anual não informa diretamente o mês da mudança. Não tratar os embeddings disponibilizados como um encoder público pronto para processar qualquer raster Planet local; são coisas diferentes.

### P67 — Neural Plasticity-Inspired Multimodal Foundation Model for Earth Observation

- **Referência:** Xiong, Z. et al., 2024. Versão consultada no arXiv — DOFA.
- **Fonte:** https://arxiv.org/abs/2403.15356
- **Método:** modelo multimodal condicionado por comprimentos de onda, com diferentes sensores.
- **Aplicação:** alternativa para investigar entrada multiespectral heterogênea.
- **Limite:** flexibilidade de bandas não elimina necessidade de reflectância consistente, normalização, ajuste e avaliação local. Não é solução automática para misturar produtos visuais e analíticos.

## 17. Engenharia de dados: transformar arquivos em acervo analítico

A referência de engenharia de dados não precisa conter o nome de uma rede neural. O problema científico depende de grade espacial, tempo, qualidade e rastreabilidade corretos. Sem essas propriedades, um modelo pode aprender diferenças de produto e processamento como se fossem mudanças no terreno.

### P68 — Earth Observation Data Cubes for Brazil: Requirements, Methodology and Products

- **Referência:** Ferreira, K. R. et al., 2020. *Remote Sensing*, 12(24), 4033 — INPE/Brazil Data Cube.
- **Fonte:** https://doi.org/10.3390/rs12244033
- **Página do projeto:** https://data.inpe.br/bdc/earth-observation-data-cubes-for-brazil-requirements-methodology-and-products/
- **Contribuição:** requisitos, dados prontos para análise, cubos multidimensionais, infraestrutura e serviços.
- **Aplicação:** principal referência brasileira para estruturar seu acervo espaço-temporal.
- **Limite:** os produtos originais não são Planet; aproveitar princípios de arquitetura, sem presumir parâmetros ou custos equivalentes.

### P69 — Building Earth Observation Data Cubes on AWS

- **Referência:** Ferreira, K. R.; Queiroz, G. R.; Marujo, R. F. B.; Costa, R. W., 2022. *ISPRS Archives*.
- **Fonte:** https://doi.org/10.5194/isprs-archives-XLIII-B3-2022-597-2022
- **Contribuição:** construção de cubos de observação da Terra com arquitetura serverless e imagens em armazenamento de objetos.
- **Aplicação:** execução por tarefas, paralelismo e processamento de grandes coleções.
- **Limite:** referência arquitetural, não recomendação obrigatória de AWS. A escolha entre local, nuvem e processamento distribuído depende do volume e recursos reais.

### P70 — Satellite Image Time Series Analysis for Big Earth Observation Data

- **Referência:** Simoes, R.; Camara, G.; Queiroz, G.; Souza, F.; Andrade, P. R.; Santos, L.; Carvalho, A.; Ferreira, K., 2021. *Remote Sensing*, 13(13), 2428.
- **Fonte:** https://doi.org/10.3390/rs13132428
- **Contribuição:** pacote `sits`, integrando cubos temporais e classificação por ML/DL.
- **Aplicação:** referência de fluxo completo entre dados e classificação de séries, e não apenas escolha de modelo.
- **Limite:** implementação de referência em R. É possível adotar os princípios em Python, mas isso constitui implementação distinta a verificar.

### P71 — On-Demand Processing of Data Cubes from Satellite Image Collections with the gdalcubes Library

- **Referência:** Appel, M.; Pebesma, E., 2019. *Data*, 4(3), 92.
- **Fonte:** https://doi.org/10.3390/data4030092
- **Contribuição:** processamento sob demanda de coleções como cubos, com definição explícita da grade e tempo.
- **Aplicação:** evitar materializar combinações completas quando apenas recortes e operações específicas são necessários.
- **Limite:** computação sob demanda muda o perfil de I/O e repetição de operações; medir desempenho em vez de pressupor economia.

### P72 — The openEO API–Harmonising the Use of Earth Observation Cloud Services Using Virtual Data Cube Functionalities

- **Referência:** Schramm, M. et al., 2021. *Remote Sensing*.
- **Fonte institucional:** https://publications.jrc.ec.europa.eu/repository/handle/JRC122714
- **Contribuição:** interface comum para processamento de dados de observação da Terra com funcionalidades de cubos virtuais.
- **Aplicação:** desacoplar especificação analítica e infraestrutura de execução.
- **Limite:** suporte efetivo depende do backend e das operações implementadas; interoperabilidade não garante igualdade numérica entre ambientes.

### P73 — Incremental Data Cube Architecture for Sentinel-2 Time Series: Multi-Cube Approaches to Dynamic Baseline Construction

- **Referência:** 2026. *Remote Sensing*, 18(2), 260.
- **Fonte:** https://doi.org/10.3390/rs18020260
- **Contribuição:** arquitetura incremental para séries Sentinel-2 e atualização de referências temporais.
- **Aplicação:** incorporar o próximo mês sem recomputar indiscriminadamente toda a série 2020–2026.
- **Limite:** algoritmo retrospectivo pode exigir reprocessar uma janela maior; definir explicitamente quais produtos são invalidados quando um mosaico histórico é corrigido.

### P74 — A spatiotemporal cube model for analyzing satellite image time series: Application to land-cover mapping and change detection

- **Referência:** 2019. *Remote Sensing of Environment*.
- **Fonte:** https://www.sciencedirect.com/science/article/abs/pii/S0034425719302251
- **Contribuição:** modelagem espaço-temporal para análise de séries, cobertura e mudança.
- **Aplicação:** fundamenta a organização conjunta de espaço, tempo e atributos.
- **Limite:** um cubo físico ou virtual não garante homogeneidade semântica dos produtos que contém; manter metadados de origem e qualidade.

## 18. Ciência de dados: amostragem, curadoria, qualidade e representação

### P75 — Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure

- **Referência:** Roberts, D. R. et al., 2017. *Ecography*.
- **Fonte:** https://doi.org/10.1111/ecog.02881
- **Contribuição:** validação que respeita dependências entre observações.
- **Aplicação:** separar bairros/blocos e períodos, evitando a falsa independência de pixels e patches próximos.
- **Limite:** estudo metodológico geral; o tamanho do bloco e o teste temporal devem refletir a aplicação. Não há uma distância de separação universal.

### P76 — Efficient Self-Supervised Learning for Earth Observation via Dynamic Dataset Curation

- **Referência:** Kerdreux, T.; Tuel, A.; Febvre, Q.; Mouche, A.; Chapron, B., 2025. Versão arXiv consultada.
- **Fonte:** https://arxiv.org/html/2504.06962v1
- **Contribuição:** seleção dinâmica para reduzir redundância e melhorar diversidade no pré-treinamento.
- **Aplicação:** inspira seleção de amostras informativas em vez de treinar com todos os patches repetidos de meses estáveis.
- **Limite:** experimentos em Sentinel-1 Wave Mode, predominantemente oceânico. É referência de curadoria, não evidência direta em cobertura terrestre Planet.

### P77 — Deep learning for multi-modal classification of cloud, shadow and land cover scenes in PlanetScope and Sentinel-2 imagery

- **Referência:** 2019. *ISPRS Journal of Photogrammetry and Remote Sensing*.
- **Fonte:** https://www.sciencedirect.com/science/article/pii/S0924271619302023
- **Método:** classificação de nuvens, sombras e cenas, incluindo avaliação de generalização e aplicação a séries densas.
- **Aplicação:** uma camada explícita de qualidade antes de detectar mudanças.
- **Limite:** nuvem/sombra não são as únicas anomalias: registro geométrico, emendas e diferenças radiométricas também precisam de controle.

### P78 — Comparing Active Learning for Satellite Imagery: Contrastive Learning, Diversity, Confidence Sampling, and Cold Start Strategies

- **Referência:** Pogorzelski, D.; Arlinghaus, P. P.; Zhang, W., 2025. *IEEE JSTARS*, 18, 20678–20689.
- **Fonte:** https://doi.org/10.1109/JSTARS.2025.3597196
- **Contribuição:** comparação de estratégias de seleção de amostras para aprendizado ativo.
- **Aplicação:** priorizar revisão humana por diversidade, incerteza e representatividade, comparando com seleção aleatória.
- **Limite:** não usar apenas baixa confiança: amostras raras que o modelo classifica incorretamente com alta confiança também precisam de auditoria.

### P79 — Scale-MAE: A Scale-Aware Masked Autoencoder for Multiscale Geospatial Representation Learning

- **Referência:** Reed, C. J. et al. Versão arXiv inicial de 2022.
- **Fonte:** https://arxiv.org/abs/2212.14532
- **Contribuição:** pré-treinamento com representação explícita de escala geográfica e reconstrução multiescala.
- **Aplicação:** estudar representações quando o acervo mistura resoluções e tamanhos físicos de objetos.
- **Limite:** tratar escalas não recupera detalhes ausentes. Super-resolução e aumento de resolução de features não criam evidência de um telhado que não foi resolvido pelo sensor.

### P80 — BuildingSAM: A Dual-Branch Feature-Augmented Segment Anything Model for Remote Sensing Building Extraction

- **Referência:** 2025. *IEEE Geoscience and Remote Sensing Letters*.
- **Fonte:** https://doi.org/10.1109/LGRS.2025.3568386
- **Método:** adaptação de SAM voltada à extração de edificações.
- **Aplicação:** candidato especializado para comparar com SAM genérico e YOLO-seg.
- **Limite:** inclusão pelo registro editorial; arquitetura, custo de anotação, pesos e compatibilidade Planet devem ser verificados integralmente antes de implementar.

## 19. Arquitetura revisada: acervo → catálogo preliminar → eventos de mudança

### 19.1 O papel de cada tecnologia

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

### 19.2 Dois catálogos diferentes

**Catálogo técnico de imagens:** registra arquivos, footprints, CRS, tamanho de pixel, bandas, datas de composição, produto, máscaras, checksum e relação entre originais e derivados. STAC é apropriado para organizar a descoberta desses assets; não reconhece construções nem vegetação.

**Catálogo semântico de observações:** registra máscara/polígono, mês/intervalo, classe sugerida, atributos, modelo, prompt, confiança e revisão. Um registro observado em um mês não deve receber automaticamente a mesma identidade de um registro no mês seguinte.

Documentação oficial de STAC: https://www.ogc.org/standards/stac/ e https://stacspec.org/. São especificações técnicas, não artigos adicionais ao total de 80.

### 19.3 Estrutura de dados proposta

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

### 19.4 Engenharia de atributos para XGBoost/LightGBM

- Bandas e índices compatíveis com o produto; NIR apenas quando realmente disponível.
- Estatísticas por segmento: média, dispersão, quantis e proporção de pixels inválidos.
- Texturas em janelas definidas em metros; manter escala física comparável.
- Geometria: área, perímetro, alongamento e compactação, reconhecendo que dependem da qualidade da segmentação.
- Contexto: vizinhança e distâncias a elementos cartográficos disponíveis à época analisada.
- Tempo: diferença para a observação anterior válida, variação sazonal, persistência e tendência.
- Embeddings: representações de patches/objetos, registrando modelo, checkpoint, resolução e normalização.

Testar grupos de atributos por ablação. Ajustar seletores, normalizadores e hiperparâmetros apenas no treino; não selecionar features olhando o teste. Se mapas atuais forem usados para explicar eventos antigos, marcar o experimento como retrospectivo e controlar vazamento de informação futura.

### 19.5 Como testar se a pré-catalogação realmente economiza trabalho

Comparar três condições na mesma amostra independente: anotação manual; pré-anotação SAM/YOLO com correção; pré-anotação sem correção, usada apenas como baseline de erro.

Medir tempo total, incluindo falsos positivos removidos e objetos omitidos acrescentados; qualidade das máscaras; acurácia das classes; cobertura de alvos pequenos; e desempenho do modelo final treinado com esses rótulos. Uma máscara visualmente convincente pode estar sistematicamente errada.

Para reduzir viés de confirmação, parte da avaliação deve começar diretamente da imagem sem mostrar a sugestão do modelo. Manter uma amostra probabilística independente para avaliação, separada do conjunto escolhido por active learning.

### 19.6 Ordem prática de implementação revisada

1. Inventariar os produtos e medir qualidade/registro; preservar os arquivos originais.
2. Criar amostra espacial e temporal representativa, com mudanças e áreas estáveis.
3. Treinar baseline XGBoost/LightGBM e baseline U-Net para cobertura.
4. Comparar pré-anotação por SAM, YOLO→SAM e um modelo semântico recente em um subconjunto; medir correção humana e omissões.
5. Aproveitar embeddings para busca de similares e seleção de amostras se houver ganho comprovado.
6. Construir catálogo semântico revisável e associação temporal, com incerteza e proveniência.
7. Comparar pós-classificação e modelos temporais em teste independente.
8. Automatizar atualização incremental só depois de estabilizar entradas, rótulos e critérios de avaliação.

**Ponto de decisão:** se o gargalo for falta de rótulos, priorizar pré-anotação e curadoria. Se for falso alerta, priorizar qualidade e consistência temporal. Se for volume de dados, priorizar acesso por blocos, processamento incremental e medição de I/O. Escolher o modelo apenas pela novidade não resolve esses três problemas.

### 19.7 Complemento do registro de busca

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

