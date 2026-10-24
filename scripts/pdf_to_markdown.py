"""Batch local PDF -> Markdown, figure crops and original raster assets."""
from __future__ import annotations
import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path
import re
import sys
import time
from urllib.parse import quote

import pymupdf
import pymupdf4llm

VERSION = 1
AUDIT_VERSION = 1
ROOT = Path(__file__).resolve().parents[1]


def dump(path, data):
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    temporary.replace(path)


def preserve_text(record, source):
    """Keep extractable text even when a layout detector absorbs it into a figure."""
    destination = Path(record['output'])
    if record.get('text_audit') == AUDIT_VERSION and (destination / 'text.md').is_file():
        return record
    pages_path = destination / 'pages.json'
    page_records = json.loads(pages_path.read_text(encoding='utf-8'))
    content = (destination / 'document.md').read_text(encoding='utf-8')
    sections = re.split(r'(?=<!-- page: \d+ -->)', content)
    plain = [f"# Texto extraído: {Path(record['source']).stem}\n\nExtração textual direta, sem reconstrução de tabelas ou fórmulas. Consulte `document.md` para layout e figuras.\n"]
    with pymupdf.open(source) as doc:
        for pno, page in enumerate(doc):
            raw = page.get_text(sort=True).strip()
            fence = '`' * max(3, max((len(x) + 1 for x in re.findall(r'`+', raw)), default=3))
            text_block = f"\n\n{fence}text\n{raw}\n{fence}\n"
            plain.append(f"\n\n<!-- page: {pno + 1} -->\n\n## Página {pno + 1}{text_block}")
            stats = page_records[pno]
            if stats['source_characters'] > 500 and stats['markdown_characters'] < stats['source_characters'] * 0.5:
                addition = '\n\n### Complemento de texto extraído\n\nA análise de layout retornou menos da metade do texto desta página. A extração direta abaixo preserva o conteúdo disponível e pode repetir trechos, rótulos ou camadas do PDF.\n' + text_block
                # The last page also includes the raster appendix; insert before it.
                appendix = '\n\n## Imagens raster incorporadas'
                if appendix in sections[pno + 1]:
                    sections[pno + 1] = sections[pno + 1].replace(appendix, addition + appendix, 1)
                else:
                    sections[pno + 1] += addition
                stats['text_supplement'] = True
                record['warnings'].append(f"Página {pno + 1}: cobertura de layout reduzida; texto direto incluído como complemento.")
    (destination / 'document.md').write_text(''.join(sections), encoding='utf-8')
    (destination / 'text.md').write_text(''.join(plain), encoding='utf-8')
    dump(pages_path, page_records)
    record['files'] = sorted(set(record['files'] + ['text.md']))
    record['text_audit'] = AUDIT_VERSION
    dump(destination / 'manifest.json', record)
    return record


