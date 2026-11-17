"""Exact EKT LL1(m,n) tangle construction, read left-associatively per EKT."""
from check_links import *
from spherogram.links.tangles import IntegerTangle
import json

def dot(a,b):
    return a.invert()+b

def ll1_tangle(m,n):
    t=dot(IntegerTangle(n),IntegerTangle(1))
    block=dot(IntegerTangle(1),RationalTangle(1,2))
    for _ in range(m):
        t=dot(t,IntegerTangle(1))
        t=dot(t,RationalTangle(1,2))
    for k in [1,1,2]:t=dot(t,IntegerTangle(k))
    return t

def seed_tangle(m,n):
    t=dot(IntegerTangle(n),IntegerTangle(1))
    block=dot(IntegerTangle(1),RationalTangle(1,2))
    for _ in range(m):
        t=dot(t,IntegerTangle(1))
        t=dot(t,RationalTangle(1,2))
    return dot(t,IntegerTangle(-1))

if __name__=='__main__':
    out=[]
    for m in range(4):
      for n in range(-3,4):
        seed=seed_tangle(m,n).numerator_closure()
        seed.simplify('global')
        t=ll1_tangle(m,n)
        link=hopf(t,IntegerTangle(-3))
        pd=link.PD_code()
        r=regina.Link.fromPD([[x+1 for x in row]for row in pd])
        row={'m':m,'n':n,'seed_crossings_after_simplification':len(seed.crossings),'crossings':len(pd),'components':r.countComponents(),'jones':str(r.jones()),'H1':fox_factors(pd),'pd':pd}
        out.append(row)
        print({k:v for k,v in row.items()if k!='pd'},flush=True)
        Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
