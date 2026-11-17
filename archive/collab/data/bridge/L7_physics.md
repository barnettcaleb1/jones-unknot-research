# L7: Physics-inspired invariants and new homology theories (bridge lane)

Started 2026-11-17. Lens: F_K(x,q) / Z-hat, BPS q-series, 3d index, resurgence,
HOMFLY-PT/sl_N homology, DGR differentials, Witten's gauge approach, osp(1|2).
Status log is appended below as work proceeds (agent may be killed; notes are incremental).

## 0. Log
- [start] read CONTEXT.md.
- [~10 min] Context read. J(trefoil inversion) = t^7+t^4-t^3, J-1 = -(1+t^3)(1-t^4)  (tools/jq_tangle.py), parallel to V-1 = -(1-t)(1-t^3).
- Candidate bridges considered: (B1) permutation-orbifold / genon (twist defect) TQFT; (B2) odd/super categorification via osp(1|2);
  (B3) Lefschetz trace of h on Kh (REFUTED quickly: trefoil Kh^red exponents {1,3,4} vs J exponents {3,4,7}, no affine match);
  (B4) Z-hat/F_K of S^3_{1/n}(K) = Sigma_2(L_n); (B5) BPS/quiver positivity; (B6) resurgence.
- KEY OBSERVATION (B1): SU(2)_8 (t = zeta_10) = Z/2-gauging of the SWAP symmetry of Fib' x Fib' (D_6 extension of SU(2)_8 has rank 4, dims 1,phi,phi,phi^2).
  spin 1/2 = genon (twist defect) sigma_1, dim 2cos(pi/10) = D_Fib; spin 1 = tau x tau. Unfolding a swap defect = double branched cover.
  => predicted GENON IDENTITY: <L>_{t=zeta_10} ~ D^2 Z_Fib(Sigma_2(L)), and at tangle level [T](zeta_10) <-> Z_Fib(S^3 - N(K)) in V_Fib(T^2)=C^2.
  This would EXPLAIN MOMENT-CYC10 (J(zeta_10)=V_K(zeta_5)) and also J(i)=1 (k=2, Ising=gauged fermion parity),
  J(e^{i pi/3})=1 (k=4, SU(2)_4 = gauged charge conjugation of Z_3 = SU(3)_1; Lickorish-Millett), J(-1)=1 (k=0).
  Hand checks: Hopf (RP^3) and trefoil (L(3,1)) both give |<L>| = 3.078 = D^2|Z_Fib|. Numerical test next.
- [~25 min] NUMERICAL TEST (bridge/L7/genon_test.py, pretzel_test.py):  |V_L(e^{i pi/5})| = |Z_Fib(Sigma_2(L))| / |Z_Fib(S^3)|
  holds EXACTLY (1e-9) for ALL 2-bridge knots K(p/q), odd p<40 (lens spaces via SL(2,Z) rep), and ALL 336 three-strand
  pretzel knots |p_i|<=7 (Seifert covers via keychain surgery formula, calibrated on P(1,1,-1)=unknot).
  e.g. T(3,5)=P(-2,3,5): |V(zeta_10)| = phi^2 = |Z_Fib(Poincare sphere)|/|Z_Fib(S^3)|.  4_1: V(zeta_10)=0 = Z_Fib(L(5,2)).
  Literature: gauging the Z/2 swap of Fib x Fib gives SU(2)_8 (Cui-Galindo-Plavnik-Wang, CMP 2016, arXiv 1510.03475).
  Knot-theoretic consequence not yet found in literature (searching).
- [~55 min] Lit: Cui-Galindo-Plavnik-Wang CMP 348 (2016) arXiv 1510.03475 (gauging swap of Fib x Fib = SU(2)_8) CONFIRMED;
  Clark AGT 17 (2017) 2961-3005 arXiv 1509.03533 (osp(1|2n) colored = so(2n+1) colored, change of variables) => our
  "colour-2 sl2 at t = osp(1|2) at -t" is the n=1 case (KNOWN). Ebert arXiv 2210.09583: osp(1|2) invariant categorified by
  Khovanov with extra Z/4 grading. Costantino-Harper-Robertson-Young arXiv 2407.12181: Z-hat for osp(1|2) vs sl2.
  No source found stating the knot-level genon identity V_L(e^{i pi/5}) <-> Z_Fib(Sigma_2(L)) (3 searches). Treat as NEW pending deeper check.

