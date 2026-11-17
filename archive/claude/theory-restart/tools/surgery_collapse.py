#!/usr/bin/env python3
"""SURGERY COLLAPSE test. For a strongly invertible knot (K,h) with quotient tangle T, the closure T(n) has double cover S^3_n(K).
Compute Kh~(T(n)) (bigraded, via kht++), the largest possible cancellation by differentials of Szabo type
(bidegree (k,2k-2), k>=2: delta drops by one, q rises by 2k-2 >= 2), and compare the resulting minimal rank with rank HF^(S^3_n(K))
from the Ozsvath-Szabo rational surgery formula for a staircase+boxes model of CFK(K).
usage: surgery_collapse.py NAME QUOTIENT_WORD [model]   model e.g. 'stairs=1,1;boxes=0'  (stairs = step lengths of the staircase, K L-space-like orientation)"""
import sys,subprocess,re,os,itertools
K='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++'
W='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/surg'
LINE=re.compile(r'^\s*\d+\)\s+h\^\s*(-?\d+)\s+q\^\s*(-?\d+)\s+δ\^\s*(-?[\d/]+)\s+(\S.*)$')
def closure_gens(name,word):
    f='examples/cl/%s.kht'%name
    d=os.path.join(W,'examples/cl',name)
    p=os.path.join(d,'cxCKh-c2')
    if not os.path.exists(p):
        open(os.path.join(W,f),'w').write('%% %s\n%s\n,1\n'%(name,word))
        try: subprocess.run([K,'-c2',f],cwd=W,capture_output=True,text=True,timeout=600,stdin=subprocess.DEVNULL)
        except subprocess.TimeoutExpired: return None
    if not os.path.exists(p): return None
    gens=[]
    for l in open(p).read().splitlines()[1:]:
        m=LINE.match(l)
        if not m: continue
        h,q,chain=int(m.group(1)),int(m.group(2)),m.group(4)
        gens.append((h,q))
        if 'H' in chain:
            mm=re.search(r'H\^(\d+)',chain); n=int(mm.group(1)) if mm else 1
            gens.append((h+1,q+2*n))
    return gens
def max_matching(gens):
    n=len(gens); adj=[[] for _ in range(n)]
    for i,(h,q) in enumerate(gens):
        for j,(h2,q2) in enumerate(gens):
            k=h2-h
            if k>=2 and q2-q==2*k-2: adj[i].append(j)
    # bipartite by delta parity; delta = q/2 - h ; sources and targets alternate levels; use general augmenting on bipartition by level parity
    match={}
    def lev(i): return gens[i][1]//2-gens[i][0]
    # a vertex can be source (to level-1) or target (from level+1): general graph but bipartite w.r.t. parity of level
    even=[i for i in range(n) if lev(i)%2==0]; 
    und=[[] for _ in range(n)]
    for i in range(n):
        for j in adj[i]: und[i].append(j); und[j].append(i)
    mate=[-1]*n
    def try_aug(u,seen):
        for v in und[u]:
            if v in seen: continue
            seen.add(v)
            if mate[v]==-1 or try_aug(mate[v],seen):
                mate[v]=u; mate[u]=v; return True
        return False
    size=0
    for u in even:
        if try_aug(u,set()): size+=1
    return size
