from t_common import *
import random, io, contextlib
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
NT = int(sys.argv[2]) if len(sys.argv) > 2 else 40
MAXC = int(sys.argv[3]) if len(sys.argv) > 3 else 9

def random_word(maxc):
    while True:
        n = 1; w = []; nc = 0
        steps = random.randint(6, 16)
        for _ in range(steps):
            ops = []
            if n <= 3: ops.append('cap')
            if n >= 2: ops += ['cr'] * 4
            if n >= 4: ops.append('cup')
            op = random.choice(ops)
            if op == 'cap':
                i = random.randint(1, n); w.append(random.choice('lr') + str(i)); n += 2
            elif op == 'cup':
                i = random.randint(0, n - 2); w.append('u' + str(i)); n -= 2
            else:
                i = random.randint(0, n - 2); w.append(random.choice('xy') + str(i)); nc += 1
        while n > 3:
            i = random.randint(0, n - 2); w.append('u' + str(i)); n -= 2
        if n == 3 and 3 <= nc <= maxc:
            return '.'.join(w)

seen = 0; bad = 0; noncollapse = []
stats = collections.Counter()
while seen < NT:
    w = random_word(MAXC)
    try:
        D = closure13(w)
    except AssertionError:
        continue
    if D.ncomp != 2 or D.comp[D.marks[0]] == D.comp[D.marks[1]]: continue
    if sum(D.mixed) == 0: continue
    seen += 1
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        R = analyse(D, w, verbose=False, show_pairs=False)
    dE1 = sum(R['E1'].values()); dH = sum(R['Htot'].values()); dT = sum(R['tensor'].values())
    ok = R['shift'] is not None and R['shift'] == -2 * D.linking(0, 1)
    stats[(dE1, dH, tuple(sorted(sum(c.values()) for c in R['comps'])))] += 1
    if not ok:
        bad += 1; print('MISMATCH', w); print(buf.getvalue())
    if dE1 > dH:
        noncollapse.append((w, dE1, dH, max(k for _, _, k in R['pairs'])))
print('tested', seen, 'random 2-component closures; mismatches with Theorem A (total homology != shifted Kh~ (x) Kh~):', bad)
print('(dim E_1, dim total, dims of Kh~ of the components): count')
for k, v in sorted(stats.items()): print('  ', k, v)
print('non-collapsing examples (word, dim E_1, dim E_inf, last page with a differential):')
for x in noncollapse[:15]: print('  ', x)
