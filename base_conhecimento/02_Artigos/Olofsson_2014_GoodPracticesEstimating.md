---
tipo: artigo
id_origem: P46
titulo: "Good practices for estimating area and assessing accuracy of land change"
ano: 2014
autores: ["Pontus Olofsson", "Giles M. Foody", "Martin Herold", "Stephen V. Stehman", "Curtis E. Woodcock", "Michael A. Wulder"]
doi: "10.1016/j.rse.2014.02.015"
arquivo_fonte: "não informado"
markdown_fonte: "não informado"
paginas: não informado
tipo_documento: "sem texto integral (resumo, documentação ou repositório)"
status_leitura: "lido (parcial)"
tarefas: []
sensores: []
conjuntos_dados: []
metodos: []
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/parcial]
---

# Olofsson 2014 — Good practices for estimating area and assessing accuracy of land change

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (parcial). Fichas de leitura profunda usadas como evidência.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Pontus Olofsson, Giles M. Foody, Martin Herold, Stephen V. Stehman et al. (2014). Good practices for estimating area and assessing accuracy of land change. Remote Sensing of Environment. Tipo no catálogo: Artigo.
- **DOI/URL:** https://doi.org/10.1016/j.rse.2014.02.015
- **Arquivo de origem:** `não disponível em coleta/ (acesso restrito ou bloqueado)`
- **Texto convertido (Markdown) e figuras:** `não informado`
- **Tipo de documento:** sem texto integral (resumo, documentação ou repositório).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Boas práticas para **estimar área e avaliar a acurácia de mapas de mudança** com uma amostra de referência. Estrutura em três componentes: **desenho amostral**, **desenho da resposta** (como se rotula a referência) e **análise**.


## 3. Área de estudo e período analisado

Ver seção 4 (dados), que traz área e período quando informados pelo artigo.

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo



## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem



## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — Recomendações verificadas (resumo):**

- Amostragem **probabilística** (por exemplo, estratificada), equilibrando acurácia, estimativa de área, custo e disponibilidade de dados de referência.
- Dados de referência **bem mais precisos que o mapa avaliado**, com definição consistente das classes de mudança.
- Análise compatível com o desenho amostral: **matriz de erro em proporções de área**, acurácia global, de usuário e do produtor, e **estimativa de área por classe com intervalo de confiança**.
- Todo mapa de mudança deve vir com: descrição da amostragem (tamanho e estratificação), matriz de erro, área (ou proporção) de cada categoria no mapa e medidas descritivas de acurácia.
- O pacote R **`mapaccuracy`** implementa os estimadores e reproduz os exemplos do artigo.
- P05 aplica exatamente este protocolo (amostragem probabilística, desenho da resposta e matriz de erro) para validar seus mapas de mudança.

- **Estratégia temporal (detecção automática, verificar):** não informado

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos



## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

Páginas: não informado (leitura feita sem texto integral convertido; ver a fonte na seção 1).

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — O que não foi verificado:**

- Fórmulas, exemplos numéricos e tabelas do texto integral.


## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** não avaliado (sem texto). 

**Interpretação — O que reaproveitar (decisões de projeto):**

- **Área alterada em hectares deve vir da estimativa amostral com IC**, nunca da contagem de pixels do mapa.
- **Amostra de avaliação probabilística, independente do conjunto de treino e do de aprendizado ativo**, estratificada por classes mapeadas (mudança rara exige super-amostrar a mudança).
- **Rótulos de referência** feitos por interpretação especializada com a série e imagens de maior resolução, quando possível.
- Relatório mínimo por mapa: tamanho da amostra, estratos, matriz de erro em áreas, UA, PA, OA e áreas com IC. Vai para a etapa E10 Avaliação e incerteza.

**Interpretação — Cuidados:**

- É leitura parcial; antes de implementar, ler o artigo e testar o `mapaccuracy`.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**

**Comparações substantivas com outros artigos:**
- [[ZarazaAguilera_2022_ChangeDetectionOver|ZarazaAguilera 2022]] aplica o protocolo de avaliação de este artigo — P05 valida os mapas de mudança pelo método de Olofsson: (p. 4).

## Anotações do leitor

- 
