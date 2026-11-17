"""E5b: S-necklace COMPLETE in (m,N) per box.  For each even m != 0 with |m| <= M0(box) = 3*Dmax+12 (ray bound),
P(m,N) = E_-1(m) s^-1 + E_0(m) + E_1(m) s, s = t^{3N}: exact Lemma-W candidates in N (all N).  Edge polynomials of the
two m-rays checked nonzero (else flagged)."""
import sys, pickle, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import s1window as W
from lp import top, bot, add, shift
def groups(terms,m):
    E={-1:{},0:{},1:{}}
    for f,g,c in terms:
        s=f*m
        d=E[g]
        for e,x in c.items(): d[e+s]=d.get(e+s,0)+x
    return {g:{e:x for e,x in d.items() if x} for g,d in E.items()}
def Ncands(E):
    out=set(); T={g:(top(p) if p else None) for g,p in E.items()}; B={g:(bot(p) if p else None) for g,p in E.items()}
    if T[1] is not None and T[0] is not None and (T[0]-T[1])%3==0: out.add((T[0]-T[1])//3)
    if T[-1] is not None and T[0] is not None and (T[-1]-T[0])%3==0: out.add((T[-1]-T[0])//3)
    if T[1] is not None and T[-1] is not None and (T[-1]-T[1])%6==0: out.add((T[-1]-T[1])//6)
    if B[1] is not None and B[0] is not None and (B[0]-B[1])%3==0: out.add((B[0]-B[1])//3)
    if B[-1] is not None and B[0] is not None and (B[-1]-B[0])%3==0: out.add((B[-1]-B[0])//3)
    if B[1] is not None and B[-1] is not None and (B[-1]-B[1])%6==0: out.add((B[-1]-B[1])//6)
    lo=-10**6; hi=10**6
    if T[1] is not None: hi=min(hi,(6-T[1])//3)
    if T[-1] is not None: lo=max(lo,-((6-T[-1])//3))
    if hi-lo<400:
        for N in range(lo,hi+1): out.add(N)
    return out
def edge_zero(terms):
    """do the edge pairs (3,-1)&(2,0) or (2,0)&(0,1) (and mirrors) ever cancel identically?"""
    d={(f,g):c for f,g,c in terms}
    flags=[]
    for p,q in [((3,-1),(2,0)),((2,0),(0,1)),((-3,1),(-2,0)),((-2,0),(0,-1))]:
        if p in d and q in d:
            c1,c2=d[p],d[q]
            k=top(c2)-top(c1)
            if add(shift(c1,k),c2)=={} or add(shift(c1,k),{e:-x for e,x in c2.items()})=={}: flags.append((p,q))
    return flags
def run(L):
    st={'cand':0,'units':[],'flag':[],'Mmax':0}; t0=time.time()
    for key,v,tag in L:
        terms=W.coeffs(v)
        Dmax=max(max(abs(top(c)),abs(bot(c))) for f,g,c in terms)
        M0=3*Dmax+12; st['Mmax']=max(st['Mmax'],M0)
        fl=edge_zero(terms)
        if fl: st['flag'].append((tag,fl))
        for m in range(-M0,M0+1,2):
            if m==0: continue
            E=groups(terms,m)
            for N in Ncands(E):
                st['cand']+=1
                P=add(shift(E[-1],-3*N),E[0],shift(E[1],3*N))
                if P==W.TARGET or P==W.NTARGET: st['units'].append((tag,m,N))
    return st,time.time()-t0
if __name__=='__main__':
    import itertools
    sys.argv=[sys.argv[0]]+sys.argv[1:]
    which,chunk,nch=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
    import lib, vc
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
    st,T=run(L)
    print(which,chunk,'boxes',len(L),'max M0',st['Mmax'],'candidates',st['cand'],'units',len(st['units']),st['units'][:4],'edge-zero flags',len(st['flag']),st['flag'][:3],'time %.0f'%T,flush=True)
