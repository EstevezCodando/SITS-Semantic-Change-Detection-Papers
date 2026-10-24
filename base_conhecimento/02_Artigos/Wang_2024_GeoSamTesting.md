---
tipo: artigo
id_origem: P164
titulo: "Geo-Sam: Testing the Reliability and Limits of Mine Feature Delineation Using Segment Anything Model"
ano: 2024
autores: ["Qitong Wang", "Emmanuel Chinkaka", "Romain Richaud", "Mehrnaz Haghdadi", "Coryn Wolk", "Kopo V. Oromeng", "Kyle Frankel Davis", "Federica Bettina Bianco"]
doi: "10.2139/ssrn.4786825"
arquivo_fonte: "não informado"
markdown_fonte: "não informado"
paginas: não informado
tipo_documento: "sem texto integral (resumo, documentação ou repositório)"
status_leitura: "lido (parcial)"
tarefas: ["[[Mineracao|Mineração]]"]
sensores: []
conjuntos_dados: []
metodos: []
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/parcial]
---

# Wang 2024 — Geo-Sam: Testing the Reliability and Limits of Mine Feature Delineation Using Segment Anything Model

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (parcial). Fichas de leitura profunda usadas como evidência.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Qitong Wang, Emmanuel Chinkaka, Romain Richaud, Mehrnaz Haghdadi et al. (2024). Geo-Sam: Testing the Reliability and Limits of Mine Feature Delineation Using Segment Anything Model. SSRN Electronic Journal. Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.2139/ssrn.4786825
- **Arquivo de origem:** `não disponível em coleta/ (acesso restrito ou bloqueado)`
- **Texto convertido (Markdown) e figuras:** `não informado`
- **Tipo de documento:** sem texto integral (resumo, documentação ou repositório).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

Esta entrada reúne duas coisas ligadas por nome:
1. O **plugin Geo-SAM para QGIS** (Zhao, Fan e Liu, 2023): segmentar, delinear e rotular feições (feições de relevo) em rasters grandes com o SAM.
2. O **registro SSRN de 2024** "Geo-Sam: Testing the Reliability and Limits of Mine Feature Delineation Using Segment Anything Model" (preprint, não aberto). Pelo título e pelo contexto parece ser a versão anterior do estudo publicado como **MO-SAM** (LP P165 Wang 2025); essa equivalência não foi confirmada porque o texto do SSRN não foi lido.


## 3. Área de estudo e período analisado

Ver seção 4 (dados), que traz área e período quando informados pelo artigo.

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo



## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem



## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — O plugin Geo-SAM (README verificado):**

- **Fluxo em duas etapas:** a imagem é codificada **uma vez** (Image Encoder) e depois o usuário interage clicando; a segmentação responde em **milissegundos em CPU de notebook** porque as características já estão calculadas.
- **Dois modos:** *Live Encoding* (codifica em tarefas de fundo no QGIS e guarda em cache) e *Pre-encoded* (gera arquivos de características reutilizáveis).
- **Entradas:** camadas raster ou camadas de tiles XYZ/WMS online. Bandas, tamanho e formatos de arquivo não são especificados no README.
- **Modelos:** SAM, SAM 2, SAM 2.1 e SAM 3 (baixados em "Model Management").
- **Saídas:** polígonos em dois modos de vetorização (nível de pixel ou simplificado) e opção de manter só o maior polígono por máscara.
- **Instalação:** Plugin Manager, "Install Missing" para dependências e reinício do QGIS. Interface multilíngue.
- **Licença:** MIT. **Citação:** Zhao, Fan e Liu (2023), Zenodo, doi:10.5281/zenodo.8191039.
- Limitações não listadas no README.

- **Estratégia temporal (detecção automática, verificar):** não informado

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos



## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

Páginas: não informado (leitura feita sem texto integral convertido; ver a fonte na seção 1).

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — O que não foi verificado:**

- Qualquer resultado quantitativo do preprint SSRN e a relação exata com o MO-SAM.
- Desempenho do plugin em imagens de 3–5 m ou de 4 bandas.


## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** não avaliado (sem texto). 

**Interpretação — O que reaproveitar:**

- **Pré-codificação de mosaicos mensais** (modo Pre-encoded): codificar cada mês uma vez e permitir cliques rápidos de anotadores, reduzindo o tempo por evento. É a base técnica mais útil do EXP6 em equipe sem GPU.
- **Vetorização com opção de maior polígono** para evitar o ruído de máscaras multiparte (problema visto em LP P165 Wang 2025).
- Integração direta em QGIS, sem passar por capturas de tela.

**Interpretação — Cuidados:**

- Foi concebido para relevo e feições de terreno em imagens de alta resolução.
- Os mosaicos Planet têm 4 bandas (RGB+NIR); verificar como o plugin escolhe as bandas e converte para 8 bits.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- trata a tarefa: [[Mineracao|Mineração]] — suporte vindo da leitura/título/resumo
- referencia (suporte manual da leitura): [[PreAnotacaoSAM|Pré-anotação assistida (SAM e plugins QGIS)]] — suporte vindo da leitura/título/resumo

**Comparações substantivas com outros artigos:**
- [[Wang_2025_SAMTestingReliability|Wang 2025]] tem versão anterior possivelmente em este artigo — O registro SSRN P164 parece ser o preprint do estudo MO-SAM; equivalência não confirmada.

## Anotações do leitor

- 
