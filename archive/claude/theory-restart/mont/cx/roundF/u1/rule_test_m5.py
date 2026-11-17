"""rule_test_m5.py -- discriminating test of rule (R) at a ring level with m = 5 k strands (Delta^2 of 5 strands; used by
E4 bodies with caps).  Random point-symmetric theta-curves: top = capA(0), splitR(0), proj(1), capK(2), capK(4)
(level a,k,k,k,k,k,a), then a random word in: k-crossings X/Y at positions 1..4, A_l rings XX/YY at 0, A_r rings XX/YY
at 5; glued with sym.symmetric.  Compare theta.J_events(original) (engineC2's direct evaluator) with lp.J of the translated
halfword, and with a WRONG-handed translation (control).  Only theta-curves (k one arc, K a knot) are counted."""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import translate as TR
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import theta, sym, lp
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools'); import alex
rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 3); NT = int(sys.argv[2]) if len(sys.argv) > 2 else 40
TOP = [('capA', 0), ('splitR', 0), ('proj', 1), ('capK', 2), ('capK', 4)]
def wrong_transfer(ev):
    out = []; i = 0
    ev2, nr = TR.transfer(ev)
    return ev2
n = agree = wrong_agree = 0; t0 = time.time(); tries = 0
while n < NT and tries < 2000:
    tries += 1
    word = []
    for _ in range(rng.randint(3, 6)):
        r = rng.random(); t = rng.choice('XY')
        if r < 0.25: word += [(t, 5), (t, 5)]
        elif r < 0.4: word += [(t, 0), (t, 0)]
        else: word.append((t, rng.randint(1, 4)))
    if not any(e == ('X', 5) or e == ('Y', 5) for e in word): continue
    ev = sym.symmetric(TOP + word)
    try:
        ev2, nr = TR.transfer(ev); h = TR.events_to_halfword(ev2)
    except AssertionError:
        continue
    if alex.diagram(alex.symmetrize(alex.parse(h))) is None: continue      # not a knot (k not one arc)
    J0 = theta.J_events(ev)
    if J0 is None: continue
    Jh = lp.J(h)
    # wrong-handed: swap X <-> Y inside every Delta^2 produced by the rule (rebuild with opposite type)
    evw = []
    i = 0; cols = []
    for e in ev: pass
    hw_wrong = None
    try:
        # rebuild by replacing each A_r ring by the opposite-handed full twist
        out = []; cols = []; j = 0
        while j < len(ev):
            e = ev[j]; typ = e[0]
            if typ in ('X', 'Y') and e[1] + 1 == len(cols) - 1 and cols[e[1] + 1] == 'a':
                out += TR.full_twist_events(e[1], 'Y' if typ == 'X' else 'X'); j += 2; continue
            if typ in ('X', 'Y'): p = e[1]; cols[p], cols[p + 1] = cols[p + 1], cols[p]
            elif typ in ('capA', 'capK'): p = e[1]; c = 'a' if typ == 'capA' else 'k'; cols[p:p] = [c, c]
            elif typ == 'cup': del cols[e[1]:e[1] + 2]
            elif typ == 'splitR': cols[e[1] + 1:e[1] + 1] = ['k']
            elif typ == 'mergeL': out += [('mergeR', 0), ('cup', 0)]; break
            out.append(e); j += 1
        hw_wrong = TR.events_to_halfword(out)
    except AssertionError:
        pass
    Jw = lp.J(hw_wrong) if hw_wrong else None
    n += 1; agree += (J0 == Jh); wrong_agree += (J0 == Jw)
    if J0 != Jh: print('MISMATCH', word, h, J0, Jh, flush=True)
print('m=5 random theta-curves', n, 'J(original) == lp.J(translated):', agree, '| wrong-handed agree:', wrong_agree,
      '| secs', round(time.time() - t0, 1))
