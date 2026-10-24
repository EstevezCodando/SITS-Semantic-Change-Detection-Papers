# Pratice — detecção automática de mudanças de cobertura com Planet de ~5 m

Contexto permanente para trabalhar nesta pasta. Leia antes de qualquer tarefa; os detalhes estão em `docs/` e os procedimentos em `.claude/skills/`.

## Objetivo

Construir um **pipeline** que, dada uma nova imagem óptica Planet de ~5 m, identifique automaticamente **o delta de alterações da cobertura do solo** em relação às imagens anteriores, com foco em:

- **início de construções** e edificações novas;
- **supressão da vegetação** (arbórea e rasteira);
- **abertura e ampliação de vias**;
- solo exposto, movimentação de terra e outras transições.

Etapas do trabalho: **testar os melhores métodos, analisar os resultados e compará-los**; depois empacotar o melhor em um fluxo repetível (modelo treinado + baixar nova imagem → delta).

## Saída obrigatória: vetores

Cada alteração detectada vira um **polígono vetorial** com atributos de especificação (tipo, classe de→para, área, datas) e de **confiabilidade**. Há dois níveis:

1. **delta mensal**: um conjunto de vetores para cada par de meses consecutivos;
2. **consolidado anual**: um conjunto por ano, que funde os eventos mensais (sem duplicar) e os confirma.

Esquema completo: `docs/esquema_vetores.md` e `configs/esquema_vetor.yaml`.

## Dados disponíveis (somente leitura, fora do repositório)

`D:\PT2-build\Imagens de Satelite` — baixado e organizado por outra pipeline. **Não copiar, não alterar.** Resumo (detalhes em `docs/dados.md`):

| Fonte | Pasta | Série | Grade |
|---|---|---|---|
| Planet basemaps `global_monthly` | `data/planet_basemaps/global_monthly/` | 81 meses, 2020-01 a 2026-09 | 4,5 m, 725 × 659 px |
| Planet basemaps `medres_normalized` | `data/planet_basemaps/medres_normalized/` | 74 mosaicos, 2020-06 a 2026-09 | 4,5 m, 725 × 659 px |
| Planet `sentinel2_8b` | `data/planet_basemaps/sentinel2_8b/` | só 2026-08 e 2026-09 | 4,5 m |
| Mosaico PSScene | `data/planet_psscene/mosaico_2026-10-23/` | 1 data (2026-10-09) | 3 m, 1087 × 988 px |
| CBERS-4A WPM fundida | `CBERS/wpm_fused_2m/` | 21 datas, 2023-04 a 2026-10 | 2 m, 1631 × 1482 px |

- **AOI:** `Jardim_Interlagos.geojson` (Maricá/RJ, península entre lagoas; ~3 × 3 km). Máscara da AOI em `mascara_aoi*.tif`.
- **CRS comum:** EPSG:32723 (SIRGAS/WGS 84 UTM 23S). Todas as datas de uma fonte compartilham a mesma grade e extensão.
- **Formato dos rasters:** GeoTIFF `uint8` de **4 bandas = RGB + alfa** (o alfa marca ausência de dado). São produtos **visuais de 8 bits**: **não há banda NIR, não há máscara UDM, não há reflectância**. Logo não existe NDVI; use índices de cor (por exemplo, Hue) e textura.
- O PNG ao lado de cada GeoTIFF é só visualização, com a data escrita na faixa inferior; **nunca use o PNG como entrada do modelo**.
- Catálogo navegável: `catalogo.html`; tabela: `data/catalogo/mosaicos.csv`.

## Restrições que moldam as decisões

1. **Uma só AOI pequena (~3 × 3 km).** Generalizar para outras áreas não foi demonstrado; avalie sempre por blocos espaciais e por período, e planeje adicionar AOIs.
2. **Não há rótulos ainda.** O primeiro trabalho é construir a referência (skill `rotulagem-referencia`).
3. **Só RGB de 8 bits.** Os mosaicos mensais "visuais" têm balanço de cor próprio e a Planet mudou o processamento em 2022 (nitidez e super-resolução), o que cria deslocamento de distribuição entre meses (`docs/dados.md`). Trate a inconsistência radiométrica como causa principal de falso positivo.
4. **Objetos pequenos.** Uma edificação tem ~4–5 px em 4,5 m; uma via estreita, 1–2 px. O melhor escore de mudança de edificação publicado em Planet de ~4 m é baixo (0,20 no SpaceNet 7). Defina a menor área detectável por validação local.
5. **GPU limitada:** NVIDIA GTX 1650 (4 GB). Treine modelos pequenos (U-Net com ResNet18/34, recortes de 256, precisão mista). Modelos fundacionais grandes exigem nuvem. Ainda **não há PyTorch instalado** (`rasterio` e `geopandas` estão disponíveis; `GDAL` Python, não).
6. **Chave da API Planet:** existe um `.env` na pasta de imagens. **Nunca ler, exibir, copiar ou versionar esse arquivo.** O pipeline lê a chave só da variável de ambiente `PL_API_KEY`.

