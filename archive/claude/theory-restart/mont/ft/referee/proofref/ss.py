# Referee's own implementation: trace the quotient arc k through a half-word; t=-1 state sum W(Jhat), deframing W(J).
import sys, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/proofref')
from common import *
def trace_k(word):
    """Passages of k (top fixed point -> bottom fixed point) through crossing tokens, in order: list of (tok, dir), dir=+1 down."""
    toks=word.split('.'); assert toks[0]=='s'
    edges={}                       # port -> port (edge partner)
    internal={}                    # port -> port (through the node)
    def E(p,q): edges[p]=q; edges[q]=p
    def I(p,q): internal[p]=q; internal[q]=p
    open_=[('S','out')]            # waiting ports (bottom ends) on half-strands 0..w-1
    for n,tk in enumerate(toks[1:],start=1):
        c,s=tk[0],int(tk[1:])
        if c in 'xy' and s>=1:
            E(open_[s-1],(n,'TL')); E(open_[s],(n,'TR')); I((n,'TL'),(n,'BR')); I((n,'TR'),(n,'BL'))
            open_[s-1]=(n,'BL'); open_[s]=(n,'BR')
        elif c in 'xy':
            E(open_[0],(n,'T')); I((n,'T'),(n,'B')); open_[0]=(n,'B')
        elif c in 'lr':
            I((n,'L'),(n,'R')); open_[s-1:s-1]=[(n,'L'),(n,'R')]
        elif c=='u':
            E(open_[s-1],(n,'L')); E(open_[s],(n,'R')); I((n,'L'),(n,'R')); del open_[s-1:s+1]
        else: raise ValueError(tk)
    assert len(open_)==1; E(open_[0],('E','in'))
    out=[]; p=edges[('S','out')]
    while p!=('E','in'):
        n,port=p
        if toks[n][0] in 'xy': out.append((n, +1 if port in ('TL','TR','T') else -1))
        p=edges[internal[p]]
    return out
def chord_data(word, sites):
    toks=word.split('.'); tr=trace_k(word)
    pos={}
    for k,(n,d) in enumerate(tr): pos.setdefault(n,[]).append((k,d))
    axis_slots=set(k for k,(n,d) in enumerate(tr) if toks[n][1:]=='0')
    recs=[]
    for n in sites:
        kap=1 if toks[n][0]=='x' else -1
        if toks[n][1:]=='0':
            assert len(pos[n])==1; recs.append(dict(kind='on',tok=n,c=pos[n][0][0],kap=kap))
        else:
            assert len(pos[n])==2, (word,n,pos[n])
            (a,da),(b,db)=sorted(pos[n]); tau=sum(1 for k in axis_slots if a<k<b)%2
            recs.append(dict(kind='off',tok=n,a=a,b=b,kap=kap,pi=(1 if da==db else -1),tau=tau))
    return recs, len(tr), axis_slots
CL={0:-1,1:3}
def loops_parity(L, axis_slots, recs, choice, active):
    """choice[i] in {'or','un','pass'} for off-axis recs; active: set of on-axis slots counting as twists.
    Returns list of winding parities of closed loops."""
    adj={}
    def lk(u,v): adj.setdefault(u,[]).append(v); adj.setdefault(v,[]).append(u)
    lk('S',('i',0)); lk(('o',L-1),'E')
    for p in range(L-1): lk(('o',p),('i',p+1))
    smoothed=set()
    for r,ch in zip(recs,choice):
        if r['kind']!='off' or ch=='pass': continue
        a,b=r['a'],r['b']; smoothed|={a,b}
        if ch=='or': lk(('i',a),('o',b)); lk(('i',b),('o',a))
        else: lk(('i',a),('i',b)); lk(('o',a),('o',b))
    for p in range(L):
        if p not in smoothed: lk(('i',p),('o',p))
    seen=set(); par=[]
    def comp(s):
        st=[s]; seen.add(s); cc=[]
        while st:
            u=st.pop(); cc.append(u)
            for v in adj[u]:
                if v not in seen: seen.add(v); st.append(v)
        return cc
    comp('S')
    for u in list(adj):
        if u in seen: continue
        cc=comp(u)
        # winding: count active twist slots p whose through-edge (i,p)-(o,p) lies in the loop
        w=sum(1 for p in active if ('i',p) in cc and p not in smoothed)
        par.append(w%2)
    return par
def W_hat(L, axis_slots, recs, idx):
    """W(Jhat) for the sites recs[i], i in idx; other recs passed (off-axis) / twist (on-axis)."""
    tot=0
    opts=[(['or','un'] if recs[i]['kind']=='off' else ['F','Id']) for i in idx]
    for ch in itertools.product(*opts):
        choice=['pass']*len(recs); active=set(axis_slots); coef=1
        for i,c in zip(idx,ch):
            r=recs[i]
            if r['kind']=='off':
                choice[i]=c; coef*=-2*r['kap']*r['pi']*(1 if c=='or' else -1)
            else:
                coef*=-r['kap']*(1 if c=='F' else 3)
                if c=='Id': active.discard(r['c'])
        val=1
        for q in loops_parity(L,axis_slots,recs,choice,active): val*=CL[q]
        tot+=coef*val
    return tot
def n_site(L,axis_slots,recs,i): return W_hat(L,axis_slots,recs,[i])
def W_J(L, axis_slots, recs):
    m=len(recs); n=[n_site(L,axis_slots,recs,i) for i in range(m)]; tot=0
    for T in itertools.product([0,1],repeat=m):
        coef=1
        for i in range(m):
            if T[i]: coef*=-n[i]
        tot+=coef*W_hat(L,axis_slots,recs,[i for i in range(m) if not T[i]])
    return tot, n
