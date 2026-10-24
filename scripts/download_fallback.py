"""Etapa 3 (fallback): tenta de novo os registros sem PDF usando curl_cffi (mesma base do Scrapling
em C:\\Desenvolvimento\\WebScrapping), meta citation_pdf_url, Semantic Scholar (openAccessPdf), busca no
arXiv por titulo, CVF e JOSS. Nao tenta contornar acesso pago nem CAPTCHA: se a resposta nao for PDF, desiste.
Uso: python -I download_fallback.py dados/catalog.json coleta
"""
import re, sys, os, json, time, difflib, urllib.parse, concurrent.futures as cf
from curl_cffi import requests as cr

sys.path.insert(0, os.path.dirname(__file__))
from download_pdfs import filename, candidates

sys.stdout.reconfigure(encoding='utf-8')


def norm(t): return re.sub(r'[^a-z0-9]+', ' ', (t or '').lower()).strip()
def sim(a, b): return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()


def try_pdf(url, dest, referer=None):
    h = {'Accept': 'application/pdf,*/*'}
    if referer: h['Referer'] = referer
    r = cr.get(url, impersonate='chrome', timeout=40, allow_redirects=True, headers=h)
    if r.status_code == 200 and r.content.startswith(b'%PDF') and len(r.content) > 30_000:
        open(dest, 'wb').write(r.content)
        return len(r.content)
    raise ValueError(f'HTTP {r.status_code} {r.headers.get("content-type", "")[:30]}')


def pdf_from_landing(url):
    try:
        return _landing(url)
    except Exception:
        return None, None


def _landing(url):
    r = cr.get(url, impersonate='chrome', timeout=25, allow_redirects=True)
    if r.status_code != 200: return None, None
    m = re.search(r'<meta[^>]+name=["\']citation_pdf_url["\'][^>]+content=["\']([^"\']+)', r.text, re.I) or \
        re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']citation_pdf_url["\']', r.text, re.I)
    return (urllib.parse.urljoin(r.url, m.group(1).replace('&amp;', '&')) if m else None), r.url


def semantic_scholar(doi):
    try:
        r = cr.get(f'https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=openAccessPdf', timeout=30)
        if r.status_code == 200:
            return ((r.json().get('openAccessPdf') or {}).get('url'))
    except Exception:
        pass
    return None


def arxiv_by_title(title):
    try:
        q = urllib.parse.quote('ti:"%s"' % re.sub(r'[^A-Za-z0-9 ]+', ' ', title)[:150])
        r = cr.get(f'http://export.arxiv.org/api/query?search_query={q}&max_results=3', timeout=30)
        for e in re.findall(r'<entry>(.*?)</entry>', r.text, re.S):
            t = re.search(r'<title>(.*?)</title>', e, re.S).group(1)
            if sim(title, t) >= 0.9:
                return re.search(r'<id>http://arxiv.org/abs/([^<]+?)(v\d+)?</id>', e).group(1)
    except Exception:
        pass
    return None


def work(r, outdir):
    try:
        return _work(r, outdir)
    except Exception as e:
        r['pdf_errors'] = ['erro: ' + type(e).__name__]
        return r


def _work(r, outdir):
    if r.get('pdf_file'): return r
    dest = os.path.join(outdir, filename(r))
    if os.path.exists(dest) and os.path.getsize(dest) > 30_000:
        r['pdf_file'] = os.path.basename(dest); r['pdf_source'] = 'fallback (execucao anterior)'
        return r
    tried = []

    def attempt(label, url, referer=None):
        if not url: return False
        try:
            size = try_pdf(url, dest, referer)
            r['pdf_file'], r['pdf_source'], r['pdf_bytes'] = os.path.basename(dest), url, size
            return True
        except Exception as e:
            tried.append(f'{label}: {str(e)[:40]}')
            return False

    for u in candidates(r):          # 1) candidatos originais com TLS de navegador
        if 'doi.org' in u:
            pu, final = pdf_from_landing(u)   # 2) meta citation_pdf_url da pagina do artigo
            if attempt('landing-meta', pu, final): return r
        elif attempt('curl_cffi', u): return r
    doi = r.get('doi') or ''
    if doi and not doi.lower().startswith('10.48550'):
        if attempt('semantic-scholar', semantic_scholar(doi)): return r
        pu, final = pdf_from_landing('https://doi.org/' + doi)
        if attempt('doi-landing', pu, final): return r
        if doi.startswith('10.21105/joss'):
            if attempt('joss', f'https://joss.theoj.org/papers/{doi}.pdf'): return r
    aid = arxiv_by_title(r.get('title') or '')
    if aid and attempt('arxiv-titulo', 'https://arxiv.org/pdf/' + aid):
        r['pdf_note'] = 'versao preprint (arXiv)'
        return r
    for u in r.get('fonte_urls', []):  # CVF open access
        if 'openaccess.thecvf.com' in u and u.endswith('.html'):
            pu = u.replace('/html/', '/papers/').replace('_paper.html', '_paper.pdf')
            if attempt('cvf', pu): return r
    r['pdf_errors'] = tried
    return r


if __name__ == '__main__':
    cat, outdir = sys.argv[1], sys.argv[2]
    recs = json.load(open(cat, encoding='utf-8'))
    with cf.ThreadPoolExecutor(4) as ex:
        recs = list(ex.map(lambda r: work(r, outdir), recs))
    json.dump(recs, open(cat, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    ok = [r for r in recs if r.get('pdf_file')]
    print(len(ok), 'PDFs de', len(recs))
    for r in recs:
        if not r.get('pdf_file'):
            print('  SEM PDF', r['id'], (r.get('title') or '')[:55], '|', '; '.join(r.get('pdf_errors', []))[:100])
