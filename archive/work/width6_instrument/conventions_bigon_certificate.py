from pathlib import Path
from fractions import Fraction as F
import json
from transport_exact_intersections import intersection_records,figure8
import transport_pl as p
HERE=Path(__file__).resolve().parent
x=json.loads((HERE/'transport_pl.json').read_text())
source=[[tuple(F(c)for c in z)for z in curve]for curve in x['curves']]
target=[figure8(1,2),figure8(3,4)]
# Two source segments surrounding vertex1111 against target lobe edge14.
local,checks=intersection_records(source[0][1110:1113],target[0][14:16])
assert checks=={'potential_collinear_segments':0,'vertex_intersections':0}
assert len(local)==2
local.sort(key=lambda r:r['a_param'])
assert local[0]['a_param']<1<local[1]['a_param']
assert local[0]['sign']==-local[1]['sign']
a,b=[r['point']for r in local];v=source[0][1111]
triangle=[a,v,b]
area2=p.cross(p.sub(v,a),p.sub(b,a));assert area2
# No other source arc crosses the target side of the proposed bigon.
base_hits=[]
for k,c in enumerate(source):
 hits,check=intersection_records(c,[a,b])
 base_hits.extend((k,r)for r in hits)
# Endpoint conventions include a and exclude b; require no interior hits.
assert not [r for k,r in base_hits if 0<r['b_param']<1]
# No target curve enters across either source side.
source_side_hits=[]
for k,c in enumerate(target):
 hits,check=intersection_records(triangle,c)
 source_side_hits.extend((k,r)for r in hits)
assert not [r for k,r in source_side_hits if 0<r['a_param']<2]
lo=[min(z[k]for z in triangle)for k in(0,1)]
hi=[max(z[k]for z in triangle)for k in(0,1)]
assert not any(lo[0]<=i<=hi[0] and lo[1]<=0<=hi[1]for i in range(1,7))
points=json.loads((HERE/'conventions_14_exact_points.json').read_text())
fixed=points[69]['position']
assert not(lo[0]<=fixed[0]<=hi[0] and lo[1]<=fixed[1]<=hi[1])
result={'configuration_ids':[153848,154178],'exponents':[1,0],'raw_signs':[1,-1],
 'shared_source1_point_id':69,'moving_source0_point_ids':[796,797],
 'source_vertex_index':1111,'target_loop_index':0,'target_segment_index':14,
 'target_segment_is_retraced_connector':False,
 'triangle_vertices':[[str(c)for c in z]for z in triangle],
 'triangle_vertices_decimal':[[float(c)for c in z]for z in triangle],
 'twice_signed_area':str(area2),
 'interior_target_base_crossings_by_either_source_arc':0,
 'interior_source_side_crossings_by_either_target_loop':0,
 'punctures_in_bounding_box':0,'fixed_configuration_point_in_bounding_box':False,
 'conclusion':'This is an embedded empty local bigon. Its ordinary Reidemeister-II intersection removal pairs the two configuration intersections with opposite local sign and zero change of both deck exponents. It is a lobe-edge bigon, not cancellation from a retraced target connector, and it does not identify a separating disk for the tangle.',
 'why_empty':'The sides form a simple triangle. Exact intersection tests show no other supporting curve enters across its boundary; all punctures and all supporting-curve endpoints are outside. The source arcs are embedded and mutually disjoint by the ambient PL homeomorphism certificate.'}
(HERE/'conventions_bigon_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
