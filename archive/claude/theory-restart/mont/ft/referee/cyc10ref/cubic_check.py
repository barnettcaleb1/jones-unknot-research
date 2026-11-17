# Referee: check M_3/36 = 7 v_3 mod 5 and the full cubic jet J(-e^h) = V_K(e^{2h}) mod (5,h^4) on random words.
import sys, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, flat_search as fs, kauffman
from fractions import Fraction as Fr
from math import factorial
def VK(word):
    kb=kauffman.bracket(word)
    if not kb: return None
    kb={e:c for e,c in kb.items() if c}; es=sorted(kb); r=es[0]%4
    if any((e-r)%4 for e in es): return None
    V={-(e-r)//4:c for e,c in kb.items()}; s=sum(V.values())
    if s not in (1,-1): return None
    V={e:c*s for e,c in V.items()}; d=sum(e*c for e,c in V.items())
    return {e-d:c for e,c in V.items()}
def jet(P,base,scale,k):   # [h^k] P(base*e^{scale h}) exactly
    return sum(Fr(c*(base**(e%2))*(scale*e)**k,factorial(k)) for e,c in P.items())
def mod5(x):  # x in Z_(5): residue
    return (x.numerator*pow(x.denominator,-1,5))%5
rnd=random.Random(int(sys.argv[1])); n=0; bad=0; badjet=0; iotas={}
while n<int(sys.argv[2]):
    w=fs.gen(rnd,rnd.randint(6,18))
    if not w: continue
    J=lp.J(w)
    if J is None: continue
    V=VK(w)
    if V is None: continue
    n+=1
    M3=sum(c*(-1)**(e%2)*e**3 for e,c in J.items())
    d2=sum(c*e*(e-1) for e,c in V.items()); d3=sum(c*e*(e-1)*(e-2) for e,c in V.items())
    v3=Fr(-(d3+3*d2),36)
    assert M3%36==0 and v3.denominator==1
    iota=Fr(M3//36-7*v3,5)
    if iota.denominator!=1: bad+=1
    iotas[iota]=iotas.get(iota,0)+1
    if any(mod5(jet(J,-1,1,k)-jet(V,1,2,k)) for k in range(4)): badjet+=1
print('samples',n,' iota non-integral:',bad,' cubic jet mismatch mod 5:',badjet)
print(' iota distribution (first 10):',sorted(((int(k),v) for k,v in iotas.items()),key=lambda kv:-kv[1])[:10])
