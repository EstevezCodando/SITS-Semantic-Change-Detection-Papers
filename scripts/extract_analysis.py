"""Etapa 5: le os PDFs de coleta/, divide em chunks por secao e extrai entidades (sensores, datasets,
metodos, metricas, tarefas, ferramentas), hiperparametros e frases numericas do resumo.
Auto-contido de proposito (rodar com `python -P -E`): os PDFs sao dados nao confiaveis, entao nenhum
modulo e importado do diretorio dos scripts ou da pasta atual.
Uso: python -P -E extract_analysis.py <raiz do projeto>
"""
import re, os, sys, json, collections, unicodedata
import fitz  # PyMuPDF

sys.stdout.reconfigure(encoding='utf-8')
root = sys.argv[1]

ENT = {
 'sensor': {
  'Planet NICFI': r'\bNICFI\b', 'PlanetScope': r'\bPlanet\s?Scope\b|\bSuperDove\b|\bDove\b', 'Planet (mosaicos e cenas)': r'\bPlanet\b(?! of)(?! Earth)',
  'SkySat': r'\bSkySat\b', 'Sentinel-2': r'\bSentinel[-\s]?2\b', 'Sentinel-1/SAR': r'\bSentinel[-\s]?1\b|\bSAR\b', 'Landsat': r'\bLandsat\b',
  'WorldView': r'\bWorld\s?View\b', 'Imagens aéreas/VHR': r'\baerial (image|imagery|photo)|\bVHR\b|very[- ]high[- ]resolution', 'UAV/drone': r'\bUAV\b|\bdrone',
 },
 'dataset': {
  'SpaceNet 7 (MUDS)': r'SpaceNet\s?7|\bMUDS\b', 'DynamicEarthNet': r'DynamicEarthNet', 'LEVIR-CD': r'LEVIR-CD', 'WHU-CD': r'WHU[-\s]?(CD|Building)',
  'SECOND': r'\bSECOND\b(?= (dataset|benchmark))|SECOND dataset', 'HRSCD': r'\bHRSCD\b', 'OSCD': r'\bOSCD\b|Onera Satellite Change', 'S2Looking': r'S2Looking',
  'xBD': r'\bxBD\b', 'DeepGlobe': r'DeepGlobe', 'PRODES': r'\bPRODES\b', 'DETER': r'\bDETER\b', 'MapBiomas': r'MapBiomas', 'Global Forest Change (Hansen)': r'Hansen et al|Global Forest (Change|Watch)',
  'Dynamic World': r'Dynamic World', 'PASTIS': r'\bPASTIS\b', 'OpenStreetMap': r'OpenStreetMap|\bOSM\b', 'Inria': r'\bInria\b', 'ImageNet': r'ImageNet',
 },
 'metodo': {
  'U-Net': r'(?i:\bU-?net\b)(?!\+)', 'UNet++': r'UNet\+\+|U-Net\+\+', 'DeepLab': r'DeepLab', 'FCN': r'\bFCN\b|fully convolutional', 'ResNet': r'\bResNet',
  'Rede siamesa': r'[Ss]iamese', 'Transformer': r'[Tt]ransformer|\bViT\b|\bSwin\b|SegFormer', 'Mamba/SSM': r'\bMamba\b|state[- ]space', 'LSTM/ConvLSTM': r'\bLSTM\b|ConvLSTM|recurrent',
  'Atenção temporal (U-TAE)': r'U-TAE|temporal attention', 'SAM': r'Segment Anything|\bSAM\b', 'YOLO': r'\bYOLO', 'Grounding DINO': r'Grounding ?DINO|Grounded[- ]SAM',
  'CLIP / visão-linguagem': r'\bCLIP\b|vision[- ]language|open[- ]vocabulary', 'DINO/DINOv3': r'\bDINO(v\d)?\b', 'Autoencoder mascarado (MAE)': r'masked auto-?encoder|\bMAE\b',
  'Modelo fundacional': r'foundation model|Prithvi|\bGFM\b', 'Random Forest': r'[Rr]andom [Ff]orest', 'XGBoost': r'XGBoost|[Xx]treme [Gg]radient', 'LightGBM': r'LightGBM',
  'SVM': r'\bSVM\b|support vector', 'BFAST': r'\bBFAST\b', 'CCDC': r'\bCCDC\b', 'LandTrendr': r'LandTrendr', 'OBIA / objetos': r'OBIA|object[- ]based',
  'Aprendizado ativo': r'[Aa]ctive learning', 'Semi/auto-supervisionado': r'semi-?supervised|self-?supervised|pseudo-?label', 'Supervisão fraca': r'weakly[- ]supervised|weak supervision',
  'Transfer learning': r'[Tt]ransfer learning|fine-?tun', 'GAN/difusão': r'\bGAN\b|generative adversarial|diffusion model', 'Super-resolução': r'[Ss]uper-?resolution',
  'Fusão de dados': r'[Dd]ata fusion|image fusion|\bfusion of\b', 'Pós-classificação': r'post-?classification', 'CVA (vetor de mudança)': r'change vector analysis|\bCVA\b',
  'NDVI/índices': r'\bNDVI\b|vegetation index',
 },
 'metrica': {
  'F1': r'\bF1\b|F-?score|F-measure', 'IoU / mIoU': r'\bIoU\b|\bmIoU\b|Jaccard', 'Acurácia global': r'overall accuracy|\bOA\b', 'Kappa': r'[Kk]appa', 'SeK': r'\bSeK\b',
  'Precisão/Recall': r'[Pp]recision|[Rr]ecall', 'mAP': r'\bmAP\b|average precision', 'AUC': r'\bAUC\b|ROC', 'RMSE/MAE': r'\bRMSE\b|\bMAE\b(?! encoder)', 'Matriz de confusão': r'confusion matrix|error matrix',
  'Estimativa de área / IC': r'area estimat|confidence interval|stratified', 'SCS (DynamicEarthNet)': r'\bSCS\b',
 },
 'tarefa': {
  'Detecção de mudança (binária)': r'change detection', 'Mudança semântica': r'semantic change', 'Séries temporais de imagens': r'time[- ]series|multi-?temporal|spatio-?temporal',
  'Desmatamento': r'deforestation|forest loss|tree cover loss', 'Degradação florestal': r'degradation|disturbance', 'Edificações': r'building|construction', 'Vias/estradas': r'\broads?\b|road network',
  'Classificação de cobertura': r'land cover|land use|LULC|LCLU', 'Mineração': r'\bmining\b|garimpo', 'Expansão urbana': r'urban (expansion|growth|sprawl|change)', 'Área queimada': r'burned area|burn scar',
  'Nuvem/sombra/QA': r'cloud (mask|detection)|cloud shadow', 'Segmentação semântica': r'semantic segmentation', 'Detecção de objetos': r'object detection', 'Previsão/forecasting': r'forecast|predict(ion)? of future',
  'Anotação/rotulagem': r'annotation|labell?ing|label-efficient', 'Cubo de dados / STAC': r'data cube|\bSTAC\b|cloud[- ]native',
 },
 'ferramenta': {
  'QGIS': r'\bQGIS\b', 'GeoAI (opengeos)': r'geoai-py|opengeos|\bGeoAI\b', 'Google Earth Engine': r'Earth Engine|\bGEE\b', 'TorchGeo': r'TorchGeo', 'PyTorch': r'PyTorch', 'TensorFlow': r'TensorFlow|Keras',
  'Hugging Face': r'Hugging ?Face', 'STAC (ferramenta)': r'\bSTAC\b|pystac', 'GDAL / rasterio': r'\bGDAL\b|rasterio', 'scikit-learn': r'scikit-learn|sklearn', 'Open-CD': r'Open-?CD',
  'Optuna': r'Optuna', 'SHAP': r'\bSHAP\b', 'Ultralytics': r'Ultralytics', 'MOLUSCE': r'MOLUSCE', 'SCP (QGIS)': r'Semi-Automatic Classification',
 },
}
ENT_RX = {c: {n: re.compile(p) for n, p in d.items()} for c, d in ENT.items()}

