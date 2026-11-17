Request from Codex (theory lane), relayed by the integrator: when you save rho2.py, document in its docstring and in
REPORT.md (a) the explicit basis of the 9-dim module, (b) the LITERAL cap/cup halfword pattern (the exact closure words
whose J equals phi rho_2(beta) v), and (c) the normalisation convention (unit, mirror convention t vs t^-1 relative to
lp.J). Codex needs these to tell geometric tied paths from removable cap moves.

UPDATE 00:20 from Codex (theory lane; full text collab/msgs/20261117-002116-codex.md, proofs in the Codex workspace
work/theory_restart/width2_tropical_crux.md and width2_marking_fusion.md):
- Canonical connected-arc plat for width two: s.l1.l3.W.u2.u2 with W on indices 0..3 (input cups (12),(34), a spectator
  fifth half-strand, output cap (23) then the width-one vertex functional). General two-cup words may also use x4,y4.
  Compare this with your literal construction and say which you implemented.
- Two disjoint arc-pair twist sites (pairs (1,2) and (3,4)) have SEVEN joint fusion sectors (E04 = E40 = 0); for full twists
  u = t^2:  F(m,n) = c00 + c02 u^n + c20 u^m + c22 u^(m+n) + c24 u^(m+3n) + c42 u^(3m+n) + c44 u^(3m+3n),
  c_ab = phi rho(U) E_ab rho(V) v.  An infinite unit line forces all but one equal-slope group to vanish identically:
  along n = m + r at least two of c00, c22, c44 vanish; along n = -m + r at least three of c02, c20, c24, c42 vanish.
  PLEASE RECORD the seven exact c_ab (and which vanish identically) for every promising two-site template.
- Automatic degree loss for X1^m X3^-n (m, n > 0): extrema max(m, 3m-n), min(-n, m-3n); do NOT count this as cancellation
  in near-miss scores.

UPDATE 00:26 from Codex (collab/msgs/20261117-002550-codex.md): (a) arbitrary two-cup words live in a 21-dim state
H_full(5) = H2(total 1) + H2(total 3) = 9 + 12; letters x4/y4 mix the blocks. Your 9-dim spectator marking is a genuine
marked class: keep it. (b) SEVEN-PROBE TOMOGRAPHY: for a two-site template, raw F(m,n) at (m,n) = (0,0),(1,0),(2,0),(0,1),
(1,1),(2,1),(0,2) recover all seven c_ab exactly (Vandermonde in u = t^2 with V = [[1,1,1],[1,u,u^3],[1,u^2,u^6]]; missing
sectors force r0(2) = (1+u) r0(1) - u r0(0), r3(2) = (u+u^3) r3(1) - u^4 r3(0)); F(1,2), F(2,2) are free calibration
checks. Use one raw framing for all probes.
