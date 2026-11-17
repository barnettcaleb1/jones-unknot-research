"""Test of the conjectural rule for the specials of two-bridge quotient tangles.
State (G, Gam) in N[u,v], u = q^2 (same level), v = q^-6 * delta (next level).
  A-letter (axis crossing):  Gam <- v*Gam + 1 + (1+u*v)*G
  B-letter (off-axis crossing):  G <- u*G + Gam
Specials (normalised: c' = c - 24 j, d' = d - 4 j) = q^(2k-2) * delta * G(u,v),  k = -4 * G(u=1, v=-1).
Negative words: mirror (c',d') -> (-c', 1-d'), k -> -k.
"""
import sympy as sp
from collections import Counter
from parse import recs
from norm import strip, norm
u,v=sp.symbols('u v')
def G_of(word):
    G=sp.Integer(0); Gam=sp.Integer(0)
    for t,n in word:
        for _ in range(abs(n)):
            if t=='A': Gam=sp.expand(v*Gam+1+(1+u*v)*G)
            else: G=sp.expand(u*G+Gam)
    return G,Gam
def predicted(word):
    signs=set(n>0 for t,n in word)
    assert len(signs)==1
    pos=signs.pop()
    G,_=G_of(word)
    k=-4*int(G.subs({u:1,v:-1}))
    out=Counter()
    if G!=0:
        for (i,l),m in sp.Poly(G,u,v).terms():
            c=2*k-2+2*i-6*l; d=1+l
            if not pos: c,d=-c,1-d
            out[(c,d)]+=int(m)
    return (k if pos else -k), out
if __name__=='__main__':
    ok=bad=0
    for r in recs():
        if r['dup'] or not r['runs']: continue
        w=strip(r['runs'])
        if len(set(n>0 for t,n in w))>1: print('mixed signs',w); continue
        if not w:
            k,pred=0,Counter()
        else:
            k,pred=predicted(w)
        obs=Counter(norm(r))
        if k==r['k'] and pred==obs: ok+=1
        else:
            bad+=1; print('FAIL',w,'k pred',k,'obs',r['k']); print('  pred',sorted(pred.items())); print('  obs ',sorted(obs.items()))
    print('ok',ok,'bad',bad)
