"""refV3: soundness check of C1's K=3 jet automaton (jauto.py copy) against EXACT Laurent computation: for every normal form with
sum|m_i| <= SMAX (exponents up to SMAX > M = 6, so the clipping m -> +-M is exercised), the automaton's final key must equal the
exact top jet of r = v_2/v_1 (degree + 4 relative coefficients; 'tiny' iff deg r <= -7) and its log-jet of a must equal the exact one."""
import sys, time
sys.dont_write_bytecode=True
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/src')
from fractions import Fraction as Fr
import jauto
from boxlemmas import seqs, Yapply, Eapply, jet, logs
SMAX=int(sys.argv[1]) if len(sys.argv)>1 else 10
K=3
order,trans=jauto.build(K,verbose=True)
def boxv(ms):
    v=({0:1},{})
    for m in ms: v=Eapply(Yapply(v,m))
    return v
def rjet(v1,v2,K):
    # top series of v2/v1: deg, coefficients c_0..c_K (absolute: r = t^d (c0 + c1 u + ...))
    d1=max(v1); l1=v1[d1]
    if not v2: return None
    d2=max(v2)
    # normalised series
    A=[Fr(v1.get(d1-i,0),l1) for i in range(K+1)]
    B=[Fr(v2.get(d2-i,0),l1) for i in range(K+1)]
    # B/A
    C=[]
    for i in range(K+1):
        s=B[i]-sum(C[j]*A[i-j] for j in range(i))
        C.append(s)
    return d2-d1, tuple(C)
t0=time.time(); S=seqs(SMAX); bad=0; n=0
for ms in S:
    key,la=jauto.run(ms,K,trans)
    v1,v2=boxv(ms)
    rj=rjet(v1,v2,K)
    ex_la=logs(jet(v1,'t',3)[2])
    ok=True
    if key=='tiny':
        ok = (rj is None) or rj[0]<=-4-K
    elif key=='init': ok=False
    else:
        d,j=key
        ok = rj is not None and rj[0]==d and tuple(rj[1])==tuple(j)
    if tuple(la)!=tuple(ex_la): ok=False
    n+=1
    if not ok:
        bad+=1
        if bad<5: print('MISMATCH',ms,key,rj,la,ex_la)
print('normal forms %d, automaton-vs-exact mismatches %d, %.1fs'%(n,bad,time.time()-t0))
