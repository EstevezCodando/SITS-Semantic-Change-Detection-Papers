"""Imprime chunks de um paper por secoes (uso de leitura): python show_chunks.py P01 secao1,secao2"""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')
pid, secs = sys.argv[1], set(sys.argv[2].split(','))
for l in open(f'dados/chunks/{pid}.jsonl', encoding='utf-8'):
    c = json.loads(l)
    if c['secao'] in secs: print(f"[{c['id']}|{c['secao']}|p{c['pagina']}|{c['titulo_secao'][:40]}] {c['texto']}\n")
