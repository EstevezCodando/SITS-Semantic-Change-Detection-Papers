# Banco `mudanca_mascara`: rótulos de cobertura para treino

O banco é definido em dois arquivos:

- `db/mudanca_mascara.sql`: o banco inteiro em SQL plain para PostgreSQL 18 + PostGIS.
- `db/testes.sql`: 42 testes das regras, que rodam numa transação e desfazem tudo no fim.

O banco guarda **rótulos**, ou seja, polígonos de cobertura com a data do que foi classificado, ligados à imagem rotulada. Os rasters continuam em `D:\PT2-build\Imagens de Satelite`. A máscara raster é gerada pelo pipeline a partir das visões do esquema `treino`.

## Criar e testar

No PowerShell, a partir da pasta `Pratice`:

```powershell
& 'C:\Program Files\PostgreSQL\18\bin\psql.exe' -h localhost -p 5432 -U postgres -c 'CREATE DATABASE mudanca_mascara'
& 'C:\Program Files\PostgreSQL\18\bin\psql.exe' -h localhost -p 5432 -U postgres -d mudanca_mascara -f db\mudanca_mascara.sql
& 'C:\Program Files\PostgreSQL\18\bin\psql.exe' -h localhost -p 5432 -U postgres -d mudanca_mascara -f db\testes.sql
```

O script roda numa única transação: ou cria tudo, ou não cria nada.

## Esquemas

| Esquema | Papel | Principais objetos |
|---|---|---|
| `dominio` | Vocabulários controlados e taxonomia | `taxonomia`, `classe`, `status_sessao`, `papel_conjunto`, `nivel_certeza`, `origem_anotacao`, `funcao_pessoa`, `vw_classe` |
| `catalogo` | O que existe para rotular | `sensor`, `grade`, `produto`, `imagem`, `aoi`, `vw_imagem` |
| `rotulo` | O trabalho de rotulagem | `pessoa`, `campanha`, `tarefa`, `sessao`, `anotacao`, `vw_tarefa`, `vw_anotacao`, `vw_lacuna`, `vw_concordancia`, `vw_progresso` |
| `treino` | O que vai para o modelo | `divisao`, `bloco`, `dataset`, `dataset_amostra`, `vw_tarefa_conjunto`, `vw_mascara_poligono`, `vw_mascara_janela`, `vw_balanco_classe` |
| `auditoria` | Rastro e utilitários | `registro` (toda alteração), `fn_multipoligono` |

## Taxonomia (`dominio.classe`)

A taxonomia é **versionada**. Mudar uma classe ou um valor de pixel exige uma nova versão, e a campanha fica presa à versão que usa. As classes formam uma **árvore**: só as folhas recebem anotação, e a macroclasse serve para avaliar em nível agregado.

| Macroclasse | Classe (folha) | Pixel | Treino |
|---|---|---|---|
| Vegetação | Vegetação densa (`vegetacao_arborea`) | 1 | aprende |
| | Vegetação rasteira (`vegetacao_rasteira`) | 2 | aprende |
| Construído | Construção (`edificacao`) | 4 | aprende |
| Sistema viário | Rua pavimentada (`via_pavimentada`) | 5 | aprende |
| | Rua de terra (`via_terra`) | 6 | aprende |
| Solo | Solo exposto (`solo_exposto`) | 3 | aprende |
| Hidrografia | Massa d'água (`agua`) | 7 | aprende |
| Sem informação | Nuvem, sombra de nuvem, sem dado, borda de mosaico, indeterminado | 251–255 | ignora |
| (fora das tarefas) | — | 0 | ignora |

Os valores 1 a 7 seguem `configs/classes.yaml`. Cada classe também traz:

- **cor**, para o QGIS;
- **critério de rotulagem**: o guia de decisão para o rotulador. É uma proposta inicial; revise com amostras reais;
- **área mínima** que vale a pena desenhar;
- `ignorar_no_treino`: marca as classes cujos pixels viram `ignore_index` na perda.

## Fluxo de rotulagem

```text
campanha ─► tarefa ─► sessão (rotulador) ─► anotações ─► envio ─► revisão (outra pessoa) ─► aprovada
 (taxonomia)  (recorte de                    (partição da     (sem      (aprova ou rejeita)    = referência
              UMA imagem)                     tarefa)          lacuna)                            da tarefa
```

