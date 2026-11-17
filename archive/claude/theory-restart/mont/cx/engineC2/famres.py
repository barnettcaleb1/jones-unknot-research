"""t = -1 resonance test for symmetric twist families: top half = PREFIX + W1 + (x)^{2k} + W2 + slot box (A_l, k1).
Fit (1+t^2)-scaled frequency components K_f, f in -3..3 (twist eigenvalues 1, -t, t^3), on k in {0,+-1,+-2,+-3}, verify on
k = +-4; then for every hull edge of the exponent set {(f,g)} (g = power of t^{3N}) test whether the edge relation can vanish
at t = -1 for a box (channel values a(-1) = 1, b(-1) = eps = +-1; t^{3N} -> (-1)^N)."""
import sys, pickle, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import sympy as sp
import gtable, plat2, sym
from gtable import tosp, fromsp
t=sp.symbols('t')
def fitfam(W1,x,W2):
    G={}
    for k in [0,1,-1,2,-2,3,-3,4,-4]:
        tw=(x*(2*k)) if k>=0 else (plat2.INVL[x]*(-2*k))
        w=W1+tw+W2
        if not plat2.is_arc(w): return None
        g=gtable.Ghat(lambda B: plat2.top_events(w)+sym.body(B,0))
        if g is None or isinstance(g,tuple): return None
        G[k]=g
    F=list(range(-3,4)); K=[[None,None],[None,None]]
    for i in range(2):
        for j in range(2):
            xs=sp.symbols('x0:7')
            eqs=[sum(xs[q]*t**(F[q]*2*k) for q in range(7))-tosp(G[k][i][j]) for k in [0,1,-1,2,-2,3,-3]]
            sol=sp.solve(eqs,xs,dict=True)[0]
            K[i][j]=[sp.factor(sol[xs[q]]) for q in range(7)]
            for k in [4,-4]:
                assert sp.simplify(sum(K[i][j][q]*t**(F[q]*2*k) for q in range(7))-tosp(G[k][i][j]))==0
    return F,K
def hull(points):
    pts=sorted(set(points))
    def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[];up=[]
    for p in pts:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0: lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(up)>=2 and cross(up[-2],up[-1],p)<=0: up.pop()
        up.append(p)
    return lo[:-1]+up[:-1]
def test(F,K):
    # terms: (f,g) -> function of (eps, Npar) at t=-1, and symbolic coefficient
    terms={}
    for q,f in enumerate(F):
        k11,k13,k31,k33=[K[i][j][q] for i,j in [(0,0),(0,1),(1,0),(1,1)]]
        if k11!=0 or k33!=0: terms[(f,0)]=(k11,k33)
        if k13!=0: terms[(f,1)]=k13
        if k31!=0: terms[(f,-1)]=k31
    H=hull(list(terms))
    res=[]
    for i in range(len(H)):
        p,q=H[i],H[(i+1)%len(H)]
        on=[pt for pt in terms if (q[0]-p[0])*(pt[1]-p[1])-(q[1]-p[1])*(pt[0]-p[0])==0 and min(p[0],q[0])<=pt[0]<=max(p[0],q[0]) and min(p[1],q[1])<=pt[1]<=max(p[1],q[1])]
        if p[0]==q[0]: res.append((p,q,'fixed-f edge (N-ray at fixed m): Lemma W per m')); continue
        # value at t=-1 of each term for eps=+-1, N parity: t^{fm} -> 1 (m even), t^{3gN} -> (-1)^{gN}; arbitrary integer shift t^c -> (-1)^c
        possible=False
        for eps in (1,-1):
            for signs in itertools.product((1,-1),repeat=len(on)):
                tot=0
                for s,pt in zip(signs,on):
                    f,g=pt; c=terms[pt]
                    if g==0: val=c[0].subs(t,-1)+c[1].subs(t,-1)*eps*eps
                    else: val=c.subs(t,-1)*eps
                    tot+=s*val
                if sp.simplify(tot)==0: possible=True
        res.append((p,q,'RESONANCE POSSIBLE at t=-1' if possible else 'excluded at t=-1 (|values| mismatch)'))
    return H,res
if __name__=='__main__':
    fams=[('','a',''),('','b',''),('d','a',''),('','a','d'),('a','b',''),('ab','a',''),('','a','bD'),('D','b','A'),('aD','a',''),('','b','ad')]
    for W1,x,W2 in fams:
        r=fitfam(W1,x,W2)
        if r is None: print(W1,x,W2,'skip (loop or fit failed)'); continue
        F,K=r
        H,res=test(F,K)
        print('family %s.(%s)^2k.%s  hull'%(W1,x,W2),H)
        for e in res: print('    edge',e)
