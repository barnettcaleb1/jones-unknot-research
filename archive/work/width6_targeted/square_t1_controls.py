"""Four fixed torus-form t=1 controls; not a geometric noodle dictionary."""
from pathlib import Path
from collections import defaultdict
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'width6_lift'))
sys.path.insert(0, str(HERE.parent / 'width6'))
import lift_pairing as lp
import probe


def add(p, r, scale=1):
    out = defaultdict(int, p)
    for a, c in r.items():
        out[a] += scale*c
    return {a:c for a,c in out.items() if c}


def mul(p, r):
    out = defaultdict(int)
    for a,c in p.items():
        for b,d in r.items():
            out[a+b] += c*d
    return {a:c for a,c in out.items() if c}


def one_cup(i,j):
    if i == j:
        return {1:-1, -1:-1}
    if abs(i-j) == 1:
        return {0:1}
    return {}


rows = []
for i,j in [(7,7),(6,7),(3,7),(5,7)]:
    caps_i = probe.caps(probe.STATES[i])
    caps_j = probe.caps(probe.STATES[j])
    assert all(b == a+1 for a,b in caps_i+caps_j)
    m = [[one_cup(a,c) for c,d in caps_j] for a,b in caps_i]
    det = add(mul(m[0][0],m[1][1]),mul(m[0][1],m[1][0]),-1)
    p = lp.pairing([],i,j)
    t1 = defaultdict(int)
    derivative = defaultdict(int)
    for (a,b),c in p.items():
        t1[a] += c
        derivative[a] -= b*c
    assert not any(t1.values())
    quotient_at_t1 = {a:c for a,c in derivative.items() if c}
    assert quotient_at_t1 == {a+2:c for a,c in det.items()}
    rows.append({'states':[i,j], 'caps': [caps_i,caps_j],
                 'one_cup_M':m, 'det_M_s_coefficients':det,
                 'P_over_1_minus_t_at_t1':quotient_at_t1})

out = {'variables':'q=s^2',
       'identity':'P/(1-t)|t=1=q det M; H(q,1)=(q-1)^2/q det M',
       'scope':'four fixed adjacent-cap controls only', 'rows':rows}
(HERE/'square_t1_controls.json').write_text(json.dumps(out,indent=2)+'\n')
print('Four t=1 determinant controls passed exactly.')
