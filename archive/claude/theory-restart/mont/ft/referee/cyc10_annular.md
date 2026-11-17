# Referee notes, LENS A (annular part) of MOMENT-CYC10
(Claude referee, 16 Nov 2026. Theorem: J_(K,h)(t) = V_K(t^2) mod Phi_10(t), preferred normalisation.)
Proof under review: Codex work/theory_restart/degree3_cyclotomic_comparison.md (Sections 1-4 = annular part; 5-6 touched only where Lens A needs them).
Scratch code: ./cyc10A/

Status legend: OK (re-derived) / REPAIRABLE / GAP / FATAL / CHECKED(n)

## 0. Skeleton (filled in as I go)
- A1 BMW parameters (r_-,d_-), (r_+,d_+), eigenvalues, skein relation, differences (1): OK (sec. 2)
- A2 Turaev annulus generation, only spanning used: OK (sec. 4)
- A3 generator values L_n^-, L_n^+, difference (6): OK (sec. 3)
- A4 framing bookkeeping (A_n framing n-1, double lift T(n,2), theta_U, Q^(5(n-1))): OK (sec. 3), one wording repair (sec. 6)
- A5 generators -> products (axis scalar composition vs split cover blocks): OK (sec. 5)
- Global annular statement E_-(D) = E_+(D) at primitive 5th roots: CHECKED(260 random annular diagrams) (sec. 5)
- Verdict: STANDS for Sections 1-4 (annular part), minor repairs only (sec. 6-7)

## 1. Conventions fixed before checking (re-derived from the code, not from the proof text)
- fs.bracket_vector / kauffman.bracket: letter x at position i = A*(keep) + A^-1*(cup-cap) = sigma_A ("type x");
  y = sigma_A^-1. symmetrize(): an off-axis x_s lifts to TWO x-crossings of K; x0 lifts to ONE x-crossing on the axis.
  quotient_word(): off-axis x_s = 2-cabled crossing of 4 x's (colour 2 x colour 2); x0 = sigma_0 sigma_1 sigma_1 sigma_0 of x's
  with the axis at position 0 = mixed full twist T of type x. So every object below is "type x" on both sides. CONSISTENT.
