# Continuacao: canvas, configuracao do grafo, README, verificacao e zip (mesmo espaco de nomes).

# ============================================================ canvas
def cnote(fid): return f'{concepts[fid]["folder"]}/{fid}.md'
def card_text(title, body, link=None):
    t = f'**{title}**\n{body}'
    if link and link in ACTIVE: t += f'\n[[{link}]]'
    return t

def overview_canvas():
    P = C.PAL
    spec = [
     ('Dados', P['Dados'], [dict(id='d1', text=card_text('Planet NICFI / PlanetScope', 'Basemaps de 4 bandas; NICFI semestral até ago/2020, mensal depois.', 'PlanetNICFI')),
                           dict(id='d2', text=card_text('Sensores complementares', 'Sentinel-2, Sentinel-1, Landsat e imagens aéreas.', 'Sentinel2')),
                           dict(id='d3', text=card_text('Referências e benchmarks', 'PRODES, GFC, SpaceNet 7, DynamicEarthNet, HRSCD, SECOND.', 'DynamicEarthNet'))]),
     ('Preparação', P['Preparo'], [dict(id='p1', text=card_text('Qualidade da observação', 'Máscara de nuvem e sombra; corregistro; UDM.', 'MascaraNuvem')),
                                  dict(id='p2', text=card_text('Normalização e patches', 'Escala para 8 bits; recortes 256×256; aumento de dados.', 'Normalizacao')),
                                  dict(id='p3', text=card_text('Rotulagem', 'Sequencial e temporal; pré-anotação com SAM no QGIS.', 'Rotulagem'))]),
     ('Métodos', P['Métodos'], [dict(id='m1', text=card_text('ML sobre atributos', 'Random Forest, XGBoost; objetos + textura.', 'RandomForest')),
                              dict(id='m2', text=card_text('U-Net e CNN', 'Base dos estudos Planet lidos.', 'UNet')),
                              dict(id='m3', text=card_text('Mudança semântica', 'Siamesas, pós-classificação, SITS-SCD.', 'MudancaSemantica')),
                              dict(id='m4', text=card_text('Séries e fundacionais', 'U-TAE; SAM; modelos fundacionais.', 'UTAE'))]),
     ('Validação', P['Validação'], [dict(id='v1', text=card_text('Três regimes de partição', 'Sem shift, temporal e espacial; blocos com folga.', 'Generalizacao')),
                                  dict(id='v2', text=card_text('Métricas por tarefa', 'F1, IoU; SeK, SCS e SCOT para mudança.', 'MetricasMudancaSemantica')),
                                  dict(id='v3', text=card_text('Área com incerteza', 'Amostra probabilística e IC.', 'EstimativaArea'))]),
     ('Resultados', P['Resultados'], [dict(id='r1', text='**Mudança é rara**\n≈5% dos pixels por mês; OA engana.\n[[Achados_Relevantes]]'),
                                    dict(id='r2', text='**Shift espacial degrada**\nQueda média de SCS de 39% (P13).\n[[Matriz_Comparativa]]'),
                                    dict(id='r3', text='**Edificações em 4–5 px**\nF1 ≈ 0,45; mudança < 0,1.\n[[Sintese_Edificacoes_Vias]]')]),
     ('Monitoramento', P['Monitoramento'], [dict(id='o1', text=card_text('Revisão humana e QGIS', 'Pré-anotar e revisar eventos.', 'QGIS')),
                                          dict(id='o2', text=card_text('Alertas e falsos alertas', 'Latência, persistência e custo.', 'Alertas')),
                                          dict(id='o3', text='**Lacuna principal**\nPoucos estudos avaliam operação contínua.\n[[L01_ValidacaoOperacional]]')]),
    ]
    return C.overview(spec)

