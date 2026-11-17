import json
from fractions import Fraction
from collections import defaultdict, Counter
recs=[json.loads(l) for l in open('/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/tilt/run_3_45.jsonl')]
def kj(r):
    rat=[c for c in r['khr'] if c['type']=='r'][0]
    k=int(rat['slope']); 
    j=(Fraction(rat['q']).limit_denominator(1000)-Fraction(k*(abs(k)+2),abs(k)+1))/24
    return k,j
for r in recs:
    if 'bn' not in r: continue
    lst=[(c['q'],Fraction(c['delta'])) for c in r['bn'] if c['cyclic']]
    hit=[(a,b) for a in lst for b in lst if a[0]==b[0] and b[1]==a[1]+1]
    if hit:
        k,j=kj(r)
        print(r['file'].split('/')[-1],'k,j=',k,j)
        print('   B-like pairs (q, delta) & (q, delta+1):',[(a[0],str(a[1]),str(b[1])) for a,b in hit])
        arc=[c for c in r['bn'] if not c['cyclic']]
        print('   arc first gen:',arc)
        bylev=defaultdict(list)
        for q,dl in lst: bylev[dl].append(q)
        print('   compact comps by level (printed frame):',{str(l):sorted(v) for l,v in sorted(bylev.items())})
        sp=defaultdict(list)
        for c in r['khr']:
            if c['type']=='s': sp[Fraction(c['delta'])].append(int(c['q']))
        print('   specials by level (printed):',{str(l):sorted(v) for l,v in sorted(sp.items())})
        print('   normalized specials (c-24j,d-4j):',{str(l-4*j):sorted(int(q-24*j) for q in v) for l,v in sorted(sp.items())})
