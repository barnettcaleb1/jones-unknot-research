import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
from family import *
def rel_hull(hw, timeout=250):
    rec = run(hw, timeout)
    if 'error' in rec: return None
    Npts = N_points(rec)
    cc = cube_coords(hw, Npts)
    if cc is None: return None
    pts, n = cc
    half = parse_word(hw)
    c = sum(1 for (l, i) in half if l in 'xy'); wr, _ = half_writhe(half)
    U = (2 * c - 2 * wr, 2 * c - 4 * wr)
    rel = sorted((h - U[0], q - U[1]) for h, q in pts)
    return rel, hull(rel), U, n
if __name__ == '__main__':
    fams = {
     'A: l1.y0.y0.y1^b.u2': ['l1.y0.y0.' + '.'.join(['y1'] * b) + '.u2' for b in range(1, 6)],
     'B: l1.y0^(2a).y1.u2': ['l1.' + '.'.join(['y0'] * (2 * a)) + '.y1.u2' for a in range(1, 5)],
     'C: l1.y0.y0.x1^b.u2': ['l1.y0.y0.' + '.'.join(['x1'] * b) + '.u2' for b in range(1, 5)],
     'D: l1.x0^(2a).y1.u2': ['l1.' + '.'.join(['x0'] * (2 * a)) + '.y1.u2' for a in range(1, 4)],
     'E: l1.y0.y0.y1.y1.y0^(2a).y1.u2 ': ['l1.y0.y0.y1.y1.' + '.'.join(['y0'] * (2 * a)) + '.y1.u2' for a in range(1, 3)],
    }
    which = sys.argv[1:] or list(fams)
    for name in fams:
        if not any(name.startswith(w) for w in which): continue
        print('FAMILY', name)
        for hw in fams[name]:
            r = rel_hull(hw)
            if r is None:
                print('   %-34s failed' % hw); continue
            rel, hv, U, n = r
            qs = [q for h, q in rel]
            top = [p for p in rel if p[1] == max(qs)]; bot = [p for p in rel if p[1] == min(qs)]
            print('   %-34s dim %2d  bottom %s top %s  hull %s' % (hw, len(rel), bot, top, hv))
