"""Diagrams attached to a half-word (K,h):  K, its quotient constituent knots K_in = k u A_in, K_out = k u A_out,
and the upstairs constituent knots U_in = K_+ u O_in, U_out = K_+ u O_out (K_+ = one half of K between the fixed points).
Generic tools: crossing lists with 4 slots (TL,TR,BL,BR), type 'x' (over strand TL-BR) or 'y' (over strand TR-BL),
edges = pairs of slots; frontier Kauffman bracket; Jones (normalised V(1)=1, V'(1)=0); Alexander/Conway by interpolation."""
import sys
from fractions import Fraction as F
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import alex

class UF:
    def __init__(s): s.p={}
    def find(s,a):
        s.p.setdefault(a,a)
        r=a
        while s.p[r]!=r: r=s.p[r]
        while s.p[a]!=r: s.p[a],a=r,s.p[a]
        return r
    def union(s,a,b):
        ra,rb=s.find(a),s.find(b)
        if ra!=rb: s.p[ra]=rb

class Diagram:
    """crossings: list of (type, (TL,TR,BL,BR)) slot ids; the strand TL-BR and TR-BL; 'x': TL-BR over.
    links: union-find over points; endpoints = slots and germs. After build(), partner[slot] = other end of its edge."""
    def __init__(s):
        s.cr=[]; s.uf=UF(); s.nid=0; s.germs=set()
    def new(s):
        s.nid+=1; return ('p',s.nid)
    def crossing(s,typ,tl,tr):
        k=len(s.cr); sl=[('c',k,j) for j in ('TL','TR','BL','BR')]
        s.cr.append((typ,tuple(sl)))
        s.uf.union(tl,sl[0]); s.uf.union(tr,sl[1])
        return sl[2],sl[3]          # new current points at bottom-left, bottom-right

def morse_diagram(tokens, init_points):
    """sweep a Morse word (list of (c,i)), starting with the given list of current points; returns (Diagram, final points)"""
    D=Diagram(); pos=list(init_points)
    for c,i in tokens:
        if c in 'xy':
            bl,br=D.crossing(c,pos[i],pos[i+1]); pos[i],pos[i+1]=bl,br
        elif c in 'lr':
            p=D.new(); pos[i:i]=[p,p]
        elif c=='u':
            D.uf.union(pos[i],pos[i+1]); del pos[i:i+2]
        else: raise ValueError(c)
    return D,pos

# ---------------------------------------------------------------- the extended full diagram K u O
def extended_tokens(half):
    """Morse tokens of the symmetric diagram of K with the axis segment O_in drawn as a centre strand.
    positions: left 0..hw-1, axis hw, right hw+1..2hw.  Returns token list (final u0 handled by caller)."""
    hw=1; out=[]
    for c,s in half:
        if s==0:
            if c=='x': out+=[('x',hw-1),('x',hw),('x',hw-1)]
            elif c=='y': out+=[('y',hw),('y',hw-1),('y',hw)]
            else: return None
        elif c in 'xy':
            out.append((c,hw+s)); out.append((c,hw-s-1))
        elif c in 'lr':
            out.append((c,hw+s)); out.append((c,hw-s+1)); hw+=2
        elif c=='u':
            out.append(('u',hw+s)); out.append(('u',hw-s-1)); hw-=2
        else: return None
        if hw<1: return None
    if hw!=1: return None
    return out

