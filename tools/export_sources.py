#!/usr/bin/env python3
"""Build a content-addressed research snapshot; never execute archived programs.

Usage: python tools/export_sources.py WORKSPACE CLAUDE_LANES ASSET_DIRECTORY
The three input locations are explicit. This script does not publish anything.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import re
import shutil
import tarfile
from collections import Counter

REPO = Path(__file__).resolve().parents[1]
VENDOR = {'venv', '.venv', 'site-packages', 'node_modules', '.git', '__pycache__', '__MACOSX', '.state', 'packages', 'wheels'}
BUILD = {'.pyc', '.o', '.so', '.dylib', '.a', '.aux', '.fdb_latexmk', '.fls', '.synctex.gz', '.DS_Store'}
HUMAN_TREES = (
    'work/source/',
    'work/pass3/ren_source/',
    'claude/g2-proof/zrho/read-kasahara/',
    'claude/theory-restart/mech2/floer/lit/',
    'claude/g2-proof/ref-kernel/ito_pdf/',
    'claude/theory-restart/mech/referee-fi/kleinian/dl/',
    'claude/theory-restart/mech2/dictionary/lit_ab/',
    'claude/theory-restart/mech2/colored/lit/bs/',
    'claude/theory-restart/mech2/colored/lit/dl/',
)
HUMAN_FILES = {'work/gz-p74.txt', 'work/gz-p79.txt', 'work/carmi-cohen.txt', 'work/kauffman-bracket.txt',
               'claude/theory-restart/lit/daemi/full.txt', 'work/proof10/homology/knotinfo_data_complete.xls',
               'claude/theory-restart/lit/daemi/intro.txt', 'claude/g2-proof/bbb-gap/bbb.txt',
               'work/proof10/homology/polys.json', 'work/proof10/homology/metadata.json',
               'work/proof10/homology/knot_polys.xlsx', 'work/research26/piwocki_traczyk_source_cache.json',
               'work/fanout16/yui_construct.rs', 'work/fanout16/yui_inv_link.rs'}
TEXT_EXT = {'.md', '.txt', '.py', '.json', '.jsonl', '.tsv', '.csv', '.tex', '.bib', '.yaml', '.yml', '.sh', '.log', '.out', '.html', '.svg', '.cpp', '.h', '.hpp'}

def digest(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def disposition(p, key):
    parts = Path(key).parts
    if any(x in VENDOR for x in parts): return 'excluded', 'retrievable dependency or interpreter cache'
    if p.name == '.DS_Store' or p.suffix in BUILD or p.name.endswith('.synctex.gz'):
        return 'excluded', 'machine-specific or compilation artifact'
    if p.name in {'build.stdout', 'main.out', 'main.log'} and p.with_name('main.tex').exists():
        return 'excluded', 'regenerable manuscript build artifact'
    if key.startswith(HUMAN_TREES) or key in HUMAN_FILES:
        return 'excluded', 'third-party source or dataset; cite upstream instead'
    if re.match(r'claude/theory-restart/lit/[^/]+/src/', key) or re.match(r'claude/theory-restart/(?:mech/(?:cube|annular|floer)|mech2/annular)/src/', key):
        return 'excluded', 'downloaded third-party paper or software source'
    if p.suffix == '.pdf':
        authored = p.name == 'main.pdf' or key == 'collab/NOTE-LATE-41.pdf' or (key.startswith('outputs/') and p.name != 'abernathy-gilmer-genus-one-tangles.pdf')
        if not authored: return 'excluded', 'third-party paper; reference supplied separately'
    if p.suffix in {'.txt', '.tex', '.html'} and p.with_suffix('.pdf').exists() and p.stem != 'main' and key != 'collab/NOTE-LATE-41.tex':
        return 'excluded', 'extracted third-party paper text'
    if p.suffix in {'.zip', '.tar', '.tgz', '.whl'} or p.name.endswith('.tar.gz'):
        return 'excluded', 'legacy bundled copy; individual research artifacts indexed separately'
    if p.name.startswith('HEARTBEAT') or p.suffix == '.pid':
        return 'excluded', 'transient coordination state'
    if p.stat().st_size > 1_000_000 or p.suffix in {'.pkl', '.gz', '.bin', '.kht', '.eps', '.pstex', '.pstex_t'}:
        return 'asset', 'generated data or large evidence; release supplement'
    if key.startswith('claude/') and ('/out/' in key or '/output/' in key or '/outputs/' in key) and p.suffix in {'.svg', '.html', '.png', '.jsonl'}:
        return 'asset', 'generated visualization or detailed run output; release supplement'
    if p.suffix == '.log' or (p.suffix == '.out' and p.with_suffix('.tex').exists()):
        return 'asset', 'historical run or compilation log; release supplement'
    if p.suffix == '' and p.name not in {'README', 'Makefile', 'LICENSE', 'COPYING'}:
        sample = p.read_bytes()[:4096]
        if b'\x00' in sample: return 'excluded', 'compiled executable or binary dependency'
    return 'git', 'original research record, code or compact evidence'

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('workspace', type=Path); ap.add_argument('claude_lanes', type=Path); ap.add_argument('assets', type=Path)
    args = ap.parse_args(); args.assets.mkdir(parents=True, exist_ok=True)
    sources = [(args.workspace / k, k) for k in ('collab', 'work', 'outputs')] + [(args.claude_lanes, 'claude')]
    # This destination contains only generated source copies, never the input roots.
    if (REPO / 'archive').exists(): shutil.rmtree(REPO / 'archive')
    rows, groups = [], {}
    for root, label in sources:
        if not root.is_dir(): raise SystemExit(f'Missing source root: {label}')
        for p in sorted(root.rglob('*')):
            if not p.is_file() or p.is_symlink(): continue
            key = label + '/' + p.relative_to(root).as_posix()
            action, reason = disposition(p, key)
            row = {'source': key, 'bytes': p.stat().st_size, 'disposition': action, 'reason': reason}
            # Excluded cache/vendor files are inventories, not required evidence.
            if action != 'excluded': row['sha256'] = digest(p)
            if action == 'git':
                dest = REPO / 'archive' / key; dest.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(p, dest)
                row['path'] = 'archive/' + key
            elif action == 'asset':
                group = 'claude-' + Path(key).parts[1] if label == 'claude' else label
                groups.setdefault(group, []).append((p, key, row))
                row['path'] = 'archive/' + key
            rows.append(row)
    assets = []
    for group, members in sorted(groups.items()):
        name = 'evidence-' + group + '.tar.gz'; target = args.assets / name
        with target.open('wb') as raw, gzip.GzipFile(filename='', mode='wb', fileobj=raw, compresslevel=1, mtime=0) as gz, tarfile.open(fileobj=gz, mode='w|') as tar:
            for p, key, row in members:
                info = tar.gettarinfo(str(p), arcname='archive/' + key)
                info.uid = info.gid = 0; info.uname = info.gname = ''; info.mtime = 0
                with p.open('rb') as f: tar.addfile(info, f)
                row['asset'] = name
        assets.append({'name': name, 'bytes': target.stat().st_size, 'sha256': digest(target), 'files': len(members), 'extract_at': 'repository root'})
    data = REPO / 'data'; data.mkdir(exist_ok=True)
    (data / 'artifact-manifest.json').write_text(json.dumps({'snapshot_date': '2026-11-17', 'policy': 'tools/export_sources.py', 'files': rows}, indent=2) + '\n')
    (data / 'release-assets.json').write_text(json.dumps(assets, indent=2) + '\n')
    counts = Counter(r['disposition'] for r in rows)
    print(json.dumps({'files': len(rows), 'dispositions': counts, 'assets': assets}, indent=2))

if __name__ == '__main__': main()
