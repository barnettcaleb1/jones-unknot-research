# The symbol W_m: chord-diagram extraction from half-words, the t = -1 state sum, deframing, and comparison with lp.J.
# Conventions: t = A^-4 (TH-2BR); lp's variable is t' = 1/t, so W^(t)_m = (-1)^m [Delta^m J/(1+t')^m](t'=-1).
import sys, random, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, flat_search as fs, alex
C_LOOP={0:-1,1:3}          # loop factor at t=-1: even winding -> -1 (= Delta_2(-1)), odd winding -> 3
def trace(word):
    """Trace the quotient arc k through the half-word. Returns dict token_index -> list of (visit_no, direction) and the
    ordered list of on-axis token indices visited. direction: +1 = passing downward (top port -> bottom port), -1 upward."""
    toks=word.split('.'); assert toks[0]=='s'
    segs=[]            # seg = [top_end, bot_end], end = (node, port)
    def newseg(top): segs.append([top,None]); return len(segs)-1
    nodes={}           # node -> (kind, token index)
    pos=[newseg(('top','p'))]; nodes['top']=('top',None)
    for n,tk in enumerate(toks[1:],start=1):
        c,s=tk[0],int(tk[1:])
        N=('n',n)
        if c in 'xy' and s>=1:
            a,b=pos[s-1],pos[s]; segs[a][1]=(N,'tl'); segs[b][1]=(N,'tr')
            pos[s-1]=newseg((N,'bl')); pos[s]=newseg((N,'br')); nodes[N]=('cross',n)
        elif c in 'xy':
            a=pos[0]; segs[a][1]=(N,'t'); pos[0]=newseg((N,'b')); nodes[N]=('axis',n)
        elif c in 'lr':
            e1=newseg((N,'l')); e2=newseg((N,'r')); pos[s-1:s-1]=[e1,e2]; nodes[N]=('cap',n)
        elif c=='u':
            a,b=pos[s-1],pos[s]; segs[a][1]=(N,'l'); segs[b][1]=(N,'r'); del pos[s-1:s+1]; nodes[N]=('cup',n)
    assert len(pos)==1; segs[pos[0]][1]=('bot','p')
    pair={'tl':'br','br':'tl','tr':'bl','bl':'tr','t':'b','b':'t','l':'r','r':'l'}
    ends={}
    for i,(tp,bt) in enumerate(segs): ends[tp]=(i,0); ends[bt]=(i,1)
    visits={}; axis_order=[]; k=0
    cur,side=0,0          # on segment 0, entered at its top end (side 0), move to the other end
    while True:
        node,port=segs[cur][1-side]
        if node=='bot': break
        kind,n=nodes[node]
        if kind in ('cross','axis'):
            down=(port in ('tl','tr','t'))
            visits.setdefault(n,[]).append((k,1 if down else -1)); k+=1
            if kind=='axis': axis_order.append(n)
        op=pair[port]; cur,side=ends[(node,op)]
    return visits
def chord_data(word,sites):
    """sites: token indices. Returns list of site records and the arc length; on-axis tokens give winding."""
    toks=word.split('.'); vis=trace(word)
    L=1+max(v for lst in vis.values() for v,_ in lst)
    axis_pos={vis[n][0][0]:n for n in vis if toks[n][1:]=='0'}   # arc position -> token, for every on-axis letter
    recs=[]
    for n in sites:
        tk=toks[n]; kap=1 if tk[0]=='x' else -1
        if tk[1:]=='0':
            recs.append(dict(kind='on',tok=n,c=vis[n][0][0],kap=kap))
        else:
            (a,da),(b,db)=sorted(vis[n]); pi=1 if da==db else -1
            recs.append(dict(kind='off',tok=n,a=a,b=b,kap=kap,pi=pi))
    return recs,L,axis_pos
