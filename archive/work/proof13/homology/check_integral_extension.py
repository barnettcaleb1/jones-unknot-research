"""Signed version of the local extension certificate, using KWZ Remark 9.5.

This is an algebraic integral lift, not a geometric diagram realization.
"""
import runpy
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import json

r=runpy.run_path(str(Path(__file__).with_name('check_extension.py')))
nodes=r['names']; mul=r['mul']; mu=r['mu']
base=[(a,b,c,-1 if (a,b)==('x0','y0') else 1) for a,b,c in r['edges']]
ext=base+[('x1','y3',('I',0,1),-1),('x2','y4',('I',0,1),1)]

def tidy(d): return {k:v for k,v in d.items() if v}
def walk(edges, length):
    ns=sorted(set(a for a,b,c,s in edges)|set(b for a,b,c,s in edges))
    out={n:[] for n in ns}
    for a,b,c,s in edges: out[a].append((b,c,s))
    def go(a,b,labs,sgn):
        if len(labs)==length: yield a,b,labs,sgn
        else:
            for c,lab,s in out[b]: yield from go(a,c,labs+[lab],sgn*s)
    for a in ns: yield from go(a,a,[],1)

def mc(edges):
    total=defaultdict(int)
    for ell in (2,4,6,8,10):
        for a,b,labs,sgn in walk(edges,ell):
            val=mu(labs)
            if val: total[(a,b,val)] += (-1)**(ell//2)*sgn
    return tidy(total)
assert mc(ext)=={}

# Solve the integral B-nullhomotopy equation delta H + H delta = G.
def bd(c):
    a,b,lab=c; ans=defaultdict(int)
    for u,v,d,sgn in base:
        if u==b:
            val=mul(lab,d)
            if val: ans[(a,v,val)] += sgn
        if v==a:
            val=mul(d,lab)
            if val: ans[(u,b,val)] += sgn
    return tidy(ans)
cands=r['candidates']; cols=[bd(c) for c in cands]
G={(n,n,a):sgn for n in nodes for a,sgn in [(('D',1,0),-1),(('S',2,0),1)]}
terms=sorted(set(G).union(*map(set,cols)))
mat=[[Fraction(col.get(t,0)) for col in cols]+[Fraction(G.get(t,0))] for t in terms]
piv=[]; row=0
for col in range(len(cands)):
    where=next((j for j in range(row,len(mat)) if mat[j][col]),None)
    if where is None: continue
    mat[row],mat[where]=mat[where],mat[row]
    z=mat[row][col]; mat[row]=[v/z for v in mat[row]]
    for j in range(len(mat)):
        if j!=row and mat[j][col]:
            z=mat[j][col]; mat[j]=[a-z*b for a,b in zip(mat[j],mat[row])]
    piv.append(col); row+=1
assert all(any(a[:-1]) or not a[-1] for a in mat)
sol=[Fraction(0)]*len(cands)
for j,col in enumerate(piv): sol[col]=mat[j][-1]
assert all(x.denominator==1 for x in sol)
H=[(*c,int(s)) for c,s in zip(cands,sol) if s]
check=defaultdict(int)
for a,b,c,s in H:
    for key,v in bd((a,b,c)).items(): check[key]+=s*v
assert tidy(check)==G

# The twisted-category differential of -H reduces to G. Since all the
# underlying algebra degrees are even and each inserted arrow has odd total
# degree, Remark 9.5 gives the same (-1)^(ell/2) sign for each arity.
def one_h_paths(length):
    out={n:[] for n in nodes}
    for a,b,c,s in ext: out[a].append((b,c,s,0))
    for a,b,c,s in H: out[a].append((b,c,-s,1))
    def go(a,b,labs,sgn,used):
        if len(labs)==length:
            if used==1: yield a,b,labs,sgn
        else:
            for c,lab,s,tag in out[b]:
                if used+tag<=1: yield from go(a,c,labs+[lab],sgn*s,used+tag)
    for a in nodes: yield from go(a,a,[],1,0)
lift=defaultdict(int)
for ell in (2,4,6,8,10):
    for a,b,labs,sgn in one_h_paths(ell):
        val=mu(labs)
        if val: lift[(a,b,val)] += (-1)**(ell//2)*sgn
lift=tidy(lift)
assert {k:v for k,v in lift.items() if k[2][2]==0}==G

cone=[('a'+a,'a'+b,c,-s) for a,b,c,s in ext]
cone += [('b'+a,'b'+b,c,s) for a,b,c,s in ext]
cone += [('a'+a,'b'+b,c,s) for (a,b,c),s in lift.items()]
cone_residue=mc(cone)
assert cone_residue=={}, cone_residue

out={'status':'signed integral module and cone MC checks passed',
     'local_system_sign':'-1, on x0 -> y0',
     'integral_nullhomotopy':H,
     'lifted_G':[(a,b,c,s) for (a,b,c),s in lift.items()],
     'scope':'formal algebraic lift only; no classical diagram'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'])
