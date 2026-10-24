"""Extrai, de output/pdf/*/document.md, evidencias rastreaveis (pagina + secao) para a base de conhecimento.
Nada e inferido alem do texto: cada item aponta para a pagina e a secao onde o trecho foi encontrado.
O markdown vem de PDFs (dado nao confiavel): so e lido como texto.
Uso: python -I kb_extract.py <raiz> -> dados/kb_extract.json
"""
import re, os, sys, json, collections
sys.stdout.reconfigure(encoding='utf-8')
root = sys.argv[1]
OUT = f'{root}/output/pdf'

# ------------------------------------------------------------------ dicionarios (pt-BR rotulos; regex em ingles/portugues/espanhol)
ENT = {
 'sensor': {
  'Planet NICFI': r'\bNICFI\b', 'PlanetScope': r'\bPlanet\s?Scope\b|\bSuperDove\b|\bDove\b', 'Planet (mosaicos e cenas)': r'\bPlanet\b(?! of)(?! Earth)',
  'SkySat': r'\bSkySat\b', 'Sentinel-2': r'\bSentinel[-\s]?2\b', 'Sentinel-1': r'\bSentinel[-\s]?1\b', 'Landsat': r'\bLandsat\b', 'WorldView': r'\bWorld\s?View\b',
  'Imagens aéreas': r'\baerial (image|imagery|photo)', 'UAV': r'\bUAV\b|\bdrone', 'SAR': r'\bSAR\b|synthetic aperture',
 },
 'dataset': {
  'SpaceNet 7 (MUDS)': r'SpaceNet\s?7|\bMUDS\b', 'DynamicEarthNet': r'DynamicEarthNet', 'LEVIR-CD': r'LEVIR-CD', 'WHU-CD': r'WHU[-\s]?(CD|Building)',
  'SECOND': r'SECOND dataset|\bSECOND\b benchmark', 'HRSCD': r'\bHRSCD\b', 'OSCD': r'\bOSCD\b|Onera Satellite', 'S2Looking': r'S2Looking', 'xBD': r'\bxBD\b',
  'DeepGlobe': r'DeepGlobe', 'PRODES': r'\bPRODES\b', 'DETER': r'\bDETER\b', 'MapBiomas': r'MapBiomas', 'Global Forest Change': r'Global Forest (Change|Watch)|Hansen et al',
  'Dynamic World': r'Dynamic World', 'OpenStreetMap': r'OpenStreetMap|\bOSM\b', 'Brazil Data Cube': r'Brazil Data Cube',
 },
 'metodo': {
  'U-Net': r'(?i:\bU-?net\b)(?!\+)', 'CNN': r'\bCNNs?\b|convolutional neural', 'Rede siamesa': r'[Ss]iamese', 'Transformer': r'[Tt]ransformer|\bViT\b|\bSwin\b',
  'Mamba': r'\bMamba\b', 'LSTM / recorrente': r'\bLSTM\b|ConvLSTM|recurrent', 'U-TAE': r'U-TAE|\bUTAE\b', 'SAM': r'Segment Anything|\bSAM\b', 'YOLO': r'\bYOLO',
  'Modelo fundacional': r'foundation model|Prithvi|\bGFM\b|DINOv\d', 'Random Forest': r'[Rr]andom [Ff]orest', 'XGBoost': r'XGBoost|[Xx]treme [Gg]radient',
  'LightGBM': r'LightGBM', 'SVM': r'\bSVM\b|support vector', 'BFAST': r'\bBFAST\b', 'CCDC': r'\bCCDC\b', 'LandTrendr': r'LandTrendr', 'OBIA': r'OBIA|GEOBIA|object[- ]based',
  'Aprendizado ativo': r'[Aa]ctive learning', 'Semi/auto-supervisionado': r'semi-?supervised|self-?supervised|pseudo-?label', 'Supervisão fraca': r'weakly[- ]supervised|weak supervision',
  'Transfer learning': r'[Tt]ransfer learning|fine-?tun', 'Pós-classificação': r'post-?classification', 'Super-resolução': r'[Ss]uper-?resolution',
 },
 'metrica': {
  'F1': r'\bF1\b|F-?score|F-measure', 'IoU': r'\bIoU\b|\bmIoU\b|Jaccard', 'Acurácia global': r'overall accuracy|\bOA\b', 'Kappa': r'[Kk]appa', 'Precisão/Recall': r'[Pp]recision|[Rr]ecall',
  'mAP': r'\bmAP\b', 'Matriz de confusão': r'confusion matrix|error matrix', 'Estimativa de área': r'area estimat|confidence interval|stratified'},
 'ferramenta': {
  'QGIS': r'\bQGIS\b', 'Google Earth Engine': r'Earth Engine|\bGEE\b', 'TorchGeo': r'TorchGeo', 'PyTorch': r'PyTorch', 'TensorFlow': r'TensorFlow|Keras', 'GDAL': r'\bGDAL\b|rasterio',
  'scikit-learn': r'scikit-learn|sklearn', 'Hugging Face': r'Hugging ?Face'},
 'preparo': {
  'Máscara de nuvem e sombra': r'cloud (mask|filter|cover|detection)|cloud shadow|cloud-free', 'Correção atmosférica / reflectância': r'atmospheric correction|surface reflectance|top[- ]of[- ]atmosphere|radiometric',
  'Corregistro / georreferenciamento': r'co-?registration|georeferenc|geo-referenc|misregistration', 'Reamostragem': r'resampl|bicubic|bilinear|nearest[- ]neighbo',
  'Mosaicos e compostos': r'mosaic|composite', 'Normalização / escala': r'normali[sz]|rescal|standardi[sz]', 'Índices espectrais': r'\bNDVI\b|vegetation index|spectral index|indices',
  'Textura (GLCM)': r'\bGLCM\b|textur', 'Recorte em patches/tiles': r'patch(es)?\b|\btiles?\b|chips?\b|crop(ped|s)? ', 'Preenchimento de lacunas': r'gap[- ]fill',
  'Aumento de dados': r'data augmentation|augmentation', 'Rotulagem / anotação': r'annotat|labell?ing|labeled|ground truth|reference data', 'Segmentação em objetos': r'segmentation (algorithm|step)|\bSNIC\b|superpixel',
 },
 'validacao': {
  'Validação cruzada': r'cross-?validation|k-?fold|\d-?fold', 'Divisão espacial': r'spatial (split|domain shift|block|cross)|geographic(al)? (split|block)|held-out (area|region)',
  'Divisão temporal': r'temporal (split|shift|domain shift)|future (year|date)|different year', 'Amostra independente': r'independent (sample|validation|test|reference)',
  'Conjuntos treino/val/teste': r'training,? validation(,| and) (and )?test|train(ing)?/val(idation)?/test|test set|validation set', 'Amostragem estratificada': r'stratified|probability sampling|probabilistic sampling',
  'Desbalanceamento': r'imbalance|rare (class|event|change)|class weight', 'Teste externo / generalização': r'generali[sz]ation|external (test|validation)|transferab|domain shift',
 },
 'monitoramento': {
  'Quase tempo real': r'near[- ]real[- ]time|real[- ]time|NRT', 'Sistema operacional': r'operational|operationali', 'Alertas': r'\balerts?\b|early warning', 'Latência / frequência': r'latency|update frequency|revisit|weekly|monthly update',
  'Falsos alertas': r'false (alarm|alert|positive rate)', 'Revisão humana': r'human (review|interpret|verification|analyst)|manual (inspection|verification|editing)|visual interpretation|expert interpretation',
  'Persistência / confirmação': r'persisten|confirm(ed|ation)', 'Drift': r'concept drift|data drift|\bdrift\b', 'Custo': r'\bcosts?\b|computational (cost|time)|processing time', 'Rastreabilidade': r'traceab|provenance|reproducib',
 },
}
HP = {'taxa de aprendizado': r'learning rate(?:[^;\n.]|\.\d){0,50}', 'batch': r'batch size(?:[^;\n.]|\.\d){0,40}', 'épocas/iterações': r'(\d[\d,.]*\s+(epochs|iterations)|(epochs|iterations)\s*(of|=|:)?\s*\d[\d,.]*)',
      'otimizador': r'\b(AdamW?|SGD|RMSprop)\b(?! [A-Z][a-z])(?=[^.;\n]{0,30}(optimi[sz]er|learning rate|\blr\b|momentum|weight decay|\())[^.;\n]{0,40}',
      'perda': r'(cross-?entropy|[Dd]ice loss|[Ff]ocal loss|binary cross|[Tt]versky)[^.;\n]{0,40}', 'tamanho do patch': r'\b(\d{2,4})\s?[×x]\s?(\d{2,4})\b[^.;\n]{0,30}(patch|tile|crop|pixel|window)'}
