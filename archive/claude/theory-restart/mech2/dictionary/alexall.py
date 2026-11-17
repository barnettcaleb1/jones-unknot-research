import json,sys,os
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from fractions import Fraction as Fr
import alex
def rawdet(word,t):
    full=alex.symmetrize(alex.parse(word)); cr=alex.diagram(full)
    if cr is None: return None
    if not cr: return 1
    M,w=alex.alex_matrix(cr,t)
    m=[r[:-1] for r in M[:-1]]
    return alex.bareiss(m)
def interp(xs,ys):
    # Newton interpolation -> coefficients (Fractions), low to high
    n=len(xs)
    coef=[Fr(y) for y in ys]
    for j in range(1,n):
        for i in range(n-1,j-1,-1):
            coef[i]=(coef[i]-coef[i-1])/(xs[i]-xs[i-j])
    # convert Newton form to monomial
    poly=[Fr(0)]*n
    for i in range(n-1,-1,-1):
        # poly = poly*(x - xs[i]) + coef[i]
        new=[Fr(0)]*n
        for d in range(n-1):
            new[d+1]+=poly[d]
            new[d]-=poly[d]*xs[i]
        new[0]+=coef[i]
        poly=new
    return poly
def alex_coeffs(word):
    full=alex.symmetrize(alex.parse(word)); cr=alex.diagram(full)
    n=len(cr)+2
    xs=list(range(2,2+n)); ys=[rawdet(word,x) for x in xs]
    p=interp(xs,ys)
    assert all(c.denominator==1 for c in p)
    co=[int(c) for c in p]
    while co and co[-1]==0: co.pop()
    while co and co[0]==0: co.pop(0)
    if sum(co)==-1: co=[-c for c in co]
    assert sum(co)==1,(word,co)
    assert co==co[::-1],(word,co)
    return co
if __name__=='__main__':
    S='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/examples/si'
    out={}
    for f in sorted(os.listdir(S)):
        if not f.endswith('.kht'): continue
        word=open(os.path.join(S,f)).read().splitlines()[1].strip()
        out[f[:-4]]=dict(word=word,alex=alex_coeffs(word))
    json.dump(out,open('alex.json','w'))
    print(len(out)); print({k:out[k]['alex'] for k in ['3_1','4_1-1','5_1','5_2-1','8_19','9_42','9_46-1','9_46-2']})
