import sys
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import kauffman
def VK(word):
    kb=kauffman.bracket(word)
    if not kb: return None
    es=sorted(kb); r=es[0]%4
    if any((e-r)%4 for e in es): return None
    V={-(e-r)//4:c for e,c in kb.items()}
    s=sum(V.values())
    if s not in (1,-1): return None
    V={e:c*s for e,c in V.items()}; d=sum(e*c for e,c in V.items())
    return {e-d:c for e,c in V.items()}
def der(V,k):
    tot=0
    for e,c in V.items():
        f=1
        for i in range(k): f*=(e-i)
        tot+=c*f
    return tot
def a2(V): return Fr(-der(V,2),6)
def v3(V): return Fr(-(der(V,3)+3*der(V,2)),36)