CODE = re.compile(r'https?://(?:www\.)?(?:github\.com|gitlab\.com|zenodo\.org|figshare\.com|huggingface\.co|osf\.io)/[^\s)\]>`]+', re.I)
RES = re.compile(r'(\d+(?:[.,]\d+)?)\s?(m|cm|km)\b(?:\s?(?:spatial\s)?(?:resolution|GSD|pixel|/\s?px|per pixel))?|GSD[^.]{0,30}?(\d+(?:[.,]\d+)?)\s?(m|cm)', re.I)
NIMG = re.compile(r'(\d[\d,.]*)\s+(?:image pairs|images|scenes|time series|sequences|tiles|patches|samples)\b', re.I)
HEAD = re.compile(r'^(?:#{1,6}\s*)?\**\s*((?:\d{1,2}(?:\.\d{1,2}){0,3}|[IVX]{1,4})[.)]?\s+[A-Za-z][^*|]{2,80}?)\s*\**$')
NAMED = re.compile(r'^(?:#{1,6}\s*)?\**\s*(abstract|introduction|related work|methods?|methodology|materials and methods|data|study area|experiments?|results|discussion|conclusions?|limitations|references|acknowledg\w+|resumen|resumo)\**\s*$', re.I)
CAP = re.compile(r'^\**\s*(Figure|Fig\.|Table)\s+(\d+)', re.I)
IMG = re.compile(r'!\[[^\]]*\]\(([^)]+)\)')
STOPSEC = ('references', 'bibliography')


