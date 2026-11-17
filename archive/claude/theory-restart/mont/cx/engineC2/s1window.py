"""E5: S-necklace, all even m with |m| <= MMAX and all N: per box, P(m,N) = sum_{f,g} t^{f m + 3 g N} c_{f,g} (times 1+t^2);
candidates = (m,N) where the top is attained twice (or <= 6); exact test P == +-(1+t^2) Phi3^2."""
import sys, pickle, time, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import fastS, lp, vc, lib
from lp import add, mul, shift, top, bot, span
F,K,Dc=pickle.load(open('Kfreq_Sneck.pkl','rb'))
TARGET=mul(Dc,fastS.PHI3SQ); NTARGET={e:-c for e,c in TARGET.items()}
def coeffs(v):
    a,b=v; at,bt=fastS.tilde(a),fastS.tilde(b)
    aa,ab,ba,bb=mul(a,at),mul(a,bt),mul(b,at),mul(b,bt)
    out=[]
    for k,f in enumerate(F):
        c11,c13,c31,c33=K[0][0][k],K[0][1][k],K[1][0][k],K[1][1][k]
        g0=add(mul(c11,aa) if c11 else {}, mul(c33,bb) if c33 else {})
        if g0: out.append((f,0,g0))
        if c13: out.append((f,1,mul(c13,ab)))
        if c31: out.append((f,-1,mul(c31,ba)))
    return out
def P_at(terms,m,N):
    r={}
    for f,g,c in terms:
        s=f*m+3*g*N
        for e,x in c.items(): r[e+s]=r.get(e+s,0)+x
    return {e:x for e,x in r.items() if x}
def candidates(terms,m,Nmax):
    tops=[(f*m+top(c),g) for f,g,c in terms]
    out=set()
    M={}; cnt={}
    for val,g in tops:
        if g not in M or val>M[g]: M[g]=val; cnt[g]=1
        elif val==M[g]: cnt[g]+=1
    gs=sorted(M)
    # pairwise group ties
    for g1,g2 in itertools.combinations(gs,2):
        num=M[g1]-M[g2]; den=3*(g2-g1)
        if num%den==0: out.add(num//den)
    # internal ties or max <= 6: scan N where that group is the max (bounded)
    for g in gs:
        if cnt[g]>=2 or M[g]<=6+3*Nmax:
            for N in range(-Nmax,Nmax+1):
                vals=[M[h]+3*h*N for h in gs]; mx=max(vals)
                if M[g]+3*g*N==mx and (cnt[g]>=2 or mx<=6): out.add(N)
    return [N for N in out if abs(N)<=Nmax]
def scan(lib_,MMAX,NMAX):
    st={'cand':0,'units':[]}; t0=time.time()
    for key,v,tag in lib_:
        terms=coeffs(v)
        for m in range(-MMAX,MMAX+1,2):
            if m==0: continue
            for N in candidates(terms,m,NMAX):
                st['cand']+=1
                P=P_at(terms,m,N)
                if P==TARGET or P==NTARGET: st['units'].append((tag,m,N))
    return st,time.time()-t0
if __name__=='__main__':
    which=sys.argv[1]; chunk=int(sys.argv[2]); nch=int(sys.argv[3]); MMAX=int(sys.argv[4]); NMAX=int(sys.argv[5])
    if which=='R7': L=[(k,v,str(T)) for k,v,T,tag in lib.rational(7)]
    elif which=='G': L=[(k,v,str(T)) for k,v,T,tag in lib.general()]
    elif which=='P5':
        R5=lib.rational(5); L=[]; seen=set()
        for i in range(len(R5)):
            for j in range(i,len(R5)):
                v,_=lib.canonY(vc.starall([R5[i][1],R5[j][1]]),None); k=lib.vkey(v)
                if k in seen: continue
                seen.add(k); L.append((k,v,'%s*%s'%(R5[i][2],R5[j][2])))
    elif which=='N5':
        R5=lib.rational(5)+lib.general(); L=[]; seen=set()
        for u in R5:
            for kk in [-4,-3,-2,-1,1,2,3,4]:
                for NN in [-2,-1,0,1,2]:
                    try: nd=lib.node(kk,NN,[u])
                    except AssertionError: continue
                    if nd is None or nd[0] in seen: continue
                    seen.add(nd[0]); L.append((nd[0],nd[1],str(nd[2])))
    elif which=='D2':
        D2=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA/d2pos_boxes.pkl','rb'))
        L=[(b[0],b[1],str(b[2])) for b in D2]
    L=L[chunk::nch]
    st,T=scan(L,MMAX,NMAX)
    print(which,chunk,'boxes',len(L),'candidates',st['cand'],'units',len(st['units']),st['units'][:5],'time %.0f'%T,flush=True)
    pickle.dump(st,open('s1w_%s_%d.pkl'%(which,chunk),'wb'))
