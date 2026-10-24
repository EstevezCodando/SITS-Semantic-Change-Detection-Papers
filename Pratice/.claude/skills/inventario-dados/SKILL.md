---
name: inventario-dados
description: Catalogar e validar a série de imagens Planet (e CBERS/PSScene) do projeto de detecção de mudanças. Use ao receber imagens novas, antes de qualquer treino, ao decidir qual família de mosaico usar, ou quando suspeitar de deriva de cor, desalinhamento, nodata ou salto de processamento entre meses.
---

# Inventário e QC da série

Objetivo: garantir que as imagens que entram no pipeline estão na mesma grade, com dado válido, e **medir a inconsistência radiométrica** entre meses, que é a principal fonte de falso positivo (`docs/dados.md`).

## Entradas e saídas

- Entrada: `dados.raiz` e `dados.fontes` de `configs/pipeline.yaml` (somente leitura).
- Saída em `runs/qc/`: `inventario.csv`, `estabilidade_cor.csv`, `estabilidade_cor.png`, `qc_resumo.md`.

## Passos

1. **Listar a série** por família: parse do nome (`global_monthly_AAAA_MM_mosaic.tif`), mês esperado, lacunas de meses, duplicatas. Para `medres_normalized`, o primeiro mosaico cobre 2020-06 a 2020-08.
2. **Checar a grade**: CRS, transform, largura e altura iguais em todas as datas da mesma fonte (725 × 659 a 4,5 m para os basemaps). Qualquer desvio é erro, não aviso.
3. **Checar o alfa e o dado**: fração de pixels com alfa 0 por data; rasters totalmente cheios devem ter 100%; registre a data com buracos.
4. **Hash** (SHA-256) de cada arquivo para rastreabilidade.
5. **Estabilidade radiométrica**: defina uma máscara de **áreas estáveis** (água profunda não conta; prefira telhado antigo, asfalto e mata fechada, escolhidos à mão em 5 a 10 polígonos que não mudam na série). Para cada mês, calcule média e desvio de R, G, B e do Hue dentro dessas áreas e trace as curvas. Procure: deriva sazonal, saltos súbitos (por exemplo, em 2022, quando a Planet mudou nitidez e super-resolução; Glazer 2025, p. 2–3) e meses discrepantes.
6. **Comparar famílias** (`global_monthly` vs `medres_normalized`) pela variância temporal dentro das áreas estáveis; a menor deriva vence como entrada principal, salvo razão contrária registrada.
7. **Nitidez**: compare a energia de alta frequência (variância do laplaciano) por mês; uma mudança brusca indica troca de processamento e justifica harmonização ou treino por período.
8. Escreva `qc_resumo.md` com decisões e problemas. Atualize `fonte_principal` em `configs/pipeline.yaml` **só** com a evidência anexa.

## Código de partida

```python
import rasterio, numpy as np, hashlib, re, pandas as pd
from pathlib import Path

def ler(path):
    with rasterio.open(path) as s:
        a = s.read()                      # (4, H, W) uint8: R, G, B, alfa
        return a, s.crs, s.transform, s.width, s.height

def mes_do_nome(p):
    m = re.search(r"(\d{4})_(\d{2})", p.name)
    return f"{m.group(1)}-{m.group(2)}" if m else None

def hue(rgb):
    r, g, b = [rgb[i].astype("float32") for i in range(3)]
    # índice Hue como em Zhang 2023 (eq. 2, p. 11): conferir na fonte antes de usar com limiares publicados
    den = 30.5 * (g - b)
    den = np.where(np.abs(den) < 1e-6, 1e-6, den)
    return np.arctan(2 * (r - g - b) / den)

linhas = []
for p in sorted(Path(pasta).glob("*.tif")):
    a, crs, tr, w, h = ler(p)
    valido = a[3] > 0
    est = estavel_mask & valido           # máscara das áreas estáveis (booleana, mesma grade)
    linhas.append(dict(
        arquivo=p.name, mes=mes_do_nome(p), crs=str(crs), w=w, h=h, transform=tuple(tr)[:6],
        pct_valido=100 * valido.mean(), sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
        r=a[0][est].mean(), g=a[1][est].mean(), b=a[2][est].mean(), hue=float(np.nanmean(hue(a[:3])[est])),
        nitidez=float(np.var(np.diff(a[:3].mean(0), axis=0)))))
pd.DataFrame(linhas).to_csv("runs/qc/inventario.csv", index=False)
```

## Armadilhas

- **Não** usar o PNG: ele tem faixa de texto e perde o valor original.
- Mosaicos visuais não têm reflectância; compare **tendências**, não valores absolutos entre produtos.
- Áreas estáveis escolhidas olhando só uma data podem mudar depois; verifique-as em `catalogo.html` em 2020 e em 2026.
- O CBERS de 2 m e o PSScene de 3 m **não** estão na mesma grade que os basemaps; trate-os como fontes distintas.

## Critérios de pronto

- Todas as datas de cada fonte na mesma grade, ou o erro registrado.
- Curvas de estabilidade geradas e interpretadas por escrito.
- Decisão sobre a família principal registrada com a evidência.
