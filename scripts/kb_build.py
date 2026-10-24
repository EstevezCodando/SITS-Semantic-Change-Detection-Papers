"""Constroi base_conhecimento/ (vault Obsidian) a partir de output/pdf (markdown), catalogo, extracao e fichas.
Uso: python -I kb_build.py <raiz>
"""
import re, os, sys, json, shutil, csv, hashlib, collections, zipfile, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_lib import *   # noqa
import kb_content as K
import kb_canvas as C

cat, kb, LP, SYN = load()
pages = Pages(kb)
PIDS = sorted(set(kb) | set(LP), key=lambda x: int(x[1:]))
NAMES = make_names(PIDS, cat)
_keep = {}   # arquivos de aparencia que o Obsidian gravou: preservados entre reconstrucoes
for _f in ('appearance.json',):
    _p = f'{KB}/.obsidian/{_f}'
    if os.path.exists(_p): _keep[_f] = open(_p, encoding='utf-8').read()
if os.path.isdir(KB): shutil.rmtree(KB)
FOLDERS = ['00_Painel', '01_Mapas', '02_Artigos', '03_Dados', '04_Preparo', '05_Metodos', '06_Validacao', '07_Resultados', '08_Monitoramento', '09_Lacunas', '90_Anexos', '99_Templates']
for f in FOLDERS: os.makedirs(f'{KB}/{f}', exist_ok=True)
NOTE_FOLDER = {}      # stem -> pasta
unresolved = []       # trechos nao localizados


def write(rel, text):
    p = f'{KB}/{rel}'
    os.makedirs(os.path.dirname(p), exist_ok=True)
    text = '\n'.join(re.sub(r'\[\[[^\]]*\]\]', lambda m: m.group(0).replace('\\|', '|').replace('|', '\\|'), l) if l.startswith('|') else l for l in text.split('\n'))
    open(p, 'w', encoding='utf-8').write(text)
    NOTE_FOLDER[os.path.splitext(os.path.basename(rel))[0]] = rel.split('/')[0]


def yq(s): return '"' + str(s).replace('\\', '\\\\').replace('"', '\\"') + '"'
def ylist(xs): return '[' + ', '.join(yq(x) for x in xs) + ']' if xs else '[]'
def label(pid): return f"{author_last(cat[pid])} {year_of(cat[pid])}"
def plink(pid, lab=None): return f"[[{NAMES[pid]}|{lab or label(pid)}]]"

# ------------------------------------------------------------------ tarefas (a partir de titulo + resumo; documentado como inferencia)
TASKS = {
 'Deteccao_Mudanca': ('Detecção de mudanças', r'change detection|detect(ing)? (land[- ]cover )?changes?|land cover change|change map', 'Identificar onde a superfície mudou entre datas.', 'Imagens de duas ou mais datas corregistradas.', 'Máscara binária de mudança ou mapa de transições.', 'Dados comparáveis entre datas (radiometria e geometria).', 'Binária não diz o que mudou; segmentação de uma imagem isolada não é evidência de mudança temporal.'),
 'MudancaSemantica': ('Mudança semântica (from–to)', r'semantic change|from-?to|change segmentation|land[- ]cover transition', 'Dizer onde mudou e de qual classe para qual classe.', 'Pares ou séries com classes de cobertura.', 'Mapas antes/depois e máscara de mudança.', 'Taxonomia fixa de classes.', 'Transições raras; número de classes cresce com N².'),
 'SITS': ('Séries temporais de imagens (SITS)', r'time[- ]series|\bSITS\b|multi-?temporal image|monthly (mosaics|series|composites)', 'Usar o histórico completo para localizar quando e o que mudou.', 'Cubo temporal de imagens.', 'Mapas por data, datas de ruptura.', 'Observações regulares e válidas.', 'Redundância entre datas próximas; lacunas por nuvem.'),
 'Desmatamento': ('Desmatamento', r'deforestation|forest loss|tree[- ]cover loss|forest cover', 'Mapear a supressão da cobertura arbórea.', 'Imagens ou mosaicos de floresta.', 'Máscaras de floresta/perda e datas.', 'Definição operacional de floresta.', 'Fogo e degradação podem ser contados como perda em produtos de referência.'),
 'DegradacaoFlorestal': ('Degradação e perturbação florestal', r'degradation|disturbance|selective logging|burn(ed|t)? area', 'Mapear perda parcial de estrutura (corte seletivo, fogo, estradas).', 'Mosaicos de alta resolução.', 'Mapas de degradação por tipo.', 'Padrão espacial reconhecível.', 'Pode não ser captada por classificadores de cobertura por data.'),
 'Edificacoes': ('Edificações e urbanização', r'building|construction|urban', 'Detectar novas construções e expansão urbana.', 'Mosaicos de alta resolução.', 'Polígonos ou máscaras de edificação.', 'Tamanho mínimo detectável.', 'Objetos de poucos pixels em 3–5 m.'),
 'Vias': ('Vias e estradas', r'\broads?\b|road network|road extraction', 'Detectar abertura e pavimentação de vias.', 'Imagens de alta resolução.', 'Máscaras/linhas de via.', 'Continuidade e largura mínima.', 'Largura de ~1 pixel em 5 m; conectividade importa.'),
 'Mineracao': ('Mineração', r'\bmining\b|\bmines?\b|garimpo', 'Detectar áreas e mudanças de mineração.', 'Imagens ópticas ou radar.', 'Polígonos de mineração.', 'Alvo separável do solo exposto natural.', 'Confusão com solo exposto e sombra.'),
 'ClassificacaoCobertura': ('Classificação de cobertura e uso da terra', r'land[- ]cover|land[- ]use|\bLULC\b', 'Mapear classes de cobertura por data.', 'Imagens e rótulos.', 'Mapa temático.', 'Classes mutuamente exclusivas.', 'Classificar uma data não valida transições mensais.'),
 'SegmentacaoSemantica': ('Segmentação semântica', r'semantic segmentation', 'Atribuir uma classe a cada pixel.', 'Patches rotulados.', 'Mapa de classes.', 'Rótulos densos.', 'Uma imagem isolada não é evidência de detecção temporal.'),
}

