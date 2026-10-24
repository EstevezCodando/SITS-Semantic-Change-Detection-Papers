"""Etapa 6: gera o vault Obsidian (vault/) a partir de dados/catalog.json, dados/analysis.json,
dados/chunks/*.jsonl e do documento original.
Uso: python -I build_vault.py <raiz do projeto>
"""
import re, os, sys, json, shutil, collections, itertools
sys.stdout.reconfigure(encoding='utf-8')
root = sys.argv[1]
V = f'{root}/vault'
cat = json.load(open(f'{root}/dados/catalog.json', encoding='utf-8'))
ana = json.load(open(f'{root}/dados/analysis.json', encoding='utf-8'))
tools = json.load(open(f'{root}/dados/tools.json', encoding='utf-8'))
orig_txt = open(f'{root}/fonte_original/REVISAO_ORIGINAL.md', encoding='utf-8').read()

# ---------------------------------------------------------------- parametros de dominio
SEC = {
    'A': 'Planet: aplicações diretas', 'B': 'Séries temporais, edificações e transições semânticas', 'C': 'Detectores profundos e modelos fundacionais',
    'D': 'Vias, redes viárias e cartografia prévia', 'E': 'Métodos temporais clássicos e avaliação', 'R': 'Revisões do documento original',
    'F': 'XGBoost, LightGBM e atributos', 'G': 'Pré-catalogação SAM/YOLO e representações', 'H': 'Engenharia de dados', 'I': 'Ciência de dados e curadoria',
    'J': 'Planet: dados, qualidade e fusão', 'K': 'Planet: aplicações adicionais', 'L': 'Desmatamento e alertas', 'M': 'Detecção de mudanças: métodos adicionais', 'N': 'GeoAI e QGIS',
}
PAPEL_SEC = {
    'A': 'aplicação Planet', 'B': 'benchmark/método temporal', 'C': 'baseline/método de mudança', 'D': 'vias e cartografia', 'E': 'método clássico/avaliação', 'R': 'revisão',
    'F': 'baseline tabular (ML)', 'G': 'pré-anotação/representação', 'H': 'engenharia de dados', 'I': 'validação/curadoria', 'J': 'dados e qualidade Planet',
    'K': 'aplicação Planet', 'L': 'desmatamento/alerta', 'M': 'método de mudança', 'N': 'GeoAI/QGIS',
}
ALTA = {'P01', 'P10', 'P12', 'P13', 'P14', 'P02', 'P05', 'P18', 'P19', 'P07', 'P46'}
MEDIA = {'P03', 'P04', 'P06', 'P11', 'P15', 'P20', 'P21', 'P23', 'P26', 'P28', 'P29', 'P33', 'P41', 'P42', 'P47', 'P51', 'P52', 'P54', 'P56', 'P57', 'P58', 'P59', 'P60', 'P62',
         'P68', 'P70', 'P75', 'P77', 'P78', 'P81', 'P82', 'P83'}
# GeoAI/QGIS e interesse declarado pelo usuario -> alta (resolvido por DOI mais abaixo)
ALTA_DOI = {'10.21105/joss.09605', '10.1016/j.softx.2023.101495', '10.21105/joss.10329', '10.2139/ssrn.4786825'}

STAGES = [
    ('E01', 'Inventário e catálogo', 'Identificar cada arquivo, período, produto, bandas, CRS e checksum; separar catálogo técnico de imagens e catálogo semântico de observações.',
     'Arquivos Planet brutos (3 m e 5 m), manifestos', 'Catálogo STAC/CSV de assets; manifestos', ['Cubo de dados / STAC', 'STAC (ferramenta)']),
    ('E02', 'Qualidade e harmonização', 'Medir registro geométrico, nuvem/sombra/emendas, radiometria e cadência real; decidir grade comum sem criar detalhe artificial.',
     'Assets catalogados', 'Máscara de observação válida; relatório de QA; grade comum documentada', ['Nuvem/sombra/QA', 'Fusão de dados', 'Super-resolução']),
    ('E03', 'Cubo espaço-temporal e partições', 'Montar o cubo (tempo × bandas × espaço), definir blocos geográficos e períodos de teste sem vazamento.',
     'Assets harmonizados', 'Cubo/coleção pronta para análise; evaluation_split versionado', []),
    ('E04', 'Rotulagem e pré-anotação', 'Criar rótulos de áreas estáveis e mudanças reais; pré-anotar com SAM/YOLO e revisar; priorizar por aprendizado ativo.',
     'Cubo + amostra espacial/temporal', 'Conjunto anotado com origem e revisor; catálogo semântico preliminar', ['Anotação/rotulagem', 'Aprendizado ativo', 'Supervisão fraca', 'Semi/auto-supervisionado', 'SAM', 'YOLO', 'Grounding DINO']),
    ('E05', 'Atributos e representações', 'Extrair bandas/índices, textura, geometria, contexto e embeddings; testar por ablação.',
     'Cubo + máscaras/objetos', 'Tabela de atributos versionada; embeddings com procedência', ['NDVI/índices', 'OBIA / objetos', 'Modelo fundacional', 'DINO/DINOv3', 'Autoencoder mascarado (MAE)', 'CLIP / visão-linguagem']),
    ('E06', 'Modelos-base de cobertura', 'Baselines: Random Forest/XGBoost/LightGBM sobre atributos e U-Net mensal; regra de persistência temporal.',
     'Atributos, rótulos, partições', 'Mapas mensais de cobertura com probabilidade', ['Random Forest', 'XGBoost', 'LightGBM', 'SVM', 'U-Net']),
    ('E07', 'Modelos de mudança em pares', 'Aprender a mudança diretamente (FC-Siam, ChangeFormer, ChangeMamba) e mudança semântica (HRSCD, SECOND, ChangeMask).',
     'Pares de datas corregistrados', 'Máscara de mudança + classes antes/depois', ['Rede siamesa', 'Transformer', 'Mamba/SSM', 'Mudança semântica', 'Detecção de mudança (binária)']),
    ('E08', 'Modelos de série temporal', 'Usar o histórico completo (TSSCD, U-TAE, BFAST/CCDC) para localizar quando e o que mudou.',
     'Cubo temporal', 'Mapa de mudança com data/intervalo e transição', ['Séries temporais de imagens', 'Atenção temporal (U-TAE)', 'BFAST', 'CCDC', 'LandTrendr', 'LSTM/ConvLSTM']),
    ('E09', 'Pós-processamento e eventos', 'Persistência, ligação de identidades no tempo, taxonomia from–to, vetorização e eventos encadeados (supressão → obra → via).',
     'Mapas de cobertura/mudança', 'change_event com geometria, intervalo, classe anterior/posterior e evidências', ['Edificações', 'Vias/estradas', 'Pós-classificação', 'Expansão urbana', 'Mineração']),
    ('E10', 'Avaliação e incerteza', 'Métricas por tarefa, matriz from–to, estimativa de área com IC, validação espacial/temporal e custo de revisão.',
     'Eventos + amostra probabilística independente', 'Métricas, áreas estimadas, falsos alertas por km²/mês', ['Estimativa de área / IC', 'Matriz de confusão', 'Kappa', 'F1', 'IoU / mIoU', 'Precisão/Recall', 'SeK', 'SCS (DynamicEarthNet)']),
    ('E11', 'Operação e atualização', 'Atualização incremental, alertas com regime operacional (só passado), revisão humana em QGIS, rastreabilidade.',
     'Novos mosaicos mensais', 'Eventos revisados e versionados', ['QGIS', 'GeoAI (opengeos)', 'MOLUSCE', 'SCP (QGIS)', 'Google Earth Engine']),
]
STAGE_BY_SEC = {'H': ['E01', 'E03'], 'J': ['E02'], 'G': ['E04', 'E05'], 'F': ['E05', 'E06'], 'A': ['E06'], 'B': ['E07', 'E08'], 'C': ['E07'], 'D': ['E09'],
                'E': ['E08', 'E10'], 'I': ['E03', 'E04', 'E10'], 'K': ['E06', 'E09'], 'L': ['E06', 'E11'], 'M': ['E07'], 'N': ['E11'], 'R': []}