SHORT = {'trata a tarefa': 'tarefa', 'emprega conjunto de dados': 'emprega', 'utiliza método': 'método', 'é avaliado por': 'avaliado por', 'utiliza dado/sensor': 'dado', 'aplica etapa de preparo': 'preparo',
         'adota desenho de validação': 'validação', 'usa ferramenta': 'ferramenta', 'discute aspecto de monitoramento': 'monitora'}

def themed_canvas(articles, cons, lacs, name_title):
    arts = [p for p in articles if p in NAMES]
    cs = [c for c in cons if c in ACTIVE]
    ls = [l for l in lacs]
    # arestas
    e1 = []
    for p in arts:
        for fid, verb, n, pg, first in paper_concepts[p]:
            if fid in cs: e1.append((f'a_{p}', f'c_{fid}', SHORT.get(verb, 'refere')))
    lac_cons = {l[0]: [re.sub(r'«C:|»', '', t) for t in l[5]] for l in K.LACUNAS}
    e2 = [(f'c_{c}', f'l_{l}', 'lacuna') for l in ls for c in cs if c in lac_cons.get(l, [])]
    # ordenacao por baricentro para reduzir cruzamentos
    idx_a = {f'a_{p}': i for i, p in enumerate(arts)}
    def bary(cid):
        ys = [idx_a[a] for a, c, _ in e1 if c == cid and a in idx_a]
        return sum(ys) / len(ys) if ys else 99
    cs = sorted(cs, key=lambda c: bary(f'c_{c}'))
    idx_c = {f'c_{c}': i for i, c in enumerate(cs)}
    def bary2(lid):
        ys = [idx_c[c] for c, l, _ in e2 if l == lid and c in idx_c]
        return sum(ys) / len(ys) if ys else 99
    ls = sorted(ls, key=lambda l: bary2(f'l_{l}'))
    cols = [('Artigos', C.PAL['Artigos'], [dict(id=f'a_{p}', file=f'02_Artigos/{NAMES[p]}.md') for p in arts]),
            ('Conceitos', C.PAL['Métodos'], [dict(id=f'c_{c}', file=cnote(c)) for c in cs]),
            ('Lacunas', C.PAL['Lacunas'], [dict(id=f'l_{l}', file=f'09_Lacunas/{l}.md') for l in ls])]
    # remove duplicatas de arestas
    seen, ed = set(), []
    for a, b, lab in e1 + e2:
        if (a, b) not in seen: seen.add((a, b)); ed.append((a, b, lab))
    return C.themed(cols, ed)