- lp.J_raw maps A^e -> t^(e/4) (t = A^{+4} for J), while VK maps A^e -> t^(-e/4) (t = A^{-4}, standard Jones).
  (The task text says "t = A^-4 conventions of lp.py"; literally lp.J uses t = A^4 for the quotient bracket variable.
   This is only a naming point, but it is exactly what makes the proof's conventions line up; see below.)
- With t = A^4 and Q := -t^-1 = -A^-4:
  colour-2 type-x crossing (KL formula lambda^{22}_c): ch0 A^-8 = Q^2, ch2 -A^-4 = Q, ch4 A^4 = -Q^-1  == proof's B_orig. OK
  mixed type-x full twist: ch1 A^-8 = Q^2, ch3 A^4 = -Q^-1  == proof's T (FT gauge). OK
  cover: J = V_K(t^2) needs K's bracket variable a with a^-4 = t^2 = A^8; the choice a = iA^-2 (a^2 = Q) makes the folded
  type-x pair sigma_a (x) sigma_a have eigenvalues Q (9-dim), -Q^-1 (6-dim), Q^-3 (1-dim) == proof's cover braid,
  and B = sigma_a has Q^{1/2} (triplet), -Q^{-3/2} (singlet) == proof's B. OK
  (With a = A^-2 instead, the folded z would be -(Q-Q^-1): wrong sign; the choice a^2 = Q is forced, and is harmless
   since V_K does not see the 4th-root choice; framing units only.)
- CHIRALITY: the opposite identification (J vs V_K(t^-2)) needs a^2 = +-t: a^2 = -t = Q^-1 flips z, and a^2 = t keeps z and d
  (mod Phi5) but gives r = -Q^-3 != Q^-2 at zeta (checked: Hopf/A_2 values then differ, 1 vs -1). The proof's choice is the one
  consistent with the code conventions. Claude's numerics (V_K(t^2) holds, V_K(t^-2) fails) agree. OK

## 2. A1 BMW parameters, eigenvalues, skein relation, differences (1)   -> OK (CHECKED, exact)
Script cyc10A/bmw_ops.py (20/20 PASS), built ONLY from the Kauffman-bracket TL rep on (C^2)^{x4} (faithful generically):
- original colour 2 = 2-cables with f2 = 1 - e/delta; type-x cabled crossing X = s2 s1 s3 s2 (exact quotient_word pattern),
  B_o = (f2xf2) X, E_o = (f2xf2) e2 e1 e3 e2 (f2xf2). Exact TL identities with Q = -A^-4:
  E_o^2 = d_- E_o, d_- = 1-Q-Q^-1;  B_o E_o = E_o B_o = Q^2 E_o (so r_- = Q^-2);  B_o - B_o^-1 = (Q-Q^-1)(1 - E_o);
  minimal polynomial (B-Q^2)(B-Q)(B+Q^-1), channel ranks 1,3,5.  The relation is an identity in TL_4 with only the f2
  denominator delta, hence valid at every A with delta != 0, in particular at A^4 = t = -zeta5^-1 (primitive 10th root).
- cover: sheetwise pair sigma_13 sigma_24 at variable a, E_W = e_13 e_24: E_W^2 = (a^2+a^-2)^2 E_W = d_+ E_W,
  B_W - B_W^-1 = (a^2-a^-2)(1-E_W) (pure TL algebra, uses only e^2 = delta e), B_W E_W = a^-6 E_W = Q^-3 E_W (r_+ = Q^3),
  min. poly (B-Q)(B+Q^-1)(B-Q^-3), ranks 9,6,1 (the two 3-dim SO(4) summands share -Q^-1: no exception). With a^2 = Q.
- (1): r_+ - r_- = Q^-2(Q^5-1), d_+ - d_- = Q^-2 Phi5(Q), and d = 1+(r-r^-1)/(Q-Q^-1) on both sides: exact.
- Kink factors: partial trace of a Dubrovnik B is r = (contraction eigenvalue)^-1. Original type-x colour-2 kink = A^8 = Q^-2 = r_-;
  cover: each of the two lifted kinks is a type-x fundamental kink -a^3 = theta_U, product a^6 = Q^3 = r_+. OK.
  (Local orientation-preserving diffeo away from the axis preserves crossing and kink type; h maps a kink in the other
   half to the reflected-and-switched picture, same type.)

## 3. A3/A4 generator values and framing   -> OK (CHECKED n = 1..5 by an INDEPENDENT route)
Script cyc10A/annulus_eval.py: a Morse-word Kauffman-bracket evaluator with kauffman.py's letter conventions.
- E_-(A_n) computed from the DEFINITION: axis drawn as the belt (the braid axis U0 is isotopic in the complement of the
  closed braid to a meridian belt around the bundle at one level: U0 ~ its 0-longitude = meridian of V), colour-2 strands
  as 2-cables with f2 on every cable pair, divided by Delta_1. This does NOT use the proof's closure-of-T^n identification.
  Result: E_-(A_n) = r_-^(n-1) L_n^- exactly for n = 1..5. Hence the marked identification "colour-2 component of
  closure(T^n) = A_n with framing shift n-1" is right, INCLUDING handedness (A_3 built from y-crossings gives a different
  value) and the zero-longitude marking. Belt built from x or from y crossings gives the same value (as it must).
- E_+(A_n) = bracket of the lift = closure of (s1...s_{n-1})^2 with blackboard framing (the annular projection lifts to the
  annular projection under w -> w^2, so blackboard = pulled-back framing). Result: = r_+^(n-1) L_n^+ exactly, n = 1..5.
  This confirms theta_U = -Q^{3/2}, the n-2 curl correction (n=1: one negative curl; n=2: raw Hopf), and that
  theta_U^(n-2) Tr_q(B^n) = Q^{3(n-1)} Tr_q(T_fold^n). Only even powers of a occur, so E_+ is a Laurent polynomial in Q
  and is independent of the choice of Q^{1/2} (T_fold = theta_U^-1 B is invariant under a -> -a).