# ------------------------------------------------------------------ suporte dos conceitos
THR = {'sensor': 3, 'dataset': 2, 'metodo': 3, 'metrica': 3, 'ferramenta': 3, 'preparo': 3, 'validacao': 3, 'monitoramento': 6}
VERB = {'sensor': 'utiliza dado/sensor', 'dataset': 'emprega conjunto de dados', 'metodo': 'utiliza método', 'metrica': 'é avaliado por', 'ferramenta': 'usa ferramenta',
        'preparo': 'aplica etapa de preparo', 'validacao': 'adota desenho de validação', 'monitoramento': 'discute aspecto de monitoramento'}
concepts = {}   # fileid -> dict
for (cat_, name), tup in K.CONCEPTS.items():
    fid, folder, titulo, tipo, d, fin, ent, sai, pres, lim = tup
    concepts[fid] = dict(cat=cat_, name=name, folder=folder, titulo=titulo, tipo=tipo, d=d, fin=fin, ent=ent, sai=sai, pres=pres, lim=lim, sup=[])
for fid, (folder, titulo, tipo, d, fin, ent, sai, pres, lim, ps) in K.MANUAL_CONCEPTS.items():
    concepts[fid] = dict(cat='manual', name=fid, folder=folder, titulo=titulo, tipo=tipo, d=d, fin=fin, ent=ent, sai=sai, pres=pres, lim=lim, sup=[], manual=ps)
for tid, (titulo, rx, d, ent, sai, pres, lim) in TASKS.items():
    concepts[tid] = dict(cat='tarefa', name=tid, folder='05_Metodos', titulo=titulo, tipo='tarefa', d=d, fin=d, ent=ent, sai=sai, pres=pres, lim=lim, sup=[], rx=re.compile(rx, re.I))

by_key = {(c['cat'], c['name']): fid for fid, c in concepts.items() if c['cat'] not in ('manual', 'tarefa')}
paper_concepts = collections.defaultdict(list)   # pid -> [(fid, verb, n, paginas, primeira)]
for pid in PIDS:
    v = kb.get(pid)
    if v:
        for cat_, d in v['ents'].items():
            for name, e in d.items():
                fid = by_key.get((cat_, name))
                if not fid: continue
                if e['n'] >= THR[cat_] and len(e['paginas']) >= 2:
                    paper_concepts[pid].append((fid, VERB[cat_], e['n'], e['paginas'], e['primeira']))
    # tarefas por titulo+resumo
    ab = (v['abstract'][1] if v and v.get('abstract') else '')
    for tid, c in concepts.items():
        if c['cat'] == 'tarefa' and (c['rx'].search(cat[pid]['title']) or (ab and len(c['rx'].findall(ab)) >= 1)):
            paper_concepts[pid].append((tid, 'trata a tarefa', 0, [], None))
for fid, c in concepts.items():
    for pid in c.get('manual', []):
        if pid in PIDS: paper_concepts[pid].append((fid, 'referencia (suporte manual da leitura)', 0, [], None))
# suporte manual para conceitos do NICFI e outros presentes nas fichas
for extra_pid, fid in [('P01', 'PlanetNICFI'), ('P07', 'PlanetNICFI'), ('P07', 'GoogleEarthEngine'), ('P07', 'Textura')]:
    if fid in concepts and extra_pid in PIDS and not any(x[0] == fid for x in paper_concepts[extra_pid]):
        paper_concepts[extra_pid].append((fid, VERB.get(concepts[fid]['cat'], 'referencia'), 0, [], None))
