#!/usr/bin/env python3
"""Mixed-sign words: E-polynomial  P^E_w = (1 0) prod Mtilde_L (1 0)^T  with
   M_Y = [[1,0],[u,u]], M_X = [[1,1+y],[0,x]],  Mt_y = [[1,0],[y/x^4, y/x]],  Mt_x = [[1, x^3(1+y)/y],[0,1/x]]
   (positive lifts of the inverse matrices at (x,y)=(-t,-t^4)).  Test: P^E_w - shift*P_N(T_w) = (1 + x^4/y) R, R >= 0."""
import sys,os,re,collections,itertools
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import run as R
import sympy as sp
from matrix_formula import x,y,u,MX,MY,letters,poly_to_counter,data
Mty=sp.Matrix([[1,0],[y/x**4,y/x]]); Mtx=sp.Matrix([[1,x**3*(1+y)/y],[0,1/x]])
MATS={'Y':MY,'X':MX,'y':Mty,'x':Mtx}
def PE(sh):
    v=sp.Matrix([1,0])
    for L in letters(sh): v=MATS[L]*v
    return poly_to_counter(sp.expand(v[0]))
def divide(diff):
    """solve diff = (1 + x^4/y) R with R>=0 : greedy along lines in direction (4,-1)"""
    diff=collections.Counter({k:v for k,v in diff.items() if v})
    if any(v<0 for v in diff.values()): return None
    Rr=collections.Counter()
    for k in sorted(diff, key=lambda k:(k[0])):   # increasing a: lowest end of each (4,-1)-line first
        v=diff[k]
        if v==0: continue
        if v<0: return None
        k2=(k[0]+4,k[1]-1)
        if diff.get(k2,0)<v: return None
        diff[k2]-=v; diff[k]=0; Rr[k]+=v
    if any(v for v in diff.values()): return None
    return Rr
def test(sh):
    d=data(sh)
    if d is None: return 'no data'
    e=PE(sh)
    ne=sum(e.values()); nd=sum(d.values())
    sols=[]
    for (a0,b0) in d:
        for (a1,b1) in e:
            s=(a1-a0,b1-b0)
            diff=collections.Counter(e)
            for (a,b),c in d.items(): diff[(a+s[0],b+s[1])]-=c
            Rr=divide(diff)
            if Rr is not None: sols.append((s,sum(Rr.values())))
    sols=sorted(set(sols))
    return 'dimE=%d dimN=%d  %s'%(ne,nd,('OK shift(s) %s'%sols) if sols else 'FAIL  E=%s N=%s'%(sorted(e.items()),sorted(d.items())))
if __name__=='__main__':
    for w in sys.argv[1:]: print(w,test(w),flush=True)
