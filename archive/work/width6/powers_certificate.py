"""Finite exact Cayley-Hamilton certificate for two all-powers bracket families."""
import json
from pathlib import Path
from collections import defaultdict
import probe as p
import kernel_words as k
STATES=p.rc.basis(6,3)
INDEX={s:i for i,s in enumerate(STATES)}
TRANS=[[(INDEX[t],l) for t,l in (p.rc.transition(s,i) for s in STATES)]for i in range(5)]
def filled(s):
    s=list(s);a,b=[i for i,x in enumerate(s) if x==-1];s[a]=b;s[b]=a;return tuple(s)
def numerator_bracket(word,i,j):
    """Unnormalized closure: EVERY circle contributes delta."""
    initial=filled(p.STATES[j]);top=filled(p.STATES[i])
    v=[{}for _ in STATES];v[INDEX[initial]]={0:1}
    for x in reversed(word):
        sign=1 if x>0 else -1;new=[defaultdict(int)for _ in STATES]
        for y,q in enumerate(v):
            p.addto(new[y],q,sign);dest,loops=TRANS[abs(x)-1][y]
            p.addto(new[dest],p.delta(q)if loops else q,-sign)
        v=[p.clean(q)for q in new]
    out=defaultdict(int)
    for s,q in zip(STATES,v):
        loops=p.rc.cap_weight(s,p.caps(top))
        for _ in range(loops):q=p.delta(q)
        p.addto(out,q)
    return p.clean(out)
def main():
    rows=[]
    for i,j in [(4,5),(5,4)]:
        ids=[p.coefficient(k.BIGELOW6_REN*n,i,j)for n in range(10)]
        nums=[numerator_bracket(k.BIGELOW6_REN*n,i,j)for n in range(7)]
        assert all(x=={}for x in ids)
        assert all(x=={4:1,0:2,-4:1}for x in nums)
        rows.append({'i':i,'j':j,'id_coefficients_n0_to9':ids,
                     'numerator_unnormalized_brackets_n0_to6':nums})
    out={'seed':'BIGELOW6_REN','word':k.BIGELOW6_REN,'rows':rows,
         'statement':'For every integer n, the framed bracket of cap_I beta^n cup_J is exactly e in TL_2 for (I,J)=(4,5),(5,4).',
         'argument':'The id sequence is a matrix coefficient of invertible 9x9 rho(beta), hence obeys its degree-9 characteristic recurrence with unit constant term. Nine initial zeros force all integer terms zero. The numerator-minus-delta^2 sequence is a coefficient of diag(rho_W(6,0)(beta),1), an invertible 6x6 matrix. Six initial zeros force all integer terms zero. Writing X_n=a_n*id+b_n*e, N(X_n)=a_n*delta+b_n*delta^2, so a_n=0 and N=delta^2 imply b_n=1 in the integral domain Z[A^+-1].',
         'topology':'This is an algebraic statement only. n=1 is separately proved split by actual unlink and unknot closures plus Property R. No uniform all-n topological conclusion is asserted.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
    print(json.dumps({key:out[key]for key in ['statement','argument','topology']}))
if __name__=='__main__':main()
