"""One fixed certificate; no search and no homology computation.

The eight origins are extracted from the freshly replayed F2 minimal BN
chain of halfword s.r1.x2.y1.y0.r2.y0.y1.y0.y1.x2.u3.u1.
This checks its augmentation, Euler polynomial, and mirror-sum endpoints.
"""
from collections import Counter
import json
from pathlib import Path

ORIGINS = [(-1,-2), (-5,-8), (-3,-4), (-2,-2),
           (-7,-10), (-6,-8), (-9,-12), (-13,-18)]
SQUARE = [(0,0), (1,2), (5,8), (6,10)]

def euler(profile):
    out = Counter()
    for (h,q), count in profile.items():
        assert q % 2 == 0
        out[q//2] += (-1 if h % 2 else 1)*count
    return {k:v for k,v in sorted(out.items()) if v}

def ends(profile):
    lo,hi = min(q for h,q in profile), max(q for h,q in profile)
    out = []
    for q in [lo,hi]:
        row = sorted((h,n) for (h,p),n in profile.items() if p == q)
        out.append(dict(q=q, homological_multiplicities=row,
                        euler=sum((-1 if h%2 else 1)*n for h,n in row)))
    return out

N = Counter({(0,0):1})
for h,q in ORIGINS:
    for dh,dq in SQUARE:
        N[h+dh,q+dq] += 1
assert sum(N.values()) == 33
J = euler(N)
assert J == {-9:-1,-8:1,-6:-1,-5:1,-1:1,2:1,3:-1}
assert ends(N) == [
    dict(q=-18,homological_multiplicities=[(-13,1)],euler=-1),
    dict(q=8,homological_multiplicities=[(4,1),(5,1)],euler=0)]

mirror = Counter({(-h,-q):n for (h,q),n in N.items()})
product = Counter()
for (h,q),n in N.items():
    for (hh,qq),m in mirror.items():
        product[h+hh,q+qq] += n*m
assert sum(product.values()) == 1089
assert ends(product) == [
    dict(q=-26,homological_multiplicities=[(-18,1),(-17,1)],euler=0),
    dict(q=26,homological_multiplicities=[(17,1),(18,1)],euler=0)]
JP = euler(product)
assert (min(JP),max(JP)) == (-12,12)

result = dict(halfword="s.r1.x2.y1.y0.r2.y0.y1.y0.y1.x2.u3.u1",
              rank=33, origins=ORIGINS, endpoints=ends(N), J=J,
              mirror_sum_rank=1089, mirror_sum_endpoints=ends(product),
              mirror_sum_J_support=[min(JP),max(JP)])
target = Path(__file__).with_suffix('.json')
target.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
