"""Exact checks behind the all-color Kinoshita--Terasaka-family obstruction.

The all-integer/all-color proof is symbolic and recorded in braid_notes.md.
This certificate verifies the source's factorization and derivatives, and
cross-checks its k=2 member by an independent Temperley--Lieb braid closure.
No floating-point arithmetic or bounded search is used in the proof.
"""
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import json, math, sys

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'attack_search'))
import search

def clean(p):return {e:c for e,c in p.items() if c}
def add(*ps):
    r=defaultdict(int)
    for p in ps:
        for e,c in p.items():r[e]+=c
    return clean(r)
def mul(a,b):
    r=defaultdict(int)
    for e,c in a.items():
        for f,d in b.items():r[e+f]+=c*d
    return clean(r)
def exp_jet(p,degree):
    return [sum(Fraction(c*e**j,math.factorial(j)) for e,c in p.items())
            for j in range(degree+1)]

f={-4:1}
for factor in [{2:1,0:1},{2:1,1:-2,0:1},{2:1,1:1,0:1},{2:1,1:-1,0:1}]:
    f=mul(f,factor)
assert f=={-4:1,-3:-2,-2:3,-1:-4,0:4,1:-4,2:3,3:-2,4:1}
assert { -e:c for e,c in f.items()}==f
fj=exp_jet(f,4)
assert fj[:4]==[0,0,6,0]

def ordinary(k):return add({0:1},mul(add({k:(-1 if k%2 else 1)},{0:-1}),f))

# A separately given 4-braid presentation of the Kinoshita--Terasaka knot.
kt_word=[1,1,1,3,3,2,-3,-1,-1,2,-1,-3,-2]
kt_a=search.jones_a(kt_word,4)
assert all(e%4==0 for e in kt_a)
kt={-e//4:c for e,c in kt_a.items()}
assert kt==ordinary(2)
assert ordinary(0)=={0:1}
assert exp_jet(add(ordinary(1),{0:-1}),3)==[0,0,-12,-6]
assert exp_jet(add(ordinary(2),{0:-1}),3)==[0,0,0,12]

data=dict(source='https://arxiv.org/html/0802.2283; Example 6.7, Table 2',
          factor_f=f,jet_f_at_q_equals_exp_h=[str(x) for x in fj],
          independent_KT_braid_word=kt_word,independent_KT_jones=kt,
          checks_passed=True,
          all_parameter_conclusion='For every integer k != 0 and color N >= 2, H_N(D_k) != 1.',
          exact_leading_terms={'k odd':'-4*(N^2-1)*h^2',
                               'k nonzero even':'2*k*(N^2-1)*h^3'},
          method='Habiro i>=2 terms vanish through order h^3; no bounded enumeration is needed.')
(ROOT/'braid_ribbon_filter.json').write_text(json.dumps(data,indent=2))
print(json.dumps(data,indent=2))
