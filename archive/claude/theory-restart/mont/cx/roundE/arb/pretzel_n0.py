"""(4a) vertical n = 0 closures (integral body Y^N; pretzels P(a,q,a) with the vertical inversion):
F = w_1(a) + wV(a) t^-3N with w_1 = t + (1+t^2)(-t)^a, wV = (-t)^a t + t^(3a-1) Phi_5.  Unit <=> F = +-t^e Phi_3.
Exact check of the hand proof (REPORT section 4a) for odd |a| <= 201, |N| <= 300; also lists the a = +-1 units."""
import sys
def add(p,q,s=1):
    r=dict(p)
    for e,c in q.items():
        r[e]=r.get(e,0)+s*c
        if r[e]==0: del r[e]
    return r
def mono(e,c=1): return {e:c}
def F(a,N):
    sa=(-1)**(a%2)  # (-t)^a = sa t^a
    w1=add(mono(1),{a:sa,a+2:sa})
    wV=add({a+1:sa},{3*a-1+i:1 for i in range(5)})
    return add(w1,{e-3*N:c for e,c in wV.items()})
def isunit(f):
    if len(f)!=3: return False
    es=sorted(f); c=set(f.values())
    return es[1]==es[0]+1 and es[2]==es[0]+2 and len(c)==1 and abs(list(c)[0])==1
units=[]; tot=0
for a in range(-201,202,2):
    for N in range(-300,301):
        tot+=1
        if isunit(F(a,N)): units.append((a,N))
print('closures',tot,'units',units)
assert all(abs(a)==1 for a,N in units)
print('OK: no unit with |a| >= 3')
