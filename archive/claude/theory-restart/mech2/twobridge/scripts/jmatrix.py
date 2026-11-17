#!/usr/bin/env python3
"""J-level matrix formula for two-bridge quotient tangles (Theorem A) and exhaustive check of non-flatness (Theorem B).
   rho(Y) = [[1,0],[t^-3,t^-3]], rho(X) = [[1,1-t^4],[0,-t]], rho(y)=rho(Y)^-1 = [[1,0],[-1,t^3]], rho(x)=rho(X)^-1 = [[1,t^-1-t^3],[0,-t^-1]].
   J_w = (1 0) rho(L_m)...rho(L_1) (1 0)^T.   Laurent polynomials as dicts exponent->coeff."""
import sys,itertools,collections,math
def padd(p,q):
    r=collections.Counter(p)
    for e,c in q.items(): r[e]+=c
    return {e:c for e,c in r.items() if c}
def pmul(p,q):
    r=collections.Counter()
    for e1,c1 in p.items():
        for e2,c2 in q.items(): r[e1+e2]+=c1*c2
    return {e:c for e,c in r.items() if c}
ONE={0:1}; ZERO={}
RHO={'Y':((ONE,ZERO),({-3:1},{-3:1})),
     'X':((ONE,{0:1,4:-1}),(ZERO,{1:-1})),
     'y':((ONE,ZERO),({0:-1},{3:1})),
     'x':((ONE,{-1:1,3:-1}),(ZERO,{-1:-1}))}
def apply(M,v):
    return (padd(pmul(M[0][0],v[0]),pmul(M[0][1],v[1])),padd(pmul(M[1][0],v[0]),pmul(M[1][1],v[1])))
def Jw(blocks):
    """blocks = [(a1,b1),(a2,b2),...] integers (sign = letter sign): word Y^a1 X^b1 Y^a2 X^b2 ..."""
    v=(ONE,ZERO)
    for a,b in blocks:
        for _ in range(abs(a)): v=apply(RHO['Y' if a>0 else 'y'],v)
        for _ in range(abs(b)): v=apply(RHO['X' if b>0 else 'x'],v)
    return v[0]
def cf_num(blocks):
    """numerator p of the continued fraction [a1, 2b1, a2, 2b2, ...] (determinant of the knot), via 2x2 integer matrices"""
    # p/q = a1 + 1/(2b1 + 1/(a2 + ...)) ; compute from the end
    seq=[]
    for a,b in blocks: seq+=[a,2*b]
    num,den=1,0   # value = infinity
    for c in reversed(seq):
        # new value = c + 1/value = (c*num + den)/num
        num,den=c*num+den,num
    return num,den
if __name__=='__main__':
    maxe=int(sys.argv[1]) if len(sys.argv)>1 else 3
    maxn=int(sys.argv[2]) if len(sys.argv)>2 else 3
    exps=[e for e in range(-maxe,maxe+1) if e!=0]
    bad=0; tot=0; spans=collections.Counter(); lead=collections.Counter()
    for n in range(1,maxn+1):
        for blocks in itertools.product(itertools.product(exps,repeat=2),repeat=n):
            p,q=cf_num(blocks)
            J=Jw(blocks)
            tot+=1
            mono=(len(J)==1)
            if mono!=(abs(p)==1):
                bad+=1
                if bad<10: print('VIOLATION',blocks,'p=',p,'J=',dict(sorted(J.items())))
            if not mono:
                lead[(J[max(J)],J[min(J)])]+=1
    print('words:',tot,' violations of [J monomial <=> |p|=1]:',bad)
    print('extreme coefficients (top,bottom) of non-monomial J:',dict(lead))
