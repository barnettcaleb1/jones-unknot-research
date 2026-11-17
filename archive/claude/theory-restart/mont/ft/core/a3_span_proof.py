# Rigorous completion of the span bound: on each residue class c = r mod 12, every coefficient of R_c = (t^c mod D) is a
# polynomial in c of degree <= a-1 (D = (t+1)^a (t-1)^b C', C' = (t^2+1)(t^2-t+1)), because t^c mod (t+1)^a is
# (-1)^c sum_{i<a} C(c,i)(-(t+1))^i and t^c mod (t-1)^b C' is polynomial in c of degree < b on residue classes mod 12.
# We interpolate the top (t^{deg D - 1}) and constant coefficients exactly (Lagrange over Fractions) and list ALL integer c
# where either vanishes; the span can drop below deg D - 1 only there, and we evaluate R_c directly at those c.
import clib, lp
from fractions import Fraction as F
from a2_span import rem, sp
def interp(xs,ys):
    # returns function evaluating the Lagrange interpolant, plus coefficients via solving Vandermonde
    n=len(xs)
    import itertools
    # Newton divided differences
    coef=list(map(F,ys))
    for j in range(1,n):
        for i in range(n-1,j-1,-1):
            coef[i]=(coef[i]-coef[i-1])/(xs[i]-xs[i-j])
    def f(x):
        r=coef[-1]
        for i in range(n-2,-1,-1): r=r*(x-xs[i])+coef[i]
        return r
    return f,coef
def int_roots(f,deg,xs_class,r):
    # brute: integer roots of a polynomial of degree<=deg with rational coeffs: recover coefficients and use rational root bound
    import sympy as sp_
    x=sp_.symbols('x')
    pts=[(xx,f(xx)) for xx in xs_class]
    poly=sp_.interpolate([(sp_.Rational(a),sp_.Rational(b.numerator,b.denominator)) for a,b in pts],x)
    poly=sp_.expand(poly)
    if poly==0: return 'IDENTICALLY ZERO'
    rts=[rr for rr in sp_.roots(sp_.Poly(poly,x)).keys() if rr.is_integer and int(rr)%12==r]
    return [int(rr) for rr in rts]
for name,(a,b) in (('D7',(2,1)),('D8 core',(3,1)),('D8b sigma=0',(2,2)),('D9 core,sigma=0',(3,2))):
    Dp=clib.D(a,b); dg=max(Dp); bad=set()
    pdeg=max(a-1,b-1)
    for r in range(12):
        xs=[r+12*k for k in range(-3,-3+pdeg+3)]   # pdeg+3 sample points (overdetermined check below)
        tops=[rem(c,Dp).get(dg-1,0) for c in xs]; cons=[rem(c,Dp).get(0,0) for c in xs]
        ft,_=interp(xs[:pdeg+1],tops[:pdeg+1]); fc,_=interp(xs[:pdeg+1],cons[:pdeg+1])
        assert all(ft(x)==y for x,y in zip(xs,tops)) and all(fc(x)==y for x,y in zip(xs,cons)), 'not polynomial of expected degree'
        for f in (ft,fc):
            rr=int_roots(f,pdeg,xs,r)
            assert rr!='IDENTICALLY ZERO', (name,r)
            bad.update(rr)
    # evaluate directly at the exceptional c (and confirm the window result)
    spans={c:sp(rem(c,Dp)) for c in sorted(bad)}
    nontriv={c:s for c,s in spans.items() if lp.shift(rem(c,Dp),-c)!={0:1}}
    print(name,'deg',dg,'| exceptional c where top or constant coeff vanishes:',sorted(bad))
    print('    spans there (J != 1):',nontriv, ' generic span:',dg-1)
