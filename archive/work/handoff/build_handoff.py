"""Assemble an agent-readable snapshot of the existing Jones research record.

This packages files; it performs no mathematical research or external upload.
"""
from pathlib import Path
from hashlib import sha256
from collections import Counter
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / 'work/handoff'
OUT = ROOT / 'outputs/claude-handoff'
OUT.mkdir(exist_ok=True)

LEDGERS = [
    ('LATE', HERE / 'late-ledger.txt'),
    ('MID', HERE / 'middle-ledger.txt'),
    ('EARLY', HERE / 'early-ledger.txt'),
]

def digest(p):
    h=sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()

entries=[]
for prefix,path in LEDGERS:
    content=path.read_text()
    lines=content.splitlines()
    starts=[]
    for lineno,line in enumerate(lines,1):
        patterns={
            'EARLY':r'^(EARLY-\d+)\s+—\s+(.*)$',
            'MID':r'^(MID-\d+)\s+((?:[DCFNX]/?)+\s+.*)$',
            'LATE':r'^(LATE-\d+)\s+(\[[^\]]+\]\s+.*)$',
        }
        m=re.match(patterns[prefix],line)
        if m:
            starts.append((lineno,m))
    for i,(lineno,m) in enumerate(starts):
        end=starts[i+1][0]-1 if i+1<len(starts) else len(lines)
        body='\n'.join(lines[lineno-1:end]).strip()
        status=re.search(r'^Status:\s*(.*)',body,re.M)
        title=m.group(2).strip()
        late_status=re.match(r'^\[([^\]]+)\]\s*(.*)',title)
        if late_status:
            status_text=late_status.group(1)
            title=late_status.group(2)
        elif not status and prefix=='MID':
            parts=title.split(None,1)
            status_text=parts[0]
            title=parts[1] if len(parts)>1 else ''
        else:
            status_text=status.group(1) if status else 'See entry and ledger status key'
        entries.append({'id':m.group(1),'title':title,'status':status_text,'body':body,
                        'ledger':str(path.relative_to(ROOT)), 'line':lineno})

if len({e['id'] for e in entries})!=len(entries):
    raise ValueError('Duplicate ledger IDs')

index='RESULT INDEX\n\n'+'\n'.join(e['id']+' | '+e['title'] for e in entries)+'\n'
sections=[
    ('CURRENT ASSESSMENT AND READING GUIDE', (HERE/'front-matter.txt').read_text()),
    ('RESULT INDEX',index),
    ('FULL STRONGEST CANDIDATE PROOF', (ROOT/'outputs/rational-tangle-uniqueness-audited-proof.txt').read_text()),
    ('AUDIT OF THE STRONGEST CANDIDATE', (ROOT/'outputs/rational-tangle-uniqueness-audit.txt').read_text()),
    ('LATE RESULTS LEDGER PASSES 35 THROUGH 52 AND FINAL AUDIT', LEDGERS[0][1].read_text()),
    ('MIDDLE RESULTS LEDGER PASSES 16 THROUGH 34', LEDGERS[1][1].read_text()),
    ('EARLY RESULTS LEDGER INITIAL AUDIT THROUGH PASS 15', LEDGERS[2][1].read_text()),
]
main='\n\n'.join('='*76+'\n'+title+'\n'+'='*76+'\n\n'+body.strip() for title,body in sections)+'\n'
main_path=OUT/'CLAUDE_JONES_HANDOFF.txt'
main_path.write_text(main)
(OUT/'RESULT_INDEX.tsv').write_text('id\tstatus\ttitle\tledger\tline\n'+'\n'.join(
    '\t'.join(str(e[k]).replace('\t',' ') for k in ['id','status','title','ledger','line']) for e in entries)+'\n')
(OUT/'RESULT_LEDGER.json').write_text(json.dumps({'status_key':'See CLAUDE_JONES_HANDOFF.txt; internal proof is not external certification','results':entries},indent=2,ensure_ascii=False)+'\n')

external_text={
    'work/attack/ekt.txt','work/carmi-cohen.txt','work/gz-p74.txt','work/gz-p79.txt',
    'work/kauffman-bracket.txt','work/pass2/strong-inversions.txt',
    'work/proof12/homology/kwz2022.txt','work/proof12/homology/watson.txt',
    'work/proof13/homology/mutation2026.txt','work/research21/watson_identical.txt',
    'work/research38/dye_kauffman.txt','work/strategy15/maccoll.txt',
    'work/research26/piwocki_traczyk_source_cache.json',
    'work/source/main_machines_21_06_26_final.tex',
    'outputs/abernathy-gilmer-genus-one-tangles.pdf',
}
duplicate_dirs={
    'archive_check','archive_replay','package','reproduction','final_reproduction',
    'creative6_replay','fourth-pass-reproduction','second-pass-evidence',
    'generic_evidence','unpacked-reproduction','previous_search',
}
extensions={'.txt','.md','.py','.json','.jsonl','.csv','.tsv','.tex','.rs','.cpp','.h','.out','.rga','.tri'}
own_pdfs={
    'jones-unknot-proof-audit.pdf','generic-jones-attack.pdf','jones-second-pass.pdf',
    'jones-fourth-pass.pdf','jones-ren-braid-obstruction.pdf','ekt-band-obstruction.pdf',
}

