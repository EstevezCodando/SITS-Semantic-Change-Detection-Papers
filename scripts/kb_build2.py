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


# ============================================================ mapas (MOCs)
MOCS = [
 ('MOC_01_AquisicaoDados', 'Aquisição e seleção de dados', ['PlanetNICFI', 'PlanetScope', 'PlanetProdutos', 'Sentinel2', 'Sentinel1', 'SAR', 'Landsat', 'ImagensAereas', 'UAV', 'SpaceNet7_MUDS', 'DynamicEarthNet', 'HRSCD', 'SECOND', 'LEVIRCD', 'OSCD', 'PRODES', 'GlobalForestChange', 'MapBiomas', 'DETER'],
  ['A escolha do produto determina o que é possível detectar. Sobre a cadência do Planet NICFI: «P01|temporal resolution of the NICFI images is currently one month» e «P07|September 2020 onward, monthly»; antes disso os mosaicos eram semestrais.',
   'O dataset DynamicEarthNet usa o produto diário gap-filled («P12|Fusion Monitoring product»), que **não** equivale ao mosaico mensal convencional.',
   'Referências usadas para comparação ou rótulo: PRODES e Global Forest Change («P01|The minimum area considered for mapping deforestation is 6.25 ha»), SpaceNet 7 para edificações («P10|101 labelled sequences»).'],
  ['L02_CadenciaPlanet', 'L07_ResolucaoObjetosPequenos', 'L10_TaxonomiaTransicoes']),
 ('MOC_02_PreparoQualidade', 'Preparação e qualidade das imagens', ['MascaraNuvem', 'Corregistro', 'CorrecaoAtmosferica', 'Reamostragem', 'MosaicosCompostos', 'Normalizacao', 'PatchesTiles', 'AumentoDados', 'GDAL'],
  ['«P01|No atmospheric correction was performed»: o estudo converteu para 8 bits e confiou na variabilidade natural para generalizar.',
   'Desalinhamento é tratado explicitamente em «P10|image geo-reference errors greater than 1 pixel», que cria uma máscara de dado inutilizável (UDM).',
   'Nuvem e sombra produzem falsa mudança na pós-classificação («P05|las áreas de cambio»), motivo pelo qual a máscara de observação válida é prioridade.'],
  ['L02_CadenciaPlanet']),
 ('MOC_03_RotulagemReferencia', 'Rotulagem e referência', ['Rotulagem', 'RotulagemTemporal', 'PreAnotacaoSAM', 'SAM', 'QGIS', 'AmostraIndependente', 'AmostragemEstratificada', 'SupervisaoFraca', 'SemiAutoSupervisionado'],
  ['Protocolos observados: auto-segmentação por textura com escolha de classes («P01|k-textures algorithm, an expert only define which»), cópia sequencial com revisão cruzada («P10|Labeling took 7 months by a team of 5»), rótulo inicial manual com portões de qualidade («P12|Three quality control gates»), vetores oficiais («P18|minimum label accuracy of 80-85%») e especialistas («P19|non-change masks»).',
   'Pré-anotação com SAM no QGIS: «P165|Annotations were performed in rounds» e simulação de prompts; limites discutidos em «L05_RotulosTemporais» e «L08_FerramentasSemAvaliacao».'],
  ['L05_RotulosTemporais', 'L08_FerramentasSemAvaliacao']),
 ('MOC_04_EngenhariaAtributos', 'Engenharia de atributos', ['Textura', 'IndicesEspectrais', 'OBIA', 'SegmentacaoObjetos', 'Normalizacao'],
  ['Textura e objetos compensam o espectro limitado do Planet: «P07|window size for GLCM was set at 2 pixels» e janela de 5 px para o PlanetScope; o ganho de OA vem do enfoque por objetos.',
   'Em «P05» a inclusão do NDVI não trouxe ganho: «P05|no hay un mayor aporte».'],
  ['L07_ResolucaoObjetosPequenos']),
 ('MOC_05_MachineLearning', 'Machine Learning (algoritmos sobre atributos)', ['RandomForest', 'XGBoost', 'SVM', 'OBIA', 'TransferLearning', 'GoogleEarthEngine'],
  ['Random Forest com pixels e com objetos em GEE: «P07|Using only the PL dataset with a typical RF PB approach produced the worse overall accuracy»; a abordagem por objetos elevou o resultado.',
   'Não há, nos artigos com texto integral aqui lidos, comparação direta entre XGBoost e Random Forest em Planet; ver o catálogo antigo para os estudos de XGBoost sem texto.'],
  ['L06_MetricasIncomparaveis']),
 ('MOC_06_DeepLearning', 'Deep Learning (arquiteturas e estratégias)', ['CNN', 'UNet', 'RedeSiamesa', 'Transformer', 'Mamba', 'UTAE', 'LSTM', 'ModeloFundacional', 'SAM', 'YOLO', 'TransferLearning', 'SemiAutoSupervisionado', 'SupervisaoFraca', 'SuperResolucao', 'PyTorch', 'TensorFlow'],
  ['A U-Net é a base dos estudos Planet lidos («P01», «P05», «P10»). Arquiteturas temporais (U-TAE) são comparadas em «P12» e estendidas em «P13».',
   'Os resultados de modelos fundacionais devem ser lidos com cautela: ver o lembrete de comparabilidade em «L06_MetricasIncomparaveis».'],
  ['L04_DomainShift', 'L06_MetricasIncomparaveis']),
 ('MOC_07_MudancaSeries', 'Detecção de mudanças e séries temporais', ['Deteccao_Mudanca', 'MudancaSemantica', 'SITS', 'PosClassificacao', 'UTAE', 'RedeSiamesa', 'MetricasMudancaSemantica', 'DynamicEarthNet', 'SpaceNet7_MUDS', 'HRSCD', 'SECOND'],
  ['Comparação direta entre as duas famílias na mesma série PlanetScope: «P05|el esquema número 2 fue el más apropiado» (mudança direta supera pós-classificação, com ressalvas).',
   'Quatro estratégias de mudança semântica em «P18»; a estratégia sequencial teve o maior kappa de mudança no HRSCD. Em séries diárias, nem sempre mais datas ajudam: «P12|using weekly samples is optimal for the considered baselines».',
   'Segmentar uma imagem isolada **não** é evidência de detecção temporal; as notas só tratam como mudança o que compara datas.'],
  ['L03_MudancaRara', 'L04_DomainShift', 'L10_TaxonomiaTransicoes']),
 ('MOC_08_ValidacaoIncerteza', 'Validação e incerteza', ['DivisaoTreinoTeste', 'DivisaoEspacialBlocos', 'DivisaoTemporal', 'Generalizacao', 'Desbalanceamento', 'AmostragemEstratificada', 'AmostraIndependente', 'ValidacaoCruzada', 'EstimativaArea', 'F1', 'IoU', 'PrecisaoRecall', 'AcuraciaGlobal', 'Kappa', 'MetricasMudancaSemantica'],
  ['Desenho de referência: três regimes de validação em «P13|average relative drop of the mIoU», que mostram a queda sob shift espacial.',
   'Acurácia global e kappa enganam quando quase tudo não muda («P19|dominant non-change pixels would cause unreasonable scores»; «P18|99.232% of all pixels are labelled as no change»).',
   'Área em hectares deve vir de estimativa amostral com intervalo de confiança (ver «P46», leitura parcial).'],
  ['L03_MudancaRara', 'L04_DomainShift', 'L06_MetricasIncomparaveis']),
 ('MOC_09_ResultadosInterpretacao', 'Resultados e interpretação', [],
  ['Esta página liga as sínteses comparativas. **Não** classifique modelos como superiores comparando métricas de bases, classes, resoluções e desenhos diferentes.',
   'Matriz: [[Matriz_Comparativa]] · Achados: [[Achados_Relevantes]] · Por tema: [[Sintese_Mudanca_Semantica]], [[Sintese_Floresta_Desmatamento]], [[Sintese_Edificacoes_Vias]] · Sínteses: [[Sintese_Rotulagem]], [[Sintese_Metricas]], [[Sintese_Particoes]], [[Sintese_Receitas]], [[Sintese_Planet]], [[Sintese_QGIS_GeoAI]], [[Sintese_Decisoes]].'],
  ['L06_MetricasIncomparaveis']),
 ('MOC_10_MonitoramentoOperacao', 'Monitoramento contínuo e operação', ['QuaseTempoReal', 'Alertas', 'RevisaoHumana', 'PersistenciaConfirmacao', 'FalsosAlertas', 'SistemaOperacional', 'QGIS', 'DETER'],
  ['A maioria dos estudos lidos é retrospectiva; veja a tabela de evidências em [[Estudos_Retrospectivos_vs_Operacionais]].',
   'Ferramentas de QGIS/GeoAI servem à revisão e à pré-anotação, mas **não** oferecem detecção temporal de mudanças nos painéis descritos: «P155|Seamless QGIS integration via a dedicated GeoAI plugin».'],
  ['L01_ValidacaoOperacional', 'L08_FerramentasSemAvaliacao', 'L09_ReprodutibilidadeCodigo']),
]
_EXTRA = {'MOC_03_RotulagemReferencia': ['AprendizadoAtivo'], 'MOC_07_MudancaSeries': ['PosProcessamentoTemporal'], 'MOC_08_ValidacaoIncerteza': ['AmostragemEstratificada', 'ReferenciaVisual'], 'MOC_10_MonitoramentoOperacao': ['PosProcessamentoTemporal']}
for _m in MOCS: _m[2].extend(x for x in _EXTRA.get(_m[0], []) if x not in _m[2])
MOC_OF = collections.defaultdict(list)
for mid, mt, cons, prose, lacs in MOCS:
    for f in cons: MOC_OF[f].append((mid, mt))

