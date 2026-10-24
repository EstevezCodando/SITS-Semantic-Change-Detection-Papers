"""Etapa 2: baixa PDFs de acesso aberto listados no catalogo para a pasta coleta/.
So usa locais abertos informados pelo OpenAlex e o PDF do arXiv; nao contorna acesso pago.
Uso: python -I download_pdfs.py dados/catalog.json coleta
"""
import re, sys, os, json, urllib.request, urllib.error, concurrent.futures as cf, unicodedata

sys.stdout.reconfigure(encoding='utf-8')
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36',
      'Accept': 'application/pdf,*/*'}


def slug(t, n=60):
    t = unicodedata.normalize('NFKD', t or '').encode('ascii', 'ignore').decode()
    return re.sub(r'[^A-Za-z0-9]+', '-', t).strip('-')[:n]


def filename(r):
    au = (r.get('authors') or ['Anon'])[0].split()[-1]
    return f"{r['id']}_{slug(au, 20)}{r.get('oa_year') or ''}_{slug(r.get('title') or r.get('oa_title'))}.pdf"


def candidates(r):
    c = []
    m = re.match(r'10\.48550/arxiv\.(.+)', (r.get('doi') or '').lower())
    if m: c.append('https://arxiv.org/pdf/' + m.group(1))
    for u in r.get('fonte_urls', []):
        m = re.match(r'https?://arxiv\.org/(?:abs|html)/(\d{4}\.\d{4,5})', u)
        if m: c.append('https://arxiv.org/pdf/' + m.group(1))
    c += r.get('pdfs', [])
    if r.get('oa_url') and r['oa_url'] not in c: c.append(r['oa_url'])
    seen, out = set(), []
    for u in c:
        if u not in seen: seen.add(u); out.append(u)
    return out


def fetch(url, dest):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read(60_000_000)
    if not data.startswith(b'%PDF') or len(data) < 30_000:
        raise ValueError('nao e PDF')
    open(dest, 'wb').write(data)
    return len(data)


def work(r, outdir):
    dest = os.path.join(outdir, filename(r))
    if os.path.exists(dest) and os.path.getsize(dest) > 30_000:
        r['pdf_file'], r['pdf_source'] = os.path.basename(dest), r.get('pdf_source', 'ja existente')
        return r
    errs = []
    for u in candidates(r):
        try:
            size = fetch(u, dest)
            r['pdf_file'], r['pdf_source'], r['pdf_bytes'] = os.path.basename(dest), u, size
            return r
        except Exception as e:
            errs.append(f'{u[:60]}: {type(e).__name__} {str(e)[:40]}')
    r['pdf_file'] = ''
    r['pdf_errors'] = errs
    return r


if __name__ == '__main__':
    cat, outdir = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    recs = json.load(open(cat, encoding='utf-8'))
    with cf.ThreadPoolExecutor(5) as ex:
        recs = list(ex.map(lambda r: work(r, outdir), recs))
    json.dump(recs, open(cat, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    ok = [r for r in recs if r.get('pdf_file')]
    print(len(ok), 'PDFs de', len(recs))
    for r in recs:
        if not r.get('pdf_file'):
            print('  SEM PDF', r['id'], (r.get('title') or '')[:60], '|', len(candidates(r)), 'candidatos', '|', (r.get('pdf_errors') or [''])[0][:90])
