#!/usr/bin/env python3
"""Checks for section 4.3: pentagon, l-formula, Pi_w >= 0 (from the closed formula), k-formula (against cached kht++ data)."""
import sys,os,itertools,collections,json,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hull_formula import P,hull
import run as R
def staircase(l): return collections.Counter([(i,-i) for i in range(l+1)]+[(i+1,-i) for i in range(l)])
def divide_square(Pc,l):
    """(P - Z_l)/((1+x)(1+y)) with nonnegative coefficients, or None"""
    d=collections.Counter(Pc); d.subtract(staircase(l))
    if any(v<0 for v in d.values()): return None
    out=collections.Counter()
    for k in sorted(d):          # lexicographic: smallest a, then smallest b
        v=d[k]
        if v==0: continue
        if v<0: return None
        for dk in ((0,0),(1,0),(0,1),(1,1)):
            q=(k[0]+dk[0],k[1]+dk[1])
            if d[q]<v: return None
            d[q]-=v
        out[k]+=v
    return out
bad=collections.Counter(); tot=0
for n in (1,2,3):
    for word in itertools.product(itertools.product(range(1,5),repeat=2),repeat=n):
        tot+=1
        Pc=P(word); A=sum(a for a,b in word); B=sum(b for a,b in word)
        H=set(hull(list(Pc)))
        pent={(0,0),(B,0),(A+B-1,1-A),(A+B-1,-A),(A,-A)}
        if H!=pent: bad['pentagon']+=1
        if any(Pc[v]!=1 for v in pent): bad['vertexcoeff']+=1
        l=sum(a for i,(a,b) in enumerate(word) if sum(bb for aa,bb in word[i:])%2==1)
        # P(-1,y): sum (-1)^a y^b
        ev=collections.Counter()
        for (a,b),c in Pc.items(): ev[b]+=c*(-1)**a
        ev={k:v for k,v in ev.items() if v}
        if ev!={-l:(-1)**l}: bad['l']+=1
        ev2=collections.Counter()
        for (a,b),c in Pc.items(): ev2[a]+=c*(-1)**b
        ev2={k:v for k,v in ev2.items() if v}
        if ev2!={0:1}: bad['x-1']+=1
        if divide_square(Pc,l) is None: bad['Pi<0']+=1
print('positive words checked:',tot,'failures:',dict(bad))
# k formula against cache
C=json.load(open(R.CACHE)); nk=0; badk=0
for key,rec in C.items():
    w=key.split('|')[0]
    body=w[len('s.l1.'):-len('.u2')].split('.')
    if any(t not in ('y0','x1') for t in body): continue
    blocks=[]; i=0
    while i<len(body):
        a=0
        while i<len(body) and body[i]=='y0': a+=1; i+=1
        b=0
        while i<len(body) and body[i]=='x1': b+=1; i+=1
        blocks.append((a,b))
    k=None
    for l_ in rec.get('kh') or []:
        m=re.search(r'\br\(([^)]*)\)',l_)
        if m: k=m.group(1)
    pred=-4*sum(b for i,(a,b) in enumerate(blocks) if sum(aa for aa,bb in blocks[:i+1])%2==1)
    nk+=1
    if str(pred)!=k: badk+=1; print('k mismatch',w,k,pred)
print('k-formula: words',nk,'mismatches',badk)