# links curados pela leitura substituem a deteccao automatica nos artigos lidos (mantem as paginas da extracao quando o conceito coincide)
for pid, fl in K.LINKS_MANUAL.items():
    if pid not in PIDS: continue
    old = {t[0]: t for t in paper_concepts[pid]}
    new = []
    for fid in fl:
        if fid not in concepts: continue
        new.append(old.get(fid) or (fid, 'referência (curado pela leitura)', 0, [], None))
    new += [t for t in paper_concepts[pid] if concepts[t[0]]['cat'] == 'manual' and t[0] not in {x[0] for x in new}]
    paper_concepts[pid] = new
for pid, lst in paper_concepts.items():
    for fid, verb, n, pg, first in lst:
        concepts[fid]['sup'].append((pid, verb, n, pg, first))
ACTIVE = {fid for fid, c in concepts.items() if len(c['sup']) >= 2}
# limita links por artigo (evita conectar tudo a tudo): mantem os mais frequentes por categoria
CAP = {'sensor': 3, 'dataset': 4, 'metodo': 6, 'metrica': 4, 'ferramenta': 3, 'preparo': 5, 'validacao': 4, 'monitoramento': 3, 'tarefa': 4, 'manual': 4}
# artigos nao lidos (so extracao automatica) ligam apenas a sensor, dado, tarefa e poucos metodos: evita que conceitos genericos (rotulagem, F1, IoU...) virem
# nos centrais ligados a tudo. Conceitos de preparo, validacao e metrica so se conectam a artigos que alguem leu.
CAP_AUTO = {'sensor': 3, 'dataset': 3, 'metodo': 3, 'tarefa': 3, 'manual': 3}
MIN_AUTO_METODO = 8   # ocorrencias minimas para o metodo de um artigo nao lido virar link
for pid in list(paper_concepts):
    byc = collections.defaultdict(list)
    lido = pid in LP
    for t in paper_concepts[pid]:
        if t[0] not in ACTIVE or (pid, t[0]) in K.EXCLUDE_LINKS: continue
        if not lido and concepts[t[0]]['cat'] == 'metodo' and t[2] < MIN_AUTO_METODO: continue
        byc[concepts[t[0]]['cat']].append(t)
    keep = []
    for cat_, lst in byc.items():
        cap = (CAP if lido else CAP_AUTO).get(cat_, 0 if not lido else 4)
        if pid in K.LINKS_MANUAL: cap = 99
        keep += sorted(lst, key=lambda x: -x[2])[:cap]
    paper_concepts[pid] = keep
for fid in concepts: concepts[fid]['sup'] = []
for pid, lst in paper_concepts.items():
    for fid, verb, n, pg, first in lst: concepts[fid]['sup'].append((pid, verb, n, pg, first))
ACTIVE = {fid for fid, c in concepts.items() if len(c['sup']) >= 2}
for fid in concepts:
    if fid not in ACTIVE: concepts[fid]['sup'] = []
for pid in list(paper_concepts):
    paper_concepts[pid] = [t for t in paper_concepts[pid] if t[0] in ACTIVE]
CNAME = {fid: fid for fid in ACTIVE}


def clink(fid): return f"[[{fid}|{concepts[fid]['titulo']}]]" if fid in ACTIVE else concepts[fid]['titulo']


def resolve(text, ctx=None):
    """Resolve tokens «Pxx», «Pxx|trecho», «C:Chave», «M:Matriz»."""
    def rp(m):
        pid, snip = m.group(1), m.group(2)
        if pid not in NAMES: return label(pid) if pid in cat else pid
        out = plink(pid)
        if snip:
            w = pages.where(pid, snip)
            if w: out += f' ({w})'
            else:
                out += ' (localização não encontrada)'; unresolved.append((ctx, pid, snip))
        return out
    def rw(m):
        w = pages.where(m.group(1), m.group(2))
        if w: return f'({w})'
        unresolved.append((ctx, m.group(1), m.group(2))); return '(localização não encontrada)'
    text = re.sub(r'«W:(P\d+)\|([^»]+)»', rw, text)
    text = re.sub(r'«(P\d+)(?:\|([^»]+))?»', rp, text)
    text = re.sub(r'«C:([A-Za-z0-9_]+)»', lambda m: clink(m.group(1)) if m.group(1) in concepts else m.group(1), text)
    text = re.sub(r'«M:([A-Za-z_]+)»', lambda m: '[[' + {'Matriz': 'Matriz_Comparativa'}.get(m.group(1), m.group(1)) + ']]', text)
    return text