def canvases():
    out = {}
    out['Mapa_Metodologico'] = overview_canvas()
    out['Canvas_MudancaSemantica'] = themed_canvas(['P10', 'P12', 'P13', 'P18', 'P19', 'P05', 'P14'], ['MudancaSemantica', 'SITS', 'UTAE', 'RedeSiamesa', 'DynamicEarthNet', 'HRSCD', 'SECOND', 'MetricasMudancaSemantica', 'PosClassificacao'],
                                                   ['L03_MudancaRara', 'L04_DomainShift', 'L06_MetricasIncomparaveis', 'L10_TaxonomiaTransicoes'], 'Mudança semântica')
    planet_arts = [p for p in PIDS if any(concepts[t[0]]['name'] in ('Planet NICFI', 'PlanetScope') and t[0] in ACTIVE for t in paper_concepts[p])]
    planet_arts = sorted(planet_arts, key=lambda p: (STATUS[p].startswith('extra'), int(p[1:])))[:12]
    out['Canvas_PlanetFloresta'] = themed_canvas(planet_arts, ['PlanetNICFI', 'PlanetScope', 'MascaraNuvem', 'MosaicosCompostos', 'Normalizacao', 'Desmatamento', 'UNet'], ['L02_CadenciaPlanet', 'L03_MudancaRara'], 'Planet')
    out['Canvas_Rotulagem_PreAnotacao'] = themed_canvas(['P165', 'P164', 'P155', 'P157', 'P156', 'P158', 'P10', 'P12', 'P01'], ['Rotulagem', 'RotulagemTemporal', 'PreAnotacaoSAM', 'SAM', 'QGIS', 'ModeloFundacional'], ['L05_RotulosTemporais', 'L08_FerramentasSemAvaliacao'], 'Rotulagem')
    ops = [p for p in PIDS if p in kb and monitor_class(p)[0].startswith('candidato')][:3]
    out['Canvas_Validacao_Monitoramento'] = themed_canvas(['P13', 'P12', 'P10', 'P18', 'P19', 'P05', 'P46'] + ops, ['Generalizacao', 'DivisaoEspacialBlocos', 'Desbalanceamento', 'EstimativaArea', 'MetricasMudancaSemantica', 'Alertas', 'RevisaoHumana', 'QuaseTempoReal'],
                                                      ['L01_ValidacaoOperacional', 'L03_MudancaRara', 'L04_DomainShift', 'L06_MetricasIncomparaveis'], 'Validação')
    stage_color = {'T1': 'Dados', 'T2': 'Preparo', 'T3': 'Preparo', 'T4': 'Métodos', 'T5': 'Métodos', 'T6': 'Validação', 'T7': 'Monitoramento'}
    tcols = [(f'{t[0][1:]}. {t[1]}', C.PAL[stage_color[t[0]]], [dict(id=f'{t[0]}_{p}', file=f'02_Artigos/{NAMES[p]}.md') for p, _ in t[3][:5] if p in NAMES]) for t in K.TRILHA]
    out['Canvas_Trilha_Objetivo'] = C.themed(tcols, [(f'g_{i}', f'g_{i + 1}', 'alimenta') for i in range(len(tcols) - 1)])
    issues = {}
    for k, cv in out.items():
        issues[k] = C.validate(cv, KB)
        C.save(f'{KB}/01_Mapas/{k}.canvas', cv)
    return issues, out

CANVAS_ISSUES, CANVASES = canvases()

# ============================================================ configuracao do Obsidian (grafo)
def rgb(h): return int(h.lstrip('#'), 16)
TIER_COLOR = {'A': '#1E40AF', 'B': '#3B82F6', 'C': '#93C5FD', 'D': '#CBD5E1'}
# o primeiro grupo que casa define a cor: as faixas de relevancia vem antes da pasta de artigos
groups = [('tag:#relevancia/A', TIER_COLOR['A']), ('tag:#relevancia/B', TIER_COLOR['B']), ('tag:#relevancia/C', TIER_COLOR['C']), ('tag:#relevancia/D', TIER_COLOR['D']), ('path:"01_Mapas"', '#475569'),
          ('path:"02_Artigos"', C.PAL['Artigos']), ('path:"03_Dados"', C.PAL['Dados']), ('path:"04_Preparo"', C.PAL['Preparo']), ('path:"05_Metodos"', C.PAL['Métodos']), ('path:"06_Validacao"', C.PAL['Validação']),
          ('path:"07_Resultados"', C.PAL['Resultados']), ('path:"08_Monitoramento"', C.PAL['Monitoramento']), ('path:"09_Lacunas"', C.PAL['Lacunas'])]
os.makedirs(f'{KB}/.obsidian', exist_ok=True)
GRAPH_SEARCH = '-path:"00_Painel" -path:"90_Anexos" -path:"99_Templates" -file:README -file:"Sem título" -file:Matriz_Comparativa -file:Estudos_Retrospectivos_vs_Operacionais'
json.dump({'collapse-filter': False, 'search': GRAPH_SEARCH, 'showTags': False, 'showAttachments': False, 'hideUnresolved': True, 'showOrphans': False,
           'collapse-color-groups': False, 'colorGroups': [{'query': q, 'color': {'a': 1, 'rgb': rgb(c)}} for q, c in groups], 'collapse-display': False, 'showArrow': False, 'textFadeMultiplier': -0.8,
           'nodeSizeMultiplier': 1.2, 'lineSizeMultiplier': 0.5, 'collapse-forces': False, 'centerStrength': 0.3, 'repelStrength': 16, 'linkStrength': 0.8, 'linkDistance': 260, 'scale': 0.5, 'close': False},
          open(f'{KB}/.obsidian/graph.json', 'w', encoding='utf-8'), indent=2)
