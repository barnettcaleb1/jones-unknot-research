# cert/ : a sound certifier for the covering knot K of a halfword

Claude (cx lane), 17 Nov 2026.  Python: `tools/venv/bin/python` or system `python3` (pure Python; sympy only for one
optional cross-check in refs.alex_ref).  mitm_cert.py imports engineB's mitm.py/rho2.py read-only.
Status of every claim below: see REPORT.md (PROVED / CHECKED(n) / CONJECTURE / GAP).

## Usage

```
certify.py [--json] [--tietze-budget S] [--rep-budget S] [--no-hit-file] HALFWORD ...
replay.py CERT.json ...            # independent re-check of saved certificates
```
```python
import sys; sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert')
import certify, replay
status, cert = certify.certify('s.l1.l1.x2.x1.x1.x1.y3.y3.x1.u2.u2')
# status in CERTIFIED_UNKNOT / CERTIFIED_NONTRIVIAL / COUNTEREXAMPLE / UNRESOLVED / NOT_A_KNOT
for c in cert['certificates']: print(replay.check(c))
```
`cert` also carries `crossings`, `V_K` (exact, from the PD code), `Delta` (exact; computed only when the representation
search runs, else None), the Tietze statistics and notes.
Every certificate in `cert['certificates']` has already been accepted by `replay.check` (a rejected certificate is
dropped and noted; that would indicate a bug).

## Results at a glance (details and marks in REPORT.md)

* Steps 1-2 validated: PD code V_K == ident3 V_K exactly and Fox-calculus Alexander == alex.py on 650/650 halfwords;
  checker's Wirtinger presentation == PD-based one literally (300/300); |Hom(pi, G)| for S3, S4, A5 agree with the
  Artin-action plat presentation (320/320).
* Suite (a), known unknots: 2721/2721 CERTIFIED_UNKNOT by replayed Tietze certificates (J = 1 configurations with
  <= 24 crossings, engineB's top/bottom re-hit families up to 32 crossings, Codex's family up to 86 crossings).
* Suite (b), known nontrivial knots (blind mode, Tietze forced): 1944/1944 CERTIFIED_NONTRIVIAL, ZERO false unknot
  certificates; stress test 26,201 long randomised attempts, zero; 6,528 transplanted certificates all rejected.
* Suite (c): 26-32 crossings median 4 ms (unknots) / 24 ms (nontrivial); ~64 crossings 18 ms / 0.58 s.
* Beyond the suites: engineB's complete (7,7) width-two screen re-run (mitm_cert.py): all 685,033 V_K = 1 survivors
  ('presumed unknots') are CERTIFIED unknots (568,895 jones24, 116,138 Tietze); all 113,348 depth-8 top/bottom re-hit
  closures are CERTIFIED unknots.  The region claim still needs geometric bottom deduplication (REPORT section 9).

## Certification standard (used exactly)

