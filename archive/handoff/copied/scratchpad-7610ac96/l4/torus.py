import sys
sys.path.insert(0,'$HOME/jones-lanes/theory-restart/tools')
import jq_tangle as jq
import sympy as sp
A=jq.A; t=sp.symbols('t')
w=sp.exp(2*sp.pi*sp.I/3)
from math import gcd
for a,b in [(2,-3),(2,-5),(2,-7),(2,-9),(3,-4),(3,-5),(3,-7),(4,-5),(2,3),(2,5),(3,4)]:
    if gcd(a,b)!=1: continue
    X=jq.add(jq.vert(a),jq.vert(b)); 
    try:
        r=jq.lq(X,-a*b)
    except Exception as e:
        print(a,b,'fail',e); continue
    J=sp.simplify(r['J'].subs(A,t**sp.Rational(-1,4)))
    J=sp.expand(sp.simplify(J))
    val=sp.nsimplify(sp.expand(J.subs(t,w)))
    N=sp.simplify(sp.expand(val*sp.conjugate(val)))
    print((a,b),'J=',sp.factor(J),' N(J(w))=',sp.N(N,8))