STAGE_OVERRIDE = {'P46': ['E10'], 'P47': ['E10'], 'P75': ['E03', 'E10'], 'P78': ['E04'], 'P77': ['E02'], 'P41': ['E08'], 'P42': ['E08'], 'P43': ['E08'], 'P44': ['E08'],
                  'P45': ['E04'], 'P10': ['E07', 'E08', 'E09', 'E10'], 'P12': ['E07', 'E08', 'E10'], 'P13': ['E08', 'E10'], 'P14': ['E08']}

CONCEPT_DESC = {
    'Planet NICFI': 'Mosaicos Planet do programa NICFI (trópicos), ~4,77 m; histórico anterior a set/2020 é semestral, depois mensal. Conferir `cadence` antes de assumir observação mensal.',
    'PlanetScope': 'Constelação Planet de cenas diárias (~3 m), 4 ou 8 bandas (SuperDove). Mosaicos mensais compõem observações de dias distintos.',
    'Sentinel-2': 'Sentinel-2 (10–20 m, 5 dias). Complemento para séries e harmonização; não resolve edificações de 3–5 m.',
    'Landsat': 'Landsat (30 m). Base de CCDC/LandTrendr e do histórico de desmatamento; não transferir parâmetros a Planet.',
    'SpaceNet 7 (MUDS)': 'Dataset de edificações em mosaicos Planet de ~4 m, ~24 meses por local, polígonos com identidade temporal. Referência para novas construções.',
    'DynamicEarthNet': 'Planet diário com rótulos mensais de 7 classes e métrica SCS. Referência para mudança semântica multiclasse.',
    'LEVIR-CD': 'Benchmark de mudança em edificações (0,5 m). Resolução diferente de Planet.', 'SECOND': 'Benchmark de mudança semântica bitemporal (classes antes/depois, métrica SeK).',
    'HRSCD': 'Dataset de mudança semântica em larga escala (aéreo RGB) usado em aprendizado multitarefa.', 'OSCD': 'Onera Satellite Change Detection: pares Sentinel-2 para mudança urbana.',
    'PRODES': 'Mapa oficial anual de desmatamento (INPE). Fonte de rótulos e referência de comparação, não verdade absoluta.', 'DETER': 'Sistema de alertas de desmatamento do INPE (quase tempo real).',
    'MapBiomas': 'Coleções brasileiras de uso e cobertura da terra (Landsat). Fonte auxiliar de pré-rótulos.',
    'U-Net': 'Encoder–decoder para segmentação. Baseline dominante para cobertura arbórea, edificações e vias em Planet.',
    'Rede siamesa': 'Dois ramos com pesos compartilhados para comparar imagens de duas datas (FC-Siam, ChangeFormer).', 'Transformer': 'Atenção de longo alcance (BIT, ChangeFormer, Swin). Não recupera objetos que a resolução não resolve.',
    'Mamba/SSM': 'Modelos de espaço de estados (ChangeMamba): eficiência em contexto longo.', 'SAM': 'Segment Anything: máscaras por prompt, sem taxonomia. Útil para pré-anotação, exige revisão.',
    'YOLO': 'Detector de objetos; fornece caixas/classes após treino adequado e prompts para SAM.', 'Modelo fundacional': 'Backbones pré-treinados em larga escala (Prithvi, DOFA, DINOv3). Conferir bandas, normalização e resolução.',
    'Random Forest': 'Baseline de ML sobre atributos; competitivo com poucos rótulos.', 'XGBoost': 'Gradient boosting sobre vetores de atributos (pixel, objeto, trajetória).', 'LightGBM': 'Gradient boosting eficiente; ótimo para tabelas grandes de atributos.',
    'BFAST': 'Decomposição de tendência/sazonalidade com rupturas (R).', 'CCDC': 'Modelagem contínua com rupturas e classificação (Landsat).', 'LandTrendr': 'Segmentação temporal de trajetórias anuais de perturbação e recuperação.',
    'Aprendizado ativo': 'Seleção de amostras para revisão por incerteza/diversidade; manter uma amostra probabilística independente para avaliação.',
    'Pós-classificação': 'Classificar cada data e comparar rótulos; propaga erros dos dois mapas.', 'F1': 'Média harmônica de precisão e recall; não comparar entre benchmarks distintos.',
    'IoU / mIoU': 'Interseção sobre união por classe; sensível a objetos pequenos.', 'SeK': 'Métrica de mudança semântica do SECOND.', 'Estimativa de área / IC': 'Área corrigida pelos erros da matriz, com intervalo de confiança (Olofsson et al.).',
    'Séries temporais de imagens': 'SITS: o problema é localizar *onde*, *quando* e *o que* mudou, e não apenas diferença de pixels.', 'Mudança semântica': 'Mudança com classe antes/depois (from–to).',
    'Desmatamento': 'Supressão da cobertura arbórea; separar de degradação e de sazonalidade.', 'Degradação florestal': 'Perda parcial de estrutura (fogo, exploração seletiva, estradas).',
    'Edificações': 'Novas construções e demolições; limitadas pela área mínima detectável em 3–5 m.', 'Vias/estradas': 'Aberturas e pavimentações; avaliar conectividade, não só pixels.',
    'QGIS': 'SIG de código aberto usado para revisão humana, pré-anotação e plugins de IA (Deepness, IAMAP, Geo-SAM, GeoAI).',
    'GeoAI (opengeos)': 'Pacote Python (geoai-py) + plugin QGIS de Qiusheng Wu; JOSS 2026.',
}

# ---------------------------------------------------------------- utilidades
def san(s): return re.sub(r'\s+', ' ', re.sub(r'[\\/:*?"<>|#^\[\]]', '-', s)).strip(' .')
def author_last(r):
    a = r.get('authors') or []
    return san(a[0].split()[-1]) if a else 'Anon'
def year(r): return (r.get('year_doc') if r['origin'] == 'original' and r.get('year_doc') else r.get('oa_year')) or 's.d.'
def note_name(r): return f"{r['id']} {author_last(r)} {year(r)}"
def wl(r, label=None): return f"[[{note_name(r)}|{label or r['id']}]]"
def yq(s): return '"' + str(s).replace('\\', '\\\\').replace('"', '\\"') + '"'
def ylist(items): return '[' + ', '.join(yq(i) for i in items) + ']' if items else '[]'
def cl(n): return f'[[{n}]]' if san(n) == n else f'[[{san(n)}|{n}]]'


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # em tabelas Markdown o "|" do alias de wikilink precisa de escape
    text = '\n'.join(re.sub(r'\[\[[^\]]*\]\]', lambda m: m.group(0).replace('\\|', '|').replace('|', '\\|'), l) if l.startswith('|') else l for l in text.split('\n'))
    open(path, 'w', encoding='utf-8').write(text)

byid = {r['id']: r for r in cat}
doi2id = {r['doi'].lower(): r['id'] for r in cat if r.get('doi')}
CAT_DIR = {'sensor': 'Sensores e produtos', 'dataset': 'Datasets', 'metodo': 'Métodos', 'metrica': 'Métricas', 'tarefa': 'Tarefas', 'ferramenta': 'Ferramentas'}
THR = {'sensor': 3, 'dataset': 2, 'metodo': 3, 'metrica': 3, 'tarefa': 10, 'ferramenta': 2}
SKIP_ENT = {'ImageNet', 'Inria'}
MAP_EXCLUDE = {'Detecção de mudança (binária)', 'Séries temporais de imagens', 'F1', 'IoU / mIoU', 'Precisão/Recall', 'Kappa', 'Matriz de confusão', 'Transformer', 'QGIS', 'Edificações', 'Vias/estradas'}
CAP = {'tarefa': 5, 'metodo': 6, 'metrica': 4, 'dataset': 4, 'sensor': 3, 'ferramenta': 3}

