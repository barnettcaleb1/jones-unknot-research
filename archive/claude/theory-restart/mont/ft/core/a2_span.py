# Span bounds. J = 1 mod D, J != 1. If span(J) < deg D then J = t^{-c} R_c with R_c = (t^c mod D) (canonical remainder of
# degree < deg D).  So min span over J != 1 is min(deg D, min_{c != 0} span(R_c)).  R_c is affine (D7) / quadratic (D8) in c on
# each residue class mod 12 (CRT: t^c mod Phi1 Phi4 Phi6 has period 12; t^c mod (t+1)^a is polynomial in c), so a finite window
# plus the asymptotic span (= degree of the c-leading term, here deg D - 1) decides.
import clib, lp
def rem(c,Dp):
    p=lp.mono(c) if c>=0 else None
    # compute t^c mod Dp for any integer c: use t^c = t^(c mod N) * (t^N)^... simpler: power by repeated multiplication with reduction
    deg=max(Dp)
    def red(p):
        q,r=clib.pdiv_poly(p,Dp)
        return r
    if c>=0:
        r=lp.ONE
        base=lp.mono(1)
        e=c
        while e:
            if e&1: r=red(lp.mul(r,base))
            base=red(lp.mul(base,base)); e>>=1
        return r
    else:
        # t^{-1} mod D: D = t^7 + t^4 - t^3 - 1 style with constant -1 -> t * (stuff) = 1 mod D
        inv=tinv(Dp)
        r=lp.ONE; base=inv; e=-c
        while e:
            if e&1: r=red(lp.mul(r,base))
            base=red(lp.mul(base,base)); e>>=1
        return r
def tinv(Dp):
    c0=Dp.get(0,0); assert abs(c0)==1
    # D = c0 + t*E  ->  t*E = -c0 mod D -> t^{-1} = -E/c0
    E={e-1:c for e,c in Dp.items() if e>0}
    return {e:-c*c0 for e,c in E.items()}
def sp(p): return (max(p)-min(p)) if p else None
import sys
res={}
for name,Dp in (('D7',clib.D(2,1)),('D8 (core)',clib.D(3,1)),('D8b=(t+1)^2(t-1)^2C (sigma=0)',clib.D(2,2)),('D9 (core & sigma=0)',clib.D(3,2))):
    best=[]
    W=600
    for c in range(-W,W+1):
        if c==0: continue
        R=rem(c,Dp)
        J=lp.shift(R,-c)
        if J=={0:1}: continue
        best.append((sp(R),c,R))
    best.sort(key=lambda x:(x[0],abs(x[1])))
    from collections import Counter
    print('   span histogram (|c|<=W, J!=1):',sorted(Counter(b[0] for b in best).items()))
    print(name,'deg',max(Dp),'  min span over |c|<=%d:'%W,best[0][0])
    for s,c,R in best[:6]:
        J=lp.shift(R,-c)
        print('   span',s,'c',c,'J=',sorted(J.items()))
    # asymptotics: span of R_c for the largest |c| in each residue class
    tail=sorted(set(sp(rem(c,Dp)) for c in list(range(W-24,W))+list(range(-W,-W+24))))
    print('   spans for |c| near %d:'%W,tail)