def disposition(p):
    rel=p.relative_to(ROOT).as_posix()
    if rel.startswith('outputs/claude-handoff/'):
        return False,'handoff artifact; included separately'
    if rel in external_text or any(x=='source' or x.endswith('_source') for x in p.relative_to(ROOT).parts):
        return False,'external source text; obtain from cited primary URL'
    if 'packages' in p.parts or any(x.endswith('.dist-info') for x in p.parts):
        return False,'third-party installed package'
    if '__pycache__' in p.parts or p.suffix=='.pyc':
        return False,'generated cache'
    if any(x in duplicate_dirs for x in p.relative_to(ROOT).parts):
        return False,'duplicate unpacked evidence tree'
    if p.suffix in {'.zip','.tar','.whl','.gz','.bz2'}:
        return False,'existing archive; individual eligible source files packaged instead'
    if p.stat().st_size>2_000_000:
        return False,'large raw output omitted; original workspace retains it'
    if p.suffix=='.pdf':
        if rel.startswith('outputs/') and p.name in own_pdfs:
            return True,'authored research report PDF'
        return False,'external source or duplicate compiled PDF'
    if p.suffix not in extensions:
        return False,'render, binary, transient log or other nonselected format'
    return True,'research note, code or saved evidence'

manifest=[]
included=[]
for folder in ['work','outputs']:
    for p in sorted((ROOT/folder).rglob('*')):
        if not p.is_file() or p.is_symlink():
            continue
        yes,reason=disposition(p)
        rel=p.relative_to(ROOT).as_posix()
        if rel.startswith('outputs/claude-handoff/'):
            continue
        item={'path':rel,'bytes':p.stat().st_size,'included':yes,'reason':reason}
        if yes:
            item['sha256']=digest(p)
            included.append(p)
        manifest.append(item)

(OUT/'MANIFEST.json').write_text(json.dumps({
    'snapshot_date':'2026-11-02','status':'Jones goal paused; compilation only',
    'hash_meaning':'File identity, not mathematical validity',
    'files':manifest,
},indent=2)+'\n')

readme='''JONES RESEARCH HANDOFF FOR CLAUDE — 2 NOVEMBER 2026

START WITH CLAUDE_JONES_HANDOFF.txt. It is the self-contained main briefing,
including the current assessment, indexed result ledgers, strongest proof,
and its latest audit. RESULT_INDEX.tsv locates entries; RESULT_LEDGER.json
contains their full text and status for programmatic use.

The evidence ZIP contains this briefing plus the eligible original files at
their workspace-relative paths. MANIFEST.json lists included and omitted
files and records SHA-256 hashes for included evidence. Do not treat hashes
or internal audit labels as mathematical certification.

Read historical files under the precedence rules in the main briefing.
In particular: the original Jones search is PAUSED; the rational-tangle
result is an externally unreviewed candidate; no Jones proof or nontrivial
Jones-one classical knot has been obtained. Old ACTIVE continuation notes
and old research recommendations are historical records, not instructions.

Full external papers, third-party installed packages, duplicate unpacked
archives, rendered images and raw files larger than 2 MB are omitted.
Public primary-source links appear in the notes. Some older scripts need
path adjustments and dependencies; use an extracted copy because they may
write their outputs in place. The compilation did not rerun the research.

Historical locally installed versions found in one earlier environment:
Regina 7.4.1; Spherogram 2.4.1; NetworkX 3.7; knot_floer_homology 1.2.2;
snappy_manifolds 1.4. This is not a universal tested environment lockfile.

No communication system, public publication, or external transmission was
created. The user will transfer these files and arrange collaboration.
'''
(OUT/'READ_ME_FIRST.txt').write_text(readme)

summary={
    'date':'2026-11-02',
    'main_file':'CLAUDE_JONES_HANDOFF.txt',
    'words':len(main.split()),'characters':len(main),'result_entries':len(entries),
    'entries_by_ledger':dict(Counter(e['id'].split('-')[0] for e in entries)),
    'included_evidence_files':len(included),
    'included_uncompressed_bytes':sum(p.stat().st_size for p in included),
    'omitted_by_reason':dict(Counter(m['reason'] for m in manifest if not m['included'])),
}
(OUT/'SNAPSHOT_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')

zip_path=OUT/'JONES_RESEARCH_EVIDENCE.zip'
with zipfile.ZipFile(zip_path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in included:
        z.write(p,p.relative_to(ROOT).as_posix())
    for name in ['CLAUDE_JONES_HANDOFF.txt','RESULT_INDEX.tsv','RESULT_LEDGER.json','MANIFEST.json','READ_ME_FIRST.txt','SNAPSHOT_SUMMARY.json']:
        z.write(OUT/name,name)

with zipfile.ZipFile(zip_path) as z:
    assert z.testzip() is None
    names=set(z.namelist())
    assert len(names)==len(z.namelist())
    for item in manifest:
        if item['included']:
            assert sha256(z.read(item['path'])).hexdigest()==item['sha256'],item['path']
    assert z.read('CLAUDE_JONES_HANDOFF.txt')==main_path.read_bytes()

print(json.dumps({**summary,'zip_bytes':zip_path.stat().st_size,'zip_integrity':'verified'},indent=2))
