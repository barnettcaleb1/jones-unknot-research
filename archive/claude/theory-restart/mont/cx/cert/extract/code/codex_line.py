"""Regression requested in Codex msg 20261117-020642: V = x2.x1, U = x1, direction (1,-1), offset 0:
s.l1.l1.x2.x1.(x1)^(2k).(y3)^(2k).x1.u2.u2 (k = -6..6).  Exact J (fastJ) and certification (word moves, then PD stages).
Also: why template_screen.py never sampled this line (its 'possible' test returns 'trivial' when all nonzero sectors share one
slope along d, and such directions are dropped)."""
import sys, json, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
import fastJ, rules, certify_lib as C, pd as PDm, vk
import template_screen as TS
nz = frozenset([(0, 0), (2, 2), (4, 4)])
print('template_screen.possible(nz={00,22,44}, d=(1,-1)) =', TS.possible(nz, (1, -1)))
out = []
for k in range(-6, 7):
    W = ['x2', 'x1'] + (['x1', 'x1'] * k if k > 0 else ['y1', 'y1'] * (-k)) + (['y3', 'y3'] * k if k > 0 else ['x3', 'x3'] * (-k)) + ['x1']
    J = fastJ.J('l1.l1', W, 'u2.u2')
    res = C.certify_word(rules.enc(W), budget=3000)
    st = res['status']; pdn = None
    if st == 'UNRESOLVED':
        q = PDm.PD.from_halfword(C.halfword(rules.enc(res['reduced'])))
        b = q.simplify(random.Random(k), budget=500); pdn = b.n()
        assert PDm.replay(C.halfword(rules.enc(res['reduced'])), b.log) == pdn
        st = 'CERT_c_pd' if pdn == 0 else ('CERT_a_pd_TS24' if pdn <= 24 and vk.VK(C.halfword(rules.enc(W))) == {0: 1} else 'UNRESOLVED')
    out.append({'k': k, 'halfword': 's.l1.l1.' + '.'.join(W) + '.u2.u2', 'J': sorted(J.items()), 'status': st,
                'reduced': res['reduced'], 'pd_best': pdn})
    print(k, 'J =', J, st, 'reduced:', res['reduced'], 'pd', pdn)
json.dump(out, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/codex_line_check.json', 'w'), indent=1)
