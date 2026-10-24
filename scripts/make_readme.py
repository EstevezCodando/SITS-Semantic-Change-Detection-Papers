"""Etapa 4: gera README.md (padrao do repositorio ML-for-Location-and-Routing-Optimization-Papers)
e coleta/_manifesto.csv a partir de dados/catalog.json, dados/tools.json e do documento original.
Uso: python -I make_readme.py <raiz do projeto>
"""
import re, sys, os, json, csv
sys.stdout.reconfigure(encoding='utf-8')
root = sys.argv[1]
cat = json.load(open(f'{root}/dados/catalog.json', encoding='utf-8'))
tools = json.load(open(f'{root}/dados/tools.json', encoding='utf-8'))
orig = open(f'{root}/fonte_original/REVISAO_ORIGINAL.md', encoding='utf-8').read().split('\n')
links1 = json.load(open(f'{root}/dados/links_original.json', encoding='utf-8'))
DATA = '24/10/2026'

# --- reparos manuais dos repositorios cuja checagem automatica bateu no limite da API (existencia confirmada por busca)
tools['repos']['IAMAP (plugin QGIS)'] = {'repo': 'umr-amap/iamap', 'ok': True, 'stars': 4, 'license': '—', 'pushed': '—', 'archived': False}
tools['repos']['MOLUSCE (plugin QGIS)'] = {'repo': 'nextgis/qgis_molusce', 'ok': True, 'stars': 59, 'license': '—', 'pushed': '—', 'archived': False}

SEC = {
    'A': 'Planet: aplicações diretas', 'B': 'Séries temporais, edificações e transições semânticas',
    'C': 'Detectores profundos e modelos fundacionais', 'D': 'Vias, redes viárias e informação cartográfica prévia',
    'E': 'Métodos temporais clássicos e avaliação científica', 'F': 'XGBoost, LightGBM e classificação baseada em atributos',
    'G': 'Pré-catalogação com SAM, YOLO e representações fundacionais', 'H': 'Engenharia de dados: do arquivo ao acervo analítico',
    'I': 'Ciência de dados: amostragem, curadoria, qualidade e representação',
    'J': 'Planet: dados, qualidade, radiometria e fusão', 'K': 'Planet: aplicações adicionais (florestas, mineração, vias, edificações)',
    'L': 'Desmatamento, degradação e sistemas de alerta', 'M': 'Detecção de mudanças: métodos, datasets e revisões adicionais',
    'N': 'GeoAI e QGIS: pacotes, plugins e fluxos de trabalho',
}
SEC_DESC = {
    'A': 'Estudos que usam Planet/PlanetScope/NICFI diretamente. Ponto de partida para supressão vegetal, degradação e mudanças de cobertura.',
    'B': 'Datasets e métodos para séries temporais e mudança semântica (SpaceNet 7, DynamicEarthNet, TSSCD, HRSCD, SECOND).',
    'C': 'Baselines siameses, transformers, Mamba e modelos fundacionais para detecção de mudanças.',
    'D': 'Mudança em vias e pontes, extração de rede viária e uso de mapas anteriores como informação auxiliar.',
    'E': 'BFAST, CCDC, LandTrendr e as práticas de estimativa de área e avaliação de acurácia.',
    'F': 'Classificadores sobre vetores de atributos (bandas, índices, textura, geometria, contexto, embeddings).',
    'G': 'SAM, Grounded SAM, YOLO e embeddings para gerar um catálogo preliminar de objetos. Segmentar, classificar e ligar identidades no tempo são tarefas distintas.',
    'H': 'Cubos de dados, STAC e processamento sob demanda: grade, tempo, qualidade e rastreabilidade corretos.',
    'I': 'Validação espacial/temporal, curadoria, aprendizado ativo e controle de qualidade.',
    'J': 'Produtos Planet, disponibilidade temporal, nuvem/sombra, reflectância e fusão com Sentinel-2.',
    'K': 'Estudos aplicados adicionais com Planet e CubeSats em florestas, mineração, vias e edificações.',
    'L': 'Deep learning para desmatamento (PRODES/DETER), alertas operacionais e mineração ilegal.',
    'M': 'Revisões, datasets e arquiteturas adicionais (SAM, modelos fundacionais, supervisão fraca, séries de satélite).',
    'N': 'Pacote GeoAI (opengeos), plugins QGIS de deep learning (Deepness, IAMAP, Geo-SAM), MOLUSCE e revisões de GeoAI.',
}
ORDER = list('ABCDEFGHIJKLMN')