def moc_note(mid, mt, cons, prose, lacs):
    fm = ['---', 'tipo: mapa', f'titulo: {yq(mt)}', f'n_conceitos: {len([c for c in cons if c in ACTIVE])}', 'tags: [mapa]', '---', '']
    b = [f'# {mt}', '', '> Mapa de conteúdo: aponta para conceitos (que carregam a relação com os artigos) e para as lacunas. Não liga diretamente todos os artigos.', '', '## Síntese com evidências', '']
    for ptxt in prose: b += [f'- {resolve(re.sub(r"«(L\d+_[A-Za-z]+)»", r"[[\1]]", ptxt), mid)}']
    b += ['', '## Conceitos deste mapa', '']
    by = collections.defaultdict(list)
    for f in cons:
        if f in ACTIVE: by[concepts[f]['tipo']].append(f)
    for tipo, fs in by.items():
        b.append(f'**{tipo.capitalize()}**')
        for f in fs: b.append(f'- [[{f}|{concepts[f]["titulo"]}]] — {len(concepts[f]["sup"])} artigos')
        b.append('')
    if lacs:
        b += ['## Lacunas relacionadas', ''] + [f'- [[{l}|{[x[1] for x in K.LACUNAS if x[0] == l][0]}]]' for l in lacs]
    b += ['', '[[00_Inicio|← Painel]]']
    write(f'01_Mapas/{mid}.md', '\n'.join(fm + b) + '\n')


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
         'Linhas “curadas” vêm das fichas de leitura; linhas “automáticas” vêm de busca por padrões no texto convertido e devem ser conferidas. Versão completa em `Matriz_Comparativa.csv` nesta pasta.', '',
         '## Estudos lidos (curada pela leitura)', '', '| Artigo | tarefa | dados | resolução | preparo | método | estratégia temporal | validação | métricas | limitações | código disponível |', '|---|---|---|---|---|---|---|---|---|---|---|']
    for d in rows:
        if d['origem'].startswith('curada'):
            b.append(f'| {plink(d["pid"])} | ' + ' | '.join(d[c].replace('|', '/') for c in COLS) + ' |')
    b += ['', '## Demais estudos com texto convertido (extração automática, verificar)', '', '| Artigo | tarefa | dados | resolução | preparo | método | estratégia temporal | validação | métricas | limitações | código disponível |', '|---|---|---|---|---|---|---|---|---|---|---|']
    for d in rows:
        if d['origem'].startswith('autom'):
            b.append(f'| {plink(d["pid"])} | ' + ' | '.join(d[c].replace('|', '/')[:150] for c in COLS) + ' |')
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
    synth('Sintese_Mudanca_Semantica', 'Síntese — mudança semântica', 'Estudos que tratam o de–para de classes (HRSCD, SECOND, DynamicEarthNet, SITS-SCD).',
          ['«P18» compara quatro estratégias; a de treino sequencial teve o maior kappa de mudança (25,49) no HRSCD.', '«P19» propõe ASN e a métrica SeK; ganho de +2,1 mIoU e +2,3 SeK sobre HRSCD.str4 em SECOND.',
           '«P12» e «P13»: melhor SCS ainda baixo (BC <23%) e forte queda sob shift espacial.', 'Comparar métricas entre HRSCD (kappa), SECOND (SeK) e DynamicEarthNet (SCS) **não é válido**.'], ['MudancaSemantica', 'SITS', 'MetricasMudancaSemantica', 'HRSCD', 'SECOND', 'DynamicEarthNet'])
    synth('Sintese_Floresta_Desmatamento', 'Síntese — floresta e desmatamento com Planet', 'Mapeamento de cobertura arbórea e perda com mosaicos NICFI e PlanetScope.',
          ['«P01» classifica a floresta em cada data com U-Net e deriva o desmatamento por diferença; não vê mudança entre datas e pode perder degradação.', '«P02» (leitura parcial) trata a degradação em separado.', '«P07» classifica cobertura estática; não valida transições.',
           '«P05» compara pós-classificação e mudança direta em mineração.'], ['Desmatamento', 'DegradacaoFlorestal', 'PlanetNICFI', 'PRODES', 'GlobalForestChange', 'UNet'])
    synth('Sintese_Edificacoes_Vias', 'Síntese — edificações e vias', 'Estudos de construção e infraestrutura viária em escalas próximas de 3–5 m.',
          ['«P10» é a referência para construção em mosaicos mensais de ~4 m (F1 0,45; mudança 0,06–0,07).', '«P13» mostra desempenho próximo do acaso em SCS no MUDS.', 'Para vias, os estudos com texto convertido devem ser consultados na tabela de [[Matriz_Comparativa]] (extração automática).'],
          ['Edificacoes', 'Vias', 'SpaceNet7_MUDS', 'SuperResolucao'])
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
    rows = []
    for pid in PIDS:
        r = cat[pid]; v = kb.get(pid)
        obs = []
        if v and v['paginas_pouco_texto']: obs.append(f'páginas com pouco texto (OCR?): {v["paginas_pouco_texto"]}')
        if v and v['avisos']: obs.append(f'{v["avisos"]} avisos de conversão')
        if not v: obs.append('sem texto convertido (leitura por resumo, documentação ou HTML)')
        rows.append(dict(id=pid, nota=NAMES[pid], titulo=r['title'], ano=year_of(r), doi=r.get('doi') or 'não informado', pdf=('coleta/' + r['pdf_file']) if r.get('pdf_file') else 'não informado',
                         markdown=('output/pdf/' + v['dir'] + '/document.md') if v else 'não informado', paginas=v['pages'] if v else '', figuras=v['n_figs'] if v else '', rasters=v['n_rasters'] if v else '',
                         sha256=v['sha256'] if v else '', status=STATUS[pid], obs='; '.join(obs)))
    sem_texto = [r for r in cat.values() if r['id'] not in PIDS]
    with open(f'{KB}/90_Anexos/Inventario_Arquivos.csv', 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, delimiter=';'); w.writerow(['id', 'nota', 'titulo', 'ano', 'doi', 'pdf', 'markdown', 'paginas', 'figuras', 'rasters', 'sha256', 'status_leitura', 'observacoes'])
        for d in rows: w.writerow([d[k] for k in ['id', 'nota', 'titulo', 'ano', 'doi', 'pdf', 'markdown', 'paginas', 'figuras', 'rasters', 'sha256', 'status', 'obs']])
        for r in sem_texto: w.writerow([r['id'], '', r['title'], year_of(r), r.get('doi') or 'não informado', '', '', '', '', '', '', 'sem texto (fora da base de notas)', 'PDF não obtido em coleta/ (acesso restrito ou bloqueado)'])
    fm = ['---', 'tipo: anexo', 'titulo: "Inventário de arquivos"', 'tags: [anexo, inventario]', '---', '']
    b = ['# Inventário de arquivos', '', f'Catalogado em {TODAY}. **{len(PIDS)}** documentos com nota principal; **{len(sem_texto)}** registros do catálogo sem texto integral (listados no CSV). '
         'Os originais (PDF) ficam em `coleta/` e a conversão em `output/pdf/`; **nada foi movido ou alterado**.', '',
         f'- Documentos convertidos: {len(kb)} (1.639 páginas no lote); falhas de conversão: 0 (relatório `output/pdf/report.json`).',
         f'- Lidos em profundidade: {sum(1 for p in PIDS if STATUS[p] == "lido (profundo)")}; leitura parcial: {sum(1 for p in PIDS if STATUS[p] == "lido (parcial)")}; extração automática: {sum(1 for p in PIDS if STATUS[p].startswith("extra"))}.',
         '- Tipos de documento: artigo completo, artigo curto (≤4 páginas, a verificar) e documentação de software. Nenhum PDF ilegível: todas as páginas tinham texto extraível; páginas com <40 caracteres são sinalizadas para OCR quando existirem.', '',
         '| Nota | Título | Ano | DOI | Páginas | Status | Observações |', '|---|---|---|---|---:|---|---|']
    for d in rows:
        b.append(f'| {plink(d["id"])} | {d["titulo"][:70].replace("|", "/")} | {d["ano"]} | {d["doi"]} | {d["paginas"] or "—"} | {d["status"]} | {d["obs"] or "—"} |')
    b += ['', '## Registros sem texto integral', '', '| ID | Título | Ano | DOI |', '|---|---|---:|---|']
    for r in sem_texto: b.append(f'| {r["id"]} | {r["title"][:80].replace("|", "/")} | {year_of(r)} | {r.get("doi") or "não informado"} |')
    b += ['', 'Planilha completa com hashes: `Inventario_Arquivos.csv`.', '', '[[00_Inicio|← Painel]]']
    write('90_Anexos/Inventario_Arquivos.md', '\n'.join(fm + b) + '\n')
    # duplicatas e versoes
    dup = []
    items = list(cat.values())
    dois = collections.defaultdict(list)
    for r in items:
        if r.get('doi'): dois[r['doi'].lower()].append(r['id'])
    for d, ids in dois.items():
        if len(ids) > 1: dup.append(('DOI repetido', d, ids))
    for i, a in enumerate(items):
        for b_ in items[i + 1:]:
            if difflib.SequenceMatcher(None, norm(a['title']), norm(b_['title'])).ratio() >= 0.92 and a.get('doi') != b_.get('doi'):
                dup.append(('títulos muito semelhantes (possível preprint/publicação)', a['title'][:60], [a['id'], b_['id']]))
    sha = collections.defaultdict(list)
    for pid, v in kb.items(): sha[v['sha256']].append(pid)
    for h, ids in sha.items():
        if len(ids) > 1: dup.append(('PDF idêntico (SHA-256)', h[:12], ids))
    b = ['# Duplicatas e versões', '', 'Verificação automática por DOI, similaridade de título (≥0,92) e hash dos PDFs.', '']
    b += ([f'- **{k}:** {d} → {", ".join(ids)}' for k, d, ids in dup] or ['- Nenhuma duplicata encontrada pelos três critérios.'])
    b += ['', 'Observação: o catálogo já descarta, na origem, duplicatas entre preprint e publicação (ex.: ChangeMamba, RB-SCD), mantendo uma entrada.', '', '[[00_Inicio|← Painel]]']
    write('90_Anexos/Duplicatas_e_Versoes.md', '\n'.join(['---', 'tipo: anexo', 'titulo: "Duplicatas e versões"', 'tags: [anexo]', '---', ''] + b) + '\n')
    # documento original
    orig = open(f'{ROOT}/fonte_original/REVISAO_ORIGINAL.md', encoding='utf-8').read()
    write('90_Anexos/Documento_Original_Revisao.md', '---\ntipo: anexo\ntitulo: "Documento original da revisão"\ntags: [anexo, original]\n---\n\n> Cópia inalterada do documento que originou a coleta (fonte: `fonte_original/REVISAO_ORIGINAL.md`).\n\n' + orig + '\n')
    # conversao e figuras
    write('90_Anexos/Conversao_Markdown.md', '---\ntipo: anexo\ntitulo: "Conversão dos PDFs em Markdown"\ntags: [anexo]\n---\n\n# Conversão dos PDFs em Markdown\n\n'
          'Cada PDF de `coleta/` foi convertido em `output/pdf/<documento>/` com `document.md` (texto por página, com marcadores `<!-- page: N -->`), `text.md` (texto direto), `images/` (recortes de figuras), `raster/` (imagens incorporadas), `pages.json`, `rasters.json` e `manifest.json` (hash SHA-256 do original). '
          'Esta base usa os marcadores de página para citar **(p. N)**. Fórmulas, tabelas complexas e ordem de leitura em duas colunas podem exigir conferência no PDF. Instruções: `scripts/PDF_PIPELINE.md`.\n\n'
          '[[Inventario_Arquivos|Inventário]] · [[Indice_Figuras|Figuras selecionadas]] · [[00_Inicio|← Painel]]\n')
    b = ['---', 'tipo: anexo', 'titulo: "Figuras selecionadas"', 'tags: [anexo, figuras]', '---', '', '# Figuras selecionadas', '',
         'Recortes copiados de `output/pdf/*/images/` para esta base, escolhidos pela legenda (arquitetura/visão geral/resultados) para os artigos lidos em profundidade. As demais figuras ficam em `output/pdf/`.', '']
    for pid, figs in FIGS.items():
        b += [f'## {plink(pid)}', '']
        for f in figs: b += [f'- `{f["file"]}` — {f["cap"]} (p. {f["p"]})']
        b.append('')
    write('90_Anexos/Indice_Figuras.md', '\n'.join(b) + '\n')
    return dup, rows, sem_texto


