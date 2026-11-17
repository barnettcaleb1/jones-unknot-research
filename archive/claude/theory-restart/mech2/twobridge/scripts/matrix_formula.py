#!/usr/bin/env python3
"""Conjectured closed formula for N(T_w), w = Y^{a1} X^{b1} ... (two-bridge quotient, kht++ word s.l1.y0^a1.x1^b1...u2):
   P_w(x,y) = (1 0) M_X^{bn} M_Y^{an} ... M_X^{b1} M_Y^{a1} (1 0)^T,   M_Y = [[1,0],[u,u]],  M_X = [[1,1+y],[0,x]],  u = x/y.
Compare with kht++ data (cached)."""
import sys,os,re,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import run as R
import sympy as sp
x,y=sp.symbols('x y')
u=x/y
MY=sp.Matrix([[1,0],[u,u]]); MX=sp.Matrix([[1,1+y],[0,x]])
MYm=MY.subs({x:1/x,y:1/y},simultaneous=True); MXm=MX.subs({x:1/x,y:1/y},simultaneous=True)
def letters(sh):
    out=[]
    for m in re.finditer(r'([YyXx])(\d*)',sh):
        n=int(m.group(2)) if m.group(2) else 1
        out+=[m.group(1)]*n
    return out
def formula(sh,mats=None):
    mats=mats or {'Y':MY,'X':MX,'y':MYm,'x':MXm}
    v=sp.Matrix([1,0])
    for L in letters(sh): v=mats[L]*v
    return sp.expand(v[0])
def poly_to_counter(p):
    p=sp.expand(p); c=collections.Counter()
    for term in sp.Add.make_args(p):
        co,mon=term.as_coeff_Mul()
        d=mon.as_powers_dict()
        c[(int(d.get(x,0)),int(d.get(y,0)))]+=int(co)
    return c
def data(sh,timeout=120):
    rec=R.run(sh,timeout)
    if rec.get('bn') is None: return None
    an=R.analyse(rec)
    return collections.Counter(an['N'])
def compare(sh):
    d=data(sh)
    if d is None: return 'no data'
    f=poly_to_counter(formula(sh))
    if f==d: return 'MATCH'
    # allow overall shift
    for (a0,b0) in f:
        for (a1,b1) in d:
            sh_=(a1-a0,b1-b0)
            if collections.Counter({(a+sh_[0],b+sh_[1]):c for (a,b),c in f.items()})==d: return 'MATCH up to shift %s'%(sh_,)
    return 'DIFFER: formula %s  data %s'%(sorted(f.items()),sorted(d.items()))
if __name__=='__main__':
    for w in sys.argv[1:]:
        print(w,compare(w),flush=True)
