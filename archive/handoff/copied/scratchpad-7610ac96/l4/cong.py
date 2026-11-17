"""L4 arithmetic probe: for random strongly invertible knots (kht++ half-diagram words), compute
normalized J (J = 1 mod (t+1)^2) and normalized V_K (V(1)=1, V'(1)=0), then test candidate identities
J(z) = F(V_K(z^k)) at primitive n-th roots z, n = 3..40. Pure python + cmath."""
import sys, random, cmath
sys.path.insert(0,'$HOME/jones-lanes/theory-restart/tools')
import alex, kauffman, flat_search as fs
from fractions import Fraction

def norm_poly_at(P, at, dpoint):
    """P: dict exponent(Fraction)->int. find unit s*t^k (k integer shift so exponents integral) with P(at)=1 and P'(at)=0"""
    pass

def to_t(p, sgn):
    # p: dict A-exponent -> coeff ; t = A^(sgn*4)
    e0=min(p)
    out={}
    for e,c in p.items():
        f=Fraction(e-e0, 4*sgn)
        out[f]=out.get(f,0)+c
    return out

def ev(P, z):
    return sum(c*z**float(e) if e.denominator!=1 else c*z**int(e) for e,c in P.items())

def deriv_at(P, z):
    return sum(c*float(e)*z**(float(e)-1) for e,c in P.items())

def normalize_V(P):
    # all exponents should be congruent mod 1 after shift; shift to integers
    es=list(P); base=min(es)
    Q={e-base:c for e,c in P.items()}
    if any(e.denominator!=1 for e in Q): return None
    Q={int(e):c for e,c in Q.items()}
    s=sum(Q.values())
    if abs(s)!=1: return None
    Q={e:c*s for e,c in Q.items()}       # now Q(1)=1
    d=sum(e*c for e,c in Q.items())      # Q'(1)
    return {e-d:c for e,c in Q.items()}  # shift by t^-d makes derivative 0 at 1

def normalize_J(P):
    es=list(P); base=min(es)
    Q={e-base:c for e,c in P.items()}
    if any(e.denominator!=1 for e in Q): return None
    Q={int(e):c for e,c in Q.items()}
    s=sum(c*(-1)**e for e,c in Q.items())
    if abs(s)!=1: return None
    Q={e:c*s for e,c in Q.items()}      # Q(-1)=1
    # derivative at -1 of t^k Q: k*(-1)^(k-1)*Q(-1)+(-1)^k Q'(-1)  -> choose k with value 0
    dq=sum(c*e*(-1)**(e-1) for e,c in Q.items())
    # (t^k Q)'(-1) = (-1)^(k-1) [k - dq*(-1)... ] compute directly
    for k in range(-200,201):
        R={e+k:c for e,c in Q.items()}
        v=sum(c*(-1)**e for e,c in R.items())
        dv=sum(c*e*(-1)**(e-1) for e,c in R.items())
        if v==1 and dv==0: return R
        if v==-1 and dv==0: return {e:-c for e,c in R.items()}
    return None

def get(word):
    half=alex.parse(word); full=alex.symmetrize(half)
    if full is None or alex.diagram(full) is None: return None
    kb=kauffman.bracket(word)
    bv=fs.bracket_vector(half)
    if kb is None or bv is None: return None
    y,x=bv
    u={}; fs.padd(u,y); fs.padd(u,fs.pdelta(x))
    u={e:c for e,c in u.items() if c}
    if len(u)!=1: return None
    (eu,cu),=u.items()
    Jraw={}
    for e,c in y.items():
        if c:
            f=Fraction(e-eu,4); Jraw[f]=Jraw.get(f,0)+c*cu
    J=normalize_J(Jraw)
    V=normalize_V(to_t(kb,-1))
    if J is None or V is None: return None
    return J,V

if __name__=='__main__':
    rnd=random.Random(int(sys.argv[1])); N=int(sys.argv[2])
    data=[]; seen=set()
    while len(data)<N:
        w=fs.gen(rnd,rnd.randint(4,14))
        if not w or w in seen: continue
        seen.add(w)
        r=get(w)
        if r is None: continue
        J,V=r
        if len(V)==1: continue
        data.append((w,J,V))
    import json
    json.dump([(w,{str(k):v for k,v in J.items()},{str(k):v for k,v in V.items()}) for w,J,V in data],open(sys.argv[3],'w'))
    print('collected',len(data))
