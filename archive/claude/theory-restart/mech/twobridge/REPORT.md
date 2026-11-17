# Lens TWO-BRIDGE: report (partial; being completed)

Status: IN PROGRESS. Results so far (details to follow in the final version):

1. DATA NOTE. The labels p/q in run_3_45.jsonl are unreliable: kht++'s generator `-qNAME:p/q` uses integer division of the
   continued fraction entries, so only fractions with all-even entries get the intended inversion (e.g. "b7_2-2" is the
   figure-eight word again, "b11_4-1" is an unknot). I therefore parametrise by the half-diagram WORD:
   s.l1.(y0)^a1.(x1)^b1.(y0)^a2.(x1)^b2...u2 = word (a1,b1,a2,b2,...); knot = two-bridge knot C(a1,2b1,a2,2b2,...).
   135 distinct words in the file; trailing A-letters are Reidemeister-I moves.

2. RULE (DERIVED FROM DATA; fits all 143 records of run_3_45.jsonl and 8 new kht++ runs with 6 and 8 runs, 20..84 specials,
   predicted before the runs). Variables u = q^2 (same level), v = q^-6 delta (one level up). State (G, Gam), start (0,0):
       A-letter (axis crossing y0):      Gam <- v*Gam + 1 + (1 + u v) G
       B-letter (off-axis crossing x1):  G   <- u*G + Gam
   Specials (c - 24j, d - 4j) = q^(2k-2) delta^1 * G(u,v);  k = -4 G(1,-1) = -4 #{B-letters preceded by an odd number of A-letters};
   2j = G(-1,1) + G(1,-1). Mirror words (x0, y1): (c',d') -> (-c', 1-d').

3. PROVED (finite computation, scripts/lemma1.py): the decategorified recursion, i.e. the Kauffman bracket of the quotient
   diagram of any word satisfies  J_w = q^(4(#A-#B)) (1 + q^-6 (1-q^8) G_w(u=-q^2, v=q^-6)).

4. Consequences of the RULE (to be written): Newton polygon of G is a rectangle with all four edges fully occupied => TILT with
   step exactly 6 and OVERHANG.

Scripts: scripts/{load,parse,norm,rule,tl,decat,lemma1,check_new}.py ; kht++ runs: kht/run_*.log (8 runs so far).
