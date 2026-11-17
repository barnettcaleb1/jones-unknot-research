"""Q4: re-verify per-box certificates for 200 random boxes of C1's 46,771 'BOTH' boxes (gen2_res.pkl), and 50 random
signature pairs from the top-300 classes (n_min = 1 and n_min = 0).
For each box:
  (1) vector: vc.vec(tree) (engineA calculus) AND independently from two raw lp.J closures (rg_vecJ) -> must agree up to a unit;
  (2) own B-data (rg_gen.bdata_from_vec) -> must equal C1's signature key;
  (3) own generator (rg_gen.prove): own cases, own grid, own exact longest-path sup -> verdict per closure class;
  (4) C1's witness y regenerated with C1's own search (gen2/v3b3 imported read-only) and RE-CHECKED EXACTLY in our framework
      (our rows, our n-rule, our sup); C1's rows compared with ours."""
import sys, pickle, random, time
from multiprocessing import Pool
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen')
import rg_gen as G, rg_core as Cc
from fractions import Fraction as Fr
RG = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen/'
C1 = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1'
EA = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA'

# ---- C1 witness regeneration (C1 code imported, not edited) ----
_c1 = {}
def c1mods():
    if not _c1:
        sys.path.insert(1, C1); sys.path.insert(2, EA)
        import os; cwd = os.getcwd(); os.chdir(C1)
        import v3b, v3b3, h3b, gen2
        os.chdir(cwd)
        _c1.update(v3b=v3b, v3b3=v3b3, h3b=h3b, gen2=gen2)
    return _c1
def c1_cert(eqs, P0, nmin, npin=None):
    """C1's gen2.certify, returning the multiplier vector ys (None if C1 finds none) -- same search order"""
    m = c1mods(); v3b3 = m['v3b3']; gen2 = m['gen2']
    E = list(eqs) + [(0, 1, 0, 0, P0)]
    coeffs = tuple(tuple(Fr(x) for x in e[:4]) for e in E); rhs = [Fr(e[4]) for e in E]
    if npin is not None and npin < nmin: return 'npin<nmin'
    if npin is None:
        for ys, c, sf in v3b3.candidates(coeffs):
            r = sum(y * x for y, x in zip(ys, rhs))
            if r > nmin * sf + 1e-9 or (r > nmin * sf - 1e-9 and sf < 0):
                s = v3b3.sup_exact(*c)
                if s is not None and s <= 0 and r > nmin * s: return ys
        return None
    for ys, c, sf in gen2.candidates_any(coeffs):
        r = sum(y * x for y, x in zip(ys, rhs))
        if r > npin * sf + 1e-9:
            s = v3b3.sup_exact(*c)
            if s is not None and r > npin * s: return ys
    return None
NAMEMAP = {'d>=3': 'off>=3', 'd<=-3': 'off<=-3', 'd=0 r=0': 'off=0 e=+1', 'd=0 r=1': 'off=0 e=-1 r=1'}
for d in (2, 1, -1, -2):
    for e in (1, -1): NAMEMAP['d=%d e=%d' % (d, e)] = 'off=%d e=%+d' % (d, e)