# ------------------------------------------------------------------ ficha -> secoes
CHUNKS = {}
def chunk_info(pid):
    if pid not in CHUNKS:
        p = f'{DATA}/chunks/{pid}.jsonl'
        CHUNKS[pid] = {json.loads(l)['id']: json.loads(l) for l in open(p, encoding='utf-8')} if os.path.exists(p) else {}
    return CHUNKS[pid]


def conv_ficha(pid, text):
    unresolved_local = 0
    def rc(m):
        cid = m.group(2); c = chunk_info(m.group(1)).get(cid)
        if not c: return 'loc?'
        w = pages.vote(pid, c['texto']) if pid in kb else None
        if not w:
            t = c.get('titulo_secao', '')
            mm = re.match(r'(\d(?:\.\d)*)', t)
            w = f'§ {mm.group(1)}' if mm else (f'seção “{t[:40]}”' if t else 'loc?')
        return w
    text = re.sub(r'\[\[(P\d+) chunks#\^(P\d+_c\d+)\|c\d+\]\]', rc, text)
    # compacta listas de paginas dentro de parenteses
    def compact(m):
        items = [x.strip() for x in m.group(1).split(',')]
        seen, out = [], []
        for x in items:
            if x not in seen: seen.append(x)
        pg = [x[3:] for x in seen if x.startswith('p. ')]
        rest = [x for x in seen if not x.startswith('p. ')]
        res = (['p. ' + ', '.join(pg)] if pg else []) + rest
        return '(' + ', '.join(res) + ')'
    text = re.sub(r'\(((?:p\. \d+|§ [\d.]+|seção “[^”]*”|loc\?)(?:, (?:p\. \d+|§ [\d.]+|seção “[^”]*”|loc\?))*)\)', compact, text)
    # wikilinks de artigos antigos -> novos
    def rl(m):
        target = m.group(1)
        mm = re.match(r'(?:LP )?(P\d+) ', target)
        if mm and mm.group(1) in NAMES and not target.startswith('LP '): return plink(mm.group(1), (m.group(2) or '|').lstrip('|') or label(mm.group(1)))
        disp = (m.group(2) or '|' + target).lstrip('|')
        return disp
    text = re.sub(r'\[\[([^\]|#]+)(\|[^\]]*)?\]\]', rl, text)
    return text


def ficha_sections(pid):
    if pid not in LP: return {}
    meta, body = LP[pid]
    body = conv_ficha(pid, body)
    parts = re.split(r'^## ', body, flags=re.M)
    secs = collections.OrderedDict()
    for p in parts[1:]:
        h, _, rest = p.partition('\n')
        secs[h.strip()] = rest.strip()
    return secs


def sect_of(h):
    hl = h.lower()
    if 'limite' in hl or 'lacuna' in hl or 'não verificado' in hl or 'o que não' in hl: return 9
    if 'reaproveitar' in hl or 'cuidado' in hl or 'teste proposto' in hl or 'como entra' in hl or 'nosso pipeline' in hl: return 11
    if 'pergunta' in hl or 'escopo' in hl or 'o que o artigo afirma' in hl: return 2
    if 'amostragem e part' in hl: return 5
    if 'rótulo' in hl or 'rotulag' in hl: return 5
    if ('dado' in hl and 'método' not in hl) or 'dataset' in hl: return 4
    if 'código' in hl or 'reprodut' in hl: return 10
    if 'resultado' in hl or 'conclus' in hl or 'evidência independente' in hl: return 8
    if 'métrica' in hl or 'partiç' in hl or 'divis' in hl or 'avaliação' in hl or 'regimes' in hl: return 7
    return 6


STATUS = {}
for pid in PIDS:
    if pid in LP:
        STATUS[pid] = 'lido (profundo)' if LP[pid][0].get('leitura', '').startswith('profunda') else 'lido (parcial)'
    else:
        STATUS[pid] = 'extraído automaticamente (não lido)'
TIER = {pid: K.RELEV.get(pid, ('D', ''))[0] for pid in PIDS}
TIER_WHY = {pid: (K.RELEV[pid][1] if pid in K.RELEV else 'não avaliada: texto não lido; ver a posição no ranking de relevância automática em [[Pendencias_Leitura]].') for pid in PIDS}

# ------------------------------------------------------------------ estrategia temporal e demais campos automaticos
BI = re.compile(r'bi-?temporal|image pairs?|pairs of images|before and after|two (dates|images|time)', re.I)
SE = re.compile(r'time[- ]series|\bSITS\b|multi-?temporal|image sequence|monthly (composites|mosaics|series)|temporal (attention|sequence)', re.I)
RAW = {}
def raw_text(pid):
    if pid not in RAW:
        v = kb.get(pid)
        if v:
            pg = parse(f"{ROOT}/output/pdf/{v['dir']}/document.md")
            RAW[pid] = ' '.join(t for p in pg for k, t in p['lines'] if k == 'T')
        else: RAW[pid] = ''
    return RAW[pid]


