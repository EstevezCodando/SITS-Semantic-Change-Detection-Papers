"""Valida wikilinks do vault (ignora os arquivos de Chunks)."""
import os, re, sys, collections
V = sys.argv[1]
stems = set()
for dp, _, fs in os.walk(V):
    for f in fs:
        if f.endswith('.md'): stems.add(f[:-3])
        elif f.endswith('.canvas'): stems.add(f)
miss, n = collections.Counter(), 0
for dp, _, fs in os.walk(V):
    for f in fs:
        if not f.endswith('.md'): continue
        t = open(os.path.join(dp, f), encoding='utf-8').read()
        t = re.sub(r'```.*?```|`[^`]*`', '', t, flags=re.S)
        for m in re.findall(r'\[\[([^\]]+)\]\]', t):
            tgt = m.replace('\|', '|').split('|')[0].split('#')[0].strip(); n += 1
            if tgt not in stems: miss[tgt] += 1
print('links', n, '| quebrados', sum(miss.values()), '| notas', len(stems))
for k, v in miss.most_common(10): print('  ', v, k)
