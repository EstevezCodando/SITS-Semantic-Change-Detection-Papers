"""Gera chunks (JSONL) de um texto limpo (ex.: pagina HTML aberta) com o mesmo formato dos PDFs.
Uso: python -I chunk_text.py <PID> <arquivo.txt> <inicio> <fim>"""
import re, sys, json
sys.stdout.reconfigure(encoding='utf-8')
pid, path, start, end = sys.argv[1:5]
t = open(path, encoding='utf-8').read()
t = t[t.index(start):t.index(end, t.index(start))]
HEAD = re.compile(r'^(\d(\.\d)*\.?)\s+[A-Z][^.]{2,80}$')
MAP = [('introdu', 'introdução'), ('study area', 'dados'), ('training', 'dados'), ('satellite data', 'dados'), ('dataset composition', 'dados'), ('textural', 'métodos'),
       ('methodology', 'métodos'), ('materials', 'métodos'), ('lulc classification', 'métodos'), ('accuracy', 'métodos'), ('results', 'resultados'), ('discussion', 'discussão'),
       ('gee', 'discussão'), ('conclusion', 'conclusão'), ('abstract', 'resumo')]
sec, head, paras, cur = 'introdução', '1. Introduction', [], ''
chunks = []
def flush():
    global paras
    buf = ''
    for p in paras:
        if buf and len(buf) + len(p) > 1700:
            chunks.append((sec, head, buf)); buf = p
        else:
            buf = (buf + ' ' + p).strip()
    if buf: chunks.append((sec, head, buf))
    paras = []
for l in t.split('\n'):
    l = l.strip()
    if HEAD.match(l) and len(l.split()) <= 9:
        flush(); head = l
        sec = next((v for k, v in MAP if k in l.lower()), sec)
        continue
    if len(l) > 70: paras.append(l)
flush()
with open(f'dados/chunks/{pid}.jsonl', 'w', encoding='utf-8') as f:
    for i, (s, h, tx) in enumerate(chunks, 1):
        f.write(json.dumps({'id': f'{pid}_c{i:03d}', 'paper': pid, 'secao': s, 'titulo_secao': h, 'pagina': 1, 'texto': tx, 'entidades': {}, 'tem_numeros_resultado': bool(re.search(r'\d\s?%', tx)), 'tem_hiperparametros': bool(re.search(r'learning rate|batch size|epochs|window size|seed spacing', tx)), 'chars': len(tx)}, ensure_ascii=False) + '\n')
        print(f'{pid}_c{i:03d} | {s} | {h[:38]} | {tx[:90]}')
