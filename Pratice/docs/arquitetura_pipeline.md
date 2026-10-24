# Arquitetura do pipeline

Princípio: **a mesma cadeia serve para treinar, avaliar e inferir.** Na inferência, uma imagem nova entra pelo mesmo caminho dos dados de treino (mesma grade, mesma normalização, mesmo detector, mesmo pós-processamento, mesma calibração), e a saída são os vetores do delta.

## Fluxo

```text
 imagem nova ─┐
              ▼
 S0 ingestão e QC ─► S1 harmonização ─► S2 recortes ─► S3 detecção ─► S4 pós-processamento temporal
 (grade, alfa,        (alinha à grade,    (blocos 256,    (probabilidade   (persistência, rastreio,
  nuvem, sombra,       normaliza cor,      sobreposição)   por par ou por   fusão com 2º método,
  borda, hash)         máscaras)                           data)            limpeza morfológica)
                                                                                   │
                                                                                   ▼
 S8 pacote e relatório ◄─ S7 consolidado anual ◄─ S6 confiança calibrada ◄─ S5 vetorização e atributos
 (manifesto, mapas,       (funde eventos,          (componentes, calibração,   (polígonos, tipo, de→para,
  tabelas, auditoria)      comparação anual)        classes de confiança)       área, flags)
```

## Etapas, contratos e responsabilidades

| Etapa | Entrada | Saída | Regra principal |
|---|---|---|---|
| S0 ingestão e QC | GeoTIFF novo ou da série | registro no catálogo + relatório de QC | recusar imagem fora da grade, com CRS errado ou sem alfa; registrar hash; estimar nuvem, sombra, borda de mosaico |
| S1 harmonização | série e imagem nova | rasters alinhados e normalizados + máscara válida | uma grade por fonte; normalização de cor **ajustada só em áreas estáveis** (invariantes); nunca com a imagem de teste no ajuste |
| S2 recortes | rasters + máscara | recortes 256 × 256 com folga, índice de blocos | recortes só com pixel válido; blocos do índice espacial definem a divisão treino/validação/teste |
| S3 detecção | recortes de um par (ou de uma série) | mapa de probabilidade de mudança (e de classe de→para) | o detector é plugável: baseline, U-Net bitemporal, por data + diferença, série |
| S4 pós-processamento | mapas de probabilidade de vários meses | máscaras de mudança limpas, com identificação de evento | persistência em N observações, rastreio por sobreposição, remoção de manchas < `area_min_m2`, fusão com o segundo método |
| S5 vetorização | máscaras de evento | polígonos com atributos de especificação | geometria simples e válida; tipo e de→para por regra sobre os mapas de classe |
| S6 confiança | polígonos + componentes | `confianca`, `classe_confianca` | calibrada em referência separada; `provisoria` até a confirmação |
| S7 consolidado | mudanças mensais do ano | `consolidado_AAAA.gpkg` | funde sem duplicar; compara com a diferença anual direta |
| S8 pacote | tudo | manifesto, mapas, tabelas, relatório | executar de novo produz os mesmos identificadores |

## Modos de execução

| Modo | O que roda | Para quê |
|---|---|---|
| `treino` | S0 → S3 com referência; salva modelo e divisão | produzir o modelo |
| `avaliacao` | S0 → S6 em blocos e meses não vistos + controles estáveis | comparar métodos (skill `avaliacao-comparacao`) |
| `serie` | S0 → S8 sobre toda a série | gerar os deltas mensais e os consolidados anuais históricos |
| `incremental` | S0 → S6 só do mês novo; reclassifica os 3 meses anteriores; S7 do ano corrente | operação: baixar uma imagem nova e obter o delta (skill `inferencia-nova-imagem`) |

## Estrutura de código sugerida (`src/mudanca/`)

```text
src/mudanca/
  io/          leitura da série, catálogo, escrita de GeoPackage
  qc/          alfa, nuvem, sombra, borda, estabilidade radiométrica
  harmonizacao/ alinhamento, normalização, máscaras
  rotulos/     referência de eventos, divisão por blocos, aprendizado ativo
  recortes/    índice de blocos, recortes, aumento de dados
  detectores/  baseline_diferenca, baseline_hue, unet_bitemporal, unet_por_data, serie_utae
  posproc/     persistência, rastreio, morfologia
  vetores/     vetorização, atributos, consolidação
  confianca/   componentes, calibração, classes
  avaliacao/   métricas por pixel e por evento, controles estáveis, tabelas
  cli.py       comandos: qc, treinar, avaliar, serie, incremental
configs/       pipeline.yaml, classes.yaml, esquema_vetor.yaml
runs/          saídas por execução (fora do git)
tests/         testes com mini-recortes sintéticos
```

## Decisões de projeto (justificadas e revisáveis)

1. **Detector plugável com interface única:** `prever(par_ou_serie) -> {prob_mudanca, prob_classes}`. Isso permite comparar métodos sem mudar o resto. Evidência de que o pós-processamento e os dados pesam mais que a arquitetura: SpaceNet 7 (Etten 2021) e TEMPO (Glazer 2025).
2. **Vetores sempre por regra determinística** a partir dos mapas; nenhuma etapa gera polígonos "à mão".
3. **Delta mensal e consolidado são dois produtos ligados por `id_evento`**; o anual não é só a união dos mensais, é confirmado também por comparação anual direta.
4. **Latência explícita:** a saída mensal é emitida logo, como `provisoria`, e é confirmada com os 3 meses seguintes (como em Zhang 2023); o sistema mede e reporta essa troca entre latência e precisão.
5. **Normalização radiométrica ajustada só em áreas estáveis** e validada em controles estáveis; o produto visual da Planet não tem reflectância.
6. **Divisão por blocos espaciais com folga e por período**, nunca por pixel ou recorte aleatório (lacuna L13).
7. **Ambiente isolado** (`venv` ou `conda`), dependências fixadas em `requirements.txt` com versões; PyTorch com CUDA compatível com a GTX 1650.

## Dependências previstas

`rasterio`, `geopandas`, `shapely`, `pyproj`, `numpy`, `scipy`, `scikit-image`, `scikit-learn`, `pyyaml`, `pandas`; treino: `torch` (CUDA), `segmentation-models-pytorch`, `albumentations`; opcionais: `torchgeo`, `open-cd`, `opencv-python`, `matplotlib`. Já presentes na máquina: `rasterio` 1.5.2 e `geopandas`.
