"""Exact determinants and divisibility for all Ren-pattern satellites/twists."""
from pathlib import Path
from fractions import Fraction
import json, sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'braid_classification/packages'))
from spherogram import Link
data=json.loads(Path(__file__).resolve().parents[1].joinpath('pass3/tangle_ren_check.json').read_text())
L=Link(data['PD_source'])
assert L.linking_number()==0
a={int(e)//4:c for e,c in data['annular_bracket_coefficients']['2'].items()}
b={int(e)//4:c for e,c in data['annular_bracket_coefficients']['0'].items()}
V={int(e)//4:c for e,c in data['Jones_K_in_A'].items()}
assert all(int(e)%4==0 for e in data['annular_bracket_coefficients']['2'])
def ev(p,x):return sum(Fraction(c)*Fraction(x)**e for e,c in p.items())
def add(*ps):
    q={}
    for p in ps:
        for e,c in p.items():q[e]=q.get(e,0)+c
    return {e:c for e,c in q.items() if c}
def mul(p,q):return add(*({e+f:c*d} for e,c in p.items() for f,d in q.items()))
def scale(p,c):return {e:c*d for e,d in p.items()}
def shift(p,n):return {e+n:c for e,c in p.items()}
def divrem_laurent(p,q):
    # q has unit leading coefficient. Move both polynomials to ordinary powers;
    # the remainder is enough to test divisibility in Q[x,x^-1].
    p=shift(p,-min(p));q=shift(q,-min(q));r=p.copy();out={}
    while r and max(r)>=max(q):
        e=max(r)-max(q);c=Fraction(r[max(r)],q[max(q)])
        out[e]=c;r=add(r,scale(shift(q,e),-c))
    return out,r
q2={1:1,0:1,-1:1} # Delta_2=delta^2-1
target=add({2:-1,1:-1},scale(add(a,b),-1)) # A^6 delta-(a+b)
quot,rem=divrem_laurent(target,a)
assert rem
assert ev(V,-1)==-11 and ev(a,-1)==50
# C2 = a Delta2/(A^6 delta) = -a Delta2/[x(x+1)].
# For every integer n, (x^(2n)-1)/(x+1) evaluates to -2n at x=-1.
# Thus (x^(2n)-1) C2 at x=-1 is 2n*a(-1)*Delta2(-1)/(-1)=100n.
slope=2*ev(a,-1)*ev(q2,-1)/(-1)
assert slope==100
samples={}
for n in range(-3,4):
    # Independently divide the vanishing factor by x+1 before evaluation.
    diff=add({2*n:1},{0:-1})
    if not diff:
        correction=Fraction(0)
    else:
        offset=min(diff)
        ordinary=shift(diff,-offset);divisor={1:1,0:1};r=ordinary.copy();quot={}
        while r and max(r)>=1:
            e=max(r)-1;c=r[max(r)];quot[e]=c
            r=add(r,scale(shift(divisor,e),-c))
        assert not r
        quotient=shift(quot,offset)
        correction=-ev(quotient,-1)*ev(a,-1)*ev(q2,-1)/(-1)
    value=ev(V,-1)+correction
    assert value==100*n-11
    samples[str(n)]=int(value)
res={'source':'https://arxiv.org/html/2609.11084v2',
     'axis_linking_number':L.linking_number(),'pattern_winding':0,
     'a_at_A4_minus1':50,'Jones_at_minus1_before_twist':-11,
     'Jones_at_minus1_after_n_twists':'100*n-11',
     'determinant_all_zero_framed_companions':'abs(100*n-11)',
     'integer_n_can_have_determinant_one':False,
     'twist_convention':'positive n acts on S_2 by A^(8n)',
     'exact_twist_samples':samples,
     'independent_divisibility_obstruction':bool(rem),
     'ordinary_polynomial_division_remainder':{str(e):str(c) for e,c in rem.items()}}
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
