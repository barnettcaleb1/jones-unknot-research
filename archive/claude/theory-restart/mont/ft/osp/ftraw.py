# (1) Raw (blackboard) y-coefficients: is D = sum_S (-1)^|S| y_S divisible by (1+A^4)^m?  (integral skein proof of FT)
# (2) h=0 parity-defect model: D/z^m at A_0 = e^{i pi/4} equals y_0(A_0) * Sigma, Sigma = state sum where each off-axis flip site
#     -> eps(vertical - horizontal), each on-axis flip site -> eps((3/2) unwound + (1/2) wound), other crossings -> swap,
#     other x0/y0 -> wound (sigma); closed loops weigh -1 (even winding) or 3 (odd winding) = str((-1)^F), the arc weighs 1.
import sys, random, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, flat_search as fs, alex
from fractions import Fraction as Fr
def padd(p,q,c=1):
    for e,v in q.items():
        nv=p.get(e,0)+c*v
        if nv: p[e]=nv
        else: p.pop(e,None)
def pmul(p,q):
    r={}
    for e,c in p.items():
        for f,d in q.items(): r[e+f]=r.get(e+f,0)+c*d
    return {e:c for e,c in r.items() if c}
def pdiv(p,q):
    if not p: return {}
    p=dict(p); out={}; qt=max(q); qb=min(q); qc=q[qt]
    while p:
        e=max(p)
        if e-qt < min(p)-qb: return None
        c=p[e]
        if c%qc: return None
        k=e-qt; out[k]=c//qc
        for f,d in q.items():
            v=p.get(f+k,0)-out[k]*d
            if v: p[f+k]=v
            else: p.pop(f+k,None)
    return out
def z8(p):   # evaluate Laurent poly in A at zeta_8 -> 4-vector over Q (basis 1,z,z^2,z^3; z^4=-1)
    v=[Fr(0)]*4
    for e,c in p.items():
        r=e%8
        if r<4: v[r]+=c
        else: v[r-4]-=c
    return v
def flip(toks,idx):
    t=list(toks)
    for i in idx: a=t[i]; t[i]=('y' if a[0]=='x' else 'x')+a[1:]
    return '.'.join(t)
def rawy(word):
    if lp.J_raw(word) is None: return None
    y,x=fs.bracket_vector(alex.parse(word))
    return {e:c for e,c in y.items() if c}
# ---- h=0 state sum on single colour-2 strands right of the axis ----
def statesum(word,sites):
    half=alex.parse(word); toks=word.split('.')[1:]   # tokens after 's'
    # map token index (in full token list incl 's') -> position in half
    st={((1,0),(0,0)):Fr(1)}      # (matching, parity); index 0 = T, index p+1 = position p
    def cap(m,par,i):             # insert pair at positions i,i+1 -> indices i+1,i+2
        j=i+1
        m2=[(x+2 if x>=j else x) for x in m]; p2=list(par)
        m2[j:j]=[j+1,j]; p2[j:j]=[0,0]
        return tuple(m2),tuple(p2)
    def cup(m,par,i):             # join positions i,i+1 ; returns (m,par,loopweight or None)
        j=i+1; a,b=m[j],m[j+1]; m=list(m); par=list(par); w=None
        if a==j+1: w=(-1 if par[j]==0 else 3)
        else:
            pp=par[j]^par[j+1]; m[a]=b; m[b]=a; par[a]=pp; par[b]=pp
        del m[j:j+2]; del par[j:j+2]
        m=[(x-2 if x>j+1 else x) for x in m]
        return tuple(m),tuple(par),w
    def swap(m,par,i):            # swap positions i,i+1
        j=i+1; m=list(m); par=list(par)
        a,b=m[j],m[j+1]
        perm=list(range(len(m))); perm[j],perm[j+1]=j+1,j
        m2=[0]*len(m); p2=[0]*len(m)
        for k in range(len(m)): m2[perm[k]]=perm[m[k]]; p2[perm[k]]=par[k]
        return tuple(m2),tuple(p2)
    def tog(m,par):               # sigma on path through position 0 (index 1)
        par=list(par); a=m[1]; par[1]^=1; par[a]^=1
        return m,tuple(par)
    for k,(c,i) in enumerate(half):
        new={}
        def add(key,val):
            new[key]=new.get(key,0)+val
            if new[key]==0: del new[key]
        tk=k+1
        for (m,par),v in st.items():
            if c in 'lr': add(cap(m,par,i-1),v)
            elif c=='u':
                m2,p2,w=cup(m,par,i-1); add((m2,p2),v*(w if w is not None else 1))
            elif i>=1:
                if tk in sites:
                    eps=1 if c=='x' else -1
                    add((m,par),eps*v)
                    m2,p2,w=cup(m,par,i-1); m3,p3=cap(m2,p2,i-1)
                    add((m3,p3),-eps*v*(w if w is not None else 1))
                else: add(swap(m,par,i-1),v)
            else:
                if tk in sites:
                    eps=1 if c=='x' else -1
                    add((m,par),eps*v*Fr(3,2)); add(tog(m,par),eps*v*Fr(1,2))
                else: add(tog(m,par),v)
        st=new
    tot=Fr(0)
    for (m,par),v in st.items():
        assert len(m)==2, m
        tot+=v
    return tot
if __name__=='__main__':
    rnd=random.Random(int(sys.argv[1])); N=int(sys.argv[2]); mode=sys.argv[3] if len(sys.argv)>3 else 'mixed'
    stats={'div':0,'nodiv':0,'zdiv':0,'model_ok':0,'model_bad':0}; done=0; tries=0; bad=[]
    while done<N and tries<50000:
        tries+=1
        w=fs.gen(rnd,rnd.randint(8,16))
        if not w: continue
        toks=w.split('.')
        if mode=='axis': fl=[i for i,a in enumerate(toks) if a in ('x0','y0')]
        elif mode=='off': fl=[i for i,a in enumerate(toks) if a[0] in 'xy' and a[1:]!='0']
        else: fl=[i for i,a in enumerate(toks) if a[0] in 'xy' and a[1:].isdigit()]
        m=rnd.choice([1,2,3,4])
        if len(fl)<m: continue
        sites=rnd.sample(fl,m); ys={}; ok=True
        for S in itertools.product([0,1],repeat=m):
            y=rawy(flip(toks,[s for s,b in zip(sites,S) if b]))
            if y is None: ok=False; break
            ys[S]=y
        if not ok: continue
        done+=1
        D={}
        for S,y in ys.items(): padd(D,y,(-1)**sum(S))
        q=pdiv(D,pmul({0:1},{e:c for e,c in [(0,1)]})) if False else None
        u={}
        u=D
        for _ in range(m):
            u=pdiv(u,{4:1,0:1}) if u is not None else None
        if u is None: stats['nodiv']+=1; bad.append(w); continue
        stats['div']+=1
        zz=D
        for _ in range(m):
            zz=pdiv(zz,{4:1,-4:-1}) if zz is not None else None
        if zz is not None: stats['zdiv']+=1
        lhs=z8(u)                                  # D/(1+A^4)^m at A_0 = 2^m * D/z^m (A_0)
        y0=z8(ys[tuple([0]*m)])
        Sg=statesum(w,set(sites))
        rhs=[2**m*Sg*c for c in y0]
        if lhs==rhs: stats['model_ok']+=1
        else:
            stats['model_bad']+=1
            if len(bad)<5: bad.append((w,sites,lhs,rhs,Sg))
    print('mode',mode,'samples',done,stats)
    for b in bad[:5]: print('  BAD',b)
