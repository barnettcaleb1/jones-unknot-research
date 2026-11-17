import itertools, sys
from fractions import Fraction as Fr
sys.path.insert(0,'.')
from burau import alex_val, perm_cycles
def target_val(t,p,q):
    t=Fr(t); return (t**(p*q)-1)*(t-1)/((t**p-1)*(t**q-1))
def is_unit_multiple(v,tv,t):
    if tv==0 or v==0: return False
    x=abs(v/tv)
    for _ in range(200):
        if x==1: return True
        if x>1: x/=t
        else: x*=t
    return False
def search(n,onaxis_pi,onaxis_0,L,p,q,limit=10):
    hits=[]
    for gam in itertools.product(range(1,n),repeat=L):
        w=list(onaxis_0)+list(gam)+list(onaxis_pi)+list(gam)[::-1]
        if perm_cycles(n,w)!=1: continue
        if all(is_unit_multiple(alex_val(n,w,t),target_val(t,p,q),Fr(t)) for t in (2,3)):
            if is_unit_multiple(alex_val(n,w,5),target_val(5,p,q),Fr(5)):
                hits.append(gam)
                if len(hits)>=limit: break
    return hits
if __name__=='__main__':
    # sanity: 3 strands T(3,4): w = s2 gamma s2 rev(gamma), |gamma|=3
    print('T(3,4) 3-braid:',search(3,[2],[2],3,3,4))
    print('T(3,5) 3-braid:',search(3,[2],[2],4,3,5))
    print('T(4,5) as 5-braid:',search(5,[2,4],[2,4],6,4,5))
