# JT_2 complexity: ROLE GADGET-A (EKT-pair amplification) -- working notes
17 Nov 2026. Written continuously; newest log entries at the bottom of LOG. Marks: PROVED / CHECKED(n) / CONJECTURE / GAP / FALSE.
Conventions: Kauffman bracket <D>, <k disjoint circles> = delta^(k-1), delta = -A^2 - A^-2, crossing = A<A-smoothing> + A^-1<B-smoothing>;
V_L(t) = (-A^3)^(-w) <D> at t = A^-4. Tangle bracket vector br(T) = (f,g): <T> = f [0] + g [inf], [0] = NW-NE,SW-SE arcs, [inf] = NW-SW,NE-SE
(EKT, Topology 42 (2003) Prop 2.2: <T^N> = delta f + g, <T^D> = f + delta g; br(1) = (A, A^-1)). Loops inside tangles count delta each.
Source text of EKT used: Codex work/attack/ekt.txt (pdf extraction; some symbols lost, re-derived by computation below).

## LOG
- 13:2x read STRESS P4, L2_complexity, bridge_complexity, depth_uniform_audit, CONTEXT, jt2/NOTE-from-integrator (Delta_L(q) = V_L(q^2)+q+q^-1;
  link jets are P-time; |N| <= 8(32n)^r for 2-comp links), Codex msg 13:14, EKT paper text. Read tools/kauffman.py, diagram.py.
  Plan: own engine (tl.py): PD with boundary + abstract boxes, bracket into TL basis, writhe/lk/Jones; then EKT reconstruction.