# texto para papers sem PDF (classificacao por metadados)
def meta_text(r):
    parts = [r.get('title', ''), r.get('note', '')]
    for k, v in (r.get('bullets') or {}).items():
        if k not in ('Fonte',): parts.append(v)
    return ' '.join(parts)

# reaproveita o dicionario de entidades do extrator (trecho entre "ENT = {" e "ENT_RX =")
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'extract_analysis.py'), encoding='utf-8').read()
_blk = _src[_src.index('ENT = {'):_src.index('ENT_RX =')]
ns = {}
exec(_blk, {'re': re}, ns)
ENT_RX = {c: {n: re.compile(p) for n, p in d.items()} for c, d in ns['ENT'].items()}

ents = {}      # id -> {cat: {nome: contagem}}
for r in cat:
    a = ana.get(r['id'])
    if a and 'entidades' in a:
        e = {c: {n: k for n, k in d.items() if n not in SKIP_ENT and k >= THR[c]} for c, d in a['entidades'].items()}
        # reforco: entidades no titulo/comentario sempre entram
        mt = meta_text(r)
        for c, d in ENT_RX.items():
            for n, rx in d.items():
                if n not in SKIP_ENT and rx.search(mt): e.setdefault(c, {}).setdefault(n, 1)
        r['_fonte_analise'] = 'texto integral (PDF) + metadados'
    else:
        e = {}
        mt = meta_text(r)
        for c, d in ENT_RX.items():
            for n, rx in d.items():
                k = len(rx.findall(mt))
                if k and n not in SKIP_ENT: e.setdefault(c, {})[n] = k
        r['_fonte_analise'] = 'apenas metadados e comentário (sem PDF)'
    ents[r['id']] = {c: dict(sorted(d.items(), key=lambda x: -x[1])[:CAP[c]]) for c, d in e.items() if d}

def tags_of(rid): return {n for d in ents[rid].values() for n in d}

# etapas por artigo
stage_of = {}
for r in cat:
    st = set(STAGE_BY_SEC.get(r['section'], []))
    if r['id'] in STAGE_OVERRIDE: st = set(STAGE_OVERRIDE[r['id']])
    tg = tags_of(r['id'])
    for sid, _, _, _, _, trig in STAGES:
        strong = [t for t in trig if t not in MAP_EXCLUDE and t in tg and any(t in ents[r['id']].get(c, {}) and ents[r['id']][c][t] >= 15 for c in ents[r['id']])]
        if strong and r['id'] not in STAGE_OVERRIDE: st.add(sid)
    stage_of[r['id']] = sorted(st) or ['E06']

def prioridade(r):
    if r['id'] in ALTA or (r.get('doi') or '').lower() in ALTA_DOI: return 'alta'
    if r['id'] in MEDIA: return 'média'
    return 'baixa'

def papel(r):
    p = [PAPEL_SEC[r['section']]]
    if r['kind'] == 'Dataset': p.append('dataset/benchmark')
    if r['kind'] == 'Revisão': p.append('revisão')
    if r['kind'] == 'Software': p.append('ferramenta')
    if r['kind'] == 'Preprint': p.append('preprint')
    return p

# relacoes explicitas P## no texto original
rel = collections.defaultdict(set)
for r in cat:
    if r['origin'] == 'original':
        txt = ' '.join(v for k, v in r['bullets'].items() if k not in ('Fonte', 'Referência'))
        for m in re.findall(r'\bP(\d\d)\b', txt):
            o = f'P{m}'
            if o != r['id'] and o in byid: rel[r['id']].add(o); rel[o].add(r['id'])
for a, b in [('P10', 'P11'), ('P18', 'P19'), ('P39', 'P40'), ('P51', 'P52'), ('P56', 'P60'), ('P29', 'P27')]:
    rel[a].add(b); rel[b].add(a)
# pares preprint/publicacao e publicados citados
for d, o in [('10.1109/jstars.2025.3649081', 'P58'), ]:
    pass
# vizinhos por similaridade de entidades (Jaccard)
sig = {rid: {(c, n) for c, d in e.items() for n in d if c in ('dataset', 'metodo', 'tarefa', 'sensor')} for rid, e in ents.items()}
nb = {}
for rid, s in sig.items():
    sc = []
    for o, so in sig.items():
        if o == rid or not s or not so: continue
        j = len(s & so) / len(s | so)
        if j >= 0.25: sc.append((j, o))
    nb[rid] = [o for _, o in sorted(sc, reverse=True)[:4]]

# ---------------------------------------------------------------- Chunks (um arquivo por paper, com ancoras ^id)
chunks_by = {}
for r in cat:
    p = f"{root}/dados/chunks/{r['id']}.jsonl"
    if os.path.exists(p):
        chunks_by[r['id']] = [json.loads(l) for l in open(p, encoding='utf-8')]
if os.path.isdir(V): shutil.rmtree(V)
for rid, chs in chunks_by.items():
    r = byid[rid]
    L = [f"---\ntipo: chunks\npaper: {yq(rid)}\nn_chunks: {len(chs)}\n---", f"# Chunks — {wl(r, note_name(r))}\n",
         '> Texto extraído automaticamente do PDF em `coleta/` (seções detectadas por regras). Use os blocos `^ID` para citar trechos: `[[%s chunks#^%s_c001]]`.\n' % (rid, rid)]
    cur = None
    for c in chs:
        if c['secao'] != cur:
            cur = c['secao']; L.append(f"\n## {cur.capitalize()} — {c['titulo_secao']} (p. {c['pagina']})\n")
        flags = []
        if c['tem_hiperparametros']: flags.append('hiperparâmetros')
        if c['tem_numeros_resultado']: flags.append('resultados numéricos')
        ev = [n for d in c['entidades'].values() for n in d if n not in SKIP_ENT][:6]
        meta = f"*{', '.join(flags + ev)}*" if (flags or ev) else ''
        L.append(f"{c['texto']}\n\n{meta} ^{c['id']}\n")
    write(f'{V}/Chunks/{rid} chunks.md', '\n'.join(L))

def chunk_links(rid):
    chs = chunks_by.get(rid)
    if not chs: return None
    lines = []
    cnt = collections.Counter(c['secao'] for c in chs)
    lines.append(f"- Arquivo de chunks: [[{rid} chunks]] ({len(chs)} chunks; " + ', '.join(f'{k} {v}' for k, v in cnt.items()) + ')')
    def pick(pred, label, k=2):
        sel = [c for c in chs if pred(c)][:k]
        if sel: lines.append(f"- {label}: " + ', '.join(f"[[{rid} chunks#^{c['id']}|{c['id'][-4:]}]]" for c in sel))
    pick(lambda c: c['secao'] == 'resumo', 'Resumo')
    pick(lambda c: c['secao'] == 'dados', 'Dados / área de estudo')
    pick(lambda c: c['secao'] == 'métodos', 'Método', 3)
    pick(lambda c: c['tem_hiperparametros'], 'Hiperparâmetros / treino', 3)
    pick(lambda c: c['secao'] in ('experimentos', 'resultados') and c['tem_numeros_resultado'], 'Resultados numéricos', 3)
    pick(lambda c: c['secao'] in ('discussão',), 'Limitações / discussão', 2)
    return lines

