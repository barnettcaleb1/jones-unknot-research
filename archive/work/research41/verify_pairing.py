"""Exact EKT pairing identities and an exhaustive 8-endpoint connectivity check."""
from collections import Counter
import json
from pathlib import Path

def add(*ps):
    q={}
    for p in ps:
        for k,v in p.items(): q[k]=q.get(k,0)+v
    return {k:v for k,v in q.items() if v}
def mul(p,q):
    r={}
    for i,a in p.items():
        for j,b in q.items():r[i+j]=r.get(i+j,0)+a*b
    return {k:v for k,v in r.items() if v}
def neg(p):return {k:-v for k,v in p.items()}

d={2:-1,-2:-1}
a={-1:-1,3:1,7:-1}; b={-3:1}
c={-11:-1,-7:2,-3:-2,1:2,5:-1}
e={-13:1,-9:-1,-5:1}
h00={-14:-1,-6:-1,-2:-2,2:-2,6:-1,14:-1}
one={0:1}
def invariant(u,v,w):return not add(mul(b,u),mul(add(e,neg(a)),v),neg(mul(c,w)))
assert invariant(d,one,d)
assert invariant(h00,mul(d,d),d)
assert add(mul(h00,d),neg(mul(d,d))) # H and Q independent: use entries 00,11.

def matching(xs):
    if not xs:yield [];return
    for j in range(1,len(xs)):
        for rest in matching(xs[1:j]+xs[j+1:]):yield [(xs[0],xs[j])]+rest
def count_components(edges):
    p=list(range(8))
    def root(i):
        while p[i]!=i:i=p[i]
        return i
    for i,j in edges:p[root(i)]=root(j)
    return len({root(i) for i in range(8)})
B=[[(0,1),(2,3)],[(0,3),(1,2)]]
D=[[(4,5),(6,7)],[(4,7),(5,6)]]
counts=Counter()
total=0
for outside in matching(list(range(8))):
    total+=1
    mu=tuple(count_components(outside+B[i]+D[j]) for i,j in [(0,0),(0,1),(1,0),(1,1)])
    if mu[0]==mu[1]+1 and mu[1]==mu[2]:counts[mu]+=1
assert total==105
assert counts==Counter({(4,3,3,2):1,(3,2,2,1):8,(2,1,1,2):4,(2,1,1,1):4})
data={'omega_preserves_H':True,'omega_preserves_Q':True,'outside_matchings':total,
      'necessary_component_tables':{','.join(map(str,k)):v for k,v in sorted(counts.items())},
      'scope':'Connectivity is necessary only; it does not prove any outside tangle is invariant.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data))
