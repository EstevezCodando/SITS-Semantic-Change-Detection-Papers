"""Confere se cada PDF em coleta/ corresponde ao titulo do catalogo (sobreposicao de palavras na 1a/2a pagina)."""
import re, sys, json, fitz
sys.stdout.reconfigure(encoding='utf-8')
root = sys.argv[1]
cat = json.load(open(f'{root}/dados/catalog.json', encoding='utf-8'))
bad = []
for r in cat:
    if not r.get('pdf_file'): continue
    d = fitz.open(f"{root}/coleta/{r['pdf_file']}")
    txt = ' '.join(d[i].get_text() for i in range(min(2, len(d)))).lower()
    words = [w for w in re.findall(r'[a-z0-9]{4,}', (r.get('oa_title') or r['title']).lower())]
    hit = sum(1 for w in set(words) if w in txt) / max(1, len(set(words)))
    r['pdf_titulo_match'] = round(hit, 2)
    if hit < 0.6: bad.append((r['id'], round(hit, 2), len(d), r['title'][:60], r['pdf_file'][:50]))
json.dump(cat, open(f'{root}/dados/catalog.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(bad), 'PDFs com baixa correspondencia de titulo')
for b in bad: print(b)
