import json
from fractions import Fraction
from collections import defaultdict, Counter
d=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-inversions/data.json'))
H=Counter(); Hadj=Counter(); n=0
levels_span=Counter()
def proc(lst):
    global n
    for a in range(len(lst)):
        for b in range(len(lst)):
            if a==b: continue
            dq=lst[b][0]-lst[a][0]; dd=lst[b][1]-lst[a][1]
            if dd>=0:
                H[(int(dd),dq)]+=1
for x in d['inversions']:
    comps=[c for c in x['khtpp']['BNr_components'] if c['compact']]
    lst=[(c['first_generator']['q'],Fraction(c['first_generator']['delta'])) for c in comps]
    proc(lst); n+=1
print('138 table: pairs of compact BN components in one tangle, (delta difference >=0, q difference): count')
for key in sorted(H): print('  ',key,H[key])
# per level min/max of compact q, adjacent levels
H2=Counter()
recs=[json.loads(l) for l in open('/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/tilt/run_3_45.jsonl')]
H.clear()
m=0
for r in recs:
    if 'bn' not in r: continue
    lst=[(c['q'],Fraction(c['delta'])) for c in r['bn'] if c['cyclic']]
    proc(lst); m+=1
print('two-bridge run (',m,'records): same statistic')
for key in sorted(H): print('  ',key,H[key])