HP = {
 'taxa de aprendizado': r'learning rate(?:[^;\n.]|\.\d){0,50}', 'batch size': r'batch size(?:[^;\n.]|\.\d){0,40}', 'épocas': r'(\d[\d,.]*\s+epochs|epochs?\s*(of|=|:)?\s*\d[\d,.]*)', 'otimizador': r'\b(AdamW?|SGD|RMSprop)\b(?! [A-Z][a-z])(?=[^.;\n]{0,30}(optimi[sz]er|learning rate|\blr\b|momentum|weight decay|\())[^.;\n]{0,40}',
 'função de perda': r'(cross-?entropy|[Dd]ice loss|[Ff]ocal loss|binary cross|BCE|contrastive loss|[Tt]versky)[^.;\n]{0,40}',
 'tamanho do patch': r'\b(\d{2,4})\s?[×x]\s?(\d{2,4})\b[^.;\n]{0,30}(patch|tile|crop|pixel|window)',
 'aumento de dados': r'(data )?augmentation[^.;\n]{0,60}',
}
HP_RX = {k: re.compile(v) for k, v in HP.items()}

SEC_KEYS = [
 ('resumo', r'^abstract|^resumo|^summary'), ('introdução', r'introduction|^background|motivation'), ('trabalhos relacionados', r'related work|literature review|state of the art|previous work'),
 ('dados', r'dataset|study area|data and|data collection|materials|^data\b|study site|imagery'), ('métodos', r'method|approach|model|architecture|framework|proposed|algorithm|implementation|network'),
 ('experimentos', r'experiment|setup|evaluation|training|implementation details|metrics'), ('resultados', r'result|performance|comparison|ablation|analysis'),
 ('discussão', r'discussion|limitation'), ('conclusão', r'conclusion|future work|summary and'), ('referências', r'^references|^bibliography|^literature cited'),
 ('agradecimentos', r'acknowledg|funding|author contribution|data availability|conflict'),
]
HEAD_RX = re.compile(r'^(?:(?:\d{1,2}(?:\.\d{1,2}){0,2}|[IVX]{1,4})[.)]?\s+)?([A-Z][A-Za-z0-9 ,:;\-–&/()\']{2,80})$')
ALLCAPS = {'ABSTRACT', 'INTRODUCTION', 'METHODS', 'METHODOLOGY', 'RESULTS', 'DISCUSSION', 'CONCLUSION', 'CONCLUSIONS', 'REFERENCES', 'RELATED WORK', 'ACKNOWLEDGMENTS', 'ACKNOWLEDGEMENTS'}


