"""Identify K for vertical closures V_a(Y^N u_1...u_n) of rational boxes with the arborescent knot
   N( 1/a  +  rot( R_1 + ... + R_n + [N] )  +  1/a ),   R_i = rational tangle of slope s(u_i) (nest Lemma L),
built independently with spherogram's tangle algebra; compare Jones polynomials (regina) up to mirror, over sign conventions."""
import sys, random, itertools
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import bk, vc, lp, a2search
import spherogram as sg
from spherogram import RationalTangle as RT
import regina

def halfword(a,N,boxes):
    body=[]
    if N>0: body+=['y0']*N
    elif N<0: body+=['x0']*(-N)
    for w in boxes: body.append(vc.ratbody(w))
    return vc.vert_word(a,'.'.join(body))

def jones_of_pd(pd):
    return bk.jones_t(regina.Link.fromPD(pd))

def mirror(V): return {-e:c for e,c in V.items()}

def tangle_link(a,N,slopes,conv):
    sa,ss,sN,rot=conv
    Rs=[RT(sa*1,a)]
    inner=None
    for s in slopes:
        s=ss*s
        T=RT(s.numerator,s.denominator)
        inner=T if inner is None else inner+T
    if N: inner=inner+RT(sN*N,1)
    M=inner.rotate(rot)
    T=RT(sa*1,a)+M+RT(sa*1,a)
    return T.numerator_closure()

def spec_ok(L):
    return len(L.link_components)==1

if __name__=='__main__':
    rnd=random.Random(int(sys.argv[1]) if len(sys.argv)>1 else 1)
    W=list(a2search.words(4).values())
    convs=list(itertools.product((1,-1),(1,-1),(1,-1),(1,-1)))
    score={c:0 for c in convs}; tested=0
    for trial in range(12):
        n=rnd.choice([1,2,2,3]); boxes=[rnd.choice(W) for _ in range(n)]
        a=rnd.choice([3,-3,5,-5]); N=rnd.randint(-2,2)
        hw=halfword(a,N,boxes)
        pdK=bk.pd_code(bk.full_K(hw))
        if pdK is None: print('not a knot?',hw); continue
        VK=jones_of_pd(pdK)
        Jw=lp.J(hw); Jf=vc.J_vert(a,vc.Ypow(N,vc.starall([vc.rat(w) for w in boxes])))
        slopes=[a2search.slope(w) for w in boxes]
        ok=[]
        for c in convs:
            L=tangle_link(a,N,slopes,c)
            if not spec_ok(L): continue
            V=jones_of_pd([tuple(x+1 for x in c) for c in L.PD_code()])
            if V==VK or V==mirror(VK):
                score[c]+=1; ok.append(c)
        tested+=1
        print(hw[:60]+('...' if len(hw)>60 else ''),'| a=%d N=%d slopes=%s'%(a,N,[str(s) for s in slopes]),
              '| cross=%d'%len(pdK),'| J(word)==J(formula):',Jw==Jf,'| matching conventions:',len(ok))
    print('tested',tested)
    for c,v in sorted(score.items(),key=lambda x:-x[1])[:4]: print('convention',c,'matches',v)
