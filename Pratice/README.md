# Pratice — mudanças de cobertura com Planet de ~5 m

Pipeline para **identificar automaticamente alterações da cobertura do solo** (início de construções, supressão da vegetação, vias e outras) em imagens ópticas Planet de ~5 m, gerando **vetores com atributos de especificação e de confiabilidade** para cada delta entre meses e um **consolidado por ano**. Depois do modelo treinado, o objetivo é baixar uma imagem nova e obter o delta sem treinar de novo.

Esta pasta guarda o **contexto** e as **skills** para construir isso com Claude Code. Abra uma sessão **dentro desta pasta**: o `CLAUDE.md` e as skills de `.claude/skills/` são carregados automaticamente.

## Leia nesta ordem

1. [`CLAUDE.md`](CLAUDE.md): objetivo, dados, restrições, convenções e lista de skills.
2. [`docs/dados.md`](docs/dados.md): o que há em `D:\PT2-build\Imagens de Satelite` e o que isso permite.
3. [`docs/arquitetura_pipeline.md`](docs/arquitetura_pipeline.md): etapas S0 a S8, modos de execução e decisões.
4. [`docs/esquema_vetores.md`](docs/esquema_vetores.md): atributos dos vetores, confiança e consolidação.
5. [`docs/metodos_e_experimentos.md`](docs/metodos_e_experimentos.md): métodos candidatos e protocolo de comparação.
6. [`docs/roteiro.md`](docs/roteiro.md): fases e primeira sessão sugerida.
7. [`docs/conhecimento.md`](docs/conhecimento.md): mapa para a base de conhecimento (`..\base_conhecimento`).

## Skills

Em `.claude/skills/`, uma por etapa: `inventario-dados`, `rotulagem-referencia`, `baselines-mudanca`, `treino-modelos`, `avaliacao-comparacao`, `vetorizacao-confianca`, `inferencia-nova-imagem`, `registro-experimentos`, `consulta-conhecimento`. Cada uma traz objetivo, passos, trechos de código de partida, armadilhas e critérios de pronto.

## Configuração

`configs/pipeline.yaml` (caminhos, grade, divisão, método, confiança), `configs/classes.yaml` (taxonomia) e `configs/esquema_vetor.yaml` (esquema legível por máquina dos vetores).

## Estado

| Item | Situação |
|---|---|
| Dados | prontos (somente leitura, fora do repositório); inventário e QC ainda não rodados |
| Rótulos | **não existem**: primeira tarefa |
| Ambiente | `rasterio` e `geopandas` presentes; **PyTorch ainda não instalado**; GPU GTX 1650 de 4 GB |
| Código (`src/`) | a criar; as skills têm modelos de partida (os trechos de `baselines`, `avaliacao` e `vetorizacao` foram executados em dados de teste; os de PyTorch ainda não) |

## Cuidados

- O arquivo `.env` da pasta de imagens contém uma chave de API: **não ler, copiar nem versionar**. Use `PL_API_KEY` do ambiente.
- Nenhum resultado da literatura é meta de desempenho aqui: os valores são de outros dados e resoluções.
- Dados, modelos e execuções ficam fora do git (ver `.gitignore`).