def anchor(t):
    return re.sub(r'\s', '-', re.sub(r'[^\w\s-]', '', t.lower()))


def esc(s): return (s or '').replace('|', '\\|').replace('\n', ' ')
def short_venue(r):
    v = (r.get('venue') or '').replace('(Cornell University)', '').strip()
    if r.get('doi', '').lower().startswith('10.48550'): return 'arXiv'
    return v[:40] + ('…' if len(v) > 40 else '')
def pub_link(r):
    d = r.get('doi') or ''
    if r['origin'] == 'original':
        us = [u for u in r.get('fonte_urls', []) if u.startswith('http')]
        u = us[0] if us else ('https://doi.org/' + d if d else '')
    else:
        u = 'https://doi.org/' + d if d else ''
    return u
def year(r): return (r.get('year_doc') if r['origin'] == 'original' and r.get('year_doc') else r.get('oa_year')) or ''
def mark(r): return '✓' if r.get('checked') else '○'
def author1(r):
    a = r.get('authors') or []
    if not a: return ''
    last = a[0].split()[-1]
    return f'{last} et al.' if len(a) > 2 else (f'{last} e {a[1].split()[-1]}' if len(a) == 2 else last)
def pdf_cell(r):
    return f"[PDF](coleta/{r['pdf_file']})" if r.get('pdf_file') else '—'
def code_cell(r):
    c = [u for u in r.get('code', []) if u.startswith('http')]
    if not c: return '—'
    out = []
    for u in c[:2]:
        host = re.sub(r'https?://(www\.)?', '', u).split('/')
        out.append(f'[{host[0].split(".")[0]}/{host[-1] if len(host) > 2 else host[-1]}]({u})' if 'github' in u else f'[link]({u})')
    return ' '.join(out)


def sect(heading_regex, end_regex):
    s = next(i for i, l in enumerate(orig) if re.match(heading_regex, l))
    e = next((i for i in range(s + 1, len(orig)) if re.match(end_regex, orig[i])), len(orig))
    body = orig[s:e]
    return '\n'.join(('#' + l if l.startswith('#') else l) for l in body).rstrip()


ID = {r['doi'].lower(): r['id'] for r in cat if r.get('doi')}
def pid(doi): return ID.get(doi.lower(), '?')


by_sec = {k: [r for r in cat if r['section'] == k] for k in SEC}
by_sec['R'] = [r for r in cat if r['section'] == 'R']
reviews = [r for r in cat if r['section'] == 'R' or r['kind'] == 'Revisão']
total = len(cat)
nchk = sum(1 for r in cat if r.get('checked'))
npdf = sum(1 for r in cat if r.get('pdf_file'))
norig = sum(1 for r in cat if r['origin'] == 'original')
nlink_ok = sum(1 for x in links1 if x[1] in (200, 301, 302, 202, 203))
nlink_blk = sum(1 for x in links1 if x[1] == 403)
nlink_other = len(links1) - nlink_ok - nlink_blk

