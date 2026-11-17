"""Exact ribbon graph and surface-state computation for a virtualized trefoil.

No third-party packages. Integer cohomology is computed in a spanning-tree gauge.
Both ribbon rotation directions are checked as an orientation-reversal audit.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
import json

PD = [(1,4,2,5),(5,3,0,2),(3,1,4,0)]

def nullspace(rows,n):
    a=[[Fraction(x) for x in r] for r in rows]
    piv=[]; k=0
    for j in range(n):
        p=next((i for i in range(k,len(a)) if a[i][j]),None)
        if p is None: continue
        a[k],a[p]=a[p],a[k]
        z=a[k][j]; a[k]=[x/z for x in a[k]]
        for i in range(len(a)):
            if i!=k:
                z=a[i][j]; a[i]=[x-z*y for x,y in zip(a[i],a[k])]
        piv.append(j); k+=1
    result=[]
    for j in range(n):
        if j in piv: continue
        v=[Fraction(0)]*n; v[j]=1
        for i,p in enumerate(piv): v[p]=-a[i][j]
        assert all(x.denominator==1 for x in v),v
        result.append([int(x) for x in v])
    return result

def calculate(rotation):
    darts=list(range(4*len(PD)))
    edges={label:[] for row in PD for label in row}
    for d in darts: edges[PD[d//4][d%4]].append(d)
    assert all(len(ds)==2 for ds in edges.values())
    alpha={a:b for ds in edges.values() for a,b in (ds,ds[::-1])}
    sign={d:1 if d<alpha[d] else -1 for d in darts}
    edge=lambda d:PD[d//4][d%4]
    sigma=lambda d:4*(d//4)+(d%4+rotation)%4
    faces=[]; remaining=set(darts)
    while remaining:
        start=min(remaining); d=start; path=[]; vec=Counter()
        while True:
            remaining.remove(d); path.append(d); vec[edge(d)]+=sign[d]
            d=sigma(alpha[d])
            if d==start:break
        faces.append((path,vec))
    chi=len(PD)-len(edges)+len(faces)
    assert chi==0,chi
    parent=list(range(len(PD)))
    def find(a):
        while parent[a]!=a:a=parent[a]
        return a
    tree=[]
    for e,ds in sorted(edges.items()):
        a,b=(find(d//4) for d in ds)
        if a!=b:parent[a]=b;tree.append(e)
    free=[e for e in sorted(edges) if e not in tree]
    basis=nullspace([[v[e] for e in free] for _,v in faces],len(free))
    assert len(basis)==2,basis
    cocycles=[{e:(v[free.index(e)] if e in free else 0) for e in edges} for v in basis]
    assert all(sum(c[e]*v[e] for e in edges)==0 for c in cocycles for _,v in faces)
    states=[]; surface={}; virtual=Counter()
    for choices in product((0,1),repeat=len(PD)):
        rho={}
        for i,ch in enumerate(choices):
            pairs=[(0,1),(2,3)] if ch==0 else [(0,3),(1,2)]
            for a,b in pairs:rho[4*i+a]=4*i+b;rho[4*i+b]=4*i+a
        unused=set(edges);loops=[]
        while unused:
            d=edges[min(unused)][0];start=d;vec=Counter();path=[]
            while True:
                e=edge(d);unused.remove(e);path.append(d);vec[e]+=sign[d]
                d=rho[alpha[d]]
                if d==start:break
            h=tuple(sum(c[e]*vec[e] for e in edges) for c in cocycles)
            if h<(0,0):h=tuple(-v for v in h)
            loops.append({'path':path,'homology':h})
        essential=tuple(sorted(l['homology'] for l in loops if l['homology']!=(0,0)))
        disks=len(loops)-len(essential)
        shift=len(PD)-2*sum(choices)
        out=surface.setdefault(essential,Counter())
        for j in range(disks+1):out[shift+2*disks-4*j]+=(-1)**disks*comb(disks,j)
        power=len(loops)-1
        for j in range(power+1):virtual[shift+2*power-4*j]+=(-1)**power*comb(power,j)
        states.append({'choices':choices,'A_power':shift,'loops':loops})
    result={'PD':PD,'rotation':rotation,'genus':1,'faces':[p for p,_ in faces],
            'tree_edges':tree,'cohomology_basis':cocycles,'states':states,
            'surface_unreduced':[{'essential_curves':e,'coefficient_A':dict(sorted((a,c) for a,c in v.items() if c))} for e,v in surface.items() if any(v.values())],
            'virtual_reduced':dict(sorted((a,c) for a,c in virtual.items() if c))}
    assert result['virtual_reduced']=={3:-1},result['virtual_reduced']
    return result

if __name__=='__main__':
    results=[calculate(1),calculate(-1)]
    target=Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(results,indent=2)+'\n')
    for r in results:
        print(json.dumps({k:v for k,v in r.items() if k!='states'},indent=2))
