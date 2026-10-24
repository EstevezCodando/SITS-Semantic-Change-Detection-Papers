---
name: baselines-mudanca
description: Implementar e rodar os métodos de linha de base sem treino para mudança de cobertura em Planet RGB (diferença de imagens, índice Hue referenciado à vizinhança com persistência de 3 meses, pós-classificação). Use para obter o piso de comparação, a primeira métrica de ponta a ponta e o segundo método da concordância de confiança.
---

# Baselines de mudança

Os baselines dão o **piso** da comparação, não custam rótulos (só para calibrar limiares) e alimentam a confiança (`conf_concordancia`). Cada um entra no pipeline como detector com a mesma interface (`prever(par_ou_serie) -> prob_mudanca`).

Evidência: `..\base_conhecimento\02_Artigos\Zhang_2023_MonitoringMonthlyTropical.md` (M1), `07_Resultados\Sintese_Receitas.md`.

## M0 — diferença de imagens

1. Alinhe e normalize as duas datas (skill `inventario-dados` e etapa S1).
2. Distância de cor por pixel entre `M-1` e `M` (por exemplo, norma L2 em Lab ou diferença absoluta média dos canais), com suavização gaussiana pequena (σ ≈ 1 px).
3. Limiar por Otsu **dentro de áreas estáveis e de mudança conhecidas do treino**, não da imagem inteira.
4. Remova manchas menores que `posproc.area_min_m2` e feche vazios.

Use como piso e como diagnóstico: se M0 já acerta a maioria dos eventos grandes, o ganho dos modelos treinados vem dos pequenos e ambíguos.

## M1 — Hue referenciado e persistência (Zhang 2023)

Receita da fonte (NICFI mensal de 5 m, 4 bandas, floresta úmida). Etapas e parâmetros relatados (valores da fonte, **recalibrar aqui**):

1. **Máscara de vegetação-alvo** (onde se procura supressão). Em Zhang 2023 vem de cinco produtos de floresta (p. 6, 10); aqui, derive de uma classificação local de vegetação arbórea e rasteira, revisada à mão.
2. **Máscara de nuvem** por mês: floresta aleatória sobre o composto de máximo anual + índice HOT (p. 9–10). Com RGB visual, comece por brilho e saturação e meça em controles.
3. **Índice Hue** `Hue = arctan( 2(R−G−B) / (30,5·(G−B)) )` (p. 11, eq. 2; confira na fonte), restrito à vegetação-alvo.
4. **rHue**: Hue menos a **mediana local** (raio de 300 m, ≈ 67 px a 4,5 m), limitado a [0, 1] (p. 11–12, eqs. 4–6). Isso anula a variação de iluminação e fenologia que atinge toda a vizinhança.
5. **Detecção possível**: primeiro mês em que `rHue > T` com `T = 0,09` na fonte (faixa sugerida 0,06–0,12) e o mês anterior abaixo de T (p. 12–13).
6. **Persistência**: confirmar só se a mudança aparece em ≥ 3 de 5 observações (um mês antes e três depois); remova manchas com < 7 pixels em janela 15 × 15 (p. 13).
7. Emita **dois mapas**: `possivel` (alerta imediato, muitos falsos positivos) e `ajustado` (confirmado, atraso ≥ 3 meses). A fonte mede, para o possível, usuário 21% e produtor 97%, e para o ajustado, usuário 85% e produtor 61% ± 46 (p. 20–21), em outra área.

```python
import numpy as np
from skimage.filters import rank
from skimage.morphology import disk

def hue_idx(rgb):
    r, g, b = [rgb[i].astype("float32") for i in range(3)]
    den = 30.5 * (g - b)
    den = np.where(np.abs(den) < 1e-6, 1e-6, den)
    return np.arctan(2 * (r - g - b) / den)

def rhue(rgb, alvo_mask, raio_px=67):
    h = hue_idx(rgb)
    q = np.clip((h + np.pi / 2) / np.pi * 255, 0, 255).astype("uint8")          # quantiza para usar a mediana rápida
    med = rank.median(q, footprint=disk(raio_px)).astype("float32") / 255 * np.pi - np.pi / 2
    return np.clip(h - med, 0, 1) * alvo_mask

def persistente(rhues, t=0.09, n_conf=3, janela=(1, 3)):
    """rhues: lista de matrizes por mês. Retorna, por mês, máscara de início confirmado."""
    meses = len(rhues); saida = []
    for m in range(meses):
        ini = (rhues[m] > t) & (rhues[m - 1] <= t if m > 0 else True)
        if m + janela[1] >= meses:                      # ainda sem os meses seguintes: provisório
            saida.append((ini, None)); continue
        conf = sum((rhues[m + k] > t / 3) for k in range(0, janela[1] + 1))
        saida.append((ini, ini & (conf >= n_conf)))
    return saida
```

Limites já conhecidos da fonte: nuvem residual e sombra geram falso positivo; solo claro e florestas deciduais confundem; degradação sub-pixel não aparece; só um ano e um país (p. 24–25). Aqui, o RGB visual sem NIR e o solo claro do loteamento agravam isso.

## M2 — pós-classificação (diferença de mapas)

1. Treine (skill `treino-modelos`) um classificador de cobertura **por data**, com as classes de `configs/classes.yaml`.
2. Para cada par, compare os mapas: mudança onde a classe difere e a probabilidade conjunta é alta; `classe_de` e `classe_para` saem direto.
3. Limite: os erros das duas datas se somam e podem gerar mudança falsa; a fonte aponta que a classificação por data não vê mudança entre datas (Wagner 2023; Zaraza-Aguilera 2022 compara com mudança direta).

## O que registrar

Para cada baseline: versão dos dados, parâmetros (T, raio, janela), métricas de pixel e de evento nos blocos de validação e **nos controles estáveis** (falsos alarmes por km² e por mês), latência. Use a skill `registro-experimentos`.

## Armadilhas

- Copiar `T = 0,09` sem recalibrar: o produto e a paisagem são outros.
- Ajustar limiares nos meses de teste.
- Usar a imagem inteira para o Otsu: a classe de mudança é rara e o limiar fica dominado pelo fundo.
- Não separar `possivel` de `ajustado`: a troca entre latência e precisão some.
