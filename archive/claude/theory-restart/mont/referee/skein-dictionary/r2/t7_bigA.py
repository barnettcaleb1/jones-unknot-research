"""Raw-marking check of (8.4) at larger |a| (odd and even) for a few bodies of each kind."""
import json
from t2_bodies import check_body
L=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/general_boxes.json'))
gen=[B for B,_ in L]
bodies=['', 'y0', 'r1.y0.y2.u1', gen[0], gen[5], gen[17], 'r2.y1.'+gen[3]+'.u1', 'r2.x1.x1.y0.'+gen[8]+'.u1']
for B in bodies:
    res,da,db=check_body(B, arange=[-6,-5,5,6])
    print(repr(B), all(res.values()), {k:v for k,v in res.items() if not v})