def classify(head, current):
    h = head.lower().strip()
    for name, rx in SEC_KEYS:
        if re.search(rx, h): return name
    return current


def page_lines(doc):
    pages = []
    for p in doc:
        pages.append([unicodedata.normalize('NFKC', l).strip() for l in p.get_text('text').split('\n') if l.strip()])
    cnt = collections.Counter(l for pg in pages for l in set(pg))
    rep = {l for l, c in cnt.items() if c >= max(3, len(pages) * 0.4) and len(l) < 120}
    return [[l for l in pg if l not in rep and not re.fullmatch(r'\d{1,4}', l)] for pg in pages]


def sections(pages):
    """Retorna lista de (tipo, titulo, pagina, [paragrafos])."""
    out, cur, head, page0 = [], 'resumo', 'Início', 1
    paras, buf = [], []
    started = False

    def flush_para():
        nonlocal buf
        if buf:
            t = ' '.join(buf)
            t = re.sub(r'(\w)- (\w)', r'\1\2', t)
            paras.append(re.sub(r'\s+', ' ', t).strip())
            buf = []

    def flush_sec():
        nonlocal paras
        flush_para()
        if paras: out.append((cur, head, page0, paras))
        paras = []

    for pi, pg in enumerate(pages, 1):
        for l in pg:
            m = HEAD_RX.match(l)
            is_head = bool(m) and len(l.split()) <= 9 and not l.endswith('.') and (re.match(r'^(\d{1,2}(\.\d{1,2}){0,2}|[IVX]{1,4})[.)]?\s', l) or l.upper() in ALLCAPS or l in ('Abstract', 'Introduction', 'References', 'Conclusion', 'Conclusions', 'Discussion', 'Results', 'Methods', 'Acknowledgments', 'Acknowledgements'))
            if is_head:
                flush_sec()
                head = l
                cur = classify(l, cur if started else 'resumo')
                page0 = pi
                started = True
                if cur == 'referências': return out
                continue
            buf.append(l)
            if l.endswith(('.', ':')) and len(' '.join(buf)) > 350: flush_para()
    flush_sec()
    return out


