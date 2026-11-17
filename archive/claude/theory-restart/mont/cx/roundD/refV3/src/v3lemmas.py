"""ENGINE C1: rigorous verification (finite automaton, jauto.py) of the box lemmas used in the proof of Theorem V3.
phi(R)=1, phi(S_j)=phi(tiny)=phi(init)=0.  Psi = rho_a + phi.  All walks start at init (first exponent m_0 != -1)."""
import sys
sys.path.insert(0,'.')
import jauto
from fractions import Fraction as Fr
K=3; M=K+3
order,trans=jauto.build(K)
def cls(k):
    if k in ('init',): return 'init'
    if k=='tiny': return 'S3+'
    d,j=k
    if d==-1: return 'R1' if j[1]==1 else 'R0'
    return 'S%d'%(-4-d)
phi=lambda k: 1 if cls(k).startswith('R') else 0
edges=[]
for (k,m),(Dj,nk) in trans.items():
    d,lc,s=jauto.norm_jet(Dj); l=jauto.logs(s)
    edges.append((k,m,nk,l))
# P1 Psi monotone
bad=[(k,m,nk,l[0]) for (k,m,nk,l) in edges if l[0]+phi(nk)-phi(k)>0]
print('P1 Psi non-increasing on all %d edges:'%len(edges), not bad, bad[:3])
# longest paths (Bellman-Ford) of a functional f(edge) from init; returns dict state->max (None if unreachable); detects + cycles
def longest(f, allowed=lambda e: True):
    best={k:None for k in order}; best['init']=Fr(0)
    for it in range(len(order)+2):
        ch=False
        for e in edges:
            if not allowed(e): continue
            k,m,nk,l=e
            if best[k] is None: continue
            v=best[k]+f(e)
            if best[nk] is None or v>best[nk]: best[nk]=v; ch=True
        if not ch: return best
    raise RuntimeError('positive cycle')
rmax=longest(lambda e: e[3][0])
byc={}
for k in order:
    if k=='init': continue
    c=cls(k); byc.setdefault(c,[]).append(rmax[k])
print('P2 max rho_a by final class:',{c:max(v) for c,v in byc.items()})
lq={}
for k in order:
    if k=='init': continue
    dq,lc,l=jauto.qlog(k,K); lq.setdefault(cls(k),set()).add((dq,lc,l[0],l[1]))
print('P3 q data (dq, lc, rho_q, lambda_q) by class:',{c:sorted(v) for c,v in lq.items()})
# per-box bound for case (B): lambda_q + rho_a
bnd={}
for k in order:
    if k=='init': continue
    dq,lc,l=jauto.qlog(k,K)
    v=l[1]+rmax[k]; c=cls(k); bnd[c]=max(bnd.get(c,v),v)
print('P6 max (lambda_q + rho_a) by class:',bnd)
# Psi-preserving walks: maximize l2(a)
pres=lambda e: e[3][0]+phi(e[2])-phi(e[0])==0
l2max=longest(lambda e: e[3][1], pres)
for c in ('R1','R0','S0','S1','S2','S3+'):
    vals=[(l2max[k], jauto.qlog(k,K)[2][1]) for k in order if k!='init' and cls(k)==c and l2max[k] is not None]
    if vals:
        print('P4/P5 Psi-preserving walks ending in %s: max l2(a) = %s, max l2(b) = %s'%(c,max(v[0] for v in vals),max(v[0]+v[1] for v in vals)))
    else: print('P4/P5 no Psi-preserving walk ends in',c)
