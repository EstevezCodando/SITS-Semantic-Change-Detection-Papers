"""Valida que cada link [[Pxx chunks#^Pxx_cNNN]] aponta para um bloco existente em vault/Chunks."""
import os, re, sys
V = sys.argv[1]
anchors = {}
for f in os.listdir(f'{V}/Chunks'):
    anchors[f[:-3]] = set(re.findall(r'\^(P\d+_c\d+)', open(f'{V}/Chunks/{f}', encoding='utf-8').read()))
LINK = re.compile(r'\[\[([^\]#|]+)#\^([^\]|]+?)\\?(?:\||\])')
bad, n = [], 0
for dp, _, fs in os.walk(V):
    if os.sep + 'Chunks' in dp or dp.endswith('Chunks'): continue
    for f in fs:
        if not f.endswith('.md'): continue
        for tgt, a in LINK.findall(open(os.path.join(dp, f), encoding='utf-8').read()):
            n += 1
            if a not in anchors.get(tgt.strip(), set()): bad.append((f, tgt, a))
print('ancoras', n, '| invalidas', len(bad))
for b in bad[:10]: print('  ', b)
