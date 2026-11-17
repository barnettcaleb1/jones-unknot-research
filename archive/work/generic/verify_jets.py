"""Replay the exact Jones commutator calculations (Python standard library).

Place tl_exact.py and commutator_jets.json alongside this file.
The unbounded result is proved in the accompanying note; this checks r=1,...,8.
"""
import json
from pathlib import Path
from tl_exact import jones_a, knot

def inverse(word):
    return [-x for x in reversed(word)]

def free_reduce(word):
    result=[]
    for x in word:
        if result and result[-1]==-x:
            result.pop()
        else:
            result.append(x)
    return result

def binomial(n,k):
    value=1
    for j in range(k):
        value=value*(n-j)//(j+1)
    return value

rows=json.loads(Path(__file__).with_name('commutator_jets.json').read_text())
c=[1,1]
b=[2,2]
for row in rows:
    r=row['r']
    word=free_reduce(c+[1,2])
    assert word==row['word']
    assert knot(word,3)
    polynomial=jones_a(word,3)
    assert polynomial=={int(k):v for k,v in row['jones_A'].items()}
    assert polynomial!={0:1}
    defect=polynomial.copy()
    defect[0]=defect.get(0,0)-1
    jet=[sum(a*binomial(e,j) for e,a in defect.items()) for j in range(2*r+5)]
    order=next(j for j,a in enumerate(jet) if a)
    assert order==row['first_nonzero_Taylor_degree'] and order>=r
    assert jet[order]==row['leading_Taylor_coefficient']
    if r%2==0:
        m=r//2
        assert order==r
        assert jet[r]==-48*64**(m-1)
        assert jet[r]//4**r==-3*4**(m-1)
    print('r =',r,'word length =',len(word),'first nonzero A-1 degree =',order)
    c=free_reduce(c+b+inverse(c)+inverse(b))
print('All 8 exact Jones polynomials and Taylor orders match the saved data.')
