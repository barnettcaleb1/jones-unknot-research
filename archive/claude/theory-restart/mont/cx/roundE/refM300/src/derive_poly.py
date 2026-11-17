"""convert the derived linear case rows (sympy) to pure-Python polynomial data: for each case, each equation, each LP
variable: list of (exponents in (p1,p2,q1,q2,m), Fraction coefficient)."""
import sympy as sp, pickle
from fractions import Fraction as Fr
D=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/derived_linear.pkl','rb'))
p1,p2,q1,q2,m=sp.symbols('p1 p2 q1 q2 m')
NS={k:getattr(sp,k) for k in dir(sp)}
out={}
for nm,lst in D.items():
    out[nm]=[]
    for eqs in lst:
        E=[]
        for e in eqs:
            r={}
            for v,s in e.items():
                ex=sp.expand(eval(s,NS))
                if ex==0: r[v]=[]; continue
                P=sp.Poly(ex,p1,p2,q1,q2,m)
                r[v]=[(tuple(int(x) for x in mon),Fr(int(sp.fraction(c)[0]),int(sp.fraction(c)[1]))) for mon,c in P.terms()]
            E.append(r)
        out[nm].append(E)
pickle.dump(out,open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/derived_poly.pkl','wb'))
print({k:len(v) for k,v in out.items()})
