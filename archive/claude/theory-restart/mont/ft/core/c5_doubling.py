# Test the "doubling congruence": compare J(-e^h) with V_K(e^{2h}).  k-th coefficient times k!:
#   D_k := M_k(J) - 2^k P_k(V_K),  P_k(V) := sum_e V_e e^k  (moments of V_K at t = 1).
# Report gcd of D_k over samples (and over pairs of inversions of the same K).
import sys, random, math, collections
import clib, lp
rnd=random.Random(int(sys.argv[1])); N=int(sys.argv[2]); KM=8
def P(V,k): return sum(c*e**k for e,c in V.items())
g=[0]*(KM+1); seen=set(); n=0; rows=[]
while n<N:
    w,J=clib.randJ(rnd,6,16)
    if w in seen: continue
    seen.add(w); V=clib.VK(w)
    if V is None: continue
    n+=1
    D=[clib.M(J,k)-2**k*P(V,k) for k in range(KM+1)]
    rows.append(D)
    for k in range(KM+1): g[k]=math.gcd(g[k],D[k])
print('samples',n)
for k in range(KM+1):
    f=sp_f=None
    print('  k=%d  gcd of D_k = M_k - 2^k P_k(V_K): %d   factor: %s   (k!=%d)'%(k,g[k],__import__('sympy').factorint(g[k]) if g[k] else 0, math.factorial(k)))