L = []
w = L.append
w('# Detecção e Classificação de Mudanças da Cobertura Terrestre com Séries Planet — Coletânea de Artigos\n')
w('**Idioma:** Português (Brasil)\n')
w(f'Lista curada de **{total} trabalhos** sobre detecção semântica de mudanças em séries temporais de imagens de satélite (SITS-SCD), orientada a **mosaicos mensais Planet de 3–5 m (2020–2026)**: supressão vegetal, novas construções, abertura de vias e outras transições de cobertura. Cada entrada informa **onde**, **entre quais datas** e **de qual cobertura para qual cobertura** o estudo trata, com comentário de método, aplicação e limite. A coletânea inclui ainda artigos sobre **GeoAI e plugins de QGIS**, bibliotecas verificadas e um guia metodológico para o experimento do projeto.\n')
w('> Os resultados citados são **os relatados pelos autores**, não reproduções. Ao comentar um artigo, as limitações indicam o que **não** se pode concluir sobre mosaicos Planet de 3–5 m. Esta é uma busca dirigida, **não** uma revisão sistemática PRISMA nem um censo da literatura. Os artigos não foram lidos integralmente.\n')
w('## Sobre esta coleta\n')
w('**Autor da coleta:** Jean Michael Estevez Alvarez\n')
w(f'- **Data da coleta e verificação:** {DATA}.')
w('- **Fontes:** OpenAlex, Crossref, arXiv, Semantic Scholar, páginas de editoras, GitHub e PyPI. Sem consulta autenticada a Scopus ou Web of Science.')
w(f'- **Origem dos registros:** {norig} do documento de revisão original (P01–P80) e {total - norig} acrescentados nesta coleta (P81 em diante).')
w(f'- **Pasta `coleta/`:** {npdf} PDFs de acesso aberto, com nomes `ID_Autor-Ano_titulo.pdf`. Veja também [`coleta/_manifesto.csv`](coleta/_manifesto.csv). Os demais são de acesso restrito, sem versão aberta localizada ou bloqueados contra download automático (parte do MDPI e do ScienceDirect, onde o 403 persistiu mesmo com o fallback); use o link da publicação na tabela.')
w('- **Scripts** em [`scripts/`](scripts/) reproduzem a coleta: `build_catalog.py`, `download_pdfs.py`, `download_fallback.py`, `check_tools.py`, `make_readme.py`. Quando uma editora bloqueou o download simples, o fallback usou o `curl_cffi` (a mesma base do Scrapling de `C:\\Desenvolvimento\\WebScrapping`).')
w('- **Direitos autorais:** os PDFs são de acesso aberto (arXiv, MDPI, Frontiers e repositórios institucionais), baixados para estudo pessoal. Respeite as licenças de cada artigo ao redistribuir.\n')
w(f'**Legenda:** ✓ = título, ano e DOI/identificador conferidos em base bibliográfica em {DATA}; ○ = não localizado automaticamente (conferir manualmente). A marca não atesta a qualidade metodológica do estudo. Em PDF, `—` indica que não há cópia aberta em `coleta/`.\n')

w('## Conteúdo\n')
w('- [Resultado principal e ordem de leitura](#resultado-principal-e-ordem-de-leitura)')
w('- [Revisões](#revisões)')
w('- [Artigos e códigos](#artigos-e-códigos)')
for k in ORDER: w(f'  - [{k}. {SEC[k]}](#{anchor(k + ". " + SEC[k])})')
w('- [GeoAI e QGIS: artigos que citam o GeoAI](#geoai-e-qgis-artigos-que-citam-o-geoai)')
w('- [Comentário por artigo](#comentário-por-artigo)')
w('- [Bibliotecas e ferramentas verificadas](#bibliotecas-e-ferramentas-verificadas)')
w('- [Verificação dos links](#verificação-dos-links)')
w('- [Tendências 2024–2026](#tendências-20242026)')
w('- [Guia metodológico do projeto](#guia-metodológico-do-projeto)')
w('- [Estrutura do repositório](#estrutura-do-repositório)\n')

w('## Resultado principal e ordem de leitura\n')
s = next(i for i, l in enumerate(orig) if l.startswith('## 1. Resultado principal'))
e = next(i for i in range(s + 1, len(orig)) if orig[i].startswith('## 2.'))
w('\n'.join(orig[s + 2:e]).strip() + '\n')

w('## Revisões\n')
for r in sorted(reviews, key=lambda x: -(int(year(x) or 0))):
    pl = pub_link(r)
    w(f"- {year(r)}, [{esc(r['title'])}]({pl}) ({author1(r) or 'autoria a importar'}), {short_venue(r)} {mark(r)} · {r['id']} · {pdf_cell(r)}")
w('')

w('## Artigos e códigos\n')
for k in ORDER:
    rs = sorted(by_sec[k], key=lambda x: x['n'])
    w(f'### {k}. {SEC[k]}\n')
    w(SEC_DESC[k] + '\n')
    w('| ID | Ano | Título | Tipo | Publicação | Código | PDF |')
    w('|----|-----|--------|------|------------|--------|-----|')
    for r in rs:
        pl = pub_link(r)
        pub = f'[{esc(short_venue(r)) or "link"}]({pl})' if pl else '—'
        w(f"| {r['id']} | {year(r)} | {esc(r['title'])} {mark(r)} | {r['kind']} | {pub} | {code_cell(r)} | {pdf_cell(r)} |")
    w('')

