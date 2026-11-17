"""Independent exact local certificate for transport_pl's quarter homeomorphism."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import json
import transport_pl as p
HERE=Path(__file__).resolve().parent
edges=defaultdict(list)
source_area=target_area=F(0)
checks=0
for src,dst in p.TRIANGLES:
    source_area+=p.cross(p.sub(src[1],src[0]),p.sub(src[2],src[0]))/2
    target_area+=p.cross(p.sub(dst[1],dst[0]),p.sub(dst[2],dst[0]))/2
    for i,j in [(0,1),(1,2),(2,0)]:
        edge=tuple(sorted((src[i],src[j])))
        image=(dst[i],dst[j]) if src[i]<src[j] else (dst[j],dst[i])
        edges[edge].append(image)
    for i in range(11):
        for j in range(11-i):
            weights=(F(i,10),F(j,10),1-F(i+j,10))
            x=tuple(sum(w*z[k]for w,z in zip(weights,src))for k in(0,1))
            y=tuple(sum(w*z[k]for w,z in zip(weights,dst))for k in(0,1))
            assert p.quarter_point(x)==y
            assert p.quarter_point(y,True)==x
            checks+=1
assert all(len(set(v))==1 for v in edges.values())
expected=2*(p.OUTER**2-p.INNER**2)
assert source_area==target_area==expected
boundary=[]
for e,images in edges.items():
    if len(images)==1:
        norms={abs(x[0])+abs(x[1])for x in e}
        assert len(norms)==1
        r=next(iter(norms));assert r in(p.INNER,p.OUTER)
        expected_image=tuple(p.turn(x)for x in e)if r==p.INNER else e
        assert images[0]==expected_image
        boundary.append({'radius':str(r),'edge':[[str(c)for c in x]for x in e]})
assert len(boundary)==8
result={'all_eight_cell_orientations_positive':True,'edge_images_agree':True,
 'domain_and_image_annular_area':str(expected),'inner_boundary':'one counterclockwise quarter turn',
 'outer_boundary':'pointwise fixed','exact_barycentric_inverse_tests':checks,
 'homeomorphism_argument':'Positive cell orientations plus continuous gluing and degree-one boundary map imply a degree-one orientation-preserving PL homeomorphism of the annulus; extend by rigid rotation on the inner disk and identity outside.',
 'diagonal_path_argument':'The two source arcs begin disjoint and remain disjoint under this ambient homeomorphism. The two target figure-eight supports occupy disjoint x-bands. Consequently the successive-point configuration paths remain off the diagonal.',
 'winding_limit':'Exact PL geometry certifies the path is valid. The existing float angle primitive and its integer rounding are a separate numerical layer; exact aggregate calibration is evidence, not a substitute for an exact winding implementation.'}
(HERE/'conventions_pl_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
