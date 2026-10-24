---
tipo: artigo
id_origem: P156
titulo: "Deepness: Deep neural remote sensing plugin for QGIS"
ano: 2023
autores: ["Przemysław Aszkowski", "Bartosz Ptak", "Marek Kraft", "Dominik Pieczyński", "Paweł Drapikowski"]
doi: "10.1016/j.softx.2023.101495"
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

# Aszkowski 2023 — Deepness: Deep neural remote sensing plugin for QGIS

> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.

**Situação da leitura:** lido (parcial). Fichas de leitura profunda usadas como evidência.

## 1. Referência bibliográfica e acesso ao original

- **Referência:** Przemysław Aszkowski, Bartosz Ptak, Marek Kraft, Dominik Pieczyński et al. (2023). Deepness: Deep neural remote sensing plugin for QGIS. SoftwareX. Tipo no catálogo: Software.
- **DOI/URL:** https://doi.org/10.1016/j.softx.2023.101495
- **Arquivo de origem:** `não disponível em coleta/ (acesso restrito ou bloqueado)`
- **Texto convertido (Markdown) e figuras:** `não informado`
- **Tipo de documento:** sem texto integral (resumo, documentação ou repositório).

## 2. Problema investigado e contribuição principal

**Evidência (leitura):**

**Deepness** (*Deep Neural Remote Sensing*) é um plugin QGIS para quem **não tem formação em ML**: um especialista cria ou converte o modelo e o usuário o aplica a qualquer camada raster pela interface. O artigo da SoftwareX (2023) não pôde ser aberto (verificação CAPTCHA); a leitura se apoia na documentação oficial e em evidência independente.


## 3. Área de estudo e período analisado

Ver seção 4 (dados), que traz área e período quando informados pelo artigo.

## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo



## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem



## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines

**Evidência (leitura) — O que foi verificado:**

- **Entrada:** qualquer camada raster (ortofoto de arquivo ou provedor online como Google Satellite), com opção de processar só uma área definida.
- **Tipos de modelo:** segmentação, regressão, detecção e super-resolução; há ferramenta de **exportação de dados de treino** (rasters e máscaras em tiles).
- **Formato de modelo:** modelos **ONNX** personalizados (P158 e a documentação de criação de modelos).
- **Parâmetros de processamento:** resolução em cm/px, **sobreposição de tiles** (inteira, em %), remoção de segmentos pequenos (P158).
- **Model zoo (24 modelos):** cobertura LandCover.ai (40 cm/px, Polônia: edificação, mata, água, estrada), edificações (Xunet, F1 de validação 81,0), estradas (Google Earth, 21 cm/px), agricultura RGB+NIR (30 cm/px), fogo, painéis solares, aviões, tanques de óleo, carros, navios, árvores, super-resolução (RDN, HAT) e outros. Só **três** modelos têm métricas publicadas no zoo (edificações F1 81,0; risco de incêndio F1 65,5; reconhecimento de lugar rank-1 75,0). Licença não declarada por modelo.
- **Aviso oficial:** os modelos "só funcionam bem em dados semelhantes aos de treino".
- **Reuso:** o diálogo de instalação de dependências do Deepness foi reaproveitado pelo IAMAP (P157). O OpenAlex lista vários plugins posteriores que citam o Deepness (YOLO-MOD, SemanticSeg4EO, TreeEyed).

- **Estratégia temporal (detecção automática, verificar):** não informado

## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos



## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas

**Evidência (leitura) — Evidência independente (estudo P158):**

Resumo em LP P158 Febrita 2025: com imagens do Google Earth e 320 edificações do OSM como referência, a configuração dos parâmetros (resolução, sobreposição e remoção de segmentos pequenos) fez o F1 passar de 48,1 % para 78,6 %.


Páginas: não informado (leitura feita sem texto integral convertido; ver a fonte na seção 1).

## 9. Limitações e condições de aplicabilidade

**Evidência (leitura) — O que não foi verificado:**

- Arquitetura do código, requisitos de versão do QGIS/Python, tratamento de bandas além de RGB e formatos exatos de saída (documentação consultada não detalha).
- Conteúdo do artigo da SoftwareX.


## 10. Reprodutibilidade: código, dados, dependências e informações ausentes

- **Código/dados:** não informado

## 11. Aplicabilidade ao monitoramento contínuo

- **Classificação (evidência):** não avaliado (sem texto). 

**Interpretação — O que reaproveitar:**

- **Rota de implantação:** exportar nossa U-Net (EXP2) para **ONNX** e rodá-la no QGIS com o Deepness para a revisão humana, usando a exportação de tiles de treino como ponte. (Hipótese: precisa conferir como o plugin trata entradas de 4 bandas.)
- **Parâmetros que precisam ser reportados em qualquer experimento com plugin:** resolução de processamento, % de sobreposição e remoção de segmentos pequenos.
- **Model zoo como baseline gratuito** para estradas e edificações antes de treinar, desde que se meça o desempenho local.

**Interpretação — Cuidados:**

- Nenhum modelo do zoo é treinado em Planet de 3–5 m; resoluções vão de 0,5 cm a 10 m, a maioria submétrica.
- Sem licença declarada nos modelos: verificar antes de uso institucional.
- Leitura parcial: não citar números do artigo original.

## 12. Relações justificadas com outras notas

**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**

**Comparações substantivas com outros artigos:**
- [[Tresson_2026_IAMAPUnlockingDeep|Tresson 2026]] reutiliza código de este artigo — IAMAP reaproveita o diálogo de instalação de dependências do Deepness (JOSS, resumo).
- [[Febrita_2025_EvaluatingDrivenAutomated|Febrita 2025]] avalia este artigo — P158 avalia o Deepness em edificações e mostra a dependência dos parâmetros (F1 48,1 → 78,6%).

## Anotações do leitor

- 