def clean(s):
    s = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', s)
    s = re.sub(r'[*_`]+', '', s)
    s = re.sub(r'\[(\d+(?:[,\s–-]+\d+)*)\]', '', s)
    return re.sub(r'\s+', ' ', s).strip()


def parse(doc):
    txt = open(doc, encoding='utf-8').read()
    pages = re.split(r'<!-- page: (\d+) -->', txt)
    out = []
    sec = 'Início'
    for i in range(1, len(pages), 2):
        n = int(pages[i]); body = pages[i + 1]
        lines = []
        figs = []
        for raw in body.split('\n'):
            ln = raw.strip()
            if not ln or ln.startswith('## Página') or ln.startswith('Texto complementar'): continue
            for m in IMG.finditer(ln):
                figs.append(m.group(1))
            m = HEAD.match(ln) or NAMED.match(ln)
            if m and len(ln) < 110:
                sec = clean(m.group(1)); lines.append(('H', sec)); continue
            c = clean(ln)
            if c: lines.append(('T', c))
        text, secs = [], []
        cur = sec_at_start = None
        out.append({'n': n, 'lines': lines, 'figs': figs})
    return out


def sentences(pages):
    """Itera (pagina, secao, sentenca)."""
    sec = 'Início'
    for p in pages:
        buf = []
        for kind, t in p['lines']:
            if kind == 'H':
                sec = t; continue
            buf.append((sec, t))
        # agrupa linhas consecutivas da mesma secao e separa sentencas dentro de cada grupo
        groups = []
        for s_, t in buf:
            if groups and groups[-1][0] == s_: groups[-1][1].append(t)
            else: groups.append((s_, [t]))
        for s_, ts in groups:
            for s in re.split(r'(?<=[.!?])\s+(?=[A-Z0-9(])', ' '.join(ts)):
                if len(s) > 25: yield p['n'], s_, s
        if buf: sec = buf[-1][0]