| status | only by |
|---|---|
| CERTIFIED_UNKNOT | (a) `jones24`: an actual diagram of K with <= 24 crossings and V_K = 1 (Tuzun-Sikora: the Jones unknot conjecture holds up to 24 crossings); (b) `tietze`: the Wirtinger presentation of pi_1(S^3 - K) reduced by replayed Tietze moves to `<a \| >` (then K is trivial by Dehn's lemma); (c) `unknot0`: a crossing-free one-component diagram |
| CERTIFIED_NONTRIVIAL | `rep`: an explicit homomorphism pi_1 -> S_d (permutation images of ALL Wirtinger generators), every relator checked, two images that do not commute |
| COUNTEREXAMPLE | CERTIFIED_NONTRIVIAL and V_K = 1: `collab/HIT-<HHMM>.md` is written immediately (BRIEF section 5) |
| UNRESOLVED | everything else; retained, never called an unknot |

V_K != 1 and Delta != 1 are recorded but are NOT used as nontriviality certificates (task standard).

**Routing.**  PD code -> V_K (Delta only when the representation search runs).  If V_K = 1: Tietze route (default budget 30 s), then `jones24` if the Morse diagram
has <= 24 crossings, then the representation search (a hit there is a COUNTEREXAMPLE).  If V_K != 1: representation
search only (the Tietze route cannot succeed on a nontrivial knot); `blind=True` forces the Tietze attempt anyway (default
budget 3 s) and is what the soundness suite (b) uses, so that the simplifier is exercised on nontrivial knots.

## Conventions

* **K.** The knot of the Morse word `full = alex.symmetrize(alex.parse(halfword))` (tools/alex.py; the same word that
  tools/kauffman.py sweeps).  Start with one cap (strands 0, 1); `('l'|'r', i)` cap inserting strands i, i+1;
  `('u', i)` cup joining strands i, i+1; `('x'|'y', i)` crossing of strands i, i+1, with slots TL, TR (before) and BL, BR
  (after); the strands are TL-BR and TR-BL; `x`: TL-BR is over; `y`: TR-BL is over.
* **Planar picture.** The word is drawn upwards (earlier letters lower), positions left to right; counterclockwise slot
  order TL, TR, BR, BL.  In this picture kauffman.py's smoothing weights are the standard ones, so V_K from our PD code
  equals the ident3-normalised V_K exactly (not up to mirror).  alex.writhe is the writhe of the downward (mirror)
  picture, which is why engineB/kcert.py flips its sign.
* **PD code** (diagram.py).  Edges 0..2n-1 consecutively along the orientation of alex.diagram (start: crossing 0, over
  strand, going along the word); crossing k = the k-th crossing of the Morse word; tuple (a,b,c,d) read counterclockwise
  from the incoming under edge a (c = a+1); sign +1 iff the over strand runs d -> b; signs stored explicitly.
  `check_pd`: every label twice, a -> a+1 and over_in -> over_in + 1, and faces = n + 2 (planar rotation system).
* **Jones.** Kauffman bracket with A-smoothing (a,b)(c,d), B-smoothing (a,d)(b,c), <O> = 1, delta = -A^2 - A^-2;
  V_K(t) = (-A^3)^-w <D>, t = A^-4.  V(right-handed trefoil) = t + t^3 - t^4.
* **Wirtinger presentation** (wirtinger.py; independently re-implemented in replay.py from alex.diagram).  Generator
  k+1 = the arc that begins at crossing k (as its outgoing under edge); relator of crossing k (over arc o, incoming
  under arc i, sign s): `x_{k+1}^-1 x_o^s x_i x_o^-s`.  Words are tuples of nonzero ints (+g, -g).
* **Plat presentation** (wirtinger.py, validation only): Morse sweep with the exact Artin action; cap -> generator g on
  strands (g, g^-1); `x`: (w_i, w_i+1) -> (w_i w_i+1 w_i^-1, w_i); `y`: (w_i, w_i+1) -> (w_i+1, w_i+1^-1 w_i w_i+1);
  cup -> relator w_i w_i+1.
* **Tietze moves** (tietze.py; replayed by replay.py).  After every move the presentation is put in canonical form: each
  relator freely and cyclically reduced and replaced by the lexicographically least rotation of itself or its inverse;
  empty and duplicate relators dropped; relators sorted by (length, word).  Moves (indices into the canonical list):
  `('elim', g, j)` g occurs exactly once in relator j = g^e u (cyclically), substitute g := u^-1 (e = 1) or u (e = -1),
  delete relator j and g; `('mult', i, j, e, kj, ki)` i != j, r_i := reduce(rot(r_j^e, kj) . rot(r_i, ki));
  `('nielsen', x, a, d, side)` x != a, substitute x -> x a^d ('R') or a^d x ('L').
* **Representation certificates.** `{'kind': 'rep', 'halfword', 'degree': d, 'images': {gen: perm}, 'noncommuting':
  [g, h], 'group'}`; perm = tuple p of length d, p[i] = image of i, product (p*q)[i] = p[q[i]].  Target groups:
  Aff(F_p) acting on F_p (metabelian, from roots lam != 1 of Delta mod p), S4, A5, S5, PSL(2,7) (on P^1(F_7)), A6, S6,
  PSL(2,11), SL(2,5), SL(2,7) (on F_p^2 - 0), A7, S7, PSL(2,13).

## Soundness argument, per output type

**`tietze` (CERTIFIED_UNKNOT, route b).**
1. *The starting presentation presents pi_1(S^3 - K).*  The checker builds it from alex.diagram, i.e. from the Morse
   diagram D of K (the definition of K).  For a connected oriented diagram, the Wirtinger presentation (arcs as
   generators, one relation x_out = x_o^{+-1} x_in x_o^{-+1} per crossing, exponent determined by the crossing sign
   through one fixed rule) presents pi_1 of the complement (Wirtinger; e.g. Rolfsen 3.D, Burde-Zieschang 3.B).  If our
   fixed rule is the opposite of the textbook one, our presentation is the textbook Wirtinger presentation of the
   reflected diagram (same arcs, every sign flipped), which is a diagram of the mirror image of K; its complement is
   homeomorphic to that of K.  So in either case the group is pi_1(S^3 - K) up to isomorphism.  What has to be right
   is the arc structure and the per-crossing signs; these are validated three independent ways (REPORT section 1-2, 6):
   Fox calculus reproduces alex.py's Alexander polynomial (CHECKED 650/650); the checker's presentation is literally
   identical to the one built from the independently coded PD code (CHECKED 300/300), whose V_K equals kauffman.py's
   exactly (CHECKED 650/650); and |Hom(pi, G)| for G = S3, S4, A5 agrees with the plat presentation built by the exact
   Artin action, a different construction with no arcs and no signs (CHECKED 320 knots x 3 groups, REPORT section 2).
2. *Every move preserves the group.*  `elim` is the inverse of the Tietze move "add a generator g with defining relation
   g = word"; the checker verifies that g occurs exactly once in the chosen relator, so the substituted word does not
   contain g.  `mult` replaces r_i by (conjugate of r_j^{+-1}) . (conjugate of r_i) with j != i, which keeps the normal
   closure (r_i is recovered from the new relator and r_j).  `nielsen` applies an elementary Nielsen automorphism of the
   free group to all relators (= add y = x a^d, then eliminate x); an automorphism carries the normal closure of R onto
   that of its image.  Canonicalisation only conjugates, inverts, or deletes trivial / repeated relators.
3. *End state.*  `<a | >` presents Z.  A knot whose group is infinite cyclic is the unknot (Dehn's lemma,
   Papakyriakopoulos).
4. *Independence.*  replay.py imports nothing from the certifier; it re-derives the presentation from the halfword, uses
   a different least-rotation algorithm, and re-checks each move's precondition, so a bug in tietze.py can only cause a
   rejection, never an acceptance.

**`jones24` (CERTIFIED_UNKNOT, route a).**  The Morse diagram of K (alex.diagram) is an actual diagram of K; the checker
counts its crossings (<= 24 required) and computes V_K with the project bracket (kauffman.bracket, ident3
normalisation).  V_K = 1 means the bracket is a unit, independent of the normalisation.  A knot with a diagram of <= 24
crossings has crossing number <= 24, and Tuzun-Sikora verified that every nontrivial such knot has V != 1.  The bracket
is validated against the independent PD-code bracket (CHECKED 650/650, exact).

**`unknot0`.**  A crossing-free one-component Morse diagram is a single circle in the plane.

**`rep` (CERTIFIED_NONTRIVIAL).**  Permutations assigned to all Wirtinger generators that satisfy every relator define a
homomorphism pi_1 -> S_d (von Dyck).  Two images that do not commute make the image, hence pi_1, nonabelian; pi_1 of the
unknot is Z.  (This needs only that the presentation presents a group isomorphic to pi_1, point 1 above.)

**COUNTEREXAMPLE.**  A `rep` certificate together with V_K = 1.  Before the HIT file is written, the certificate has
passed replay.check; a second independent check (another implementation, e.g. SnapPy) must follow (BRIEF section 5).

**What is not claimed.**  UNRESOLVED means nothing.  V_K != 1 is not used as a certificate.  The certifier does not
decide knot types beyond trivial / nontrivial.  Reidemeister-move certificates (route c beyond crossing-free diagrams)
are not implemented: the Tietze route already certifies every unknot in the suites (REPORT section 5-6).

## Files

| file | role |
|---|---|
| certify.py | API `certify(halfword) -> (status, certificate)` and CLI |
| diagram.py | Morse word -> oriented PD code, planarity check, bracket, V_K, Fox/Alexander |
| wirtinger.py | Wirtinger (from PD) and plat (Artin action) presentations, abelianisation |
| tietze.py | simplifier recording replayable moves |
| reps.py | representation search (affine, S_n, A_n, PSL(2,p), SL(2,p)) |
| replay.py | INDEPENDENT checker for all certificate kinds |
| refs.py | project reference implementations (ident3 V_K, alex.py Alexander) and random halfwords |
| validate_pd.py, validate_group.py | validation of steps 1-2 |
| gen_sets.py, gen_families.py, suites.py | test sets and validation suites |
| stress_tietze.py | soundness stress test: long Tietze budgets on nontrivial knots (two-bridge, Alexander-trivial) |
| bulk_cert.py | bulk certification of families of expected unknots (lean path, full certify on failure, unresolved retained) |
| mitm_cert.py | re-runs engineB's exhaustive width-two screen (mitm.py imported read-only) and certifies every survivor |
| run_queue.sh, run_queue3.sh | the sequential run queues used for the final validation |
| out/ | logs, summaries (`*.summary.json`) and full per-knot certificates (`*.jsonl`, `*.jsonl.gz`) |
| extract/ | NOT part of this certifier: a parallel lane's own folder (its own REPORT.md); left untouched |
