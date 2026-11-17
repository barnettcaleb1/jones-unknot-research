#!/usr/bin/env python3
"""Validate new guide links, catalogs and distributed-source hashes."""
from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import re

root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'data/artifact-manifest.json').read_text())['files']
errors=[]; count=0
for r in manifest:
    if r['disposition']!='git':continue
    p=root/r['path']; count+=1
    if not p.is_file(): errors.append('Missing: '+r['path']); continue
    if hashlib.sha256(p.read_bytes()).hexdigest()!=r['sha256']:errors.append('Hash mismatch: '+r['path'])
guides=list((root/'docs').rglob('*.md'))+[root/'README.md',root/'CONTRIBUTING.md',root/'AGENTS.md']
for p in guides:
    text=re.sub(r'```[^\n]*\n.*?```','',p.read_text(),flags=re.S)
    for m in re.finditer(r'(?<!!)\[[^\]\n]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)',text):
        target=m.group(1).strip('<>')
        if re.match(r'[A-Za-z][A-Za-z0-9+.-]*:',target) or target.startswith('#'):continue
        target=unquote(target.split('#',1)[0])
        if target and not (p.parent/target).exists():errors.append(f'Broken guide link: {p.relative_to(root)} -> {target}')
claims=json.loads((root/'data/claims.json').read_text())
if len({c['key'] for c in claims})!=len(claims):errors.append('Duplicate claim keys')
for c in claims:
    if not (root/c['page']).is_file():errors.append('Missing claim card: '+c['key'])
if errors:
    print('\n'.join(errors[:80])); raise SystemExit(f'{len(errors)} validation errors')
print(f'PASS: {count} source hashes, {len(claims)} claim cards, and {len(guides)} guide pages.')
print('Historical archive links and mathematical correctness are not certified by this check.')
