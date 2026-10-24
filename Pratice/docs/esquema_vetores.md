# Esquema dos vetores de mudança

Cada alteração detectada é um **polígono** com atributos de especificação e de confiabilidade. Versão legível por máquina: `configs/esquema_vetor.yaml`. Nomes em português, `snake_case`, sem acento.

## Saídas

Um GeoPackage por nível, em EPSG:32723 (e uma cópia em EPSG:4326 opcional para publicação):

| Arquivo | Camada | Conteúdo |
|---|---|---|
| `delta_AAAA-MM.gpkg` | `mudancas` | alterações entre o mosaico do mês anterior e o do mês `AAAA-MM` |
| `delta_AAAA-MM.gpkg` | `qualidade` | polígonos de nuvem, sombra, borda de mosaico e sem dado do par (para auditoria) |
| `consolidado_AAAA.gpkg` | `eventos` | eventos do ano, fundidos entre meses, sem duplicar |
| `consolidado_AAAA.gpkg` | `resumo` | tabela: área por tipo de alteração e por classe de confiança |
| `consolidado_AAAA.gpkg` | `mudancas_mensais` | as mudanças mensais que formaram cada evento (rastreabilidade) |

Um `manifesto.json` por execução registra versões, configuração, imagens usadas (arquivo e hash) e contagens.

## Atributos de `mudancas` (delta mensal)

| Atributo | Tipo | Descrição |
|---|---|---|
| `id_mudanca` | texto | identificador estável: hash de (mês, geometria arredondada) |
| `id_evento` | texto | evento ao qual pertence (ligação com o consolidado) |
| `mes_ini` / `mes_fim` | texto `AAAA-MM` | mosaicos comparados (anterior e atual) |
| `imagem_ini` / `imagem_fim` | texto | arquivos usados (caminho relativo) |
| `tipo_alteracao` | texto (domínio) | `supressao_vegetacao_arborea`, `supressao_vegetacao_rasteira`, `inicio_construcao`, `edificacao_nova`, `abertura_via`, `ampliacao_via`, `solo_exposto_movimentacao`, `mineracao`, `outra` |
| `classe_de` / `classe_para` | texto (domínio de `classes.yaml`) | cobertura antes e depois |
| `estagio` | texto | `novo`, `em_expansao`, `consolidado`, `revertido` (por exemplo, rebrota) |
| `area_m2` / `area_ha` | número | área do polígono |
| `perimetro_m` | número | perímetro |
| `compacidade` | número | 4πA/P² (1 = círculo; vias têm valores baixos) |
| `largura_media_m` | número | só para vias: 2A/P aproximado |
| `confianca` | número 0–1 | probabilidade calibrada de a alteração ser real e do tipo informado |
| `classe_confianca` | texto | `alta`, `media`, `baixa`, `provisoria` |
| `conf_modelo` | número 0–1 | probabilidade média calibrada do detector dentro do polígono |
| `conf_persistencia` | número 0–1 | fração das observações seguintes (até 3) que confirmam a mudança |
| `n_obs_confirma` / `n_obs_disponiveis` | inteiro | quantos meses seguintes confirmam e quantos existem |
| `conf_qualidade` | número 0–1 | 1 menos a fração de pixels com nuvem, sombra, borda ou baixa qualidade |
| `conf_concordancia` | número 0–1 | concordância (IoU) com um segundo método independente |
| `conf_tamanho` | número 0–1 | penaliza áreas próximas do limite de detecção (`area_min_m2` em `pipeline.yaml`) |
| `flag_nuvem`, `flag_sombra`, `flag_borda_mosaico`, `flag_registro`, `flag_sazonal`, `flag_radiometria` | booleano | riscos de pseudomudança |
| `modelo_id` / `versao_pipeline` / `run_id` | texto | rastreabilidade |
| `resolucao_m` | número | resolução da grade usada |
| `status_revisao` | texto | `nao_revisado`, `confirmado`, `rejeitado` |
| `revisor` / `data_revisao` | texto | preenchidos na revisão humana |

## Atributos extras de `eventos` (consolidado anual)

| Atributo | Descrição |
|---|---|
| `id_evento` | identificador do evento (primeiro mês + hash) |
| `ano` | ano de consolidação |
| `mes_primeira_deteccao` / `mes_ultima_deteccao` | primeiro e último mês em que o evento aparece |
| `n_meses_ativo` | quantos meses o evento teve atividade |
| `area_final_m2` | área da geometria fundida |
| `crescimento_m2` | área ganha entre a primeira e a última detecção |
| `tipo_alteracao`, `classe_de`, `classe_para` | decididos por voto ponderado pela confiança mensal; `classe_para` usa o mês mais recente |
| `confianca_anual`, `classe_confianca` | combinação da confiança mensal máxima, da persistência ao longo do ano e da concordância com a comparação anual direta |
| `conf_comparacao_anual` | concordância com a diferença direta entre os compostos do fim do ano anterior e do fim do ano |
| `n_mudancas_mensais` | quantas mudanças mensais formaram o evento |

## Como a confiança é composta (proposta, a calibrar)

Componentes em [0, 1] listados acima. A combinação é **aprendida**, não escolhida à mão:

1. Em um conjunto de referência (eventos reais, eventos rejeitados e áreas estáveis), ajuste uma regressão logística sobre os componentes (com `tipo_alteracao` como variável adicional se houver dados).
2. Calibre a saída com regressão isotônica em um conjunto separado do de ajuste.
3. Defina as classes por **meta de precisão medida**, por exemplo `alta` = menor limiar cuja precisão na validação seja ≥ 0,90; `media` ≥ 0,70; o restante `baixa`. Os valores 0,90 e 0,70 são pontos de partida do projeto, não resultados da literatura.
4. Mudanças ainda sem os 3 meses seguintes recebem `classe_confianca = provisoria` e `conf_persistencia` nulo. Elas **são emitidas** (latência mínima) e **reclassificadas** quando a confirmação chega, mantendo o `id_mudanca`.
5. Publique o diagrama de confiabilidade (confiança prevista × precisão observada) e o erro de calibração esperado (ECE) junto com cada versão do modelo.

Fundamento na literatura lida (valores relatados em cada estudo): confirmação por persistência de ≥ 3 observações (Zhang 2023, p. 13; Ygorra 2024, p. 10), níveis de confiança baixa/alta/mais alta por concordância entre sistemas (Reiche 2024, p. 7–8), atualização bayesiana com limiares de 0,85 e 0,975 (Reiche 2021, p. 5) e clareza do pixel pela máscara de qualidade (Glazer 2025, p. 7–8).

## Regras de consistência

- Geometrias válidas, polígonos simples, sem sobreposição dentro do mesmo mês; vazios fechados quando menores que `area_min_m2`.
- Nada fora da máscara da AOI e nada sobre pixels com alfa 0 em qualquer das duas datas.
- `classe_de` ≠ `classe_para`, exceto `estagio = em_expansao` (mesma transição, área crescendo).
- Um evento nunca perde histórico: o consolidado referencia as mudanças mensais que o formaram.
- Rodar a mesma execução duas vezes com a mesma configuração produz os mesmos identificadores.
