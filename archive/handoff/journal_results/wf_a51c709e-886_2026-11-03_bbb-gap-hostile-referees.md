# BBB gap: three hostile referees (parity, t = -1 conventions, construction)

- Workflow: wf_a51c709e-886 (bbb-gap-adversarial-check-wf_a51c709e-886.js)
- Session: structure chat (genus-two lane, ~/jones-lanes/g2-proof)
- Launched (script written): 2026-11-03 15:24 local; journal last written: 2026-11-03 15:28 local
- Agents started: refute:parity, refute:tminus1, refute:construction
- Results extracted here: refute:parity, refute:construction, refute:tminus1
- Context: Launched 3 Nov 15:24 in the structure chat. ~/jones-lanes/g2-proof/BBB-GAP.md (readable by Codex) records that three hostile referees found no refutation and folds in their corrections; the referees' own verdicts and objections exist only in the journal. Scripts: g2-proof/bbb-gap/check-parity/sec7.py, check-tminus1/{brunn,chk}.py.
- Provenance: contemporaneous agent outputs recorded in the workflow journal (runtime state, not copied). Text below is verbatim except formatting (JSON fields rendered as markdown), em dashes replaced by ' - ', email addresses redacted, and home-directory paths shortened to ~ (session scratchpad roots to <scratch>). These are internal AI agent outputs, not external review; statuses are as the agent stated them at the time and may be superseded by later board entries.


## Agent: refute:parity


### verdict

survives

### strongest_objection

I could not break Lemma 1 or the way section 3 uses it. (a) |W_i| = |P(Delta_i)| holds by definition: Section 3 sets W_i = +-k, where Delta_i is the k-punctured disk bounded by alpha_i and beta_i. Lemma 3.1 (W_i = k_{i+1} - k_i) is plain covering theory, because alpha_i and beta_i form a simple closed curve, so its exponent sum is +-(number of punctures it encloses). The global sign convention does not matter, since only the parity is used. (b) Every disk Delta_i is embedded and exists for every consecutive pair. beta_i has no interior points on alpha, alpha_i avoids p1 and p2, and the curve stays off the boundary of D, so Jordan-Schoenflies gives an embedded disk. No puncture can be counted twice. If p3 sits inside, it counts consistently in both W_i and P. (c) The parity condition (Section 4) is imposed on exactly these disks, the full disk sequence Delta_1..Delta_{m-1}. (d) Cor 6.8 deduces M_{f(Phi)Gamma} != M_Gamma only from the sums of |coefficients|: "By Proposition 6.7 we can assume iota != iota. The result follows." Section 3 reads this correctly. (e) The paper's own data agrees with Lemma 1. In Fig 3.1(b), M(-1) = 6 = m. In Section 7, M_{Phi Gamma}(-1) = 8 = m and M_Gamma(-1) = -20 = -m, with one value of eps_i (-1)^{k_i} across all 20 terms. The non-parity M_Phi gives M(-1) = 2 with m = 8. The only problems are minor. The note's citation is weak: it credits |W_i| = |P| to Fig 4.1 and Lemma 4.2, but it is the Section 3 definition. The note's m is the number of points of whatever representative is used, not necessarily iota. That gap closes itself: |M(-1)| <= iota <= m, so a parity representative is automatically in minimal position. This hurts the note's section 5 more than its section 3. Prop 5.1 cannot be the failing input, because parity alone forces sum = iota. So listing Prop 5.1 as a possible failure point is redundant, and the real gap is narrower than the note says.

### location

BBB-GAP.md section 1 proof of Lemma 1 (citation for |W_i|=|P(Delta_i)|); section 5 bullet listing Prop 5.1 as a candidate failure. Paper: bbb.txt lines 265-299 (definition of W_i, Lemma 3.1), 350-379 (parity condition, Lemma 4.2), 1182-1204 (Cor 6.8 proof).

### fix

In Lemma 1, cite the Section 3 definition (W_i = +-k, where Delta_i is the k-punctured disk bounded by alpha_i and beta_i) together with Lemma 3.1, not Fig 4.1 or Lemma 4.2. Add one line: parity on any transverse representative with m points gives m = |M(-1)| <= iota <= m, so that representative is minimal and m = iota without Prop 5.1. Then in section 5, drop Prop 5.1 from the list of possible failures. The contradiction then lies in the parity claims of Prop 6.7 (Lemmas 6.3-6.6), its Furthermore clause, or the proper-product criterion for Gamma_1. Optionally cite the paper's own Section 7 example as a consistency check: M_Gamma(-1) = -20 = -m.