json.dump({'useMarkdownLinks': False, 'newLinkFormat': 'shortest', 'alwaysUpdateLinks': True, 'attachmentFolderPath': '90_Anexos/figuras', 'showFrontmatter': True}, open(f'{KB}/.obsidian/app.json', 'w', encoding='utf-8'), indent=2)
json.dump(['file-explorer', 'global-search', 'graph', 'backlink', 'outgoing-link', 'tag-pane', 'properties', 'canvas', 'outline', 'templates', 'page-preview'], open(f'{KB}/.obsidian/core-plugins.json', 'w', encoding='utf-8'))
json.dump({'folder': '99_Templates'}, open(f'{KB}/.obsidian/templates.json', 'w', encoding='utf-8'))
for _f, _t in _keep.items(): open(f'{KB}/.obsidian/{_f}', 'w', encoding='utf-8').write(_t)

write('00_Painel/Guia_Grafo.md', '---\ntipo: painel\ntitulo: "Guia do grafo"\ntags: [painel, grafo]\n---\n\n# Guia do grafo\n\n'
      'O arquivo `.obsidian/graph.json` já traz os filtros e as cores abaixo. O Obsidian reescreve esse arquivo quando você mexe nos controles, e a interface pode variar conforme a versão instalada: se algum controle não existir na sua versão, aplique os valores manualmente em *Grafo → Configurações*.\n\n'
      '## Como o grafo foi organizado\n\n- **Artigos por relevância para o objetivo** (Planet de ~5 m): quatro tons de azul, do mais escuro (A, dado Planet de 3–5 m e alvo próximo, lido) ao mais claro (D, não lido). A definição está em [[Trilha_Objetivo_Planet5m]].\n'
      '- **Conceitos de preparo, validação e métrica só se ligam a artigos lidos.** Artigos não lidos ligam apenas a sensor, dado, tarefa e poucos métodos, para que conceitos genéricos (rotulagem, F1, IoU) não virem nós ligados a tudo.\n'
      '- **Painéis, anexos e templates ficam ocultos** (campo de busca do grafo). Os mapas (`01_Mapas`) ficam em cinza-escuro e funcionam como centros de cada etapa.\n'
      '- Relações entre artigos (usa o dado de, valida com, compara-se com) são links com explicação na seção 12 de cada nota.\n\n'
      '## Quatro visões úteis\n\n| Pergunta | Como ver |\n|---|---|\n| Quais artigos importam para o objetivo e como se relacionam? | Campo de busca do grafo: `tag:#relevancia/A OR tag:#relevancia/B` (só artigos, ligados pelas relações) |\n'
      '| O que sustenta cada etapa do fluxo? | Abra [[Trilha_Objetivo_Planet5m]] → Grafo local, profundidade 2 |\n| Quem usa um conceito ou dado? | Abra a nota do conceito → Grafo local, profundidade 1 |\n| Quais são as lacunas? | Campo de busca: `path:"09_Lacunas" OR tag:#relevancia/A` |\n\n'
      '## Cores (grupos)\n\n'
      'O Obsidian aplica a cor do **primeiro grupo da lista** que casa com o nó; se as cores aparecerem trocadas na sua versão, arraste os grupos de relevância para o topo.\n\n'
      '| Grupo | Cor | Consulta |\n|---|---|---|\n| Artigo relevância A | azul-escuro `#1E40AF` | `tag:#relevancia/A` |\n| Artigo relevância B | azul `#3B82F6` | `tag:#relevancia/B` |\n| Artigo relevância C | azul-claro `#93C5FD` | `tag:#relevancia/C` |\n| Artigo não lido (D) | cinza-azulado `#CBD5E1` | `tag:#relevancia/D` |\n| Mapas | cinza-escuro `#475569` | `path:"01_Mapas"` |\n| 03_Dados | ciano `#06B6D4` | `path:"03_Dados"` |\n| 04_Preparo | laranja `#F97316` | `path:"04_Preparo"` |\n'
      '| 05_Metodos | roxo `#8B5CF6` | `path:"05_Metodos"` |\n| 06_Validacao | amarelo `#EAB308` | `path:"06_Validacao"` |\n| 07_Resultados | verde `#22C55E` | `path:"07_Resultados"` |\n| 08_Monitoramento | turquesa `#14B8A6` | `path:"08_Monitoramento"` |\n| 09_Lacunas | vermelho `#EF4444` | `path:"09_Lacunas"` |\n\n'
      'Ciano e turquesa são próximos por pedido de paleta; se confundirem, aumente a saturação de um deles.\n\n## Filtros\n\n- Campo de busca do grafo: `-path:"00_Painel" -path:"90_Anexos" -path:"99_Templates" -file:README -file:"Sem título" -file:Matriz_Comparativa -file:Estudos_Retrospectivos_vs_Operacionais` (esconde painéis, anexos, templates, README e as duas tabelas que listam quase todos os artigos e virariam centros artificiais).\n- Desmarque “Anexos” e “Tags”; mantenha “Existentes apenas” ligado para ocultar links não resolvidos.\n- Para investigar, abra **Grafo local** (ícone no painel da nota) com **profundidade 1** (vizinhos diretos) ou **2** (vizinhos dos vizinhos). Em um conceito, a profundidade 1 mostra os artigos que o utilizam.\n\n'
      '## Forças (ponto de partida, não valores fixos)\n\n| Controle | Valor inicial | Como ajustar |\n|---|---|---|\n| Força central | 0,35 | aumente se os nós se espalham demais; diminua se tudo se aglomera |\n| Repulsão | 12 | suba (14–18) com mais de ~300 notas; desça (8–10) com poucas |\n| Força dos links | 1 | reduza (0,6–0,8) se os mapas puxam clusters demais |\n| Distância dos links | 220 | aumente (300+) com muitos nós para reduzir sobreposição |\n| Tamanho dos nós | 1 | opcional |\n\n'
      'O grafo de forças é dinâmico: as posições mudam a cada abertura e **não há garantia** de distância exata nem de ausência de sobreposição. Para uma disposição fixa use os Canvas (`01_Mapas/*.canvas`).\n\n[[00_Inicio|← Painel]]\n')

