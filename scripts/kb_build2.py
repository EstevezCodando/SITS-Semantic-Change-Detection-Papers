# Continuacao de kb_build.py (executado no mesmo espaco de nomes): conceitos, mapas, lacunas, resultados, monitoramento,
# painel, anexos, templates, canvas, configuracao do grafo, README, verificacao e zip.

TODAY = '24/10/2026'

# ============================================================ conceitos
def concept_note(fid):
    c = concepts[fid]
    sup = sorted(c['sup'], key=lambda x: (-(x[2] or 0), x[0]))
    fm = ['---', 'tipo: conceito', f'subtipo: {yq(c["tipo"])}', f'titulo: {yq(c["titulo"])}', f'aliases: {ylist([c["titulo"]])}', f'pasta_tematica: {yq(c["folder"])}', f'n_artigos: {len(sup)}',
          f'tags: [conceito, {fold(c["tipo"]).split("/")[0].replace(" ", "-")}]', '---', '']
    b = [f'# {c["titulo"]}', '', f'**Natureza:** {c["tipo"]}. A base distingue algoritmo, arquitetura, ferramenta, tarefa, etapa metodológica, dado e desenho de validação por este campo.', '',
         '> *Definição, pressupostos e limitações* abaixo são **interpretação/conhecimento geral da base**, salvo onde há token de página. Os fatos dos artigos estão na tabela de evidências.', '',
         '## Definição', '', resolve(c['d'], f'conceito {fid}'), '', '## Finalidade', '', c['fin'], '', '## Entradas', '', c['ent'], '', '## Saídas', '', c['sai'], '',
         '## Pressupostos', '', c['pres'], '', '## Limitações', '', c['lim'], '', '## Evidência nos artigos lidos', '',
         '| Artigo | Relação | Ocorrências | Páginas | Status de leitura |', '|---|---|---:|---|---|']
    for pid, verb, n, pg, first in sup:
        b.append(f'| {plink(pid)} | {verb} | {n or "—"} | {pgs(pg) if pg else "ver nota do artigo"} | {STATUS[pid]} |')
    b += ['', '## Navegação', '']
    for m in MOC_OF.get(fid, []): b.append(f'- Mapa: [[{m[0]}|{m[1]}]]')
    lac = [l for l in K.LACUNAS if f'«C:{fid}»' in l[5]]
    for l in lac: b.append(f'- Lacuna que afeta este conceito: [[{l[0]}|{l[1]}]]')
    write(f'{c["folder"]}/{fid}.md', '\n'.join(fm + b) + '\n')


MOC_OF = {}


# ============================================================ lacunas
def lacunas():
    cstat = collections.Counter()
    for pid in PIDS:
        c_ = codigo(pid)
        cstat['sim' if c_.startswith('sim') else 'dados' if c_.startswith('dados') else 'declarado' if c_.startswith('declarado') else 'não informado'] += 1
    for lid, titulo, tema, desc, evs, cons, opp in K.LACUNAS:
        fm = ['---', 'tipo: lacuna', f'titulo: {yq(titulo)}', f'tema: {tema}', 'status: aberta', 'tags: [lacuna]', '---', '']
        b = [f'# {titulo}', '', '## Descrição', '', resolve(desc, lid), '', '## Evidências nos artigos', '']
        for e in evs: b.append(f'- {resolve(e, lid)}')
        if lid.startswith('L09'):
            b += ['', f'Contagem automática em {len(PIDS)} artigos (a partir do texto convertido): código em repositório {cstat["sim"]}; apenas dados {cstat["dados"]}; declarado sem URL {cstat["declarado"]}; não informado {cstat["não informado"]}. Ver [[Matriz_Comparativa]].']
        b += ['', '## O que isto afeta (método, dado ou resultado)', '']
        for t in cons:
            fid = re.sub(r'«C:|»', '', t)
            if fid in ACTIVE: b.append(f'- afeta {concepts[fid]["tipo"]}: [[{fid}|{concepts[fid]["titulo"]}]]')
        b += ['', '## Oportunidade (interpretação)', '', opp, '', '[[00_Sintese_Lacunas|← Síntese das lacunas]]']
        write(f'09_Lacunas/{lid}.md', '\n'.join(fm + b) + '\n')
    fm = ['---', 'tipo: mapa', 'titulo: "Síntese das lacunas"', 'tags: [lacuna, mapa]', '---', '']
    b = ['# Síntese das lacunas', '', 'Cada lacuna tem evidências com página e uma oportunidade (interpretação).', '', '| Lacuna | Tema | Resumo |', '|---|---|---|']
    unlink = lambda s_: re.sub(r'\[\[[^\]|]*\|([^\]]*)\]\]', r'\1', s_)
    for lid, titulo, tema, desc, *_ in K.LACUNAS: b.append(f'| [[{lid}\\|{titulo}]] | {tema} | {unlink(resolve(desc, lid))[:170].replace("|", "/")}… |')
    b += ['', '[[00_Inicio|← Painel]]']
    write('09_Lacunas/00_Sintese_Lacunas.md', '\n'.join(fm + b) + '\n')