def c1_witnesses(Bd, sigB, deltaB, nmin):
    """{(fam, myclass, end, mycase): (ys or None, C1 rows)}"""
    m = c1mods(); v3b = m['v3b']; h3b = m['h3b']
    out = {}
    mB = sigB + 1
    if mB != 0:
        for end in ('top', 'bot'):
            for asg in (1, -1):
                typ = '+' if (end == 'top') == (asg > 0) else '-'
                for a3 in (True, False):
                    if typ == '+' and not a3: continue
                    if typ == '+': cls = ['a=3', 'a>=5'] if end == 'top' else ['a=-3', 'a<=-5']
                    elif a3: cls = ['a=-3'] if end == 'top' else ['a=3']
                    else: cls = ['a<=-5'] if end == 'top' else ['a>=5']
                    for name, eqs, P0 in v3b.cases(Bd[end], mB, typ, a3):
                        if name.startswith('d=0'):
                            if typ == '-' and a3: ys = c1_cert(eqs, P0, nmin, npin=deltaB + 4)
                            elif typ == '-': ys = c1_cert(eqs, P0, max(nmin, deltaB + 6))
                            else: ys = c1_cert(eqs, P0, max(nmin, deltaB + 4))
                        else: ys = c1_cert(eqs, P0, nmin)
                        for c in cls:
                            out[('V', c, end, NAMEMAP[name])] = (ys, list(eqs) + [(0, 1, 0, 0, P0)])
    hn = {1: 'mu=1', -1: 'mu=-1', 2: 'mu=2', -2: 'mu=-2', 3: 'mu=3', -3: 'mu=-3', 4: 'mu>=4', -4: 'mu<=-4'}
    for mu in h3b.MUS:
        o, sgs, ds = h3b.WJ[mu]
        mBh = sigB - sgs; npin = deltaB - ds
        for end in ('top', 'bot'):
            p, q, _, _ = o[end]
            for name, eqs, P0 in h3b.cases_pq(Bd[end], mBh, p, q, allow_r1=(mBh != 0)):
                ys = c1_cert(eqs, P0, nmin, npin=npin) if name.startswith('d=0') else c1_cert(eqs, P0, nmin)
                out[('H', hn[mu], end, NAMEMAP[name])] = (ys, list(eqs) + [(0, 1, 0, 0, P0)])
    return out

def nrule_for(fam, cls, off0, deltaB, nmin):
    if not off0: return ('min', nmin)
    if fam == 'V':
        if cls in ('a=3', 'a=-3'):
            n = deltaB + 4
            return ('pin', n) if n >= nmin else ('pin', -1)
        return ('min', max(nmin, deltaB + 6))
    o, sgs, rule = G.HCL[cls]
    k, n = rule(deltaB)
    return ('pin', n) if n >= nmin else ('pin', -1)

def verify_sig(Bd, sigB, deltaB, nmin):
    """own generator + exact re-check of C1 witnesses.  Returns summary dict."""
    mine = G.prove(Bd, sigB, deltaB, nmin)
    mine_open = {k: v for k, v in mine.items() if v}
    wit = c1_witnesses(Bd, sigB, deltaB, nmin)
    nwit = 0; wit_ok = 0; wit_bad = []; rows_diff = 0; c1_none = 0
    for fam in ('V', 'H'):
        CL = G.VCL if fam == 'V' else G.HCL
        for cls, (o, sgs, rule) in CL.items():
            mB = sigB - sgs
            for end in ('top', 'bot'):
                pw, qw = o[end]
                for cname, rows, off0 in G.cases(pw, qw, Bd[end], mB):
                    key = (fam, cls, end, cname)
                    if key not in wit:
                        continue
                    ys, c1rows = wit[key]
                    if [tuple(Fr(x) for x in r) for r in c1rows] != [tuple(Fr(x) for x in r) for r in rows]:
                        rows_diff += 1
                    if ys is None: c1_none += 1; continue
                    nwit += 1
                    if ys == 'npin<nmin':
                        nr = nrule_for(fam, cls, off0, deltaB, nmin)
                        ok = (nr[0] == 'pin' and nr[1] < 0)
                    else:
                        ok = G.check_cert(rows, nrule_for(fam, cls, off0, deltaB, nmin), ys)
                    if ok: wit_ok += 1
                    else: wit_bad.append((key, ys))
    return dict(mine_open=mine_open, nwit=nwit, wit_ok=wit_ok, wit_bad=wit_bad[:5], nbad=len(wit_bad),
                rows_diff=rows_diff, c1_none=c1_none)

def work_box(arg):
    x, T, key = arg
    sys.path.insert(1, EA)
    import vc
    import rg_vecJ as VJ
    t0 = time.time()
    v = vc.vec(T)
    a, b = v
    res = dict(x=x)
    Bd, sg, dl, lcok, spa = G.bdata_from_vec(a, b)
    res['key_match'] = ((Bd['top'], Bd['bot'], sg, dl) == key) and lcok and spa >= 1
    res['span_a'] = spa
    try:
        w = VJ.vec_from_J(vc.word(T))
        res['vecJ'] = (w is not None and VJ.same_up_to_unit(v, w))
    except Exception as e:
        res['vecJ'] = 'err %s' % e
    res['tvec'] = time.time() - t0
    res.update(verify_sig(Bd, sg, dl, 1))
    res['t'] = time.time() - t0
    return res

