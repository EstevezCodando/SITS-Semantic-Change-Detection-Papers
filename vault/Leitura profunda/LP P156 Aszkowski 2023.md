---
tipo: leitura_profunda
paper: "P156"
leitura: "parcial (documentação oficial, model zoo e avaliação independente em P158; artigo da SoftwareX atrás de CAPTCHA)"
fonte_lida: "qgis-plugin-deepness.readthedocs.io (features, model zoo); estudo P158; descrições em P157"
etapas_pipeline: ["[[E11 Operação e atualização|E11]]"]
tags: [leitura_profunda, prioridade/alta]
---

# Leitura profunda — P156 Aszkowski 2023

**Deepness: Deep neural remote sensing plugin for QGIS**

Nota do artigo: [[P156 Aszkowski 2023|P156 Aszkowski 2023]] · Leitura: *parcial (documentação oficial, model zoo e avaliação independente em P158; artigo da SoftwareX atrás de CAPTCHA)*

> Leitura feita nesta coleta; valores e afirmações vêm do texto lido, com link para o chunk de origem. O que não foi verificado está marcado.

## Pergunta e escopo
**Deepness** (*Deep Neural Remote Sensing*) é um plugin QGIS para quem **não tem formação em ML**: um especialista cria ou converte o modelo e o usuário o aplica a qualquer camada raster pela interface. O artigo da SoftwareX (2023) não pôde ser aberto (verificação CAPTCHA); a leitura se apoia na documentação oficial e em evidência independente.

## O que foi verificado
- **Entrada:** qualquer camada raster (ortofoto de arquivo ou provedor online como Google Satellite), com opção de processar só uma área definida.
- **Tipos de modelo:** segmentação, regressão, detecção e super-resolução; há ferramenta de **exportação de dados de treino** (rasters e máscaras em tiles).
- **Formato de modelo:** modelos **ONNX** personalizados (P158 e a documentação de criação de modelos).
- **Parâmetros de processamento:** resolução em cm/px, **sobreposição de tiles** (inteira, em %), remoção de segmentos pequenos (P158).
- **Model zoo (24 modelos):** cobertura LandCover.ai (40 cm/px, Polônia: edificação, mata, água, estrada), edificações (Xunet, F1 de validação 81,0), estradas (Google Earth, 21 cm/px), agricultura RGB+NIR (30 cm/px), fogo, painéis solares, aviões, tanques de óleo, carros, navios, árvores, super-resolução (RDN, HAT) e outros. Só **três** modelos têm métricas publicadas no zoo (edificações F1 81,0; risco de incêndio F1 65,5; reconhecimento de lugar rank-1 75,0). Licença não declarada por modelo.
- **Aviso oficial:** os modelos "só funcionam bem em dados semelhantes aos de treino".
- **Reuso:** o diálogo de instalação de dependências do Deepness foi reaproveitado pelo IAMAP (P157). O OpenAlex lista vários plugins posteriores que citam o Deepness (YOLO-MOD, SemanticSeg4EO, TreeEyed).

## O que não foi verificado
- Arquitetura do código, requisitos de versão do QGIS/Python, tratamento de bandas além de RGB e formatos exatos de saída (documentação consultada não detalha).
- Conteúdo do artigo da SoftwareX.

## Evidência independente (estudo P158)
Resumo em [[LP P158 Febrita 2025]]: com imagens do Google Earth e 320 edificações do OSM como referência, a configuração dos parâmetros (resolução, sobreposição e remoção de segmentos pequenos) fez o F1 passar de 48,1 % para 78,6 %.

## O que reaproveitar
- **Rota de implantação:** exportar nossa U-Net (EXP2) para **ONNX** e rodá-la no QGIS com o Deepness para a revisão humana, usando a exportação de tiles de treino como ponte. (Hipótese: precisa conferir como o plugin trata entradas de 4 bandas.)
- **Parâmetros que precisam ser reportados em qualquer experimento com plugin:** resolução de processamento, % de sobreposição e remoção de segmentos pequenos.
- **Model zoo como baseline gratuito** para estradas e edificações antes de treinar, desde que se meça o desempenho local.

## Cuidados
- Nenhum modelo do zoo é treinado em Planet de 3–5 m; resoluções vão de 0,5 cm a 10 m, a maioria submétrica.
- Sem licença declarada nos modelos: verificar antes de uso institucional.
- Leitura parcial: não citar números do artigo original.