# --- GeoAI / QGIS
w('## GeoAI e QGIS: artigos que citam o GeoAI\n')
w(f'Consulta feita em {DATA} no OpenAlex (citações indexadas) e nas páginas oficiais do projeto:\n')
w(f'- **Existe um artigo citável do pacote:** Wu, Q. (2026). *GeoAI: A Python package for integrating artificial intelligence with geospatial data analysis and visualization*. Journal of Open Source Software, 11(118), 9605. https://doi.org/10.21105/joss.09605 (**{pid('10.21105/joss.09605')}**).')
w('- **O plugin QGIS faz parte do pacote.** O README do repositório [opengeos/geoai](https://github.com/opengeos/geoai) lista a "integração com o QGIS por um plugin dedicado" (código na pasta `qgis_plugin`; documentação em https://opengeoai.org/qgis_plugin/). **Não localizei um artigo separado só do plugin.** O trabalho a citar é o do JOSS.')
w(f"- **Pacote:** PyPI `geoai-py` {tools['pypi']['geoai-py']['version']}, licença MIT, Python {tools['pypi']['geoai-py']['requires_python']}.")
w('- **Trabalhos que citam o JOSS do GeoAI (OpenAlex, 24/10/2026):** o índice mostrou apenas 4, o que reflete a publicação recente (fev/2026) e o atraso de indexação:')
w(f'  1. Zhou, Huang, Wang e Mai (2026). *Measuring the spatial explicitness of GeoAI and geospatial foundation models: a systematic review and future roadmap*. ISPRS J. Photogramm. Remote Sens. https://doi.org/10.1016/j.isprsjprs.2026.08.001 (**{pid('10.1016/j.isprsjprs.2026.08.001')}**).')
w(f'  2. Le Guillou, A. (2026). *SemanticSeg4EO: an open-source unified framework and QGIS plugin for semantic segmentation in Earth Observation*. SoftwareX. https://doi.org/10.1016/j.softx.2026.102741 (**{pid('10.1016/j.softx.2026.102741')}**).')
w('  3. Polanco et al. (2026). *Dry forest wood and fiber provision for traditional crafts and its potential impact on woody cactus (Leptocereus paniculatus) populations in the Dominican Republic*. Conservation, 6(4), 127. https://doi.org/10.3390/conservation6040127 (aplicação ecológica; fora do escopo de mudança de cobertura).')
w('  4. Fraser et al. (2026). *A multi-year assessment of oak response to spongy moth using uncrewed aerial vehicles*. J. Earth Obs. Geospat. Appl. https://doi.org/10.65372/ptapac10 (aplicação com UAV; fora do escopo).')
w(f'- **Outros plugins QGIS de deep learning com artigo:** Deepness (**{pid('10.1016/j.softx.2023.101495')}**, SoftwareX 2023), IAMAP (**{pid('10.21105/joss.10329')}**), Geo-SAM e MO-SAM, Land Classification Plugin com Pix2Pix, SemanticSeg4EO, YOLO-MOD, TreeEyed e SpecDeepMap, todos na seção N. O Deepness acumula citações de plugins posteriores (YOLO-MOD, SemanticSeg4EO, TreeEyed, GSIP).')
w('- **Mudança de cobertura no QGIS:** o plugin MOLUSCE (previsão de uso/cobertura por autômatos celulares e redes neurais) tem vários estudos aplicados, listados na seção N. Nenhum deles usa mosaicos Planet mensais nem substitui um modelo temporal.')
w('- **Limite:** nenhum artigo localizado combina GeoAI/QGIS com mosaicos Planet mensais para eventos de mudança. A integração é uma oportunidade de implementação (pré-anotar no QGIS, rodar o modelo e revisar o resultado), não um fluxo validado.\n')

