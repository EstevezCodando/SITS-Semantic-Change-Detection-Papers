---
name: inferencia-nova-imagem
description: Rodar o pipeline já treinado sobre uma imagem nova (baixada depois) para obter o delta de alterações em relação aos meses anteriores, reclassificar mudanças provisórias e atualizar o consolidado anual. Use na operação, ao testar o modo incremental ou ao validar que uma imagem nova pode entrar no pipeline.
---

# Inferência sobre uma imagem nova

Modo `incremental` de `docs/arquitetura_pipeline.md`: **sem treinar de novo**, a imagem nova passa pelo mesmo caminho dos dados de treino e gera os vetores do delta. Contrato de saída: `docs/esquema_vetores.md`.

## Entradas

- A imagem nova (GeoTIFF de 4 bandas RGB + alfa, na grade da fonte principal), ou o mosaico do mês seguinte baixado pela pipeline em `D:\PT2-build\Imagens de Satelite\pipeline\` (`p02_baixar_mosaicos_existentes.py`; a chave da Planet vem de `PL_API_KEY`, **nunca** do arquivo `.env` lido por este projeto).
- O modelo e a calibração versionados (`models/<modelo_id>/` com pesos, `config.yaml`, limiares, calibração e hash dos dados de treino).
- A série anterior (pelo menos os 3 meses anteriores, para a confirmação).

## Passos

1. **Admissão (S0):** recuse a imagem se: CRS ou grade diferentes da fonte; sem alfa; cobertura válida da AOI abaixo do mínimo (`qc`: sugerido 95%); nuvem/névoa acima do limite; hash já registrado (duplicata); data fora de sequência. Registre o motivo em `runs/incremental/<mes>/qc.json`.
2. **Harmonização (S1):** mesma normalização ajustada no treino (parâmetros do modelo, **não reajustados com a imagem nova**); máscara de qualidade.
3. **Escolher o par:** mês anterior válido mais próximo; se o anterior estiver ruim, use o último válido e registre o intervalo (a mudança passa a cobrir mais de um mês).
4. **Detecção (S3) e pós-processamento (S4):** probabilidade de mudança do par; segundo método (`baseline_hue`) para concordância; vetorização (S5).
5. **Confiança (S6):** componentes e calibração do modelo; mudanças do mês novo saem `provisoria`.
6. **Reclassificar** as mudanças dos 3 meses anteriores: a imagem nova fornece a observação de confirmação; recalcule `conf_persistencia`, `confianca` e `classe_confianca` mantendo `id_mudanca`; marque `estagio = revertido` quando a mudança desaparecer.
7. **Consolidado do ano corrente (S7):** atualize `consolidado_AAAA.gpkg`; no início do ano, feche o consolidado do ano anterior com a comparação anual direta.
8. **Saída e auditoria:** `delta_AAAA-MM.gpkg` (camadas `mudancas` e `qualidade`), manifesto, mapa de síntese, tabela por tipo e classe de confiança, lista das mudanças que mudaram de classe.

## Comando-alvo (a implementar em `src/mudanca/cli.py`)

```bash
python -m mudanca incremental --imagem <arquivo.tif> --mes 2026-10 --modelo <modelo_id> --config configs/pipeline.yaml
```

Saída em `runs/incremental/2026-10/`. A execução deve ser **idempotente**: repetir o comando gera os mesmos identificadores.

## Como testar sem esperar um mês novo

- **Teste de retrocesso:** trate `2026-09` como "nova", usando só dados até `2026-08`; compare com a série completa.
- **Teste de fonte diferente:** o mosaico PSScene de 2026-10 (`planet_psscene/mosaico_2026-10-23`, 3 m, produto diferente do basemap) é **outra distribuição**; reamostre para 4,5 m e meça o deslocamento antes de interpretar. Se o modelo falhar nele, isso é informação sobre a robustez à troca de produto, não necessariamente defeito do modelo.
- **Simulação operacional:** reprocessar a série mês a mês, vendo só o passado, para medir latência e falsos alertas (lacuna L01).

## Verificações de saída (falha se alguma não passar)

- Esquema válido; geometrias válidas; nada fora da AOI nem sobre alfa 0.
- Quantidade de mudanças e área total dentro de uma faixa histórica plausível (alerta, não bloqueio, se muito fora).
- Falso alarme em `controles_estaveis` abaixo do limite aceito na avaliação.
- Mesma execução repetida produz o mesmo conjunto de identificadores.

## Armadilhas

- Reajustar normalização ou limiar com a imagem nova (vazamento do futuro).
- Esquecer de reclassificar os meses anteriores: a confiança dos provisórios ficaria para sempre sem confirmação.
- Aceitar imagem com mosaico de cor muito diferente sem checar a deriva (skill `inventario-dados`).
- Tratar mudança de mais de um mês (par com lacuna) como mudança mensal.
- Ler o `.env` da pasta de imagens para obter a chave: use só `PL_API_KEY` do ambiente.
