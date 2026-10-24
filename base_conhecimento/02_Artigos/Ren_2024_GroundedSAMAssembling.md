---
tipo: artigo
id_origem: P57
titulo: "Grounded SAM: Assembling Open-World Models for Diverse Visual Tasks"
ano: 2024
autores: ["Tianhe Ren", "Shilong Liu", "Ailing Zeng", "Jing Lin", "Kunchang Li", "He Cao", "Jiayu Chen", "Xinyu Huang"]
doi: "10.48550/arXiv.2401.14159"
arquivo_fonte: "coleta/P57_Ren2024_Grounded-SAM-Assembling-Open-World-Models-for-Diverse-Visual.pdf"
markdown_fonte: "output/pdf/P57_Ren2024_Grounded-SAM-Assembling-Open-World-Models-for-Diverse-Visual/document.md"
paginas: 11
tipo_documento: "artigo completo (texto integral convertido)"
status_leitura: "extraído automaticamente (não lido)"
relevancia_objetivo: "D"
tarefas: []
sensores: []
conjuntos_dados: []
metodos: ["[[SAM|Segment Anything (SAM)]]"]
preparo: []
validacao: []
ferramentas: []
tags: [artigo, leitura/automatica, relevancia/D]
---

# Ren 2024 — Grounded SAM: Assembling Open-World Models for Diverse Visual Tasks

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** extraído automaticamente (não lido). Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.

**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **D** — não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Tianhe Ren, Shilong Liu, Ailing Zeng, Jing Lin et al. (2024). Grounded SAM: Assembling Open-World Models for Diverse Visual Tasks. arXiv (Cornell University). Tipo no catálogo: Preprint.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2401.14159
- **Arquivo de origem:** `coleta/P57_Ren2024_Grounded-SAM-Assembling-Open-World-Models-for-Diverse-Visual.pdf`
- **Texto convertido (Markdown) e figuras:** `output/pdf/P57_Ren2024_Grounded-SAM-Assembling-Open-World-Models-for-Diverse-Visual/document.md` — 11 páginas, 61 recortes de figuras, 0 avisos de conversão
- **Tipo de documento:** artigo completo (texto integral convertido).

## 2. Problema investigado e contribuição principal

**Resumo detectado automaticamente (p. 1):** We introduce Grounded SAM , which uses Grounding DINO [ 38 ] as an open-set object detector to combine with the segment anything model (SAM) [ 25 ]. This integration enables the detection and segmentation of any regions based on arbitrary text inputs and opens a door to connecting vari- ous vision models. 1, a wide range of vision tasks can be achieved by using the versatile Grounded SAM pipeline. For example, an automatic annotation pipeline 1 based solely on input images can be realized by incorporat- ing models such as BLIP [ 31 ] and Recognize Anything [ 83 ]. Additionally, incorporating Stable-Diffusion [ 52 ] allows for controllable image editing, while the integration of OSX [ 33 ] facilitates promptable 3D human motion analysis. Grounded SAM also shows superior performance on open-vocabulary benchmarks, achieving 48.7 mean AP on SegInW (Segmenta- tion in the wild) zero-shot bench…

- “We introduce Grounded SAM , which uses Grounding DINO [ 38 ] as an open-set object detector to combine with the segment anything model (SAM) [ 25 ].” (p. 1, seção Abstract)
- “To validate the effectiveness of Grounded SAM, we evaluate its performance on the Segmentation in the Wild (SGinW) zero-shot benchmark, which comprises 25 zero-shot in-thewild datasets.” (p. 7, seção 4. Effectiveness of Grounded SAM)

## 3. Área de estudo e período analisado

Não informado (nenhum trecho de área ou período detectado automaticamente).

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo

**Detectado automaticamente (verificar):**
- “These applications demand robust and versatile visual perception models capable of interpreting and interacting with open-world environments.” (p. 2, seção 1. Introduction)

## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem

**Detectado automaticamente (verificar):**
- **Rotulagem / anotação**: 25 ocorrências (p. 1, 2, 3, 4, 5)

## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

- **Estratégia temporal (detecção automática, verificar):** imagem única ou não detectado (auto)
**Métodos detectados automaticamente:**
- método/família **SAM**: 70 ocorrências (p. 1, 2, 3, 4, 5)

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos

Não informado (nada detectado automaticamente).

## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

Não informado (nenhum trecho com métrica e valor detectado).

## 9. Limitações e condições de aplicabilidade

**Trechos detectados automaticamente (verificar contexto):**
- “However, a significant limitation of such an approach is its limited scope in data, especially in complex tasks like openset segmentation.” (p. 2, seção 1. Introduction)
- “However, this method is heavily reliant on the functionalities and limitations of large language models.” (p. 2, seção 1. Introduction)
- “Despite of its strong zero-shot performance, the model cannot identify the masked objects based an arbitrary text input and normally requires point or box prompts to run.” (p. 3, seção 3.1. Preliminary)

## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** sim: github.com/IDEA-Research/Grounded-Segment-Anything (p. 1)
- URL citada: https://github.com/IDEA-Research/Grounded-Segment-Anything (p. 1)
- URL citada: https://github.com/CiaoHe (p. 8)
- URL citada: https://github.com/tuofeilunhifi (p. 8)
- URL citada: https://github.com/fengxiuyaun (p. 8)
- hiperparâmetros **não detectados** automaticamente: taxa de aprendizado, batch, épocas/iterações, otimizador, perda (podem existir no texto; verificar).

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** retrospectivo (sem evidência extraída de operação contínua). 
- menções de termos de monitoramento (contagem, não avaliação): Custo 4 (p. 3, 4, 7); Quase tempo real 1 (p. 4)

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**
- utiliza método: [[SAM|Segment Anything (SAM)]] — 70 ocorrências (p. 1, 2, 3, 4, 5)

## Anotações do leitor

- 
