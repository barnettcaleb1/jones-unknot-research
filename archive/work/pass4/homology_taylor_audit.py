"""Independent moment audit for every companion in the odd-p,q Ren family."""
from collections import defaultdict
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
from ren_jones_locus import poly, fa

def moment(terms,r,nvars):
    out=defaultdict(int)
    def compositions(total,parts):
        if parts==1:
            yield(total,);return
        for i in range(total+1):
            for tail in compositions(total-i,parts-1):yield(i,)+tail
    for exponents,c in terms.items():
        for powers in compositions(r,nvars+1):
            coeff=c*factorial(r)
            for power in powers:coeff//=factorial(power)
            for base,power in zip(exponents,powers):coeff*=base**power
            out[powers[:-1]]+=coeff
    return {e:c for e,c in out.items() if c}

def add(*ps):
    q=defaultdict(int)
    for p in ps:
        for e,c in p.items():q[e]+=c
    return {e:c for e,c in q.items() if c}
def mul(p,q):return add(*({e+f:c*d} for e,c in p.items() for f,d in q.items()))
def power(p,n):
    q={0:1}
    for _ in range(n):q=mul(q,p)
    return q
def substitute(moment,params):
    result={}
    for exps,c in moment.items():
        term={0:c}
        for p,e in zip(params,exps):term=mul(term,power(p,e))
        result=add(result,term)
    return result

M2,M3=[moment(poly,r,3) for r in (2,3)]
Fa1=moment({(a,b,c,e):v for (a,b,c,e),v in fa.items()},1,3)
assert Fa1=={(0,0,0):-16,(0,1,0):-16,(1,0,0):-16}
# p=320r²+32r−1, q=−320r²+32r+1; m=(p−1)/2,l=(q−1)/2.
params=[{2:160,1:16,0:-1},{2:-160,1:16},{3:800,1:-7}]
assert substitute(M2,params)=={}
third=substitute(M3,params)
assert third=={1:2496,3:2370048,5:-169574400,7:2949120000}
required_H2={e-1:Q(c,18*64) for e,c in third.items()}
assert required_H2=={0:Q(13,6),2:Q(6172,3),4:Q(-147200),6:Q(2560000)}
numerator={e:int(6*c) for e,c in required_H2.items()}
assert numerator[0]%2==1 and all(c%2==0 for e,c in numerator.items() if e)
Szero=substitute(M3,[{0:-1},{},{1:1}])
assert Szero=={1:-576}

# Independent direct verification of the parameterized determinant relation.
p,q,n=[{2:320,1:32,0:-1},{2:-320,1:32,0:1},{3:800,1:-7}]
S=add(p,q);D=add(p,{e:-c for e,c in q.items()})
det=add({0:36},{e:30*c for e,c in D.items()},
        {e:-25*c for e,c in mul(p,q).items()},
        {e:-50*c for e,c in mul(S,n).items()})
assert det=={0:1}

result={'Fa_first_A_log_moment':{'m^%s_l^%s_n^%s'%e:c for e,c in Fa1.items()},
        'parameterization':{'p':'320r^2+32r-1','q':'-320r^2+32r+1','n':'800r^3-7r'},
        'G2_on_parameter_family':{},'determinant_signed_core_on_family':1,
        'G3_on_parameter_family':third,
        'required_log_second_derivative_H3':{e:str(c) for e,c in required_H2.items()},
        'six_times_required_H3_second_derivative':numerator,
        'numerator_always_odd':True,'G3_at_p_minus1_q1':Szero,
        'conclusion':'Jones one for any companion requires p=-1,q=1,n=0; then reduced color-three Jones of the companion must be one.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
