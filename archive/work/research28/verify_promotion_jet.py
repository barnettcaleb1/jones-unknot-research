#!/usr/bin/env python3
"""Exact low-color input check. Clasper realization is a cited theorem.

This portable check needs no packages or other files. The full independent
braid computation is work/proof12/braid/all_color_collision_check.py.
"""
from collections import defaultdict
from fractions import Fraction
from math import factorial
import json
from pathlib import Path

def add(a,b):
    c=defaultdict(int,a)
    for e,v in b.items(): c[e]+=v
    return {e:v for e,v in c.items() if v}

def mul(a,b):
    c=defaultdict(int)
    for e,v in a.items():
        for f,w in b.items(): c[e+f]+=v*w
    return {e:v for e,v in c.items() if v}

def shift(a,k): return {e+k:v for e,v in a.items()}

uk={40:1,32:-1,30:-1,28:-1,14:1,12:1,10:1,8:1,6:1}
ul={44:1,40:-1,30:-1,24:-1,16:1,14:1,10:1,6:1,0:2,-4:-1}
du=add(uk,{e:-c for e,c in ul.items()})
jet=[Fraction(sum(c*e**j for e,c in du.items()),factorial(j)) for j in range(6)]
assert jet[:5]==[0]*5 and jet[5]==-30720
reduced_h5=jet[5]/3/Fraction(-2)**5
assert reduced_h5==320

# q=u^-2, so an even u exponent e becomes q exponent -e/2.
assert all(e%2==0 for e in du)
dq={-e//2:c for e,c in du.items()}
da2=shift(mul(mul({2:1,0:-1},{3:1,0:1}),{5:1,0:1}),-15)
p32=mul({3:1,-3:1,1:-1,-1:-1},{3:1,-3:1,2:-1,-2:-1})
assert mul(mul(da2,p32),{1:1,0:1,-1:1})==dq
assert sum(da2.values())==0
assert sum(e*c for e,c in da2.items())==8

out={
    'ordinary_Jones_q':{-2:1,-4:1,-5:-1,-6:1,-7:-1},
    'unreduced_difference_h5_u_variable':str(jet[5]),
    'reduced_color3_h5_q_variable':str(reduced_h5),
    'Habiro_a2_difference':da2,
    'all_color_fifth_coefficient':'8*(m*m-1)*(m*m-4)',
    'Casimir_image':'8*c*(c-3), c=m*m-1; inferred by the all-color proof',
    'geometric_step':'Habiro Theorems5.4 and6.18, not computed by this script',
}
span_k=max(uk)-min(uk)
span_l=max(ul)-min(ul)
assert (span_k,span_l)==(34,48)
assert span_k < span_l  # UK/UL cannot be a Laurent polynomial.
out['completed_ratio_color3_span_obstruction']={
    'numerator_span':span_k,'denominator_span':span_l,
    'would_be_Laurent_quotient_span':span_k-span_l,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: exact color-three coefficient320 and cyclotomic coefficient8; no color scan.')
