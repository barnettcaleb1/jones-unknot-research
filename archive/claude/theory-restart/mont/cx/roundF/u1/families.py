"""families.py -- engineC2's identically-J = 1 periodic S2 families (AAbd)^n, (Ab)^n, (aB)^n, (BB)^n.
For a family W_n = (W0)^n the translated halfword is s.l2 . w^n . f(w)^n . u1 with w = T(W0), f(w) = T(f(W0)) (translate.T).
LEMMA K test (gen_kernel, exact, PROVED criterion): is w a stabiliser of the top tangle T(s.l2) (acting at its lower end),
is f(w) a stabiliser of the bottom tangle B(u1 + u0) (acting at its upper end)?  If both: K(W_n) = K(s.l2.u1) for all n >= 0.
Also tests powers w^p, f(w)^p (p <= 6) and records the halfwords of the members n = 0..12 for certification."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gen_kernel as G, translate as TR
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2'); import plat2, lp
P = G.S2PIC
FAM = ['AAbd', 'Ab', 'aB', 'BB']
res = {}; words = []
for W0 in FAM:
    w = '.'.join(TR.T[ch] for ch in W0).split('.'); fw = '.'.join(TR.T[ch] for ch in TR.fword(W0)).split('.')
    r = {'w': '.'.join(w), 'f(w)': '.'.join(fw)}
    r['top_stab_p'] = [p for p in range(1, 7) if P.same_top([], w * p)]
    r['bot_stab_p'] = [p for p in range(1, 7) if P.same_bottom(fw * p, [])]
    Js = {}
    for n in range(0, 13):
        W = W0 * n
        if n and not plat2.is_arc(W):
            r.setdefault('not_arc_n', []).append(n); continue      # k = arc + closed loop: not a theta-curve
        h = TR.s2_halfword(W) if n else 's.l2.u1'
        assert h == '.'.join(['s', 'l2'] + w * n + fw * n + ['u1'])
        if n <= 8:
            Jp = plat2.J(W) if n else None
            Js[n] = (lp.J(h) == {0: 1}, Jp == {0: 1} if n else None)
        words.append(['%s^%d' % (W0, n), h])
    r['J_lp_plat2_unit_n<=8'] = Js
    res[W0] = r
    print(W0, 'w =', r['w'], '| f(w) =', r['f(w)'], '| top stabiliser for p in', r['top_stab_p'], '| bottom stabiliser for p in', r['bot_stab_p'])
    print('    J = 1 (lp, plat2) for n = 0..8:', Js, '| not a theta-curve for n in', r.get('not_arc_n'))
json.dump(res, open(os.path.join(HERE, 'out', 'families.json'), 'w'), indent=1)
json.dump(words, open(os.path.join(HERE, 'out', 'words_families.json'), 'w'))
