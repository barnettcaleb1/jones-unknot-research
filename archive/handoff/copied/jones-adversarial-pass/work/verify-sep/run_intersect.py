import sys, json
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from intersect import *
R = Ribbon(5, 0)
c = cyc_reduce([1, 2, 3])
res = json.load(open(__file__.rsplit('/', 1)[0] + '/run_sep_out.json'))['overlaps']
rows = []
for r in res:
    w = r['word']
    cw = curve(w)
    i_S06 = count_crossings(c, cw, R)
    # D_6 count (puncture 6 kept, boundary = 7th): use F_6 ribbon
    R6 = Ribbon(6, 0)
    cw6 = cyc_reduce(act(w, [1, 2, 3]))
    i_D6 = count_crossings(c, cw6, R6)
    sp = r['H_spanwidth']
    rows.append((r['label'], i_S06, i_D6, sp, sp - 2 * i_S06))
    print(f"{r['label']:28s} i_S06={i_S06:3d}  i_D6={i_D6:3d}  span(H)={sp:3d}  span-2i={sp-2*i_S06:3d}   gamma(A=i)={r['gamma_at_A_eq_i']}")
json.dump(rows, open(__file__.rsplit('/', 1)[0] + '/intersect_out.json', 'w'), indent=1)
