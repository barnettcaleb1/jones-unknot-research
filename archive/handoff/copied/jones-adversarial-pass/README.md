# Adversarial pass on the Jones unknot collab (3 November 2026)

Review of the Claude/Astra bridge chat, plus the verification, design and referee rounds behind it.

- `MESSAGE-to-bridge.md` is the paste-ready message for the bridge chat.
- `workflow-results.json` holds every agent's full report: 5 verifiers, the process audit, 3 designers and 6 referees.
- `work/` holds the scripts and outputs. The ones referred to in the message:
  - `work/verify-sep/` (separating-curve criterion)
  - `work/peer-checks/bbb_phi0.py` (Phi0 under Burau)
  - `work/peer-checks/thmA.py` (Theorem A check)
  - `work/referee-logic-criterion-prove/` (the word that breaks the Schottky bound)

## Verdicts

| Item | Verdict |
|---|---|
| Plat chain: a genus-two kernel gives 3-bridge knots with V = 1 | Holds once fixed (cite Ichihara-Saito, conjugate by tau_c^N). It is a second proof of Kasahara 2008 + Ito. |
| Separating-curve criterion | Holds, using the Hermitian form. Orthogonality is impossible, so collisions are the only kernel source. |
| Process audit | 34 outputs, 0 progress, all of them correct. |
| Design: CH^4 complex reflections, Haken form H_n | Dead (both referees). |
| Design: half-twist "foreign line" criterion | Dead (both referees). It is the existing collision certificate. |
| Design: Torelli Schottky inequality | Dead: false on an explicit word. The filling-triple fact survives numerically. |
| Peer claim: BBB Burau_4 proof has a gap | Phi0 computation reproduced, and the t = -1 logic is sound. The reading of Prop 6.7 is still unconfirmed. |
| Peer claim: Theorem A | Consistent: |N(zeta8)| was odd on 3000 random words. |
