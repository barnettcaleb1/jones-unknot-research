# Stress test of the Phi_5 part of the doubling congruence: J(-t) = V_K(t^2) mod Phi_5(t) = 1+t+t^2+t^3+t^4.
# Also test the full modulus (t^2-1)(t^3-1)(t^5-1), and look for extra common factors in the core.
import sys, random, itertools, collections
import clib, lp
PHI5={0:1,1:1,2:1,3:1,4:1}
MOD=lp.mul(lp.mul(lp.P((-1,0),(1,2)),lp.P((-1,0),(1,3))),lp.P((-1,0),(1,5)))   # (t^2-1)(t^3-1)(t^5-1)
def rem_mod(f,m):
    if not f: return {}
    lo=min(f); g=lp.shift(f,-lo) if lo<0 else f
    # make polynomial: multiply by t^(-lo) (t is a unit mod m since m(0) != 0)
    q,r=clib.pdiv_poly(g,m)
    # remainder of t^{lo} * r: need inverse of t^{-lo}; just test divisibility of g, since t is a unit
    return r
def test(w,J,stats,core_extra):
    V=clib.VK(w)
    if V is None: return
    f=lp.sub({e:c*(-1)**(e%2) for e,c in J.items()},{2*e:c for e,c in V.items()})
    stats['n']+=1
    if not f: stats['f=0']+=1; return
    stats['Phi5 ok' if not rem_mod(f,PHI5) else 'Phi5 FAIL']+=1
    stats['full ok' if not rem_mod(f,MOD) else 'full FAIL']+=1
mode=sys.argv[1]
stats=collections.Counter(); core_extra=collections.Counter()
if mode=='2br':
    letters=['y0','x0','x1','y1']
    for L in range(1,8):
        for W in itertools.product(letters,repeat=L):
            if any(W[i][1:]==W[i+1][1:] and W[i][0]!=W[i+1][0] for i in range(L-1)): continue
            w='s.l1.'+'.'.join(W)+'.u2'
            J=lp.J(w)
            if J is None: continue
            test(w,J,stats,core_extra)
else:
    rnd=random.Random(int(sys.argv[2])); seen=set()
    while stats['n']<int(sys.argv[3]):
        w,J=clib.randJ(rnd,6,20)
        if w in seen: continue
        seen.add(w); test(w,J,stats,core_extra)
print(mode,dict(stats))
