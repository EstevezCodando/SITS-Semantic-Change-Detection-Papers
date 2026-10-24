---
titulo: Síntese — protocolos de rotulagem comparados
etapas: [E04, E03]
---
# Protocolos de rotulagem comparados

Resumo do que cada artigo de leitura profunda fez para obter rótulos, com a lição transferível para mosaicos mensais Planet de 3–5 m.

| Artigo | Unidade de rótulo | Como foi feito | Custo/equipe | Lição transferível |
|---|---|---|---|---|
| [[P01 Wagner 2023]] | máscara floresta / não-floresta em patches 256 × 256 | auto-segmentação por textura (k-textures, 8 classes) + escolha das classes de floresta + correção manual + amostras de nuvem e neblina | "um par de dias" | começar por segmentação não supervisionada e só escolher classes; incluir exemplos de nuvem como não-floresta |
| [[P10 Etten 2021]] | polígono de edificação com ID persistente | anotar a 1ª imagem; copiar para a seguinte e editar só com confiança; revisão cruzada; apoio de mapa de alta resolução | 7 meses, 5 pessoas | exclusão de efêmeros pela série; UDM para nuvem e co-registro |
| [[P12 Toker 2022]] | mapa de 7 classes no dia 1 de cada mês | 1ª imagem manual; mapas seguintes atualizados só quando a mudança é evidente; 3 portões de qualidade | não informado | rótulo temporalmente consistente, QC por três anotadores |
| [[P18 Daudt 2019]] | pares de mapas de cobertura (Urban Atlas) + mapa de mudança | rasterização de vetores oficiais de 2006 e 2012 | automático | barato e em escala, mas ruidoso (80–85 %) e com bordas de parcela inteira |
| [[P19 Yang 2021]] | par de mapas de cobertura + máscara de não-mudança | grupo de especialistas em visão da Terra | não informado | permite mudança dentro da mesma classe; 6 classes → 30 tipos |
| [[P05 Zaraza-Aguilera 2022]] | polígonos mineração / não mineração em 3 datas | vetores existentes + blocos 1,6 km com folga | não informado | usar vetores por data e derivar mudança por pares |
| [[P07 Vizzari 2022]] | 2.400 pontos de 7 classes | ≈850 do Brazil Data Cube + pontos no QGIS (AcATaMa) sobre Bing/Google/Planet | não informado | amostra pontual barata, mas pontos independentes são necessários para teste justo |

## Padrão que se repete
1. **Rótulo inicial na primeira data** e atualização apenas quando há evidência (P10, P12).
2. **Uma camada de dado inválido** (nuvem, sombra, erro de georreferenciamento) separada do rótulo (P10 UDM; P01 trust; P12 QC).
3. **Referência de maior resolução ou independente** ao menos na validação (P10 mapa privado; P01 LiDAR; P46).
4. **Auto-segmentação ou pré-anotação** para acelerar, com revisão humana (P01 k-textures).
5. **Rótulos de mapas oficiais** são baratos e em escala, mas têm ruído e bordas imprecisas (P18).

## Como usar no projeto
- Combina com [[E04 Rotulagem e pré-anotação]]: pré-anotar (SAM/YOLO/k-textures), revisar na série inteira e guardar a origem.
- Combina com o formato `mapa antes + mapa depois + máscara de não-mudança` de [[P19 Yang 2021]].
- Medir tempo por evento confirmado com e sem pré-anotação (ver [[EXP6 Pré-anotação assistida (SAM-YOLO-QGIS)]]).