def temporal(pid):
    t = raw_text(pid); b = len(BI.findall(t)); s = len(SE.findall(t))
    if not t: return 'não informado'
    if s >= 8 and s >= 2 * b: return f'série temporal (auto: {s} menções vs {b} de pares)'
    if b >= 5 and b > s / 2 and s >= 5: return f'bitemporal e série (auto: {b} pares; {s} série)'
    if b >= 5: return f'bitemporal / pares (auto: {b} menções)'
    return 'imagem única ou não detectado (auto)'


def resolutions(pid):
    v = kb.get(pid)
    if not v: return []
    vals = []
    rx = re.compile(r'(\d+(?:[.,]\d+)?)\s?(m|cm)\b')
    for e in v['ev']['resolucao']:
        for m in rx.finditer(e['t']):
            val = f"{m.group(1)} {m.group(2)}"
            if val not in [x[0] for x in vals]: vals.append((val, e['p']))
    return vals[:3]


def task_names(pid):
    return [concepts[t[0]]['titulo'] for t in paper_concepts[pid] if concepts[t[0]]['cat'] == 'tarefa']


def codigo(pid):
    v = kb.get(pid)
    if not v: return 'não informado'
    urls = [c for c in v['code'] if re.search(r'github|gitlab|huggingface', c['u'])]
    data = [c for c in v['code'] if re.search(r'zenodo|figshare|osf', c['u'])]
    if urls: return f"sim: {urls[0]['u'].replace('https://', '')[:70]} (p. {urls[0]['p']})"
    if data: return f"dados: {data[0]['u'].replace('https://', '')[:60]} (p. {data[0]['p']})"
    if v['code_stmt']: return f"declarado sem URL localizada (p. {v['code_stmt'][0]['p']})"
    return 'não informado'


def cites(pid, cat_, k=3, minn=3):
    v = kb.get(pid)
    if not v: return []
    items = sorted(v['ents'].get(cat_, {}).items(), key=lambda x: -x[1]['n'])
    return [(n, e) for n, e in items if e['n'] >= minn][:k]


def pgs(pages_):
    return ', '.join(str(p) for p in pages_[:5])


def ev_lines(pid, key, n=3):
    v = kb.get(pid)
    if not v: return []
    return [f"- “{e['t']}” (p. {e['p']}, seção {e['s'] or 'início'})" for e in v['ev'].get(key, [])[:n]]


def monitor_class(pid):
    if pid in K.MONITORAMENTO_MANUAL:
        c, t = K.MONITORAMENTO_MANUAL[pid]
        return c, resolve(t, f'monitor {pid}')
    v = kb.get(pid)
    if not v: return 'não avaliado (sem texto)', ''
    m = v['ents'].get('monitoramento', {})
    g = lambda k: m.get(k, {}).get('n', 0)
    if g('Sistema operacional') >= 3 and (g('Alertas') >= 3 or g('Quase tempo real') >= 3):
        return 'candidato a sistema operacional (verificar no texto)', f"menções: operacional {g('Sistema operacional')}, alertas {g('Alertas')}, quase tempo real {g('Quase tempo real')}"
    return 'retrospectivo (sem evidência extraída de operação contínua)', ''