# --- comentarios
w('## Comentário por artigo\n')
w('Os registros P01–P80 reproduzem a revisão original; os de P81 em diante trazem a relevância para o projeto, e o resumo do artigo não foi lido integralmente.\n')
SKIP = {'Fonte', 'Referência'}
for k in ORDER:
    rs = sorted(by_sec[k], key=lambda x: x['n'])
    w(f'### {k}. {SEC[k]}\n')
    for r in rs:
        if r['origin'] == 'original':
            b = r['bullets']
            head = f"**[{r['id']}] {author1(r) or 'Autoria a importar'} {year(r)} — {r['title']}.** {mark(r)}"
            ref = re.sub(r'\*', '', b.get('Referência', ''))
            parts = [f'_Referência:_ {ref}'] if ref else []
            for key, val in b.items():
                if key in SKIP or key.startswith('Código') or key == 'Projeto': continue
                parts.append(f'_{key}:_ {val}')
            w(head + ' ' + ' '.join(parts) + '\n')
        else:
            w(f"**[{r['id']}] {author1(r)} {year(r)} — {r['title']}.** {mark(r)} _Tipo:_ {r['kind']}. _Relevância:_ {r.get('note', '')}\n")
# secao R (revisoes P48-P50) no comentario
w('### Revisões do documento original (P48–P50)\n')
for r in sorted(by_sec['R'], key=lambda x: x['n']):
    b = r['bullets']
    parts = [f'_{key}:_ {val}' for key, val in b.items() if key not in SKIP and not key.startswith('Código')]
    w(f"**[{r['id']}] {author1(r)} {year(r)} — {r['title']}.** {mark(r)} _Referência:_ {re.sub(r'[*]', '', b.get('Referência', ''))} " + ' '.join(parts) + '\n')

# --- ferramentas
w('## Bibliotecas e ferramentas verificadas\n')
w(f'Repositórios consultados na API do GitHub e pacotes no PyPI em {DATA}. Um repositório existente não garante que o ambiente rode sem adaptação, e as licenças devem ser conferidas antes do uso.\n')
w('| Ferramenta | Repositório | Estrelas | Licença | Último push | Status |')
w('|------------|-------------|---------:|---------|-------------|--------|')
for n, v in tools['repos'].items():
    if v.get('ok'):
        st = 'arquivado' if v.get('archived') else 'ativo' if (v.get('pushed', '0') >= '2025-10') else ('estável/sem atividade recente' if v['pushed'] != '—' else 'existe')
        w(f"| {n} | [{v['repo']}](https://github.com/{v['repo']}) | {v.get('stars')} | {v.get('license') or '—'} | {v.get('pushed')} | {st} |")
    else:
        w(f"| {n} | {v['repo']} | — | — | — | **não encontrado ({v.get('status')})** |")
w('')
w('**Pacotes PyPI:**\n')
w('| Pacote | Versão | Python | Licença |')
w('|--------|--------|--------|---------|')
for n, v in tools['pypi'].items():
    w(f"| `{n}` | {v.get('version', '—')} | {v.get('requires_python') or '—'} | {(v.get('license') or '—')[:30]} |" if v.get('ok') else f"| `{n}` | **não publicado no PyPI** | — | — |")
w('\nNotas: BFAST (R, https://bfast.r-forge.r-project.org/) respondeu 503 na checagem automática. O Open-CD não está no PyPI e deve ser instalado do GitHub. O Ultralytics usa AGPL-3.0, o que importa para uso comercial.\n')

# --- links
w('## Verificação dos links\n')
w(f'Todos os {len(links1)} URLs do documento original foram testados em {DATA}: **{nlink_ok}** responderam normalmente (incluindo redirecionamentos para IEEE e PubMed), **{nlink_blk}** devolveram 403 (bloqueio de robôs por editoras como MDPI, ScienceDirect, Taylor & Francis e Wiley; os DOIs correspondentes foram confirmados no OpenAlex) e **{nlink_other}** indisponível (503 transitório no site do BFAST). Nenhum retornou 404. Detalhes em [`dados/links_original.json`](dados/links_original.json).\n')
bad = [r for r in cat if not r.get('checked')]
w(f'Registros não conferidos automaticamente: **{len(bad)}**.' + ('' if not bad else ' ' + ', '.join(r['id'] for r in bad)) + '\n')