def components(L,recs,choice,active_axis):
    """1-manifold after smoothing the off-axis sites by choice ('or'/'un'); returns winding parities of the closed loops.
    Arc positions 0..L-1 are visit slots; half-edges: ('in',p), ('out',p). Segments join ('out',p) -> ('in',p+1) (and top/bottom)."""
    adj={}
    def link(u,v): adj.setdefault(u,[]).append(v); adj.setdefault(v,[]).append(u)
    link(('top',),('in',0))
    for p in range(L-1): link(('out',p),('in',p+1))
    link(('out',L-1),('bot',))
    sm={}
    for r,ch in zip(recs,choice):
        if r['kind']!='off': continue
        a,b=r['a'],r['b']
        if ch=='or': link(('in',a),('out',b)); link(('in',b),('out',a))
        else: link(('in',a),('in',b)); link(('out',a),('out',b))
        sm[a]=sm[b]=1
    for p in range(L):
        if p not in sm: link(('in',p),('out',p))   # pass straight through every non-smoothed slot
    # winding: slot p contributes 1 if it is an active on-axis twist; count on loops
    seen=set(); loops=[]
    def walk(start):
        comp=[]; stack=[start]; seen.add(start)
        while stack:
            u=stack.pop(); comp.append(u)
            for v in adj.get(u,[]):
                if v not in seen: seen.add(v); stack.append(v)
        return comp
    walk(('top',))
    for u in list(adj):
        if u in seen: continue
        comp=walk(u)
        par=sum(1 for v in comp if v[0]=='in' and v[1] in active_axis)%2
        loops.append(par)
    return loops
def W_hat(L,recs,axis_pos,site_mask):
    """symbol of the exact evaluation for the sites with mask 1 (others: plain crossings, on-axis ones remain twists)."""
    act=[r for r,mk in zip(recs,site_mask) if mk]
    base_active=set(p for p in axis_pos)        # every on-axis letter is a twist (winding 1) unless it is an active site with choice Id
    tot=0
    opts=[('or','un') if r['kind']=='off' else ('F','Id') for r in act]
    for choice in itertools.product(*opts):
        coef=1; active=set(base_active)
        for r,ch in zip(act,choice):
            if r['kind']=='off': coef*=-2*r['kap']*r['pi']*(1 if ch=='or' else -1)
            else:
                coef*=-r['kap']*(1 if ch=='F' else 3)
                if ch=='Id': active.discard(r['c'])
        val=1
        for par in components(L,act,choice,active): val*=C_LOOP[par]
        tot+=coef*val
    return tot
def W_pred(word,sites):
    recs,L,axis_pos=chord_data(word,sites); m=len(recs)
    n=[W_hat(L,recs,axis_pos,[1 if j==i else 0 for j in range(m)]) for i in range(m)]
    tot=0
    for T in itertools.product([0,1],repeat=m):
        f=1
        for i in range(m):
            if T[i]: f*=-n[i]
        tot+=f*W_hat(L,recs,axis_pos,[1-T[i] for i in range(m)])
    return tot,n,recs
def flip(toks,idxs):
    t=list(toks)
    for i in idxs: a=t[i]; t[i]=('y' if a[0]=='x' else 'x')+a[1:]
    return '.'.join(t)
def divpow(p,m):
    p=dict(p)
    for _ in range(m):
        if not p: return {}
        lo=min(p); hi=max(p); q={}; r=dict(p)
        for e in range(lo,hi):
            c=r.get(e,0)
            if c: q[e]=c; r[e]=0; r[e+1]=r.get(e+1,0)-c
        if any(v for v in r.values()): return None
        p={e:c for e,c in q.items() if c}
    return p
def W_num(word,sites):
    toks=word.split('.'); m=len(sites); alt={}
    for S in itertools.product([0,1],repeat=m):
        J=lp.J(flip(toks,[s for s,b in zip(sites,S) if b]))
        for e,c in J.items(): alt[e]=alt.get(e,0)+(-1)**sum(S)*c
    q=divpow({e:c for e,c in alt.items() if c},m)
    return (-1)**m*lp.ev(q,-1)
if __name__=='__main__':
    rnd=random.Random(int(sys.argv[1])); N=int(sys.argv[2]); ms=[int(v) for v in sys.argv[3].split(',')]
    kinds=sys.argv[4] if len(sys.argv)>4 else 'mixed'
    res={}; done=0; tries=0; bad=[]
    while done<N and tries<50000:
        tries+=1
        w=fs.gen(rnd,rnd.randint(8,16))
        if not w or lp.J(w) is None: continue
        toks=w.split('.')
        fl=[i for i,a in enumerate(toks) if len(a)>=2 and a[0] in 'xy' and a[1:].isdigit()]
        if kinds=='off': fl=[i for i in fl if toks[i][1:]!='0']
        m=rnd.choice(ms)
        if len(fl)<m: continue
        sites=rnd.sample(fl,m)
        try: wn=W_num(w,sites)
        except Exception as ex: continue
        wp,n,recs=W_pred(w,sites)
        done+=1; key=m; res.setdefault(key,[0,0])
        if wn==wp: res[key][0]+=1
        else: res[key][1]+=1; bad.append((w,sites,wn,wp))
    print('W_m prediction vs exact (m: [match, mismatch]):',res)
    for b in bad[:6]: print('  MISMATCH',b)
