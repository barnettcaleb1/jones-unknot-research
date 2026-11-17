# Projective graph complexity equals classical crossing number

[Claim index](../CLAIM_INDEX.md) · [Evidence policy](../EVIDENCE_POLICY.md)

**Record type:** early handoff

**Status as recorded:**

```text
D/N
```

**Interpretation:** Historical status only; check later corrections. Internal review is not external specialist review.

## Statement and recorded scope

```text
MID-31  D/N  Projective graph complexity equals classical crossing number
------------------------------------------------------------------------
In Boyle--Spyropoulos arXiv2609.40122v1 conventions, alpha(G) is the minimum
edge deletion making the embedded RP2 graph local; beta=e-alpha;
beta_Re(K) minimizes the integral-Jones-sector checkerboard beta.
For any nullhomologous projective K with lift component Ktilde,
 beta_Re(K)>=c_S3(Ktilde).
For classical K placed in a ball in RP3, beta_Re(K)=c_S3(K).
Proof chooses canonical sheet parity from an antisymmetric region index on
the lift; self-crossing edges are positive. Positive edges form a local
subgraph, so beta>=self crossings>=c(Ktilde). A Seifert-state parity
calculation identifies this shading with the Re sector; it is not arbitrary.
The disk diagram gives the opposite inequality for local K.
Consequences: the source Conj1.1(2) local specialization span(V)>=beta_Re
is false, e.g. T(3,4) has V=t3+t5-t8 (span5) while Alexander span6 forces
c>=6. This is an internally audited candidate refutation of an AUXILIARY
conjecture, not externally reviewed or a Jones counterexample.
Earlier global beta-compression optimism is superseded: beta_Re on local
knots is exactly crossing complexity, unbounded on infinite fixed-Jones
families. Another source induction defect: an essential projective triangle
has beta2 and EVERY single-edge deletion leaves beta2, so the asserted
beta-decreasing edge need not exist. This gap alone did not refute its
small-beta classifications; the later crossing identity gives the sharper
span countertest.
Proofs: work/research31/projective_crossing_identity.txt,
projective_local_crossing_audit.txt, projective_crossing_hostile_audit.txt;
verify_torus_countertest.py. Earlier fixed-diagram dual-systole formula and
finite-template construction: work/research30/projective_dual_systole_audit.txt,
projective_templates.txt. No claim about beta_Im or arbitrary links.

------------------------------------------------------------------------
```

## Provenance

[Source record](../../archive/outputs/claude-handoff/RESULT_LEDGER.json). The source wording is retained; consult the chronology for later restrictions or withdrawals.

## Identified supporting artifacts

- [projective_dual_systole_audit.txt](../../archive/work/research30/projective_dual_systole_audit.txt)
- [projective_templates.txt](../../archive/work/research30/projective_templates.txt)
- [projective_crossing_hostile_audit.txt](../../archive/work/research31/projective_crossing_hostile_audit.txt)
- [projective_crossing_identity.txt](../../archive/work/research31/projective_crossing_identity.txt)
- [projective_local_crossing_audit.txt](../../archive/work/research31/projective_local_crossing_audit.txt)
- [verify_torus_countertest.py](../../archive/work/research31/verify_torus_countertest.py)

These links identify recorded evidence; they are not a claim that the logical dependency list is complete.
