"""Exact flat-torus realization and two-braid certificate, no external packages."""
from fractions import Fraction as Q
from pathlib import Path
import json

H=Path(__file__).resolve().parent
j=json.loads((H/'virtual_surface_states.json').read_text())[0]
pd=j['PD']
pos=[tuple(map(Q,v)) for v in [
    ('0','0'),('-1/2','-19/30'),('-1/2','-11/30'),
    ('-5/8','-1/2'),('-1/4','-13/60'),('1/4','13/60'),
    ('-3/8','-1/2'),('1/4','-13/60'),('-1/4','13/60'),
    ('-1/2','0'),('0','-1/2'),('-1/2','-1/2')]]
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,t):return tuple(x*t for x in a)
def det(a,b):return a[0]*b[1]-a[1]*b[0]
occ={e:[] for e in range(6)}
for i,row in enumerate(pd):
    for p,e in enumerate(row):occ[e].append(4*i+p)
al={a:b for ds in occ.values() for a,b in (ds,ds[::-1])}
edge=lambda d:pd[d//4][d%4]
sgn=lambda d:1 if d<al[d] else -1
co=[{int(k):v for k,v in c.items()} for c in j['cohomology_basis']]
vol={e:tuple(Q(c[e]) for c in co) for e in occ}
areas=[]
for f,face in enumerate(j['faces']):
    g=(Q(0),Q(0)); center=pos[9+f]
    for d in face:
        e=edge(d);a=add(pos[d//4],g)
        mid=add(pos[3+e],g if sgn(d)>0 else sub(g,vol[e]))
        g2=add(g,mul(vol[e],sgn(d)));b=add(pos[al[d]//4],g2)
        areas.extend([det(sub(a,center),sub(mid,center))/2,
                      det(sub(mid,center),sub(b,center))/2])
        g=g2
    assert g==(0,0)
assert len(areas)==24 and all(a<0 for a in areas) and sum(areas)==-1
# With the exact integral cohomology basis, this is a degree-minus-one
# nonfolding triangulated map of tori; hence it is a homeomorphism.
triples=[];g=(Q(0),Q(0));d=0
while True:
    e=edge(d);a=add(pos[d//4],g)
    mid=add(pos[3+e],g if sgn(d)>0 else sub(g,vol[e]))
    g2=add(g,mul(vol[e],sgn(d)));b=add(pos[al[d]//4],g2)
    assert a[1]>mid[1]>b[1]
    triples.append([str(a[1]),str(mid[1]),str(b[1])])
    D=al[d];d=4*(D//4)+(D%4+2)%4;g=g2
    if d==0:break
assert len(triples)==6 and g==(0,-2)
result={'flat_torus_vertices':[[str(x) for x in v] for v in pos],
        'triangle_areas':[str(a) for a in areas],
        'total_signed_area':str(sum(areas)),
        'strictly_decreasing_longitude_triples':triples,
        'knot_homology':[int(x) for x in g],
        'conclusion':'Whenever the first basis curve is meridional in one complementary solid torus, the knot is a closed two-strand braid.'}
(H/'verify_flat_braid.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['flat_torus_vertices','triangle_areas']},indent=2))
