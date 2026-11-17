# Claims 9/11: local-knot inversions. Own long-knot half-words from closed Morse diagrams; lp.J vs own J_3 (KL), t -> 1/t;
# product formula J(K0 with L tied into the arc near the top vertex) = J(K0) * J_3(L)(1/t).
import sys, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, alex
from rlib import *
from gens import sample
def longknot_letters(ops, kink='x'):
    """closed ops (first ('cap',0), last ('cup',0)) -> half-word letters (no 's'); T-strand at half position 0"""
    assert ops[-1]==('cup',0)
    out=[]
    for c,i in ops[:-1]:
        if c=='cap': out.append('l%d'%(i+2))
        elif c=='cup': out.append('u%d'%(i+2))
        else: out.append('%s%d'%(c,i+2))
    out+=[kink+'1','u2']
    return out
def inv(P): return {-e:c for e,c in P.items()}
KN={'3_1':(2,[1,1,1]),'3_1*':(2,[-1,-1,-1]),'4_1':(3,[1,-2,1,-2]),'5_2':(3,[1,1,1,2,-1,2]),'6_1':(4,[1,1,2,-1,-3,2,-3]),
    '6_2':(3,[1,1,1,-2,1,-2]),'6_3':(3,[1,1,-2,1,-2,-2]),'T(3,4)':(3,[1,2]*4)}
if __name__=='__main__':
    res=[]
    for name,(n,w) in KN.items():
        ops=braid_ops(n,w); J3L=J3(ops)
        for kink in 'xy':
            hw='s.'+'.'.join(longknot_letters(ops,kink))
            J=lp.J(hw)
            res.append((name,kink,J==inv(J3L)))
            print(name,kink,hw,' lp.J == J_3(L)(1/t):',J==inv(J3L), '' if J==inv(J3L) else (sorted(J.items()) if J else None, sorted(inv(J3L).items())))
    # Alexander check on two
    for name in ('3_1','4_1'):
        n,w=KN[name]; hw='s.'+'.'.join(longknot_letters(braid_ops(n,w)))
        print(name,'Delta(K) =',alex.alex_poly(hw))
    # product formula
    rnd=random.Random(404); ok=bad=0
    Ls=[('3_1',J3(braid_ops(2,[1,1,1])),longknot_letters(braid_ops(2,[1,1,1]))),('4_1',J3(braid_ops(3,[1,-2,1,-2])),longknot_letters(braid_ops(3,[1,-2,1,-2]))),
        ('5_2',J3(braid_ops(3,[1,1,1,2,-1,2])),longknot_letters(braid_ops(3,[1,1,1,2,-1,2])))]
    done=0
    while done<24:
        w0=sample(rnd,rnd.choice(['long','mont']))
        if not w0: continue
        J0=lp.J(w0)
        if J0 is None: continue
        name,J3L,lw=rnd.choice(Ls)
        t=w0.split('.'); hw='.'.join(['s']+lw+t[1:])
        J=lp.J(hw)
        if J is None: continue
        done+=1
        pred=lp.normalize(P_mul(J0,inv(J3L)))
        if J==pred: ok+=1
        else: bad+=1; print('PRODUCT FAIL',w0,name)
    print('product formula: ok',ok,'bad',bad)
