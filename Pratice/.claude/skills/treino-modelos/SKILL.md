---
name: treino-modelos
description: Preparar o ambiente e treinar detectores de mudança (U-Net bitemporal, classificação por data, série temporal) em recortes de Planet RGB com GPU de 4 GB. Use ao criar o ambiente Python, montar recortes e amostragem, escolher perda e aumento de dados, treinar com sementes, ou pré-treinar em dados abertos.
---

# Treino de modelos de mudança

Detectores candidatos e hipóteses: `docs/metodos_e_experimentos.md` (M2 a M7). Todos seguem a interface do pipeline e a **mesma divisão por blocos** (`runs/referencia/divisao.json`).

**Estado do ambiente (2026-10-24):** `rasterio` 1.5.2 e `geopandas` presentes; **PyTorch não instalado**; GPU NVIDIA GTX 1650 de 4 GB. Os trechos de PyTorch abaixo são **modelos de partida ainda não executados nesta máquina**; rode e ajuste antes de confiar.

## 0. Ambiente

```bash
python -m venv .venv && .venv/Scripts/activate
pip install numpy scipy pandas pyyaml scikit-image scikit-learn rasterio geopandas shapely pyproj matplotlib
nvidia-smi                      # confirme o driver; escolha a versão de CUDA do wheel compatível
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
pip install segmentation-models-pytorch albumentations
python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
pip freeze > requirements.txt   # fixar versões
```

Se `cu121` não for compatível com o driver, use o índice indicado no site do PyTorch para a versão de CUDA suportada.

## 1. Recortes

- Lê só pixels com alfa > 0; descarta recortes com fração válida < `recortes.min_fracao_valida`.
- Tamanho `recortes.tamanho_px` (256), sobreposição de 32 px na inferência; no treino, deslocamentos aleatórios.
- O índice de blocos (`divisao.json`) decide o conjunto de cada recorte; **o recorte pertence ao conjunto do bloco onde está seu centro e é descartado se tocar a faixa de folga**.
- **Pares de treino:** pares de meses consecutivos e também de distância 2 e 3 (mais sinal de mudança); pares **sem mudança** do mesmo local para ensinar a ignorar cor.
- **Amostragem proporcional à mudança** (Metzger 2023, p. 5): `p_i ∝ a + N_i`, com `N_i` = pixels de mudança do recorte e `a ≈ 50` (valor da fonte; ajuste), mantendo recortes vazios; sem isso, 99% dos recortes não têm mudança.

## 2. Aumento de dados (o que mais importa aqui)

- Geometria igual nas duas datas: giros de 90°, espelhamentos, pequenos recortes.
- **Radiometria independente por data:** brilho, contraste, matiz e gama sorteados **para cada mês**, para simular a deriva de cor dos mosaicos visuais. É a defesa contra aprender diferença de produto como mudança. Limite o intervalo ao observado em `runs/qc/estabilidade_cor.csv`.
- Desfoque e ruído leves em uma das datas (robustez a mudança de nitidez, como a de 2022 nos basemaps; Chen 2024 testa robustez a desfoque e ruído, p. 17).
- Não aplique deformação elástica nem deslocamento relativo entre as datas, a menos que seja para simular erro de registro de ~1 px (e registre isso).

## 3. Modelos de partida

```python
import torch, torch.nn as nn
import segmentation_models_pytorch as smp

class UNetBitemporal(nn.Module):
    """Par de meses empilhado (6 canais) -> 1 canal de mudança (logit). Fusão precoce."""
    def __init__(self, encoder="resnet18", pretrained=True):
        super().__init__()
        self.net = smp.Unet(encoder_name=encoder, encoder_weights="imagenet" if pretrained else None,
                            in_channels=6, classes=1)
    def forward(self, a, b):                       # a, b: (B, 3, H, W) normalizados
        return self.net(torch.cat([a, b], dim=1))

class DiceFocal(nn.Module):
    def __init__(self, alpha=0.75, gamma=2.0, peso_dice=1.0):
        super().__init__(); self.alpha, self.gamma, self.pd = alpha, gamma, peso_dice
    def forward(self, logit, y, ignorar=None):
        p = torch.sigmoid(logit); m = torch.ones_like(y) if ignorar is None else (~ignorar).float()
        pt = torch.where(y > 0.5, p, 1 - p)
        focal = -(self.alpha * (1 - pt) ** self.gamma * torch.log(pt.clamp_min(1e-6)) * m).sum() / m.sum().clamp_min(1)
        inter = (p * y * m).sum(); dice = 1 - (2 * inter + 1) / ((p * m).sum() + (y * m).sum() + 1)
        return focal + self.pd * dice
```

- `smp.Unet(in_channels=6, encoder_weights="imagenet")` repete/adapta os pesos para 6 canais; confirme a adaptação.
- Alternativas: **siamesa** com encoder compartilhado e diferença/concatenação das características por escala; **por data + diferença** (M2) com 7 classes; **série** (U-TAE) com a série inteira.
- GPU de 4 GB: `resnet18` ou `resnet34`, recortes 256, lote 4–8 com **precisão mista** (`torch.autocast`) e acumulação de gradiente; congele o encoder nas primeiras épocas.

## 4. Treino e seleção

- Otimizador AdamW, taxa 1e-4 a 3e-4 com `OneCycleLR` ou cosseno; épocas máximas e parada antecipada pelo F1 de **evento** na validação.
- **Limiar de decisão escolhido por F1 na validação** (Metzger 2023, p. 5: média móvel do limiar ótimo por lote), não 0,5.
- Ajuste de hiperparâmetros com o **mesmo orçamento** para todos os métodos (`deteccao.tentativas_hiperparametros`).
- **Três sementes** por método (`avaliacao.sementes`); reporte média e desvio.
- Salve: pesos, `config.yaml` efetivo, semente, hash dos dados e da divisão, curvas, limiar escolhido (skill `registro-experimentos`). **Nunca** use o teste para escolher nada.

## 5. Pré-treino em dados abertos (M6)

SpaceNet 7/MUDS (Planet de ~4 m, 24 meses, 101 locais, AWS Open Data) e DynamicEarthNet (Planet Fusion de 3 m). Pré-treinar em **detecção de mudança** e ajustar com os eventos locais deu +2–3 pontos de F1 sobre ImageNet em previsão de construção (Metzger 2023, p. 7; outra tarefa e dados). Antes de usar: alinhar bandas e escala radiométrica ao nosso produto (RGB 8 bits), reamostrar para 4,5 m e verificar a licença. Fonte: `..\base_conhecimento\02_Artigos\Etten_2021_SpaceNetMultiTemporal.md`.

## 6. Aprendizado ativo

Depois do primeiro modelo, preveja sobre recortes não rotulados, ordene por entropia, anote os mais incertos e retreine (skill `rotulagem-referencia`).

## Armadilhas

- Treinar sem aumento radiométrico independente por data: o modelo vira detector de cor.
- Selecionar épocas e limiar no teste.
- Usar acurácia global: com poucos % de mudança ela chega a 97% prevendo "sem mudança" (lacuna L03).
- Lote grande demais para 4 GB: monitore `torch.cuda.max_memory_allocated()`.
- Não fixar sementes e versões: os resultados não se reproduzem.
