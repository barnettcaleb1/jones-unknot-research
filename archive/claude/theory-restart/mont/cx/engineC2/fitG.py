import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
from gform import *
import sympy as sp
t=sp.symbols('t')
def tosp(p): return sum(c*t**e for e,c in p.items())
def fromsp(ex):
    ex=sp.expand(ex); 
    if ex==0: return {}
    num,den=sp.fraction(sp.together(ex))
    pn=sp.Poly(sp.expand(num),t); pd=sp.Poly(sp.expand(den),t)
    assert len(pd.terms())==1, den
    (dexp,),dc=pd.terms()[0]
    return {m[0]-dexp: int(c/dc) for m,c in pn.terms()}
def fit(top_fn, boxes):
    """top_fn(B) -> W_top; fit G from boxes list of (bodyword, ratword) with known vectors"""
    eqs=[]; G=sp.symbols('g11 g13 g31 g33')
    rows=[]
    for bw,rw in boxes:
        v=vc.rat(rw); R,r0=raw_t(sym.symmetric(top_fn(bw)))
        rows.append((v,R,r0))
    # residues must agree for a common unit
    return rows
def solveG(rows):
    # unknown Laurent polys: use sympy linear solve over Q(t)
    g=sp.symbols('g11 g13 g31 g33')
    eqs=[]
    for v,R,r0 in rows:
        a,b=tosp(v[0]),tosp(v[1]); at,bt=a.subs(t,1/t),b.subs(t,1/t)
        eqs.append(sp.Eq(a*at*g[0]+a*bt*g[1]+b*at*g[2]+b*bt*g[3], tosp(R)))
    sol=sp.solve(eqs[:4],g,dict=True)
    return sol, eqs
if __name__=='__main__':
    boxes=[('', ''),('y0','Y'),('x0','y'),('y0.y0','YY'),('r2.x1.y0.u1','XY'),('r2.y1.x0.u1','xy'),('r2.x1.y0.y0.u1','XYY')]
    for m in [2,-2,4,-4]:
        rows=fit(lambda B: sym.Sneck_top(m,B), boxes)
        print('m',m,'residues',[r[2] for r in rows])
        sol,eqs=solveG(rows[:1]+rows[1:2]+rows[2:3]+rows[4:5])
        if not sol: print(' no solution'); continue
        s=sol[0]
        Gs=[[sp.factor(s[sp.Symbol('g11')]),sp.factor(s[sp.Symbol('g13')])],[sp.factor(s[sp.Symbol('g31')]),sp.factor(s[sp.Symbol('g33')])]]
        print(' G =',Gs)
        # verify on the remaining boxes
        g=sp.symbols('g11 g13 g31 g33')
        okc=0
        for e in eqs[3:]+[solveG([r])[1][0] for r in rows[3:4]+rows[5:]]:
            lhs=e.lhs.subs({g[i]:s[g[i]] for i in range(4)})
            okc+= sp.simplify(lhs-e.rhs)==0
        print(' verified on',okc,'extra boxes (of',len(rows)-4+1,')')
