"""Check the general opposite-omega orbit formula against full link diagrams."""
from check_links import *
from spherogram.links.tangles import IntegerTangle, InfinityTangle
import json

def omega(t,sign=1):
    return ((t+IntegerTangle(2*sign))*IntegerTangle(sign))+IntegerTangle(2*sign)

def iterate(t,n):
    for _ in range(abs(n)):t=omega(t,1 if n>0 else -1)
    return t

def pell(n):
    a,b=1,0
    for _ in range(abs(n)):a,b=3*a+8*b,a+3*b
    return a,b if n>=0 else -b

if __name__=='__main__':
    out=[]
    for k in range(-2,3):
      for n in [-2,-1,1,2]:
        a,b=pell(n)
        D=1+12*b*(b+a*k)
        t=iterate(RationalTangle(1,k),n)
        u=iterate(InfinityTangle()+IntegerTangle(2),-n)
        link=hopf(t,u)
        pd=link.PD_code()
        h=fox_factors(pd)
        assert h==([abs(D)],1),(k,n,h,D)
        r=regina.Link.fromPD([[x+1 for x in row] for row in pd])
        out.append(dict(k=k,n=n,a=a,b=b,D=D,H1=h,pd=pd,jones=str(r.jones())))
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
    print('All',len(out),'full-diagram opposite-omega checks passed, including positive and negative iterates.')
