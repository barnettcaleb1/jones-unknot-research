"""U5: regenerate engineA's Lemma W brute-force validation units EXACTLY and store them.
Source of the procedure: engineA's validation was run inline (python -c, not saved as a file); the exact code was recovered
from engineA's session transcript (tool calls at 00:27:28 and 00:33:44 CST): 
  run 1 (seed 5): 80 horizontal trials (products of k in {1,1,2} random rational words of length 1..5, brute force
         N in [-14,14], mu in [-30,30] minus {0}; units with N in the 'scalar' set allN of eng.hclosures excluded) -> '167 units',
         then, SAME random stream, 50 vertical trials (word length 0..5, odd a in [-31,31], N in [-14,14]) -> 140 units;
  run 2 (seed 11): 60 vertical trials -> 168 units.   167 horizontal + 308 = 140 + 168 vertical, as in engineA's REPORT.
The random stream is reproduced statement by statement (rword, k, word lengths); the brute force uses only engineA's vc.py
(read-only import); eng.hclosures / eng.vclosures (engineA's eng.py, read-only) are re-run as the Lemma W completeness check.
Each unit's knot is built with engineA's own dictionary (units.py unit_word): horizontal ('H', mu, N, T) ->
vc.hw(('n', -mu, [T] + [Y^N])), vertical ('V', a, N, T) -> vc.vert_word(a, vc.word(('p', [T] + [Y^N]))), T = ('p', leaves).
Output: units.json (every unit with its halfword, the calculus J, and the recovery flag)."""
import sys, json, time
sys.dont_write_bytecode = True
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import eng, vc
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45/u5/'

def make_rword(rnd):
    def rword(L):
        w = ''
        while len(w) < L:
            c = rnd.choice('XxYy')
            if w and {'X': 'x', 'x': 'X', 'Y': 'y', 'y': 'Y'}[c] == w[-1]: continue
            w += c
        return w
    return rword

def ynode(N): return [('w', ('Y' if N > 0 else 'y') * abs(N))] if N else []
def h_word(mu, N, words):
    T = ('p', [('w', w) for w in words])
    return vc.hw(('n', -mu, [T] + ynode(N))), ('n', -mu, [T] + ynode(N))
def v_word(a, N, words):
    T = ('p', [('w', w) for w in words])
    return vc.vert_word(a, vc.word(('p', [T] + ynode(N))))

units = []; scalar_units = []; summary = {}
import random
# ---------------- run 1, seed 5 ----------------
rnd = random.Random(5); rword = make_rword(rnd)
t0 = time.time(); tot = 0; agree = 0; nunits = 0
for trial in range(80):
    k = rnd.choice([1, 1, 2])
    words = [rword(rnd.randint(1, 5)) for _ in range(k)]
    vs = [vc.rat(w) for w in words]
    p = vc.starall(vs)
    bf = set()
    for N in range(-14, 15):
        for mu in range(-30, 31):
            if mu == 0: continue
            J = vc.Xpow(mu, vc.Ypow(N, p))[0]
            if len(J) == 1: bf.add((mu, N))
    hc = eng.hclosures(p)
    allN = set(N for mu, N, J in hc if mu == 'all' and len(J) == 1)
    cs = set((mu, N) for mu, N, J in hc if mu != 'all' and len(J) == 1)
    bf2 = set(x for x in bf if x[1] not in allN)
    tot += 1; agree += (bf2 <= cs); nunits += len(bf2)
    for (mu, N) in sorted(bf):
        hw, T = h_word(mu, N, words)
        Jt = vc.Jtree(T)
        rec = {'set': 'H', 'run': 'seed5', 'trial': trial, 'words': words, 'mu': mu, 'N': N, 'halfword': hw,
               'J_calculus': sorted(Jt.items()) if Jt else None, 'recovered_by_eng': (mu, N) in cs}
        if (mu, N) in bf2: units.append(rec)
        else: rec['set'] = 'H-scalar'; scalar_units.append(rec)
summary['horizontal'] = {'trials': tot, 'complete': agree, 'units_nonscalar': nunits, 'secs': round(time.time() - t0, 1)}
print('horizontal: trials', tot, 'complete', agree, 'units (non-scalar) found', nunits, round(time.time() - t0, 1), flush=True)
def vertical(rnd, rword, ntr, run):
    t0 = time.time(); tot = agree = nunits = 0
    for trial in range(ntr):
        k = rnd.choice([1, 1, 2])
        words = [rword(rnd.randint(0, 5)) for _ in range(k)]
        p = vc.starall([vc.rat(w) for w in words])
        bf = set()
        for N in range(-14, 15):
            for a in range(-31, 32, 2):
                J = vc.raw_vert(a, vc.Ypow(N, p))
                if len(J) == 1: bf.add((a, N))
        cs = set((a, N) for a, N, J in eng.vclosures(p) if len(J) == 1)
        tot += 1; agree += (bf <= cs); nunits += len(bf)
        for (a, N) in sorted(bf):
            hw = v_word(a, N, words)
            Jv = vc.J_vert(a, vc.Ypow(N, p))
            units.append({'set': 'V', 'run': run, 'trial': trial, 'words': words, 'a': a, 'N': N, 'halfword': hw,
                          'J_calculus': sorted(Jv.items()) if Jv else None, 'recovered_by_eng': (a, N) in cs})
    print('vertical', run, ': trials', tot, 'complete', agree, 'units', nunits, round(time.time() - t0, 1), flush=True)
    return {'trials': tot, 'complete': agree, 'units': nunits, 'secs': round(time.time() - t0, 1)}
summary['vertical_seed5'] = vertical(rnd, rword, 50, 'seed5')
rnd2 = random.Random(11); rword2 = make_rword(rnd2)
summary['vertical_seed11'] = vertical(rnd2, rword2, 60, 'seed11')
json.dump({'summary': summary, 'units': units, 'scalar_units': scalar_units}, open(OUT + 'units.json', 'w'), indent=0)
from collections import Counter
print('stored units', Counter(u['set'] for u in units), 'scalar (excluded from 167)', len(scalar_units),
      'distinct halfwords', len(set(u['halfword'] for u in units)), len(set(u['halfword'] for u in scalar_units)))
print('J_calculus == 1:', Counter((u['set'], u['J_calculus'] == [[0, 1]]) for u in units + scalar_units))
