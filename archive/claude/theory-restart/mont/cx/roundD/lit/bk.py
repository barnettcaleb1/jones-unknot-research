"""Round D lit lane: branch knots L_n = T(1/n) of strongly invertible knots given by half-diagram words.
Builds full Morse words for K (symmetrised) and for closures of the quotient tangle T (flat_search.quotient_word),
converts to PD codes, and evaluates with project tools (alex.py) and regina (Jones, SnapPea kernel).
Run with: PYTHONPATH=<codex packages> /opt/homebrew/bin/python3.13"""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import alex, flat_search as fs, kauffman
from kauffman import padd, pshift, pdelta

def full_K(word):
    return alex.symmetrize(alex.parse(word))

def full_closure(word, fill):
    """full Morse word of a closure of the quotient tangle of s.<word>.
    positions after the shifted quotient word: 0 = return strand (= top end T), 1,2,3 = b1,b2,b3.
    fill = list of Morse letters acting on positions 0..3 followed by closing cups (must close everything)."""
    half=alex.parse(word)
    q=fs.quotient_word(half)
    return [(c,i+1) for c,i in q]+list(fill)

C_INF=[('u',2),('u',0)]       # c-pattern: T-b1, b2-b3   (T(inf) = unknot)
C_ZERO=[('u',1),('u',0)]      # b-pattern: T-b3, b1-b2   (T(0) up to framing)

def bracket_full(full):
    """Kauffman bracket <D>/delta of a full Morse word starting with one cap (positions 0,1), same conventions as kauffman.bracket."""
    state={(1,0):{0:1}}
    for c,i in full:
        new={}
        for m,p in state.items():
            if c in 'lr':
                padd(new.setdefault(kauffman.cap(m,i),{}),p)
            elif c=='u':
                m2,loop=kauffman.cup(m,i)
                padd(new.setdefault(m2,{}),pdelta(p) if loop else p)
            else:
                a,b=(1,-1) if c=='x' else (-1,1)
                padd(new.setdefault(m,{}),pshift(p,a))
                m2,loop=kauffman.cup(m,i)
                q=pdelta(p) if loop else p
                padd(new.setdefault(kauffman.cap(m2,i),{}),pshift(q,b))
        state={m:p for m,p in new.items() if p}
    assert set(state)<={()}, 'not closed'
    p=dict(state.get((),{}))
    r={}
    while p:
        e=max(p); v=p[e]
        r[e-2]=-v
        padd(p,{e:-v,e-4:-v})
    return r

def det_from_bracket(br):
    """|<D>(A=exp(i pi/4))| / ... : det = |V(-1)| = |<D>/delta at A=e^{i pi/4}| (|delta|=0 there, so use <D>/delta directly)."""
    import cmath
    A=cmath.exp(1j*cmath.pi/4)
    v=sum(c*A**e for e,c in br.items())
    return round(abs(v))

def pd_code(full):
    """PD code (KnotTheory convention, consecutive labels along the orientation) of a KNOT diagram given by a full Morse word.
    Uses alex.diagram for edges/orientation."""
    cr=alex.diagram(full)
    if cr is None: return None
    if not cr: return []
    n=len(cr)
    ends={}
    for k,x in enumerate(cr):
        for key in ('ot','ob','ut','ub'):
            ends.setdefault(x[key],[]).append((k,key))
    # traverse in the orientation recorded by alex.diagram (od/ud: True = strand runs downwards)
    lab={}   # (edge id) -> label
    k,s=0,'o'; label=0
    seq=[]
    for step in range(2*n):
        x=cr[k]; down=x[s+'d']
        outkey=s+('b' if down else 't')
        e=x[outkey]
        label+=1; lab[e]=label
        a,b=ends[e]
        nxt=b if a==(k,outkey) else a
        k=nxt[0]; s=nxt[1][0]
    assert len(lab)==2*n, (len(lab),n)
    pd=[]
    for x in cr:
        a,b,cc,d=x['ot'],x['ut'],x['ub'],x['ob']   # placeholder, fixed below by type
        if x['ty']=='x':
            TL,BR=x['ot'],x['ob']; TR,BL=x['ut'],x['ub']   # over TL-BR, under TR-BL
            if x['ud']: tup=(TR,TL,BL,BR)      # under goes down: incoming TR, ccw TR,TL,BL,BR
            else:       tup=(BL,BR,TR,TL)
        else:
            TR,BL=x['ot'],x['ob']; TL,BR=x['ut'],x['ub']   # over TR-BL, under TL-BR
            if x['ud']: tup=(TL,BL,BR,TR)
            else:       tup=(BR,TR,TL,BL)
        pd.append(tuple(lab[e] for e in tup))
    return pd

