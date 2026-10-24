---
name: avaliacao-comparacao
description: Avaliar e comparar métodos de detecção de mudança de forma justa (blocos espaciais, período de teste, métricas de pixel e de evento, falsos alarmes em controles estáveis, latência, tamanho, calibração da confiança e estimativa de área com intervalo). Use ao medir qualquer detector, ao montar a tabela de comparação ou ao escrever conclusões.
---

# Avaliação e comparação

Regra central: **só se comparam métodos medidos no mesmo recorte, na mesma divisão, com a mesma métrica e o mesmo orçamento de ajuste.** Valores da literatura são relatados em dados diferentes e não servem de meta (lacuna L06). Base: `..\base_conhecimento\07_Resultados\Sintese_Metricas.md`, `Sintese_Particoes.md`, `06_Validacao\*`.

## O que medir

| Medida | Definição | Por quê |
|---|---|---|
| F1 e IoU de pixel da classe de mudança | sobre blocos de teste, só pixels válidos | nunca a acurácia global (a mudança é rara; lacuna L03) |
| **Precisão e recall de evento** | evento previsto casa com evento de referência se IoU ≥ `avaliacao.iou_evento` (0,25, como no SpaceNet 7) | pixel mascara o que importa: achar o evento |
| Erro do mês de início | mês detectado menos `mes_inicio` da referência (em meses) | o objetivo é datar |
| Recall por tamanho | por faixa de área (`avaliacao.faixas_area_px`) | acha o limite de detecção; edificações têm ~4–5 px |
| Por tipo | métricas por `tipo_alteracao` | edificação e vegetação se comportam diferente |
| **Falso alarme em controles estáveis** | polígonos previstos dentro de `controles_estaveis`, por km² e por mês | separa ruído de cor de erro do modelo |
| Latência | meses até a detecção **confirmada**; fração de `provisoria` que vira falso positivo | custo da persistência |
| Calibração | diagrama de confiabilidade, ECE, precisão por `classe_confianca` | a confiança precisa significar probabilidade |
| Área | estimativa por amostragem estratificada com IC (Olofsson 2014; Zhang 2023, p. 14–16) | área de mudança é produto final |
| Robustez | troca de família de mosaico, de ano, de bloco; desfoque e ruído | generalização |
| Custo | tempo de treino, memória, tempo por mosaico | decisão prática |

## Divisão e honestidade

- Use **só** `runs/referencia/divisao.json` (blocos com folga + período final). O conjunto de teste é aberto **uma vez** por versão de método, depois que hiperparâmetros e limiar foram fixados na validação.
- Reporte validação e teste em colunas separadas e a diferença entre eles.
- **Três sementes** para métodos com treino; média e desvio. Diferenças menores que o desvio não são diferenças.
- Registre o orçamento de ajuste (nº de tentativas) de cada método na tabela.

## Código de partida

```python
import geopandas as gpd, numpy as np

def casar_eventos(prev: gpd.GeoDataFrame, ref: gpd.GeoDataFrame, iou_min=0.25):
    """Casa polígonos previstos com os de referência (1 a 1, maior IoU). Retorna tp, fp, fn e pares."""
    prev = prev.reset_index(drop=True); ref = ref.reset_index(drop=True)
    cand = gpd.sjoin(prev[["geometry"]].reset_index(names="i"), ref[["geometry"]].reset_index(names="j"), predicate="intersects")
    pares = []
    for _, r in cand.iterrows():
        a, b = prev.geometry[r.i], ref.geometry[r.j]
        u = a.union(b).area
        iou = a.intersection(b).area / u if u > 0 else 0
        if iou >= iou_min: pares.append((r.i, r.j, iou))
    usados_i, usados_j, ok = set(), set(), []
    for i, j, iou in sorted(pares, key=lambda x: -x[2]):
        if i not in usados_i and j not in usados_j:
            usados_i.add(i); usados_j.add(j); ok.append((i, j, iou))
    tp = len(ok); fp = len(prev) - tp; fn = len(ref) - tp
    return dict(tp=tp, fp=fp, fn=fn, precisao=tp / max(tp + fp, 1), recall=tp / max(tp + fn, 1), pares=ok)

def falsos_alarmes(prev: gpd.GeoDataFrame, controles: gpd.GeoDataFrame, n_meses, area_km2):
    dentro = gpd.sjoin(prev, controles[["geometry"]], predicate="intersects")
    return dict(n=len(dentro), por_km2_mes=len(dentro) / max(area_km2 * n_meses, 1e-9))

def ece(prob, y, bins=10):
    prob, y = np.asarray(prob), np.asarray(y)
    idx = np.minimum((prob * bins).astype(int), bins - 1); e = 0.0
    for b in range(bins):
        m = idx == b
        if m.any(): e += m.mean() * abs(prob[m].mean() - y[m].mean())
    return e
```

Estimador de área e acurácia estratificado (Stehman 2014, como em Zhang 2023, p. 14–16 e Olofsson 2014): para estratos `h` com tamanho `N_h` e `n_h` pontos de referência, `p_k = (1/N) Σ_h N_h · ȳ_hk`, com erro-padrão e IC de 95% = ±1,96·EP. Defina estratos por mês de detecção e por classe do mapa, com 50 pontos por estrato de mudança no mínimo e um estrato grande de "estável"; a referência vem de interpretação visual **com registro de concordância**.

## Tabela de comparação (modelo)

| Tarefa | Método | Dados (família, período) | Divisão | Sementes | Ajuste (tentativas) | F1 pixel | Precisão evento | Recall evento | Erro de mês (mediana) | Falso alarme (por km²·mês) | Latência (meses) | ECE | Custo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Uma tabela por tarefa (supressão arbórea, edificação, via, geral). Nunca misture divisões.

## Relatório

1. Perguntas respondidas e perguntas que **não** se pode responder (uma AOI, rótulos feitos por nós, só RGB, intérpretes discordam).
2. Tabela, curvas e mapas de erro por mês dos melhores métodos, mais um exemplo de falha de cada.
3. Recall por tamanho (limite de detecção) e falso alarme por tipo de superfície.
4. Decisão: qual método segue e por quê, com o custo em latência.
5. Salve em `runs/avaliacao/<data>_<nome>/` com o manifesto (skill `registro-experimentos`).

## Armadilhas

- Escolher limiar ou época no teste.
- Comparar F1 de pixel de um método com F1 de evento de outro.
- Medir só o que o modelo acerta por estar nos mesmos blocos de treino.
- Reportar confiança sem calibração; classes de confiança sem a precisão observada.
- Esquecer os controles estáveis: sem eles, falso alarme por cor parece "erro do modelo".