# ============================================================ painel
def painel(rows_inv, sem_texto, dup):
    n_prof = sum(1 for p in PIDS if STATUS[p] == 'lido (profundo)'); n_par = sum(1 for p in PIDS if STATUS[p] == 'lido (parcial)'); n_aut = sum(1 for p in PIDS if STATUS[p].startswith('extra'))
    fm = ['---', 'tipo: painel', 'titulo: "Painel — mudanças da cobertura terrestre com séries Planet"', 'tags: [painel]', '---', '']
    b = ['# Painel — mudanças da cobertura terrestre com séries Planet', '',
         f'Base de conhecimento construída em {TODAY} a partir de **{len(PIDS)} artigos** com texto convertido em Markdown. **Autor da coleta:** Jean Michael Estevez Alvarez.', '',
         f'**Situação de leitura:** {n_prof} lidos em profundidade · {n_par} em leitura parcial · {n_aut} por extração automática (não lidos por mim) · {len(sem_texto)} registros do catálogo sem texto integral.', '',
         '## Comece aqui', '', '- [[Trilha_Objetivo_Planet5m]] — o fluxo do objetivo (Planet de ~5 m: construção, supressão de vegetação, vias) ligado aos artigos de maior relevância.', '',
         '## Mapas principais', ''] + [f'- [[{m[0]}|{m[1]}]]' for m in MOCS] + ['',
         '## Comparação, lacunas e operação', '', '- [[Matriz_Comparativa]] · [[Achados_Relevantes]] · [[Estudos_Retrospectivos_vs_Operacionais]]', '- [[00_Sintese_Lacunas]]', '',
         '## Navegação e verificação', '', '- [[Guia_Navegacao]] · [[Guia_Grafo]] · [[Pendencias_Leitura]] · [[Verificacao]]', '- Anexos: [[Inventario_Arquivos]] · [[Duplicatas_e_Versoes]] · [[Conversao_Markdown]] · [[Indice_Figuras]] · [[Documento_Original_Revisao]]', '',
         '## Canvas', '', '- `Mapa_Metodologico.canvas` (visão geral) e canvas temáticos na pasta `01_Mapas` (ver [[Guia_Navegacao]]).']
    write('00_Painel/00_Inicio.md', '\n'.join(fm + b) + '\n')
    nav = ['---', 'tipo: painel', 'titulo: "Guia de navegação"', 'tags: [painel]', '---', '', '# Guia de navegação', '',
           '1. Comece em [[00_Inicio]] e escolha um mapa em `01_Mapas`.', '2. Os mapas apontam para **conceitos** (notas de dado, preparo, método, validação e monitoramento). Cada conceito traz uma tabela com os artigos que o utilizam, a relação e as páginas.',
           '3. Cada artigo (`02_Artigos`) tem as mesmas 12 seções e separa *evidência do artigo* de *interpretação*.', '4. Para comparar estudos use [[Matriz_Comparativa]], sem classificar superioridade entre bases diferentes.',
           '5. Para investigar uma nota, abra o **grafo local** (profundidade 1 ou 2). Veja [[Guia_Grafo]].', '6. Os Canvas mostram o fluxo Dados → Preparação → Métodos → Validação → Resultados → Monitoramento.', '',
           '## Convenções', '', '- `status_leitura`: *lido (profundo)*, *lido (parcial)* ou *extraído automaticamente (não lido)*.', '- “não informado”: o texto convertido não trouxe a informação (ou a busca automática não a encontrou).',
           '- Páginas (p. N) são as do PDF; § indica seção. Itens “detectado automaticamente” devem ser conferidos na página.', '- Novos artigos: copie `99_Templates/Template_Artigo.md`.', '', '[[00_Inicio|← Painel]]']
    write('00_Painel/Guia_Navegacao.md', '\n'.join(nav) + '\n')
    p = ['---', 'tipo: painel', 'titulo: "Pendências de leitura"', 'tags: [painel, pendencias]', '---', '', '# Pendências de leitura', '',
         'Registro explícito do que foi lido e do que falta. Prioridade: artigos com extração automática que aparecem em vários conceitos.', '', '## Lidos em profundidade', '']
    p += [f'- {plink(x)}' for x in PIDS if STATUS[x] == 'lido (profundo)']
    p += ['', '## Leitura parcial (falta texto integral ou verificação)', ''] + [f'- {plink(x)} — ver seção 9 da nota' for x in PIDS if STATUS[x] == 'lido (parcial)']
    cnt = {x: len(paper_concepts[x]) for x in PIDS if STATUS[x].startswith('extra')}
    p += ['', '## Extração automática (não lidos) — ordenados por número de conceitos ligados', '']
    p += [f'- {plink(x)} — {cnt[x]} conceitos' for x in sorted(cnt, key=lambda y: -cnt[y])]
    rk = f'{DATA}/ranking_relevancia.json'
    if os.path.exists(rk):
        R = json.load(open(rk, encoding='utf-8'))
        nr = [r for r in R if r['id'] in NAMES and STATUS[r['id']].startswith('extra')][:25]
        p += ['', '## Próximos a ler: ranking de relevância automática (não lidos)', '',
              'Pontuação por contagem de termos no texto convertido (Planet/NICFI, resolução de 3–5 m, mudança, desmatamento, edificações e vias, séries, métodos e métricas; peso maior no início do artigo). **É triagem, não avaliação**: um artigo de pontuação alta pode ser irrelevante.', '',
              '| Artigo | Pontuação | Menções a Planet | Menções a mudança | Menções a desmatamento |', '|---|---:|---:|---:|---:|']
        p += [f'| {plink(r["id"])} | {r["score"]} | {r["planet"]} | {r["mud"]} | {r["alvo"]} |' for r in nr]
    p += ['', f'## Sem texto integral ({len(sem_texto)})', '', 'Veja [[Inventario_Arquivos]]. Obter o PDF aberto ou texto alternativo antes de qualquer nota.', '', '[[00_Inicio|← Painel]]']
    write('00_Painel/Pendencias_Leitura.md', '\n'.join(p) + '\n')