### checked

I read the full note, then paper Sections 2-4 (definitions of the Moody polynomial and the signs, the disk sequence and W_i, Lemma 3.1, Cor 3.2, Fig 4.1 caption, the parity condition, Lemma 4.2 and its proof), Section 5 (proper product, Prop 5.1), Section 6 (Lemmas 6.1-6.6, Prop 6.7 including Furthermore, Cor 6.8 proof, Thm 6.9) and Section 7. I checked the embeddedness and multiplicity questions directly from the definitions. Script ~/jones-lanes/g2-proof/bbb-gap/check-parity/sec7.py tests Lemma 1 on the paper's four explicit unsimplified Moody polynomials: all three parity cases have a single sign at t=-1 with |M(-1)|=m, and the non-parity case does not. Not checked (outside this lens): Lemma 2, the Phi0 computation, and whether Phi = Phi'*Gamma_1 is really a proper product.


## Agent: refute:construction


### verdict

survives

### strongest_objection

The note never checks the paper's actual definition of a proper product for Phi = Phi'*Gamma_1. Condition 2 is geometric: it asks whether Gamma_I and Gamma_F meet beta', the beta-component of the innermost p4-only disk of Phi'. Condition 1 asks for no bigon-forming polygons. Both are certified only by the shortcut paragraph in the proof of Thm 6.9: "only trigons and rectangles can occur, trigons are resolved by isotopy, rectangles are excluded by alternation", and a freely reduced juxtaposition gives Condition 2. With the figures missing, no geometric check is possible. The objection fails, though, because the note puts exactly that criterion in its list of statements that could be false. The construction meets the criterion as the paper states it. Phi0 lies in [K4,K4] and is nontrivial, so it is not a power of y1, and for m larger than its reduced length, y1^m Phi0 y1^-m reduces to y1^(m+a) u y1^(b-m). Gamma_1^-1 ends in y2, so Phi' is reduced, and Phi' ends in y1^-1 while Gamma_1 starts with y2^-1, so Phi'Gamma_1 is reduced. The paper adds no cyclic-reduction condition, no condition on Phi', and no condition on the 4-disks at the hypothesis level. The hypotheses of Lemma 6.3 (Phi in K4, Phi = Psi*Gamma_1 proper), Prop 6.7 (Phi in B4) and Cor 6.8 (Phi in K4, iota > 0, since Phi is a nontrivial Brunnian conjugate and so pseudo-Anosov) all hold. Remaining damage is cosmetic. (1) The note says "exponent sum zero"; the property actually needed is "not a power of y1", which exponent sum zero plus nontriviality implies. (2) Prop 5.1 does not belong in the list of suspects. Parity on any representative forces no cancellation, so the count m equals sum|coeffs|, which is at most iota, so m = iota. Lemma 1 plus Lemma 2 therefore contradict Prop 6.7's three claims directly. Also, f(Phi) is not in K5, so Prop 6.7's "proper product in B5" lies outside the definition and outside Prop 5.1's hypothesis. That is a misapplication inside Prop 6.7, not a separate failure. (3) The claim "the reduction in Thm 6.9 is repairable" is conditional on the shortcut criterion, which belongs to that same reduction.

### location

BBB-GAP.md sections 4 and 5. Paper: proper-product definition (bbb.txt about lines 564-585), Prop 5.1 (line 599, hypothesis Phi in K_n), Prop 6.7 statement (f(Phi)*Gamma proper in B5), Thm 6.9 shortcut paragraph (about lines 1233-1247).

### fix

State that Phi'*Gamma_1 is proper only by the criterion in the Thm 6.9 proof, which the paper asserts without proof, and that the geometric Conditions 1 and 2 are unverified. Replace "exponent sum zero" with "not a power of y1". Drop Prop 5.1 as an independent suspect, since parity alone forces the count to equal iota. Add that Prop 6.7 applies the proper-product notion to f(Phi), which is not in K5. Recast section 5: either the shortcut criterion is false, or Prop 6.7 (through Lemmas 6.2 to 6.6, or the Furthermore clause) is false.

