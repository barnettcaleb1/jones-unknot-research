"""Second-order automaton for rational boxes (top end).
States: ('init',), ('R',c) c in {0,1}, ('S',j).  Returns final state and rho_a = sum of normalised 2nd coeffs of the E-denominators."""
from nt import *
from fractions import Fraction
def step(st,m):
    """returns (newstate, rhoD)"""
    if st[0]=='init':
        return (('R',1),-1) if m>=1 else (('S',0),0)
    if m>=1:
        if st[0]=='R':
            return (('R',0),0) if m==1 else (('R',1),-1)
        return (('R',1),-1)
    # negative
    if st[0]=='R':
        return (('S',0), st[1])
    j=st[1]
    if m<=-2: return (('S',0), -1 if j==0 else 0)
    return (('S',j+1), -1 if j==0 else 0)
def run(seq):
    st=('init',); rho=0
    for m in seq:
        st,r=step(st,m); rho+=r
    return st,rho
def rhoq(st):
    if st[0]=='R': return st[1]
    return -1 if st[1]==0 else 0
def c2rat(p):
    e=top(p); return Fraction(p.get(e-1,0),p[e])
if __name__=='__main__':
    import random
    rnd=random.Random(7); bad=0; n=0
    seqs=normal_seqs(4,4)
    extra=[]
    for _ in range(3000):
        k=rnd.randint(5,9); s=[rnd.choice([m for m in range(-5,6) if m]) for _ in range(k)]
        if s[0]==-1: s[0]=-2
        extra.append(tuple(s))
    for s in seqs+extra:
        u=box(s); a,b=chan(u)
        st,rho=run(s)
        ra=c2rat(a); rb=c2rat(b)
        # also check c in R state from r expansion
        ok = (ra==rho) and (rb==rho+rhoq(st))
        n+=1
        if not ok:
            bad+=1
            if bad<10: print('BAD',s,st,rho,ra,rb)
    print('checked',n,'bad',bad)
