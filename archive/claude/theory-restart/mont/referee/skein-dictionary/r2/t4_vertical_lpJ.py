"""Theorem V vs lp.J on vertical closures s.l1.B.(x2)^a.u1 (odd a: knot closures).
Body amplitudes (A,B) computed INDEPENDENTLY by the raw TL3 sandwich + preferred normalisation; also
compared against the project's general_boxes.json pinned vectors."""
import json, random, sys
from tlib import *
L=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/general_boxes.json'))
gen=[(B,[dict((e,c) for e,c in v[0]),dict((e,c) for e,c in v[1])]) for B,v in L]
rat=['y0','x0','y0.y0','x0.x0','y0.y0.y0','x0.x0.x0','r1.y0.y2.u1','r1.x0.x2.u1','r1.y0.y2.y0.u1','l1.x0.x0.y2.u1',
     'r1.r1.y0.y2.y4.u1.u1','y0.r1.x0.x2.u1.y0','r1.x0.y2.y2.u1','l1.y0.y2.y2.y2.u1']
rnd=random.Random(int(sys.argv[1]) if len(sys.argv)>1 else 3)
nested=[]
for _ in range(16):
    k=rnd.choice([1,2,2,3]); Bs=[rnd.choice([g[0] for g in gen]+rat) for _ in range(k)]; m=rnd.choice([-2,-1,1,2])
    nested.append(neck_body(m,Bs))
for _ in range(6):
    inner=neck_body(rnd.choice([-1,1,2]), [rnd.choice([g[0] for g in gen])])
    nested.append(neck_body(rnd.choice([-1,1]), [inner, rnd.choice(rat)]))
stats={'vec_match_json':0,'vec_json_total':0,'closures':0,'ok':0,'none':0}
mism=[]
for kind,lst in (('gen',[g[0] for g in gen]),('rat',rat),('nested',nested)):
    for B in lst:
        pr=body_pref(B)
        if pr is None: print('no pref',B); continue
        A0,B0=pr
        # compare with json pinned vector
        if kind=='gen':
            v=dict(gen)[B]; a_j,b_j=ab_from_v(v); stats['vec_json_total']+=1
            if a_j==A0 and b_j==B0: stats['vec_match_json']+=1
            else: print('JSON VECTOR MISMATCH',B)
        # J(s.B) == A0
        assert lp.J('s.'+B)==A0, ('closure a mismatch',B)
        for a in rnd.sample([-7,-5,-3,-1,1,3,5,7],3):
            w=vword(B,a); Jw=lp.J(w)
            if Jw is None: stats['none']+=1; continue
            F=vert_formula(A0,B0,a)
            stats['closures']+=1
            if F is not None and normalize(F)==Jw: stats['ok']+=1
            else: mism.append((w,a)); print('MISMATCH',kind,w)
print(stats); print('mismatches',mism)
