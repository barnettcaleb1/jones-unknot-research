# Referee: span theorem (claim 3), own implementation.
# For D = (t+1)^a (t-1)^b (t^2+1)(t^2-t+1): every J with D | J-1 and span J < deg D equals t^{-c} R_c, R_c = t^c mod D (deg < deg D).
# (i) brute force spans of R_c for |c| <= 400; (ii) rigorous tail: per residue class mod 12 the coefficients of R_c are
# polynomials in c of degree <= max(a,b)-1; interpolate exactly and find all integer zeros of the top / constant coefficients
# (and of the next ones, to see where span could drop by 2).
import rlib
from rlib import pmul, ppow, Fr
import sympy as sp
def Dab(a,b): return pmul(pmul(ppow(rlib.T1,a),ppow(rlib.TM,b)),pmul(rlib.C4,rlib.C6))
def polymod(p,D):
    """p polynomial (exps >= 0) reduced mod D (monic up to sign)."""
    dg=max(D); lc=D[dg]; r=dict(p)
    while r and max(r)>=dg:
        e=max(r); c=r[e]*lc; s=e-dg
        for f,d in D.items():
            r[f+s]=r.get(f+s,0)-c*d
            if r[f+s]==0: del r[f+s]
    return r
def Rc_table(D,cmin,cmax):
    dg=max(D); d0=D[0]; assert abs(d0)==1
    E={e-1:c for e,c in D.items() if e>0}          # D = t E + d0
    tinv=polymod({e:-d0*c for e,c in E.items()},D)  # t^{-1} = -d0 E mod D
    out={0:{0:1}}
    p={0:1}
    for c in range(1,cmax+1):
        p=polymod(pmul(p,{1:1}),D); out[c]=dict(p)
    p={0:1}
    for c in range(-1,cmin-1,-1):
        p=polymod(pmul(p,tinv),D); out[c]=dict(p)
    return out
def check(name,a,b,C=400):
    D=Dab(a,b); dg=max(D)
    tab=Rc_table(D,-C,C)
    for c,R in tab.items():   # sanity: R = t^c mod D, i.e. D | t^{-c}R - 1
        assert rlib.divmod_laurent(rlib.psub({e-c:v for e,v in R.items()},{0:1}),D) is not None
    spans={}
    for c,R in tab.items():
        J={e-c:v for e,v in R.items()}
        if J=={0:1}: continue
        spans[c]=rlib.span(R)
    mn=min(spans.values())
    small=sorted((s,c) for c,s in spans.items() if s<dg-1)
    # J's attaining small spans (deduplicate: different c can give the same J only if equal as Laurent polys)
    Js={}
    for s,c in small:
        J={e-c:v for e,v in tab[c].items()}
        Js.setdefault(tuple(sorted(J.items())),(s,c))
    # rigorous tail: coefficient k of R_c as polynomial in c on residue classes
    pdeg=max(a,b)-1
    x=sp.symbols('x'); zeros=set()
    for r in range(12):
        xs=[r+12*k for k in range(-4,-4+pdeg+4)]
        for k in list(range(0,3))+list(range(dg-3,dg)):
            ys=[tab[c].get(k,0) for c in xs]
            poly=sp.expand(sp.interpolate(list(zip(xs[:pdeg+1],ys[:pdeg+1])),x))
            assert all(poly.subs(x,xx)==yy for xx,yy in zip(xs,ys)), 'degree assumption fails'
            if poly==0: zeros.add(('IDENT0',r,k)); continue
            for rt in sp.roots(sp.Poly(poly,x)).keys():
                if rt.is_integer and int(rt)%12==r: zeros.add((int(rt),k))
    big=[z for z in zeros if z[0]!='IDENT0' and abs(z[0])>C]
    ident=[z for z in zeros if z[0]=='IDENT0']
    print(name,'deg',dg,'| min span over c in [-%d,%d] (J!=1):'%(C,C),mn)
    print('   J with span < deg-1:',[(s,c,J) for J,(s,c) in sorted(Js.items(),key=lambda kv:kv[1])])
    print('   integer zeros of coefficients k in {0,1,2,deg-3..deg-1} outside window:',big,' identically-zero classes:',ident)
    return spans
for name,(a,b) in (('D7 (F1)',(2,1)),('D8 core',(3,1)),('D8b sigma=0',(2,2)),('D9 core+sigma=0',(3,2))):
    sp_=check(name,a,b)
    if name.startswith('D8 core'):
        bad=[c for c,s in sp_.items() if (c<0 or c>7) and s!=7]
        print('   core: c outside [0,7] with span != 7:',bad)
