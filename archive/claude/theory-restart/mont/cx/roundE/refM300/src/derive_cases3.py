"""instantiate the derived linear rows at random rational (p1,p2,q1,q2,m) -> numeric rows (Fractions) for comparison"""
import sympy as sp, pickle, random
from fractions import Fraction as Fr
D=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/derived_linear.pkl','rb'))
p1,p2,q1,q2,m=sp.symbols('p1 p2 q1 q2 m')
random.seed(5)
pts=[]
for i in range(40):
    pt={k:Fr(random.randint(-12,12),random.choice([1,2,3,6])) for k in ('p1','p2','q1','q2','m')}
    if pt['m']==0: pt['m']=Fr(1)
    pts.append(pt)
out=[]
for pt in pts:
    sub={p1:sp.Rational(pt['p1'].numerator,pt['p1'].denominator),p2:sp.Rational(pt['p2'].numerator,pt['p2'].denominator),
         q1:sp.Rational(pt['q1'].numerator,pt['q1'].denominator),q2:sp.Rational(pt['q2'].numerator,pt['q2'].denominator),
         m:sp.Rational(pt['m'].numerator,pt['m'].denominator)}
    rows={}
    for nm,lst in D.items():
        rows[nm]=[]
        for eqs in lst:
            num=[]
            for e in eqs:
                r={}
                for v,s in e.items():
                    val=sp.sympify(eval('sp.'+s) if False else sp.parse_expr(s) if False else sp.sympify(s)) if False else eval(s,{**{k:getattr(sp,k) for k in dir(sp)}})
                    val=sp.nsimplify(val.subs(sub))
                    r[v]=Fr(int(sp.fraction(val)[0]),int(sp.fraction(val)[1]))
                num.append(r)
            rows[nm].append(num)
    out.append((pt,rows))
pickle.dump(out,open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/derived_numeric.pkl','wb'))
print('points',len(out))
