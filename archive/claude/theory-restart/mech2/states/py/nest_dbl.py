import sys, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
from famrel import rel_hull
from nest_test import blocks
out = open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/nest_dbl.log', 'a')
prev = None
for b in (1, 3, 5, 7):
    hw = 'l2.' + '.'.join(['y1'] * b) + '.u2'
    try:
        r = rel_hull(hw, 280)
    except Exception as ex:
        r = None
    if r is None:
        line = '%s failed' % hw; cur = None
    else:
        cur = collections.Counter(r[0])
        qs = [q for h, q in r[0]]
        top = sorted(p for p in r[0] if p[1] == max(qs)); bot = sorted(p for p in r[0] if p[1] == min(qs))
        line = '%s dim %d top %s bottom %s' % (hw, sum(cur.values()), top, bot)
        if prev is not None:
            lost = prev - cur; new = cur - prev
            line += ' | nested in the next: %s lost %s new %s' % (not lost, sorted(lost.elements()), sorted(new.elements()))
        line += ' | N-U = %s' % sorted(cur.elements())
    out.write(line + '\n'); out.flush(); print(line)
    if cur is not None: prev = cur
