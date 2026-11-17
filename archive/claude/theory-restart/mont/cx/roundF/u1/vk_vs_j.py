"""vk_vs_j.py -- 'V_K of the translated K agrees with engineC2's J-side data where comparable' (BRIEF N1, N2):
for every certified record with its V_K (certifier's PD-code bracket, ident3 normalisation) and J (lp.J of the halfword,
which equals engineC2's plat2.J by validate_s2), check
  (i)  a_2(K) = -V_K''(1)/6  equals  -J''(-1)/24 = lp.a2(J)          (N1: J''(-1) = -24 a_2(K));
  (ii) J(t) - V_K(t^2) == 0 mod Phi_10(t) = t^4 - t^3 + t^2 - t + 1   (N2, MOMENT-CYC10).
usage: vk_vs_j.py FILE.jsonl.gz [...]"""
import sys, gzip, json
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont'); import lp
from fractions import Fraction
PHI10 = [1, -1, 1, -1, 1]          # t^4 - t^3 + t^2 - t + 1, highest first
def a2_of_V(V):
    return Fraction(-sum(c * e * (e - 1) for e, c in V.items()), 6)
def rem_phi10(P):
    """remainder of a Laurent polynomial {e: c} modulo Phi_10 (t is a unit mod Phi_10, so shift to a polynomial)"""
    if not P: return []
    lo = min(P); poly = {e - lo: c for e, c in P.items()}
    deg = max(poly); coeffs = [poly.get(d, 0) for d in range(deg, -1, -1)]
    while len(coeffs) >= 5:
        c = coeffs[0]
        for i in range(5): coeffs[i] -= c * PHI10[i]
        coeffs.pop(0)
    return [c for c in coeffs if c] and coeffs
def check(rec):
    V = rec.get('V_K'); J = rec.get('J')
    if V is None or J is None or isinstance(J, str): return None
    V = {int(e): c for e, c in (V.items() if isinstance(V, dict) else V)}
    J = {int(e): c for e, c in J}
    a2V = a2_of_V(V); a2J = Fraction(lp.a2(J)).limit_denominator(1000)
    P = dict(J)
    for e, c in V.items(): P[2 * e] = P.get(2 * e, 0) - c
    P = {e: c for e, c in P.items() if c}
    r = rem_phi10(P)
    return (a2V == a2J, not r)
if __name__ == '__main__':
    from collections import Counter
    for f in sys.argv[1:]:
        cnt = Counter(); bad = []
        with gzip.open(f, 'rt') as fh:
            for line in fh:
                rec = json.loads(line); r = check(rec)
                cnt[r] += 1
                if r is not None and not all(r) and len(bad) < 5: bad.append((rec['w'], r))
        print(f, dict(cnt), 'examples of failure:', bad)