# ============================================================ verificacao
def wikilinks(text):
    text = re.sub(r'```.*?```|`[^`\n]*`', '', text, flags=re.S)
    out = []
    for m in re.finditer(r'!?\[\[([^\]]+)\]\]', text):
        t = m.group(1).replace('\\|', '|').split('|')[0].split('#')[0].strip()
        out.append((m.group(0).startswith('!'), t))
    return out

def verify(final=False):
    stems, dupstems = {}, []
    for dp, _, fs in os.walk(KB):
        if '.obsidian' in dp: continue
        for f in fs:
            if f.endswith('.md'):
                s = f[:-3]
                if s in stems: dupstems.append(s)
                stems[s] = os.path.join(dp, f)
    figs = set(os.listdir(f'{KB}/90_Anexos/figuras')) if os.path.isdir(f'{KB}/90_Anexos/figuras') else set()
    broken, inbound, nlinks = [], collections.Counter(), 0
    for s, p in stems.items():
        for emb, t in wikilinks(open(p, encoding='utf-8').read()):
            nlinks += 1
            if emb and t in figs: continue
            if t in stems: inbound[t] += 1
            else: broken.append((s, t))
    orphan = [s for s in stems if inbound[s] == 0 and not NOTE_FOLDER.get(s, '').startswith('99') and s not in ('00_Inicio',)]
    yaml_missing = []
    req = ['tipo', 'titulo', 'ano', 'autores', 'doi', 'arquivo_fonte', 'status_leitura', 'tags']
    notrace = []
    for pid in PIDS:
        t = open(stems[NAMES[pid]], encoding='utf-8').read()
        head = t.split('---')[1]
        for k in req:
            if not re.search(rf'^{k}:', head, re.M): yaml_missing.append((NAMES[pid], k))
        s8 = t.split('## 8.')[1].split('## 9.')[0]
        if not re.search(r'\(p\. |\(§|não informado|Não informado', s8): notrace.append(NAMES[pid])
    return dict(n_notas=len(stems), n_links=nlinks, broken=broken, dupstems=dupstems, orphan=orphan, yaml_missing=yaml_missing, notrace=notrace)

