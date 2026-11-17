#!/usr/bin/env python3
"""Import only a hash-pinned, editorially reviewed handoff; never execute it.

Usage: python tools/import_handoff.py HANDOFF_ROOT [--prepared REVIEWED_COPIES]
The manifest is the admission list, not a directory-wide permission to copy.
Original private staging is not part of this repository. Readers can verify
published hashes without having it. Reimport requires the received files and,
for editorially redacted records, the separately prepared reviewed copies.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def sha(data):
    return hashlib.sha256(data).hexdigest()

def normalize_paths(data):
    text = data.decode('utf-8')
    text = re.sub(r'/Users/[^/\s\"\'<>`]+', '$HOME', text)
    text = re.sub(r'-Users-[^-\s/\"\'<>`]+-', '-USER_HOME-', text)
    return text.encode('utf-8')

def safe_join(root, relative):
    p = root / relative
    if not p.resolve().is_relative_to(root.resolve()) or p.is_symlink():
        raise ValueError('Unsafe handoff path: ' + relative)
    return p

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('handoff_root', type=Path)
    ap.add_argument('--prepared', type=Path)
    args = ap.parse_args()
    registry = json.loads((ROOT/'data/handoff-artifacts.json').read_text())
    prepared = []
    for row in registry['records']:
        if row['disposition'] != 'git':
            continue
        source = safe_join(args.handoff_root, row['received_path'])
        received = source.read_bytes()
        if sha(received) != row['received_sha256']:
            raise ValueError('Received hash mismatch: ' + row['received_path'])
        if row.get('editorial_input_sha256'):
            if args.prepared is None:
                raise ValueError('Reviewed copies required; no raw fallback is allowed')
            data = safe_join(args.prepared, row['received_path']).read_bytes()
            if sha(data) != row['editorial_input_sha256']:
                raise ValueError('Editorial input hash mismatch: ' + row['received_path'])
        else:
            data = received
        if row.get('normalize_home_paths'):
            data = normalize_paths(data)
        if sha(data) != row['published_sha256']:
            raise ValueError('Published hash mismatch: ' + row['received_path'])
        target = safe_join(ROOT, row['path'])
        if not row['path'].startswith('archive/handoff/'):
            raise ValueError('Destination outside handoff archive')
        prepared.append((row, target, data))
    # Complete all preflight checks before writing anything.
    manifest_path = ROOT/'data/artifact-manifest.json'
    manifest = json.loads(manifest_path.read_text())
    manifest['files'] = [r for r in manifest['files'] if not r['source'].startswith('handoff/')]
    for row, target, data in prepared:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        manifest['files'].append({
            'source': 'handoff/' + row['received_path'],
            'path': row['path'], 'bytes': len(data), 'disposition': 'git',
            'reason': 'reviewed Claude handoff; transformations in data/handoff-artifacts.json',
            'sha256': row['published_sha256']})
    manifest['handoff_policy'] = 'tools/import_handoff.py and data/handoff-artifacts.json'
    manifest_path.write_text(json.dumps(manifest, indent=2)+'\n')
    print(f'Imported {len(prepared)} reviewed handoff records; no programs executed.')

if __name__ == '__main__':
    main()
