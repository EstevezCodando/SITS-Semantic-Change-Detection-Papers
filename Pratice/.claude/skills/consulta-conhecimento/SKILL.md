---
name: consulta-conhecimento
description: Consultar a base de conhecimento (artigos lidos, conceitos, lacunas, fichas) para fundamentar uma decisão do pipeline e citar com página, sem comparar métricas entre bases diferentes. Use antes de escolher método, parâmetro, métrica ou desenho de validação, e ao escrever relatórios.
---

# Consulta ao conhecimento acumulado

A base fica fora desta pasta, em `..\base_conhecimento` (Obsidian, 41 artigos lidos, conceitos do projeto, 14 lacunas), com fichas em `..\dados\leitura_profunda\Pxx.md` e o texto integral convertido em `..\output\pdf\<artigo>\document.md` (marcadores `<!-- page: N -->`).

## Como procurar

1. **Pela etapa**: abra `..\base_conhecimento\01_Mapas\Trilha_Objetivo_Planet5m.md` (etapas, artigos e resultados) e `docs/conhecimento.md` (mapa por etapa).
2. **Pelo conceito**: `..\base_conhecimento\04_Preparo`, `05_Metodos`, `06_Validacao`, `08_Monitoramento` (cada conceito traz a tabela dos artigos que o usam, com páginas).
3. **Pela lacuna**: `..\base_conhecimento\09_Lacunas\00_Sintese_Lacunas.md` diz o que a literatura **não** resolve.
4. **Por termo**: busque com a ferramenta de busca nas fichas e notas (por exemplo, `persist`, `NICFI`, `calibr`, `active learning`).
5. **Para conferir um número**: ache a nota do artigo, abra a ficha, vá à página citada em `output/pdf/.../document.md` (procure o marcador `<!-- page: N -->`). Se a ficha disser "não verificado", **não** cite o número como fato.

## Como citar

- `Autor Ano, p. N` para cada afirmação sobre um artigo; seção (§) se não houver página; "não informado" quando o texto não traz.
- Diga se o valor é o **relatado pelo estudo** (dado e escala dele) e **não compare** com resultados de outras bases ou resoluções (lacuna L06).
- Separe **evidência** (do artigo) de **interpretação** (nossa) com rótulos explícitos.
- Se a ficha foi de **leitura parcial**, diga (as fichas trazem o campo `leitura`).

## Níveis de relevância (campo `relevancia_objetivo`)

| Nível | Significado |
|---|---|
| A | Planet de 3–5 m e alvo próximo, texto lido |
| B | método, validação ou alerta transferível, texto lido |
| C | contexto, revisão ou ferramenta |

Para o objetivo do projeto, comece por A e B. Os 56 textos convertidos não lidos estão em `..\base_conhecimento\00_Painel\Pendencias_Leitura.md`, com pontuação de triagem (não é avaliação).

## O que a base **não** responde

Veja o fim de `docs/conhecimento.md`: desempenho em RGB visual de 8 bits sem NIR, desempenho nesta AOI, calibração de confiança de polígonos e custo real de rotulagem aqui.

## Acrescentar conhecimento novo

1. Leia o texto integral (`output/pdf`) e escreva a ficha em `..\dados\leitura_profunda\Pxx.md` no formato das existentes (pergunta, dados, método, métricas, limites, reaproveitamento, cuidados; páginas em cada afirmação).
2. Inclua o artigo em `scripts/kb_content2.py` (`RELEV`, `MATRIX_A`) e regenere a base com `python -I scripts/kb_build.py .` na raiz do repositório.
3. Confirme em `base_conhecimento/00_Painel/Verificacao.md`: 0 links quebrados, 0 órfãs.
4. Commit.

## Armadilhas

- Citar resultado de um artigo como meta de desempenho nossa.
- Usar número de uma ficha de leitura parcial sem checar a página.
- Esquecer que a base é só de Planet e de estudos até 2026; não cobre outros sensores com profundidade.