def init_worker():
    G.load_gtab(RG + 'rg_gtab.pkl')

if __name__ == '__main__':
    mode = sys.argv[1]
    t0 = time.time()
    Gr = pickle.load(open(C1 + '/gen2_res.pkl', 'rb'))
    sigs = Gr['sigs']; resV = Gr['resV']; resH = Gr['resH']
    both = [k for k in sigs if resV[k][0] and all(not v for v in resH[k].values())]
    if mode == 'boxes':
        NB = int(sys.argv[2]) if len(sys.argv) > 2 else 200
        pool_x = [(x, k) for k in both for x in sigs[k]]
        assert len(pool_x) == 46771, len(pool_x)
        random.seed(20261117)
        pick = random.sample(pool_x, NB)
        args = [(x, Gr['trees'][x], k) for x, k in pick]
        with Pool(int(sys.argv[3]) if len(sys.argv) > 3 else 6, initializer=init_worker) as P:
            out = []
            for i, r in enumerate(P.imap_unordered(work_box, args)):
                out.append(r)
                if (i + 1) % 20 == 0: print('  done', i + 1, round(time.time() - t0, 1), flush=True)
        pickle.dump(out, open(RG + 'rg_q4_boxes.pkl', 'wb'))
        nprov = sum(1 for r in out if not r['mine_open'])
        print('boxes checked', len(out), '| vector via lp.J closures == vc.vec up to unit:', sum(1 for r in out if r['vecJ'] is True),
              '| own B-data == C1 signature key:', sum(1 for r in out if r['key_match']))
        print('own generator proves ALL classes (V all odd |a|>=3, H all mu):', nprov, '/', len(out))
        print('C1 witnesses regenerated:', sum(r['nwit'] for r in out), ' exact re-check OK:', sum(r['wit_ok'] for r in out),
              ' FAILED:', sum(r['nbad'] for r in out), ' C1 rows != own rows:', sum(r['rows_diff'] for r in out),
              ' C1 found no witness:', sum(r['c1_none'] for r in out))
        for r in out:
            if r['mine_open'] or r['nbad'] or r['vecJ'] is not True or not r['key_match']:
                print('  ISSUE', r['x'], r['mine_open'], r['wit_bad'], r['vecJ'], r['key_match'])
        print('min span a', min(r['span_a'] for r in out), 'time %.1f' % (time.time() - t0))
    elif mode == 'pairs':
        NP = int(sys.argv[2]) if len(sys.argv) > 2 else 50
        top = sorted(sigs.items(), key=lambda kv: -len(kv[1]))[:300]
        import itertools
        allpairs = list(itertools.combinations_with_replacement(range(300), 2))
        random.seed(20261118)
        pick = random.sample(allpairs, NP)
        init_worker()
        def add(a, b): return tuple(x + y for x, y in zip(a, b))
        tot = dict(n=0, prov1=0, prov0=0, wit=0, witok=0, bad=0, rowsd=0, none=0)
        issues = []
        for (i, j) in pick:
            k1 = top[i][0]; k2 = top[j][0]
            Bd = {'top': add(k1[0], k2[0]), 'bot': add(k1[1], k2[1])}; sg = k1[2] + k2[2]; dl = k1[3] + k2[3]
            for nmin in (1, 0):
                r = verify_sig(Bd, sg, dl, nmin)
                tot['n'] += 1
                if not r['mine_open']: tot['prov%d' % nmin] += 1
                else: issues.append((i, j, nmin, r['mine_open']))
                tot['wit'] += r['nwit']; tot['witok'] += r['wit_ok']; tot['bad'] += r['nbad']; tot['rowsd'] += r['rows_diff']
                tot['none'] += r['c1_none']
                if r['nbad']: issues.append((i, j, nmin, 'witness fail', r['wit_bad']))
        print('pairs', NP, tot)
        for s in issues[:20]: print('  ISSUE', s)
        print('time %.1f' % (time.time() - t0))
