"""Independent a_2 check: Conway coefficient a_2 = Delta''(1)/2 from the Alexander polynomial of K (alex.py matrix, evaluated
exactly at integer points and interpolated), compared with -J''(-1)/24."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import bk
import alex, lp, identK, examples
from fractions import Fraction as Fr
def alex_values(word, ts):
    full=alex.symmetrize(alex.parse(word)); cr=alex.diagram(full)
    out=[]
    for t in ts:
        M,w=alex.alex_matrix(cr,t)
        m=[r[:-1] for r in M[:-1]]
        out.append(alex.bareiss(m))
    return out
def interp(xs,ys):
    # Lagrange -> coefficient list (exact)
    n=len(xs); coeffs=[Fr(0)]*n
    for i in range(n):
        num=[Fr(1)]; den=Fr(1)
        for j in range(n):
            if j==i: continue
            num=[ (num[k-1] if k>0 else 0) - xs[j]*(num[k] if k<len(num) else 0) for k in range(len(num)+1)]
            den*= (xs[i]-xs[j])
        for k in range(len(num)): coeffs[k]+=ys[i]*num[k]/den
    return coeffs
for name in sys.argv[1:]:
    a,N,boxes=examples.EX[name]; hw=identK.halfword(a,N,boxes)
    cr=alex.diagram(alex.symmetrize(alex.parse(hw))); n=len(cr)
    xs=list(range(2,2*n+6)); ys=alex_values(hw,xs)
    c=interp(xs,ys)
    while c and c[-1]==0: c.pop()
    lo=next(i for i,x in enumerate(c) if x!=0); c=c[lo:]
    if sum(c)<0: c=[-x for x in c]
    d=len(c)-1
    # symmetric Delta(t)=sum c_k t^(k-d/2); a2 = Delta''(1)/2 for the Conway-normalised form
    a2=sum(ck*Fr(k-Fr(d,2))*Fr(k-Fr(d,2)-1) for k,ck in enumerate(c))/2 + sum(ck*Fr(k-Fr(d,2)) for k,ck in enumerate(c))/2
    J=lp.J(hw)
    print(name,'Delta coeffs',[int(x) for x in c],'Delta(1)=',sum(c),'a2 from Delta =',a2,'| a2 from J =',lp.a2(J))
