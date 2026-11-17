"""Q5 (and Q3 identity checks): random closures built from C1-certified ('BOTH') boxes B plus n = 1..3 random non-integral
rational boxes, integral part N chosen at a Lemma-W end coincidence (top or bottom degree tie) whenever one exists.
 mode 'ident'  (cheap, exact polynomial arithmetic, many closures):
     (i)  sigma-law: (X2-X1)_top + (X2-X1)_bot == m_B := sigma(B) - sigma*(closure)  [X_i = l1 of the normalised S_i]
     (ii) offset formulas: the normalised x1, x2 of F at each end equal the case formula used by the generator
     (iii) F is never c t^e Phi_3 (no unit)
 mode 'lpJ'    (expensive): exact lp.J of the explicit half-word; must equal the vector-calculus J; must not be a unit."""
import sys, pickle, random, time
from multiprocessing import Pool
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen')
sys.path.insert(1, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
sys.path.insert(2, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import rg_core as C, rg_gen as G
from fractions import Fraction as Fr
RG = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen/'
C1 = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1'
PHI3 = {0: 1, 1: 1, 2: 1}
INV = {'X': 'x', 'x': 'X', 'Y': 'y', 'y': 'Y'}
def rand_ratword(rng, Lmax=5):
    while True:
        L = rng.randint(2, Lmax)
        w = rng.choice('Xx')
        while len(w) < L:
            c = rng.choice('XxYy')
            if INV[c] != w[-1]: w += c
        # non-integral?
        n, nf = C.normal_form(w)
        if nf: return w
def xs(p, end, K=2):
    d, c, x = C.enddata(p, end, K)
    return d, c, x
def norm_coeffs_F(S1, S2, end):
    """exact normalised (x1, x2) of F = S1 + S2 at end, and (off, eps, x(s1), x(s2))"""
    F = C.padd(S1, S2)
    d1, c1, x1 = xs(S1, end, 3); d2, c2, x2 = xs(S2, end, 3)
    off = (d1 - d2) if end == 'top' else (d2 - d1)
    eps = Fr(c2, c1)
    dF, cF, xF = xs(F, end, 2)
    return off, eps, x1, x2, xF, dF, (d1 if off >= 0 else d2)
def predicted(off, e, x1, x2):
    if off >= 3: return (x1[0], x1[1])
    if off == 2: return (x1[0], x1[1] + e)
    if off == 1: return (x1[0] + e, x1[1] + e * x2[0])
    if off == 0 and e == 1: return ((x1[0] + x2[0]) / 2, (x1[1] + x2[1]) / 2)
    if off == 0 and e == -1:
        k = x1[0] - x2[0]
        if k == 0: return None
        return ((x1[1] - x2[1]) / k, (x1[2] - x2[2]) / k)
    if off == -1: return (x2[0] + e, x2[1] + e * x1[0])
    if off == -2: return (x2[0], x2[1] + e)
    return (x2[0], x2[1])
def build(rng, B, fam, Lmax=5, nmax=3):
    """returns closure dict with product channels (A, Bc), w-factors, N, tree"""
    tag, T, v, key = B
    n = rng.randint(1, nmax)
    words = [rand_ratword(rng, Lmax) for _ in range(n)]
    import vc
    rv = [vc.rat(w) for w in words]
    A = v[0]; Bc = v[1]
    for r in rv: A = C.pmul(A, r[0]); Bc = C.pmul(Bc, r[1])
    if fam == 'H':
        mu = rng.choice([x for x in range(-6, 7) if x])
        w1 = G.w1(mu); w2 = G.w3(mu); par = mu
    else:
        a = rng.choice([-7, -5, -3, -1, 1, 3, 5, 7])
        w1 = G.w1(a); w2 = G.wV(a); par = a
    cands = []
    for end in ('top', 'bot'):
        if end == 'top': x = max(w2) + max(Bc) - max(w1) - max(A)
        else: x = min(w2) + min(Bc) - min(w1) - min(A)
        if x % 3 == 0: cands.append(x // 3)
    N = rng.choice(cands) if cands else rng.randint(-3, 3)
    return dict(tag=tag, T=T, words=words, fam=fam, par=par, N=N, A=A, Bc=Bc, w1=w1, w2=w2, forced=bool(cands), key=key)
def ident(cl):
    """sigma-law + offset formulas + no-unit on an exact closure"""
    A, Bc, w1, w2, N = cl['A'], cl['Bc'], cl['w1'], cl['w2'], cl['N']
    S1 = C.pmul(w1, A); S2 = C.pmul(w2, C.pshift(Bc, -3 * N))
    key = cl['key']; sigB = key[2]
    o, sgs, ds = G.wjets(w1, w2)
    mB = sigB - sgs
    mism = 0; out = dict(form_ok=0, form_n=0, unit=False)
    for end in ('top', 'bot'):
        off, eps, x1, x2, xF, dF, d0 = norm_coeffs_F(S1, S2, end)
        l1a = x1[0]; l1b = x2[0]
        mism += l1b - l1a                  # X2 - X1 (x1 = l1)
        p = predicted(off, eps, x1, x2)
        if p is not None and (off != 0 or eps != -1 or True):
            # r=1 prediction applies only if the order-1 cancellation is exactly one order
            if off == 0 and eps == -1:
                # F degree must be d0 - 1 (top) / d0 + 1 (bot) for the formula
                if (end == 'top' and dF != d0 - 1) or (end == 'bot' and dF != d0 + 1):
                    continue
            out['form_n'] += 1
            if tuple(p) == tuple(xF[:2]): out['form_ok'] += 1
            else: out.setdefault('form_bad', []).append((end, off, eps))
    out['sigma_ok'] = (mism == mB)
    F = C.padd(S1, S2)
    if (max(F) - min(F)) == 2 and len(F) == 3:
        c = F[max(F)]
        if all(F.get(min(F) + i, 0) == c for i in range(3)) and abs(c) == 1: out['unit'] = True
    return out
def lpJ(cl):
    import vc, lp
    kids = [cl['T']] + [('w', w) for w in cl['words']]
    N = cl['N']
    if N: kids.append(('w', ('Y' if N > 0 else 'y') * abs(N)))
    if cl['fam'] == 'H':
        mu = cl['par']; m = -mu
        T = ('n', m, kids)
        hw = vc.hw(T)
        Jc = vc.J_neck(mu, vc.starall([vc.vec(k) for k in kids]))
    else:
        a = cl['par']
        body = vc.word(('p', kids))
        hw = vc.vert_word(a, body)
        Jc = vc.J_vert(a, vc.starall([vc.vec(k) for k in kids]))
    t0 = time.time()
    J = lp.J(hw)
    return dict(hw_len=len(hw.split('.')), J_unit=(J is not None and len(J) == 1), J_none=(J is None),
                agree=(J == Jc), spanJ=(max(J) - min(J)) if J else None, t=time.time() - t0, fam=cl['fam'],
                par=cl['par'], forced=cl['forced'], tag=cl['tag'])
def load_boxes():
    import vc
    Gr = pickle.load(open(C1 + '/gen2_res.pkl', 'rb'))
    sigs = Gr['sigs']; resV = Gr['resV']; resH = Gr['resH']
    both = [k for k in sigs if resV[k][0] and all(not v for v in resH[k].values())]
    return Gr, [(x, k) for k in both for x in sigs[k]]
def job_ident(arg):
    seed, NPER = arg
    import vc
    rng = random.Random(seed)
    Gr, pool = load_boxes()
    res = dict(n=0, sig_ok=0, form_n=0, form_ok=0, units=0, forced=0, bad=[])
    for i in range(NPER):
        x, k = rng.choice(pool)
        T = Gr['trees'][x]; v = vc.vec(T)
        B = (Gr['tags'][x], T, v, k)
        cl = build(rng, B, rng.choice('HV'))
        r = ident(cl)
        res['n'] += 1; res['sig_ok'] += r['sigma_ok']; res['form_n'] += r['form_n']; res['form_ok'] += r['form_ok']
        res['units'] += r['unit']; res['forced'] += cl['forced']
        if not r['sigma_ok'] or r['form_ok'] != r['form_n']:
            if len(res['bad']) < 5: res['bad'].append((x, cl['fam'], cl['par'], cl['N'], cl['words'], r))
    return res
def job_lpJ(arg):
    seed, = arg
    import vc
    rng = random.Random(seed)
    Gr, pool = load_boxes()
    x, k = rng.choice(pool)
    T = Gr['trees'][x]; v = vc.vec(T)
    for tries in range(12):        # prefer closures with a Lemma-W end coincidence (forced N)
        cl = build(rng, (Gr['tags'][x], T, v, k), rng.choice('HV'), Lmax=3, nmax=2)
        if cl['forced']: break
    r = lpJ(cl); r['x'] = x; r['seed'] = seed; r['N'] = cl['N']; r['words'] = cl['words']
    return r
NPER = 500
if __name__ == '__main__' and sys.argv[1] in ('ident', 'lpJ'):
    mode = sys.argv[1]
    t0 = time.time()
    if mode == 'ident':
        NPER = int(sys.argv[2]) if len(sys.argv) > 2 else 500
        nj = int(sys.argv[3]) if len(sys.argv) > 3 else 6
        with Pool(nj) as P:
            rs = P.map(job_ident, [(1000 + i, NPER) for i in range(nj * 2)])
        tot = {k: sum(r[k] for r in rs) for k in ('n', 'sig_ok', 'form_n', 'form_ok', 'units', 'forced')}
        print('identity checks:', tot, 'time %.1f' % (time.time() - t0))
        for r in rs:
            for b in r['bad']: print('  BAD', b)
    else:
        NC = int(sys.argv[2]); nj = int(sys.argv[3]) if len(sys.argv) > 3 else 6
        out = []
        with Pool(nj) as P:
            for i, r in enumerate(P.imap_unordered(job_lpJ, [(50000 + i,) for i in range(NC)])):
                out.append(r)
                if (i + 1) % 50 == 0:
                    print('  %d done, units %d, disagreements %d, None %d, %.0fs' % (
                        i + 1, sum(o['J_unit'] for o in out), sum(not o['agree'] for o in out),
                        sum(o['J_none'] for o in out), time.time() - t0), flush=True)
                    pickle.dump(out, open(RG + 'rg_q5_lpJ.pkl', 'wb'))
        pickle.dump(out, open(RG + 'rg_q5_lpJ.pkl', 'wb'))
        print('closures', len(out), 'lp.J units', sum(o['J_unit'] for o in out), 'lp.J == vector calculus',
              sum(o['agree'] for o in out), 'J None', sum(o['J_none'] for o in out),
              'forced coincidence', sum(o['forced'] for o in out), 'H', sum(o['fam'] == 'H' for o in out),
              'min span J', min(o['spanJ'] for o in out if o['spanJ'] is not None), 'time %.0f' % (time.time() - t0))

# ---- redesigned lp.J run (load-aware): V from all certified boxes, H from certified boxes of nesting depth <= 3 ----
def _depth(word):
    d = 0; mx = 0
    for tok in word.split('.'):
        if tok and tok[0] in 'rl': d += 1; mx = max(mx, d)
        elif tok and tok[0] == 'u': d -= 1
    return mx
def rand_light_word(rng, Lmax=3, maxX=1):
    while True:
        w = rand_ratword(rng, Lmax)
        if sum(1 for c in w if c in 'Xx') <= maxX: return w
def job_lpJ2(arg):
    seed, fam = arg
    import vc
    rng = random.Random(seed)
    Gr, pool = load_boxes()
    while True:
        x, k = rng.choice(pool)
        T = Gr['trees'][x]
        if fam == 'V' or _depth(vc.word(T)) <= 3: break
    v = vc.vec(T)
    for tries in range(12):
        n = rng.randint(1, 2)
        words = [rand_light_word(rng, 3, 2 if fam == 'V' else 1) for _ in range(n)]
        rv = [vc.rat(w) for w in words]
        A = v[0]; Bc = v[1]
        for r in rv: A = C.pmul(A, r[0]); Bc = C.pmul(Bc, r[1])
        if fam == 'H':
            par = rng.choice([y for y in range(-6, 7) if y]); w1 = G.w1(par); w2 = G.w3(par)
        else:
            par = rng.choice([-7, -5, -3, -1, 1, 3, 5, 7]); w1 = G.w1(par); w2 = G.wV(par)
        cands = []
        for end in ('top', 'bot'):
            xx = (max(w2) + max(Bc) - max(w1) - max(A)) if end == 'top' else (min(w2) + min(Bc) - min(w1) - min(A))
            if xx % 3 == 0: cands.append(xx // 3)
        if cands: break
    N = rng.choice(cands) if cands else rng.randint(-3, 3)
    cl = dict(tag=Gr['tags'][x], T=T, words=words, fam=fam, par=par, N=N, forced=bool(cands), key=k)
    r = lpJ(cl); r['x'] = x; r['seed'] = seed; r['N'] = N; r['words'] = words
    return r
if __name__ == '__main__' and sys.argv[1] == 'lpJ2':
    NC = int(sys.argv[2]); nj = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    args = []
    for i in range(NC):
        args.append((70000 + i, 'V' if i % 2 == 0 else 'H'))
    out = []
    t0 = time.time()
    with Pool(nj) as P:
        for i, r in enumerate(P.imap_unordered(job_lpJ2, args)):
            out.append(r)
            if (i + 1) % 50 == 0:
                print('  %d done, units %d, disagreements %d, None %d, %.0fs' % (
                    i + 1, sum(o['J_unit'] for o in out), sum(not o['agree'] for o in out),
                    sum(o['J_none'] for o in out), time.time() - t0), flush=True)
                pickle.dump(out, open(RG + 'rg_q5_lpJ.pkl', 'wb'))
    pickle.dump(out, open(RG + 'rg_q5_lpJ.pkl', 'wb'))
    sj = [o['spanJ'] for o in out if o['spanJ'] is not None]
    print('closures', len(out), '| lp.J units', sum(o['J_unit'] for o in out), '| lp.J == vector calculus',
          sum(o['agree'] for o in out), '| J None', sum(o['J_none'] for o in out),
          '| forced coincidence', sum(o['forced'] for o in out), '| H', sum(o['fam'] == 'H' for o in out),
          '| V', sum(o['fam'] == 'V' for o in out), '| min span J', min(sj) if sj else None, '| time %.0f' % (time.time() - t0))