def analyse(doc, pid):
    pages = parse(doc)
    sents = list(sentences(pages))
    res = {'pages': len(pages), 'ents': {}, 'ev': {}, 'figs': [], 'code': [], 'hp': {}, 'numsent': [], 'caps': []}
    # secoes para ignorar referencias
    in_refs = False
    keep = []
    for pn, sec, s in sents:
        if sec.lower().startswith(STOPSEC): in_refs = True
        if not in_refs: keep.append((pn, sec, s))
    full_pages = collections.defaultdict(list)
    for pn, sec, s in keep: full_pages[pn].append((sec, s))
    for cat, d in ENT.items():
        for name, rx in d.items():
            r = re.compile(rx)
            hits = collections.Counter(); first = None
            for pn, sec, s in keep:
                k = len(r.findall(s))
                if k:
                    hits[pn] += k
                    if first is None: first = (pn, sec, s[:230])
            tot = sum(hits.values())
            if tot:
                res['ents'].setdefault(cat, {})[name] = {'n': tot, 'paginas': sorted(hits)[:8], 'primeira': first}
    # resumo
    ab = None
    for i, (pn, sec, s) in enumerate(keep):
        if re.match(r'^abstract|^resumo|^resumen', sec, re.I) or re.match(r'^(abstract|resumo)\b', s, re.I):
            ab = (pn, ' '.join(x[2] for x in keep[i:i + 7])[:1400]); break
    res['abstract'] = ab
    # frases-evidencia
    def pick(rx, n=3, secs=None, maxlen=240):
        r = re.compile(rx, re.I); out = []
        for pn, sec, s in keep:
            if secs and not re.search(secs, sec, re.I): continue
            if r.search(s):
                out.append({'p': pn, 's': sec[:60], 't': s[:maxlen]})
                if len(out) >= n: break
        return out
    res['ev']['area'] = pick(r'study (area|site|region)|is located in|located (in|at)|\bcovers? (an area|a total)', 2)
    res['ev']['periodo'] = pick(r'\b(19|20)\d\d\s?(?:–|-|to|and)\s?(19|20)\d\d\b|between [A-Z][a-z]+ (19|20)\d\d|from [A-Z][a-z]+ (19|20)\d\d', 2)
    res['ev']['resolucao'] = pick(r'\b\d+(?:[.,]\d+)?\s?(?:m|cm)\b[^.]{0,30}(resolution|GSD|pixel|spatial)|(resolution|GSD)[^.]{0,40}\b\d+(?:[.,]\d+)?\s?(?:m|cm)\b|\bmeters?\b[^.]{0,20}resolution', 3)
    res['ev']['n_imagens'] = pick(r'\d[\d,.]*\s+(image pairs|images|scenes|time series|sequences|patches|samples|tiles)\b', 3)
    res['ev']['referencia'] = pick(r'ground truth|reference (data|sample|map|label)|field (data|survey)|manually (annotat|label|digitiz|delineat)|interpret', 3)
    res['ev']['limitacoes'] = pick(r'limitation|limited by|future work|drawback|fails? to|struggle|cannot|not (able|possible) to', 3, secs=r'discussion|conclusion|limitation|result|future|^\d')
    res['ev']['tarefa'] = pick(r'we (propose|present|introduce|develop|evaluate|compare|investigate|tackle|address|study)|this (paper|study|work|research) (aims?|presents?|proposes?|investigates?|evaluates?|compares?)|the (aim|objective|purpose|goal) of', 2)
    for k, rx in HP.items():
        r = re.compile(rx)
        for pn, sec, s in keep:
            m = r.search(s)
            if m:
                res['hp'][k] = {'p': pn, 't': re.sub(r'\s+', ' ', m.group(0))[:80]}; break
    # numeros de resultado
    nr = re.compile(r'(F1|IoU|accuracy|precision|recall|kappa|mIoU|\bOA\b|RMSE|SeK|SCS|SCOT|mAP)[^.]{0,80}\d', re.I)
    num = re.compile(r'\d+(?:[.,]\d+)?\s?%|\b0[.,]\d{2,}\b')
    for pn, sec, s in keep:
        if nr.search(s) and num.search(s) and re.search(r'result|discussion|conclusion|abstract|experiment|evaluation|^\d', sec, re.I) and len(s) < 420:
            res['numsent'].append({'p': pn, 's': sec[:50], 't': s[:260]})
            if len(res['numsent']) >= 6: break
    # codigo e dados
    seen = set()
    for pn, sec, s in keep:
        for u in CODE.findall(s):
            u = u.rstrip('.,;')
            if u not in seen: seen.add(u); res['code'].append({'p': pn, 'u': u})
    res['code_stmt'] = pick(r'code (is|are|will be)? ?(publicly )?available|open[- ]source|data (is|are) available|available (at|on|from|in) (the )?(github|zenodo|repository)|our (complete )?code|data availability', 2)
    # figuras e legendas
    for p in pages:
        for f in p['figs']:
            res['figs'].append({'p': p['n'], 'f': f})
        for kind, t in p['lines']:
            m = CAP.match(t)
            if kind == 'T' and m:
                res['caps'].append({'p': p['n'], 'k': f'{m.group(1)} {m.group(2)}', 't': t[:200]})
    return res


if __name__ == '__main__':
    out = {}
    for d in sorted(os.listdir(OUT)):
        dd = f'{OUT}/{d}'
        if not os.path.isdir(dd) or not os.path.exists(f'{dd}/document.md'): continue
        pid = d.split('_')[0]
        try:
            out[pid] = analyse(f'{dd}/document.md', pid)
            out[pid]['dir'] = d
            man = json.load(open(f'{dd}/manifest.json', encoding='utf-8'))
            out[pid]['sha256'] = man['key']['sha256']; out[pid]['avisos'] = len(man.get('warnings', []))
            out[pid]['n_figs'] = man.get('figure_crops'); out[pid]['n_rasters'] = man.get('raster_objects')
            pg = json.load(open(f'{dd}/pages.json', encoding='utf-8'))
            out[pid]['paginas_pouco_texto'] = [p['page'] for p in pg if p.get('source_characters', 0) < 40]
            print(pid, out[pid]['pages'], 'pg', sum(len(v) for v in out[pid]['ents'].values()), 'ents', len(out[pid]['code']), 'codigo')
        except Exception as e:
            print(pid, 'ERRO', type(e).__name__, str(e)[:80])
    json.dump(out, open(f'{root}/dados/kb_extract.json', 'w', encoding='utf-8'), ensure_ascii=False)
    print('ok', len(out))