def regina_link(pd):
    import regina
    return regina.Link.fromPD(pd)

def jones_t(L):
    """Jones polynomial of a regina link as dict {t-exponent: coeff} (regina returns a polynomial in x=t^(1/2))."""
    p=L.jones()
    out={}
    lo=p.minExp(); hi=p.maxExp()
    for e in range(lo,hi+1):
        c=int(str(p[e]))
        if c:
            assert e%2==0, 'half-integer exponent: not a knot?'
            out[e//2]=c
    return out

def alexander(full):
    import sympy as sp
    t=sp.symbols('t')
    cr=alex.diagram(full)
    if cr is None: return None
    if not cr: return sp.Integer(1)
    M,w=alex.alex_matrix(cr,t)
    m=sp.Matrix([r[:-1] for r in M[:-1]])
    d=sp.expand(m.det(method='berkowitz'))
    # normalise: symmetric, positive at t=1
    P=sp.Poly(sp.expand(d*t**200),t)
    coeffs=P.all_coeffs()[::-1]
    lo=next(i for i,c in enumerate(coeffs) if c!=0)
    coeffs=coeffs[lo:]
    while coeffs and coeffs[-1]==0: coeffs.pop()
    s=sum(coeffs)
    if s<0: coeffs=[-c for c in coeffs]
    return tuple(int(c) for c in coeffs)

def vstr(V):
    return ' '.join('%+d t^%d'%(c,e) for e,c in sorted(V.items()))

# ---------- branch knots and SnapPea checks ----------
def tw(pos,k): return [('x' if k>0 else 'y',pos)]*abs(k)

def frame(word, rng=range(-30,31)):
    """integer f with det([s0^f][b-closure]) = 0 (the 0-framing of the quotient tangle)."""
    zs=[f for f in rng if det_from_bracket(bracket_full(full_closure(word,tw(0,f)+C_ZERO)))==0]
    assert len(zs)==1, zs
    return zs[0]

def full_Ln(word,n,f=None):
    if f is None: f=frame(word)
    return full_closure(word,tw(0,f)+tw(1,n)+C_INF)

def snap(pd):
    import regina
    return regina.SnapPeaTriangulation(regina.Link.fromPD(pd))

def filled(S,p,q):
    """volume, solution type and H_1 of the (p,q) filling (p*meridian + q*longitude)."""
    S.fill(p,q,0)
    v=S.volume(); st=S.solutionType(); h=S.homologyFilled()
    S.unfill(0)
    return v,str(st),h.str() if hasattr(h,'str') else str(h)

def branched_double_cover_volume(pd):
    """volume / solution type / homology of the 2-fold branched cover of S^3 over the knot with PD code pd:
    the 2-fold cyclic cover of the complement, filled along the (1,0) curve of the cover's cusp (lift of meridian^2)."""
    import regina
    S=snap(pd)
    res=[]
    def act(C,ct):
        C.fill(1,0,0)
        res.append((C.volume(),str(C.solutionType()),str(C.homologyFilled())))
    S.enumerateCovers(2, regina.SnapPeaTriangulation.CoverEnumeration.Cyclic, act)
    return res

# ---------- adequacy of a PD diagram ----------
def adequacy(pd):
    """returns (A_adequate, B_adequate, #circles_A, #circles_B) for a PD diagram (KnotTheory convention:
    A-smoothing of X[a,b,c,d] = P[a,b] P[c,d], B-smoothing = P[a,d] P[b,c])."""
    res=[]
    for pairs in (((0,1),(2,3)),((0,3),(1,2))):
        par={}
        def find(x):
            par.setdefault(x,x)
            while par[x]!=x:
                par[x]=par[par[x]]; x=par[x]
            return x
        def uni(x,y): par[find(x)]=find(y)
        where={}
        for k,X in enumerate(pd):
            for s,lab in enumerate(X): where.setdefault(lab,[]).append((k,s))
        for lab,ends in where.items():
            assert len(ends)==2
            uni(ends[0],ends[1])
        for k,X in enumerate(pd):
            for p,q in pairs: uni((k,p),(k,q))
        ok=all(find((k,pairs[0][0]))!=find((k,pairs[1][0])) for k in range(len(pd)))
        ncirc=len(set(find((k,s)) for k in range(len(pd)) for s in range(4)))
        res.append((ok,ncirc))
    return res[0][0],res[1][0],res[0][1],res[1][1]