def full_structure(word):
    """returns dict with Diagram D, the germs, and strand classes for K_+, K_-, O_in."""
    half=alex.parse(word)
    toks=extended_tokens(half)
    if toks is None: return None
    g=lambda v,n:('g',v,n)
    D,pos=morse_diagram(toks,[g('t','KL'),g('t','O'),g('t','KR')])
    if len(pos)!=3: return None
    # bottom fixed point: germs
    D.uf.union(pos[0],g('b','KL')); D.uf.union(pos[1],g('b','O')); D.uf.union(pos[2],g('b','KR'))
    # edges: group endpoints by class
    ends={}
    allpts=[sl for _,sls in D.cr for sl in sls]+[g(v,n) for v in 'tb' for n in ('KL','O','KR')]
    for p in allpts: ends.setdefault(D.uf.find(p),[]).append(p)
    partner={}
    for r,ps in ends.items():
        if len(ps)!=2: return None
        partner[ps[0]]=ps[1]; partner[ps[1]]=ps[0]
    opp={'TL':'BR','BR':'TL','TR':'BL','BL':'TR'}
    def through(sl): return ('c',sl[1],opp[sl[2]])
    def trace(start):
        """from germ start, follow the strand; return list of (crossing, strand id 0/1 for TL-BR / TR-BL) and end germ"""
        passes=[]; p=partner[start]
        while p[0]=='c':
            k,j=p[1],p[2]; passes.append((k,0 if j in ('TL','BR') else 1, j))
            q=through(p); p=partner[q]
        return passes,p
    kp,endp=trace(g('t','KR'))
    km,endm=trace(g('t','KL'))
    ox,endo=trace(g('t','O'))
    if endo!=g('b','O') or {endp,endm}!={g('b','KL'),g('b','KR')}: return None
    lab={}
    for k,st,_ in kp: lab[(k,st)]='K+'
    for k,st,_ in km: lab[(k,st)]='K-'
    for k,st,_ in ox: lab[(k,st)]='O'
    if len(lab)!=2*len(D.cr): return None
    return dict(D=D,partner=partner,lab=lab,kp=kp,km=km,ox=ox,endp=endp,endm=endm)

def sub_knot(S, keep, joins):
    """crossings among kept strands, edges re-linked through deleted crossings. keep: set of labels among K+,K-,O,Oout.
    joins: list of germ pairs to identify at the vertices (germ ('g','t'|'b',name); Oout is ('g','t','Oout')~('g','b','Oout')).
    Returns (crossings, partner) for the generic bracket: crossings list of (typ, slots)."""
    D=S['D']; partner=dict(S['partner']); lab=S['lab']
    partner[('g','t','Oout')]=('g','b','Oout'); partner[('g','b','Oout')]=('g','t','Oout')
    opp={'TL':'BR','BR':'TL','TR':'BL','BL':'TR'}
    kept=[]; 
    for k,(typ,sls) in enumerate(D.cr):
        a=lab[(k,0)] in keep; b=lab[(k,1)] in keep
        kept.append((a,b))
    # build new edges by walking: an endpoint is a kept slot (crossing with both strands kept) or a germ in a join
    UFj=UF()
    for a,b in joins: UFj.union(a,b)
    def is_end(p):
        if p[0]=='c':
            k=p[1]; return kept[k][0] and kept[k][1]
        return False
    newp={}
    def walk(p):
        # p is an endpoint slot; follow its edge until another endpoint
        q=partner[p]
        while True:
            if q[0]=='c':
                k,j=q[1],q[2]
                if kept[k][0] and kept[k][1]: return q
                st=0 if j in ('TL','BR') else 1
                if not kept[k][st]: raise RuntimeError('walked into deleted strand')
                q=partner[('c',k,opp[j])]
            else:
                # germ: jump to the joined germ
                mates=[x for x in (('g',q[1],n) for n in ('KL','O','KR','Oout')) if x!=q and UFj.find(x)==UFj.find(q)]
                if len(mates)!=1: raise RuntimeError('bad join at %s'%(q,))
                q=partner[mates[0]]
    crs=[]; idx={}
    for k,(typ,sls) in enumerate(D.cr):
        if kept[k][0] and kept[k][1]:
            idx[k]=len(crs); crs.append((typ,sls))
    for k in idx:
        for sl in D.cr[k][1]:
            newp[sl]=walk(sl)
    # free loops (kept components without crossings)
    return crs,newp

# ---------------------------------------------------------------- generic Kauffman bracket by frontier contraction
def padd(p,q,c=1):
    for e,v in q.items():
        nv=p.get(e,0)+c*v
        if nv: p[e]=nv
        elif e in p: del p[e]