# ---- CFK model: staircase + unit boxes; compute rank H(A^_s), nu
def model_ranks(stairs,boxes):
    """stairs: list of step lengths (alternating horizontal, vertical, starting horizontal) for the L-space orientation; boxes: number of unit boxes.
    returns dict with R(K), nu(K), R(mK), nu(mK), rank HFK^"""
    def hook_R(gens,arrows):
        # gens: list of Alexander gradings; arrows: (src,dst,type) type 'h' or 'v'
        import itertools
        A=[g for g in gens]; R=0
        for s in range(min(A)-1,max(A)+2):
            keep=[(a,b) for (a,b,t) in arrows if (t=='v' and A[a]<=s) or (t=='h' and A[a]>=s)]
            # rank of F2 matrix
            rows={}
            n=len(A); M=[[0]*n for _ in range(n)]
            for a,b in keep: M[b][a]^=1
            rk=0; cols=list(range(n)); Mx=[r[:] for r in M]
            r=0
            for c in range(n):
                piv=next((i for i in range(r,n) if Mx[i][c]),None)
                if piv is None: continue
                Mx[r],Mx[piv]=Mx[piv],Mx[r]
                for i in range(n):
                    if i!=r and Mx[i][c]: Mx[i]=[x^y for x,y in zip(Mx[i],Mx[r])]
                r+=1
            rk=r
            R+=(n-2*rk)-1
        return R
    def build(stairs,mirror):
        # staircase generators x_0..x_m ; L-space orientation: x_1 -> x_0 horizontal length a1, x_1 -> x_2 vertical length a2, ...
        m=len(stairs); gens=[0]*(m+1); arrows=[]
        # Alexander gradings: horizontal arrow x->y of length a: A(y)=A(x)+a ; vertical arrow of length b: A(y)=A(x)-b
        A=[0]*(m+1)
        # odd-indexed generators are sources (L-space) ; x_{2i+1} -> x_{2i} horizontal (len stairs[2i]) and x_{2i+1} -> x_{2i+2} vertical (len stairs[2i+1])
        for i in range(m):
            if i%2==0:  # between x_i and x_{i+1}: horizontal arrow x_{i+1} -> x_i : A(x_i)=A(x_{i+1})+a
                A[i+1]=A[i]-stairs[i]; arrows.append((i+1,i,'h'))
            else:       # vertical arrow x_i -> x_{i+1}: A(x_{i+1})=A(x_i)-b
                A[i+1]=A[i]-stairs[i]; arrows.append((i,i+1,'v'))
        if mirror:
            # mirror: reverse all arrows, negate A, swap h/v
            arrows=[(b,a,t) for (a,b,t) in arrows]; A=[-x for x in A]
        gens=A[:]
        for _ in range(boxes):
            base=len(gens); gens+= [1,0,0,-1]   # a (A=1), b1, b2 (A=0), e (A=-1): a->b1 vertical, a->b2 ... 
            # box: x at A=0 top-right corner? use: p (A=0) -> r (A=1) horizontal, p -> s (A=-1) vertical, r -> w (A=0) vertical, s -> w (A=0) horizontal
            p,r_,s_,w=base+1,base,base+3,base+2
            arrows+=[(p,r_,'h'),(p,s_,'v'),(r_,w,'v'),(s_,w,'h')]
        return gens,arrows
    out={}
    g,a=build(stairs,False); out['R']=hook_R(g,a)
    g2,a2=build(stairs,True); out['Rm']=hook_R(g2,a2)
    tau=sum(stairs[0::2]) if stairs else 0
    # for L-space orientation staircase: tau = genus-like = sum of horizontal steps ; nu = tau ; mirror: tau' = -tau, nu' = tau'+1 if tau>0 else 0
    out['nu']=tau; out['num']=(-tau+1) if tau>0 else 0
    out['rank']=len(stairs)+1+4*boxes
    return out
def hf_rank(n,R,nu):
    # n>0 integer surgery
    return n+2*max(0,2*nu-1-n)+R
if __name__=='__main__':
    name,word=sys.argv[1],sys.argv[2]
    model=None
    if len(sys.argv)>3:
        st,bx=sys.argv[3].split(';')
        stairs=[int(x) for x in st.split('=')[1].split(',') if x]; boxes=int(bx.split('=')[1])
        model=model_ranks(stairs,boxes)
        print('CFK model:',sys.argv[3],model)
    g=closure_gens(name+'_inf',word+'.u1'); print('slope inf closure generators:',g)
    for n in [0,1,2,3,4]:
        for sign,letter in ((1,'y1'),(-1,'x1')):
            if n==0 and sign==-1: continue
            w=word+''.join('.'+letter for _ in range(n))+'.u0'
            gens=closure_gens('%s_%s%d'%(name,'p' if sign>0 else 'm',n),w)
            if gens is None: print('T(%+d): timeout'%(sign*n)); continue
            mm=max_matching(gens)
            levels={}
            for h,q in gens: levels.setdefault(q/2-h,[]).append(q)
            lv=' | '.join('d=%g:%s'%(d,sorted(levels[d])) for d in sorted(levels))
            line='T(%+d): rank Kh~ %d, max Szabo matching %d, minimal E_inf rank %d'%(sign*n,len(gens),mm,len(gens)-2*mm)
            if model and n>0:
                line+='   [HF^ rank of S^3_n(K): %d, of S^3_-n(K): %d]'%(hf_rank(n,model['R'],model['nu']),hf_rank(n,model['Rm'],model['num']))
            print(line); print('      levels: '+lv)
