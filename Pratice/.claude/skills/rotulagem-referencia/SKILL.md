---
name: rotulagem-referencia
description: Construir a referência (verdade de campo visual) de mudanças de cobertura com mês de início, tipo e áreas estáveis de controle, e definir a divisão treino/validação/teste por blocos. Use quando não houver rótulos, ao ampliar a referência, ao medir concordância entre intérpretes ou ao montar um ciclo de aprendizado ativo.
---

# Rotulagem e referência

Hoje **não há rótulos**. Sem referência confiável nenhuma comparação de métodos vale. Esta skill produz três coisas: **eventos** (mudanças reais), **controles estáveis** (onde nada muda) e a **divisão por blocos**.

Base de conhecimento: `..\base_conhecimento\07_Resultados\Sintese_Rotulagem.md`, `04_Preparo\AprendizadoAtivo.md`, `04_Preparo\RotulagemTemporal.md`, `06_Validacao\ReferenciaVisual.md`, `02_Artigos\Masolele_2024_MappingDiversityLand.md`.

## Unidade de referência

A referência vive no banco PostGIS `mudanca_mascara` (`db/mudanca_mascara.sql`, guia em `docs/banco_mascara.md`): eventos em `rotulo.evento`, controles em `rotulo.controle_estavel`, cobertura por data em `rotulo.tarefa`/`anotacao`, divisão em `treino.bloco`. O GeoPackage abaixo é a exportação para o pipeline.

Camada `referencia_eventos` (GeoPackage em `runs/referencia/`, EPSG:32723; espelha `rotulo.evento`):

| Campo | Descrição |
|---|---|
| `id_ref` | identificador |
| `tipo_alteracao` | domínio de `configs/classes.yaml` |
| `classe_de`, `classe_para` | cobertura antes e depois |
| `mes_inicio` | **primeiro mês em que a mudança é visível** na série (`AAAA-MM`) |
| `mes_visivel_completo` | mês em que a obra/supressão termina (opcional) |
| `certeza` | `certa`, `provavel`, `duvidosa` |
| `evidencia` | fontes que confirmam (`planet`, `cbers_2m`, `psscene_3m`, `outra`) |
| `interprete` | iniciais |
| `observacao` | texto livre |

Camada `controles_estaveis` (polígonos que **não** mudam entre 2020-01 e 2026-09, por tipo: telhado antigo, asfalto, mata fechada, água, solo compactado). Servem para medir falso alarme e deriva de cor.

## Como rotular

1. **Ferramentas:** QGIS com a série em ordem temporal (Temporal Controller ou camadas ordenadas) e o `catalogo.html` para navegação rápida. Para confirmar um evento ambíguo, abra o **CBERS de 2 m** (`CBERS/wpm_fused_2m`, a partir de 2023-04) e o **PSScene de 3 m**.
2. **Procedimento por evento:** ache a mudança na imagem final, volte mês a mês até o último mês **sem** a mudança; `mes_inicio` é o seguinte. Em meses nublados ou com cor discrepante, marque `certeza = provavel` e registre o intervalo possível no campo de observação.
3. **Contorno:** desenhe a extensão visível do último mês em que o evento está completo; o pipeline compara a geometria por sobreposição, não por contorno perfeito.
4. **Evitar viés de seleção:** não rotule só o que o detector acerta. Monte a amostra por **estratos**: (a) candidatos do baseline M0/M1 com pontuação alta, média e baixa; (b) amostra aleatória de áreas sem candidato; (c) locais conhecidos por mudança, vistos no começo e no fim da série.
5. **Controles estáveis:** escolha pelo menos 30 polígonos distribuídos pelos tipos de superfície e pelos blocos; confirme em 2020 e em 2026.
6. **Duas pessoas em 20% dos eventos** (ou o mesmo intérprete em dois momentos, com semanas de intervalo). Registre a concordância em `runs/referencia/concordancia.md` (acordo de existência, de tipo e do mês de início ± 1). Em Zhang 2023 a discordância entre três intérpretes foi de 32,43% (p. 7): espere divergência e **registre-a**, não a esconda.

## Aprendizado ativo (reduz o custo)

Ciclo por entropia, como em Masolele 2024 (p. 2 e 10; F1 macro de 43% para 84% em dois ciclos, em outra tarefa e dados):

1. treinar com a referência atual (skill `treino-modelos`);
2. prever sobre recortes **ainda não rotulados** e calcular a entropia de cada recorte;
3. anotar os de maior entropia (e uma fração aleatória para não enviesar);
4. devolver ao treino; repetir. O conjunto de teste fica **fora** do ciclo, em blocos nunca anotados por esse caminho.

## Divisão por blocos (anti-vazamento)

- Grade de blocos de `divisao.tamanho_bloco_m` (600 m) sobre a AOI; atribua cada bloco a treino, validação ou teste; **descarte uma faixa de folga** (`divisao.folga_m`) entre blocos de conjuntos diferentes.
- Reserve também um **período final** (`divisao.periodo_teste_final`) para testar no tempo.
- Um evento que atravessa blocos fica **inteiro** no mesmo conjunto.
- Salve `runs/referencia/divisao.json` (bloco → conjunto, semente, versão dos dados) e verifique: nenhum pixel de treino a menos de `folga_m` de um pixel de teste.
- Para os controles estáveis use a **mesma** divisão.

## Gerar rótulos raster por par de meses

Para cada par de meses consecutivos `(M-1, M)`, rasterize na grade da série:

- classe 1 (mudança) no par `(M-1, M)` quando `mes_inicio == M` (mudança **nova** naquele par). Nos pares seguintes o evento é "mudança já ocorrida" e não leva rótulo de mudança nova; registre essa regra em `rotulos.md`.
- alfa 0, fora da AOI e fora das tarefas viram `valor_nao_rotulado` (0); `indeterminado` é 255 e nuvem, sombra, sem dado e borda são 251–254. Todos entram como `ignore_index` (convenção do banco `mudanca_mascara`, `docs/banco_mascara.md`).
- Guarde também a rasterização de `classe_de` e `classe_para` para os modelos semânticos.

## Quanto rotular (ponto de partida a validar)

Não existe número mágico. Comece por 100 a 150 eventos e todos os controles; meça a curva de aprendizado (métrica de validação × número de eventos) e pare quando a curva achatar. Registre a quantidade por tipo e por bloco.

## Armadilhas

- Tratar rebrota ou obra paralisada como evento permanente: use `estagio = revertido`.
- Rotular com a imagem de uma só data depois do fato: sem a série, o mês de início fica errado.
- Misturar `inicio_construcao` e `edificacao_nova` sem critério: defina por escrito o que é "início" (terraplenagem, fundação, canteiro).
- Rotular os controles olhando a mesma data em que o modelo foi ajustado.

## Critérios de pronto

- Referência com tipo, de→para e mês de início; controles estáveis; `divisao.json`; concordância registrada; contagens por tipo.
