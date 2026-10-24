---
tipo: sintese
etapas: ["[[E06 Modelos-base de cobertura|E06]]", "[[E07 Modelos de mudança em pares|E07]]", "[[E08 Modelos de série temporal|E08]]"]
tags: [sintese]
---

# Receitas de treino comparadas

Valores **lidos nos textos** (não extraídos automaticamente). Confirme no código antes de replicar.

| Artigo | Modelo | Entrada | Perda | Otimizador / lr | Batch | Épocas / iterações | Augmentation |
|---|---|---|---|---|---|---|---|
| [[P01 Wagner 2023]] | U-Net (34,6 M par.) | 256 × 256 × 4, 8 bits | BCE + Dice | Adam, 1e-4 | 256 | 20.000 épocas (melhor 17.058) | flips H/V |
| [[P10 Etten 2021]] | U-Net VGG16 / EfficientNet-B5 | imagem 1024², RGB | Jaccard + 4·BCE / Focal + Dice | Adam, 1e-4 / 2e-4 | — | 300 / 100 épocas | — |
| [[P13 Vincent 2024]] | U-TAE modificado | crops 128 × 128; 12 meses de 24 | focal | AdamW, aquecimento até 1e-4 em 5.000 it | — | 500.000 iterações | crop, flips, rotações |
| [[P18 Daudt 2019]] | FC-EF-Res / rede integrada | patches de pares RGB | entropia cruzada com pesos inversos à frequência | — | — | 3–5 h GTX 1080 Ti | — |
| [[P19 Yang 2021]] | ASN (+ ATL) | 512² pares | CE em 3 saídas (α = β = 1) | SGD, 0,005 poly 0,9, momentum 0,9, wd 1e-4 | 4 | 50 + 20 (ATL) | flip, escala 0,5–2 |
| [[P05 Zaraza-Aguilera 2022]] | U-Net/FPN (EffNet-B3) e U-Net modificada | 256 × 256 patches | DiceFocal / Focal-Tversky | Adam, lr 0,1 (declarado) | 16 | 45–100 épocas | rotação, flips |
| [[P07 Vizzari 2022]] | Random Forest (GEE) | pixels ou objetos SNIC + GLCM | — | — | — | — | — |

## Padrões
- **Perdas para classes raras:** Dice, Focal e combinações (P01, P05, P10, P13) em vez de CE simples.
- **Entradas 4 bandas (RGB+NIR) e normalização simples** bastam para Planet (P01, P05); adicionar NDVI não ajudou em P05.
- **Patches de 128–256 px** extraídos de imagens maiores; **inferência com borda espelhada** (P01).
- **Modelo escolhido pelo melhor checkpoint no conjunto de validação**, não pela última época (P01, P13).
- Séries: reduzir a redundância (semanal em vez de diária em P12; 12 de 24 meses em P13).

## Receita sugerida para o primeiro ciclo (hipótese)
- U-Net, 256² × 4 bandas, perda `BCE + Dice` ou `DiceFocal`, AdamW 1e-4 com aquecimento, flips e rotações, checkpoint por métrica de mudança de validação, inferência com sobreposição e borda espelhada.
- Baseline tabular (RF/XGBoost) com SNIC + GLCM como em [[P07 Vizzari 2022]].

Etapas: [[E06 Modelos-base de cobertura]], [[E07 Modelos de mudança em pares]], [[E08 Modelos de série temporal]]. Receitas extraídas automaticamente dos demais artigos: [[Receitas de treino]].
