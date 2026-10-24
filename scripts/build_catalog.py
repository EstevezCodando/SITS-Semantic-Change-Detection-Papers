"""Etapa 1: le o documento original (P01-P80), junta os candidatos extras e confere cada
registro no OpenAlex. Gera catalog.json com metadados, flags de verificacao e URLs de PDF aberto.
Uso: python -I build_catalog.py <REVISAO_ORIGINAL.md> <saida catalog.json>
"""
import re, sys, json, urllib.request, urllib.error, urllib.parse, difflib, concurrent.futures as cf
sys.path.insert(0, __file__.rsplit('\\', 1)[0])
from extras import EXTRAS

sys.stdout.reconfigure(encoding='utf-8')
UA = {'User-Agent': 'Mozilla/5.0 (research-collection script)'}
TODAY = '2026-10-24'


def get(url):
    import time
    for attempt in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and attempt < 5:
                time.sleep(2 + attempt * 3)
                continue
            raise


def norm(t):
    return re.sub(r'[^a-z0-9]+', ' ', (t or '').lower()).strip()


def sim(a, b):
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()


SECTIONS = {  # faixas de IDs do documento original -> secao
    'A': range(1, 10), 'B': range(10, 23), 'C': range(23, 36), 'D': range(36, 41),
    'E': range(41, 48), 'R': range(48, 51), 'F': range(51, 56), 'G': range(56, 68),
    'H': range(68, 75), 'I': range(75, 81),
}


def section_of(n):
    for s, r in SECTIONS.items():
        if n in r:
            return s


def parse_original(path):
    txt = open(path, encoding='utf-8').read()
    recs = []
    for m in re.finditer(r'^### P(\d\d) — (.+?)\n(.*?)(?=^### |^## |\Z)', txt, re.S | re.M):
        n, title, body = int(m.group(1)), m.group(2).strip(), m.group(3)
        bullets = {}
        for b in re.finditer(r'^- \*\*(.+?):\*\*\s*(.*)$', body, re.M):
            bullets[b.group(1)] = b.group(2).strip()
        ref = bullets.get('Referência', '')
        fonte = bullets.get('Fonte', '')
        urls = re.findall(r'https?://[^\s)\]]+', fonte)
        code = ''
        for k, v in bullets.items():
            if k.startswith('Código') or k == 'Projeto':
                code += ' ' + ' '.join(re.findall(r'https?://[^\s)\]]+', v))
        ym = re.findall(r'\b(20[12]\d)\b', ref)
        kind = 'Artigo'
        if re.search(r'[Pp]reprint', ref): kind = 'Preprint'
        if re.search(r'[Dd]ataset|MUDS', ref): kind = 'Dataset'
        if section_of(n) == 'R': kind = 'Revisão'
        recs.append({
            'id': f'P{n:02d}', 'n': n, 'section': section_of(n), 'title': title, 'kind': kind,
            'ref': ref, 'fonte_urls': urls, 'code': code.split(), 'bullets': bullets,
            'year_doc': ym[0] if ym else '', 'origin': 'original',
        })
    return recs


def doi_from_urls(urls):
    for u in urls:
        m = re.match(r'https?://doi\.org/(10\.\S+)', u)
        if m: return m.group(1)
        m = re.match(r'https?://arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})', u)
        if m: return '10.48550/arXiv.' + m.group(1)
        m = re.match(r'https?://www\.mdpi\.com/2072-4292/(\d+)/(\d+)/(\d+)', u)
        if m: return '10.3390/rs%s%02d%04d' % (m.group(1), int(m.group(2)), int(m.group(3)))
    return ''


def fetch_work(doi, title):
    w = None
    if doi:
        try:
            w = get('https://api.openalex.org/works/doi:' + urllib.parse.quote(doi, safe='/:'))
        except Exception:
            w = None
    if w is None and title:
        try:
            res = get('https://api.openalex.org/works?per-page=5&search=' + urllib.parse.quote(title))
            best = max(res['results'], key=lambda x: sim(title, x.get('title')), default=None)
            if best and sim(title, best.get('title')) >= 0.80:
                w = best
        except Exception:
            pass
    return w


def summarize(w):
    pdfs = []
    for loc in ([w.get('best_oa_location')] + (w.get('locations') or [])):
        if loc and loc.get('pdf_url') and loc['pdf_url'] not in pdfs:
            pdfs.append(loc['pdf_url'])
    return {
        'oa_title': w.get('title'), 'oa_year': w.get('publication_year'),
        'oa_doi': (w.get('doi') or '').replace('https://doi.org/', ''),
        'authors': [a['author']['display_name'] for a in w.get('authorships', [])],
        'venue': ((w.get('primary_location') or {}).get('source') or {}).get('display_name') or '',
        'oa_type': w.get('type'), 'pdfs': pdfs, 'is_oa': (w.get('open_access') or {}).get('is_oa'),
        'oa_url': (w.get('open_access') or {}).get('oa_url'),
        'cited_by': w.get('cited_by_count'),
    }


def process(rec):
    doi = rec.get('doi') or doi_from_urls(rec.get('fonte_urls', []))
    w = fetch_work(doi, rec['title'] if not doi or rec['origin'] == 'original' else None)
    if w is None and doi:  # DOI nao indexado: tenta por titulo
        w = fetch_work('', rec['title'])
    if w is None and rec['origin'] == 'original':  # fallback: Crossref por titulo
        try:
            cr = get('https://api.crossref.org/works?rows=3&query.bibliographic=' + urllib.parse.quote(rec['title']))
            for it in cr['message']['items']:
                if sim(rec['title'], (it.get('title') or [''])[0]) >= 0.85:
                    doi = it['DOI']
                    w = fetch_work(doi, None)
                    rec['via_crossref'] = True
                    break
        except Exception:
            pass
    rec['doi'] = doi
    if w is None:
        rec['checked'] = False
        return rec
    rec.update(summarize(w))
    if not rec.get('title_known'):
        rec['title'] = rec['oa_title'] if rec['origin'] == 'extra' else rec['title']
    rec['title_sim'] = round(sim(rec['title'], rec['oa_title']), 2)
    # DOI resolvido com titulo diferente (ex.: preprint x versao publicada) ainda conta como conferido
    rec['checked'] = rec['title_sim'] >= 0.75 or (bool(doi) and rec['title_sim'] >= 0.4)
    return rec


if __name__ == '__main__':
    recs = parse_original(sys.argv[1])
    for r in recs:  # fontes sem DOI na pagina primaria (PMLR): usa o preprint equivalente
        if r['id'] == 'P11': r['doi'] = '10.48550/arXiv.2102.11958'
    for i, (doi, sec, kind, note, code) in enumerate(EXTRAS, start=81):
        recs.append({'id': f'P{i}', 'n': i, 'section': sec, 'title': '', 'kind': kind, 'doi': doi,
                     'note': note, 'code': [code] if code else [], 'origin': 'extra', 'fonte_urls': []})
    with cf.ThreadPoolExecutor(3) as ex:
        out = list(ex.map(process, recs))
    json.dump(out, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    bad = [r for r in out if not r.get('checked')]
    print(len(out), 'registros;', len(bad), 'nao conferidos automaticamente')
    for r in bad:
        print('  ', r['id'], r['title'][:70], r.get('doi'), r.get('title_sim'), r.get('oa_title', '')[:70] if r.get('oa_title') else '')
    noP = [r for r in out if r.get('checked') and not r.get('pdfs')]
    print(len(noP), 'conferidos sem PDF aberto no OpenAlex')