# ---------------------------------------------------------------- Notas de artigos
def reuse_lines(r):
    L = []
    b = r.get('bullets') or {}
    ap = b.get('Aplicação')
    if ap: L.append(f"**Uso proposto:** {ap}")
    elif r.get('note'): L.append(f"**Relevância:** {r['note']}")
    if r['kind'] == 'Dataset': L.append('**Dataset/benchmark:** candidato a treino, validação ou comparação; verificar licença, resolução e divisão oficial.')
    if r['kind'] == 'Revisão': L.append('**Revisão:** usar para expandir a bibliografia por rastreamento de referências (família de arquitetura, tipo de mudança).')
    codes = [u for u in r.get('code', []) if u.startswith('http')] + (ana.get(r['id'], {}).get('github') or [])
    codes = list(dict.fromkeys(codes))
    if codes: L.append('**Código:** ' + ' · '.join(codes[:4]))
    hp = ana.get(r['id'], {}).get('hiperparametros') or {}
    if hp: L.append('**Receita de treino extraída:** ' + '; '.join(f"{k} — `{v['trecho']}`" for k, v in list(hp.items())[:5]) + ' (confirmar nos chunks).')
    t = ents[r['id']]
    if t.get('metrica'): L.append('**Métricas usadas:** ' + ', '.join(f'{cl(n)}' for n in t['metrica']))
    if t.get('dataset'): L.append('**Dados/benchmarks citados:** ' + ', '.join(f'{cl(n)}' for n in t['dataset']))
    return L

for r in cat:
    t = ents[r['id']]
    b = r.get('bullets') or {}
    fm = ['---', 'tipo: artigo', f"id: {r['id']}", f"titulo: {yq(r['title'])}", f"autores: {yq(', '.join((r.get('authors') or [])[:4]) or 'a importar')}", f"ano: {year(r)}",
          f"secao: {r['section']}", f"categoria: {yq(SEC[r['section']])}", f"tipo_publicacao: {yq(r['kind'])}", f"papel: {ylist(papel(r))}", f"prioridade: {prioridade(r)}",
          f"doi: {yq(r.get('doi', ''))}", f"pdf: {yq('coleta/' + r['pdf_file']) if r.get('pdf_file') else yq('')}", f"texto_integral: {'sim' if r.get('pdf_file') else 'nao'}",
          f"fonte_analise: {yq(r['_fonte_analise'])}", f"n_chunks: {len(chunks_by.get(r['id'], []))}"]
    for c, key in [('sensor', 'sensores'), ('tarefa', 'tarefas'), ('metodo', 'metodos'), ('dataset', 'datasets'), ('metrica', 'metricas'), ('ferramenta', 'ferramentas')]:
        fm.append(f"{key}: {ylist([f'{cl(n)}' for n in t.get(c, {})])}")
    fm.append(f"etapas_pipeline: {ylist([f'[[{s} {next(x[1] for x in STAGES if x[0]==s)}|{s}]]' for s in stage_of[r['id']]])}")
    fm.append('status_leitura: não lido')
    tg = ['artigo', f"secao/{r['section']}", f"prioridade/{prioridade(r)}"] + [f"etapa/{s}" for s in stage_of[r['id']]]
    fm.append('tags: [' + ', '.join(tg) + ']')
    fm.append('---')
    body = [f"# {r['id']} — {r['title']}\n"]
    meta = f"**{', '.join((r.get('authors') or [])[:3]) or 'Autoria a importar'}** · {year(r)} · {r['kind']} · {(r.get('venue') or '').split('/')[0][:70]}"
    link = (r.get('fonte_urls') or [None])[0] if r['origin'] == 'original' and r.get('fonte_urls') else ('https://doi.org/' + r['doi'] if r.get('doi') else '')
    body.append(meta + (f" · [publicação]({link})" if link else '') + (f" · [PDF](../../coleta/{r['pdf_file']})" if r.get('pdf_file') else ' · PDF indisponível em coleta/') + '\n')
    body.append(f"Seção: **{SEC[r['section']]}** · Prioridade: **{prioridade(r)}** · Análise: *{r['_fonte_analise']}*\n")
    body.append('## O que reaproveitar\n')
    body += [f'- {x}' for x in reuse_lines(r)] or ['- (sem item extraído)']
    body.append('')
    if b.get('Método/dados') or b.get('Método') or b.get('Evidência direta') or b.get('Contribuição'):
        body.append('## Método e dados (da revisão original)\n')
        for k in ('Método/dados', 'Método', 'Evidência direta', 'Resultado contextualizado', 'Contribuição'):
            if b.get(k): body.append(f'- **{k}:** {b[k]}')
        body.append('')
    lim = b.get('Limite')
    body.append('## Limites e cuidados\n')
    body.append(f'- {lim}' if lim else '- Conferir resolução, bandas, região e rótulos antes de transferir resultados; síntese baseada em registro e metadados.')
    if r.get('title_sim') is not None and r['title_sim'] < 0.75: body.append('- O título da versão publicada difere do preprint; confira a versão citada.')
    body.append('')
    body.append('## Contextos de uso no projeto\n')
    body.append('- Etapas do pipeline: ' + ', '.join(f"[[{s} {next(x[1] for x in STAGES if x[0]==s)}|{s}]]" for s in stage_of[r['id']]))
    for c, lab in [('tarefa', 'Tarefas'), ('sensor', 'Sensores/produtos'), ('metodo', 'Métodos')]:
        if t.get(c): body.append(f"- {lab}: " + ', '.join(f'{cl(n)}' for n in t[c]))
    body.append('')
    if t:
        body.append('## Entidades detectadas\n')
        body.append('| Categoria | Entidade | Ocorrências |\n|---|---|---:|')
        for c in ('sensor', 'dataset', 'metodo', 'metrica', 'tarefa', 'ferramenta'):
            for n, k in sorted(t.get(c, {}).items(), key=lambda x: -x[1]): body.append(f'| {c} | {cl(n)} | {k} |')
        body.append('')
    fr = (ana.get(r['id']) or {}).get('frases_resultado')
    if fr:
        body.append('## Resultados citados pelos autores (extraídos automaticamente)\n')
        body += [f'> {s}' for s in fr[:3]]
        body.append('\n*Frases extraídas por regra; podem estar truncadas. Confirmar no chunk de resultados.*\n')
    chl = chunk_links(r['id'])
    body.append('## Chunks\n')
    body += chl if chl else ['- Sem PDF em `coleta/` (acesso restrito ou bloqueado); chunking indisponível. Use o link da publicação.']
    body.append('')
    body.append('## Relações\n')
    rl = sorted(rel.get(r['id'], []))
    if rl: body.append('- Relação explícita: ' + ', '.join(wl(byid[o]) for o in rl))
    if nb.get(r['id']): body.append('- Vizinhos por entidades em comum: ' + ', '.join(wl(byid[o]) for o in nb[r['id']]))
    body.append('')
    body.append('## Anotações\n\n- ')
    write(f"{V}/Artigos/{note_name(r)}.md", '\n'.join(fm + [''] + body) + '\n')

# ---------------------------------------------------------------- Notas de conceito
ent_papers = collections.defaultdict(list)   # (cat,nome) -> [ (id,count) ]
for rid, e in ents.items():
    for c, d in e.items():
        for n, k in d.items(): ent_papers[(c, n)].append((rid, k))
