# Métodos candidatos e plano de comparação

Objetivo: testar os melhores métodos para mudança de cobertura em Planet de ~5 m (visual RGB), analisar e comparar. As fontes citadas estão na base de conhecimento (`..\base_conhecimento\`); os valores são os **relatados por cada estudo**, em dados diferentes dos nossos, e **não são expectativa de desempenho aqui**.

## Famílias de método

| Id | Método | Precisa de rótulo? | GPU 4 GB? | Fonte na base | Hipótese e risco |
|---|---|---|---|---|---|
| M0 | Diferença de imagens + limiar (e vetor de mudança) | não | não | Shafique 2022 (revisão) | Linha de base trivial; sensível a radiometria; serve de piso |
| M1 | **Hue referenciado à vizinhança + persistência ≥ 3 meses** | não (calibrar limiar com poucos eventos) | não | Zhang 2023 (p. 9–13) | Bom para supressão arbórea; Hue só vê cor; falha em solo claro, sombra e sazonalidade; latência de 3 meses |
| M2 | Classificação de cobertura por data (U-Net) + **diferença de mapas** (pós-classificação) | sim (cobertura por data) | sim, modelo pequeno | Wagner 2023, Carter 2024, Zaraza-Aguilera 2022 | Erros somam-se nas duas datas; não vê mudança entre datas; bom para de→para |
| M3 | **U-Net bitemporal** (par de meses empilhado em 6 canais, ou siamesa) | sim (mudança) | sim | Wang 2024, Daudt 2019, Metzger 2023 | Direto e simples; precisa de rótulos de mudança e de cuidado com a divisão (Wang 2024 usou divisão aleatória) |
| M4 | **Mudança semântica bitemporal** (de→para) com decodificadores semânticos | sim (de→para) | sim | Yang 2020 (ASN), Daudt 2019, Shen 2026 (referência) | Taxonomia grande, transições raras; pouca amostra por par de classes |
| M5 | **Série temporal** (U-TAE, ConvLSTM) com saída por data | sim | limitado | Vincent 2024, Toker 2022 | Usa o histórico; pode ficar próximo do acaso com poucos dados (MUDS); custo de memória |
| M6 | Pré-treino em dados abertos de mudança em Planet (SpaceNet 7/MUDS, DynamicEarthNet) e ajuste fino local | sim (local, poucos) | sim | Metzger 2023 (pré-treino em mudança supera ImageNet em 2–3 pontos de F1), Etten 2021 | Mitiga a falta de rótulos; precisa baixar e alinhar os dados |
| M7 | Modelo fundacional congelado + ramo de mudança treinável | sim, poucos | não (nuvem) | Li 2024 (BAN), Shen 2026 | Só RGB bitemporal testado; não validado em 3–5 m; custo |
| M8 | **Pós-processamento temporal** sobre qualquer detector: persistência, janela de 4 datas, colapso temporal, integração com um 2º método | não | não | Zhang 2023, Etten 2021 (p. 8–9), Glazer 2025 (p. 7–8), Reiche 2024 | No SpaceNet 7 foi o que mais pesou; custo em latência |

Sugestão de ordem: M0 → M1 → M3 (+M8) → M2 → M6 → M5 → M4 → M7. Não passe adiante sem a avaliação do anterior.

## Dimensões da comparação

| Dimensão | Como fazer |
|---|---|
| Mesmo dado, mesma divisão | blocos espaciais com folga + período final reservado; as mesmas semente, tamanho de recorte e reamostragem |
| Mesmo orçamento | mesmas tentativas de ajuste de hiperparâmetros por método (por exemplo, 10), mesmas épocas máximas, parada pelo mesmo critério |
| Repetição | ≥ 3 sementes por método de aprendizado; reporte média e desvio |
| Pixel | F1 e IoU da classe de mudança (nunca acurácia global) |
| Evento | precisão e recall de **eventos** (IoU ≥ 0,25 com a referência, como no SpaceNet 7); mês de início detectado vs real |
| Tamanho | recall por faixa de área (< 4 px, 4–16 px, 16–64 px, > 64 px) para achar o limite de detecção |
| Tipo | métricas por `tipo_alteracao` |
| Falso alarme | taxa por km² e por mês em **áreas estáveis de controle**; separa ruído radiométrico de erro de modelo |
| Latência | meses até a detecção confirmada e fração `provisoria` que vira falso positivo |
| Confiança | diagrama de confiabilidade, ECE e precisão por classe de confiança |
| Área | estimativa de área por amostragem estratificada com intervalo de confiança (Olofsson 2014; Zhang 2023) |
| Robustez | desempenho sob troca de família de mosaico, de ano e de bloco; teste de desfoque e ruído (Chen 2024, p. 17) |
| Custo | tempo de treino, memória de GPU, tempo por mosaico |

## Como relatar

- Uma tabela por **tarefa** (supressão arbórea, edificação, via, geral), nunca misturando divisões.
- Cada linha traz método, versão dos dados, divisão, semente, métricas e custos; o registro está em `runs/` (skill `registro-experimentos`).
- Escrever o que **não** se pode concluir (uma AOI, rótulos feitos por nós, só RGB).
- Mapas de erro (falso positivo, falso negativo) por mês para os melhores métodos e para um exemplo de falha de cada.

## O que a literatura ainda não resolve (nossas hipóteses a testar)

| Lacuna (base) | Teste proposto |
|---|---|
| L11: início de construção em ~5 m tem escore baixo | medir recall de eventos por faixa de tamanho e mês de início; testar M8 com janela de 3 a 4 meses |
| L12: supressão de vegetação sem comparação entre famílias | M1 vs M2 vs M3 na mesma referência e divisão |
| L13/L14: divisão aleatória e referência visual frágil | divisão por blocos + registro da concordância entre intérpretes |
| L01: operação contínua | modo `incremental` simulado: só o passado disponível, medir latência e falsos alertas |
| L02: cadência dos mosaicos | comparar `global_monthly` e `medres_normalized` em áreas estáveis |
