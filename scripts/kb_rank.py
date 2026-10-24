import sys, os, re, json
sys.stdout.reconfigure(encoding='utf-8')
root = sys.argv[1]
P = os.path.join(root, 'output', 'pdf')
W = {  # peso por termo (contagem limitada) - objetivo: mudanca de cobertura com Planet ~5 m
 'planet': ('planetscope|planet labs|planet nicfi|nicfi|planet fusion|planet basemap|\bplanet\b', 6, 20),
 'res': ('\b[345](\.\d+)?\s?m\b|3-5 m|4\.77', 3, 10),
 'mud': ('change detection|semantic change|land[- ]cover change|land[- ]use change', 2, 20),
 'alvo': ('deforestation|forest loss|clear[- ]?cut|vegetation (loss|removal)|tree cover loss|forest disturbance|degradation', 2, 15),
 'cons': ('building|construction|new built|urban expansion|road|settlement', 1.5, 15),
 'ts': ('time series|multi-?temporal|monthly|mosaic', 1, 15),
 'dl': ('u-?net|deep learning|segmentation|transformer|random forest|xgboost', 0.7, 15),
 'res_num': ('\bf1\b|\biou\b|overall accuracy|kappa|precision|recall', 0.5, 20),
}
def pages(t):
    return len(re.findall(r'<!-- page: \d+ -->', t)) or 1
out = []
for d in sorted(os.listdir(P)):
    f = os.path.join(P, d, 'document.md')
    if not os.path.exists(f): continue
    t = open(f, encoding='utf-8', errors='ignore').read().lower()
    first = t[:6000]
    s = 0; det = {}
    for k, (rx, w, cap) in W.items():
        c = len(re.findall(rx, t)); cf = len(re.findall(rx, first))
        v = (min(c, cap) + 2 * min(cf, 5)) * w
        det[k] = c; s += v
    out.append(dict(id=d.split('_')[0], dir=d, score=round(s, 1), pg=pages(t), **det))
out.sort(key=lambda r: -r['score'])
json.dump(out, open(os.path.join(root, 'dados', 'ranking_relevancia.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for r in out[:45]:
    print(r['id'], r['score'], 'planet', r['planet'], 'mud', r['mud'], 'alvo', r['alvo'], r['dir'][:60])
