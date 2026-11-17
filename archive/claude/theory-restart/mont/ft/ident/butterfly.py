"""Butterfly links of (K,h) (band move on K along a half-axis, components K_+ u O' and K_- u O''),
built from a half-word, with n_b crossings inserted between the two band strands.
Generic oriented link tools: components, linking number, Alexander polynomial, Conway coefficients."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex, diag
from fractions import Fraction as F

def tokens_doubled_axis(half):
    """symmetric diagram of K with the inner axis segment doubled (band strands O'' at hw, O' at hw+1)."""
    hw=1; out=[]
    for c,s in half:
        if s==0:
            if c=='x': out+=[('x',hw-1),('x',hw),('x',hw+1),('x',hw),('x',hw-1)]
            elif c=='y': out+=[('y',hw+1),('y',hw),('y',hw-1),('y',hw),('y',hw+1)]
        elif c in 'xy': out.append((c,hw+1+s)); out.append((c,hw-s-1))
        elif c in 'lr': out.append((c,hw+1+s)); out.append((c,hw-s+1)); hw+=2
        elif c=='u': out.append(('u',hw+1+s)); out.append(('u',hw-s-1)); hw-=2
        if hw<1: return None
    return out if hw==1 else None

def build(word, axis, nb, btype):
    """returns (crs, partner, start1, start2) ; start slots: first slot of C1 along K_+ from f_top (forward),
    and a slot to start C2 such that tracing goes forward along K_- orientation (we trace then reverse)."""
    half=alex.parse(word)
    g=lambda n:('g',n)
    if axis=='out':
        full=alex.symmetrize(half)
        if full is None: return None
        body=full[:-1]          # drop final ('u',0)
        toks=[(btype,0)]*nb + [(c,i+2) for c,i in body]
        D,pos=diag.morse_diagram(toks,[g('L1'),g('L2'),g('Kl'),g('Kr')])
        if len(pos)!=4: return None
        D.uf.union(pos[0],g('L1e')); D.uf.union(pos[1],g('L2e')); D.uf.union(pos[2],g('Kle')); D.uf.union(pos[3],g('Kre'))
        joins=[(g('L1'),g('Kr')),(g('L2'),g('Kl')),(g('L2e'),g('Kle')),(g('L1e'),g('Kre'))]
    else:
        body=tokens_doubled_axis(half)
        if body is None: return None
        toks=[(btype,1)]*nb + body
        D,pos=diag.morse_diagram(toks,[g('Kl'),g('Oll'),g('Orr'),g('Kr')])
        if len(pos)!=4: return None
        D.uf.union(pos[0],g('Kle')); D.uf.union(pos[1],g('Olle')); D.uf.union(pos[2],g('Orre')); D.uf.union(pos[3],g('Kre'))
        joins=[(g('Kl'),g('Oll')),(g('Orr'),g('Kr')),(g('Kle'),g('Olle')),(g('Orre'),g('Kre'))]
    # endpoints per class
    germs=[g(n) for n in ('L1','L2','Kl','Kr','L1e','L2e','Kle','Kre','Oll','Orr','Olle','Orre')]
    allpts=[sl for _,sls in D.cr for sl in sls]+germs
    ends={}
    for p in allpts:
        if p in D.uf.p or p[0]=='c': ends.setdefault(D.uf.find(p),[]).append(p)
    partner={}
    for r,ps in ends.items():
        ps=[p for p in ps if p in D.uf.p or p[0]=='c']
        if len(ps)!=2: return None
        partner[ps[0]]=ps[1]; partner[ps[1]]=ps[0]
    jmap={}
    for a,b in joins: jmap[a]=b; jmap[b]=a
    # resolve germ chains to slot-to-slot partner
    newp={}
    for sl,q in partner.items():
        if sl[0]!='c': continue
        while q[0]!='c':
            q=partner[jmap[q]]
        newp[sl]=q
    # start slot for C1: the slot whose edge leads back to germ Kr (first crossing along K_+)
    def slot_of(germ):
        q=partner[germ]
        return q if q[0]=='c' else None
    s1=slot_of(g('Kr')); s2=slot_of(g('Kl'))
    return D.cr,newp,s1,s2

OPP={'TL':'BR','BR':'TL','TR':'BL','BL':'TR'}
VEC={'TL':(-1,1),'TR':(1,1),'BL':(-1,-1),'BR':(1,-1)}
def trace_from(crs,partner,s):
    """s: entry slot ('c',k,name). returns list of (k, entry name) along the component"""
    seq=[]; p=s
    while True:
        k,j=p[1],p[2]; seq.append((k,j))
        q=('c',k,OPP[j]); p=partner[q]
        if p==s: break
        if len(seq)>4*len(crs)+4: raise RuntimeError('trace loop')
    return seq
def link_data(crs,partner,starts,reverse_flags):
    comps=[]
    for s,rev in zip(starts,reverse_flags):
        seq=trace_from(crs,partner,s)
        if rev:
            seq=[(k,OPP[j]) for k,j in reversed(seq)]
        comps.append(seq)
    npass=sum(len(c) for c in comps)
    if npass!=2*len(crs): return None
    comp_of={}; dirs={}
    for ci,seq in enumerate(comps):
        for k,j in seq:
            st=0 if j in ('TL','BR') else 1
            comp_of[(k,st)]=ci
            a=VEC[j]; b=VEC[OPP[j]]; dirs[(k,st)]=(b[0]-a[0],b[1]-a[1])
    signs=[]
    for k,(typ,sls) in enumerate(crs):
        so=0 if typ=='x' else 1; su=1-so
        do=dirs[(k,so)]; du=dirs[(k,su)]
        signs.append(1 if do[0]*du[1]-do[1]*du[0]>0 else -1)
    lk2=sum(signs[k] for k in range(len(crs)) if comp_of[(k,0)]!=comp_of[(k,1)])
    return comps,comp_of,dirs,signs,lk2
def alexander_link(crs,partner,comps,signs):
    """single-variable Alexander polynomial (as {exp:coeff} in t, unnormalised) of an oriented link diagram."""
    def is_over(k,j):
        typ=crs[k][0]; st=0 if j in ('TL','BR') else 1
        return (typ=='x' and st==0) or (typ=='y' and st==1)
    arcs=0; over_arc={}; uin={}; uout={}
    for seq in comps:
        m=len(seq)
        unders=[i for i,(k,j) in enumerate(seq) if not is_over(k,j)]
        if not unders:
            a=arcs; arcs+=1
            for k,j in seq: over_arc[k]=a
            continue
        i0=unders[0]; first=arcs; cur=arcs
        for t in range(m):
            k,j=seq[(i0+t)%m]
            if not is_over(k,j):
                if t==0: uout[k]=cur
                else:
                    uin[k]=cur; cur+=1; uout[k]=cur
            else: over_arc[k]=cur
        last=cur
        k0,_=seq[i0]; uin[k0]=last
        arcs=last+1
    n=len(crs)
    if arcs!=n: return None
    rows=[(signs[k],over_arc[k],uin[k],uout[k]) for k in range(n)]
    def det_at(tv):
        M=[[0]*n for _ in range(n)]
        for r,(sg,o,ui,uo) in enumerate(rows):
            if sg>0: M[r][ui]+=tv; M[r][o]+=1-tv; M[r][uo]-=1
            else: M[r][ui]+=1; M[r][o]+=tv-1; M[r][uo]-=tv
        return alex.bareiss([row[:-1] for row in M[:-1]])
    pts=list(range(2,2+n+1)); vals=[det_at(x) for x in pts]
    co=diag._interp(pts,vals)
    return {i:c for i,c in enumerate(co) if c}
def conway_2comp(P, lk):
    """Conway coefficients [a1,a3,a5,..] of a 2-component link from its Alexander polynomial P(t) (unnormalised),
    sign fixed by a1 = lk (requires lk != 0). Returns None if inconsistent."""
    if not P: return [0]
    lo=min(P); hi=max(P); d=hi-lo
    if d%2==0: return None
    # Q(s) = s^{-(lo+hi)} P(s^2) has odd exponents from -d..d ; divide by (s - 1/s)
    Q={2*e-(lo+hi):c for e,c in P.items()}
    # long division by s - s^-1 : Q = (s - s^-1) R, R even
    Q=dict(Q); R={}
    while Q:
        e=max(Q); c=Q[e]
        R[e-1]=c
        Q[e]=Q.get(e,0)-c; Q[e-2]=Q.get(e-2,0)+c
        Q={k:v for k,v in Q.items() if v}
        if Q and max(Q)<min(R)-1-10**6: break
    if any(e%2 for e in R): return None
    Rt={e//2:c for e,c in R.items()}       # symmetric Laurent poly in t
    if any(Rt.get(e,0)!=Rt.get(-e,0) for e in Rt): return None
    cw=diag.conway(Rt)
    if cw[0]==0: return None
    if lk==0: return None
    sgn=1 if cw[0]*lk>0 else -1
    if abs(cw[0])!=abs(lk): return ('lkmismatch',cw[0],lk)
    return [sgn*c for c in cw]
def butterfly_a3(word, axis):
    """Sato-Levine type invariant: a3 of the butterfly link (lk=0), via a3(L^{lk=e}) - e*a2(K) with lk=e=+-1."""
    half=alex.parse(word)
    n0=sum(1 for c,s in half if s==0)
    # first: untwisted band (nb = parity only) to get lk
    res={}
    for btype in ('x','y'):
        for nb in range(n0%2, 40, 2):
            b=build(word,axis,nb,btype)
            if b is None: return None
            crs,partner,s1,s2=b
            ld=link_data(crs,partner,[s1,s2],[False,True])
            if ld is None: return None
            comps,comp_of,dirs,signs,lk2=ld
            res[(btype,nb)]=lk2
    return res

def link_conway(word, axis, nb, btype):
    b=build(word,axis,nb,btype)
    if b is None: return None
    crs,partner,s1,s2=b
    ld=link_data(crs,partner,[s1,s2],[False,True])
    if ld is None: return None
    comps,comp_of,dirs,signs,lk2=ld
    P=alexander_link(crs,partner,comps,signs)
    if P is None: return None
    cw=conway_2comp(P,lk2//2) if lk2!=0 else None
    return lk2//2, cw, P
def sato_levine(word, axis, check=True):
    """a3 of the lk=0 butterfly link along the half-axis ('in' or 'out').  Uses the members with lk=+-1,+-2
    of the band-twist family (where the Conway sign is fixed by a1=lk) and the skein relation
    a3(L^(n+1)) - a3(L^(n)) = const (= +-a2(K), checked)."""
    half=alex.parse(word)
    n0=sum(1 for c,s in half if s==0)
    found=None
    for btype in ('x','y'):
        for nb in range(n0%2, 60, 2):
            b=build(word,axis,nb,btype)
            if b is None: return None
            crs,partner,s1,s2=b
            ld=link_data(crs,partner,[s1,s2],[False,True])
            if ld is None: return None
            if ld[4]==0: found=(btype,nb); break
        if found: break
    if not found: return None
    btype,nb=found
    r1=link_conway(word,axis,nb+2,btype); r2=link_conway(word,axis,nb+4,btype)
    if r1 is None or r2 is None or not isinstance(r1[1],list) or not isinstance(r2[1],list): return ('fail',r1,r2)
    a3_1=r1[1][1] if len(r1[1])>1 else 0
    a3_2=r2[1][1] if len(r2[1])>1 else 0
    step=a3_2-a3_1
    return dict(a3=a3_1-step, step=step, lk1=r1[0], lk2=r2[0], btype=btype, nb=nb)
