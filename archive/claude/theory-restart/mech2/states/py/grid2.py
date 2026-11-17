import sys, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
from famrel import rel_hull
def analyse(hw):
    r = rel_hull(hw, 280)
    if r is None: return None
    rel, hv, U, n = r
    qs = [q for h, q in rel]
    top = sorted(set(p for p in rel if p[1] == max(qs))); bot = sorted(set(p for p in rel if p[1] == min(qs)))
    ntop = sum(1 for p in rel if p[1] == max(qs)); nbot = sum(1 for p in rel if p[1] == min(qs))
    return dict(dim=len(rel), top=top, bot=bot, ntop=ntop, nbot=nbot, hull=hv)
if __name__ == '__main__':
    hk, tw = sys.argv[1], sys.argv[2]
    amax, bmax = int(sys.argv[3]), int(sys.argv[4])
    for a in range(1, amax + 1):
        for b in range(1, bmax + 1):
            hw = 'l1.' + '.'.join([hk] * (2 * a)) + '.' + '.'.join([tw] * b) + '.u2'
            r = analyse(hw)
            if r is None:
                print('a=%d b=%d failed' % (a, b)); continue
            flag = '' if (len(r['top']) == 1 and len(r['bot']) == 1) else '  <-- NP FAILS'
            print('a=%d b=%d dim %3d top %s x%d bottom %s x%d%s' % (a, b, r['dim'], r['top'], r['ntop'], r['bot'], r['nbot'], flag))
            sys.stdout.flush()
