"""a_2 census for the Theorem V3 class (vertical closures V_a of Y^N u_1...u_n, u_i NON-INTEGRAL rational boxes), Theorem V level.
Box word w (letters X,x,Y,y; last letter acts first on e_1) lifts to the rational tangle of slope s(w) (nest Lemma L, horizontal
axis): start s=0; Y: s+1, y: s-1, X: s/(1+2s), x: s/(1-2s).  Non-integral <=> denominator of s(w) has |q| >= 3 (q odd)."""
import sys, itertools
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, lp
def slope(w):
    s=Fr(0)
    for ch in reversed(w):
        if ch=='Y': s+=1
        elif ch=='y': s-=1
        elif ch=='X': s=s/(1+2*s)
        elif ch=='x': s=s/(1-2*s)
    return s
def words(maxlen):
    out={}
    for L in range(2,maxlen+1):
        for w in itertools.product('XxYy',repeat=L):
            w=''.join(w)
            if w[0] not in 'Xx' or w[-1] not in 'Yy': continue
            s=slope(w)
            if s.denominator<3: continue
            # dedupe by slope mod 1 (integral parts go into N)
            key=s-(s.numerator//s.denominator)
            out.setdefault(key,w)
    return out
if __name__=='__main__':
    W=words(int(sys.argv[1]) if len(sys.argv)>1 else 5)
    print('distinct non-integral box slopes mod 1:',len(W))
    vecs={w:vc.rat(w) for w in W.values()}
    tot=0; zero=[]
    for n in (2,3):
        for combo in itertools.combinations_with_replacement(sorted(vecs),n):
            p=vc.starall([vecs[w] for w in combo])
            for N in range(-3,4):
                q=vc.Ypow(N,p)
                for a in (3,-3,5,-5,7,-7):
                    J=vc.J_vert(a,q)
                    if J is None: continue
                    tot+=1
                    if lp.a2(J)==0: zero.append((lp.span(J),a,N,combo,[str(slope(w)) for w in combo]))
    print('closures',tot,'a2=0:',len(zero))
    zero.sort()
    for z in zero[:20]: print(z)
