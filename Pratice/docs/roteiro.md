# Roteiro por fases

Cada fase termina com um entregável verificável e um commit. As skills correspondentes estão entre parênteses.

| Fase | Objetivo | Entregáveis | Critério de pronto |
|---|---|---|---|
| 0. Ambiente | Python isolado com `rasterio`, `geopandas`, `torch` (CUDA) e `segmentation-models-pytorch` | `requirements.txt` fixado, script de verificação | `python -c "import torch; print(torch.cuda.is_available())"` retorna verdadeiro na GTX 1650 |
| 1. Inventário e QC (`inventario-dados`) | Catalogar a série, checar grade, alfa, hashes e estabilidade radiométrica | `runs/qc/inventario.csv`, relatório de estabilidade, escolha da família principal | todas as datas na mesma grade; relatório mostra a deriva de cor por mês e o salto de 2022 |
| 2. Rotulagem (`rotulagem-referencia`) | Referência de eventos 2020–2026 com mês de início e tipo, áreas estáveis de controle, divisão por blocos | GeoPackage de referência, `divisao.json`, registro de concordância | mínimo acordado de eventos por tipo; controles estáveis definidos; divisão sem vazamento verificada |
| 3. Baselines (`baselines-mudanca`) | M0 e M1 funcionando sobre toda a série | vetores de baseline, métricas de pixel e evento | resultado reproduzível e registrado |
| 4. Modelos (`treino-modelos`) | M3 e M2 treinados; depois M6, M5, M4 conforme resultado | modelos, curvas, métricas por semente | cada modelo avaliado na mesma divisão |
| 5. Comparação (`avaliacao-comparacao`) | Tabelas por tarefa, falsos alarmes, latência, tamanho, calibração | relatório de comparação com limites explícitos | conclusões escritas com o que não se pode afirmar |
| 6. Vetores e confiança (`vetorizacao-confianca`) | S5–S7: delta mensal e consolidado anual com confiança calibrada | GeoPackages de toda a série, diagrama de confiabilidade | esquema validado; mesmos identificadores em duas execuções |
| 7. Inferência (`inferencia-nova-imagem`) | Modo `incremental`: baixar uma imagem nova e obter o delta | comando único, teste com a imagem de 2026-10 | delta gerado sem treinar de novo; reclassificação dos 3 meses anteriores |
| 8. Generalização | 2 a 4 AOIs adicionais (outros bairros do RJ, outro bioma) para testar fora da área | novas séries e referências | métricas fora da AOI de treino reportadas separadamente |

## Primeira sessão sugerida

1. Criar o ambiente e rodar a verificação (fase 0).
2. Rodar o inventário e abrir o relatório de estabilidade (fase 1); decidir a família principal.
3. Escolher 3 a 5 locais com mudança evidente (por exemplo, o canto nordeste e a borda do loteamento) e montar a primeira referência no QGIS, usando o `catalogo.html` e o CBERS de 2 m para confirmar.
4. Rodar M0 e M1 só nesses locais para ter a primeira métrica de ponta a ponta.

## Riscos que merecem atenção desde o início

- Rotular só o que o modelo acerta fácil (viés de seleção). Use amostragem estratificada e inclua áreas estáveis.
- Treinar e testar em blocos vizinhos da mesma AOI e declarar generalização.
- Tratar a deriva de cor como mudança real.
- Ajustar limiares com os mesmos meses usados para avaliar.
- Declarar confiança sem calibrar.
