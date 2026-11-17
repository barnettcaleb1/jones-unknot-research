"""Referee's independent invariant code for lane IDENT.  Uses only the shared tools lp.J (J of a half-word),
kauffman.bracket (bracket of the full symmetric diagram) and alex (parse/symmetrize/diagram/alex_matrix).
Nothing is imported from the builder's folder."""
import sys, random, itertools
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, kauffman, alex

def mom(J,k):   # M_k = sum_e J_e (-1)^e e^k
    return sum(c*(1 if e%2==0 else -1)*e**k for e,c in J.items())
def nmom(J,k):  # N_k = sum_e J_e e^k
    return sum(c*e**k for e,c in J.items())

def V_from_bracket(kb):
    """standard: t = A^-4 applied to the code's bracket; normalise V(1)=1, V'(1)=0 (knots)."""
    kb={e:c for e,c in kb.items() if c}
    if not kb: return None
    es=sorted(kb); r=es[0]%4
    if any((e-r)%4 for e in es): return None
    V={}
    for e,c in kb.items():
        V[-(e-r)//4]=V.get(-(e-r)//4,0)+c
    s=sum(V.values())
    if s not in (1,-1): return None
    V={e:s*c for e,c in V.items()}
    d=sum(e*c for e,c in V.items())
    return {e-d:c for e,c in V.items() if c}
def VK(word):
    kb=kauffman.bracket(word)
    if kb is None: return None
    return V_from_bracket(kb)
def vinv(V):
    """a2, v3, j4 from V via power sums m_k = sum V_e e^k (V(1)=1, m_1=0)."""
    m=[sum(c*e**k for e,c in V.items()) for k in range(5)]
    assert m[0]==1 and m[1]==0, m
    a2=Fr(-m[2],6)                 # V''(1) = m2 - m1 = m2 = -6 a2
    v3=Fr(-m[3],36)                # V'''(1)+3V''(1) = m3 - 3m2 + 2m1 + 3(m2 - m1) = m3
    j4=Fr(m[4],24)                 # [h^4] V(e^h) = m4/24
    return a2,v3,j4

# ---------- Alexander polynomial of the full symmetric diagram, exact, via modular evaluation + interpolation
PRIMES=[2305843009213693951, 4611686018427387847, 9223372036854775783]
def det_mod(M,p):
    n=len(M); A=[[x%p for x in row] for row in M]; d=1
    for c in range(n):
        piv=next((i for i in range(c,n) if A[i][c]),None)
        if piv is None: return 0
        if piv!=c: A[c],A[piv]=A[piv],A[c]; d=-d
        d=d*A[c][c]%p; inv=pow(A[c][c],p-2,p)
        for i in range(c+1,n):
            if A[i][c]:
                f=A[i][c]*inv%p
                A[i]=[(x-f*y)%p for x,y in zip(A[i],A[c])]
    return d%p
def interp_mod(xs,ys,p):
    # Newton interpolation mod p -> coefficient list
    n=len(xs); coef=list(ys)
    for j in range(1,n):
        for i in range(n-1,j-1,-1):
            coef[i]=(coef[i]-coef[i-1])*pow(xs[i]-xs[i-j],p-2,p)%p
    poly=[0]*n
    for i in range(n-1,-1,-1):
        # poly = poly*(x - xs[i]) + coef[i]
        new=[0]*n
        for k in range(n-1):
            new[k+1]=(new[k+1]+poly[k])%p
        for k in range(n):
            new[k]=(new[k]-xs[i]*poly[k])%p
        new[0]=(new[0]+coef[i])%p
        poly=new
    return poly
def alexander(word):
    full=alex.symmetrize(alex.parse(word))
    if full is None: return None
    cr=alex.diagram(full)
    if cr is None: return None
    if not cr: return {0:1}
    n=len(cr)
    res=[]
    for p in PRIMES:
        xs=list(range(1,n+1)); ys=[]
        for x in xs:
            M,_=alex.alex_matrix(cr,x)
            ys.append(det_mod([r[:-1] for r in M[:-1]],p))
        res.append(interp_mod(xs,ys,p))
    # CRT
    Ptot=1
    for p in PRIMES: Ptot*=p
    coeffs=[]
    for k in range(n):
        x=0
        for p,c in zip(PRIMES,res):
            q=Ptot//p; x=(x+c[k]*q*pow(q,p-2,p))%Ptot
        if x>Ptot//2: x-=Ptot
        coeffs.append(x)
    P={i:c for i,c in enumerate(coeffs) if c}
    if not P: return None
    lo,hi=min(P),max(P)
    if (lo+hi)%2: return None
    mid=(lo+hi)//2; P={e-mid:c for e,c in P.items()}
    s=sum(P.values())
    if s not in (1,-1): return None
    P={e:s*c for e,c in P.items()}
    if any(P.get(e,0)!=P.get(-e,0) for e in P): return None
    return P
def conway_a2a4(D):
    """Delta(e^h) = 1 + a2 z^2 + a4 z^4 + ..., z^2 = h^2 + h^4/12 + ...  =>  a2 = mu2/2, a4 = mu4/24 - a2/12."""
    mu2=sum(c*e**2 for e,c in D.items()); mu4=sum(c*e**4 for e,c in D.items())
    a2=Fr(mu2,2); a4=Fr(mu4,24)-a2/12
    return a2,a4

def Kinv(word, with_alex=False):
    V=VK(word)
    if V is None: return None
    a2,v3,j4=vinv(V)
    out=dict(V=V,a2=a2,v3=v3,j4=j4)
    if with_alex:
        D=alexander(word)
        if D is None: return None
        a2c,a4=conway_a2a4(D)
        out.update(Delta=D,a2c=a2c,a4=a4)
    return out
def M4loc(a2,a4,j4): return -1440*a2*a2-1440*a4+864*j4-120*a2
def all_vals(word, with_alex=False):
    J=lp.J(word)
    if J is None: return None
    K=Kinv(word,with_alex)
    if K is None: return None
    out=dict(J=J,M2=mom(J,2),M3=mom(J,3),M4=mom(J,4),M5=mom(J,5),N1=nmom(J,1),N2=nmom(J,2),N3=nmom(J,3))
    out.update(K)
    out['D']=Fr(out['M3']-432*K['v3'],180)
    # F4 residue mod 1440 does not need a4 (coefficient -1440): G4 := M4 + 1440 a2^2 - 864 j4 + 120 a2
    out['G4']=out['M4']+1440*K['a2']**2-864*K['j4']+120*K['a2']
    if with_alex: out['F4']=Fr(out['M4']-M4loc(K['a2'],K['a4'],K['j4']),1440)
    return out

# ---------- my own random half-word generator (wider diagrams, many windings)
def gen2(rnd, L, maxw=7, pw=0.35):
    hw=1; w=['s']
    for _ in range(L):
        r=rnd.random()
        opts=[]
        if r<pw: opts=[('x0',),('y0',)]
        else:
            r2=rnd.random()
            if r2<0.55 and hw>=2:
                i=rnd.randint(1,hw-1); opts=[('x%d'%i,),('y%d'%i,)]
            elif r2<0.8 and hw+2<=maxw:
                i=rnd.randint(1,hw+1); opts=[('l%d'%i,),('r%d'%i,)]
            elif hw>=3:
                i=rnd.randint(1,hw-1); opts=[('u%d'%i,)]
            else:
                i=rnd.randint(1,hw+1); opts=[('r%d'%i,)]
        tok=rnd.choice(opts)[0]
        if tok[0]=='u': hw-=2
        elif tok[0] in 'lr': hw+=2
        w.append(tok)
    while hw>1:
        i=rnd.randint(1,hw-1); w.append('u%d'%i); hw-=2
    return '.'.join(w)
def flip(tokens, idxs):
    t=list(tokens)
    for i in idxs:
        a=t[i]; t[i]=('y' if a[0]=='x' else 'x')+a[1:]
    return '.'.join(t)
