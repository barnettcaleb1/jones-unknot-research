# Abstract symbol on equivariant chord diagrams.  A diagram is a token list along the quotient arc k:
#   ('E',i) endpoint of off-axis chord i (twice), ('O',j) on-axis site, ('T',) a non-site on-axis twist (only changes sheets).
# All upstairs signs eps = +1 (W_m(J) = prod eps_i * w(D)).  w(D) = deframed state sum of symbol.py, section 3.2.
import itertools
C_LOOP={0:-1,1:3}
def labels(D):
    pos={}
    for p,tk in enumerate(D):
        if tk[0]=='E': pos.setdefault(tk[1],[]).append(p)
    tau={i:sum(1 for q in range(a+1,b) if D[q][0] in 'OT')%2 for i,(a,b) in pos.items()}
    return pos,tau
def comps(D,choice_off,active):
    L=len(D); adj={}
    def link(u,v): adj.setdefault(u,[]).append(v); adj.setdefault(v,[]).append(u)
    link(('top',),('in',0))
    for p in range(L-1): link(('out',p),('in',p+1))
    link(('out',L-1),('bot',))
    pos,_=labels(D); sm=set()
    for i,ch in choice_off.items():
        a,b=pos[i]
        if ch=='or': link(('in',a),('out',b)); link(('in',b),('out',a))
        else: link(('in',a),('in',b)); link(('out',a),('out',b))
        sm|={a,b}
    for p in range(L):
        if p not in sm: link(('in',p),('out',p))
    seen=set(); loops=[]
    def walk(s):
        st=[s]; seen.add(s); comp=[s]
        while st:
            u=st.pop()
            for v in adj.get(u,[]):
                if v not in seen: seen.add(v); st.append(v); comp.append(v)
        return comp
    walk(('top',))
    for u in list(adj):
        if u not in seen:
            comp=walk(u); loops.append(sum(1 for v in comp if v[0]=='in' and v[1] in active)%2)
    return loops
def W_hat(D,act_off,act_on):
    pos,tau=labels(D)
    twist=set(p for p,tk in enumerate(D) if tk[0]=='T' or (tk[0]=='O'))
    onpos={tk[1]:p for p,tk in enumerate(D) if tk[0]=='O'}
    tot=0
    for co in itertools.product(('or','un'),repeat=len(act_off)):
        for cn in itertools.product(('F','Id'),repeat=len(act_on)):
            coef=1; active=set(twist)
            for i,ch in zip(act_off,co): coef*=-2*((-1)**tau[i])*(1 if ch=='or' else -1)   # eps=+1: kappa*pi = (-1)^tau
            for j,ch in zip(act_on,cn):
                coef*=(1 if ch=='F' else 3)                                               # eps=+1: -kappa = +1
                if ch=='Id': active.discard(onpos[j])
            val=1
            for par in comps(D,dict(zip(act_off,co)),active): val*=C_LOOP[par]
            tot+=coef*val
    return tot
def w(D):
    offs=sorted(set(tk[1] for tk in D if tk[0]=='E')); ons=sorted(set(tk[1] for tk in D if tk[0]=='O'))
    sites=[('E',i) for i in offs]+[('O',j) for j in ons]; m=len(sites); tot=0
    for T in itertools.product([0,1],repeat=m):
        ao=[s[1] for s,b in zip(sites,T) if not b and s[0]=='E']; an=[s[1] for s,b in zip(sites,T) if not b and s[0]=='O']
        tot+=(-4)**sum(T)*W_hat(D,ao,an)
    return tot
def shape(D):
    """canonical description: sequence of site tokens (chords renamed in order of first appearance) + labels."""
    ren={}; seq=[]
    for tk in D:
        if tk[0]=='E':
            if tk[1] not in ren: ren[tk[1]]=len(ren)
            seq.append('c%d'%ren[tk[1]])
        elif tk[0]=='O': seq.append('o')
    _,tau=labels(D)
    lab=tuple(tau[i] for i,_ in sorted(ren.items(),key=lambda kv:kv[1]))
    return ' '.join(seq),lab
def all_diagrams(n_off,n_on):
    """all site sequences with n_off chords, n_on on-axis points, and all sheet-label assignments (via T tokens in gaps)."""
    out={}
    toks=[('E',i) for i in range(n_off) for _ in (0,1)]+[('O',j) for j in range(n_on)]
    for perm in set(itertools.permutations(toks)):
        # canonical: chords appear in order of first endpoint
        first=[tk[1] for tk in perm if tk[0]=='E']; order=[]
        for i in first:
            if i not in order: order.append(i)
        if order!=sorted(order): continue
        onord=[tk[1] for tk in perm if tk[0]=='O']
        if onord!=sorted(onord): continue
        gaps=len(perm)-1
        for par in itertools.product([0,1],repeat=gaps):
            D=[perm[0]]
            for g,tk in zip(par,perm[1:]):
                if g: D.append(('T',))
                D.append(tk)
            sh=shape(D); val=w(D)
            out.setdefault(sh,set()).add(val)
    return out
if __name__=='__main__':
    import sys
    for (no,nn) in [(2,0),(1,1),(0,2)]:
        res=all_diagrams(no,nn)
        print('m=2  off=%d on=%d'%(no,nn))
        for sh,vals in sorted(res.items()): print('   ',sh,vals)
