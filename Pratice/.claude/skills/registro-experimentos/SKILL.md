---
name: registro-experimentos
description: Registrar cada execução (baseline, treino, avaliação, inferência) com configuração, versão dos dados, divisão, sementes, métricas e custo, e comparar execuções. Use ao rodar qualquer experimento, ao montar tabelas de comparação ou ao reproduzir um resultado.
---

# Registro de experimentos

Sem rastro, um número não existe. Cada execução cria uma pasta em `runs/` (fora do git) e deixa um `run.json` que permite reproduzi-la e compará-la.

## Estrutura

```text
runs/
  <tarefa>/<AAAA-MM-DD_hhmm>_<metodo>_<semente>/
    run.json            # tudo que identifica a execução (abaixo)
    config.yaml         # cópia da configuração efetiva
    metricas.json       # métricas de validação e, se aberto, de teste
    curvas.csv          # perda e métricas por época
    previsoes/          # mapas e vetores (opcional)
    log.txt
  tabela_comparacao.csv # gerada, uma linha por execução
```

## `run.json` mínimo

| Campo | Conteúdo |
|---|---|
| `run_id`, `data_hora`, `tarefa`, `metodo`, `modelo_id` | identificação |
| `commit_git`, `git_sujo` | versão do código e se havia alterações não commitadas |
| `dados` | família, intervalo de meses, hashes dos arquivos (de `runs/qc/inventario.csv`) |
| `divisao` | hash de `divisao.json`, semente, período de teste |
| `semente` | semente da execução |
| `hiperparametros` | todos, mais o número de tentativas de ajuste usadas (orçamento) |
| `ambiente` | versões de Python, torch, rasterio, GPU |
| `metricas` | F1/IoU de pixel, precisão e recall de evento, erro de mês, falso alarme em controles, latência, ECE |
| `custo` | tempo de treino, memória máxima de GPU, tempo por mosaico |
| `limitacoes` | texto curto: o que esta execução **não** mostra |
| `teste_aberto` | `true` se o conjunto de teste foi usado (só uma vez por versão de método) |

## Regras

1. **Teste aberto uma única vez** por versão de método; qualquer alteração depois abre uma nova versão.
2. **Não comparar** execuções com `dados` ou `divisao` diferentes na mesma tabela; separe por bloco.
3. Execuções com `git_sujo = true` não entram em comparação oficial.
4. Reportar média e desvio de, no mínimo, três sementes antes de afirmar diferença.
5. Registrar também os **resultados negativos** (método que não funcionou e por quê).
6. Registrar o que mudou entre versões do modelo (dados, rótulos, perda, aumento).

## Comparação

Um script `compara_execucoes.py` lê os `run.json` e gera `tabela_comparacao.csv` com uma linha por execução e colunas do modelo de tabela de `avaliacao-comparacao`. Agrupe por `tarefa`, `dados` e `divisao`; calcule média e desvio por método.

```python
import json, pandas as pd
from pathlib import Path

def carregar(raiz="runs"):
    linhas = []
    for p in Path(raiz).rglob("run.json"):
        j = json.loads(p.read_text(encoding="utf-8")); m = j.get("metricas", {})
        linhas.append(dict(run=p.parent.name, tarefa=j["tarefa"], metodo=j["metodo"], semente=j["semente"],
                           dados=j["dados"]["familia"], divisao=j["divisao"]["hash"], teste=j.get("teste_aberto", False),
                           sujo=j.get("git_sujo", False), **m))
    return pd.DataFrame(linhas)

df = carregar()
oficial = df[~df.sujo]
resumo = oficial.groupby(["tarefa", "dados", "divisao", "metodo"]).agg(["mean", "std"]).round(3)
```

## Ligação com o conhecimento

Quando um experimento responder uma pergunta aberta da base (por exemplo, L11, L12, L13, L14), adicione uma nota curta em `..\base_conhecimento` com: pergunta, dados, método, resultado, limite e o caminho do `run.json`. Regra do repositório: commit para cada alteração.
