#!/usr/bin/env python3
"""Independent check that the simplified word in the .kht header is the tangle whose BN~ is stored:
(1) my Kauffman bracket of the 1-3 tangle: <T> = alpha_b [Q_0] + alpha_c [Q_inf];  T(inf) = T.u1 must be an unknot (unit bracket);
(2) graded Euler characteristic of the stored b-generators must be +- q^s * alpha_b (A -> q via q = -A^-2)."""
import json, sys, time
from morse import parse, Trace, bracket, padd, pmul, DELTA, pstr
from words import header_word, names
N = json.load(open('N_from_chains.json'))
MB = (3, 2, 1, 0); MC = (1, 0, 3, 2)
def to_q(pol):
    """Kauffman polynomial in A -> polynomial in q up to a unit: A^e -> (-q)^(-(e-e0)/2)"""
    e0 = min(pol)
    out = {}
    for e, c in pol.items():
        assert (e - e0) % 2 == 0
        k = (e - e0) // 2
        out[-k] = out.get(-k, 0) + c * (-1) ** (k % 2)
    return {k: v for k, v in out.items() if v}
def normalise(p):
    m = min(p); lead = p[m]
    s = 1 if lead > 0 else -1
    return tuple(sorted((k - m, v * s) for k, v in p.items()))
bad = 0; res = {}
t0 = time.time()
for nm in names():
    if nm not in N: continue
    ev = parse(header_word(nm))
    st = bracket(ev, 1)
    assert set(st) <= {MB, MC}, st.keys()
    ab = st.get(MB, {}); ac = st.get(MC, {})
    tinf = padd(ab, pmul(ac, DELTA))
    unit_inf = (len(tinf) == 1 and abs(list(tinf.values())[0]) == 1)
    chi = {}
    for h, q in N[nm]:
        chi[q] = chi.get(q, 0) + (-1) ** (h % 2)
    chi = {k: v for k, v in chi.items() if v}
    # chi in q; alpha_b in q (up to unit).  q-exponents of alpha_b come in steps of 1 (A^2 steps); chi has all q even or all odd
    aq = to_q(ab)
    ok = normalise(aq) == normalise(chi)
    res[nm] = dict(unit_inf=unit_inf, chi_ok=ok, nterms=len(aq))
    if not (ok and unit_inf):
        bad += 1
        print('FAIL', nm, 'T(inf) unit:', unit_inf, 'chi ok:', ok)
        print('   alpha_b(q):', normalise(aq)); print('   chi N    :', normalise(chi))
print('checked', len(res), 'failures', bad, 'time %.1fs' % (time.time() - t0))
