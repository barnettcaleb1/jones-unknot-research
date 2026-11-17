# Look for B-like sub-configurations in actual data: two compact BN~ components that are
# homological shifts of one another (same first-generator q, same chain, delta differing by 1).
import json, sys
from fractions import Fraction
from collections import defaultdict
d=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-inversions/data.json'))
k138={json.loads(l)['file']:json.loads(l) for l in open('/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/k138.jsonl')}
tot=0; hits=[]
kj=defaultdict(int)
for x in d['inversions']:
    name=x['name']
    comps=[c for c in x['khtpp']['BNr_components'] if c['compact']]
    k=x['rational_component']['slope_k']
    qav=Fraction(x['rational_component']['bigrading']['q_average'])
    # 24 j = qav - k(|k|+2)/(|k|+1)
    j=(qav-Fraction(k*(abs(k)+2),abs(k)+1))/24
    kj[(k,j)]+=1
    lst=[(c['first_generator']['q'],Fraction(c['first_generator']['delta']),c['first_generator']['h'],c['chain'],c['n_generators']) for c in comps]
    tot+=len(lst)
    for a in range(len(lst)):
        for b in range(len(lst)):
            if a==b: continue
            qa,da,ha,ca,na=lst[a]; qb,db,hb,cb,nb=lst[b]
            if qa==qb and ca==cb and db==da-1:
                hits.append((name,k,j,qa,da,db,na))
print('compact BN components total',tot)
print('B-like pairs (gamma, h gamma) inside actual tangles:',len(hits))
for h in hits: print('  ',h)
print('distribution of (k,j):')
for key,v in sorted(kj.items()): print('  ',key,v)
print('distinct compact chain shapes:')
shapes=defaultdict(int)
for x in d['inversions']:
    for c in x['khtpp']['BNr_components']:
        if c['compact']: shapes[(c['n_generators'],c['chain'])]+=1
for s,v in shapes.items(): print('  ',v,s)
