import sys, itertools
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
from famrel import rel_hull
from bcube import *
def analyse(hw, timeout=150):
    try:
        r = rel_hull(hw, timeout)
    except Exception as ex:
        return None
    if r is None: return None
    rel, hv, U, n = r
    qs = [q for h, q in rel]
    top = sorted(p for p in rel if p[1] == max(qs)); bot = sorted(p for p in rel if p[1] == min(qs))
    return dict(dim=len(rel), top=top, bot=bot, hull=hv)
if __name__ == '__main__':
    hk1, tw1, hk2, tw2 = sys.argv[1:5]
    out = open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/grid3.log', 'a')
    for a1, b1, a2, b2 in itertools.product((1, 2), (1, 2, 3), (1, 2), (1, 2, 3)):
        hw = 'r1.' + '.'.join([hk1] * a1 + [tw1] * b1 + [hk2] * a2 + [tw2] * b2) + '.u1'
        r = analyse(hw)
        if r is None:
            line = '%s FAILED' % hw
        else:
            flag = ''
            if len(set(r['top'])) > 1 or len(set(r['bot'])) > 1: flag = '  <-- NP FAILS'
            elif len(r['top']) > 1 or len(r['bot']) > 1: flag = '  (extreme degree of dimension > 1, one h)'
            line = '%s dim %d top %s bottom %s%s' % (hw, r['dim'], r['top'], r['bot'], flag)
        out.write(line + '\n'); out.flush()
        print(line); sys.stdout.flush()
