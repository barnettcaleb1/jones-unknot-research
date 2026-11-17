"""reduce the derived conditions to LINEAR equations in the LP variables (first condition pins A1 or B1), dump as
coefficient dicts (polynomials in p1,p2,q1,q2,m) for comparison with lpgen's case_rows."""
import sympy as sp, pickle
u=sp.symbols('u')
A1,A2,B1,B2,m=sp.symbols('A1 A2 B1 B2 m')
al,P,La,Lam,RA,LA,RB,LB,mB,p1,p2,q1,q2=sp.symbols('al P La Lam RA LA RB LB mB p1 p2 q1 q2')
VARS=[al,P,La,Lam,RA,LA,RB,LB,mB]
def ser(a1,a2,K=3): return sp.series(sp.exp(a1*u+a2*u**2),u,0,K).removeO()
s1=ser(A1,A2); s2=ser(B1,B2)
def coef(e,k): return sp.expand(e).coeff(u,k)
SUB={A1:p1+RA+al, A2:p2+LA+La, B1:q1+RB+al+P, B2:q2+LB+La+Lam}
P0=sp.expand(q1+RB+al+P-(p1+RA+al)-mB)
cases={}
for d in (1,2,3):
    for e in (1,-1):
        for sgn in (1,-1):
            if sgn>0: F=s1+e*u**d*s2; lead=A1
            else: F=s2+e*u**d*s1; lead=B1
            c1=coef(F,1)-1; c2=coef(F,2)-1
            val=sp.solve(c1,lead)[0]                 # pinned first log-coefficient
            c2r=sp.expand(c2.subs(lead,val))
            eqs=[sp.expand((lead-val).subs(SUB)), sp.expand(c2r.subs(SUB)), P0]
            nm=('d=%d'%(sgn*d) if d<3 else ('d>=3' if sgn>0 else 'd<=-3'))+('' if d==3 else ' e=%d'%e)
            cases.setdefault(nm,[]).append(eqs)
# d = 0, r = 0 (e=+1): A1 + B1 = 2 and B1 - A1 = m  -> A1 = 1 - m/2, B1 = 1 + m/2
F=(s1+s2)/2
c1=coef(F,1)-1; c2=coef(F,2)-1
c2r=sp.expand(c2.subs({A1:1-m/2,B1:1+m/2}))
cases['d=0 r=0']=[[sp.expand(c1.subs(SUB)*2), sp.expand(c2r.subs(SUB)), P0.subs(mB,m)]]
# d = 0, r = 1 (e=-1): c2 - c1 = 0 with B1 = A1 + m
G=s1-s2
cond=sp.expand((coef(G,2)-coef(G,1)).subs(B1,A1+m))
cases['d=0 r=1']=[[sp.expand(cond.subs(SUB)), P0.subs(mB,m)]]
def todict(e):
    e=sp.expand(e); out={}
    for v in VARS+[None]:
        if v is None:
            c=e.subs({x:0 for x in VARS})
        else:
            c=sp.expand(e).coeff(v)
            # must be linear: coefficient free of VARS
            assert not (c.free_symbols & set(VARS)), ('nonlinear',e,v,c)
        out[str(v)]=sp.srepr(sp.expand(c))
    return out
dump={nm:[[todict(e) for e in eqs] for eqs in lst] for nm,lst in cases.items()}
pickle.dump(dump,open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/derived_linear.pkl','wb'))
for nm,lst in dump.items(): print(nm,len(lst),'variant(s)')
