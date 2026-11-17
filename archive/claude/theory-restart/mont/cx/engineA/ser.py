"""Truncated Laurent series at t=infinity ('top') and t=0 ('bot') with exact Fraction coefficients.
A series datum is (d, lc, s) with f = lc * t^d * (1 + s[0] u + s[1] u^2 + ...), u = 1/t (top) or t (bot)."""
from fractions import Fraction as Fr
def pdata(f,end,K):
    if end=='top':
        D=max(f); c=f[D]; s=tuple(Fr(f.get(D-i,0),c) for i in range(1,K+1)); return (D,c,s)
    else:
        D=min(f); c=f[D]; s=tuple(Fr(f.get(D+i,0),c) for i in range(1,K+1)); return (D,c,s)
def smul(x,y):
    K=len(x); X=(1,)+x; Y=(1,)+y
    return tuple(sum(X[i]*Y[n-i] for i in range(n+1)) for n in range(1,K+1))
def sinv(x):
    K=len(x); X=(1,)+x; inv=[Fr(1)]
    for n in range(1,K+1):
        inv.append(-sum(X[i]*inv[n-i] for i in range(1,n+1)))
    return tuple(inv[1:])
def sdiv(x,y): return smul(x,sinv(y))
def ratio(fb,fa):   # series datum of fb/fa
    return (fb[0]-fa[0], Fr(fb[1],1)/fa[1], sdiv(fb[2],fa[2]))
def mulD(x,y): return (x[0]+y[0], x[1]*y[1], smul(x[2],y[2]))
def divD(x,y): return (x[0]-y[0], Fr(x[1],1)/y[1], sdiv(x[2],y[2]))
def slope(v,end,K):
    a,b=v
    return ratio(pdata(b,end,K),pdata(a,end,K))
