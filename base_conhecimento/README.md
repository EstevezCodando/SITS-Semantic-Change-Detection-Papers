# Base de conhecimento — mudanças da cobertura terrestre com séries Planet

Vault Obsidian gerado em 24/10/2026 a partir de 103 artigos (texto convertido em `output/pdf/`). **Autor da coleta:** Jean Michael Estevez Alvarez.
Este vault **não substitui** o anterior (`../vault/`), que permanece intacto.

## Como abrir
1. No Obsidian: *Abrir pasta como cofre* → selecione `base_conhecimento/`.
2. Abra `00_Painel/00_Inicio.md`. Os mapas ficam em `01_Mapas/`; os canvases também (`Mapa_Metodologico.canvas` é o principal).
3. As figuras selecionadas estão em `90_Anexos/figuras/`. Os PDFs e o Markdown completo ficam fora do vault (`../coleta/`, `../output/pdf/`); as notas citam o caminho.

## Estrutura
`00_Painel` início e guias · `01_Mapas` mapas de conteúdo e canvases · `02_Artigos` uma nota por artigo (103) · `03_Dados` sensores, produtos e conjuntos · `04_Preparo` etapas de preparo · `05_Metodos` algoritmos, arquiteturas, estratégias e tarefas · `06_Validacao` desenhos e métricas · `07_Resultados` matriz comparativa e sínteses · `08_Monitoramento` operação e ferramentas · `09_Lacunas` · `90_Anexos` inventário, duplicatas, original e figuras · `99_Templates`.

## Convenções
- Relações são **links no texto** com o significado ao lado (“utiliza método: …”, “emprega conjunto de dados: …”, “é avaliado por: …”).
- Artigos ligam-se entre si só quando há comparação substantiva (explicada na seção 12); o resto da conexão passa por conceitos compartilhados.
- `status_leitura`: *lido (profundo)* · *lido (parcial)* · *extraído automaticamente (não lido)*. Onde faltou informação consta “não informado”.
- **Evidência vs. interpretação:** cada nota rotula o que é fato do artigo (com página) e o que é leitura da base.

## Grafo e Canvas
Veja `00_Painel/Guia_Grafo.md` (cores por pasta, filtros, grafo local de profundidade 1–2 e forças iniciais). Canvases: cartões de 320×180, intervalos de 120 (horizontal) e 80 (vertical), cores da mesma paleta do grafo.

## Verificação
`00_Painel/Verificacao.md`: 235 notas, 3190 wikilinks, 0 links quebrados, 0 nomes duplicados, 0 órfãs. Canvases validados geometricamente; **inspeção visual pendente**.

## Regenerar
`python -I scripts/kb_extract.py .` e `python -I scripts/kb_build.py .` (a pasta `base_conhecimento/` é recriada; copie edições manuais antes).
