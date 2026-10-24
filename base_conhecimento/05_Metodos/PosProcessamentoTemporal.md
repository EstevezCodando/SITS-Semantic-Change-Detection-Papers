---
tipo: conceito
subtipo: "método"
titulo: "Pós-processamento temporal (persistência, janela e colapso)"
aliases: ["Pós-processamento temporal (persistência, janela e colapso)"]
pasta_tematica: "05_Metodos"
n_artigos: 6
tags: [conceito, metodo]
---

# Pós-processamento temporal (persistência, janela e colapso)

**Natureza:** método. A base distingue algoritmo, arquitetura, ferramenta, tarefa, etapa metodológica, dado e desenho de validação por este campo.

> *Definição, pressupostos e limitações* abaixo são **interpretação/conhecimento geral da base**, salvo onde há token de página. Os fatos dos artigos estão na tabela de evidências.

## Definição

Regras sobre a série de mapas por data para eliminar mudanças efêmeras e datar o evento: persistência em N ou mais observações, voto de maioria em janela deslizante ou colapso temporal.

## Finalidade

Transformar mapas por data em eventos de mudança confiáveis.

## Entradas

Mapas ou probabilidades por data e máscaras de qualidade.

## Saídas

Mapa de eventos com data estimada.

## Pressupostos

A mudança real persiste por algumas datas e os falsos positivos são efêmeros.

## Limitações

Aumenta a latência (3 meses em P91, até um trimestre em P103) e remove mudanças reais curtas ou em áreas muito nubladas.

## Evidência nos artigos lidos

| Artigo | Relação | Ocorrências | Páginas | Status de leitura |
|---|---|---:|---|---|
| [[Carter_2024_DetectionForestDisturbance\|Carter 2024]] | referência (curado pela leitura) | — | ver nota do artigo | lido (profundo) |
| [[Glazer_2025_TEMPOGlobalTemporal\|Glazer 2025]] | referencia (suporte manual da leitura) | — | ver nota do artigo | lido (profundo) |
| [[Etten_2021_SpaceNetMultiTemporal\|Etten 2021]] | referencia (suporte manual da leitura) | — | ver nota do artigo | lido (profundo) |
| [[Reiche_2021_ForestDisturbanceAlerts\|Reiche 2021]] | referencia (suporte manual da leitura) | — | ver nota do artigo | lido (parcial) |
| [[Ygorra_2024_NearRealTime\|Ygorra 2024]] | referencia (suporte manual da leitura) | — | ver nota do artigo | lido (parcial) |
| [[Zhang_2023_MonitoringMonthlyTropical\|Zhang 2023]] | referencia (suporte manual da leitura) | — | ver nota do artigo | lido (profundo) |

## Navegação

- Mapa: [[MOC_07_MudancaSeries|Detecção de mudanças e séries temporais]]
- Mapa: [[MOC_10_MonitoramentoOperacao|Monitoramento contínuo e operação]]
