"""Check Sigma_2(L_n) = S^3_{1/n}(K) numerically: 2-fold cyclic cover of the complement of L_n, every small filling slope with
H_1 = 0, compare SnapPea volumes with S^3_{+-1/n}(K)."""
import sys, regina
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import bk, identK, examples
name=sys.argv[1]; ns=[int(x) for x in sys.argv[2:]]
a,N,boxes=examples.EX[name]
hw=identK.halfword(a,N,boxes); f=bk.frame(hw)
S=bk.snap(bk.pd_code(bk.full_K(hw)))
for n in ns:
    target={s:bk.filled(S,1,s*n)[0] for s in (1,-1)}
    pd=bk.pd_code(bk.full_Ln(hw,n,f))
    T=bk.snap(pd); covers=[]
    T.enumerateCovers(2, regina.SnapPeaTriangulation.CoverEnumeration.Cyclic, lambda C,ct: covers.append(regina.SnapPeaTriangulation(C)))
    C=covers[0]; found=[]
    for p in range(-3,4):
        for q in range(0,4):
            if (p,q)==(0,0) or (q==0 and p<=0): continue
            from math import gcd
            if gcd(abs(p),q)!=1: continue
            C.fill(p,q,0)
            try:
                h=str(C.homologyFilled()); v=C.volume(); st=str(C.solutionType())
            except Exception as e:
                continue
            if h=='0': found.append(((p,q),round(v,8),st))
            C.unfill(0)
    print(name,'n=%d'%n,'vol S^3_{1/n}(K)=%.8f, S^3_{-1/n}(K)=%.8f'%(target[1],target[-1]),'| H1=0 fillings of the 2-fold cyclic cover of L_n:',found,flush=True)
