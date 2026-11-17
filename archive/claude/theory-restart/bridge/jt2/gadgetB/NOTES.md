# JT_2 / GADGET-B: planar tensor networks and Holant view
17 Nov 2026. Role GADGET-B. Written continuously; newest log entries at the bottom of LOG.
Marks: PROVED / CHECKED(n) / CONJECTURE / GAP / FALSE.
Code: this folder (tl.py = exact TL / bracket engine). Python: tools/venv/bin/python.

Conventions (fixed for the whole note):
- R = Z[A^+-1], delta = -A^2 - A^-2, <O> = 1 (reduced bracket for closed diagrams), t = A^-4.
- Crossing tensor sigma = A * (A-smoothing) + A^-1 * (B-smoothing).
- A 2n-ended tangle T has bracket br(T) in the free R-module TL(2n) with basis the Catalan(n)
  crossingless matchings of 2n boundary points (numbered 0..2n-1 counterclockwise).
- Unreduced convention for tangles: each closed loop gives a factor delta (so a closed link has
  <L>_unreduced = delta * <L>).

Read (13:35): CONTEXT, STRESS P4, L2_complexity, bridge_complexity, depth_uniform_audit, lit/NOTES.md, both
integrator notes, Codex jt2_{difference_algebra, clause_gate_scope, root_gates, scope_audit}.md. To avoid duplicating:
Codex already has: constant-braid finite-image lemma, 2-adic no-rational-Hadamard lemma, carrier criterion h_E = 0,
serial TL2 obstruction, projector component-cost theorem, root gates (t^3-1) | F_L, Phi_4 for |N|>2, Phi_6 for
counts 1,2,3, fixed jets of links in P, 2-component depth bound |N| <= 8(32n)^r.

## LOG
