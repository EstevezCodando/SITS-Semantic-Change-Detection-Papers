"""Biblioteca da base de conhecimento: carga de dados, nomes, busca de pagina por trecho, tokens e conceitos."""
import re, os, sys, json, unicodedata, collections, difflib

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kb_content as K
from kb_extract import parse, clean  # noqa: E402  (usa sys.argv[1] como raiz)

ROOT = sys.argv[1]
KB = f'{ROOT}/base_conhecimento'
DATA = f'{ROOT}/dados'
STOP = set('the a an of for and in on with using from to by via based de la el los las para con y da do em e um uma des du le les sur pour pour use'.split())


def fold(s):
    return unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode()


def norm(s):
    return re.sub(r'[^a-z0-9]', '', fold(s).lower())


def split_fm(txt):
    m = re.match(r'---\n(.*?)\n---\n(.*)', txt, re.S)
    meta = {}
    for l in m.group(1).split('\n'):
        if ': ' in l:
            k, v = l.split(': ', 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta, m.group(2).strip()


def load():
    cat = {r['id']: r for r in json.load(open(f'{DATA}/catalog.json', encoding='utf-8'))}
    kb = json.load(open(f'{DATA}/kb_extract.json', encoding='utf-8'))
    LP, SYN = {}, {}
    d = f'{DATA}/leitura_profunda'
    for f in sorted(os.listdir(d)):
        meta, body = split_fm(open(f'{d}/{f}', encoding='utf-8').read())
        if re.fullmatch(r'P\d+\.md', f): LP[f[:-3]] = (meta, body)
        elif f.startswith('_sintese_'): SYN[f] = (meta, body)
    return cat, kb, LP, SYN


def year_of(r):
    return (r.get('year_doc') if r.get('origin') == 'original' and r.get('year_doc') else r.get('oa_year')) or 's.d.'


def author_last(r):
    a = r.get('authors') or []
    return fold(a[0].split()[-1]).replace('-', '').replace("'", '') if a else 'Anon'


def short_title(t):
    words = [w for w in re.findall(r"[A-Za-z0-9]+", fold(t)) if w.lower() not in STOP and len(w) > 2]
    return ''.join(w[:1].upper() + w[1:] for w in words[:3])[:30] or 'Artigo'


def make_names(pids, cat):
    names, used = {}, set()
    for pid in pids:
        r = cat[pid]
        base = f"{author_last(r)}_{year_of(r)}_{short_title(r['title'])}"
        n, i = base, 0
        while n in used:
            i += 1; n = base + chr(96 + i)
        used.add(n); names[pid] = n
    return names


class Pages:
    """Texto por pagina (normalizado) para localizar trechos; P07 usa o HTML (secao em vez de pagina)."""
    def __init__(self, kb):
        self.pages = {}       # pid -> [(n, normtext)]
        self.html = {}
        for pid, v in kb.items():
            doc = f"{ROOT}/output/pdf/{v['dir']}/document.md"
            pg = parse(doc)
            self.pages[pid] = [(p['n'], norm(' '.join(t for _, t in p['lines']))) for p in pg]
        h = f'{DATA}/textos_extra/P07_mdpi_html.txt'
        if os.path.exists(h):
            self.html['P07'] = open(h, encoding='utf-8').read()

    def where(self, pid, snippet):
        if pid in self.html:
            t = self.html[pid]
            i = t.lower().find(snippet.lower()[:60])
            if i < 0:
                nt = norm(t)
                if norm(snippet)[:40] not in nt: return None
                # busca aproximada: acha a linha
                for ln in t.split('\n'):
                    if norm(snippet)[:30] in norm(ln): i = t.find(ln); break
                if i < 0: return None
            head = None
            for m in re.finditer(r'^(\d(?:\.\d)*\.?)\s+[A-Z][^\n]{2,70}$', t[:i + 1], re.M): head = m.group(1)
            return f'§ {head.strip(".")}' if head else 'início'
        ns = norm(snippet)
        if len(ns) < 12: return None
        for w in (ns, ns[:max(12, int(len(ns) * 0.7))], ns[:24]):
            for n, t in self.pages.get(pid, []):
                if w in t: return f'p. {n}'
        return None

    def vote(self, pid, text):
        """Pagina de um trecho longo (chunk antigo): vota com janelas."""
        if pid in self.html: return None
        ns = norm(text)
        if len(ns) < 60: return None
        wins = [ns[:50], ns[len(ns) // 3:len(ns) // 3 + 50], ns[2 * len(ns) // 3:2 * len(ns) // 3 + 50], ns[-50:]]
        votes = collections.Counter()
        for w in wins:
            for n, t in self.pages.get(pid, []):
                if w in t: votes[n] += 1
        return f'p. {votes.most_common(1)[0][0]}' if votes else None