==========================================================================================================
## 1. VERDICT (short)

Best bridge: **"Kauffman strands are Z/2 twist defects (genons)."**  At even levels the Jones polynomial is the
evaluation of a Z/2-gauged (orbifold) TQFT in which the spin-1/2 line is a branch locus. At level k=8 (t = e^{i pi/5})
the gauged theory is the SWAP orbifold of Fib x Fib (a published categorical fact), so the twist defect unfolds to the
double branched cover and

    |V_L(e^{i pi/5})| = |Z_Fib(Sigma_2(L))| / |Z_Fib(S^3)|          (GENON IDENTITY; exact on 2-bridge + 336 pretzels)

Applied to the quotient tangle of (K,h) this is MOMENT-CYC10 (J(zeta_10) = V_K(zeta_5)) with a conceptual proof, and
the same mechanism at k = 0, 2, 4 gives J(-1) = J(i) = J(e^{i pi/3}) = 1.  So ALL FIVE cyclotomic facts of the program
(Phi_1, Phi_2, Phi_4, Phi_6, Phi_10) are one phenomenon.  A classification shows k in {0,2,4,8} are the ONLY levels
where this mechanism forgets h; combined with the certified figure-eight inversion pair, J mod Phi_n is K-only for at
most finitely many n (rigorous).  So: physics explains the arithmetic completely, and certifies that the rest of Lemma Q
is genuinely h-dependent ("equivariant") information.  It does NOT by itself force J != unit (precise obstruction §5).

==========================================================================================================
## 2. DEFINITIONS (standard, with sources)

D1 (G-crossed extension, gauging).  For a modular category B with a braided action of G = Z/2 = <g>, a G-crossed
extension is B_G = B (+) B_g with g-twisted sector B_g ("twist defects"); its equivariantization (B_G)^G is a modular
category, "B with G gauged".  [Barkeshli-Bonderson-Cheng-Wang arXiv 1410.4540; CGPW arXiv 1510.03475.]
D2 (genon).  B = C x C with g = swap.  Twisted sector B_g is equivalent to C as a module category: objects sigma_a,
a in Irr(C), with (X x Y).sigma_a = sigma_{X Y a}.  dim sigma_a = d_a * D_C.  sigma_1 x sigma_1 = (+)_a  a x abar.
[Barkeshli-Jian-Qi PRB 87 (2013) 045130, arXiv 1208.4834; Barmeier-Schweigert arXiv 1004.1825 (2d modular functors
built from double covers).]
D3 (unfolding).  C x C on M with a swap defect along a link L (cut along a Seifert surface, glue layers crosswise) is the
C theory on the double branched cover Sigma_2(M,L).  A line X x Y in the quotient lifts to X on sheet 1, Y on sheet 2;
an arc colored a x abar with both ends on sigma_1 lifts to a closed loop colored a.
D4 (the levels).  SU(2)_k, q = e^{2 pi i/(k+2)}, Kauffman variable t = A^{-4} = q, spin-1/2 dim 2cos(pi/(k+2)).
  k = 0 mod 4: V_{k/2} is a boson; condensing it gives the D-type extension C_k (rank k/4+2; Kirillov-Ostrik 2002),
  and SU(2)_k = C_k with a Z/2 gauged; half-integer spins = twisted sector.  The Z/2 swaps the two halves of the split
  fixed point j = k/4 and fixes all other simples.
  k = 2 mod 4: V_{k/2} is a fermion; SU(2)_k = fermion-parity gauging of a spin TQFT (twisted sector = spin twist,
  not a branched cover).  k odd: V_{k/2} a semion, no Z/2 gauging.

