"""Exact counterexample to recovering spin-one Jones from ordinary Jones.

Explicit table braids, exact TL ordinary Jones, and Jackson--Kerler spin-one
R-matrix at q=2. The RT q variable is the square root of the ordinary Jones
variable, up to mirroring; equality/inequality do not depend on that choice.
"""
from pathlib import Path
from fractions import Fraction as F
import itertools,sys,json
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'pass5'))
from braid_color3_kernel import local_R,inverse,q
sys.path.insert(0,str(ROOT.parent/'attack_search'))
import search
R=local_R();RI=inverse(R);dim=q*q+1+q**-2

def colored(word,n):
    total=F(0)
    allstates=list(itertools.product(range(3),repeat=n))
    for weight in range(2*n+1):
        states=[v for v in allstates if sum(v)==weight]
        index={v:i for i,v in enumerate(states)};d=len(states)
        M=[[F(i==j) for j in range(d)] for i in range(d)]
        for letter in word:
            i=abs(letter)-1;r=R if letter>0 else RI
            transitions=[]
            for state in states:
                a,b=state[i:i+2];tr=[]
                for c,e in itertools.product(range(3),repeat=2):
                    value=r[3*c+e][3*a+b]
                    if value:
                        dest=state[:i]+(c,e)+state[i+2:]
                        tr.append((index[dest],value))
                transitions.append(tr)
            M=[[sum(row[k]*value for k,value in tr) for tr in transitions] for row in M]
        total+=q**(2*n-2*weight)*sum(M[i][i] for i in range(d))
    writhe=sum(1 if s>0 else -1 for s in word)
    return total/(dim*q**(2*writhe))

WORDS={'5_1':[-1,-1,-1,-1,-1],
       '10_132':[-1,2,-3,-2,3,-4,3,-2,1,-3,2,-3,4,-3,-3,-2]}

if __name__=='__main__':
    for word in WORDS.values():
        n=max(abs(g) for g in word)+1
        perm=list(range(n))
        for g in word:
            i=abs(g)-1;perm[i],perm[i+1]=perm[i+1],perm[i]
        visited=set();i=0
        while i not in visited:visited.add(i);i=perm[i]
        assert len(visited)==n
    assert colored([],1)==1
    assert colored([1],2)==colored([-1],2)==1
    assert colored([1,2],3)==colored([1,-2],3)==1
    v1=search.jones_a(WORDS['5_1'],2)
    v2=search.jones_a(WORDS['10_132'],5)
    assert v1==v2
    h1=colored(WORDS['5_1'],2);h2=colored(WORDS['10_132'],5)
    assert h1!=h2
    # Also check the framing factor on this actual nontrivial five-braid.
    assert colored(WORDS['10_132']+[5],6)==h2
    assert colored(WORDS['10_132']+[-5],6)==h2
    out=dict(braids=WORDS,ordinary_Jones_in_A=v1,ordinary_Jones_equal=True,
             quantum_group_parameter_q=2,spin_one_values={'5_1':str(h1),'10_132':str(h2)},
             difference=str(h1-h2),
             normalization_checks='Unknot, both two-strand Markov stabilizations, two three-strand unknot presentations, and positive/negative stabilization of the nontrivial five-braid.',
             conclusion='Ordinary Jones equality does not imply equality of the three-dimensional colored Jones or of zero-framed two-parallel Jones polynomials.')
    (ROOT/'quantum_two_copy_test.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
