---
tipo: reuso
tags: [reuso, taxonomia]
---
# Taxonomia inicial de transições

Copiada do documento original (seção 11). Proposta a validar com amostras locais.

As classes abaixo são uma proposta a validar por interpretação de amostras locais. **Cobertura física, uso do solo e processo de transformação são conceitos diferentes.** Uma imagem pode mostrar solo exposto sem determinar se é terraplenagem, mineração ou outra atividade.

| Transição observável | Evento candidato | O que precisa ser confirmado |
|---|---|---|
| Vegetação arbórea → solo exposto | Supressão de cobertura arbórea | Persistência, exclusão de sombra/nuvem e sazonalidade |
| Vegetação arbórea → vegetação baixa | Perda parcial ou mudança de estrutura | Separar degradação, manejo e erro de classificação |
| Vegetação baixa → solo exposto | Remoção de cobertura rasteira | Separar cultivo, seca e preparo do terreno |
| Solo exposto → cobertura edificada | Nova construção | Tamanho detectável e estabilidade em observações seguintes |
| Vegetação → cobertura edificada | Conversão direta aparente | Pode haver etapa de solo exposto não observada |
| Solo/vegetação → estrutura linear viária | Nova via ou acesso | Continuidade, largura e conexão com a rede |
| Via não pavimentada → superfície pavimentada | Pavimentação candidata | Pode ser espectralmente ambígua em 3–5 m |
| Edificação → solo exposto | Remoção/demolição candidata | Excluir sombra, cobertura por nuvem e desalinhamento |
| Solo exposto → vegetação persistente | Revegetação/regeneração candidata | Distinguir crescimento sazonal e recuperação duradoura |
| Água → solo/vegetação, ou inverso | Mudança hídrica/inundação/retração | Sazonalidade, maré e contexto hidrológico |
| Qualquer classe → observação inválida | Sem conclusão | Não registrar como alteração territorial |

**Saída mínima por evento:** identificador, geometria, classe anterior, classe posterior, intervalo temporal, área, resolução/produto, número de observações válidas, confiança avaliada, referências às imagens e estado de revisão humana.

Supressão, construção e abertura de via podem ser etapas do mesmo processo. Guardar eventos encadeados e evitar contabilizar repetidamente a mesma área como nova conversão independente. Legalidade, finalidade e responsabilidade não são classes diretamente observáveis no mosaico.

Etapa: [[E09 Pós-processamento e eventos]] · Avaliação: [[E10 Avaliação e incerteza]]