write('00_Painel/Verificacao.md', '---\ntipo: painel\ntitulo: "Verificação"\ntags: [painel]\n---\n\n# Verificação\n\n(em geração)\n\n[[00_Inicio|← Painel]]\n')
V1 = verify()
cv_lines = [f'- `{k}.canvas`: {len(cv["nodes"])} nós, {len(cv["edges"])} arestas — ' + ('válido, sem sobreposição geométrica' if not CANVAS_ISSUES[k] else f'{len(CANVAS_ISSUES[k])} problemas: {CANVAS_ISSUES[k][:3]}') for k, cv in CANVASES.items()]
n_fig_ok = sum(1 for v in FIGS.values() for f in v if os.path.exists(f'{KB}/90_Anexos/figuras/{f["file"]}'))
lines = ['---', 'tipo: painel', 'titulo: "Verificação"', 'tags: [painel]', '---', '', '# Verificação', '', f'Executada em {TODAY} pelo script `scripts/kb_build.py`.', '',
         f'- **Notas Markdown:** {V1["n_notas"]}; **wikilinks:** {V1["n_links"]}.', f'- **Links quebrados:** {len(V1["broken"])}' + (f' → {V1["broken"][:10]}' if V1['broken'] else '.'),
         f'- **Nomes de arquivo duplicados:** {len(V1["dupstems"])}' + (f' → {V1["dupstems"]}' if V1['dupstems'] else '.'),
         f'- **Notas órfãs (sem link de entrada):** {len(V1["orphan"])}' + (f' → {V1["orphan"][:20]}' if V1['orphan'] else '.'),
         f'- **Artigos com YAML incompleto:** {len(V1["yaml_missing"])}.', f'- **Artigos cuja seção 8 não traz página, seção ou “não informado”:** {len(V1["notrace"])}.',
         f'- **Trechos de evidência não localizados no texto (página não encontrada):** {len(unresolved)}' + (f' → {[(c, p, s[:40]) for c, p, s in unresolved[:8]]}' if unresolved else '.'),
         f'- **Figuras copiadas e embutidas:** {n_fig_ok} de {sum(len(v) for v in FIGS.values())}.', '', '## Canvas', ''] + cv_lines + ['',
         '**Verificação visual pendente:** a renderização no Obsidian não foi inspecionada (sem acesso ao aplicativo nesta execução); foi feita somente a checagem geométrica (sobreposição de cartões/grupos, cartões dentro dos grupos, arestas que cruzam cartões, ids e arquivos referenciados). '
         'Abra cada canvas, confira cortes de texto e ajuste alturas se necessário.', '', '## Rastreabilidade', '',
         '- Cada afirmação de leitura traz página (p.), seção (§) ou “não informado”. Trechos “detectados automaticamente” vêm de busca por padrões e **não foram lidos** por mim.',
         '- A conversão PDF→Markdown pode errar fórmulas, tabelas e ordem de colunas; confira o PDF quando um número for decisivo.', '', '[[00_Inicio|← Painel]]']
