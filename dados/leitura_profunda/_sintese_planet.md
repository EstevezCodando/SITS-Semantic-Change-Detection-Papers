---
titulo: Síntese — cuidados específicos com produtos Planet
etapas: [E01, E02]
---
# Cuidados específicos com produtos Planet

| Tema | O que os artigos mostram | Fonte |
|---|---|---|
| **Cadência do NICFI** | semestral de dez/2015 a ago/2020 e mensal a partir de set/2020; um estudo de 2018–2019 teve só **um composto de 6 meses** | [[P01 Wagner 2023]], [[P07 Vizzari 2022]] |
| **Radiometria** | a reflectância absoluta não é garantida; há variação entre satélites, datas e dentro da mesma imagem; funcionou com escala simples para 8 bits e sem correção atmosférica | [[P01 Wagner 2023]] |
| **Bandas** | 4 bandas (RGB+NIR) em NICFI/PlanetScope; MUDS é RGB visual; NDVI **não ajudou** como entrada extra | [[P10 Etten 2021]], [[P05 Zaraza-Aguilera 2022]] |
| **Georreferenciamento** | desvios de 5–10 m em cenas de mosaicos mensais; > 1 px entra na máscara UDM; bordas e rios viram falsa mudança | [[P10 Etten 2021]], [[P01 Wagner 2023]] |
| **Nuvem e sombra** | mosaicos mensais são "mais ou menos livres de nuvem"; há resíduos; a pós-classificação superestima a mudança com nuvem | [[P01 Wagner 2023]], [[P05 Zaraza-Aguilera 2022]] |
| **Planet Fusion não é mosaico mensal** | diário, gap-filled, calibrado ao HLS; resultados não transferem diretamente | [[P12 Toker 2022]] |
| **Composição temporal** | o composto mistura datas; atrasa a data da mudança em filtros de ±3 datas | [[P01 Wagner 2023]] |
| **Resolução** | 3 m e 5 m não são intercambiáveis; objetos de 4–5 px já dão F1 ~0,45 | [[P10 Etten 2021]] |
| **Textura vs. espectro** | OB + GLCM compensa o espectro limitado de 4 bandas: OA 66,7 % (PB) → 82,2 % (OB) | [[P07 Vizzari 2022]] |

## Checklist antes de rodar o modelo (para [[E02 Qualidade e harmonização]])
1. Confirmar produto (visual RGB × analítico), bandas e cadência real em cada arquivo.
2. Medir deslocamento entre meses em alvos estáveis; mascarar > 1 px.
3. Gerar máscara de observação válida (nuvem, sombra, emendas, sem dado).
4. Definir a normalização (escala 8 bits ou reflectância) e registrá-la no `image_asset`.
5. Decidir a grade comum (3 m × 5 m) sem criar detalhe artificial; resultados separados por produto.