DICTIONARY at k = 8 (t = e^{i pi/5}), from CGPW: SU(2)_8 = gauge_{Z/2}(Fib' x Fib', swap), Fib' with theta_tau =
e^{-4 pi i/5} (central charge check: c(SU(2)_8) = 12/5 = 2(-14/5) mod 8).
   spin 0,4  <-> (1 x 1)^{+-}          spin 1,3 <-> (tau x tau)^{+-}      spin 2 <-> tau x 1 (+) 1 x tau
   spin 1/2, 7/2 <-> sigma_1^{+-} (dim 2cos(pi/10) = D_Fib = 1.902)    spin 3/2, 5/2 <-> sigma_tau^{+-} (dim phi D_Fib)
   checks: theta_{spin1} = e^{2 pi i/5} = theta_tau'^2;  theta_{spin2} = e^{6 pi i/5} = theta_tau';  [5]/... dims match.
   Two-channel braid: sigma_1 x sigma_1 = (1x1) + (tau x tau)  <->  V_{1/2}^2 = V_0 + V_1 (TL!).  Kauffman R-eigenvalue
   ratio (channel 1 / channel 0) = -A^{-4} = -t = e^{6 pi i/5} at t = e^{i pi/5}; its square e^{2 pi i/5} =
   theta(tau x tau)/theta(1 x 1) = theta_tau'^2, as the ribbon relation requires for the genon braid.  Also -t = theta_tau'
   is exactly the twist factor driving <L_n> = A^n P + (-A^{-3})^n Q vs the Gauss factor in Z_Fib(S^3_{1/n}(K)).

==========================================================================================================
## 3. PROPOSITIONS

