"""Exact checks for the rank-two skein algebra unit argument (standard library)."""
from collections import defaultdict

def clean(p): return {e:c for e,c in p.items() if c}
def add(p,q):
    r=defaultdict(int,p)
    for e,c in q.items(): r[e]+=c
    return clean(r)
def neg(p):return {e:-c for e,c in p.items()}
def mul(p,q):
    r=defaultdict(int)
    for e,c in p.items():
        for f,d in q.items():r[e+f]+=c*d
    return clean(r)
def shift(p,k,s=1):return {e+k:c*s for e,c in p.items()}
ONE={0:1}; ZERO={}; DELTA={2:-1,-2:-1}
def pairmul(x,y):
    f,g=x; h,k=y
    return mul(f,h),add(add(mul(f,k),mul(g,h)),mul(DELTA,mul(g,k)))
def eigen(x):f,g=x;return f,add(f,mul(DELTA,g))
def power_b(k):
    b=({-1:1},{1:1}) if k>=0 else ({1:1},{-1:1})
    out=(ONE,ZERO)
    for _ in range(abs(k)):out=pairmul(out,b)
    return out

if __name__=='__main__':
    checks=0
    for k in range(-40,41):
        b=power_b(k)
        assert eigen(b)==({-k:1},{3*k:(-1)**k})
        assert pairmul(b,power_b(-k))==(ONE,ZERO)
        for r in range(-8,9):
            for s in (-1,1):
                u=tuple(shift(p,r,s) for p in b)
                v=tuple(shift(p,-r,s) for p in power_b(-k))
                assert pairmul(u,v)==(ONE,ZERO)
                checks+=1
    # A rotated two-crossing rational tangle has an unknot numerator closure,
    # but its bracket is not a unit under horizontal concatenation.
    f,g=power_b(2)[::-1]
    assert (f,g)==({0:1,4:-1},{-2:1})
    assert add(mul(DELTA,f),g)=={6:1}
    assert eigen((f,g))[1]=={4:-1,-4:-1}
    print(f'{checks} exact unit/inverse checks passed; one-closure counterexample verified.')
    # Algebraic tangle T=-1+1/2+1/3, where rotation negates reciprocal.
    t=pairmul(pairmul(power_b(-1),power_b(-2)[::-1]),power_b(-3)[::-1])
    assert t==({2:1,-2:-2,-6:2,-10:-1},{4:1,-8:1,-12:-1})
    assert add(mul(DELTA,t[0]),t[1])==ONE
    q=t[::-1]
    assert pairmul((ZERO,ONE),q)==(ZERO,ONE)
    print('Nonrational algebraic tangle absorption identity e[Q]=e verified.')