## Conhecimento acumulado

A base `..\base_conhecimento\` (vault Obsidian) e as fichas `..\dados\leitura_profunda\` reúnem 41 artigos lidos. Comece por `..\base_conhecimento\01_Mapas\Trilha_Objetivo_Planet5m.md` (fluxo, resultados e lacunas) e use a skill `consulta-conhecimento`. Regras ao citar:

- Os valores são os **relatados por cada estudo**; **não compare entre bases diferentes** (L06).
- Toda afirmação sobre um artigo leva página (p. N) ou seção, como nas notas.
- Separe **evidência** (do artigo) de **interpretação** (nossa).

Resumo do que a literatura sustenta para este projeto:

- Supressão de vegetação em NICFI mensal de 5 m funciona sem rótulos de treino com índice Hue referenciado à vizinhança e **persistência de ≥ 3 meses**; o custo é latência e omissão pouco conhecida (Zhang 2023).
- U-Net por data + diferença de mapas é o padrão para cobertura arbórea (Wagner 2023, Carter 2024); U-Net bitemporal confirma candidatos (Wang 2024, mas com divisão aleatória).
- **Pós-processamento temporal pesa mais que a arquitetura** em construção (colapso temporal no SpaceNet 7; janela de 4 datas no TEMPO).
- Aprendizado ativo por entropia dá o maior ganho de rótulo (F1 43% → 84% em dois ciclos, Masolele 2024).
- Divisão aleatória ou por pixel infla métricas (lacuna L13); a referência visual tem discordância (32% em Zhang 2023, L14).

## Convenções de trabalho

- **Regra do usuário (global):** todo arquivo alterado tem commit associado. Antes de editar, `git status`; commite o estado atual; ao fim, commite com mensagem descritiva. Este diretório está no repositório `ML-DPL-Changes`.
- **Idioma:** português do Brasil em documentos, mensagens de commit e nomes de atributos; código e identificadores em inglês ou português sem acento, de modo consistente com o resto do arquivo.
- **Reprodutibilidade:** todo experimento registra semente, divisão, versão dos dados, configuração e métricas (skill `registro-experimentos`). Nada de resultado sem rastro.
- **Nada de números inventados.** Se um valor não foi medido aqui, diga que não foi medido.
- **Dados e modelos grandes** (`runs/`, `models/`, `data/`, `*.pt`, `*.tif`) ficam fora do git (`.gitignore`).
- **Caminhos** vêm de `configs/pipeline.yaml`; nada de caminho absoluto dentro do código.
- **Comparação justa:** mesmo recorte, mesma divisão, mesma métrica, mesmo orçamento de ajuste de hiperparâmetros. Reporte blocos separados por tarefa e nunca ordene modelos medidos em bases diferentes.

## Mapa do projeto

```text
Pratice/
  CLAUDE.md                 este contexto
  README.md                 visão geral e primeiros passos
  configs/                  pipeline.yaml, classes.yaml, esquema_vetor.yaml
  docs/                     dados, arquitetura, esquema dos vetores, métodos, roteiro, conhecimento, banco da máscara
  db/                       mascara_cobertura.sql: banco PostGIS dos rótulos de cobertura (docs/banco_mascara.md)
  .claude/skills/           procedimentos reutilizáveis (um por etapa)
  src/  (a criar)           código do pipeline, por etapa
  runs/ (a criar, ignorado) saídas de cada execução e experimento
```

## Skills disponíveis

| Skill | Use para |
|---|---|
| `inventario-dados` | catalogar, validar grade, alinhamento, nodata e qualidade da série |
| `rotulagem-referencia` | construir a referência de mudança (eventos com mês de início), divisão por blocos |
| `baselines-mudanca` | métodos sem treino: diferença, Hue com persistência, pós-classificação |
| `treino-modelos` | preparar recortes, treinar U-Net bitemporal, por data e em série, com ambiente |
| `avaliacao-comparacao` | protocolo de avaliação e comparação de métodos, calibração, controles estáveis |
| `vetorizacao-confianca` | raster → polígonos, atributos, confiança, delta mensal e consolidado anual |
| `inferencia-nova-imagem` | rodar o pipeline treinado sobre uma imagem nova e gerar o delta |
| `registro-experimentos` | registrar e comparar execuções com rastreabilidade |
| `consulta-conhecimento` | achar evidência na base de conhecimento e citá-la corretamente |