for (c, n), lst in ent_papers.items():
    lst.sort(key=lambda x: (-x[1], x[0]))
    L = ['---', 'tipo: conceito', f'categoria: {c}', f"n_artigos: {len(lst)}", f'tags: [conceito, {c}]', '---', f'# {n}\n']
    L.append(CONCEPT_DESC.get(n, f'Entidade da categoria *{CAT_DIR[c].lower()}* detectada automaticamente nos artigos coletados.') + '\n')
    st = [s for s in STAGES if n in s[5]]
    if st: L.append('**Etapas relacionadas:** ' + ', '.join(f'[[{s[0]} {s[1]}|{s[0]}]]' for s in st) + '\n')
    L.append(f'## Artigos ({len(lst)})\n')
    L.append('| Artigo | Ano | Ocorrências | Prioridade |\n|---|---|---:|---|')
    for rid, k in lst:
        r = byid[rid]
        L.append(f"| {wl(r, note_name(r))} — {r['title'][:70]} | {year(r)} | {k} | {prioridade(r)} |")
    write(f'{V}/Conceitos/{CAT_DIR[c]}/{san(n)}.md', '\n'.join(L) + '\n')

# ---------------------------------------------------------------- Pipeline
HOWTO = {
    'E01': ['Registrar para cada arquivo: produto, intervalo de composição, CRS, resolução, bandas, URI e checksum (`image_asset`).', 'Manter o catálogo técnico (STAC) separado do catálogo semântico de observações.', 'Preservar os originais; derivados apontam para a origem.'],
    'E02': ['Medir desalinhamento em alvos estáveis; mascarar nuvem, sombra e emendas; manter classe de observação inválida.', 'Verificar bandas (RGB visual não gera NDVI) e cadência real (NICFI anterior a set/2020 é semestral).', '3 m e 5 m não são intercambiáveis: preservar originais e testar grade comum; reamostrar não cria detalhe.'],
    'E03': ['Separar treino/validação/teste por blocos geográficos e reservar períodos posteriores para teste temporal.', 'Documentar quando o teste muda de produto/resolução ao mesmo tempo.', 'Evitar patches vizinhos ou sobrepostos entre conjuntos.'],
    'E04': ['Comparar três condições na mesma amostra: manual, pré-anotação com correção e pré-anotação sem correção.', 'Medir tempo total, falsos positivos removidos e omissões acrescentadas.', 'Manter amostra probabilística independente, separada da escolhida por aprendizado ativo.'],
    'E05': ['Bandas/índices compatíveis com o produto; estatísticas por segmento; texturas em janelas definidas em metros.', 'Testar grupos de atributos por ablação; ajustar seletores e hiperparâmetros só no treino.', 'Registrar modelo, checkpoint, resolução e normalização dos embeddings.'],
    'E06': ['Começar por RF/XGBoost/LightGBM e U-Net mensal + regra de persistência.', 'Reportar métricas de cobertura por mês separadas das de mudança.', 'Usar como baseline contra o qual os modelos de mudança devem ganhar.'],
    'E07': ['Comparar FC-Siam ou ChangeFormer com a pós-classificação nos mesmos dados, rótulos e orçamento.', 'Modelos semânticos conjuntos devem manter coerência entre "mudou" e as classes.', 'Binário não diz *o que* mudou: exigir saída semântica.'],
    'E08': ['Testar se o histórico mensal melhora a detecção em relação a pares de datas.', 'Avaliar anos e áreas inéditos (domain shift), não só patches da mesma paisagem.', 'Registrar intervalo de ocorrência, não dia exato inferido do nome do arquivo.'],
    'E09': ['Aplicar a taxonomia from–to; guardar eventos encadeados (supressão → obra → via) sem contar a mesma área duas vezes.', 'Associação temporal de objetos deve modelar divisão/fusão; o ID de uma máscara não é identidade no mundo.', 'Saída mínima: id, geometria, classe anterior/posterior, intervalo, área, produto, observações válidas, confiança e revisão.'],
    'E10': ['Métricas por tarefa (mudança, from–to, edificações por objeto e tamanho, vias por conectividade, data, área).', 'Estimar área com amostragem probabilística e intervalo de confiança; área mapeada ≠ área estimada.', 'Não comparar F1 publicado entre benchmarks distintos.'],
    'E11': ['Distinguir avaliação retrospectiva (pode usar meses futuros) de alerta operacional (só passado).', 'Definir quais produtos são invalidados quando um mosaico histórico é corrigido.', 'Usar QGIS/GeoAI/Deepness/Geo-SAM para revisão humana e pré-anotação, medindo o custo por evento confirmado.'],
}
RISCOS = {
    'E02': 'Aprender diferenças de produto e processamento como se fossem mudanças no terreno.', 'E03': 'Vazamento espacial/temporal que infla as métricas.', 'E04': 'Máscaras convincentes porém sistematicamente erradas (viés de confirmação).',
    'E06': 'Acurácia global alta escondendo baixa detecção de eventos raros.', 'E07': 'Resultados de benchmarks (LEVIR-CD, SECOND) não transferem para 3–5 m.', 'E09': 'Contar repetidamente a mesma área como nova conversão independente.',
}
stage_name = {s[0]: s[1] for s in STAGES}
stage_note = {s[0]: f'{s[0]} {s[1]}' for s in STAGES}
for i, (sid, name, obj, ins, outs, trig) in enumerate(STAGES):
    papers = [byid[k] for k, v in stage_of.items() if sid in v]
    papers.sort(key=lambda r: ({'alta': 0, 'média': 1, 'baixa': 2}[prioridade(r)], r['n']))
    L = ['---', 'tipo: pipeline', f'etapa: {sid}', f'tags: [pipeline, etapa/{sid}]', '---', f'# {sid} — {name}\n', f'**Objetivo:** {obj}\n', f'**Entradas:** {ins}  \n**Saídas:** {outs}\n']
    if i: L.append(f'**Anterior:** [[{stage_note[STAGES[i-1][0]]}]]' + (f' · **Próxima:** [[{stage_note[STAGES[i+1][0]]}]]' if i + 1 < len(STAGES) else '') + '\n')
    else: L.append(f'**Próxima:** [[{stage_note[STAGES[1][0]]}]]\n')
    L.append('## Como fazer (decisões da literatura e do documento original)\n')
    L += [f'- {x}' for x in HOWTO[sid]]
    if sid in RISCOS: L.append(f'\n**Risco principal:** {RISCOS[sid]}')
    L.append('\n## Conceitos relacionados\n')
    L.append(', '.join(f'{cl(n)}' for n in trig if (any(n == k[1] for k in ent_papers))) or '—')
    L.append(f'\n## Artigos de apoio ({len(papers)})\n')
    L.append('| Prioridade | Artigo | Título | O que aproveitar |\n|---|---|---|---|')
    for r in papers[:40]:
        use = (r.get('bullets') or {}).get('Aplicação') or r.get('note') or ''
        L.append(f"| {prioridade(r)} | {wl(r, note_name(r))} | {r['title'][:60]} | {use[:110].replace('|', '/')} |")
    if len(papers) > 40: L.append(f'\n*(+{len(papers) - 40} artigos de prioridade menor; veja a tag `etapa/{sid}`.)*')
    L.append('\n## Experimentos ligados\n')
    L.append(', '.join(f'[[{e}]]' for e in [] ) or '')
    write(f'{V}/Pipeline/{stage_note[sid]}.md', '\n'.join(L) + '\n')

