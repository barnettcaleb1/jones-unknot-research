"""Render the stage-count table for REPORT section 5 from the data files."""
import json, gzip
from collections import Counter
D = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/'
def stage_counts(fn):
    try: R = json.load(open(D + fn))
    except FileNotFoundError: return None
    return dict(Counter(r['status'] for r in R))
def cert_counts(tag):
    c = Counter(); cp = Counter()
    try:
        with gzip.open(D + tag + '_certificates.jsonl.gz', 'rt') as f:
            for line in f:
                x = json.loads(line); c[x['status']] += 1; cp[x['status']] += len(x['prov'])
    except FileNotFoundError: return None, None
    return dict(c), dict(cp)
for tag in ('s1', 's2', 's3a', 's3b'):
    w, p = cert_counts(tag)
    print(tag, 'stage1 words', w, '| configurations', p)
    for st in ('stage2', 'stage3'):
        sc = stage_counts(tag + '_' + st + '.json')
        if sc: print('   ', st, sc)
