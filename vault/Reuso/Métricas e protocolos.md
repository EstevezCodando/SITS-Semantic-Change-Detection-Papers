---
tipo: reuso
tags: [reuso, metricas]
---
# Métricas e protocolos de avaliação

Do documento original (seções 12.3 e 12.4). Conceitos: [[F1]], [[IoU - mIoU]], [[Kappa]], [[SeK]], [[Estimativa de área - IC]].

## Rótulos e separação dos dados

- Rotular **áreas estáveis e mudanças reais**, com exemplos difíceis: sombras, variação hídrica, mosaicos desalinhados, solo arenoso, telhados claros e vegetação sazonal.
- Separar treino/validação/teste por blocos geográficos; evitar patches vizinhos ou sobrepostos entre os conjuntos.
- Reservar períodos posteriores para teste temporal, além do teste espacial. Documentar se o teste envolve simultaneamente outro produto ou resolução.
- Rotular a transição com imagem anterior e posterior válidas; incluir intervalo de incerteza quando houver nuvens ou composição temporal ampla.
- Distinguir avaliação retrospectiva, que pode usar meses futuros, de alerta operacional, que só pode usar o passado disponível. Comparar os dois regimes separadamente.
- Se usar pseudorrótulos de outro mapa/modelo, construir amostra final independente com interpretação especializada e, quando possível, imagens de maior resolução ou campo.

## Métricas mínimas

| Dimensão | Avaliação recomendada |
|---|---|
| Mudança/não mudança | Precisão, recall, F1, IoU e curva precisão–recall |
| Tipo de transição | Matriz de confusão from–to, F1 por transição e macro-F1 |
| Cobertura em cada mês | IoU/F1 por classe, separadas das métricas de mudança |
| Edificações | Precisão/recall por objeto e faixa de tamanho; associação temporal de identidades |
| Vias | Sobreposição, continuidade/conectividade e erros de rede; não apenas área de pixels |
| Data | Erro ou compatibilidade com intervalo de ocorrência; atraso do alerta operacional |
| Área alterada | Área mapeada e estimativa amostral com intervalo de confiança, sem confundi-las |
| Transferência | Resultados por ano, região, resolução, produto e qualidade da observação |
| Uso operacional | Falsos alertas por km²/mês, tempo de revisão e tempo de processamento |

Não comparar F1 publicado de LEVIR-CD, SECOND, SpaceNet 7 e desmatamento como se fossem medidos na mesma tarefa. Classes, resoluções, prevalência de mudança, referência e divisão dos dados são diferentes. Acurácia global alta pode esconder baixa detecção de eventos raros.