# ============================================================ matriz comparativa
def auto_row(pid):
    v = kb[pid]
    sens = [n for n, e in cites(pid, 'sensor', 3, 3)] + [n for n, e in cites(pid, 'dataset', 3, 2)]
    res = resolutions(pid)
    lim = v['ev']['limitacoes'][0] if v['ev']['limitacoes'] else None
    return dict(tarefa='; '.join(task_names(pid)) or 'não informado (título/resumo sem padrão reconhecido)', dados='; '.join(sens) or 'não informado', resolucao='; '.join(f'{a} (p. {p})' for a, p in res) or 'não informado',
                preparo='; '.join(n for n, e in cites(pid, 'preparo', 4, 3)) or 'não informado', metodo='; '.join(n for n, e in cites(pid, 'metodo', 4, 3)) or 'não informado', temporal=temporal(pid),
                validacao='; '.join(n for n, e in cites(pid, 'validacao', 3, 3)) or 'não informado', metricas='; '.join(n for n, e in cites(pid, 'metrica', 4, 3)) or 'não informado',
                limitacoes=(f'{lim["t"][:110]}… (p. {lim["p"]})' if lim else 'não informado'), codigo=codigo(pid))

COLS = ['tarefa', 'dados', 'resolucao', 'preparo', 'metodo', 'temporal', 'validacao', 'metricas', 'limitacoes', 'codigo']
def matriz():
    rows = []
    for pid in PIDS:
        if pid in K.MATRIX_A:
            d = dict(K.MATRIX_A[pid]); d['temporal'] = d.pop('temporal'); origem = 'curada pela leitura'
        elif pid in kb:
            d = auto_row(pid); origem = 'automática (verificar)'
        else:
            continue
        d['pid'] = pid; d['origem'] = origem; rows.append(d)
    with open(f'{KB}/07_Resultados/Matriz_Comparativa.csv', 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, delimiter=';'); w.writerow(['artigo', 'status_leitura', 'origem'] + COLS)
        for d in rows: w.writerow([NAMES[d['pid']], STATUS[d['pid']], d['origem']] + [d[c] for c in COLS])
    fm = ['---', 'tipo: resultado', 'titulo: "Matriz comparativa dos estudos"', 'tags: [resultado, matriz]', '---', '']
    b = ['# Matriz comparativa dos estudos', '',
         '> **Aviso de comparabilidade.** As colunas descrevem cada estudo; **não** ordenam modelos. Métricas de bases, classes, resoluções e desenhos de validação diferentes não são comparáveis. '
         'Todas as linhas vêm das fichas de leitura. Versão completa em `Matriz_Comparativa.csv` nesta pasta.', '',
         '## Estudos lidos (curada pela leitura)', '', '| Artigo | tarefa | dados | resolução | preparo | método | estratégia temporal | validação | métricas | limitações | código disponível |', '|---|---|---|---|---|---|---|---|---|---|---|']
    for d in rows:
        if d['origem'].startswith('curada'):
            b.append(f'| {plink(d["pid"])} | ' + ' | '.join(d[c].replace('|', '/') for c in COLS) + ' |')
    b += ['', '## Retrospectivo vs. operacional', '', 'Ver [[Estudos_Retrospectivos_vs_Operacionais]]. Nenhum estudo aprofundado foi avaliado em monitoramento contínuo.', '', '[[00_Inicio|← Painel]]']
    write('07_Resultados/Matriz_Comparativa.md', '\n'.join(fm + b) + '\n')
    return rows


