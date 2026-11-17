#!/usr/bin/env python3
"""Index records without inferring new mathematical truth or dependencies."""
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
from collections import Counter, defaultdict
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
DOCS = ROOT / 'docs'

def write_json(name, data):
    (DATA/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

def slug(s):
    return re.sub('[^a-z0-9]+','-',s.lower()).strip('-')[:90]

def link(path):
    return quote(path, safe='/._-')

def main():
    manifest=json.loads((DATA/'artifact-manifest.json').read_text())['files']
    available={r['path']:r for r in manifest if r['disposition']=='git'}
    by_name=defaultdict(list)
    for path in available: by_name[Path(path).name].append(path)
    claims=[]
    source='archive/outputs/claude-handoff/RESULT_LEDGER.json'
    early=json.loads((ROOT/source).read_text())
    for n,r in enumerate(early['results']):
        claims.append({'key':'early-'+slug(r['id']), 'id':r['id'], 'title':r['title'], 'recorded_status':r['status'],
          'statement':r['body'], 'source':source, 'source_line':None, 'collection':'early handoff',
          'historical_ledger':r.get('ledger'), 'historical_line':r.get('line'), 'review':'Historical status only; check later corrections.'})
    source='archive/collab/SCAFFOLD.md'
    for line_num,line in enumerate((ROOT/source).read_text().splitlines(),1):
        if not line.startswith('|') or line.count('|')<4:continue
        cells=[x.strip() for x in line.strip('|').split('|')]
        if len(cells)<3 or cells[0].lower() in {'node','id','claim','result'} or re.fullmatch('[-: ]+',cells[0]):continue
        identity=cells[0]; key='scaffold-'+slug(identity)+'-'+str(line_num)
        claims.append({'key':key,'id':identity,'title':identity,'recorded_status':cells[-1],
          'statement':' | '.join(cells[1:-1]),'source':source,'source_line':line_num,'collection':'final scaffold snapshot',
          'review':'Snapshot transcription, not a fresh proof audit; latest pause and corrections take precedence.'})
    for c in claims:
        names=set(re.findall(r'[A-Za-z0-9_./-]+\.(?:md|txt|py|tex|json)',c['statement']+' '+c['recorded_status']))
        proofs=[]
        for name in names:
            options=[]
            for candidate in ('archive/'+name,'archive/work/'+name,'archive/claude/'+name):
                if candidate in available: options.append(candidate)
            if not options and len(by_name[Path(name).name])==1: options=by_name[Path(name).name]
            proofs.extend(options)
        c['linked_artifacts']=sorted(set(proofs))
        c['page']='docs/claims/'+c['key']+'.md'
    write_json('claims.json',claims)
    out=DOCS/'claims'
    if out.exists(): shutil.rmtree(out)
    out.mkdir(exist_ok=True)
    for c in claims:
        src=link('../../'+c['source'])+(('#L'+str(c['source_line'])) if c['source_line'] else '')
        text=f"# {c['title']}\n\n[Claim index](../CLAIM_INDEX.md) · [Evidence policy](../EVIDENCE_POLICY.md)\n\n"
        text+='**Record type:** '+c['collection']+'\n\n**Status as recorded:**\n\n```text\n'+c['recorded_status']+'\n```\n\n'
        text+='**Interpretation:** '+c['review']+' Internal review is not external specialist review.\n\n'
        text+='## Statement and recorded scope\n\n```text\n'+c['statement']+'\n```\n\n## Provenance\n\n'
        text+=f"[Source record]({src}). The source wording is retained; consult the chronology for later restrictions or withdrawals.\n"
        if c['linked_artifacts']:
            text+='\n## Identified supporting artifacts\n\n'
            text+='\n'.join('- ['+Path(p).name+']('+link('../../'+p)+')' for p in c['linked_artifacts'])+'\n'
            text+='\nThese links were resolved from explicit filenames, not inferred as a complete logical dependency list.\n'
        (ROOT/c['page']).write_text(text)
    lines=['# Claim index','','This index retains the early handoff and the final scaffold as **separate records**. It does not silently merge conflicting versions. Read [Evidence policy](EVIDENCE_POLICY.md) and [human-work corrections](HUMAN_WORK_AND_CORRECTIONS.md).','','The small proofs are introduced in [Small results](SMALL_RESULTS.md); many additional proof notes are reached from the cards below.','','| Claim | Record | Status excerpt |','|---|---|---|']
    for c in claims:
        status=c['recorded_status'].replace('|',' / ').replace('\n',' ')[:140]
        lines.append(f"| [{c['id'].replace('|',' / ')}]({link('claims/'+c['key']+'.md')}) | {c['collection']} | {status} |")
    (DOCS/'CLAIM_INDEX.md').write_text('\n'.join(lines)+'\n')
    letters=[]
    for p in sorted((ROOT/'archive/collab/msgs').glob('*.md')):
        text=p.read_text(errors='replace'); header=text.split('---',1)[0]
        fields={m.group(1):m.group(2).strip() for m in re.finditer(r'^(from|to|type|node|budget|re):\s*(.*)$',header,re.M)}
        letters.append({'id':p.stem,'path':p.relative_to(ROOT).as_posix(),'date':p.name[:8],**fields})
    write_json('correspondence.json',letters)
    edges=[]
    ids={r['id'] for r in letters}
    for r in letters:
        for ident in re.findall(r'\d{8}-\d{6}-(?:claude|codex)',r.get('re','')):
            if ident in ids: edges.append({'from':r['id'],'to':ident,'type':'reply_to'})
    write_json('provenance-edges.json',edges)
    lines=['# Chronology','','Messages preserve the investigation, including later-refuted claims and historical instructions that are no longer active. See [Evidence policy](EVIDENCE_POLICY.md).','','| Date and ID | From / type | Subject |','|---|---|---|']
    for r in letters:
        lines.append('| ['+r['id']+']('+link('../'+r['path'])+') | '+r.get('from','')+' / '+r.get('type','')+' | '+r.get('node','').replace('|',' / ')+' |')
    (DOCS/'CHRONOLOGY.md').write_text('\n'.join(lines)+'\n')
    groups=defaultdict(list)
    for path in available:
        parts=Path(path).parts
        group='/'.join(parts[1:3]) if len(parts)>3 else parts[1]
        groups[group].append(path)
    idir=DOCS/'archive'
    if idir.exists(): shutil.rmtree(idir)
    idir.mkdir(exist_ok=True)
    lines=['# Archive index','','The archive preserves source bytes. It includes obsolete arguments and machine-specific scripts; read the [status policy](EVIDENCE_POLICY.md) before treating a file as an established result. Large evidence is listed separately in the [manifest](../data/artifact-manifest.json) and [release inventory](../data/release-assets.json).','','| Collection | Included files |','|---|---|']
    for group,paths in sorted(groups.items()):
        name=slug(group)+'.md'; lines.append(f'| [{group}](archive/{name}) | {len(paths)} |')
        listing=['# '+group,'','[Archive index](../ARCHIVE_INDEX.md)','','These are historical source files, not automatically endorsed or portable.','']
        listing += ['- ['+p.removeprefix('archive/')+']('+link('../../'+p)+')' for p in sorted(paths)]
        (idir/name).write_text('\n'.join(listing)+'\n')
    (DOCS/'ARCHIVE_INDEX.md').write_text('\n'.join(lines)+'\n')
    counts=Counter(r['disposition'] for r in manifest)
    byte_counts={k:sum(r['bytes'] for r in manifest if r['disposition']==k) for k in counts}
    summary={'snapshot_date':'2026-11-17','claims':len(claims),'letters':len(letters),'artifacts':len(manifest),'dispositions':dict(counts),'bytes':byte_counts}
    write_json('coverage.json',summary)
    lines=['# Completeness of this snapshot','','This is an inventory of the available research record, not a claim that every proposed proof has been verified or that every conversation ever held was recoverable. The source scope is the workspace `collab/`, `work/`, `outputs/` and the separate `jones-lanes/` research tree. Live chat transcripts outside the saved letters and reports are not fabricated.','','| Category | Files | Bytes |','|---|---:|---:|']
    for k in counts:lines.append(f'| {k} | {counts[k]:,} | {byte_counts[k]:,} |')
    lines += ['',f'The catalog contains {len(claims)} claim records and {len(letters)} letters. Claims may overlap or supersede one another; these are not counts of theorems.','','## What is preserved','','- Original research notes, correspondence, proof drafts, programs, and compact evidence in Git.','- Large generated evidence and historical logs in hash-indexed release supplements, restored at their original archive-relative paths.','- A disposition for every inventoried file, with a reason for exclusion.','- Original wording, including mistakes and unfinished reviews, with a separate current reading guide.','','## What is excluded','','Downloaded human papers and source bundles are cited rather than republished. Vendored dependencies, interpreter environments, compiled executables, and transient state are omitted. Legacy ZIP/tar bundles are inventoried as bundled copies rather than added again; extraction contents are reviewed separately for any unique research documents. These decisions are visible in [artifact-manifest.json](../data/artifact-manifest.json).','','The [source audit](REPRODUCIBILITY_AUDIT.md) describes dependency and provenance limitations. Hash coverage is for the distributed original research files; it does not certify their mathematical correctness. The export program is included so the selection policy is inspectable.','','## Review still needed','','The bibliography is a curated primary-source map, not a fresh verification of every citation in every archived document. Historical bare paths may require the mapping in [Reproducing](REPRODUCING.md). Full manuscript specialist review, complete dependency pinning, and replay of all large certificate collections are not claimed. The contribution tasks make these gaps explicit.']
    (DOCS/'COMPLETENESS.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
