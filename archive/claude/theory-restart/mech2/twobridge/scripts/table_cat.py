#!/usr/bin/env python3
"""(CAT) data check on the table: letters calculus  P^E_w = (1 0) prod M (1 0)^T with M_Y, M_X, Mt_y, Mt_x;
   test P^E_w = shift * P_N + (1 + x^4/y) R with R >= 0, and collect Newton polygon directions of N, top/bottom multiplicity."""
import sys,os,glob,re,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import chain, run as R
from hull_formula import hull,edges
def mm(p,m): return collections.Counter({(a+m[0],b+m[1]):v for (a,b),v in p.items()})
def add(*ps):
    r=collections.Counter()
    for p in ps:
        for k,v in p.items(): r[k]+=v
    return r
def step(v,L):
    v1,v2=v
    if L=='Y': return v1, add(mm(v1,(1,-1)),mm(v2,(1,-1)))
    if L=='X': return add(v1,v2,mm(v2,(0,1))), mm(v2,(1,0))
    if L=='y': return v1, add(mm(v1,(-4,1)),mm(v2,(-1,1)))
    if L=='x': return add(v1,mm(v2,(3,-1)),mm(v2,(3,0))), mm(v2,(-1,0))
def divide(diff):
    diff=collections.Counter({k:v for k,v in diff.items() if v})
    if any(v<0 for v in diff.values()): return None
    n=0
    for k in sorted(diff, key=lambda k:(k[0])):
        v=diff[k]
        if v==0: continue
        if v<0: return None
        k2=(k[0]+4,k[1]-1)
        if diff.get(k2,0)<v: return None
        diff[k2]-=v; diff[k]=0; n+=v
    return n
base='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/examples/si/'
tot=0; ok=0; dirs=collections.Counter(); topmult=collections.Counter(); mixeddirs=collections.Counter()
for f in sorted(glob.glob(base+'*.kht')):
    nm=os.path.basename(f)[:-4]
    word=open(f).read().split('\n')[1].strip()
    m=re.fullmatch(r's\.[lr]1\.((?:[xy][01]\.)*)u2',word)
    if not m: continue
    fn=base+nm+'/cxBNr-c2-qs'
    if not os.path.exists(fn): continue
    seq=[{'y0':'Y','x0':'y','x1':'X','y1':'x'}[t] for t in m.group(1).split('.') if t]
    v=(collections.Counter({(0,0):1}),collections.Counter())
    for L in seq: v=step(v,L)
    E=v[0]
    rec={'word':nm,'bn':[l for l in open(fn,encoding='utf-8').read().splitlines() if not l.startswith('%')]}
    an=R.analyse(rec); d=collections.Counter(an['N'])
    tot+=1; found=None
    for (a0,b0) in d:
        for (a1,b1) in E:
            s=(a1-a0,b1-b0)
            diff=collections.Counter(E)
            for (a,b),c in d.items(): diff[(a+s[0],b+s[1])]-=c
            r=divide(diff)
            if r is not None: found=r; break
        if found is not None: break
    if found is not None: ok+=1
    else: print('FAIL',nm,word,'dimE',sum(E.values()),'dimN',sum(d.values()))
    td=[k[0]+4*k[1] for k in d.elements()]
    topmult[(td.count(max(td)),td.count(min(td)))]+=1
    for e in set(e[0] for e in edges(hull(list(d)))): dirs[e]+=1
print('entries:',tot,' P^E = shift*N + (1+x^4/y)R with R>=0:',ok)
print('multiplicity of N in (top, bottom) quantum degree:',dict(topmult))
print('hull directions of N:',dict(dirs))
