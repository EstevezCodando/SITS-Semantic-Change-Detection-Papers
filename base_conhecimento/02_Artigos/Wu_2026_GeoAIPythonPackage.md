---
tipo: artigo
id_origem: P155
titulo: "GeoAI: A Python package for integrating artificial intelligence with geospatial data analysis and visualization"
ano: 2026
autores: ["Qiusheng Wu"]
doi: "10.21105/joss.09605"
arquivo_fonte: "coleta/P155_Wu2026_GeoAI-A-Python-package-for-integrating-artificial-intelligen.pdf"
markdown_fonte: "output/pdf/P155_Wu2026_GeoAI-A-Python-package-for-integrating-artificial-intelligen/document.md"
paginas: 3
tipo_documento: "artigo curto (≤4 páginas; verificar)"
status_leitura: "lido (profundo)"
tarefas: []
sensores: []
conjuntos_dados: []
metodos: []
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/profunda]
---

# Wu 2026 — GeoAI: A Python package for integrating artificial intelligence with geospatial data analysis and visualization

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (profundo). Fichas de leitura profunda usadas como evidência.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Qiusheng Wu (2026). GeoAI: A Python package for integrating artificial intelligence with geospatial data analysis and visualization. The Journal of Open Source Software. Tipo no catálogo: Software.
- **DOI/URL:** https://doi.org/10.21105/joss.09605
- **Arquivo de origem:** `coleta/P155_Wu2026_GeoAI-A-Python-package-for-integrating-artificial-intelligen.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P155_Wu2026_GeoAI-A-Python-package-for-integrating-artificial-intelligen/document.md` — 3 páginas, 3 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo curto (≤4 páginas; verificar).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Apresentar o **GeoAI**, um pacote Python que unifica busca de dados, preparo de datasets, treino, inferência e visualização de modelos de IA sobre dados geoespaciais, mais um **plugin para QGIS** que expõe parte desses fluxos em painéis, sem código. O artigo JOSS (Wu, 2026) é curto: descreve as capacidades e a necessidade, não traz avaliação quantitativa.

**Evidência (leitura):**

- Seis capacidades: (1) busca e download interativos ou programáticos de imagens; (2) preparo automático de datasets com chips e rótulos; (3) treino para classificação, detecção e segmentação; (4) pipelines de inferência; (5) visualização com Leafmap e MapLibre; (6) **integração com o QGIS por um plugin dedicado** (p. 1).
- Construído sobre PyTorch, Transformers, `segmentation_models.pytorch` e a biblioteca `torchange` (mudança), com formatos GeoTIFF, JPEG2000, GeoJSON, Shapefile e GeoPackage e gestão automática de GPU (p. 1).
- Posicionamento: lacuna entre bibliotecas de base (TorchGeo, TerraTorch, SRAI) e uma **interface de alto nível**; exemplos citados: extração de pegadas de edificações, classificação de cobertura e **detecção de mudanças** "com poucas linhas de código" (p. 2).
- Licença CC BY 4.0 do artigo; publicado em 3/fev/2026 (JOSS 11(118):9605) (p. 1).


## 3. Área de estudo e período analisado

Ver seção 4 (dados), que traz área e período quando informados pelo artigo.

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo



## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem



## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — O que a documentação e o repositório acrescentam:**

- **Plugin QGIS** (QGIS ≥ 3.28, Windows/Linux/macOS, roda em CPU se não houver GPU). Na primeira execução um painel detecta a GPU, cria um ambiente virtual em `~/.qgis_geoai/` e instala os pacotes com um clique.
- Painéis do plugin: segmentação de árvores (DeepForest), segmentação de água (OmniWaterMask), Moondream (legenda, perguntas e detecção por linguagem), **Segment Anything via SamGeo (SAM1, SAM2, SAM3; prompts de texto, ponto e caixa; lote; regularização de polígonos)**, **segmentação semântica** (criar tiles de treino a partir de raster e vetor, treinar U-Net, DeepLabV3+, FPN etc. e inferir com vetorização), **segmentação de instâncias** (Mask R-CNN) e utilitários.
- Entradas: camadas raster/arquivos e vetores de rótulo; saídas: GeoTIFF e GeoPackage/Shapefile/GeoJSON; exporta tiles de treino em PASCAL_VOC, COCO e YOLO (detecção de árvores).
- O repositório (MIT; ~3,4 mil estrelas) lista "mudança" como extração de feições "AI-enhanced" com classificação multitemporal, e um catálogo de 20 modelos fundacionais (`geoai.list_foundation_models()`).
- Fontes de dados nomeadas: Sentinel, Landsat, NAIP e Overture Maps; **Planet não é citado**.
- Pacote no PyPI: `geoai-py` 0.43.1, MIT, **Python ≥ 3.12** (checagem de 24/10/2026), enquanto a documentação do plugin cita Python 3.10+.

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos



## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — Lacunas e cuidados (verificados):**

- **O plugin não tem painel de detecção de mudanças nem de séries temporais**; a mudança está só no pacote Python (via `torchange` e exemplos), não no QGIS.
- Sem avaliação quantitativa, benchmark ou comparação com outras ferramentas no artigo; é um artigo de software.
- SAM3 exige GPU NVIDIA com CUDA e aprovação no Hugging Face; o QGIS 3.42.2 tem bug no Windows ao salvar `.qgz` (a documentação fixa o QGIS 3.44 no ambiente Pixi); possíveis erros de memória CUDA em modelos grandes.
- Contagem de citações: o OpenAlex mostrava só 4 trabalhos citando o artigo em 24/10/2026 (ver README), por ser recente.


## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/openjournals/joss-reviews/issues/9605 (p. 1)
- URL citada: https://github.com/openjournals/joss-reviews/issues/9605 (p. 1)
- URL citada: https://github.com/opengeos/geoai (p. 1)
- URL citada: https://github.com/RaczeQ (p. 1)
- URL citada: https://github.com/jbousquin (p. 1)
- declaração: “Journal of Open Source 1 Software, 11 [(118), 9605. https://doi.org/10.21105/joss.09605.](https://doi.org/10.21105/joss.09605)” (p. 1)
- declaração: “80NSSC22K1742, awarded under the Open Source Tools, Frameworks, and Libraries Program.” (p. 2)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** ferramenta (sem avaliação). Pacote e plugin; sem avaliação quantitativa de operação.
- menções de termos de monitoramento (contagem, não avaliação): Rastreabilidade 2 (p. 2)

**Interpretação — O que reaproveitar:**

- **Revisão e pré-anotação em QGIS sem código:** SamGeo (pontos/caixas/texto) para pré-segmentar objetos e **Semantic Segmentation** para treinar uma U-Net a partir de raster + vetor dentro do QGIS, o que cobre a rotulagem e o baseline EXP2 U-Net mensal + persistência com a equipe que usa QGIS.
- **Exportação de tiles de treino** (PASCAL_VOC/COCO/YOLO) como ponte para outros frameworks.
- **Ambiente isolado automático** (`~/.qgis_geoai`) como modelo para reproduzir o ambiente do plugin em outras máquinas.
- **Catálogo de modelos fundacionais** (`list_foundation_models`) para escolher backbones do EXP5/EXP6.
- Para mudança temporal, usar o **pacote Python** (com `torchange`) e não o plugin.

**Interpretação — Como entra no nosso pipeline:**

- E04 Rotulagem e pré-anotação: pré-anotar com SamGeo e corrigir em QGIS.
- E06 Modelos-base de cobertura: treino de segmentação via painel ou API.
- E11 Operação e atualização: revisão humana dos eventos em QGIS, com camadas vetoriais versionadas.
- Teste proposto: repetir o EXP6 usando o plugin e medir o tempo por evento confirmado.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- referencia (suporte manual da leitura): [[PreAnotacaoSAM|Pré-anotação assistida (SAM e plugins QGIS)]] — suporte vindo da leitura/título/resumo

**Comparações substantivas com outros artigos:**
- este artigo integra a mesma família de ferramentas de [[Wang_2025_SAMTestingReliability|Wang 2025]] — O plugin GeoAI inclui SamGeo (SAM); MO-SAM usa o SAM fora do plugin, com capturas de tela.

## Anotações do leitor

- 
