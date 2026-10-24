# Banco `mudanca_mascara` v2: rótulos de cobertura e de mudança

O banco é definido em dois arquivos:

- `db/mudanca_mascara.sql`: o banco inteiro em SQL plain para PostgreSQL 18 + PostGIS. Tem 44 tabelas, 19 visões e roda numa única transação: ou cria tudo, ou não cria nada.
- `db/testes.sql`: 88 verificações das regras, numa transação desfeita no fim.

O banco guarda **rótulos**. Os rasters ficam em `D:\PT2-build\Imagens de Satelite`, e as máscaras raster são geradas pelo pipeline a partir das visões do esquema `treino`.

## Criar e testar

No PowerShell, de qualquer pasta (cada comando pede a senha do `postgres`):

```powershell
& 'C:\Program Files\PostgreSQL\18\bin\psql.exe' -h localhost -p 5432 -U postgres -c 'CREATE DATABASE mudanca_mascara'
& 'C:\Program Files\PostgreSQL\18\bin\psql.exe' -h localhost -p 5432 -U postgres -d mudanca_mascara -f 'C:\Desenvolvindo\ML-DPL-Changes\Pratice\db\mudanca_mascara.sql'
& 'C:\Program Files\PostgreSQL\18\bin\psql.exe' -h localhost -p 5432 -U postgres -d mudanca_mascara -f 'C:\Desenvolvindo\ML-DPL-Changes\Pratice\db\testes.sql'
```

## Duas referências complementares

| Referência | Para quê | Onde |
|---|---|---|
| **Cobertura por data** | treinar e avaliar a classificação por data (M2) e, por diferença, a mudança | `rotulo.tarefa` → `sessao` → `anotacao`; séries em `rotulo.serie` |
| **Eventos de mudança** | referência de delta: tipo, de→para, estágio e mês de início (M0–M8) | `rotulo.evento` + `evento_evidencia` |
| **Controles estáveis** | falso alarme por km²·mês e deriva de cor | `rotulo.controle_estavel` |

## Esquemas

| Esquema | Conteúdo |
|---|---|
| `dominio` | Vocabulários (status, conjuntos, certeza, origem, condição de rotulagem, modo de seleção, QC, regime de processamento, ferramenta, estágio, superfície estável). Taxonomia de cobertura versionada e hierárquica (`taxonomia`, `classe`, `vw_classe`). Taxonomia de alterações (`tipo_alteracao`, `transicao_permitida`, de `configs/classes.yaml`). |
| `catalogo` | `sensor`, `grade` (3 grades reais lidas dos GeoTIFFs), `produto`, `imagem` (179 imagens, com QC), `aoi`, `vw_imagem`. |
| `rotulo` | Pessoas, campanha, proveniência (`processamento`), aprendizado ativo (`ciclo_aprendizado`), amostragem (`plano_amostral`, `estrato`), `serie`, `objeto`, cobertura (`tarefa`, `sessao`, `anotacao`), mudança (`evento`, `evento_evidencia`, `controle_estavel`). |
| `treino` | Divisão espaço-temporal (`divisao`, `bloco`), datasets congelados (`dataset`, `dataset_amostra`, `dataset_evento`, `dataset_controle`) e visões da máscara. |
| `auditoria` | `registro`, com todas as alterações (antes e depois em JSON, e quem fez), e utilitários. |

## Classes (`dominio.classe`)

Só as folhas recebem anotação. A macroclasse serve para avaliar em nível agregado.

| Macroclasse | Classe | Pixel | Treino |
|---|---|---|---|
| Vegetação | Vegetação densa (`vegetacao_arborea`), Vegetação rasteira (`vegetacao_rasteira`) | 1, 2 | aprende |
| Construído | Construção (`edificacao`) | 4 | aprende |
| Sistema viário | Rua pavimentada (`via_pavimentada`), Rua de terra (`via_terra`) | 5, 6 | aprende |
| Solo | Solo exposto (`solo_exposto`) | 3 | aprende |
| Hidrografia | Massa d'água (`agua`) | 7 | aprende |
| Sem informação | nuvem, sombra, sem dado, borda de mosaico, indeterminado | 251–255 | ignora |
| — | fora das tarefas, alfa 0, fora da AOI | 0 | ignora |

