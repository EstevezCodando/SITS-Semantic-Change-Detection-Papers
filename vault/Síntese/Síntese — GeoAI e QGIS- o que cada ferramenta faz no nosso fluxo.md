---
tipo: sintese
etapas: ["[[E04 Rotulagem e pré-anotação|E04]]", "[[E05 Atributos e representações|E05]]", "[[E06 Modelos-base de cobertura|E06]]", "[[E11 Operação e atualização|E11]]"]
tags: [sintese]
---

# GeoAI e QGIS: o que cada ferramenta faz no nosso fluxo

Comparação das ferramentas lidas (fichas [[LP P155 Wu 2026]], [[LP P156 Aszkowski 2023]], [[LP P157 Tresson 2026]], [[LP P164 Wang 2024]], [[LP P165 Wang 2025]], [[LP P158 Febrita 2025]]).

| Ferramenta | O que faz | Entrada | Saída | CPU/GPU | Licença | Treina? | Mudança temporal? |
|---|---|---|---|---|---|---|---|
| **GeoAI (plugin + pacote)** | painéis de SamGeo (SAM1/2/3), segmentação semântica (treino e inferência), Mask R-CNN, DeepForest, água, VLM | raster + vetor de rótulos | GeoTIFF, GPKG/SHP/GeoJSON | CPU ou GPU (SAM3 exige CUDA) | MIT | **sim** (U-Net, DeepLabV3+, FPN…) | **não no plugin**; pacote Python usa `torchange` |
| **Deepness** | roda modelos ONNX de segmentação, detecção, regressão e super-resolução; exporta tiles de treino | qualquer raster | camadas do QGIS | CPU/GPU | (ver repositório) | não (só inferência) | não |
| **IAMAP** | características de modelos fundacionais (ViT), redução, agrupamento, similaridade, ML leve | raster | GeoTIFF de características, mapas | **CPU por desenho** | GPL-3.0 | só modelos sklearn | não |
| **Geo-SAM (plugin)** | segmentação interativa com SAM, codificação prévia | raster ou tiles XYZ/WMS | polígonos | CPU de notebook | MIT | não | não |
| **MO-SAM (método)** | SAM com prompts de pontos, fora do plugin | capturas RGB do QGIS | máscaras | — | — | não | não |

## O que isso significa para o projeto
- **Nenhuma** das ferramentas oferece **detecção de mudança temporal em QGIS**. Para o núcleo do projeto (transições mensais) é preciso o pipeline Python; o QGIS entra na **rotulagem, na revisão e na inspeção**.
- **Papéis possíveis:**
  - Pré-anotar: GeoAI/SamGeo e Geo-SAM (pontos, caixas, texto) → [[E04 Rotulagem e pré-anotação]].
  - Buscar exemplos e escolher amostras: IAMAP (similaridade, agrupamento sobre embeddings) → [[E04 Rotulagem e pré-anotação]], [[E05 Atributos e representações]].
  - Treinar baseline de cobertura: GeoAI Semantic Segmentation → [[E06 Modelos-base de cobertura]].
  - Revisar eventos e rodar um modelo exportado: Deepness (ONNX) e camadas versionadas → [[E11 Operação e atualização]].
- **Todas assumem RGB ou ortofoto submétrica.** O tratamento de **4 bandas (RGB+NIR)** e de **normalização 8 bits** não está documentado em IAMAP, Deepness e Geo-SAM e precisa ser testado com mosaicos Planet.

## Lições de uso (da evidência lida)
1. **Os parâmetros do plugin mudam o resultado tanto quanto o modelo:** resolução de processamento, sobreposição de tiles e remoção de segmentos pequenos levaram o F1 de 48 % a 79 % no Deepness ([[LP P158 Febrita 2025]]). Registrar sempre esses parâmetros no `processing_run`.
2. **Prompts de SAM:** 20–30 pontos funcionam melhor que 50; o contraste entre alvo e fundo prevê o sucesso; reportar o esquema de pontos ([[LP P165 Wang 2025]]).
3. **Selecionar a máscara sem consultar a anotação**, senão o resultado fica otimista ([[LP P165 Wang 2025]]).
4. **Codificar uma vez, clicar muitas** (Geo-SAM Pre-encoded) reduz o custo de rotular uma série mensal ([[LP P164 Wang 2024]]).
5. **Distribuição do ambiente:** GeoAI e IAMAP instalam dependências por conta própria; fixar versões (QGIS 3.44 no Pixi do GeoAI, bug do 3.42.2 no Windows).

## Riscos
- **Reprodutibilidade:** modelos do zoo do Deepness sem licença declarada; backbones baixados do Hugging Face (SAM3 exige aprovação).
- **GPL-3.0 no IAMAP** versus MIT nas demais: relevante se o código for incorporado a um produto.
- **Sem avaliação quantitativa nos artigos de software** (GeoAI, IAMAP): o ganho de tempo precisa ser medido por nós no EXP6.

## Teste sugerido (EXP6 ampliado)
Medir, em uma amostra de mosaicos Planet: tempo por objeto e mIoU com (a) rotulagem manual no QGIS, (b) SamGeo/GeoAI, (c) Geo-SAM pré-codificado, (d) IAMAP para escolher exemplos. Registrar os parâmetros de cada ferramenta e usar uma amostra de avaliação independente.