# ============================================================ monitoramento
MKEYS = ['Quase tempo real', 'Latência / frequência', 'Falsos alertas', 'Persistência / confirmação', 'Revisão humana', 'Drift', 'Custo', 'Rastreabilidade', 'Alertas', 'Sistema operacional']
def monitoramento():
    fm = ['---', 'tipo: monitoramento', 'titulo: "Estudos retrospectivos vs. operacionais"', 'tags: [monitoramento, matriz]', '---', '']
    b = ['# Estudos retrospectivos vs. operacionais', '',
         'Um sistema de monitoramento contínuo exige evidência de frequência de atualização, latência, falsos alertas, persistência, revisão humana, drift, custos e rastreabilidade. '
         'A tabela mostra a **contagem de menções** de cada termo (não é avaliação) e a classificação. “Custo” inclui custo computacional, por isso aparece em quase todos os artigos.', '',
         '| Artigo | Classificação | ' + ' | '.join(MKEYS) + ' |', '|---|---|' + '---|' * len(MKEYS)]
    for pid in PIDS:
        v = kb.get(pid)
        if not v: continue
        cl, why = monitor_class(pid)
        m = v['ents'].get('monitoramento', {})
        cells = [(f'{m[k]["n"]} (p. {pgs(m[k]["paginas"][:2])})' if k in m else '—') for k in MKEYS]
        b.append(f'| {plink(pid)} | {cl[:60]} | ' + ' | '.join(cells) + ' |')
    b += ['', '## Leitura da tabela', '',
          '- Classificações curadas (leitura): ' + '; '.join(f'{plink(p)} → {c}' for p, (c, _) in K.MONITORAMENTO_MANUAL.items() if p in NAMES) + '.',
          '- “candidato a sistema operacional” significa apenas que o texto menciona operação e alertas; **deve ser verificado** (ex.: sistemas DETER).',
          '- Lacuna principal: [[L01_ValidacaoOperacional]].', '', '[[00_Inicio|← Painel]]']
    write('08_Monitoramento/Estudos_Retrospectivos_vs_Operacionais.md', '\n'.join(fm + b) + '\n')


