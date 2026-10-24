---
tipo: guia
tags: [guia, chunks]
---
# Estratégia de chunks

**Objetivo:** recuperar o trecho certo (método, dados, hiperparâmetros, resultados, limitações) sem misturar contextos, tanto no Obsidian quanto em busca semântica/RAG.

## Regras usadas
1. **Fronteira por seção.** O PDF é dividido em seções por cabeçalhos (numerados, em caixa-alta ou nomes padrão). Um chunk nunca atravessa duas seções.
2. **Tipo da seção:** resumo, introdução, trabalhos relacionados, dados, métodos, experimentos, resultados, discussão, conclusão. Referências e agradecimentos são descartados.
3. **Tamanho:** alvo de ~1.700 caracteres (≈400 tokens), no máximo ~2.400, com sobreposição de ~180 caracteres. Parágrafos são preservados; parágrafos gigantes são divididos por sentença. Chunks finais < 300 caracteres são fundidos ao anterior.
4. **Limpeza:** cabeçalhos e rodapés repetidos e números de página são removidos; hifenização de fim de linha é corrigida; ligaduras são normalizadas (NFKC).
5. **Metadados por chunk:** `paper`, `secao`, `titulo_secao`, `pagina`, entidades (sensor, dataset, método, métrica, tarefa, ferramenta), `tem_hiperparametros`, `tem_numeros_resultado`.

## Onde está
- `dados/chunks/Pxx.jsonl` — formato para embeddings/RAG (um JSON por linha).
- `vault/Chunks/Pxx chunks.md` — o mesmo texto em Markdown, com âncoras `^Pxx_cNNN` para `[[Pxx chunks#^Pxx_c017]]`.

## Quais chunks usar para quê
| Necessidade | Filtro | Etapa |
|---|---|---|
| Definir produto, área de estudo e rótulos | `secao = dados` | [[E01 Inventário e catálogo]], [[E04 Rotulagem e pré-anotação]] |
| Arquitetura e entradas | `secao = métodos` | [[E07 Modelos de mudança em pares]], [[E08 Modelos de série temporal]] |
| Receita de treino | `tem_hiperparametros` | [[Receitas de treino]] |
| Números para comparar | `tem_numeros_resultado` | [[Quadro de resultados]] |
| Limitações e riscos | `secao = discussão` | todas |
| Citação curta | `secao = resumo` | README / texto |

## Limites
- Extração por regra: artigos de duas colunas podem misturar linhas; tabelas e figuras não são reconstruídas.
- Seção mal detectada cai na seção anterior. Confira o título da seção no arquivo de chunks.
- Artigos sem PDF aberto (89 de 185) só têm metadados e comentário.
