"""Codex's countermodel B through the same matching test.
K(B) = r_1(0) + specials at (c+1, e), (c-1, e), (c+1, e-1), (c-1, e-1) in kht labels (offset, level); j = 0 (rational part = that of Q_0).
If B were Kh~ of the quotient tangle of (kappa,h), the Floer side would have some (m, D') with 16 - D' >= |m|, parity D' = m mod 2.
Question: for which (c, e, m, D') is the Szabo-direction matching feasible for n -> +-infinity?"""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/floer/scripts')
from ss_match import gens, maxmatch
L = 30
res = {}
for c in range(-40, 42, 2):          # c+1 must be even offsets: c odd?  offsets of specials are even -> c odd
    pass
feasible = {}
for Dp in range(0, 17, 2):
    m = 0
    ok = []
    for c1 in range(-41, 42, 2):       # c odd so that offsets c+-1 are even
        for e in range(-6, 8):
            sp = [(c1+1, e), (c1-1, e), (c1+1, e-1), (c1-1, e-1)]
            good = True
            for n in (L, -L):
                G = gens(sp, 0, 0, n)
                need2 = len(G) - (Dp + abs(n - m))
                need = need2 // 2
                if need < 0 or maxmatch(G, '+') < need: good = False
            if good: ok.append((c1, e))
    feasible[Dp] = ok
    print("D' =", Dp, ": feasible (c, top level e) count", len(ok), 'of', 41*14, '; e.g.', ok[:6])
