"""Referee P4a: Corollary S on random AXIS-FREE words (n0 = 0 <=> connected-sum diagram K_R # K_R swapped by h).
Compare lp.J(word) with the independent 2-cable J_3(K_R) (j3lib).  Also necklace words with axis-free boxes."""
import random, sys, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import lp
from j3lib import J3, jones_KR, inv

def rand_noaxis(rnd, L, maxw):
    for _ in range(500):
        w = 1; toks = []
        for _ in range(L):
            r = rnd.random()
            if w < maxw and (w < 2 or r < 0.25):
                i = rnd.randint(1, w + 1); toks.append(rnd.choice('lr') + str(i)); w += 2
            elif w >= 3 and r < 0.38:
                i = rnd.randint(1, w - 1); toks.append('u' + str(i)); w -= 2
            else:
                i = rnd.randint(1, w - 1); toks.append(rnd.choice('xy') + str(i))
        while w > 1:
            if rnd.random() < 0.6:
                i = rnd.randint(1, w - 1); toks.append(rnd.choice('xy') + str(i))
            i = rnd.randint(1, w - 1); toks.append('u' + str(i)); w -= 2
        out = []
        for t in toks:
            if out and out[-1][1:] == t[1:] and out[-1][0] in 'xy' and t[0] in 'xy' and out[-1][0] != t[0]:
                out.pop()
            else:
                out.append(t)
        if sum(1 for t in out if t[0] in 'xy') >= 3:
            return '.'.join(out)
    return None

rnd = random.Random(int(sys.argv[2]) if len(sys.argv)>2 else 424242)
t0 = time.time()
stats = {'words': 0, 'knots': 0, 'nontrivialKR': 0, 'equal': 0, 'equal_mirror_only': 0, 'fail': 0}
fails = []
spans = {}
for it in range(int(sys.argv[1]) if len(sys.argv)>1 else 400):
    B = rand_noaxis(rnd, rnd.randint(8, 26), rnd.choice([3, 5, 7]))
    if B is None:
        continue
    if rnd.random() < 0.35:
        # necklace word with axis-free boxes
        B2 = rand_noaxis(rnd, rnd.randint(4, 10), 5)
        m = rnd.choice([1, -1, 2, -2, 3])
        tw = ['y1'] * m if m > 0 else ['x1'] * (-m)
        word = 's.' + '.'.join(['r2'] + tw + B.split('.') + (B2.split('.') if B2 else []) + ['u1'])
    else:
        word = 's.' + B
    stats['words'] += 1
    Jw = lp.J(word)
    if Jw is None:
        continue
    stats['knots'] += 1
    j3 = J3(word)
    if not isinstance(j3, dict):
        fails.append((word, 'J3 error', str(j3)[:60])); stats['fail'] += 1; continue
    jk = jones_KR(word)
    triv = (jk is not None and len(jk) == 1)
    if not triv:
        stats['nontrivialKR'] += 1
        spans[len(j3)] = spans.get(len(j3), 0) + 1
    if Jw == j3:
        stats['equal'] += 1
    elif Jw == inv(j3):
        stats['equal_mirror_only'] += 1; fails.append((word, 'mirror only'))
    else:
        stats['fail'] += 1; fails.append((word, 'DIFFERENT'))
print(stats, 'time %.1f' % (time.time() - t0))
print('number-of-terms histogram of J3 over nontrivial K_R:', sorted(spans.items()))
for f in fails[:10]:
    print('FAIL', f)
# distinct nontrivial K_R seen (by Jones of K_R up to mirror)