def bracket_generic(crs, partner, free_loops=0):
    """sum over states A^(#A-#B) delta^(loops-1), delta=-A^2-A^-2. crs in processing order. Returns {exp:coeff}."""
    n=len(crs)
    if n==0:
        r={0:1}
        for _ in range(free_loops-1): r=_mulDelta(r)
        return r
    order=list(range(n))
    done=set()
    # state: frozenset of frontier pairs (as tuple sorted), value poly
    states={():({0:1})}
    loops_cache=None
    for k in order:
        typ,sls=crs[k]; TL,TR,BL,BR=sls
        wV,wH=(1,-1) if typ=='x' else (-1,1)
        new={}
        for st,poly in states.items():
            M=dict()
            for a,b in st: M[a]=b; M[b]=a
            for arcs,w in (((TL,BL),(TR,BR)),wV),((((TL,TR),(BL,BR)),wH)):
                # graph: frontier matching M (paths), smoothing arcs, edges from this crossing's slots to processed partners
                adj={}
                def link(a,b):
                    adj.setdefault(a,[]).append(b); adj.setdefault(b,[]).append(a)
                for a,b in arcs: link(a,b)
                for sl in sls:
                    q=partner[sl]
                    if q in M: link(sl,q)         # edge closes into processed region
                    elif q in sls: link(sl,q)     # edge from crossing to itself (kink)
                for a,b in st:
                    link(a,b)
                # components: endpoints still open = slots of this crossing whose partner unprocessed (not in M, not in sls),
                # and frontier slots not touched (their own partner unprocessed) -- those are in M already.
                opens=set()
                for sl in sls:
                    q=partner[sl]
                    if q not in M and q not in sls: opens.add(sl)
                for a in M:
                    q=partner[a]
                    if q not in sls: opens.add(a)
                seen=set(); pairs=[]; loops=0
                for a in list(adj):
                    if a in seen: continue
                    # BFS component
                    comp=[a]; seen.add(a); i=0
                    while i<len(comp):
                        x=comp[i]; i+=1
                        for y in adj.get(x,[]):
                            if y not in seen: seen.add(y); comp.append(y)
                    oc=[x for x in comp if x in opens]
                    if len(oc)==0: loops+=1
                    elif len(oc)==2: pairs.append(tuple(sorted(oc)))
                    else: raise RuntimeError('bad component %s'%len(oc))
                key=tuple(sorted(pairs))
                p2={e+w:c for e,c in poly.items()}
                for _ in range(loops): p2=_mulDelta(p2)
                padd(new.setdefault(key,{}),p2)
        states={k2:v for k2,v in new.items() if v}
    tot={}
    for st,poly in states.items():
        assert st==(), st
        padd(tot,poly)
    # tot = sum A^.. delta^loops ; divide by delta once, times delta^free_loops
    for _ in range(free_loops): tot=_mulDelta(tot)
    return _divDelta(tot)
def _mulDelta(p):
    r={}; padd(r,{e+2:-c for e,c in p.items()}); padd(r,{e-2:-c for e,c in p.items()}); return r
def _divDelta(p):
    r={}; p=dict(p)
    while p:
        e=max(p); v=p[e]; r[e-2]=-v; padd(p,{e:-v,e-4:-v})
    return r

def order_crossings(crs, partner):
    """greedy order: start with crossing 0, repeatedly add the crossing with most slots adjacent to processed ones"""
    n=len(crs)
    if n==0: return crs,partner
    slot2k={sl:k for k,(t,sls) in enumerate(crs) for sl in sls}
    done=[0]; ds={0}
    while len(done)<n:
        best=None; bs=-1
        cand=set()
        for k in done:
            for sl in crs[k][1]:
                q=partner[sl]; kk=slot2k[q]
                if kk not in ds: cand.add(kk)
        if not cand: cand={next(k for k in range(n) if k not in ds)}
        for kk in cand:
            sc=sum(1 for sl in crs[kk][1] if slot2k[partner[sl]] in ds or slot2k[partner[sl]]==kk)
            if sc>bs: bs=sc; best=kk
        done.append(best); ds.add(best)
    return [crs[k] for k in done],partner