### checked

Read the full note, paper Section 5 (definition, Fig 5.6 caption, Prop 5.1) and Section 6 (Lemmas 6.1 to 6.6, Gamma_1, Prop 6.7 with its proof, Cor 6.8, Thm 6.9 including the free-basis paragraph), plus the earlier reading. Reran phi0_check.py with python3 -I and the output matches: rho4 and rho5 of Phi0 are I at t=-1 and not I at t=2 and t=3. Checked A14, A24, A34 and the Burau block and its inverse. Checked Delta3^4 = (s1s2)^6, so Phi0 = [delta^-2, b] lies in [K4,K4]. Checked that Phi0 is Brunnian and in K4 (K4 is normal). Checked free reduction of Phi' and of Phi'Gamma_1 at both junctions. Checked the hypothesis lists of Lemma 6.3, Prop 6.7 and Cor 6.8. No reading found that keeps the chain from applying to this Phi.


## Agent: refute:tminus1


### verdict

survives

### strongest_objection

Lemma 2 as literally stated (M_{YX}(-1) = M_X(-1)) is false in general. The paper fixes M only up to a power of t (first crossing gets t^0), so the honest statement is M_{YX}(-1) = ±M_X(-1). Section 3 of the note already uses ±, so this is cosmetic. A second point the note skips: the paper defines M_Phi on the class of the boundary loop of a neighborhood of (beta*_3)Phi, not of the arc itself. Each crossing q_i then appears twice with opposite signs and exponents k_i and k_i ± 1, so the loop pairing is (1 - t^{±1}) M_arc. The only denominator is 1 - t^{±1}, which is 2 at t = -1, not 0. The equivariant intersection pairing of H_1(D~_n,{p~*}) with the lift of alpha (a lf cycle ending at punctures) is Z[t^{±1}]-sesquilinear with no denominators. If rho(Y) = I at t = -1, then (Y - 1)H lies in (t+1)H, X preserves (t+1)H, and the pairing lands in (t+1)Z[t^{±1}]. This works for both right- and left-action conventions, since the condition is invariant under transpose, inverse and t -> 1/t. I found no way to break Lemma 2 or the Phi0 facts.

### location

BBB-GAP.md section 2 (Lemma 2 statement, missing ±) and the proof's appeal to "proof of Thm 2.3". Paper bbb.txt lines ~226-231 (M_Phi well defined on the homology class of the loop) and lines 245-255 (Thm 2.3).

### fix

Restate Lemma 2 as M_{YX}(-1) = ±M_X(-1). Add one line: the paper's class is the boundary loop, the loop pairing equals (1 - t^{±1}) times the arc polynomial, and so M_arc(-1) = M_loop(-1)/2 is determined by the class mod (t+1). In section 4, say explicitly that Phi0 is pure (that is needed for strand-forgetting to be a homomorphism). It holds because (s1 s2)^6 = Delta_3^4 and the A_ij are pure.

### checked

I wrote my own exact Fraction code (check-tminus1/chk.py) and checked braid relations for every matrix set. The A_ij words are A14=[3,2,1,1,-2,-3], A24=[3,2,2,-3] and A34=[3,3], and Phi0 has length 112. I ran four conventions: unreduced block [[1-t,t],[1,0]] and its transpose, and reduced Burau and its transpose. In all four, in B4 and in B5 (stabilized), rho(Phi0) = I at t = -1 and rho(Phi0) != I at t = 2 and at t = 1/3. (s1 s2)^6 = I at t = -1 everywhere, and b = [[A14,A24],A34] is not I at t = -1. Brunnian check (check-tminus1/brunn.py): I used the Artin action on F_4 with free reduction, with images of length 2.4M to 9.5M letters. It confirms Phi0 is nontrivial and pure. For each i = 1..4, setting x_i = 1 gives the identity automorphism of F_3, so every strand deletion is trivial (Artin is faithful on B_3). I also checked that the parity definition makes |W_i| = |P(Delta_i)| by the definition of W_i (lines ~279, 355), so the sign at t = -1 is constant. The 2-chain explanation also holds: (s1 s2)^6 = T_c^2, where c surrounds 3 points, which lifts to a separating twist.