# ---------------------------------------------------------------- Experimentos
EXPS = [
    ('EXP0 Piloto de verificação dos dados', 'Inventariar, medir QA e registro; responder: produto, bandas, cadência real, meses disponíveis, deslocamento.', ['E01', 'E02', 'E03'], ['P46', 'P47', 'P75', 'P77'], 'Definir 3 m x 5 m, grade comum e quais meses são válidos.'),
    ('EXP1 Baseline de atributos (RF/XGBoost/LightGBM)', 'Baseline de ML com atributos espectrais/texturais + comparação temporal.', ['E05', 'E06'], ['P07', 'P42', 'P51', 'P52', 'P53', 'P54'], 'Um baseline tabular pode ser competitivo com poucos rótulos?'),
    ('EXP2 U-Net mensal + persistência', 'Segmentação mensal de cobertura com regra de persistência temporal.', ['E06', 'E09'], ['P01', 'P02', 'P03', 'P05'], 'A segmentação consistente basta para parte dos eventos?'),
    ('EXP3 Pares siameses (FC-Siam / ChangeFormer)', 'Aprender a mudança diretamente entre duas datas.', ['E07'], ['P23', 'P26', 'P25', 'P28'], 'Aprender a mudança reduz erros da pós-classificação?'),
    ('EXP4 Modelo semântico conjunto', 'Classes antes/depois e máscara de mudança coerentes entre si.', ['E07', 'E09'], ['P18', 'P19', 'P20', 'P21', 'P22'], 'A coerência entre classes e mudança melhora as transições?'),
    ('EXP5 Modelo de série temporal', 'TSSCD/U-TAE: localizar onde, quando e o que mudou usando o histórico.', ['E08'], ['P13', 'P14', 'P15', 'P12'], 'O histórico reduz sazonalidade e melhora a localização temporal?'),
    ('EXP6 Pré-anotação assistida (SAM/YOLO/QGIS)', 'AnyChange/SAM/YOLO como candidato e assistente de rotulagem, com revisão independente.', ['E04', 'E11'], ['P29', 'P56', 'P57', 'P58', 'P60', 'P62'], 'A pré-anotação reduz o esforço humano mantendo a qualidade?'),
]
EXPS = [(san(e[0]),) + tuple(e[1:]) for e in EXPS]
for name, desc, sts, ps, q in EXPS:
    L = ['---', 'tipo: experimento', 'status: planejado', f"etapas: {ylist([f'[[{stage_note[s]}|{s}]]' for s in sts])}", 'tags: [experimento]', '---', f'# {name}\n', f'{desc}\n', f'**Pergunta:** {q}\n',
         '## Etapas\n', ', '.join(f'[[{stage_note[s]}]]' for s in sts), '\n## Base bibliográfica\n']
    L += [f"- {wl(byid[p], note_name(byid[p]))} — {byid[p]['title'][:80]}" for p in ps if p in byid]
    L += ['\n## Protocolo mínimo\n', '- Mesmos conjuntos de teste e critérios dos demais experimentos (blocos geográficos + período posterior).', '- Registrar produto, resolução, bandas, número de datas de entrada e origem dos rótulos.',
          '- Reportar métricas em [[Quadro de resultados]].', '\n## Registro de execução\n', '| Data | Configuração | Resultado | Observações |\n|---|---|---|---|\n|  |  |  |  |']
    write(f'{V}/Experimentos/{name}.md', '\n'.join(L) + '\n')

write(f'{V}/Resultados/Quadro de resultados.md', '''---
tipo: resultados
tags: [resultados]
---
# Quadro de resultados

Preencha uma linha por experimento × produto × partição. Não compare com F1 publicado de outros benchmarks (classes, resolução, prevalência de mudança e divisão dos dados diferem).

| Experimento | Modelo | Produto/res. | Partição (espacial/temporal) | F1 mudança | IoU | Macro-F1 from–to | Erro de data | Área mapeada | Área estimada (IC) | Falsos alertas/km²/mês | Tempo de revisão |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |

## Leituras do quadro

- Responda às seis perguntas do piloto em [[00 Início]] (histórico mensal, área mínima, 3 m × 5 m, transferência, NIR × RGB, custo de revisão).
''')

# ---------------------------------------------------------------- Reuso
rows = []
for r in cat:
    hp = (ana.get(r['id']) or {}).get('hiperparametros')
    if hp: rows.append((r, hp))
L = ['---', 'tipo: reuso', 'tags: [reuso, receitas]', '---', '# Receitas de treino extraídas dos artigos\n',
     'Trechos detectados automaticamente nos PDFs (primeira ocorrência de cada item). **Confirme sempre no chunk indicado**; valores podem pertencer a um baseline e não ao modelo proposto.\n',
     '| Artigo | Taxa de aprendizado | Batch | Épocas | Otimizador | Perda | Patch | Chunk |', '|---|---|---|---|---|---|---|---|']
for r, hp in sorted(rows, key=lambda x: x[0]['n']):
    g = lambda k: f"`{hp[k]['trecho'][:34]}`" if k in hp else ''
    ch = next((v['chunk'] for v in hp.values()), '')
    L.append(f"| {wl(r)} | {g('taxa de aprendizado')} | {g('batch size')} | {g('épocas')} | {g('otimizador')} | {g('função de perda')} | {g('tamanho do patch')} | [[{r['id']} chunks#^{ch}\\|{ch[-4:]}]] |")
write(f'{V}/Reuso/Receitas de treino.md', '\n'.join(L) + '\n')

L = ['---', 'tipo: reuso', 'tags: [reuso, datasets]', '---', '# Datasets e benchmarks\n', 'Datasets citados (≥2 ocorrências no texto integral) e artigos de dataset da coleta.\n', '| Dataset | Resolução/produto | Para quê | Artigos |', '|---|---|---|---|']
DS_INFO = {'SpaceNet 7 (MUDS)': ('Planet ~4 m, mensal', 'edificações e identidade temporal'), 'DynamicEarthNet': ('Planet diário, rótulos mensais', 'mudança semântica multiclasse'),
           'LEVIR-CD': ('0,5 m', 'edificações (comparação de arquiteturas)'), 'SECOND': ('aéreo', 'mudança semântica bitemporal (SeK)'), 'HRSCD': ('aéreo RGB', 'multitarefa cobertura+mudança'),
           'OSCD': ('Sentinel-2', 'mudança urbana'), 'S2Looking': ('visada lateral', 'edificações'), 'PRODES': ('Landsat, anual', 'rótulo de desmatamento'), 'DETER': ('alertas', 'detecção operacional'),
           'MapBiomas': ('Landsat 30 m', 'pré-rótulos de cobertura'), 'Global Forest Change (Hansen)': ('Landsat 30 m', 'perda florestal global'), 'Dynamic World': ('Sentinel-2 10 m', 'cobertura com probabilidades'),
           'PASTIS': ('Sentinel-2', 'séries / segmentação panóptica'), 'OpenStreetMap': ('vetor', 'rótulos de vias/edificações'), 'WHU-CD': ('aéreo', 'edificações'), 'xBD': ('submétrico', 'dano em edificações'), 'DeepGlobe': ('0,5 m', 'vias')}
for (c, n), lst in sorted(ent_papers.items(), key=lambda x: -len(x[1])):
    if c != 'dataset': continue
    inf = DS_INFO.get(n, ('', ''))
    L.append(f"| {cl(n)} | {inf[0]} | {inf[1]} | " + ', '.join(wl(byid[i]) for i, _ in lst[:8]) + ' |')
L.append('\n## Artigos cuja contribuição é um dataset\n')
L += [f"- {wl(r, note_name(r))} — {r['title'][:90]}" for r in cat if r['kind'] == 'Dataset']
write(f'{V}/Reuso/Datasets e benchmarks.md', '\n'.join(L) + '\n')

L = ['---', 'tipo: reuso', 'tags: [reuso, codigo]', '---', '# Código, pacotes e plugins\n', f"Verificados em 24/10/2026 (GitHub/PyPI). Detalhes completos no README da raiz.\n", '| Ferramenta | Repositório | Estrelas | Licença | Último push |', '|---|---|---:|---|---|']
for n, v in tools['repos'].items():
    if v.get('ok'): L.append(f"| {n} | https://github.com/{v['repo']} | {v.get('stars')} | {v.get('license') or '—'} | {v.get('pushed')} |")
