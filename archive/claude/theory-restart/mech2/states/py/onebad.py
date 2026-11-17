import sys, os, glob, json, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
from bcube import *
from badblocks import bad_blocks, SI, describe
rows = {}
for l in open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/survey.jsonl'):
    r = json.loads(l); rows[r['name']] = r
agg = collections.defaultdict(list)
for nm, r in sorted(rows.items()):
    if 'err' in r: continue
    half, orient, sym = read_kht(os.path.join(SI, nm + '.kht'))
    for end, tag in ((1, 'top'), (0, 'bot')):
        blocks, k = bad_blocks(half, end)
        bad = [b for b in blocks if b['nbad']]
        n = r['ncr']
        defect = (n - r['N_top'][0], r['top_gap']) if end == 1 else (r['N_bot'][0], r['bot_gap'])
        if len(bad) == 1:
            b = bad[0]
            comp = b['comp'] if b['comp'] in 'ab' else 'circle'
            agg[(b['kind'], b['state'], comp, defect)].append(nm + ':' + tag)
        if len(bad) == 2:
            key = tuple(sorted((b['kind'][0] + b['state'][0] + (b['comp'] if b['comp'] in 'ab' else 'c')) for b in bad))
            agg[('TWO',) + key + (defect,)].append(nm + ':' + tag)
for k, v in sorted(agg.items(), key=lambda t: str(t[0])):
    print(k, len(v), v[:6])
