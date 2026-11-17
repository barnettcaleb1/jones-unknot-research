"""refV3 test (i): EXHAUSTIVE search for unit J among vertical closures V_a(Y^N u_1...u_n) = s.l1.(y0)^N.B(u_1)...B(u_n).(x2)^a.u1,
u_i in R(6) (98 canonical non-integral rational boxes, multisets), n = 1..4, every odd a in [-9,9], every N in [-12,12].
NO Lemma W: every (multiset, a, N) is tested.  Test = necessary condition for J = +-t^e evaluated exactly mod two primes:
   F(t0) := w_1(a)(t0) A(t0) + wV(a)(t0) t0^(-3N) B(t0)  must equal  +- t0^e Phi_3(t0)  (mod p)   [J Phi_3 = F, Theorem V]
(p,t0) = (2^31-1, 2) [ord 31] and (2^19-1, 2) [ord 19].  Survivors are re-tested with exact Laurent arithmetic; exact units are
then evaluated with lp.J on the explicit half-word and K is tested (det, |Delta(2)|, |Delta(3)|).
For n <= 2 the EXACT J is also computed for every case (span statistics / near misses)."""
import sys, time, itertools, pickle
sys.dont_write_bytecode=True
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/src')
import numpy as np
import vc, lib
OUT='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/'
NMAX=int(sys.argv[1]) if len(sys.argv)>1 else 4
AS=list(range(-9,10,2)); NS=list(range(-12,13))
R6=lib.rational(6)
print('R(6) boxes:',len(R6),flush=True)
PR=[(2**31-1,2),(2**19-1,2)]
def evp(poly,t0,p):
    inv=pow(t0,p-2,p); s=0
    for e,c in poly.items():
        s=(s+c*(pow(t0,e,p) if e>=0 else pow(inv,-e,p)))%p
    return s%p
def w1(a): return vc.add({1:1}, vc.mul(vc.tmono(a),vc.T2P1))
def wV(a): return vc.add(vc.shift(vc.tmono(a),1), vc.shift(vc.PHI5,3*a-1))
data=[]
for p,t0 in PR:
    av=np.array([evp(b[1][0],t0,p) for b in R6],dtype=np.int64)
    bv=np.array([evp(b[1][1],t0,p) for b in R6],dtype=np.int64)
    inv=pow(t0,p-2,p)
    cA={a:evp(w1(a),t0,p) for a in AS}
    cB={(a,N):(evp(wV(a),t0,p)*pow(inv,3*N,p) if N>=0 else evp(wV(a),t0,p)*pow(t0,-3*N,p))%p for a in AS for N in NS}
    inv7=pow(7,p-2,p)
    pw=set(); x=1
    for e in range(200):
        pw.add(x); pw.add((p-x)%p); x=x*t0%p
    data.append(dict(p=p,av=av,bv=bv,cA=cA,cB=cB,inv7=inv7,pw=np.array(sorted(pw),dtype=np.int64)))
def unit_mask(D,A,B,a,N):
    p=D['p']
    F=((D['cA'][a]*A)%p + (D['cB'][(a,N)]*B)%p)%p
    x=(F*D['inv7'])%p
    return np.isin(x,D['pw'])
surv=[]; counts={}
t0=time.time()
nb=len(R6)
for n in range(1,NMAX+1):
    tested=0
    for i1 in range(nb):
        if n==1: combos=np.array([[i1]],dtype=np.int64)
        else:
            rest=np.array(list(itertools.combinations_with_replacement(range(i1,nb),n-1)),dtype=np.int64)
            combos=np.concatenate([np.full((len(rest),1),i1,dtype=np.int64),rest],axis=1)
        prods=[]
        for D in data:
            p=D['p']; A=np.ones(len(combos),dtype=np.int64); B=np.ones(len(combos),dtype=np.int64)
            for j in range(n):
                A=(A*D['av'][combos[:,j]])%p; B=(B*D['bv'][combos[:,j]])%p
            prods.append((A,B))
        for a in AS:
            for N in NS:
                m=unit_mask(data[0],prods[0][0],prods[0][1],a,N)
                if m.any():
                    m&=unit_mask(data[1],prods[1][0],prods[1][1],a,N)
                    for r in np.nonzero(m)[0]: surv.append((n,tuple(int(x) for x in combos[r]),a,N))
                tested+=len(combos)
    counts[n]=tested
    print('n=%d tested %d (multiset,a,N); survivors so far %d; %.1fs'%(n,tested,len(surv),time.time()-t0),flush=True)
# exact re-test of survivors
PHI3={0:1,1:1,2:1}
exact_units=[]
for (n,cmb,a,N) in surv:
    p=vc.Ypow(N,vc.starall([R6[i][1] for i in cmb]))
    J=vc.raw_vert(a,p)
    if len(J)==1: exact_units.append((n,cmb,a,N,J))
print('mod-p survivors:',len(surv),' exact units:',len(exact_units),flush=True)
byna={}
for (n,cmb,a,N,J) in exact_units: byna[(n,a)]=byna.get((n,a),0)+1
print('exact units by (n,a):',byna,flush=True)
pickle.dump(dict(counts=counts,surv=surv,exact_units=exact_units,R6keys=[b[0] for b in R6]),open(OUT+'brute_n%d.pkl'%NMAX,'wb'))
print('done %.1fs'%(time.time()-t0))