def convert(job):
    source, relative, destination, dpi, force = job
    source, destination = Path(source), Path(destination)
    key = {"sha256": hashlib.sha256(source.read_bytes()).hexdigest(), "dpi": dpi,
           "pipeline": VERSION, "pymupdf": pymupdf.__version__, "pymupdf4llm": "0.0.27"}
    manifest = destination / "manifest.json"
    if manifest.exists() and not force:
        old = json.loads(manifest.read_text(encoding="utf-8"))
        if old.get("key") == key and all((destination / p).is_file() for p in old.get("files", [])) and old.get("files"):
            return old
    destination.mkdir(parents=True, exist_ok=True)
    # An interrupted forced rebuild must not leave an apparently valid old cache.
    manifest.unlink(missing_ok=True)
    figures = destination / "images"
    originals = destination / "raster"
    figures.mkdir(exist_ok=True)
    originals.mkdir(exist_ok=True)
    warnings, page_records, raster_records, seen = [], [], [], set()
    parts = [f"# {source.stem}\n\nFonte: `{relative}`\n"]
    started = time.monotonic()
    with pymupdf.open(source) as doc:
        if doc.needs_pass:
            raise ValueError("PDF protegido por senha")
        headers = pymupdf4llm.IdentifyHeaders(doc)
        for number, page in enumerate(doc):
            raw = page.get_text(sort=True)
            if len(raw.strip()) < 40:
                warnings.append(f"Página {number + 1}: pouco texto; verificar necessidade de OCR.")
            try:
                chunks = pymupdf4llm.to_markdown(doc, pages=[number], hdr_info=headers,
                    write_images=True, image_path=figures.as_posix(), image_format="png",
                    image_size_limit=0, dpi=dpi, page_chunks=True, margins=0,
                    force_text=True, show_progress=False)
                chunk = chunks[0]
                md = chunk.pop("text")
                md = md.replace(figures.as_posix() + "/", "images/")
                md = md.replace(str(figures) + "\\", "images/")
                mode = "layout"
            except Exception as exc:
                warnings.append(f"Página {number + 1}: fallback de texto ({type(exc).__name__}: {exc}).")
                md, chunk, mode = raw, {}, "fallback"
                snapshot = figures / f"fallback-page-{number + 1:04d}.png"
                page.get_pixmap(dpi=dpi).save(snapshot)
                md += f"\n\n![Página original]({snapshot.relative_to(destination).as_posix()})\n"
            # Preserve every embedded raster object, including those omitted/grouped by layout detection.
            for item in page.get_images(full=True):
                xref = item[0]
                if xref in seen:
                    continue
                seen.add(xref)
                try:
                    image = doc.extract_image(xref)
                    if not image:
                        continue
                    target = originals / f"xref-{xref:06d}.{image['ext']}"
                    target.write_bytes(image['image'])
                    raster_records.append({"xref": xref, "first_page": number + 1,
                        "file": target.relative_to(destination).as_posix(),
                        "width": image['width'], "height": image['height'], "smask": image.get('smask', 0)})
                except Exception as exc:
                    warnings.append(f"Imagem xref {xref}: {exc}")
            parts.append(f"\n\n<!-- page: {number + 1} -->\n\n## Página {number + 1}\n\n{md.strip()}\n")
            page_records.append({"page": number + 1, "source_characters": len(raw),
                "markdown_characters": len(md), "mode": mode, "layout": chunk})
        metadata = doc.metadata
    parts.append("\n\n## Imagens raster incorporadas\n\nOs recortes acima preservam a aparência da página. Abaixo estão os objetos raster do PDF, que podem ser painéis, máscaras ou componentes de figuras.\n")
    parts.extend(f"- [Imagem {r['xref']} (primeira ocorrência: página {r['first_page']})]({r['file']})\n" for r in raster_records)
    content = "".join(parts)
    (destination / "document.md").write_text(content, encoding="utf-8")
    missing = [p for p in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", content)
               if p.startswith(("images/", "raster/")) and not (destination / p).is_file()]
    if missing:
        raise ValueError(f"Links de imagens inexistentes: {missing}")
    dump(destination / "pages.json", page_records)
    dump(destination / "rasters.json", raster_records)
    files = ["document.md", "pages.json", "rasters.json"]
    files += sorted({p for p in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", content) if p.startswith(("images/", "raster/"))})
    record = {"source": relative, "key": key, "pages": len(page_records),
        "figure_crops": len([p for p in files if p.startswith('images/')]),
        "raster_objects": len(raster_records), "warnings": warnings,
        "metadata": metadata, "seconds": round(time.monotonic() - started, 2), "files": files,
        "output": str(destination)}
    dump(manifest, record)
    return record


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=ROOT / "coleta")
    parser.add_argument("--output", type=Path, default=ROOT / "output" / "pdf")
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--dpi", type=int, default=180)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()
    if args.workers < 1 or args.dpi < 72:
        parser.error("workers deve ser >= 1 e dpi >= 72")
    source, output = args.input.resolve(), args.output.resolve()
    pdfs = sorted(p for p in source.rglob('*') if p.is_file() and p.suffix.lower() == '.pdf')
    if args.limit:
        pdfs = pdfs[:args.limit]
    if not pdfs:
        parser.error(f"Nenhum PDF encontrado em {source}")
    output.mkdir(parents=True, exist_ok=True)
    results, errors = [], []
    jobs = [(str(p), p.relative_to(source).as_posix(), str(output / p.relative_to(source).with_suffix('')), args.dpi, args.force) for p in pdfs]
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(convert, job): job[1] for job in jobs}
        for future in as_completed(futures):
            name = futures[future]
            try:
                result = future.result()
                result = preserve_text(result, source / result['source'])
                results.append(result)
                print(f"[{len(results) + len(errors)}/{len(pdfs)}] OK {name}: {result['pages']} páginas, {result['figure_crops']} recortes", flush=True)
            except Exception as exc:
                errors.append({"source": name, "error": f"{type(exc).__name__}: {exc}"})
                print(f"ERRO {name}: {exc}", flush=True)
    results.sort(key=lambda r: r['source'])
    report = {"pdfs_found": len(pdfs), "converted": len(results), "failed": len(errors),
        "pages": sum(r['pages'] for r in results), "figure_crops": sum(r['figure_crops'] for r in results),
        "raster_objects": sum(r['raster_objects'] for r in results), "errors": errors, "documents": results}
    dump(output / "report.json", report)
    lines = ["# PDFs convertidos\n", f"\n{len(results)}/{len(pdfs)} PDFs; {report['pages']} páginas; {report['figure_crops']} recortes; {report['raster_objects']} objetos raster.\n",
             "\nConversão automática. Confira fórmulas, tabelas complexas e ordem de leitura no original. Avisos detalhados em `report.json`.\n\n"]
    for r in results:
        link = (Path(r['output']) / 'document.md').relative_to(output).as_posix()
        lines.append(f"- [{Path(r['source']).stem}]({quote(link)}) — {r['pages']} páginas, {r['figure_crops']} recortes, {len(r['warnings'])} avisos\n")
    if errors:
        lines.append("\n## Falhas\n" + '\n'.join(f"- {e['source']}: {e['error']}" for e in errors))
    (output / "README.md").write_text(''.join(lines), encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k != 'documents'}, ensure_ascii=False), flush=True)
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