# ------------------------------------------------------------------ nota de artigo
def article(pid):
    r = cat[pid]; v = kb.get(pid); name = NAMES[pid]
    fs = ficha_sections(pid)
    byS = collections.defaultdict(list)
    for h, txt in fs.items(): byS[sect_of(h)].append((h, txt))
    pc = paper_concepts[pid]
    groups = collections.defaultdict(list)
    for fid, verb, n, pg, first in pc: groups[concepts[fid]['cat']].append((fid, verb, n, pg, first))
    def yl(cats):
        return ylist([f"[[{f}|{concepts[f]['titulo']}]]" for c_ in cats for f, *_ in groups.get(c_, [])])
    authors = (r.get('authors') or [])[:8]
    npg = v['pages'] if v else None
    tipo_doc = ('artigo completo (texto integral convertido)' if v and npg > 4 else 'artigo curto (≤4 páginas; verificar)' if v else ('artigo completo (HTML aberto)' if pid == 'P07' else 'sem texto integral (resumo, documentação ou repositório)'))
    fm = ['---', 'tipo: artigo', f'id_origem: {pid}', f'titulo: {yq(r["title"])}', f'ano: {year_of(r)}', f'autores: {ylist(authors) if authors else "[]"}',
          f'doi: {yq(r.get("doi") or "não informado")}', f'arquivo_fonte: {yq("coleta/" + r["pdf_file"]) if r.get("pdf_file") else yq("não informado" if pid != "P07" else "HTML MDPI (sem PDF em coleta/)")}',
          f'markdown_fonte: {yq("output/pdf/" + v["dir"] + "/document.md") if v else yq("não informado")}', f'paginas: {npg if npg else "não informado"}', f'tipo_documento: {yq(tipo_doc)}',
          f'status_leitura: {yq(STATUS[pid])}', f'relevancia_objetivo: {yq(TIER[pid])}', f'tarefas: {yl(["tarefa"])}', f'sensores: {yl(["sensor"])}', f'conjuntos_dados: {yl(["dataset"])}', f'metodos: {yl(["metodo"])}',
          f'preparo: {yl(["preparo"])}', f'validacao: {yl(["validacao", "metrica"])}', f'ferramentas: {yl(["ferramenta"])}',
          f'tags: [artigo, leitura/{"profunda" if STATUS[pid].startswith("lido (p") and "profundo" in STATUS[pid] else "parcial" if "parcial" in STATUS[pid] else "automatica"}, relevancia/{TIER[pid]}]', '---', '']
    body = [f'# {label(pid)} — {r["title"]}', '',
            '> **Convenção desta nota.** *Evidência do artigo* traz fatos com página (p.), seção (§) ou “não informado”. *Interpretação* é a leitura da base de conhecimento e aparece sempre sob esse rótulo. '
            'Blocos “detectado automaticamente” vêm de busca por padrões no texto convertido e **devem ser conferidos na página citada**.', '']
    body.append(f'**Situação da leitura:** {STATUS[pid]}. ' + ('Fichas de leitura profunda usadas como evidência.' if pid in LP else 'Nenhuma leitura humana: seções preenchidas por extração automática; onde nada foi detectado, consta “não informado”.'))
    body.append('')
    body.append(f'**Relevância para o objetivo** (detectar automaticamente mudanças de cobertura com imagem óptica Planet de ~5 m: início de construção, supressão de vegetação, vias): **{TIER[pid]}** — {TIER_WHY[pid]}')
    body.append('')
    # 1 referencia
    body += ['## 1. Referência bibliográfica e acesso ao original', '',
             f'- **Referência:** {", ".join(authors[:4]) + (" et al." if len(r.get("authors") or []) > 4 else "") if authors else "autoria não informada no catálogo"} ({year_of(r)}). {r["title"]}. {(r.get("venue") or "veículo não informado").split("/")[0]}. Tipo no catálogo: {r["kind"]}.',
             f'- **DOI/URL:** {("https://doi.org/" + r["doi"]) if r.get("doi") else "não informado"}',
             f'- **Arquivo de origem:** `{("coleta/" + r["pdf_file"]) if r.get("pdf_file") else ("HTML MDPI aberto (sem PDF em coleta/)" if pid == "P07" else "não disponível em coleta/ (acesso restrito ou bloqueado)")}`',
             f'- **Texto convertido (Markdown) e figuras:** `{("output/pdf/" + v["dir"] + "/document.md") if v else "não informado"}`' + (f' — {npg} páginas, {v["n_figs"]} recortes de figuras, {v["avisos"]} avisos de conversão' if v else ''),
             f'- **Tipo de documento:** {tipo_doc}.']
    if v and v['paginas_pouco_texto']: body.append(f'- **Atenção:** páginas com pouco texto extraível (possível OCR): {v["paginas_pouco_texto"]}.')
    body.append('')
    # 2 problema
    body += ['## 2. Problema investigado e contribuição principal', '']
    if byS.get(2):
        for h, t in byS[2]: body += ['**Evidência (leitura):**', '', t, '']
    if v and v.get('abstract'):
        body += [f'**Resumo detectado automaticamente (p. {v["abstract"][0]}):** {v["abstract"][1][:900]}…', '']
    elif not byS.get(2):
        body += ['Resumo: não localizado no texto convertido.', '']
    body += ev_lines(pid, 'tarefa', 2) or []
    body.append('')
    # 3 area e periodo
    body += ['## 3. Área de estudo e período analisado', '']
    a = ev_lines(pid, 'area', 2); p_ = ev_lines(pid, 'periodo', 2)
    body += (['**Detectado automaticamente (verificar):**'] + a + p_) if (a or p_) else ['Não informado (nenhum trecho de área ou período detectado automaticamente).' if pid not in LP else 'Ver seção 4 (dados), que traz área e período quando informados pelo artigo.']
    body.append('')
    # 4 dados
    body += ['## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo', '']
    for h, t in byS.get(4, []): body += ['**Evidência (leitura):**', '', t, '']
    auto = []
    for n, e in cites(pid, 'sensor', 4, 2): auto.append(f'- sensor/produto **{n}**: {e["n"]} ocorrências (p. {pgs(e["paginas"])})')
    for n, e in cites(pid, 'dataset', 4, 2): auto.append(f'- conjunto de dados **{n}**: {e["n"]} ocorrências (p. {pgs(e["paginas"])})')
    for val, p_ in resolutions(pid): auto.append(f'- resolução mencionada: {val} (p. {p_})')
    auto += ev_lines(pid, 'n_imagens', 3) + ev_lines(pid, 'referencia', 2)
    body += (['**Detectado automaticamente (verificar):**'] + auto) if auto else ['Não informado (nada detectado automaticamente).' if pid not in LP else '']
    body.append('')
    # 5 preparo
    body += ['## 5. Preparação: nuvens, correções, corregistro, reamostragem, mosaicos, normalização, índices, texturas, recortes e rotulagem', '']
    for h, t in byS.get(5, []): body += [f'**Evidência (leitura) — {h}:**', '', t, '']
    auto = [f'- **{n}**: {e["n"]} ocorrências (p. {pgs(e["paginas"])})' for n, e in cites(pid, 'preparo', 6, 2)]
    body += (['**Detectado automaticamente (verificar):**'] + auto) if auto else ['Não informado (nada detectado automaticamente).' if pid not in LP else '']
    body.append('')
    # 6 analise
    body += ['## 6. Análise: tarefa, modelos, atributos, arquitetura, estratégia temporal, treinamento, hiperparâmetros e baselines', '']
    for h, t in byS.get(6, []): body += [f'**Evidência (leitura) — {h}:**', '', t, '']
    body.append(f'- **Estratégia temporal (detecção automática, verificar):** {temporal(pid)}')
    auto = [f'- método/família **{n}**: {e["n"]} ocorrências (p. {pgs(e["paginas"])})' for n, e in cites(pid, 'metodo', 6, 3)]
    body += (['**Métodos detectados automaticamente:**'] + auto) if auto else []
    if v and v['hp']: body += ['**Hiperparâmetros detectados automaticamente (verificar):**'] + [f'- {k}: “{h_["t"]}” (p. {h_["p"]})' for k, h_ in v['hp'].items()]
    body.append('')
    # 7 validacao
    body += ['## 7. Validação: divisão espacial e temporal, independência, desbalanceamento, vazamento e testes externos', '']
    for h, t in byS.get(7, []): body += [f'**Evidência (leitura) — {h}:**', '', t, '']
    auto = [f'- **{n}**: {e["n"]} ocorrências (p. {pgs(e["paginas"])})' for n, e in cites(pid, 'validacao', 6, 2)]
    auto += [f'- métrica **{n}**: {e["n"]} ocorrências (p. {pgs(e["paginas"])})' for n, e in cites(pid, 'metrica', 4, 3)]
    body += (['**Detectado automaticamente (verificar):**'] + auto) if auto else ['Não informado (nada detectado automaticamente).' if pid not in LP else '']
    body.append('')
    # 8 resultados
    body += ['## 8. Resultados: métricas, valores, classes, conjunto avaliado e incertezas', '']
    for h, t in byS.get(8, []): body += [f'**Evidência (leitura) — {h}:**', '', t, '']
    if v and v['numsent']:
        body += ['**Trechos numéricos detectados automaticamente (verificar):**'] + [f'- “{e["t"]}” (p. {e["p"]}, seção {e["s"]})' for e in v['numsent'][:4]]
    elif not byS.get(8):
        body += ['Não informado (nenhum trecho com métrica e valor detectado).']
    if not v:
        body += ['', 'Páginas: não informado (leitura feita sem texto integral convertido; ver a fonte na seção 1).']
    body.append('')
    # 9 limitacoes
    body += ['## 9. Limitações e condições de aplicabilidade', '']
    for h, t in byS.get(9, []): body += [f'**Evidência (leitura) — {h}:**', '', t, '']
    lim = ev_lines(pid, 'limitacoes', 3)
    body += (['**Trechos detectados automaticamente (verificar contexto):**'] + lim) if lim else ([] if byS.get(9) else ['Não informado (nenhum trecho de limitação detectado).'])
    body.append('')
    # 10 reprodutibilidade
    body += ['## 10. Reprodutibilidade: código, dados, dependências e informações ausentes', '']
    for h, t in byS.get(10, []): body += [t, '']
    rep = [f'- **Código/dados:** {codigo(pid)}']
    if v:
        for c_ in v['code'][:4]: rep.append(f'- URL citada: {c_["u"]} (p. {c_["p"]})')
        for e in v['code_stmt'][:2]: rep.append(f'- declaração: “{e["t"]}” (p. {e["p"]})')
        miss = [k for k in ('taxa de aprendizado', 'batch', 'épocas/iterações', 'otimizador', 'perda') if k not in v['hp']]
        if miss: rep.append(f'- hiperparâmetros **não detectados** automaticamente: {", ".join(miss)} (podem existir no texto; verificar).')
    body += rep + ['']
    # 11 aplicabilidade
    body += ['## 11. Aplicabilidade ao monitoramento contínuo', '']
    cl, why = monitor_class(pid)
    body += [f'- **Classificação (evidência):** {cl}. {why}']
    v_m = (v or {}).get('ents', {}).get('monitoramento', {})
    if v_m: body.append('- menções de termos de monitoramento (contagem, não avaliação): ' + '; '.join(f'{n} {e["n"]} (p. {pgs(e["paginas"])})' for n, e in sorted(v_m.items(), key=lambda x: -x[1]['n'])[:5]))
    for h, t in byS.get(11, []): body += ['', f'**Interpretação — {h}:**', '', t]
    body.append('')
    # 12 relacoes
    body += ['## 12. Relações justificadas com outras notas', '']
    body.append('**Conceitos (ligam o estudo ao mapa conceitual; a relação está descrita ao lado do link):**')
    for fid, verb, n, pg, first in pc:
        c = concepts[fid]
        det = f' — {n} ocorrências (p. {pgs(pg)})' if n else ' — suporte vindo da leitura/título/resumo'
        body.append(f'- {verb}: [[{fid}|{c["titulo"]}]]{det}')
    rel = [x for x in K.RELACOES if pid in (x[0], x[1])]
    if rel:
        body += ['', '**Comparações substantivas com outros artigos:**']
        for a_, b_, relt, expl in rel:
            other = b_ if a_ == pid else a_
            if other not in NAMES: continue
            if a_ == pid: body.append(f'- este artigo {relt} {plink(other)} — {resolve(expl, f"rel {a_}-{b_}")}')
            else: body.append(f'- {plink(a_)} {relt} este artigo — {resolve(expl, f"rel {a_}-{b_}")}')
    if not pc and not rel: body.append('- Nenhuma relação com suporte suficiente foi criada para este artigo (evita ligações por coincidência de palavras).')
    # figuras
    figs = FIGS.get(pid, [])
    if figs:
        body += ['', '## Figuras selecionadas', '']
        for f in figs: body += [f'![[{f["file"]}|520]]', f'*{f["cap"]} (p. {f["p"]}; recorte do PDF convertido)*', '']
    body += ['', '## Anotações do leitor', '', '- ']
    write(f'02_Artigos/{name}.md', '\n'.join(fm + body) + '\n')