# ============================================================ resultados escritos
def resultados():
    fm = lambda t: ['---', 'tipo: resultado', f'titulo: {yq(t)}', 'tags: [resultado]', '---', '']
    ach = [
        ('Shift espacial é o que mais degrada o desempenho', '«P13|average relative drop of the mIoU»: queda média de mIoU de 31,9% (DynamicEarthNet) e 10,5% (MUDS); o shift temporal afeta principalmente a detecção de mudança.', ['Generalizacao', 'DivisaoEspacialBlocos', 'DivisaoTemporal']),
        ('A mudança é rara', '«P18|99.232% of all pixels are labelled as no change» e «P12|only 5% of all pixels change from month to month».', ['Desbalanceamento', 'AcuraciaGlobal']),
        ('Mais datas nem sempre ajudam', '«P12|using weekly samples is optimal for the considered baselines»: observações diárias são correlacionadas e desestabilizam o treino.', ['SITS', 'UTAE']),
        ('Edificações de 4–5 px têm F1 em torno de 0,45', '«P10|Intriguingly, our object detection performance of F1 = 0.45» para objetos de 4–5 px; o termo de mudança do SCOT foi 0,06–0,07.', ['SpaceNet7_MUDS', 'MetricasMudancaSemantica']),
        ('Mudança direta e pós-classificação em PlanetScope', '«P05|El esquema número 2 fue el más apropiado» (mudança direta), com a ressalva de uma só mina e oito datas.', ['PosClassificacao', 'UNet']),
        ('NDVI não ajudou como entrada extra', '«P05|no hay un mayor aporte»: modelos de 4 bandas igualaram ou superaram os de 5.', ['IndicesEspectrais']),
        ('Objetos e textura compensam o espectro do Planet', '«P07|Using only the PL dataset with a typical RF PB approach produced the worse overall accuracy» (66,7%); com objetos, 82,2% no mesmo dado.', ['OBIA', 'Textura', 'RandomForest']),
        ('Mais pontos de prompt não melhoram sempre o SAM', '«P165|an excessive number of points prompts generally degrades»: o ótimo ficou em ~20–30 pontos; contraste do alvo prevê o sucesso.', ['SAM', 'PreAnotacaoSAM']),
        ('Parâmetros do plugin importam tanto quanto o modelo', '«P158|The 12% tile overlap was selected»: resolução, sobreposição e remoção de segmentos levaram o F1 de 48,1% a 78,6%.', ['QGIS']),
        ('Métricas próprias para mudança semântica', '«P19|dominant non-change pixels would cause unreasonable scores»: SeK, SCS e SCOT foram criadas para evitar que a classe “sem mudança” domine.', ['MetricasMudancaSemantica']),
    ]
    b = fm('Achados relevantes') + ['# Achados relevantes', '', '> Cada achado vale **dentro** do estudo citado. Não compare valores entre bases diferentes. As frases de “interpretação” estão marcadas.', '']
    for i, (t, e, cs) in enumerate(ach, 1):
        b += [f'## {i}. {t}', '', f'**Evidência:** {resolve(e, "achados")}', '', '**Conceitos:** ' + ', '.join(clink(c) for c in cs if c in ACTIVE), '']
    b += ['', '[[00_Inicio|← Painel]]']
    write('07_Resultados/Achados_Relevantes.md', '\n'.join(b) + '\n')
    # sinteses por tema (curtas, com links)
    def synth(file, titulo, intro, bullets, concepts_):
        t = fm(titulo) + [f'# {titulo}', '', intro, '']
        t += [f'- {resolve(x, file)}' for x in bullets]
        t += ['', '**Conceitos:** ' + ', '.join(clink(c) for c in concepts_ if c in ACTIVE), '', '**Lacunas:** [[00_Sintese_Lacunas]]', '', '[[00_Inicio|← Painel]]']
        write(f'07_Resultados/{file}.md', '\n'.join(t) + '\n')
    # sinteses das fichas (reescritas com links novos)
    names = {'_sintese_rotulagem.md': 'Sintese_Rotulagem', '_sintese_metricas.md': 'Sintese_Metricas', '_sintese_particoes.md': 'Sintese_Particoes', '_sintese_receitas.md': 'Sintese_Receitas',
             '_sintese_planet.md': 'Sintese_Planet', '_sintese_qgis_geoai.md': 'Sintese_QGIS_GeoAI', '_sintese_decisoes.md': 'Sintese_Decisoes'}
    for f, (meta, body) in SYN.items():
        nm = names.get(f)
        if not nm: continue
        t = conv_ficha('P00', body)
        t = re.sub(r'\[\[(E\d\d [^\]|]+)(\|[^\]]*)?\]\]', lambda m: (m.group(2) or '|' + m.group(1)).lstrip('|'), t)
        write(f'07_Resultados/{nm}.md', '\n'.join(fm(meta['titulo']) + [f'# {meta["titulo"]}', '', '> Síntese herdada do vault anterior (`vault/`); os links de artigos foram convertidos para esta base. Afirmações sobre artigos têm fonte nas respectivas notas; itens “hipótese” são interpretação.', '', t, '', '[[00_Inicio|← Painel]]']) + '\n')


# ============================================================ anexos
def anexos():
    sem_texto = [r for r in cat.values() if r['id'] not in PIDS_ALL]
    return [], [], sem_texto


