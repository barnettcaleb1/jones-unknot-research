"""Verify an exact degree obstruction for arbitrary words in two kernel blocks.

For P=sigma2^-1 K sigma2 and Q=P(sigma2 K sigma2^-1)P, any nonempty
positive word W(P,Q) has Jones lowest t-degree 3-37a-112b after closing
W sigma1 sigma2 sigma3 sigma4; a,b count P,Q. Thus it is never Jones-one.
"""
from braid_leading import *
import random

def pmul(p,q):return tuple(p[q[i]] for i in range(len(p)))
def pinv(p):return tuple(p.index(i) for i in range(len(p)))
def hurwitz(word,initial):
    state=list(initial)
    for s in word:
        i=abs(s)-1;a,b=state[i],state[i+1]
        if s>0:state[i],state[i+1]=pmul(pmul(a,b),pinv(a)),a
        else:state[i],state[i+1]=b,pmul(pmul(pinv(b),a),b)
    return state

def run():
    Pword=bk.reduce([-2]+bk.KERNEL+[2])
    Rword=bk.reduce([2]+bk.KERNEL+[-2])
    Qword=bk.reduce(Pword+Rword+Pword)
    Pm,Rm=tl.rho(Pword),tl.rho(Rword)
    Qm=tl.matmul(tl.matmul(Pm,Rm),Pm)
    L=[[0]*5 for _ in range(5)];L[2][2]=-1;L[2][4]=1
    LR=[[0]*5 for _ in range(5)];LR[4][2]=1
    assert lead(Pm)==(148,L)
    assert lead(Rm)==(152,LR)
    assert lead(Qm)==(448,L)
    # Integer leading matrices: L^2=-L, and tr(L*lead(C))=1.
    def imul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(5)) for j in range(5)] for i in range(5)]
    assert imul(L,L)==[[-x for x in row] for row in L]
    dc,LC=lead(tl.rho(bk.ANCHOR));assert dc==0
    assert sum(imul(L,LC)[i][i] for i in range(5))==1
    assert tl.trace(tl.rho(bk.ANCHOR))=={}
    assert bk.identity(bk.burau(Pword)) and bk.identity(bk.burau(Rword))
    assert bk.permutation(Pword)==list(range(5)) and bk.permutation(Rword)==list(range(5))
    examples=[]
    for letters in [(0,),(1,),(0,1),(1,0),(0,1,0)]:
        w=sum((Pword if s==0 else Qword for s in letters),[])+bk.ANCHOR
        v=bk.search.jones_a(w,5)
        a=letters.count(0);b=letters.count(1)
        assert max(v)==148*a+448*b-12
        assert v[max(v)]==(-1)**(len(letters)-1)
        examples.append(dict(letters=list(letters),max_A_degree=max(v),leading_coefficient=v[max(v)]))
    rng=random.Random(20261031);initial=[]
    for _ in range(5):
        p=list(range(7));rng.shuffle(p);initial.append(tuple(p))
    commutator=bk.comm(Pword,Qword);result=hurwitz(commutator,initial)
    assert result!=initial,'Choose a larger finite quotient if this witness happens to vanish.'
    report=dict(P=Pword,R=Rword,Q=Qword,degrees=[148,152,448],leading_P_Q=L,
                leading_R=LR,anchor=bk.ANCHOR,leading_anchor=LC,
                formula_lowest_t_degree='3-37*a-112*b',examples=examples,
                noncommutativity_witness=dict(group='S7',input=initial,output=result),
                conclusion='Every nonempty positive word in P,Q closes with C to a nontrivial Jones polynomial.')
    (ROOT/'braid_obstruction_certificate.json').write_text(json.dumps(report,indent=2))
    print('Verified arbitrary-word obstruction, five full Jones cross-checks, and P,Q noncommutativity.',flush=True)
    return report

if __name__=='__main__':run()
