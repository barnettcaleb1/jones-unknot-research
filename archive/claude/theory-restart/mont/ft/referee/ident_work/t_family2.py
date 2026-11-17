# Family P(2k,4k-1,4k+1): J from the necklace closure in MATRIX form (lp.apply / lp.star / lp.close; BRIEF Theorem N,
# CHECKED there, not proved), validated against lp.J of the half-word for k = 1, 2.  K-invariants from the half-word's
# symmetric diagram (V_K) for k <= KV, and from a width-6 pretzel Morse diagram (chirality pinned by V equality) for all k.
import sys, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/ident_work')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import refinv as R, words, lp, alex
from t_local import bracket_tokens, divpoly, DELTA
from fractions import Fraction as Fr
def J_matrix(k):
    v1=lp.apply('X'*(2*k-1)+'Y'); v2=lp.apply('X'*(2*k)+'Y')
    return lp.normalize(lp.close(k, lp.star(v1,v2)))
def pretzel_inv(ps,c):
    toks=[('r',0),('l',1),('l',3)]+[(c,0)]*ps[0]+[(c,2)]*ps[1]+[(c,4)]*ps[2]+[('u',3),('u',1),('u',0)]
    B=bracket_tokens(toks); kb=divpoly(B,DELTA); V=R.V_from_bracket(kb); a2,v3,j4=R.vinv(V)
    cr=alex.diagram(toks[1:]); n=len(cr); res=[]
    for p in R.PRIMES:
        xs=list(range(1,n+1)); ys=[]
        for x in xs:
            M,_=alex.alex_matrix(cr,x); ys.append(R.det_mod([r[:-1] for r in M[:-1]],p))
        res.append(R.interp_mod(xs,ys,p))
    Pt=1
    for p in R.PRIMES: Pt*=p
    co=[]
    for i in range(n):
        x=0
        for p,cc in zip(R.PRIMES,res):
            q=Pt//p; x=(x+cc[i]*q*pow(q,p-2,p))%Pt
        co.append(x-Pt if x>Pt//2 else x)
    P={i:cc for i,cc in enumerate(co) if cc}; lo,hi=min(P),max(P); mid=(lo+hi)//2
    P={e-mid:cc for e,cc in P.items()}; s=sum(P.values()); D={e:s*cc for e,cc in P.items()}
    a2c,a4=R.conway_a2a4(D); assert a2c==a2
    return dict(V=V,a2=a2,v3=v3,j4=j4,a4=a4)
KV=int(sys.argv[2]) if len(sys.argv)>2 else 3
for k in range(1,int(sys.argv[1])+1):
    t0=time.time(); w=words.mont(-k,[4*k-1,4*k+1])
    J=J_matrix(k)
    if k<=2: assert J==lp.J(w), 'matrix necklace J != lp.J at k=%d'%k
    if k<=KV:
        Vw=R.VK(w); match=[c for c in 'xy' if pretzel_inv([2*k,4*k-1,4*k+1],c)['V']==Vw]
        assert len(match)==1, match
        cc=match[0]
    inv=pretzel_inv([2*k,4*k-1,4*k+1],cc)
    a2,v3,a4,j4=inv['a2'],inv['v3'],inv['a4'],inv['j4']
    M3,M4=R.mom(J,3),R.mom(J,4)
    D=Fr(M3-432*v3,180); F4=Fr(M4-R.M4loc(a2,a4,j4),1440)
    cf=(v3==Fr(-2*k*(7*k*k-1),3), D==Fr(-2*k*(2*k*k+1),3), M3==-2256*k**3+168*k)
    print('k=%d c=%s a2=%s v3=%s a4=%s j4=%s M3=%s M4=%s D=%s F4=%s closed-forms(v3,D,M3)=%s v3%%5=%s j4%%5=%s M2=%d %.1fs'%(
        k,cc,a2,v3,a4,j4,M3,M4,D,F4,cf,v3%5,j4%5,R.mom(J,2),time.time()-t0),flush=True)