- (6) L_n^- - L_n^+ = Q^-3n (Q^5n - 1) - Q^-2 Phi5(Q)(-Q^-1)^n: exact algebra (re-derived by hand), vanishes at zeta5 for all n.
  Framing ratio r_+^(n-1)/r_-^(n-1) = Q^{5(n-1)}. So E_-(A_n)(zeta) = E_+(A_n)(zeta) for every n >= 1.
- Cleaner equivalent form (referee remark): with C_n := 0-framed colour-2 component of closure(T^n) = r^-(n-1) A_n in either
  skein, E_-(C_n) = L_n^- and E_+(C_n) = L_n^+; the two framing computations of the proof (meridian lemma for T_fold and the
  n-2 curl count) are mutually consistent: E_+(C_n) = r_+^-(n-1) r_+^(n-1) L_n^+ = Tr_q(T_fold^n).

## 4. A2 Turaev annular generation   -> OK (only spanning is used, and used correctly)
- The unoriented framed Dubrovnik skein of annulus x I is spanned, over Z[z, r^{+-1}, d], by monomials (stacked products)
  in A_n, n >= 1, plus the empty diagram. Proof shape (re-derived): induction on (crossings, bad crossings) with
  B = B^-1 + z(1 - E) (MULTIPLIES by z, never divides), curls cost r^{+-1}, contractible loops cost d; a descending diagram
  is a stacked product of single-component descending curves; a descending curve of winding n != 0 (traversed in the
  positive direction, legal since curves are unoriented) is a framed A_n, winding 0 is a framed contractible loop.
  Spanning survives specialisation (right-exactness of (x)_R C), so it holds in the specialised skein S_zeta.
- Hidden-assumption check: depending on the descending convention the representatives may be the y-family A_n^y rather
  than A_n = A_n^x; either family spans (A_n^y = A_n^x + fewer-crossing terms, induction). This matters only because the
  generator VALUES are family-specific (A_3^y has a different E_- value; sec. 3): the proof computes both sides on the
  same x-family, so it is consistent. Unoriented => no separate negative-winding generators needed.
- What makes "same skein" true: at Q = zeta (primitive 5th root) the parameter triples coincide,
  z = zeta - zeta^-1, r_- = zeta^-2 = zeta^3 = r_+, d_- = d_+ (Phi5(zeta) = 0), and both are consistent with
  d = 1 + (r - r^-1)/z. E_- (resp. E_+) kills the Dubrovnik relations with its own triple (sec. 2: exact TL identities,
  regular at A^4 = -zeta^-1 since delta != 0 there; the lift of a local relation is the product of two bracket relations
  in disjoint balls). Hence both are linear functionals on the SAME S_zeta; equality on a spanning set suffices.
  No freeness, no idempotent basis, no division by a quantum integer. Correct.
- Note: at t a primitive 10th root of unity the KL colour-2 theory is honestly semisimple ([k] != 0 for k <= 9);
  the "integral FT lattice" remark in Section 1 is not needed for Sections 1-4 (it matters only near t = -1).

## 5. A5 generators -> products; global check   -> OK
- Original: annulus x I = complement of the axis with I PARALLEL to the axis; stacking = composition of (1,1)-tangles on
  the colour-1 strand; End(V_1) = TL_1 = scalars at every A (no Schur lemma needed, no division by Delta_1).
  So z(D1 D2) = z(D1) z(D2). Concentric = stacked (isotopy in annulus x I).
- Cover: the level plane between two stacked factors is a sphere meeting the axis in 2 points; its branched lift is a
  sphere; lifted links split; bracket with <empty> = 1 is multiplicative. (Normalisation matters: with <O> = 1 one would
  get an extra delta; the proof uses absolute brackets, consistent with E_+(A_1) = delta.)
