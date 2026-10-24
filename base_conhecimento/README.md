# Base de conhecimento — mudanças da cobertura terrestre com séries Planet

Vault Obsidian gerado em 24/10/2026. **Autor da coleta:** Jean Michael Estevez Alvarez. Tem nota para os 41 artigos lidos (texto convertido em `../output/pdf/`); os demais textos estão em `00_Painel/Pendencias_Leitura.md`.

## Como abrir
1. No Obsidian: *Abrir pasta como cofre* → selecione `base_conhecimento/`.
2. Abra `00_Painel/00_Inicio.md` e depois `01_Mapas/Trilha_Objetivo_Planet5m.md`.
3. As figuras (uma por artigo de relevância A ou B) estão em `90_Anexos/figuras/`. Os PDFs e o Markdown completo ficam fora do vault (`../coleta/`, `../output/pdf/`); as notas citam o caminho.

## Estrutura
`00_Painel` início, guias e pendências · `01_Mapas` trilha e canvases · `02_Artigos` uma nota por artigo lido (41) · `03_Dados`, `04_Preparo`, `05_Metodos`, `06_Validacao`, `08_Monitoramento` conceitos do projeto · `07_Resultados` matriz comparativa, achados e sínteses · `09_Lacunas` · `90_Anexos/figuras` · `99_Templates`.

## Convenções
- Relações são **links no texto** com o significado ao lado (“utiliza método: …”, “emprega conjunto de dados: …”).
- `relevancia_objetivo` (A–C) e `status_leitura` estão no YAML de cada artigo; A e B formam o núcleo para o objetivo (Planet de ~5 m).
- **Evidência vs. interpretação:** cada nota rotula o que é fato do artigo (com página) e o que é leitura da base.

## Grafo
Veja `00_Painel/Guia_Grafo.md` (cores por relevância, filtros e visões prontas).

## Verificação
`00_Painel/Verificacao.md`: 118 notas, 1287 wikilinks, 0 links quebrados, 0 nomes duplicados, 0 órfãs. Canvases validados geometricamente; **inspeção visual pendente**.

## Regenerar
`python -I scripts/kb_extract.py .` e `python -I scripts/kb_build.py .` (a pasta `base_conhecimento/` é recriada; copie edições manuais antes).
