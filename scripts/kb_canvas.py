"""Geracao e validacao de arquivos .canvas (JSON Canvas) com disposicao controlada."""
import json, os, re

W, H, GX, GY, PAD, TOP = 320, 180, 120, 80, 40, 70   # cartao 320x180; intervalos 120 (horizontal) e 80 (vertical)
PAL = {'Artigos': '#3B82F6', 'Dados': '#06B6D4', 'Preparo': '#F97316', 'Métodos': '#8B5CF6', 'Validação': '#EAB308', 'Resultados': '#22C55E',
       'Monitoramento': '#14B8A6', 'Lacunas': '#EF4444', 'Conceitos': '#8B5CF6'}


def card_h(text):
    return 180 if len(text) <= 150 else 240


def build_columns(columns, edges=(), loop=None):
    """columns: lista de dict(name, color, cards=[dict(id, text|file, color?)]). Retorna dict canvas."""
    nodes, eds = [], []
    gw = W + 2 * PAD
    # altura de cada coluna
    heights = []
    for col in columns:
        h = TOP
        for c in col['cards']:
            c['_h'] = c.get('h') or (card_h(c['text']) if 'text' in c else H)
            h += c['_h'] + GY
        heights.append(h - GY + PAD)
    GH = max(heights)
    for i, col in enumerate(columns):
        x = i * (gw + GX)
        gid = f'g_{i}'
        nodes.append({'id': gid, 'type': 'group', 'x': x, 'y': 0, 'width': gw, 'height': GH, 'label': col['name'], 'color': col['color']})
        y = TOP
        for c in col['cards']:
            n = {'id': c['id'], 'x': x + PAD, 'y': y, 'width': W, 'height': c['_h'], 'color': c.get('color', col['color'])}
            if 'file' in c: n.update(type='file', file=c['file'])
            else: n.update(type='text', text=c['text'])
            nodes.append(n)
            y += c['_h'] + GY
        col['_gid'] = gid
    for k, (a, b, lab) in enumerate(edges):
        eds.append({'id': f'e{k}', 'fromNode': a, 'fromSide': 'right', 'toNode': b, 'toSide': 'left', 'label': lab, 'toEnd': 'arrow'})
    if loop:
        eds.append({'id': 'eloop', 'fromNode': loop[0], 'fromSide': 'bottom', 'toNode': loop[1], 'toSide': 'bottom', 'label': loop[2], 'toEnd': 'arrow'})
    return {'nodes': nodes, 'edges': eds}


def overview(columns_spec):
    cols = []
    for name, color, cards in columns_spec:
        cols.append(dict(name=name, color=color, cards=cards))
    edges = []
    labels = ['prepara', 'alimenta', 'avalia', 'gera', 'sustenta']
    for i in range(len(cols) - 1):
        edges.append((f'g_{i}', f'g_{i + 1}', labels[i]))
    return build_columns(cols, edges, loop=(f'g_{len(cols) - 1}', 'g_0', 'novos mosaicos'))


def validate(canvas, vault_root=None):
    issues = []
    nodes = {n['id']: n for n in canvas['nodes']}
    if len(nodes) != len(canvas['nodes']): issues.append('ids duplicados')
    groups = [n for n in canvas['nodes'] if n['type'] == 'group']
    cards = [n for n in canvas['nodes'] if n['type'] != 'group']

    def inter(a, b):
        return not (a['x'] + a['width'] <= b['x'] or b['x'] + b['width'] <= a['x'] or a['y'] + a['height'] <= b['y'] or b['y'] + b['height'] <= a['y'])

    for i, a in enumerate(cards):
        for b in cards[i + 1:]:
            if inter(a, b): issues.append(f'sobreposição de cartões: {a["id"]} x {b["id"]}')
    for i, a in enumerate(groups):
        for b in groups[i + 1:]:
            if inter(a, b): issues.append(f'sobreposição de grupos: {a["id"]} x {b["id"]}')
    for c in cards:
        inside = [g for g in groups if g['x'] <= c['x'] and g['y'] <= c['y'] and c['x'] + c['width'] <= g['x'] + g['width'] and c['y'] + c['height'] <= g['y'] + g['height']]
        if groups and not inside: issues.append(f'cartão fora de grupo: {c["id"]}')
    for e in canvas['edges']:
        if e['fromNode'] not in nodes or e['toNode'] not in nodes: issues.append(f'aresta com nó inexistente: {e["id"]}')
    if vault_root:
        for n in cards:
            if n['type'] == 'file' and not os.path.exists(os.path.join(vault_root, n['file'])): issues.append(f'arquivo inexistente: {n["file"]}')
    # arestas retas atravessando cartoes que nao sao suas extremidades
    def pt(n, side):
        return {'right': (n['x'] + n['width'], n['y'] + n['height'] / 2), 'left': (n['x'], n['y'] + n['height'] / 2), 'bottom': (n['x'] + n['width'] / 2, n['y'] + n['height']), 'top': (n['x'] + n['width'] / 2, n['y'])}[side]
    for e in canvas['edges']:
        if e['fromNode'] not in nodes or e['toNode'] not in nodes: continue
        if e['fromSide'] == e['toSide'] == 'bottom': continue
        (x1, y1), (x2, y2) = pt(nodes[e['fromNode']], e['fromSide']), pt(nodes[e['toNode']], e['toSide'])
        for c in cards:
            if c['id'] in (e['fromNode'], e['toNode']): continue
            # amostra pontos ao longo do segmento
            for t in [k / 40 for k in range(1, 40)]:
                x, y = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
                if c['x'] < x < c['x'] + c['width'] and c['y'] < y < c['y'] + c['height']:
                    issues.append(f'aresta {e["id"]} cruza cartão {c["id"]}'); break
    return issues


def themed(columns_spec, edges):
    """columns_spec: [(nome, cor, [dict(id,file)])]; edges: [(a,b,rotulo)] entre colunas adjacentes."""
    cols = [dict(name=n, color=c, cards=cards) for n, c, cards in columns_spec]
    return build_columns(cols, edges)


def save(path, canvas):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(canvas, f, ensure_ascii=False, indent=2)