Cada classe tem uma cor, um critério de rotulagem (proposta inicial, a revisar com amostras) e uma área mínima.

## Como o banco atende às falhas da análise

| Falha | Solução no banco | Regra garantida |
|---|---|---|
| **F1** Não modelava mudança | `rotulo.evento` com tipo, de→para, estágio, `mes_inicio` e intervalo possível (`mes_inicio_min`/`max`), certeza, objeto e revisão. `evento_evidencia` registra as imagens antes, de início, completa e de confirmação (CBERS). `vw_concordancia_evento` mede a concordância (IoU ≥ 0,25, mesmo tipo, mês ± 1). | A transição precisa estar em `transicao_permitida` para o tipo. Os meses são sempre o dia 1. A evidência "antes" precisa ser anterior ao início. O revisor é outra pessoa. |
| **F2** Sem consistência temporal | `rotulo.serie` (mesmo recorte em várias datas), `fn_criar_serie`, `fn_propagar_sessao` (copia a sessão para a data seguinte; você edita só o que mudou), `anotacao.editada` e `objeto_id` persistente. `vw_mudanca_derivada` dá a pós-classificação da série. | A tarefa da série herda o recorte. A propagação só vale dentro da série e a partir de sessão enviada ou aprovada. Sessão propagada não conta como concordância independente. |
| **F3** Sem controles estáveis | `rotulo.controle_estavel` com tipo de superfície, classe, período e imagens de conferência nas pontas. | Não pode sobrepor evento ativo no período (nem o evento pode cair num controle). Só entra em dataset se confirmado. |
| **F4** Sem reserva temporal | `divisao.teste_temporal_inicio`/`fim` (2026-01 a 2026-09) e `treino.fn_conjunto`. | Uma data no período reservado vira `teste_temporal` (blocos de treino ou validação) ou `teste_espaco_tempo` (blocos de teste). Com o `teste` espacial, são os três regimes de Vincent 2024. |
| **F5** Sem amostra probabilística | `dominio.modo_selecao`, `tarefa.prob_inclusao`, `plano_amostral` e `estrato`. `fn_sortear_pontos` sorteia células de 1 pixel com a semente do plano. `vw_amostra_avaliacao` dá o peso (1/π) e a classe de referência. | Sorteio sem probabilidade é recusado. Plano de `avaliacao_independente` nunca entra em dataset. Aprendizado ativo exige ciclo, e tarefa de aprendizado ativo em conjunto de teste é excluída do dataset. |
| **F6** Mistura de resolução | `dataset.grade_id` obrigatório. | Só entram tarefas de imagens daquela grade. |
| **F7** Pré-anotação sem proveniência | `rotulo.processamento` (ferramenta, versão, modelo, parâmetros, `run_id`), `sessao.condicao_codigo` e `tempo_ativo_s`, e `anotacao.editada`. | Pré-rótulo sem processamento é recusado. O banco marca o pré-rótulo ou a propagação corrigidos. |
| **F8** Sem QC por imagem | `catalogo.imagem` com `qc_status`, regime de processamento (antes e depois da mudança de 2022), `pct_valido`, `pct_nuvem_estimada`, `deslocamento_px`, `nitidez` e `estabilidade_cor`. | Imagem reprovada não recebe tarefa. O congelamento exige `sha256` e QC aceito. |
| **F9** Folga desperdiçava área | A folga é aplicada só entre conjuntos diferentes, e cede o conjunto de menor ordem (o treino cede para a validação e o teste; o teste nunca perde área). A limitação do tamanho de bloco fica em `divisao.limitacao`. `vw_divisao_resumo` mostra o custo. | As áreas úteis de conjuntos diferentes ficam a pelo menos 100 m (`join=mitre` garante isso também nas quinas). A área útil subiu de 69,4% para 84,2%: teste 100%, validação 89,3%, treino 78,0%. |
| Menores | `vw_minha_anotacao` (rotulagem cega, editável no QGIS); convenção de valores 0 e 251–255 alinhada com a skill; congelamento sem hash proibido; aviso, ou recusa com `exigir_todas_classes`, quando falta uma classe em algum conjunto. | A pessoa só vê e grava nas próprias sessões (`WITH CHECK OPTION`). |

