"""Exact table of Ghat(m) = Phi3^2 * G(m) for a symmetric 2-slot special region, from 4 test boxes."""
import sys, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
from gform import *
import sympy as sp
t=sp.symbols('t')
def tosp(p): return sum(c*t**e for e,c in p.items())
def fromsp(ex):
    ex=sp.cancel(sp.expand(ex))
    if ex==0: return {}
    num,den=sp.fraction(ex)
    pn=sp.Poly(sp.expand(num),t); pd=sp.Poly(sp.expand(den),t)
    assert len(pd.terms())==1, ('nonmonomial denominator',den)
    (dexp,),dc=pd.terms()[0]
    out={}
    for (e,),c in pn.terms():
        assert (c/dc).is_integer
        out[e-dexp]=int(c/dc)
    return out
TEST=[('','',(1,1)),('y0','Y',None),('x0','y',None),('r2.x1.y0.u1','XY',None)]
def Ghat(top_fn):
    vals=[]
    for bw,rw,_ in TEST:
        v=vc.rat(rw); res=raw_t(sym.symmetric(top_fn(bw)))
        if res is None: return None
        R,r0=res; vals.append((v,R,r0))
    if len(set(r[2] for r in vals))!=1: return ('residue clash',[r[2] for r in vals])
    g=sp.symbols('g11 g13 g31 g33'); eqs=[]
    for v,R,_ in vals:
        a,b=tosp(v[0]),tosp(v[1]); at,bt=a.subs(t,1/t),b.subs(t,1/t)
        eqs.append(a*at*g[0]+a*bt*g[1]+b*at*g[2]+b*bt*g[3]-tosp(R))
    sol=sp.solve(eqs,g,dict=True)[0]
    P3=(1+t+t**2)**2
    return [[fromsp(sol[g[0]]*P3),fromsp(sol[g[1]]*P3)],[fromsp(sol[g[2]]*P3),fromsp(sol[g[3]]*P3)]]
if __name__=='__main__':
    tab={}
    for m in range(-12,13,2):
        G=Ghat(lambda B: sym.Sneck_top(m,B)); tab[m]=G
        print(m,[[ (lp.bot(x),lp.top(x)) if x else None for x in row] for row in G], flush=True)
    pickle.dump(tab,open('Gtab_Sneck.pkl','wb'))