L.append('\n## Repositórios citados dentro dos PDFs\n')
for r in cat:
    g = (ana.get(r['id']) or {}).get('github')
    if g: L.append(f"- {wl(r)}: " + ' · '.join(g[:4]))
write(f'{V}/Reuso/Código e repositórios.md', '\n'.join(L) + '\n')

# metricas e protocolos
orig_sections = {}
def grab(h1, h2):
    m = re.search(h1 + r'(.*?)' + h2, orig_txt, re.S)
    return m.group(1).strip() if m else ''
tax = grab(r'## 11\. Taxonomia inicial proposta para as alterações', r'## 12\.')
met = grab(r'### 12\.4 Métricas mínimas', r'## 13\.')
split = grab(r'### 12\.3 Rótulos e separação dos dados', r'### 12\.4')
write(f'{V}/Reuso/Taxonomia from-to.md', '---\ntipo: reuso\ntags: [reuso, taxonomia]\n---\n# Taxonomia inicial de transições\n\nCopiada do documento original (seção 11). Proposta a validar com amostras locais.\n\n' + tax + '\n\nEtapa: [[E09 Pós-processamento e eventos]] · Avaliação: [[E10 Avaliação e incerteza]]\n')
write(f'{V}/Reuso/Métricas e protocolos.md', '---\ntipo: reuso\ntags: [reuso, metricas]\n---\n# Métricas e protocolos de avaliação\n\nDo documento original (seções 12.3 e 12.4). Conceitos: [[F1]], [[IoU - mIoU]], [[Kappa]], [[SeK]], [[Estimativa de área - IC]].\n\n## Rótulos e separação dos dados\n\n' + split + '\n\n## Métricas mínimas\n\n' + met + '\n')

# ---------------------------------------------------------------- Hub, guia, chunks, grafo
n_text = sum(1 for r in cat if r.get('pdf_file'))
L = ['---', 'tipo: hub', 'tags: [hub]', '---', '# 00 Início — Mudanças de cobertura com séries Planet\n',
     f'Vault construído a partir de **{len(cat)} artigos** ({n_text} com texto integral analisado em `coleta/`). **Autor da coleta:** Jean Michael Estevez Alvarez.\n',
     '## Perguntas do piloto\n', '1. O histórico mensal melhora a detecção em relação a pares de datas? → [[EXP5 Modelo de série temporal]]', '2. Qual a menor área/largura detectável? → [[E10 Avaliação e incerteza]]',
     '3. Diferença entre 3 m e 5 m? → [[EXP0 Piloto de verificação dos dados]]', '4. Quanto os erros aumentam ao mudar de ano, produto e setor? → [[E03 Cubo espaço-temporal e partições]]',
     '5. Benefício do NIR frente ao RGB? → [[E02 Qualidade e harmonização]]', '6. Custo de revisão humana por evento? → [[EXP6 Pré-anotação assistida (SAM-YOLO-QGIS)]]\n',
     '## Pipeline (do dado ao resultado)\n']
L += [f"{i+1}. [[{stage_note[s[0]]}]] — {s[2][:100]}" for i, s in enumerate(STAGES)]
L += ['', 'Mapa visual: [[Pipeline.canvas]]\n', '## Experimentos\n'] + [f'- [[{e[0]}]]' for e in EXPS] + ['- [[Quadro de resultados]]\n', '## Reuso\n',
      '- [[Receitas de treino]] · [[Datasets e benchmarks]] · [[Código e repositórios]] · [[Taxonomia from-to]] · [[Métricas e protocolos]]\n', '## Navegação\n',
      '- [[01 Guia de uso]] · [[02 Estratégia de chunks]] · [[03 Mapa do grafo]]\n', '## Ordem de leitura (prioridade alta)\n']
L += [f"- {wl(r, note_name(r))} — {r['title'][:90]}" for r in sorted(cat, key=lambda x: x['n']) if prioridade(r) == 'alta']
L += ['\n## Artigos por seção\n']
for k in SEC:
    L.append(f"- **{SEC[k]}** ({sum(1 for r in cat if r['section'] == k)}): " + ' '.join(wl(r) for r in sorted(cat, key=lambda x: x['n']) if r['section'] == k))
write(f'{V}/00 Início.md', '\n'.join(L) + '\n')

write(f'{V}/01 Guia de uso.md', '''---
tipo: guia
tags: [guia]
---
# Guia de uso do vault

## Como abrir
Abra a pasta `vault/` como vault no Obsidian. O grafo (Ctrl+G) já vem com cores por tipo de nota e esconde os arquivos de chunks.

## Tipos de nota
| Pasta | Conteúdo | Grafo |
|---|---|---|
| `Artigos/` | uma nota por artigo, com propriedades, reaproveitamento, limites e contextos | nós azuis |
| `Conceitos/` | sensores, datasets, métodos, métricas, tarefas e ferramentas (hubs) | nós coloridos por categoria |
| `Pipeline/` | 11 etapas do dado ao resultado | nós vermelhos |
| `Experimentos/` | EXP0–EXP6 com base bibliográfica e registro de execução | nós roxos |
| `Reuso/` | receitas de treino, datasets, código, taxonomia, métricas | nós verdes |
| `Chunks/` | texto do PDF dividido por seção, com âncoras `^ID` | oculto no grafo |

## Fluxo de trabalho sugerido
1. Comece por [[00 Início]] e pela lista de prioridade alta.
2. Ao ler um artigo, mude `status_leitura` (não lido → lendo → lido → aplicado) e escreva em **Anotações**.
3. Ao decidir algo (ex.: grade comum), registre na nota da etapa e linke os artigos que sustentam.
4. Execute um experimento: copie `Templates/Execução de experimento`, preencha e atualize o [[Quadro de resultados]].
5. Para citar um trecho: `![[P01 chunks#^P01_c017]]` incorpora o chunk.

## Consultas Dataview (opcional)
```dataview
TABLE ano, papel, prioridade FROM "Artigos" WHERE contains(etapas_pipeline, "E08") SORT prioridade ASC
```
```dataview
TABLE rows.file.link AS Artigos FROM "Artigos" FLATTEN datasets AS d GROUP BY d
```
```dataview
LIST FROM "Artigos" WHERE texto_integral = "nao" AND prioridade = "alta"
```

## Regras de confiança
- `fonte_analise` indica se a extração veio do texto integral ou só de metadados e comentário.
- Entidades, hiperparâmetros e frases de resultado são **extraídos por regra**; confirme no chunk antes de reutilizar.
- Nada aqui substitui a leitura integral dos artigos de prioridade alta.
''')

