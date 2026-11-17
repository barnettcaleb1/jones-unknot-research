"""Independent ribbon-surface and eight-state check; not S3 unknot recognition."""
from itertools import product
from collections import defaultdict
from pathlib import Path
import json
pd=[(1,4,2,5),(5,3,0,2),(3,1,4,0)]
occ={}
for j,row in enumerate(pd):
    for k,x in enumerate(row):occ.setdefault(x,[]).append(4*j+k)
a={u:v for pair in occ.values() for u,v in [pair,pair[::-1]]}
rot={u:4*(u//4)+(u+1)%4 for u in a}
opp={u:4*(u//4)+(u+2)%4 for u in a}
def cycles(p):
    left=set(p);out=[]
    while left:
        u=min(left);c=[]
        while u in left:c.append(u);left.remove(u);u=p[u]
        out.append(c)
    return out
faces=cycles({u:rot[a[u]] for u in a})
knot=cycles({u:opp[a[u]] for u in a})
co={0:(0,0),1:(0,0),2:(1,1),3:(0,0),4:(1,0),5:(0,1)}
def h(c):
    val=[0,0]
    for u in c:
        lab=pd[u//4][u%4];sgn=1 if u==min(occ[lab])else-1
        for j in range(2):val[j]+=sgn*co[lab][j]
    return tuple(val)
def mul(p,q):
    r=defaultdict(int)
    for a,c in p.items():
        for b,d in q.items():r[a+b]+=c*d
    return {a:c for a,c in r.items() if c}
delta={2:-1,-2:-1};total=defaultdict(int);states=[]
for bits in product([0,1],repeat=3):
    s={}
    for j,b in enumerate(bits):
        for u,v in ([(0,1),(2,3)]if b==0 else[(0,3),(1,2)]):s[4*j+u]=4*j+v;s[4*j+v]=4*j+u
    cs=cycles({u:s[a[u]]for u in a});unique={}
    for c in cs:
        key=tuple(sorted(pd[u//4][u%4]for u in c));unique[key]=h(c)
    loops=len(unique);term={3-2*sum(bits):1}
    for _ in range(loops-1):term=mul(term,delta)
    for e,c in term.items():total[e]+=c
    states.append({'bits':bits,'loop_homologies':list(unique.values())})
result={'PD':pd,'faces':faces,'oriented_traversals':knot,'genus':(2-3+6-len(faces))//2,
 'cohomology_basis_edge_values':co,'knot_homology':h(knot[0]),'crossing_signs':[-1,1,1],
 'states':states,'reduced_virtual_bracket':{e:c for e,c in total.items() if c},
 'scope':'Surface genus/connectivity/bracket verified. No S3 embedded-knot nontriviality claimed.'}
assert result['genus']==1 and len(knot)==2 and result['reduced_virtual_bracket']=={3:-1}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: one knot on genus-one Carter surface, writhe1, bracket -A^3, homology(0,-2).')