# ============================================================ templates
def templates():
    write('99_Templates/Template_Artigo.md', '---\ntipo: artigo\nid_origem: \ntitulo: ""\nano: \nautores: []\ndoi: "não informado"\narquivo_fonte: ""\nmarkdown_fonte: ""\npaginas: \ntipo_documento: ""\nstatus_leitura: "não lido"\ntarefas: []\nsensores: []\nconjuntos_dados: []\nmetodos: []\npreparo: []\nvalidacao: []\nferramentas: []\ntags: [artigo]\n---\n\n# Autor Ano — Título\n\n'
          '> Evidência do artigo (com página) vs. Interpretação (rotulada). Use “não informado” quando faltar.\n\n## 1. Referência bibliográfica e acesso ao original\n\n## 2. Problema investigado e contribuição principal\n\n## 3. Área de estudo e período analisado\n\n## 4. Dados: sensores, bandas, resoluções, quantidade de imagens e referência de campo\n\n## 5. Preparação\n\n## 6. Análise\n\n## 7. Validação\n\n## 8. Resultados\n\n## 9. Limitações e condições de aplicabilidade\n\n## 10. Reprodutibilidade\n\n## 11. Aplicabilidade ao monitoramento contínuo\n\n## 12. Relações justificadas com outras notas\n\n- utiliza método: `[[Conceito]]` — (p. )\n')
    write('99_Templates/Template_Conceito.md', '---\ntipo: conceito\nsubtipo: ""\ntitulo: ""\naliases: []\nn_artigos: 0\ntags: [conceito]\n---\n\n# Título\n\n## Definição\n\n## Finalidade\n\n## Entradas\n\n## Saídas\n\n## Pressupostos\n\n## Limitações\n\n## Evidência nos artigos lidos\n\n| Artigo | Relação | Ocorrências | Páginas | Status de leitura |\n|---|---|---:|---|---|\n')
    write('99_Templates/Template_Lacuna.md', '---\ntipo: lacuna\ntitulo: ""\ntema: ""\nstatus: aberta\ntags: [lacuna]\n---\n\n# Título\n\n## Descrição\n\n## Evidências nos artigos\n\n- `[[Artigo]]` (p. )\n\n## O que isto afeta (método, dado ou resultado)\n\n## Oportunidade (interpretação)\n')
    write('99_Templates/Template_Mapa.md', '---\ntipo: mapa\ntitulo: ""\ntags: [mapa]\n---\n\n# Título\n\n## Síntese com evidências\n\n## Conceitos deste mapa\n\n## Lacunas relacionadas\n')
    write('99_Templates/Template_Resultado.md', '---\ntipo: resultado\ntitulo: ""\ntags: [resultado]\n---\n\n# Título\n\n> Valores valem dentro do estudo citado; não comparar entre bases diferentes.\n\n## Achado\n\n**Evidência:** `[[Artigo]]` (p. )\n')


# ============================================================ trilha para o objetivo
def trilha():
    cnt = collections.Counter(TIER[p] for p in PIDS)
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
for m in MOCS: moc_note(*m)
lacunas()
rows = matriz()
monitoramento()
resultados()
trilha()
dup, rows_inv, sem_texto = anexos()
templates()
painel(rows_inv, sem_texto, dup)
exec(compile(open(os.path.join(HERE, 'kb_build3.py'), encoding='utf-8').read(), 'kb_build3.py', 'exec'))
