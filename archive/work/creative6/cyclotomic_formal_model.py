"""Exact formal colored-sequence countermodel; NOT a knot construction.

Python standard library only. Integer Laurent polynomials are exponent dictionaries.
The argument for all N is in cyclotomic_formal_model.txt; these are exact spot checks.
"""
from collections import defaultdict
from fractions import Fraction
import json
from pathlib import Path

def add(*ps):
    out = defaultdict(int)
    for p in ps:
        for e, c in p.items(): out[e] += c
    return {e:c for e,c in sorted(out.items()) if c}

def scale(p,c): return {e:c*v for e,v in p.items() if c*v}

def mul(p,q):
    out=defaultdict(int)
    for e,c in p.items():
        for f,d in q.items(): out[e+f] += c*d
    return {e:c for e,c in sorted(out.items()) if c}

def val(p,x): return sum(c*Fraction(x)**e for e,c in p.items())

def derivative(p,r=1):
    for _ in range(r): p={e-1:c*e for e,c in p.items() if e}
    return p

def coefficients(n):
    a=[1]
    for k in range(1,n):
        a.append(-(4*a[k-2] if k>=2 else 0)-(a[k-3] if k>=3 else 0))
    return a

def kernel(N,k):
    p={0:1}
    for j in range(1,k+1):
        p=mul(p,add({N:1,-N:1},{j:-1,-j:-1}))
    return p

def colored(N):
    a=coefficients(N)
    return add(*(scale(kernel(N,k),a[k]) for k in range(N)))

def main():
    s={1:1,0:-2,-1:1}
    delta=add({0:1},scale(mul(s,s),4),mul(mul(s,s),s))
    assert delta=={-3:1,-2:-2,-1:-1,0:5,1:-1,2:-2,3:1}
    assert val(delta,1)==val(delta,-1)==1
    assert val(derivative(delta,2),1)==0
    a=coefficients(24)
    for k in range(1,len(a)):
        assert a[k]+(4*a[k-2] if k>=2 else 0)+(a[k-3] if k>=3 else 0)==0
    assert colored(1)==colored(2)=={0:1}
    assert colored(3)==add({0:1},scale(kernel(3,2),-4))!={0:1}
    checks=[]
    for N in range(1,16):
        p=colored(N)
        assert val(p,1)==1
        assert val(derivative(p),1)==0
        assert p=={-e:c for e,c in p.items()}
        assert kernel(N,N)=={}
        checks.append({'N':N,'terms':len(p),'min_degree':min(p),'max_degree':max(p),
                       'value_at_2':str(val(p,2))})
    out={'warning':'Formal sequence only: no knot realizes it in this work.',
         'delta':delta,'cyclotomic_coefficients':a,'F3':colored(3),'checks':checks}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'a_first_10':a[:10],'F1':colored(1),'F2':colored(2),
                      'F3':colored(3),'checked_N':15,'delta':delta},indent=2))

if __name__=='__main__': main()