# ============================================================ painel
def painel(rows_inv, sem_texto, dup):
    n_prof = sum(1 for p in PIDS if STATUS[p] == 'lido (profundo)'); n_par = sum(1 for p in PIDS if STATUS[p] == 'lido (parcial)'); n_nl = len(PIDS_ALL) - len(PIDS)
    fm = ['---', 'tipo: painel', 'titulo: "Painel — mudanças da cobertura terrestre com séries Planet"', 'tags: [painel]', '---', '']
    b = ['# Painel — mudanças da cobertura terrestre com séries Planet', '',
         f'Base de conhecimento construída em {TODAY}. **Autor da coleta:** Jean Michael Estevez Alvarez. Há nota para os **{len(PIDS)} artigos lidos** ({n_prof} em profundidade e {n_par} em parte); os outros {n_nl} textos convertidos ficam listados em [[Pendencias_Leitura]], com o caminho do Markdown, e {len(sem_texto)} registros do catálogo não têm texto integral.', '',
         '## Comece aqui', '', '- [[Trilha_Objetivo_Planet5m]] — o fluxo do objetivo (Planet de ~5 m: construção, supressão de vegetação, vias) ligado aos artigos de maior relevância.', '',
         '## Conhecimento', '', '- [[Matriz_Comparativa]] · [[Achados_Relevantes]] · [[Estudos_Retrospectivos_vs_Operacionais]]', '- [[00_Sintese_Lacunas]]',
         '- Sínteses: [[Sintese_Receitas]] · [[Sintese_Decisoes]] · [[Sintese_Planet]] · [[Sintese_Rotulagem]] · [[Sintese_Metricas]] · [[Sintese_Particoes]] · [[Sintese_QGIS_GeoAI]]', '',
         '## Navegação', '', '- [[Guia_Navegacao]] · [[Guia_Grafo]] · [[Pendencias_Leitura]] · [[Verificacao]]', '', '## Canvas', '', '- `Canvas_Trilha_Objetivo.canvas` e `Mapa_Metodologico.canvas` na pasta `01_Mapas`.']
    write('00_Painel/00_Inicio.md', '\n'.join(fm + b) + '\n')
    nav = ['---', 'tipo: painel', 'titulo: "Guia de navegação"', 'tags: [painel]', '---', '', '# Guia de navegação', '',
           '1. Comece em [[00_Inicio]] e abra [[Trilha_Objetivo_Planet5m]].', '2. A trilha aponta para os **artigos** (`02_Artigos`) e para os **conceitos** do projeto (dado, preparo, método, validação e monitoramento). Cada conceito traz a tabela dos artigos que o usam e as páginas.',
           '3. Cada artigo tem as mesmas 12 seções e separa *evidência do artigo* de *interpretação*.', '4. Para comparar estudos use [[Matriz_Comparativa]], sem classificar superioridade entre bases diferentes.',
           '5. Para investigar uma nota, abra o **grafo local** (profundidade 1 ou 2). Veja [[Guia_Grafo]].', '',
           '## Convenções', '', '- `status_leitura`: *lido (profundo)* ou *lido (parcial)*. Textos não lidos não têm nota; veja [[Pendencias_Leitura]].', '- “não informado”: o texto convertido não trouxe a informação.',
           '- Páginas (p. N) são as do PDF; § indica seção. Itens “detectado automaticamente” devem ser conferidos na página.', '- Novos artigos: copie `99_Templates/Template_Artigo.md`.', '', '[[00_Inicio|← Painel]]']
    write('00_Painel/Guia_Navegacao.md', '\n'.join(nav) + '\n')
    p = ['---', 'tipo: painel', 'titulo: "Pendências de leitura"', 'tags: [painel, pendencias]', '---', '', '# Pendências de leitura', '',
         'Registro explícito do que foi lido e do que falta.', '', '## Lidos em profundidade', '']
    p += [f'- {plink(x)}' for x in PIDS if STATUS[x] == 'lido (profundo)']
    p += ['', '## Leitura parcial (falta texto integral ou verificação)', ''] + [f'- {plink(x)} — ver seção 9 da nota' for x in PIDS if STATUS[x] == 'lido (parcial)']
    rk = f'{DATA}/ranking_relevancia.json'
    R = json.load(open(rk, encoding='utf-8')) if os.path.exists(rk) else []
    sc = {r['id']: r for r in R}
    nl = [x for x in PIDS_ALL if x not in LP]
    nl.sort(key=lambda x: -(sc[x]['score'] if x in sc else 0))
    p += ['', f'## Não lidos ({len(nl)}): texto convertido sem nota', '',
          'Ordenados por uma pontuação automática de relevância (contagem de termos no texto: Planet/NICFI, resolução de 3–5 m, mudança, desmatamento, edificações e vias, séries, métodos e métricas; peso maior no início). **É triagem, não avaliação.** Para ler, abra o Markdown indicado.', '',
          '| Artigo | Título | Pontuação | Menções a Planet | Markdown |', '|---|---|---:|---:|---|']
    for x in nl:
        v = kb.get(x); r = cat[x]
        p.append(f'| {label(x)} | {r["title"][:80].replace("|", "/")} | {sc[x]["score"] if x in sc else "—"} | {sc[x]["planet"] if x in sc else "—"} | `{("output/pdf/" + v["dir"] + "/document.md") if v else "não informado"}` |')
    p += ['', f'## Sem texto integral ({len(sem_texto)})', '', 'Registros do catálogo sem PDF aberto: veja `coleta/_manifesto.csv` e o README da raiz.', '', '[[00_Inicio|← Painel]]']
    write('00_Painel/Pendencias_Leitura.md', '\n'.join(p) + '\n')


