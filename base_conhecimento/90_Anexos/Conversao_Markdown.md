---
tipo: anexo
titulo: "Conversão dos PDFs em Markdown"
tags: [anexo]
---

# Conversão dos PDFs em Markdown

Cada PDF de `coleta/` foi convertido em `output/pdf/<documento>/` com `document.md` (texto por página, com marcadores `<!-- page: N -->`), `text.md` (texto direto), `images/` (recortes de figuras), `raster/` (imagens incorporadas), `pages.json`, `rasters.json` e `manifest.json` (hash SHA-256 do original). Esta base usa os marcadores de página para citar **(p. N)**. Fórmulas, tabelas complexas e ordem de leitura em duas colunas podem exigir conferência no PDF. Instruções: `scripts/PDF_PIPELINE.md`.

[[Inventario_Arquivos|Inventário]] · [[Indice_Figuras|Figuras selecionadas]] · [[00_Inicio|← Painel]]