def jones_from_bracket(kb):
    kb={e:c for e,c in kb.items() if c}
    es=sorted(kb); r=es[0]%4
    if any((e-r)%4 for e in es): return None
    V={-(e-r)//4:c for e,c in kb.items()}
    s=sum(V.values())
    if s not in (1,-1): return None
    V={e:c*s for e,c in V.items()}
    d=sum(e*c for e,c in V.items())
    return {e-d:c for e,c in V.items()}

def der(V,k,x=1):
    tot=0
    for e,c in V.items():
        f=1
        for i in range(k): f*=(e-i)
        tot+=c*f*F(x)**(e-k)
    return tot

# ---------------------------------------------------------------- Alexander / Conway from a generic knot diagram
def alexander_generic(crs, partner):
    """symmetric normalised Alexander polynomial {exp: coeff} (Delta(1)=1) of a knot diagram (crossing list + partner)."""
    n=len(crs)
    if n==0: return {0:1}
    opp={'TL':'BR','BR':'TL','TR':'BL','BL':'TR'}
    slot={}
    for k,(t,sls) in enumerate(crs):
        for sl in sls: slot[sl]=(k,sl[2])
    # traverse from crossing 0 slot TL going "in"
    start=crs[0][1][0]
    seq=[]   # (k, strand, direction entering slot name)
    p=start
    for _ in range(2*n+2):
        k,j=slot[p]
        seq.append((k,j))
        q=crs[k][1][['TL','TR','BL','BR'].index(opp[j])]
        p=partner[q]
        if p==start: break
    if len(seq)!=2*n: return None
    vec={'TL':(-1,1),'TR':(1,1),'BL':(-1,-1),'BR':(1,-1)}
    dirs={}
    for k,j in seq:
        a=vec[j]; b=vec[opp[j]]; d=(b[0]-a[0],b[1]-a[1])
        st=0 if j in ('TL','BR') else 1
        dirs[(k,st)]=d
    # arcs: cut at under-passes
    def is_over(k,j):
        typ=crs[k][0]; st=0 if j in ('TL','BR') else 1
        return (typ=='x' and st==0) or (typ=='y' and st==1)
    arc_of_pass=[]; a=0
    # find an under-pass to start
    i0=next(i for i,(k,j) in enumerate(seq) if not is_over(k,j))
    m=len(seq); cur=0; under_in={}; under_out={}; over_arc={}
    for t in range(m):
        k,j=seq[(i0+t)%m]
        if not is_over(k,j):
            under_in[k]=cur if t>0 else None
            cur+=1 if t>0 else 0
            under_out[k]=cur
        else:
            over_arc[k]=cur
    narcs=cur+1 if False else cur
    # fix the first under pass: incoming arc is the last arc (cur), which wraps to arc 0
    k0,_=seq[i0]
    under_in[k0]=cur
    # wrap: arc 'cur' is the same as arc 0? arcs numbered 0..cur-1 then the segment after last under pass continues to i0 -> it is arc 'cur'
    # the segment starting at seq[i0] outgoing is arc 0; final arc 'cur' runs into seq[i0] (under). they are different arcs
    # unless... number of arcs = number of under passes = n: arcs 0..n-1 where arc after the last under pass is index n-1+1? recount:
    NA=n
    def A(x): return x%NA
    rows=[]
    for k,(typ,sls) in enumerate(crs):
        st_o=0 if typ=='x' else 1; st_u=1-st_o
        do=dirs[(k,st_o)]; du=dirs[(k,st_u)]
        sign=1 if do[0]*du[1]-do[1]*du[0]>0 else -1
        rows.append((sign,A(over_arc[k]),A(under_in[k]),A(under_out[k])))
    def det_at(tv):
        M=[[0]*NA for _ in range(NA)]
        for r,(sg,o,ui,uo) in enumerate(rows):
            if sg>0: M[r][ui]+=tv; M[r][o]+=1-tv; M[r][uo]-=1
            else: M[r][ui]+=1; M[r][o]+=tv-1; M[r][uo]-=tv
        m=[row[:-1] for row in M[:-1]]
        return alex.bareiss(m)
    pts=list(range(2,2+NA+1))
    vals=[det_at(x) for x in pts]
    # interpolate polynomial of degree <= NA
    coeffs=_interp(pts,vals)
    poly={i:c for i,c in enumerate(coeffs) if c}
    if not poly: return None
    lo=min(poly); hi=max(poly)
    if (hi-lo)%2: return None
    mid=(hi+lo)//2
    P={e-mid:c for e,c in poly.items()}
    s=sum(P.values())
    if s not in (1,-1): return None
    P={e:c*s for e,c in P.items()}
    if any(P.get(e,0)!=P.get(-e,0) for e in P): return None
    return P
def _interp(xs,ys):
    n=len(xs); coeffs=[F(0)]*n
    for i in range(n):
        # basis polynomial
        num=[F(1)]; den=F(1)
        for j in range(n):
            if j==i: continue
            num=[F(0)]+num
            for t in range(len(num)-1): num[t]-=xs[j]*num[t+1]
            den*=xs[i]-xs[j]
        for t in range(n): coeffs[t]+=ys[i]*num[t]/den
    out=[]
    for c in coeffs:
        assert c.denominator==1, c
        out.append(int(c))
    return out
def conway(P):
    """Conway coefficients [a0,a2,a4,...] from symmetric Alexander {e:c}"""
    # t^j + t^-j as polynomial in w = z^2 : T_j(w) with t+1/t = w+2; use recursion s_j = (w+2) s_{j-1} - s_{j-2}, s_0=2, s_1=w+2
    m=max(P) if P else 0
    S=[[2],[2,1]]
    for j in range(2,m+1):
        a=S[j-1]; b=S[j-2]
        c=[0]*(len(a)+1)
        for i,v in enumerate(a): c[i]+=2*v; c[i+1]+=v
        for i,v in enumerate(b): c[i]-=v
        S.append(c)
    res=[0]*(m+1)
    res[0]+=P.get(0,0)
    for j in range(1,m+1):
        for i,v in enumerate(S[j]): res[i]+=P.get(j,0)*v
    return res

# ---------------------------------------------------------------- quotient constituent knots K_in, K_out (Morse words)
def quotient_constituent_tokens(word, which):
    """K_in = k u A_in: axis segment at position 0, arc half-strand j at position j+1; x0/y0 -> full twist (c,0),(c,0).
       K_out = k u A_out: same with x0/y0 deleted (A_out is crossing-free)."""
    half=alex.parse(word); out=[]
    for c,s in half:
        if s==0:
            if which=='in': out+=[(c,0),(c,0)]
        elif c in 'xy': out.append((c,s))
        elif c in 'lr': out.append((c,s))
        elif c=='u': out.append(('u',s))
    out.append(('u',0))
    return out
def morse_knot(tokens):
    """generic (crs, partner) from a closed Morse word starting with a cap (2 strands)"""
    p0=('p',0)
    D,pos=morse_diagram(tokens,[p0,p0])
    if pos: return None
    ends={}
    allpts=[sl for _,sls in D.cr for sl in sls]
    for p in allpts: ends.setdefault(D.uf.find(p),[]).append(p)
    partner={}
    for r,ps in ends.items():
        if len(ps)!=2: return None
        partner[ps[0]]=ps[1]; partner[ps[1]]=ps[0]
    return D.cr,partner

def knot_invariants(crs,partner):
    """returns dict with V (normalised Jones), a2, v3, j4, Delta, conway coeffs"""
    crs2,partner2=order_crossings(crs,partner)
    kb=bracket_generic(crs2,partner2)
    V=jones_from_bracket(kb)
    if V is None: return None
    Dl=alexander_generic(crs,partner)
    if Dl is None: return None
    cw=conway(Dl)
    a2=F(-der(V,2),6)
    v3=F(-(der(V,3)+3*der(V,2)),36)
    j4=F(der(V,4)+6*der(V,3)+7*der(V,2)+der(V,1),24)
    a2c=cw[1] if len(cw)>1 else 0
    a4=cw[2] if len(cw)>2 else 0
    return dict(V=V,a2=a2,v3=v3,j4=j4,Delta=Dl,a2c=a2c,a4=a4)

def all_invariants(word):
    S=full_structure(word)
    if S is None: return None
    out={}
    g=lambda v,n:('g',v,n)
    endp=S['endp']; endm=S['endm']
    # K
    crs,pt=sub_knot(S,{'K+','K-'},[(g('t','KR'),g('t','KL')),(endp,endm)])
    out['K']=knot_invariants(crs,pt)
    crs,pt=sub_knot(S,{'K+','O'},[(g('t','KR'),g('t','O')),(endp,g('b','O'))])
    out['Uin']=knot_invariants(crs,pt)
    crs,pt=sub_knot(S,{'K+','Oout'},[(g('t','KR'),g('t','Oout')),(endp,g('b','Oout'))])
    out['Uout']=knot_invariants(crs,pt)
    for which in ('in','out'):
        mk=morse_knot(quotient_constituent_tokens(word,which))
        out['K'+which]=knot_invariants(*mk) if mk else None
    return out

def K_invariants(word):
    S=full_structure(word)
    if S is None: return None
    g=lambda v,n:('g',v,n)
    crs,pt=sub_knot(S,{'K+','K-'},[(g('t','KR'),g('t','KL')),(S['endp'],S['endm'])])
    return knot_invariants(crs,pt)