PROP A (genon identity, links).  For every link L in S^3,
      |V_L(e^{i pi/5})| = |Z_Fib(Sigma_2(L))| / |Z_Fib(S^3)|   ( = D_Fib |Z_Fib(Sigma_2 L)|, Z(S^3)=1/D, Z(S^1xS^2)=1 ).
 Proof sketch. (1) V_L(t) = unit * <L>/delta with spin-1/2 colouring of SU(2)_8.  (2) SU(2)_8 = gauged swap of Fib'xFib'
 with spin 1/2 = sigma_1 (CGPW).  (3) Link invariants of twisted-sector objects in an equivariantization = G-crossed
 evaluation on (S^3, Z/2-bundle branched along L) (charges only change signs/units on closed diagrams).
 (4) Unfolding (D3): the swap-crossed evaluation on (S^3, L) is D^2 Z_Fib(Sigma_2(L)) (normalisation fixed by unlinks:
 <O^n> = D^n, Sigma_2(O^n) = #^{n-1} S^1xS^2, Z = D^{n-2}).  Steps (3)-(4) are standard in the physics literature and in
 2d (Barmeier-Schweigert); a written 3d proof with signs is NOT in hand -> status: theorem-sketch + exact numerics.
 EVIDENCE (bridge/L7/genon_test.py, pretzel_test.py): equality to 1e-9 for every 2-bridge knot K(p/q), odd p < 40
 (lens spaces via the SL(2,Z) rep of Fib), and all 336 three-strand pretzel knots |p_i| <= 7 (Seifert covers, keychain
 surgery).  Examples: 3_1: phi = |Z(L(3,1))|/|Z(S^3)|;  4_1: 0 = Z_Fib(L(5,2));  T(3,5): phi^2 = Poincare sphere;
 P(-2,3,7): 2.148961 = Sigma(2,3,7).  Hopf: |<H>| = 3.078 = D^2|Z(RP^3)|.
 Consequence (JC): if V_K = 1 then Sigma_2(K) is a Z-homology sphere M with |Z_Fib(M)| = |Z_Fib(S^3)|
 ("Fibonacci-invisible"), on top of Arf = 0 (k=2) and the Z/3 condition (k=4, Lickorish-Millett).

PROP B (tangle form; strongly invertible knots).  Let T be the quotient tangle of (K,h), E(K) = Sigma_2(B^3,T).
 The 4-point sphere with four genons double covers the torus dE(K), and Hom(1, sigma_1^{x4}) = V_Fib(T^2) = C^2 = the TL
 space span{b, c}.  Under this fixed isomorphism, [T](t=e^{i pi/5}) = Z_Fib(E(K)), the Fib vector of the knot exterior.
 Hence x(zeta_10), y(zeta_10) depend on K only; in the meridian-colour basis Z_Fib(E(K)) = (1, <K,tau>) and the arc k
 coloured spin 1 = tau x tau lifts to K coloured tau:  J(zeta_10) = <K,tau>/d_tau = V_K(zeta_5)  == MOMENT-CYC10
 (checked on the trefoil inversion: J = t^7+t^4-t^3, J(zeta_10) = V_{3_1}(zeta_10^2) exactly).
 Same mechanism, other levels:
   k = 4 (t = e^{i pi/3}): SU(2)_4 = gauged charge conjugation of Z/3 = SU(3)_1 (conformal embedding; = metaplectic
     SO(3)_2, Goldschmidt-Jones 1989).  Arc k = Z/3-anyon loop K in S^3: abelian, 0-framed => J(e^{i pi/3}) = 1.
   k = 2 (t = i): Ising = gauged fermion parity of sVec; K in S^3 has unique spin structure => J(i) = 1 (Arf-type).
   k = 0 (t = -1): trivial theory => J(-1) = 1.     (t = 1 classical.)
 => the program's J-1 divisible by Phi_1 Phi_2^2 Phi_4 Phi_6 and J = V_K(t^2) mod Phi_10 are exactly the genon levels.

PROP C (classification + finiteness; the obstruction).
 (i) Among SU(2)_k, the Z/2 gauging forgets the involution (bilayer swap, or pointed C) only for k in {0,2,4,8}.
   Proof: k = 0 mod 4: the Z/2 on C_k fixes k/4 simples and swaps ONE pair.  A swap of DxD fixes r = rank D simples and
   swaps r(r-1)/2 pairs => r = 2, k/4 = 2, k = 8 (dims 1,phi,phi,phi^2 force D = Fib-type).  C_k pointed iff all
   [2j+1] = 1 or split => k <= 4.  k = 2 mod 4: twisted sector is a spin-structure twist; trivial only for C = sVec (k=2).
   k odd: no gauging.  (Exceptional extensions E6 at k=10, E8 at k=28 are not simple-current gaugings: spin 1/2 confined.)
 (ii) RIGOROUS finiteness: the team's certified figure-eight pair (K,h_1),(K,h_2) has J_1 != J_2 (M3 = -180 vs +180).
   Phi_n | (J_1 - J_2) for only finitely many n (degree bound), so "J mod Phi_n is determined by K" holds for at most
   finitely many n.  No TQFT/level mechanism yields K-only information at infinitely many roots of unity.
   This is the root-of-unity twin of FT-DEEP (no finite jet at t=-1 detects).
 => STOP looking for further cyclotomic congruences: the remaining content of Lemma Q is h-dependent.

==========================================================================================================
## 4. q-GENERIC READING (heuristic, explains OSP-SYMBOL/OSP-DEFECT/TH-COLOR3)
 SU(2) = SO(3) with its Z/2 (centre one-form symmetry) "ungauged"; the spin-1/2 line is the boundary of the Z/2 surface,
 i.e. a Z/2 twist defect for the SO(3) theory.  SO(3)/colour 2 = osp(1|2) at -q (Clark 2017, n=1).  So
   J(K,h) = SO(3) (vector) Wilson line on k in the Z/2-twisted background along the axis
          = an h-twisted ("equivariant") spin-1 coloured Jones polynomial of K.
 Checks: (a) OSP-DEFECT "colour-two root braid = superflip, mixed monodromy = parity": the parity IS the Z/2 twist.
 (b) TH-COLOR3: swap inversion of L # rL folds to J = J_3(L) (spin-1 coloured Jones of L): the twisted background
 trivialises when h is a swap of two copies -- the q-generic shadow of the k = 8 bilayer swap.
 Reformulation: Lemma Q = "the h-twisted SO(3) Wilson loop of (K,h) is a monomial only for the unknot" -- an
 equivariant-TQFT detection statement; the categorified version is Watson's kappa (Adv. Math. 313, 2017).

## 5. OBSTRUCTIONS (why this lens cannot directly force J != unit)
 O1. Fixed colours: (1/2,1/2,m) admissible only for m <= 1, so J is ONE member; volume-conjecture/resurgence needs colours
     scaling with level (the orbifold family <Theta; a,a,2m>), perturbative q->1 is FT-DEEP.
 O2. Positivity/BPS integrality live in categorifications or all-colour generating functions (quivers, F_K); a single
     specialisation has signed cancellation by design (JC is exactly a cancellation problem).
 O3. Prop C: the root-of-unity TQFT information that is K-only is exhausted by 5 cyclotomic classes.
 O4. Lefschetz idea "J = graded trace of h on Kh(K)" REFUTED: trefoil Kh^red q-exponents {1,3,4} (in t) vs J exponents
     {3,4,7}: no affine matching.

## 6. SUGGESTED NEXT STEPS (cheap)
 S1. Write the 3d unfolding proof with signs (Prop A) -- likely a short paper-level note; check novelty with an expert
     search (Turaev HQFT / permutation-equivariant RT literature).
 S2. Arborescent gates at cube roots (a(omega)a(omega^2)=1): t = omega and t = e^{i pi/3} are abelian (pointed) levels,
     so those gates should be classical invariants (Goeritz / linking forms of double branched covers of the pieces),
     hence Mayer-Vietoris compatible.  Test: compare a(omega) of boxes with det/Goeritz data of box closures.
 S3. Categorify Prop B: Ebert's Z/4-graded Khovanov (osp(1|2)) on the quotient tangle + Lobb-Watson/Sano equivariant
     Khovanov: look for a Smith-type localization whose Euler characteristic is J (Watson's kappa).

## 7. BRIDGE LIST (as reported)
 B1 [best, developed] Genon/permutation-orbifold: SU(2)_8 = gauged swap of Fib'xFib' => |V_L(e^{i pi/5})| = Fib invariant
    of Sigma_2(L); tangle form = MOMENT-CYC10; k in {0,2,4,8} = all cyclotomic facts; finiteness via figure-eight pair.
    Status: categorical input KNOWN (CGPW 2016, BJQ 2013); knot-level identity NEW as far as found; explanation NEW.
 B2 q-generic: J = h-twisted SO(3)(=osp(1|2) at -q, Clark 2017) Wilson loop; Lemma Q = equivariant-TQFT detection.
    PARTLY_KNOWN (osp<->so3 known; twisted-defect reading new framing). Mostly reformulation.
 B3 Z-hat/F_K: Sigma_2(L_n) = S^3_{1/n}(K) so V(L_n)(zeta_10) = Fib (SO(3)_3) WRT of S^3_{1/n}(K) = radial limit of
    Z-hat; osp(1|2) Z-hat exists (Costantino-Harper-Robertson-Young 2407.12181). UNCLEAR leverage (single root).
 B4 Categorified: Watson kappa (Euler char <-> J), Lobb-Watson refinement, Ebert Z/4-graded osp Khovanov, Smith
    localization (Lipshitz-Sarkar, Stoffregen-Zhang). KNOWN detection; decategorification is the open cancellation.
 B5 REFUTED: J = graded Lefschetz trace of h on Kh(K) (trefoil exponents).
 B6 Arborescent gates at abelian levels are classical (Goeritz/linking of double covers of pieces) => Mayer-Vietoris.
    NEW conjecture, untested.

## 8. FILES
 /Users/calebbarnett/jones-lanes/theory-restart/bridge/L7_physics.md          (this file)
 /Users/calebbarnett/jones-lanes/theory-restart/bridge/L7/genon_test.py       (2-bridge test; run: python3 genon_test.py)
 /Users/calebbarnett/jones-lanes/theory-restart/bridge/L7/pretzel_test.py     (pretzel/Seifert test)
- [~70 min] Notes complete. No outward actions taken.
- [~72 min] Prop A also exact on all 173 two-component 2-bridge LINKS (even p<=40), 0 mismatches. (k=12 run is data only, not a Sigma_2 control.)