- CHECKED exactly (cyc10A/random_annular.py): both functionals multiplicative on concentric products (4 cases each),
  closure of e_1 = contractible loop gives d_- and d_+, A_1 x loop factorises.
- GLOBAL CHECK of the conclusion of Sections 2-4, independent of the proof's argument: for 260 random annular diagrams
  (closures of random words in s_j^{+-1} and colour-2 cup-caps e_j on 2-4 strands, so including winding-deficient and
  non-braid diagrams), E_-(D) computed from the definition (belt axis, f2-cables) and E_+(D) = bracket of the branched lift
  (closure of the word repeated twice) agree EXACTLY modulo Phi5(Q): 260/260; they differ as Laurent polynomials in
  260/260 (so the test is not vacuous), and both are integral Laurent polynomials in Q in 40/40 audited cases.

## 6. Issues found (all minor / presentational; none affects the annular argument)
M1 (chirality bookkeeping is implicit). The proof never writes the relation between the quotient bracket variable and t,
   nor that B_orig and B are the SAME letter. This is exactly where J = V(t^2) vs J = V(t^-2) is decided (with the wrong
   chirality, a^2 = t, the folded theory still has the right z and the right d mod Phi5 but r = -Q^-3 != Q^-2 at zeta, so
   the comparison fails, matching Claude's 173/300 failures for V(t^-2)). Repair (one paragraph): "an off-axis quotient
   crossing and its two lifts are the same letter (local orientation-preserving diffeomorphism; symmetrize() and
   quotient_word() copy the letter); lp.J uses t = A^4 for the quotient bracket; the cover bracket variable is a with
   a^2 = Q = -A^-4 (forced by matching z); hence the cover Jones variable is a^-4 = t^2."
   Side remark on the task statement: lp.J maps A^e -> t^(e/4) (t = A^{+4}), whereas VK maps A^e -> t^(-e/4); so "t = A^-4
   conventions of lp.py" is accurate for V_K but not for J. In a uniform t = A^-4 convention for both, the theorem reads
   J(t) = V_K(t^-2) mod Phi10. The theorem must be stated with J = lp.J as it is.
M2 (axis framing). The annular functional E_- presumes a ZERO-framed colour-1 axis. A theta diagram whose axis cycle has
   framing f contributes (-A^3)^f on the original side and nothing on the cover side, so the RAW equality claimed at the
   end of Section 5 holds only for the 0-framed axis (the natural diagrams have no axis self-crossings, so f = 0; the
   preferred normalisation is unaffected either way). Section 6's assertion "F in Q(Q) by the annular formulas" already
   presupposes this. Repair: one sentence fixing the axis cycle to be 0-framed in F.
M3 (family). State that the spanning family and the evaluated family are the same x-family (sec. 4); a reader who takes
   Turaev's descending representatives as the y-family must convert first.
M4 (wording). "Ordinary Jones variable Q^-2" for the cover vs "t = q^2" in the FT gauge for the quotient look like
   opposite conventions; they are consistent only because of M1. Worth one line.

## 7. Verdict for Lens A
Sections 1-4 (and the annular inputs used in Section 5) STAND. Every Lens-A step was re-derived and the decisive ones
recomputed by routes that do not use the proof's own derivations: Dubrovnik structure as exact TL identities; generator
values from the definitions (belt axis with f2-cables; lifted torus links); and the end statement E_- = E_+ at primitive
fifth roots on 260 random annular diagrams. No fatal or serious defect. Repairs M1-M4 are expository. Not covered here:
the vertex marking / bending scalar / P_0 identification of Section 5 and the unit argument of Section 6 (other lenses);
I only checked (7) at TL level (T has eigenvalues Q^2 (mult 2), -Q^-1 (mult 4) on the f2-image; (T+Q^-1)/(Q^2+Q^-1) is an
idempotent of rank dim V_1) and that the reduced closure of T^n equals L_n^- (n = 1..5).
Scripts: cyc10A/bmw_ops.py, annulus_eval.py, random_annular.py, loops_check.py, closureT_and_P1.py, integrality.py.
