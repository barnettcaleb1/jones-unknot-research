# value-level test: is F4 = (M4 - M4loc)/1440 a polynomial (degree <= 4 in the Vassiliev grading) in the known invariants?
import sys, json, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import lp
import sympy as sp
from fractions import Fraction as F
def N(J,k): return sum(c*e**k for e,c in J.items())
rows=json.load(open('inv_rows5.json'))
for r in rows:
    J=lp.J(r['w']); r['N4']=N(J,4); r['N1']=N(J,1); r['N2']=N(J,2); r['N3']=N(J,3)
    r['F4']=str(F(r['E4'])/1440)
KEYS=['K','Kin','Kout','Uin','Uout']
def val(r,f):
    out=sp.Integer(1)
    for g in f.split('*'): out*=sp.Rational(str(r[g]))
    return out
feats=[k+'.a2' for k in KEYS]+['N2','N1*N1']
feats+=[a+'.a2*'+b+'.a2' for a,b in itertools.combinations_with_replacement(KEYS,2)]
feats+=[k+'.a4' for k in KEYS]+[k+'.j4' for k in KEYS]
feats+=['N4','N1*N3','N2*N2','N1*N1*N2','N1*N1*N1*N1']+['N1*N1*'+k+'.a2' for k in KEYS]+['N2*'+k+'.a2' for k in KEYS]
feats+=['N1*'+k+'.v3' for k in KEYS]+['N1*D','N1*SLin','N1*SLout','N1*SLax']
import modrank
A=[[val(r,f) for f in feats] for r in rows]; b=[val(r,"F4") for r in rows]
print("rows",len(rows),"features",len(feats),"(rank A, rank [A|F4]) mod primes:",modrank.in_span(A,b))
# also M4 itself (sanity: M4 should be in span since M4loc uses K.a2^2, K.a4, K.j4, K.a2 + F4)
