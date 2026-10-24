"""Validate all current manifest outputs, page coverage and image decoding."""
import json
from pathlib import Path
import re
import hashlib
import argparse
import sys
import pymupdf

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--input', type=Path, default=root / 'coleta')
parser.add_argument('--output', type=Path, default=root / 'output/pdf')
args = parser.parse_args()
output = args.output.resolve()
source_root = args.input.resolve()
report = json.loads((output / 'report.json').read_text(encoding='utf-8'))
failures = []
quality_notes = []
images = 0
for record in report['documents']:
    folder = Path(record['output'])
    md = (folder / 'document.md').read_text(encoding='utf-8')
    replacement_count = md.count('\ufffd')
    if replacement_count:
        quality_notes.append({'source': record['source'], 'replacement_characters': replacement_count,
                              'note': 'Caracteres não reconhecidos; conferir fórmulas e símbolos no PDF.'})
    page_data = json.loads((folder / 'pages.json').read_text(encoding='utf-8'))
    short_pages = [p['page'] for p in page_data if p['source_characters'] > 500
                   and p['markdown_characters'] < p['source_characters'] * 0.5]
    if short_pages:
        quality_notes.append({'source': record['source'], 'short_pages': short_pages,
                              'note': 'Markdown significativamente menor que o texto extraível; revisar cobertura.'})
    pages = [int(n) for n in re.findall(r'<!-- page: (\d+) -->', md)]
    if pages != list(range(1, record['pages'] + 1)):
        failures.append(f"Cobertura de páginas: {record['source']}")
    text_path = folder / 'text.md'
    if not text_path.is_file():
        failures.append(f"Texto de salvaguarda ausente: {record['source']}")
    elif [int(n) for n in re.findall(r'<!-- page: (\d+) -->', text_path.read_text(encoding='utf-8'))] != list(range(1, record['pages'] + 1)):
        failures.append(f"Cobertura do texto de salvaguarda: {record['source']}")
    source = source_root / record['source']
    if hashlib.sha256(source.read_bytes()).hexdigest() != record['key']['sha256']:
        failures.append(f"Original alterado: {record['source']}")
    all_files = set(record['files'])
    all_files.update(p.relative_to(folder).as_posix() for sub in ('images', 'raster')
                     for p in (folder / sub).glob('*') if p.is_file())
    for name in sorted(all_files):
        path = folder / name
        if not path.is_file() or path.stat().st_size == 0:
            failures.append(f"Arquivo ausente ou vazio: {path}")
        elif name.startswith(('images/', 'raster/')):
            try:
                pix = pymupdf.Pixmap(path)
                assert pix.width > 0 and pix.height > 0
                images += 1
            except Exception as exc:
                failures.append(f"Imagem ilegível: {path}: {exc}")
    for name in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', md):
        if name.startswith(('images/', 'raster/')) and not (folder / name).is_file():
            failures.append(f"Link quebrado: {folder / name}")
pdf_count = sum(1 for p in source_root.rglob('*') if p.is_file() and p.suffix.lower() == '.pdf')
if report['converted'] != pdf_count or report['failed']:
    failures.append('O relatório não cobre todos os PDFs com sucesso.')
result = {'documents': len(report['documents']), 'pages': report['pages'],
          'images_decoded': images, 'failures': failures,
          'warnings': sum(len(r['warnings']) for r in report['documents']),
          'quality_notes': quality_notes}
(output / 'validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(bool(failures))