write('00_Painel/Verificacao.md', '\n'.join(lines) + '\n')
V = verify()

# ============================================================ README e zip
readme = f'''# Base de conhecimento — mudanças da cobertura terrestre com séries Planet

Vault Obsidian gerado em {TODAY} a partir de {len(PIDS)} artigos (texto convertido em `output/pdf/`). **Autor da coleta:** Jean Michael Estevez Alvarez.
Este vault **não substitui** o anterior (`../vault/`), que permanece intacto.

## Como abrir
1. No Obsidian: *Abrir pasta como cofre* → selecione `base_conhecimento/`.
2. Abra `00_Painel/00_Inicio.md`. Os mapas ficam em `01_Mapas/`; os canvases também (`Mapa_Metodologico.canvas` é o principal).
3. As figuras selecionadas estão em `90_Anexos/figuras/`. Os PDFs e o Markdown completo ficam fora do vault (`../coleta/`, `../output/pdf/`); as notas citam o caminho.

## Estrutura
`00_Painel` início e guias · `01_Mapas` mapas de conteúdo e canvases · `02_Artigos` uma nota por artigo ({len(PIDS)}) · `03_Dados` sensores, produtos e conjuntos · `04_Preparo` etapas de preparo · `05_Metodos` algoritmos, arquiteturas, estratégias e tarefas · `06_Validacao` desenhos e métricas · `07_Resultados` matriz comparativa e sínteses · `08_Monitoramento` operação e ferramentas · `09_Lacunas` · `90_Anexos` inventário, duplicatas, original e figuras · `99_Templates`.

## Convenções
- Relações são **links no texto** com o significado ao lado (“utiliza método: …”, “emprega conjunto de dados: …”, “é avaliado por: …”).
- Artigos ligam-se entre si só quando há comparação substantiva (explicada na seção 12); o resto da conexão passa por conceitos compartilhados.
- `status_leitura`: *lido (profundo)* · *lido (parcial)* · *extraído automaticamente (não lido)*. Onde faltou informação consta “não informado”.
- **Evidência vs. interpretação:** cada nota rotula o que é fato do artigo (com página) e o que é leitura da base.

## Grafo e Canvas
Veja `00_Painel/Guia_Grafo.md` (cores por pasta, filtros, grafo local de profundidade 1–2 e forças iniciais). Canvases: cartões de 320×180, intervalos de 120 (horizontal) e 80 (vertical), cores da mesma paleta do grafo.

## Verificação
`00_Painel/Verificacao.md`: {V["n_notas"]} notas, {V["n_links"]} wikilinks, {len(V["broken"])} links quebrados, {len(V["dupstems"])} nomes duplicados, {len(V["orphan"])} órfãs. Canvases validados geometricamente; **inspeção visual pendente**.

## Regenerar
`python -I scripts/kb_extract.py .` e `python -I scripts/kb_build.py .` (a pasta `base_conhecimento/` é recriada; copie edições manuais antes).
'''
open(f'{KB}/README.md', 'w', encoding='utf-8').write(readme)
zp = f'{ROOT}/base_conhecimento.zip'
if os.path.exists(zp): os.remove(zp)
with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED) as z:
    for dp, _, fs in os.walk(KB):
        for f in fs: z.write(os.path.join(dp, f), os.path.relpath(os.path.join(dp, f), ROOT))
print('RESULTADO | notas', V['n_notas'], '| links', V['n_links'], '| quebrados', len(V['broken']), '| duplicados', len(V['dupstems']), '| orfas', len(V['orphan']), '| yaml', len(V['yaml_missing']),
      '| sem rastreio', len(V['notrace']), '| nao localizados', len(unresolved))
for k, v in CANVAS_ISSUES.items(): print('canvas', k, 'problemas', len(v), v[:3])
print('quebrados', V['broken'][:10]); print('orfas', V['orphan'][:15])