def chunk_section(paras, target=1700, hard=2400, overlap=180):
    chunks, cur = [], ''
    for p in paras:
        if len(p) > hard:  # paragrafo gigante: divide por sentencas
            parts = re.split(r'(?<=[.!?])\s+', p)
        else:
            parts = [p]
        for s in parts:
            if cur and len(cur) + len(s) > target:
                chunks.append(cur)
                cur = cur[-overlap:].split(' ', 1)[-1] + ' ' + s
            else:
                cur = (cur + ' ' + s).strip()
    if cur: chunks.append(cur)
    if len(chunks) > 1 and len(chunks[-1]) < 300:
        chunks[-2] += ' ' + chunks[-1]
        chunks.pop()
    return chunks


def find_entities(text, min_count=1):
    res = {}
    for cat, d in ENT_RX.items():
        for n, rx in d.items():
            c = len(rx.findall(text))
            if c >= min_count: res.setdefault(cat, {})[n] = c
    return res


def numeric_sentences(text, limit=3):
    out = []
    for s in re.split(r'(?<=[.!?])\s+', text):
        if re.search(r'\b(F1|IoU|accuracy|precision|recall|kappa|mIoU|OA|RMSE|SeK)\b', s, re.I) and re.search(r'\d+(\.\d+)?\s?%|\b0\.\d{2,}\b', s):
            out.append(s.strip()[:230])
        if len(out) >= limit: break
    return out


def analyse(pdf, pid):
    doc = fitz.open(pdf)
    pages = page_lines(doc)
    nchars = sum(len(l) for pg in pages for l in pg)
    secs = sections(pages)
    chunks, body = [], []
    for stype, head, pg, paras in secs:
        if stype == 'agradecimentos': continue
        for c in chunk_section(paras):
            chunks.append({'id': f'{pid}_c{len(chunks) + 1:03d}', 'paper': pid, 'secao': stype, 'titulo_secao': head, 'pagina': pg, 'texto': c})
            body.append(c)
    full = ' '.join(body)
    ents_all = find_entities(full, 1)
    for c in chunks:
        e = find_entities(c['texto'], 1)
        c['entidades'] = {k: sorted(v) for k, v in e.items()}
        c['tem_numeros_resultado'] = bool(numeric_sentences(c['texto'], 1))
        c['tem_hiperparametros'] = any(rx.search(c['texto']) for rx in HP_RX.values())
        c['chars'] = len(c['texto'])
    hp = {}
    for k, rx in HP_RX.items():
        for c in chunks:
            m = rx.search(c['texto'])
            if m:
                hp[k] = {'trecho': re.sub(r'\s+', ' ', m.group(0))[:90], 'chunk': c['id']}
                break
    abstract = ' '.join(c['texto'] for c in chunks if c['secao'] == 'resumo')[:3000] or (chunks[0]['texto'][:1500] if chunks else '')
    return chunks, {
        'paginas': len(doc), 'chars_por_pagina': round(nchars / max(1, len(doc))), 'n_chunks': len(chunks),
        'secoes': dict(collections.Counter(c['secao'] for c in chunks)), 'entidades': ents_all, 'hiperparametros': hp,
        'github': sorted(set(re.findall(r'https?://github\.com/[\w.\-]+/[\w.\-]+', ' '.join(' '.join(pg) for pg in pages))))[:6],
        'frases_resultado': numeric_sentences(abstract + ' ' + ' '.join(c['texto'] for c in chunks if c['secao'] in ('resultados', 'conclusão')), 4),
        'qualidade_texto': 'baixa (possivel PDF escaneado)' if nchars / max(1, len(doc)) < 600 else 'ok',
    }


if __name__ == '__main__':
    cat = json.load(open(f'{root}/dados/catalog.json', encoding='utf-8'))
    os.makedirs(f'{root}/dados/chunks', exist_ok=True)
    result = {}
    for r in cat:
        if not r.get('pdf_file'): continue
        try:
            chunks, info = analyse(f"{root}/coleta/{r['pdf_file']}", r['id'])
            with open(f"{root}/dados/chunks/{r['id']}.jsonl", 'w', encoding='utf-8') as f:
                for c in chunks: f.write(json.dumps(c, ensure_ascii=False) + '\n')
            result[r['id']] = info
            print(r['id'], info['paginas'], 'pg', info['n_chunks'], 'chunks', info['qualidade_texto'])
        except Exception as e:
            result[r['id']] = {'erro': f'{type(e).__name__}: {str(e)[:80]}'}
            print(r['id'], 'ERRO', e)
    json.dump(result, open(f'{root}/dados/analysis.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('ok', len(result))