# --- tendencias
w('## Tendências 2024–2026\n')
w('Observadas nesta coleta; são leituras do conjunto de títulos e resumos, não resultados medidos:\n')
w(f'1. **Modelos fundacionais (SAM, DINOv3, Prithvi) adaptados à detecção de mudanças**, com muitos trabalhos novos em 2025–2026 (seções C, G e M). Há também avisos de que modelos especializados podem não superar baselines supervisionados ({pid('10.48550/arXiv.2411.02796')}).')
w(f'2. **Mudança semântica em séries temporais**, e não só em pares de datas: TSSCD, DynamicEarthNet, MUDS e redes espaço-temporais (P10–P16, {pid('10.1109/tgrs.2026.3713303')}).')
w(f'3. **Supervisão fraca e poucos rótulos**: supervisão temporal fraca, pseudorrótulos, aprendizado ativo e pré-anotação com SAM/YOLO (P33, P59, P78, {pid('10.1111/phor.70021')}).')
w(f'4. **Planet NICFI como base operacional para floresta**: cobertura arbórea, degradação, perturbações mensais e validação de alertas (P01–P04, {pid('10.1016/j.agrformet.2023.109676')}).')
w('5. **IA geoespacial dentro do QGIS**: plugins de inferência (Deepness, IAMAP, Geo-SAM, GeoAI) reduzem a barreira de uso, mas ainda não há validação publicada com mosaicos Planet mensais (seção N).')
w('6. **Engenharia de dados antes do modelo**: cubos, STAC e controle de qualidade são pré-requisitos para não aprender diferenças de produto como mudança no terreno (seção H).\n')

# --- guia
w('## Guia metodológico do projeto\n')
w('Seções do documento original, mantidas sem alteração de conteúdo: verificações dos mosaicos, taxonomia, experimento, passos para uma revisão sistemática, limitações e arquitetura. Os IDs P01–P80 referem-se às tabelas acima.\n')
w(sect(r'## 3\. O que conferir', r'## 4\.') + '\n')
w(sect(r'## 11\. Taxonomia', r'## 12\.') + '\n')
w(sect(r'## 12\. Experimento', r'## 13\.') + '\n')
w(sect(r'## 13\. Como continuar', r'## 14\.') + '\n')
w(sect(r'## 14\. Limitações', r'## 15\.') + '\n')
w(sect(r'## 19\. Arquitetura', r'\Z_nunca') + '\n')

w('## Estrutura do repositório\n')
w('```text')
w('README.md                 este arquivo')
w('coleta/                   PDFs de acesso aberto + _manifesto.csv')
w('dados/catalog.json        metadados verificados de cada registro')
w('dados/tools.json          repositórios GitHub e pacotes PyPI verificados')
w('dados/links_original.json resultado da checagem dos URLs do documento original')
w('dados/analysis.json       entidades, hiperparametros e frases de resultado extraidos dos PDFs')
w('dados/chunks/             chunks por secao em JSONL (para RAG; fora do git)')
w('dados/leitura_profunda/   fichas de leitura profunda (11 artigos) e sinteses; fonte do vault')
w('vault/                    vault Obsidian: artigos, conceitos, pipeline, experimentos, reuso (abra esta pasta no Obsidian)')
w('fonte_original/           documento de revisão que originou a coleta (inalterado)')
w('scripts/                  scripts de coleta, verificação e geração do README')
w('```\n')
w('## Referências de formato\n')
w('Estrutura inspirada no repositório [ML-for-Location-and-Routing-Optimization-Papers](https://github.com/EstevezCodando/ML-for-Location-and-Routing-Optimization-Papers).')

open(f'{root}/README.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
with open(f'{root}/coleta/_manifesto.csv', 'w', encoding='utf-8-sig', newline='') as f:
    wr = csv.writer(f, delimiter=';')
    wr.writerow(['id', 'secao', 'ano', 'titulo', 'tipo', 'doi', 'verificado', 'arquivo_pdf', 'fonte_pdf', 'origem'])
    for r in sorted(cat, key=lambda x: x['n']):
        wr.writerow([r['id'], r['section'], year(r), r['title'], r['kind'], r.get('doi', ''), 'sim' if r.get('checked') else 'nao',
                     r.get('pdf_file', ''), r.get('pdf_source', ''), r['origin']])
print('README.md:', len(L), 'linhas;', total, 'registros;', nchk, 'conferidos;', npdf, 'PDFs')