# ============================================================ templates
def templates():
    write('99_Templates/Template_Artigo.md', '---\ntipo: artigo\nid_origem: \ntitulo: ""\nano: \nautores: []\ndoi: "não informado"\narquivo_fonte: ""\nmarkdown_fonte: ""\npaginas: \ntipo_documento: ""\nstatus_leitura: "não lido"\ntarefas: []\nsensores: []\nconjuntos_dados: []\nmetodos: []\npreparo: []\nvalidacao: []\nferramentas: []\ntags: [artigo]\n---\n\n# Autor Ano — Título\n\n'
          '> Evidência do artigo (com página) vs. Interpretação (rotulada). Use “não informado” quando faltar.\n\n## 1. Referência bibliográfica e acesso ao original\n\n## 2. Problema investigado e contribuição principal\n\n## 3. Área de estudo e período analisado\n\n## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo\n\n## 5. Preparação\n\n## 6. Análise\n\n## 7. Validação\n\n## 8. Resultados\n\n## 9. Limitações e condições de aplicabilidade\n\n## 10. Reprodutibilidade\n\n## 11. Aplicabilidade ao monitoramento contínuo\n\n## 12. Relações justificadas com outras notas\n\n- utiliza método: `[[Conceito]]` — (p. )\n')


# ============================================================ trilha para o objetivo
def trilha():
    cnt = collections.Counter(TIER[p] for p in PIDS_ALL)
    b = ['---', 'tipo: mapa', 'titulo: "Trilha para o objetivo"', 'tags: [mapa, trilha]', '---', '',
         '# Trilha para o objetivo: detectar mudanças de cobertura com Planet de ~5 m', '',
         '> **Objetivo:** identificar de forma automática mudanças na cobertura do solo com imagens ópticas Planet de ~5 m (início de construções, supressão da vegetação, vias). '
         'Esta página liga cada etapa do fluxo aos artigos que a sustentam. **Os valores são os relatados por cada estudo e não são comparáveis entre bases diferentes.** A última seção é proposta (interpretação), não resultado.', '',
         '## Relevância dos artigos', '',
         f'Campo `relevancia_objetivo` de cada nota: **A** ({cnt["A"]}) dado Planet de 3–5 m e alvo próximo, texto lido; **B** ({cnt["B"]}) método, validação ou alerta transferível, texto lido; **C** ({cnt["C"]}) contexto, revisão ou ferramenta; **D** ({cnt["D"]}) não lido, ver [[Pendencias_Leitura]].', '',
         '## Resultados mais próximos do objetivo', '', '| Artigo | Dado | Alvo | Métrica relatada | Força da validação (minha leitura) |', '|---|---|---|---|---|']
    for pid, dado, alvo, met, forca in K.TRILHA_TABELA:
        b.append(f'| {plink(pid)} | {dado} | {alvo} | {met} | {forca} |')
    b += ['', 'A coluna final é interpretação desta base: resume o desenho de validação lido em cada ficha (divisão, referência independente e amostragem).', '']
    for tid, titulo, perg, arts, cons, lacs in K.TRILHA:
        b += [f'## {tid[1:]}. {titulo}', '', f'*{perg}*', '']
        for pid, txt in arts:
            if pid in NAMES: b.append(f'- {plink(pid)} (relevância {TIER[pid]}) — {txt}')
        b += ['', '**Conceitos:** ' + ', '.join(clink(c) for c in cons if c in ACTIVE), '', '**Lacunas:** ' + ', '.join(f'[[{l}|{[x[1] for x in K.LACUNAS if x[0] == l][0]}]]' for l in lacs), '']
    b += ['## Proposta de arquitetura inicial (interpretação)', '', 'Não é conclusão experimental: é um ponto de partida montado a partir do que as fichas mostram.', '']
    b += [f'{i}. {resolve(t, "trilha")}' for i, t in enumerate(K.PROPOSTA, 1)]
    b += ['', 'Canvas desta trilha: `Canvas_Trilha_Objetivo.canvas` (pasta `01_Mapas`).', '', '[[00_Inicio|← Painel]]']
    write('01_Mapas/Trilha_Objetivo_Planet5m.md', '\n'.join(b) + '\n')


# ============================================================ execucao
for fid in sorted(ACTIVE): concept_note(fid)
lacunas()
rows = matriz()
monitoramento()
resultados()
trilha()
dup, rows_inv, sem_texto = anexos()
templates()
painel(rows_inv, sem_texto, dup)
exec(compile(open(os.path.join(HERE, 'kb_build3.py'), encoding='utf-8').read(), 'kb_build3.py', 'exec'))