1. **Tarefa**: um recorte de uma imagem. A `data_referencia` é copiada da imagem e não pode ser editada. A tarefa precisa caber na extensão da imagem e não pode sobrepor outra tarefa da mesma imagem e campanha. Para criar uma tarefa por bloco da divisão, use `treino.fn_criar_tarefas_por_bloco(campanha, imagem, divisao)`.
2. **Sessão**: a passada de uma pessoa sobre a tarefa (`rotulo.fn_iniciar_sessao(tarefa, 'apelido')`). Duas pessoas na mesma tarefa permitem medir a concordância.
3. **Anotações**: cada polígono é corrigido e **recortado ao limite da tarefa**. Polígonos da mesma sessão **não podem se sobrepor**. A data e a tarefa vêm da sessão. Só classes folha da taxonomia da campanha são aceitas. Cada anotação leva uma certeza (alta, média ou baixa, com peso sugerido para a perda) e pode indicar uma imagem de apoio (por exemplo, a CBERS de 2 m).
4. **Envio** (`rotulo.fn_enviar_sessao`): recusado se a tarefa tiver mais de 1 pixel sem classe. Onde não for possível decidir, use `indeterminado`. A partir daí as anotações ficam travadas.
5. **Revisão** (`rotulo.fn_revisar_sessao(sessao, 'revisor', aprovar, comentario)`): o revisor tem de ser outra pessoa, e só uma sessão por tarefa pode ser aprovada. A sessão aprovada é a referência.

O banco impõe as transições da sessão:

- `em_andamento → enviada → aprovada | rejeitada`;
- reabrir volta para `em_andamento`, mas é bloqueado se a sessão é referência de um dataset congelado.

## Qualidade

- `rotulo.vw_lacuna`: o que falta classificar em cada sessão em andamento.
- `rotulo.vw_concordancia`: para cada par de sessões da mesma tarefa, o **IoU por classe** e o **acordo global** (fração da área com a mesma classe). É a forma de medir a discordância da referência (lacuna L14).
- `rotulo.vw_progresso`: tarefas e área por situação.
- `auditoria.registro`: quem mudou o quê e quando, com o antes e o depois em JSON. Para identificar a pessoa, rode `SET app.usuario = 'apelido'` na conexão.

## Divisão espacial e datasets

- `treino.divisao` e `treino.bloco`: blocos de 600 m com folga de 100 m e semente 42 (`configs/pipeline.yaml`). O sorteio é determinístico (md5 da semente com a posição do bloco) e resultou em 18 blocos de treino, 6 de validação e 6 de teste. O **bloco útil** desconta a folga.
- `treino.vw_tarefa_conjunto`: dá o conjunto de cada tarefa. Uma tarefa que cruza fronteira ou folga fica como `fora_de_bloco` e não entra em dataset.
- `treino.fn_congelar_dataset(id)`: inclui toda tarefa aprovada da campanha que cabe num bloco útil e congela o dataset. Opcionalmente filtra produtos com `parametros = '{"produtos": ["global_monthly"]}'`. Depois de congelado, amostras não entram, não saem e não trocam, e a sessão de referência não pode ser reaberta. Só é permitido registrar a máscara gerada (`caminho_mascara`, `sha256_mascara`, `pixels_por_valor`).
- `treino.vw_balanco_classe`: área e porcentagem por classe em cada conjunto.

## Gerar a máscara

Para cada amostra:

1. `treino.vw_mascara_janela` dá a janela da tarefa em pixels da grade da imagem (`col_ini`, `lin_ini`, `col_fim`, `lin_fim`, com o fim exclusivo) e o valor de fundo.
2. `treino.vw_mascara_poligono` dá os polígonos com o `valor` do pixel e o `peso` da certeza.

Rasterize os polígonos na grade da imagem (`origem_x`, `pixel_x`, `origem_y`, `pixel_y` estão em `catalogo.grade`), com fundo 0. Registre o arquivo e o hash em `treino.dataset_amostra`. No treino, use `ignore_index` para 0 e para 251–255.

## QGIS

Para editar, adicione `rotulo.anotacao` e `rotulo.tarefa`. As visões servem para visualizar, e a chave de cada uma é a coluna `id`.

Na camada `rotulo.anotacao`:

- configure `classe_id`, `certeza_codigo` e `origem_codigo` como **Mapa de valores relacionados** apontando para `dominio.classe`, `dominio.nivel_certeza` e `dominio.origem_anotacao`;
- deixe `sessao_id` com valor padrão fixo durante o trabalho;
- ative a aderência e a opção **Evitar sobreposição**.

`tarefa_id` e `data_referencia` são preenchidas pelo banco: deixe-as vazias ou com qualquer valor.

## Testes executados

Em 2026-10-24 o script foi carregado num cluster PostgreSQL 18 + PostGIS temporário e `db/testes.sql` passou inteiro (42 verificações). Ficaram cobertos:

- **Carga:** as contagens da carga (179 imagens, 3 grades, 12 classes folha, 30 blocos) e a AOI válida e contida na grade.
- **Taxonomia:** as regras da árvore de classes.
- **Tarefas:** as regras de tarefa (data herdada, sobreposição, extensão).
- **Anotações:** recorte, herança de data, classe agregadora, sobreposição, lacuna e trava após o envio.
- **Concordância:** valores calculados à mão.
- **Revisão e congelamento:** a máquina de estados e a revisão, o congelamento do dataset e a janela em pixels.
- **Auditoria:** registro das alterações.

Ficou sem teste: a rasterização em Python a partir das visões. O Python do sistema não tem `rasterio`, então isso precisa ser verificado quando o ambiente do pipeline existir.

A geometria original de `Jardim_Interlagos.geojson` tem uma autointerseção; a carga a corrige com `ST_MakeValid`.
