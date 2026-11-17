"""Exact phase-order tests and numerical normalization checks for finite-level invisibility."""
from fractions import Fraction
from math import lcm, sin, pi
from cmath import exp
import json
from pathlib import Path

levels=[1,2,3,4,5,6,7,8]
R=lcm(*(k+2 for k in levels))
M=4*R
m=2*M+1
checks=[]
for k in levels:
    r=k+2
    qdim=lambda a:sin((a+1)*pi/r)/sin(pi/r)
    for a in range(k+1):
        theta=Fraction(a*(a+2),4*r)
        trace=0j
        channels=list(range(0,min(2*a,2*k-2*a)+1,2))
        for c in channels:
            twist_c=Fraction(c*(c+2),4*r)
            # R^aa_c=(-1)^(a-c/2)*exp(pi*i*(twist_c-2*theta)).
            u=Fraction(a-c//2,2)+(twist_c-4*theta)/2
            assert (2*M*u).denominator==1
            assert ((m-1)*u).denominator==1
            trace+=qdim(c)*exp(2j*pi*float(u))/qdim(a)
        assert abs(trace-1)<1e-12,(k,a,trace)
        checks.append({'level':k,'color':a,'fusion_channels':channels,
                       'unknot_trace_error':abs(trace-1)})
# First fundamental-only period, at each chosen Jones root.
for k in levels:
    r=k+2
    # phase convention uses A=i exp(-pi*i/(2r)); both eigenvalues to 2R are1.
    A=Fraction(1,4)-Fraction(1,4*r)
    lam0=Fraction(1,2)-2*A
    lam2=-6*A
    assert (2*R*lam0).denominator==1
    assert (2*R*lam2).denominator==1
out={'levels':levels,'common_r':R,'all_color_twist_order_bound':M,
     'all_color_invisible_torus_knot':[2,m],
     'fundamental_only_invisible_torus_knot':[2,2*R+1],
     'phase_orders_exact':True,'checks':checks}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({key:val for key,val in out.items() if key!='checks'},indent=2))
print('All',len(checks),'color/level normalizations checked; phase-order assertions exact.')

# Independent polynomial-level check, using the standard T(2,2s+1) Jones formula.
s=60
m_small=2*s+1
V={s:1}
for j in range(2,m_small+1): V[s+j]=(-1)**j
P=dict(V)
P[0]=-1

def remainder(poly, divisor):
    r=dict(poly)
    d=max(divisor)
    while r and max(r)>=d:
        e=max(r)
        c=r[e]
        for j,a in divisor.items():
            index=e-d+j
            r[index]=r.get(index,0)-c*a
            if not r[index]: del r[index]
    return r

for cyclotomic in ({0:1,1:1,2:1},{0:1,2:1},{0:1,1:1,2:1,3:1,4:1}):
    assert remainder(P,cyclotomic)=={}
assert sum(a*(-1)**e for e,a in V.items())==121
assert P
print('Independent Jones-polynomial check: T(2,121) has V=1 at primitive orders3,4,5, but V(-1)=121.')
