# Laurent polynomials in A as dict exponent->coeff
def add(p,q):
    r=dict(p)
    for k,v in q.items(): r[k]=r.get(k,0)+v
    return {k:v for k,v in r.items() if v!=0}
def mul(p,q):
    r={}
    for a,x in p.items():
        for b,y in q.items(): r[a+b]=r.get(a+b,0)+x*y
    return {k:v for k,v in r.items() if v!=0}
def mono(e,c=1): return {e:c}
delta=add(mono(2,-1),mono(-2,-1))   # -A^2 - A^-2
# tangle bracket vector (a,b) meaning a<0> + b<inf>; unknot normalized to 1
def tsum(T,S):
    a,b=T; c,d=S
    return (mul(a,c), add(add(mul(a,d),mul(b,c)), mul(mul(b,d),delta)))
def rot(T): return (T[1],T[0])
one=(mono(1),mono(-1)); mone=(mono(-1),mono(1))
def integ(n):
    T=({0:1},{}) if n==0 else None
    base=one if n>0 else mone
    T=({0:1},{})
    for _ in range(abs(n)): T=tsum(T,base)
    return T
def frac_inv(n): return rot(integ(-n))   # <1/n> = R(<-n>)
def N(T): return add(mul(T[0],delta),T[1])
def D(T): return add(T[0],mul(T[1],delta))
def show(p): return ' + '.join(f"{v}A^{k}" for k,v in sorted(p.items())) or '0'
import cmath
def ev(p,z): return sum(v*z**k for k,v in p.items())
X=tsum(frac_inv(3),frac_inv(-3))
z=cmath.exp(1j*cmath.pi/4)
print("[N(X)] =",show(N(X)),"  |at e^{i pi/4}| =",round(abs(ev(N(X),z)),6))
print("[N(<0>)] =",show(N(({0:1},{}))))
print("[D(X)] =",show(D(X)),"  det =",round(abs(ev(D(X),z)),6))
# ratio N(X)/delta if divisible
print("N(X) == unit*delta ?", [ (k, N(X)==mul(mono(k,s),delta)) for k in range(-12,13) for s in (1,-1) if N(X)==mul(mono(k,s),delta)])
# square knot check: D(<1/3>) bracket times D(<-1/3>) bracket
print("[D(<1/3>)]*[D(<-1/3>)] =",show(mul(D(frac_inv(3)),D(frac_inv(-3)))))