## Fluxos de trabalho

**Cobertura numa série** (o mais barato para obter mudança):
1. `SELECT rotulo.fn_criar_serie(campanha, 'global_monthly', geom, '2020-01-01', '2026-09-01');`
2. Rotule a primeira data: `fn_iniciar_sessao(tarefa, 'apelido')`, desenhe em `vw_minha_anotacao`, depois `fn_enviar_sessao(sessao, segundos)`.
3. Revise com `fn_revisar_sessao(sessao, 'revisor', true)`. O revisor tem de ser outra pessoa.
4. `fn_propagar_sessao(sessao_aprovada, tarefa_do_mes_seguinte, 'apelido')`, edite só o que mudou, envie e revise. Repita mês a mês.
5. `rotulo.vw_mudanca_derivada` mostra onde e quando a classe mudou, com os tipos de alteração candidatos.

**Eventos** (referência de delta direta): desenhe em `rotulo.evento` olhando a série, registre as evidências e peça a revisão (`fn_revisar_evento`). Em 20% dos eventos, faça uma segunda pessoa rotular às cegas e confira `vw_concordancia_evento`.

**Avaliação independente:**
1. Crie o `plano_amostral` (uso `avaliacao_independente`) e os `estrato`s.
2. Sorteie com `fn_sortear_pontos(estrato, imagem, n)`.
3. Rotule os pontos.
4. `vw_amostra_avaliacao` entrega estrato, peso e classe para o estimador de Olofsson 2014.

**Dataset:**
1. Crie o `treino.dataset` com `grade_id`.
2. Rode `fn_congelar_dataset(id)`. Ele inclui as máscaras aprovadas, os eventos confirmados e os controles confirmados.
3. Gere as máscaras com `vw_mascara_janela` e `vw_mascara_poligono`.
4. Registre `caminho_mascara`, `sha256_mascara` e `pixels_por_valor`.

Depois de congelado, nada muda: nem amostras, nem eventos, nem controles, nem a sessão de referência.

## QGIS

- **Edição:** use `rotulo.vw_minha_anotacao`, com chave `id`. Cada pessoa se conecta com o próprio login, igual ao `apelido`, ou roda `SET app.usuario = 'apelido'`.
  - Configure `classe_id`, `certeza_codigo` e `origem_codigo` como **Mapa de valores relacionados**.
  - Ative a aderência e a opção **Evitar sobreposição**.
- **Eventos e controles:** `rotulo.evento` e `rotulo.controle_estavel`.
- **Referência visual:** `rotulo.vw_tarefa`, `rotulo.vw_lacuna`, `treino.bloco` e `catalogo.vw_imagem`. A chave de cada visão é `id`.

## Testes executados

Em 2026-10-24, o script carregou num cluster PostgreSQL 18 + PostGIS temporário, e `db/testes.sql` passou inteiro (88 verificações):

- **Carga:** catálogo, grades, taxonomia, AOI e sorteio dos blocos.
- **F1 a F9:** cada uma com cenários positivos e de recusa.
- **Regras da v1:** recorte, lacuna, sobreposição, revisão e congelamento continuam valendo.

Dois defeitos apareceram nos testes e foram corrigidos:
- uma comparação que lia uma coluna inexistente na proteção do dataset;
- a autointerseção da geometria original da AOI, corrigida com `ST_MakeValid`.

**Sem teste:** a rasterização em Python a partir das visões (falta `rasterio` no Python do sistema) e o uso real no QGIS (edição pela visão `vw_minha_anotacao`).