# ------------------------------------------------------------------ figuras (selecao por legenda)
FIGS = {}
import struct
def png_ok(path):
    # so embute recortes que parecem figuras inteiras (largura >= 500 px e altura >= 150 px); componentes pequenos sao ignorados
    try:
        with open(path, 'rb') as f: h = f.read(24)
        w, hh = struct.unpack('>II', h[16:24])
        return w >= 500 and hh >= 150
    except Exception:
        return False


def pick_figs():
    kw1 = re.compile(r'architecture|overview|pipeline|workflow|framework|methodolog|scheme|study area|location|flowchart', re.I)
    kw2 = re.compile(r'result|comparison|qualitative|prediction|example', re.I)
    for pid in PIDS:
        if pid not in LP or pid not in kb: continue
        v = kb[pid]; src = f"{ROOT}/output/pdf/{v['dir']}"
        chosen = []
        anyfig = re.compile(r'.')
        for rx in (kw1, kw2, kw1, anyfig, anyfig):
            for c in v['caps']:
                if not c['k'].lower().startswith(('fig',)): continue
                if rx.search(c['t']) and not any(x['key'] == (c['p'], c['k']) for x in chosen):
                    imgs = [f['f'] for f in v['figs'] if f['p'] == c['p'] and os.path.exists(f'{src}/{f["f"]}') and png_ok(f'{src}/{f["f"]}')]
                    if not imgs: continue
                    best = max(imgs, key=lambda f: os.path.getsize(f'{src}/{f}'))
                    chosen.append(dict(key=(c['p'], c['k']), img=best, p=c['p'], cap=c['t'][:140])); break
            if len(chosen) >= 3: break
        out = []
        for i, c in enumerate(chosen):
            fname = f"{NAMES[pid]}_p{c['p']}_{c['key'][1].replace(' ', '')}.png"
            os.makedirs(f'{KB}/90_Anexos/figuras', exist_ok=True)
            shutil.copyfile(f'{src}/{c["img"]}', f'{KB}/90_Anexos/figuras/{fname}')
            out.append(dict(file=fname, p=c['p'], cap=c['cap']))
        FIGS[pid] = out


pick_figs()
for pid in PIDS: article(pid)
print('artigos', len(PIDS), '| figuras', sum(len(v) for v in FIGS.values()), '| conceitos ativos', len(ACTIVE))

exec(compile(open(os.path.join(HERE, 'kb_build2.py'), encoding='utf-8').read(), 'kb_build2.py', 'exec'))