write(f'{V}/02 Estratégia de chunks.md', '''---
tipo: guia
tags: [guia, chunks]
---
# Estratégia de chunks

**Objetivo:** recuperar o trecho certo (método, dados, hiperparâmetros, resultados, limitações) sem misturar contextos, tanto no Obsidian quanto em busca semântica/RAG.

## Regras usadas
1. **Fronteira por seção.** O PDF é dividido em seções por cabeçalhos (numerados, em caixa-alta ou nomes padrão). Um chunk nunca atravessa duas seções.
2. **Tipo da seção:** resumo, introdução, trabalhos relacionados, dados, métodos, experimentos, resultados, discussão, conclusão. Referências e agradecimentos são descartados.
3. **Tamanho:** alvo de ~1.700 caracteres (≈400 tokens), no máximo ~2.400, com sobreposição de ~180 caracteres. Parágrafos são preservados; parágrafos gigantes são divididos por sentença. Chunks finais < 300 caracteres são fundidos ao anterior.
4. **Limpeza:** cabeçalhos e rodapés repetidos e números de página são removidos; hifenização de fim de linha é corrigida; ligaduras são normalizadas (NFKC).
5. **Metadados por chunk:** `paper`, `secao`, `titulo_secao`, `pagina`, entidades (sensor, dataset, método, métrica, tarefa, ferramenta), `tem_hiperparametros`, `tem_numeros_resultado`.

## Onde está
- `dados/chunks/Pxx.jsonl` — formato para embeddings/RAG (um JSON por linha).
- `vault/Chunks/Pxx chunks.md` — o mesmo texto em Markdown, com âncoras `^Pxx_cNNN` para `[[Pxx chunks#^Pxx_c017]]`.

## Quais chunks usar para quê
| Necessidade | Filtro | Etapa |
|---|---|---|
| Definir produto, área de estudo e rótulos | `secao = dados` | [[E01 Inventário e catálogo]], [[E04 Rotulagem e pré-anotação]] |
| Arquitetura e entradas | `secao = métodos` | [[E07 Modelos de mudança em pares]], [[E08 Modelos de série temporal]] |
| Receita de treino | `tem_hiperparametros` | [[Receitas de treino]] |
| Números para comparar | `tem_numeros_resultado` | [[Quadro de resultados]] |
| Limitações e riscos | `secao = discussão` | todas |
| Citação curta | `secao = resumo` | README / texto |

## Limites
- Extração por regra: artigos de duas colunas podem misturar linhas; tabelas e figuras não são reconstruídas.
- Seção mal detectada cai na seção anterior. Confira o título da seção no arquivo de chunks.
- Artigos sem PDF aberto (89 de 185) só têm metadados e comentário.
''')

# mapa do grafo
nedges = sum(len(v) for v in rel.values()) // 2
write(f'{V}/03 Mapa do grafo.md', f'''---
tipo: guia
tags: [guia, grafo]
---
# Mapa do grafo

```mermaid
graph LR
  A[Artigos] -->|usa| C[Conceitos: sensores, datasets, métodos, métricas]
  A -->|alimenta| P[Pipeline E01-E11]
  P --> X[Experimentos EXP0-EXP6]
  X --> R[Quadro de resultados]
  A -->|reuso| U[Receitas, datasets, código]
  A -.->|vizinhos| A
```

## Tipos de aresta
- **artigo → conceito** (propriedades `sensores`, `tarefas`, `metodos`, `datasets`, `metricas`, `ferramentas`): conecta artigos que usam o mesmo dado ou método.
- **artigo → etapa** (`etapas_pipeline`): diz em que ponto do fluxo cada artigo ajuda.
- **artigo ↔ artigo**: relação explícita do documento original ({nedges} pares) e vizinhos por entidades em comum.
- **experimento → artigos/etapas**: hipótese, base bibliográfica e protocolo.

## Como ler
- Selecione um dataset (ex.: [[SpaceNet 7 (MUDS)]]) e veja os artigos ao redor: são os que podem compartilhar rótulos ou protocolo.
- Selecione uma etapa e veja os conceitos e artigos que a sustentam.
- Etapas contíguas formam a espinha dorsal: E01 → E11. Abra [[Pipeline.canvas]].
''')

# templates
write(f'{V}/Templates/Novo artigo.md', '''---
tipo: artigo
id:
titulo: ""
autores: ""
ano:
secao:
tipo_publicacao: ""
papel: []
prioridade: baixa
doi: ""
pdf: ""
texto_integral: nao
sensores: []
tarefas: []
metodos: []
datasets: []
metricas: []
ferramentas: []
etapas_pipeline: []
status_leitura: não lido
tags: [artigo]
---
# ID — Título

## O que reaproveitar

## Limites e cuidados

## Contextos de uso no projeto

## Anotações
''')
write(f'{V}/Templates/Execução de experimento.md', '''---
tipo: execucao
experimento:
data:
tags: [execucao]
---
# Execução — {{title}}

- **Dados:** produto, resolução, bandas, meses, partição espacial/temporal
- **Rótulos:** origem, revisor, tamanho
- **Modelo:** arquitetura, entradas temporais, hiperparâmetros (links para [[Receitas de treino]])
- **Métricas:** ver [[Métricas e protocolos]]
- **Resultado:** (preencher [[Quadro de resultados]])
- **Problemas / próximos passos:**
''')

# canvas
nodes, edges = [], []
for i, (sid, name, *_ ) in enumerate(STAGES):
    nodes.append({'id': sid, 'type': 'file', 'file': f'Pipeline/{stage_note[sid]}.md', 'x': (i % 4) * 520, 'y': (i // 4) * 380, 'width': 440, 'height': 300, 'color': '1'})
    if i: edges.append({'id': f'e{i}', 'fromNode': STAGES[i - 1][0], 'toNode': sid, 'fromSide': 'right' if i % 4 else 'bottom', 'toSide': 'left' if i % 4 else 'top'})
for j, (name, *_ ) in enumerate(EXPS):
    nodes.append({'id': f'X{j}', 'type': 'file', 'file': f'Experimentos/{name}.md', 'x': j * 400, 'y': 1180, 'width': 360, 'height': 220, 'color': '6'})
    for s in EXPS[j][2]: edges.append({'id': f'x{j}{s}', 'fromNode': s, 'toNode': f'X{j}', 'fromSide': 'bottom', 'toSide': 'top'})
nodes.append({'id': 'R', 'type': 'file', 'file': 'Resultados/Quadro de resultados.md', 'x': 1200, 'y': 1550, 'width': 460, 'height': 200, 'color': '4'})
for j in range(len(EXPS)): edges.append({'id': f'r{j}', 'fromNode': f'X{j}', 'toNode': 'R', 'fromSide': 'bottom', 'toSide': 'top'})
write(f'{V}/Pipeline.canvas', json.dumps({'nodes': nodes, 'edges': edges}, ensure_ascii=False, indent=1))

# configuracao do obsidian
def rgb(h): return int(h, 16)
groups = [('path:Artigos', '4c9be8'), ('path:"Conceitos/Datasets"', 'f2b134'), ('path:"Conceitos/Métodos"', '9b6de0'), ('path:"Conceitos/Sensores e produtos"', '45b36b'),
          ('path:"Conceitos/Tarefas"', 'e8704c'), ('path:"Conceitos/Métricas"', 'd44f9a'), ('path:"Conceitos/Ferramentas"', '9aa5b1'), ('path:Pipeline', 'e03c3c'),
          ('path:Experimentos', '7a4de0'), ('path:Reuso', '2db39e'), ('path:Resultados', 'f2e234')]
write(f'{V}/.obsidian/graph.json', json.dumps({'search': '-path:Chunks -path:Templates', 'showTags': False, 'showAttachments': False, 'hideUnresolved': True,
    'colorGroups': [{'query': q, 'color': {'a': 1, 'rgb': rgb(c)}} for q, c in groups], 'showOrphans': False, 'centerStrength': 0.4, 'repelStrength': 12, 'linkStrength': 1, 'linkDistance': 200, 'nodeSizeMultiplier': 1.1}, indent=1))
write(f'{V}/.obsidian/app.json', json.dumps({'useMarkdownLinks': False, 'newLinkFormat': 'shortest', 'alwaysUpdateLinks': True, 'showFrontmatter': True}, indent=1))
write(f'{V}/.obsidian/core-plugins.json', json.dumps(['file-explorer', 'global-search', 'graph', 'backlink', 'outgoing-link', 'tag-pane', 'properties', 'canvas', 'outline', 'templates', 'page-preview'], indent=1))

# estatisticas
tot_links = 0
for dp, _, fs in os.walk(V):
    for f in fs:
        if f.endswith('.md') and '/Chunks' not in dp.replace('\\', '/'):
            tot_links += len(re.findall(r'\[\[', open(os.path.join(dp, f), encoding='utf-8').read()))
print('artigos', len(cat), '| conceitos', len(ent_papers), '| chunks arquivos', len(chunks_by), '| links', tot_links, '| pares explicitos', nedges)
