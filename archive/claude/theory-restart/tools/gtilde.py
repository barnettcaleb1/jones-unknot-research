#!/usr/bin/env python3
"""g~ = 2q - 3h = q/2 + 3*delta on the J-set (bullet generators of BN~(T)).
J-set (uncentred kht labels) = {(24j+2k, 4j)} + {(c+4, d-1), (c-4, d) : (c,d) special}.
Reports, per record: number of generators, delta-levels, g~ range, g~ width, sign-coherence, END at both ends."""
import json,sys,collections
from fractions import Fraction as Fr
def valid(khr):
    rs=[c for c in khr if c['type']=='r']
    if len(rs)!=1: return False
    if any(c['type']=='s' and c['slope']!='∞' for c in khr): return False
    try: int(rs[0]['slope'])
    except: return False
    return True
def jset(khr):
    r=[c for c in khr if c['type']=='r'][0]
    k=int(r['slope'])
    qr=Fr(r['q']).limit_denominator(1000)
    j=(qr-Fr(k*(abs(k)+2),abs(k)+1))/24
    if j.denominator!=1: return None
    j=int(j)
    pts=[(24*j+2*k,4*j)]
    for c in khr:
        if c['type']=='s':
            q=int(round(c['q'])); d=int(round(c['delta']))
            L=int(c['len']) if c['len'] else 4
            if L!=4: return None
            pts.append((q+4,d-1)); pts.append((q-4,d))
    return k,j,pts
def analyse(pts):
    gt=[(q//2+3*d,d,q) for q,d in pts]
    gs=[g for g,d,q in gt]
    width=max(gs)-min(gs)
    byq=collections.defaultdict(list)
    for g,d,q in gt: byq[q].append(g)
    coh=all(len(set(x%2 for x in v))==1 for v in byq.values())
    qmax=max(byq); qmin=min(byq)
    e=lambda v: sum((-1)**(x%2) for x in v)
    return dict(n=len(pts),levels=len(set(d for g,d,q in gt)),width=width,coh=coh,etop=e(byq[qmax]),ebot=e(byq[qmin]),
                puretop=len(set(x%2 for x in byq[qmax]))==1,purebot=len(set(x%2 for x in byq[qmin]))==1)
if __name__=='__main__':
    tot=collections.Counter(); seen=set(); rows=[]
    for fn in sys.argv[1:]:
        for line in open(fn):
            try: r=json.loads(line)
            except: continue
            khr=r.get('khr') or []
            if not khr or not valid(khr): continue
            js=jset(khr)
            if js is None: tot['skipped']+=1; continue
            k,j,pts=js
            if len(pts)==1: continue
            key=(k,j,tuple(sorted(pts)))
            if key in seen: continue
            seen.add(key)
            a=analyse(pts); a['name']=r.get('file') or r.get('knot'); a['k']=k; a['j']=j
            rows.append(a)
    print('distinct nontrivial tangles:',len(rows),dict(tot))
    print('g~ width distribution:',sorted(collections.Counter(a['width'] for a in rows).items()))
    print('sign coherent (no cancellation in J at all):',sum(a['coh'] for a in rows))
    print('END fails (top or bottom Euler zero):',[a['name'] for a in rows if a['etop']==0 or a['ebot']==0])
    print('extreme not parity pure:',[a['name'] for a in rows if not(a['puretop'] and a['purebot'])])
    print('max width examples:',[(a['name'],a['width'],a['n'],a['levels']) for a in sorted(rows,key=lambda a:-a['width'])[:12]])
    nc=[a for a in rows if not a['coh']]
    print('non-coherent width distribution:',sorted(collections.Counter(a['width'] for a in nc).items()))
    print('coherent width distribution:',sorted(collections.Counter(a['width'] for a in rows if a['coh']).items()))
