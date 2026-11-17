"""Do the E3 near-miss J's occur among SHORT width-two words?  Hash every (top,bottom) pair of the (D1,D2) enumeration at
t = zeta_7 against the unit-orbits {+-zeta_7^k J_i(zeta_7)} of target J_i; confirm hits exactly.  usage: find_short.py D1 D2"""
import sys, json, glob
from collections import defaultdict
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
import mitm, rho2, fastJ
P = mitm.P
def main(D1, D2):
    z7 = mitm.root_of_unity(7)
    targets = []
    for f in sorted(glob.glob('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/e3_n*_s1[0-9][0-9].json')):
        r = json.load(open(f))
        for x in r['top_a2zero'][:6]:
            targets.append((tuple(map(tuple, x['J'])), x['word']))
    targets = list(dict(targets).items())
    tmap = {}
    for J, w in targets:
        val = sum(c * pow(z7, e % (P - 1), P) for e, c in J) % P
        for k in range(7):
            for s in (1, -1):
                tmap[(s * val * pow(z7, k, P)) % P] = J
    MT, VT, PHIT = rho2.normalised()
    import random
    tg = random.Random(1).randrange(2, P - 1)
    ts = [tg, z7]
    Ms = [{L: [[mitm.evt(x, t) for x in row] for row in m] for L, m in MT.items()} for t in ts]
    V = [[mitm.evt(x, t) for x in VT['l1.l1']] for t in ts]
    PH = []
    for t in ts:
        c = t * t % P * pow(pow(1 + t, 4, P), P - 2, P) % P
        PH.append([mitm.evt(x, t) * c % P for x in PHIT['u2.u2']])
    tops = mitm.bfs(Ms, V, D1, 'top'); bots = mitm.bfs(Ms, PH, D2, 'bot')
    TG = defaultdict(list); BG = defaultdict(list)
    for w, vecs in tops: TG[mitm.top_class(w)].append((w, vecs[1]))
    for w, vecs in bots: BG[mitm.bot_class(w)].append((w, vecs[1]))
    found = {}
    for tc, tl in TG.items():
        for bc, bl in BG.items():
            if not mitm.knot_ok(tc, bc): continue
            for wb, b in bl:
                for wt, u in tl:
                    s = sum(x * y for x, y in zip(b, u)) % P
                    if s in tmap:
                        J = tmap[s]
                        W = list(wt) + list(wb)
                        if J in found and len(found[J]) <= len(W): continue
                        Jx = fastJ.J('l1.l1', W, 'u2.u2')
                        if Jx is not None and tuple(sorted(Jx.items())) == J: found[J] = W
    print('targets', len(targets), 'realised by words of length <=', D1 + D2, ':', len(found))
    for J, w in targets:
        print('  span', max(e for e, _ in J) - min(e for e, _ in J), 'E3 word length', len(w.split('.')) - 5,
              '-> shortest found', ('.'.join(found[J]) if J in found else None))
if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
