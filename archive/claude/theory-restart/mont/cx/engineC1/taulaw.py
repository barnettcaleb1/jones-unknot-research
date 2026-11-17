"""PROOF (finite product automaton) of the third-order end law for rational boxes:
   tau(u) := l2_top(q(u)) + l2_bot(q(u)) = -1 for every non-integral rational box u (normal form, k >= 1),
together with Lemma S (sigma = l1_top + l1_bot = 0, delta = -1) re-derived the same way.
Bottom data of u = top data of the mirror u'' = u(-m_0-1, -m_1, ..., -m_{k-1}) (notie R2, PROVED).
Product automaton on (state(u), state(u'')); exponents clipped independently in each factor (sound by jauto's clipping lemma)."""
import sys
sys.path.insert(0,'.')
import jauto
from fractions import Fraction as Fr
K=3; M=K+3
order,trans=jauto.build(K)
clip=lambda m: max(-M,min(M,m))
start=('init','init')
seen={start}; todo=[start]; inv=set()
qd={k:jauto.qlog(k,K) for k in order if k!='init'}
while todo:
    s,s2=todo.pop()
    first=(s=='init')
    for m in range(-M-3,M+4):
        if m==0: continue
        if first:
            if m==-1: continue
            mm=-m-1
        else: mm=-m
        a=trans.get((s,clip(m))); b=trans.get((s2,clip(mm)))
        assert a is not None and b is not None, (s,s2,m,mm)
        ns=(a[1],b[1])
        if ns not in seen: seen.add(ns); todo.append(ns)
vals=set()
for (s,s2) in seen:
    if s=='init': continue
    dq,lc,l=qd[s]; dq2,lc2,l2=qd[s2]
    vals.add((dq-(3-dq2), lc*lc2, l[0]+l2[0], l[1]+l2[1]))
print('reachable product states (excl. init):',len(seen)-1)
print('(delta = d_top - d_bot, lc_top*lc_bot, sigma, tau) values over all rational boxes:',sorted(vals))
