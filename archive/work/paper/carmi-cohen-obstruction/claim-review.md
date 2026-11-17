# Carmi–Cohen obstruction: exact claim and dependency review

Prepared 3 November 2026 for the second manuscript. This review checks the scope of the obstruction, not a new counterexample search. Source: Avishy Carmi and Eliahu Cohen, *On trivial Jones–Vassiliev polynomials*, arXiv:2606.22410v1, 21 June 2026, as preserved in `work/carmi-cohen.txt`. All page numbers below are the paper's printed page numbers. This is a version-specific review; no claim about the current version history is needed.

The primary statements and their proofs were read directly, particularly Sections 5.1–5.3, Theorem 5.10, Proposition 5.12, and the beginning of the proof of Theorem 6.8. The mathematical scope agrees with EARLY-01 in `work/handoff/early-ledger.txt`, LATE-03 in `work/handoff/late-ledger.txt`, and `work/research36/descent_audit.txt`. The root agent is independently deriving and checking the recurrence and explicit polynomials for the manuscript appendix; this review does not report a new execution of those computations.

## 1. Exact target

The counterexample is to the following universal consequence of the paper's machine package:

> For the crossing-flip family of a fixed pre-planting knot diagram with $n$ crossings, the entire ordinary residual twist cube of the proposed clasping machine has Jones–Vassiliev degree at most $3n+13$, independently of its odd residual length $L\geq3$.

This is the conjunction of Proposition 5.12's claimed geometric realization, Theorem 5.6's signed-cube compression, and Lemma 5.8's residual initialization. It is not the statement of the paper's main theorem. It does not require the host to have Jones polynomial $1$, or even to satisfy any positive-layer vanishing condition. The minimal trefoil therefore falls within the universal scope claimed for this intermediate package.

The exact notation is

\[
p=x-x^{-1},\qquad x^2=px+1,\qquad
V=A(p)+xB(p),\qquad
f_q(V)=(a_q,b_q)^T,
\]

where $A=\sum a_qp^q$, $B=\sum b_qp^q$, and $\deg_p V=\max(\deg A,\deg B)$. The expression is unique in the free $\mathbb Z[p]$-module with basis $1,x$. Thus $b_{51}=-1$ means that the vector $f_{51}$ is nonzero; it should not be written $f_{51}=-1$.

## 2. Source dependency map

| Source | Assumptions and asserted conclusion | Role in the contradiction |
|---|---|---|
| Corollary 3.7, p. 13 | An oriented diagram with $n$ crossings and $\ell$ components has $\deg_p V\leq3n+\ell-1$. | Supplies the ordinary cap for the pre-planting host. This statement is not contradicted. |
| Definition 5.4, p. 24 | The residual block has odd $L\geq3$; the full signed machine cube has four clasp coordinates and $L$ residual coordinates. The seed crossing is smoothed before planting. | Specifies the claimed construction and domain. |
| Section 5.1.1, p. 25 | $B_{\rm host}$ refers to the pre-planting shadow, with the seed still counted. The asserted effective threshold is $\widehat B=B_{\rm host}+11$, independent of $L$ and the exterior state. | For a three-crossing knot host, $B_{\rm host}=9$, $\widehat B=20$. |
| Section 5.1.3, pp. 26–27 | $G_q(Q)$ denotes vanishing of $f_q$ at every vertex of $Q$. Conditions (C1)–(C3) impose controlled and exceptional vanishing and anti-parallel clasp relations; (C4) identifies the double-smoothed original primed-sign slice with the ordinary residual twist cube. | The quantifier is over the entire residual cube, including its extreme all-positive state. |
| Proposition 5.12, pp. 39–40 | For a machine planted at a seed crossing and every odd $L>1$, the asserted local facts hold relative to the exterior. (G0) supplies anti-parallel residual relations; (G1)–(G3) supply (C1)–(C3), with overhead $11$; (G4) supplies (C4). The proposition and its proof assert uniformity in exterior states. | Purports to provide the hypotheses needed to apply the subsequent conditional conclusions to the trefoil host. No Jones-unit or host-vanishing assumption appears here. |
| Theorem 5.6, pp. 30–31 | Assuming (C1)–(C3) uniformly over a fixed-shadow exterior family, $G_q(Q_M(\mathcal H))$ holds for every $q>\widehat B(\mathcal H)$, independently of $L$. | The claimed signed-state cap is $20$. Its descending proof uses Lemma 5.5 and an ambient finite cap that may depend on $L$. |
| Lemma 5.8, pp. 31–33 | Assuming (C1)–(C4) uniformly, $G_r(Q_\rho(\mathcal H))$ holds for every $r>\widehat B(\mathcal H)+2$. | The claimed entire residual-cube cap is $22$. No anchor vanishing or inequality $L>\widehat B+2$ is assumed. |
| Definition 5.9 and (H1), p. 34; Theorem 5.10, p. 35 | The two selected residual sign states cancel to effective single crossings. Theorem 5.10 additionally assumes $L>\widehat B+2$, the anchor condition, and $f_r(K)=0$ for $1\leq r\leq\widehat B+2$. | These are later hypotheses. The trefoil obstruction does not assert that the trefoil meets the host-vanishing assumption of Theorem 5.10. |

The cap in Remark 5.7, p. 31, is different: a full machine has a legitimate ambient estimate $A_M\leq B_{\rm host}+3L+11$. Theorem 5.6 claims to descend from that $L$-dependent ambient cap to the $L$-independent cap $\widehat B$. Confusing those two caps would misstate the target.

## 3. The paired-skein step is valid

Fix the primed clasp signs at $y'_0=-$, $y'_{L+1}=+$, as in Lemma 5.8, and write $V_{st}$ for the Jones polynomial with the two unprimed clasp coordinates equal to $s,t\in\{-,0,+\}$. In the source convention,

\[
x^{-2}V_+-x^2V_-=pV_0.
\]

Applying this identity first at one clasp and then at the other gives

\[
V_{-+}=x^{-4}V_{++}-p^2V_{00}-px^2V_{0-},
\qquad
V_{+-}=x^4V_{--}+px^2V_{0-}.
\]

Adding them proves the paper's equation (29):

\[
V_{-+}+V_{+-}=x^{-4}V_{++}+x^4V_{--}-p^2V_{00}.
\tag{*}
\]

The degree shift used in Lemma 5.8 is also correct. Indeed,

\[
x(A+xB)=B+x(A+pB),\qquad
x^{-1}(A+xB)=(B-pA)+xA,
\]

so multiplication by either $x^4$ or $x^{-4}$ increases $\deg_p$ by at most four. If all four signed states in (*) have degree at most $\widehat B$, then (*) gives

\[
\deg_p(p^2V_{00})\leq\widehat B+4,
\qquad
\deg_p V_{00}\leq\widehat B+2.
\]

Condition (C4) identifies $V_{00}$ with the ordinary residual twist. Consequently this part of the implication needs no correction from $+2$ to $+4$. It also shows exactly what the obstruction forces: for the stated residual family, a simultaneous uniform cap on the four signed states and the claimed ordinary-double-smoothing identification cannot hold. The argument does not by itself identify which geometric assertion or earlier conditional step fails.

## 4. Manuscript-ready statement and proof of the incompatibility

**Proposition (failure of the universal residual bound).** For the minimal three-crossing trefoil host, the universal residual bound obtained by combining Proposition 5.12, Theorem 5.6, and Lemma 5.8 of Carmi–Cohen, arXiv:2606.22410v1, is false. More precisely, the ordinary anti-parallel residual twist family at the marked seed has Jones–Vassiliev degree $2L+5$ for every positive odd $L$. Thus no bound of the form $B_{\rm host}+\kappa+2$, with $\kappa$ independent of $L$, can hold for all its residual states.

**Proof.** Use the marked anti-parallel seed in the three-crossing trefoil diagram used for the twist construction, with the source's Jones convention. The ordinary residual family $K_L$ has

\[
V_1=x^2+x^6-x^8,
\qquad H=-x-x^5,
\]

where $H$ is the fixed oriented smoothing. The oriented skein relation, followed by a Reidemeister-II cancellation in the switched diagram, gives, for odd $L\geq3$,

\[
V_L=x^4V_{L-2}+C(x),\qquad
C(x)=x^2-x^4+x^6-x^8.
\]

For $L=2m+1$, iteration gives

\[
V_L=x^{4m}(x^2+x^6-x^8)
+C(x)\sum_{j=0}^{m-1}x^{4j},
\]

with the sum empty for $m=0$. The first summand has a unique highest power $-x^{4m+8}=-x^{2L+6}$; the second has degree at most $4m+4$. Every monomial in this formula has positive exponent. For $N\geq1$, reduction of $x^N$ to the basis $1,x$ gives an $x$-coefficient that is monic of degree $N-1$: this follows by induction from $x^2=px+1$. Its scalar coefficient has degree at most $N-2$ for $N\geq2$. Thus the unique highest monomial of $V_L$ yields

\[
\deg_p V_L=2L+5,
\qquad b_{2L+5}(K_L)=-1.
\]

Take the fixed-shadow host family containing this trefoil state. The pre-planting shadow has three crossings and one component, hence $B_{\rm host}=9$. The asserted machine overhead is $11$, so the cited package predicts $\deg_p V\leq22$ at every vertex of the ordinary residual cube, for every odd $L\geq3$. Its all-positive vertex is $K_L$. At $L=23$, the prediction conflicts with $b_{51}(K_{23})=-1$. This establishes the incompatibility. The same formula proves unbounded degree as $L\to\infty$, so replacing $11$ by a different fixed overhead cannot repair this universal assertion. \(\square\)

The geometric identification of the marked seed should appear explicitly in the note or its figure. Replacing an arbitrary crossing in the usual parallel-strand trefoil braid is not a substitute for specifying this anti-parallel twist family. The root agent's independent recurrence derivation and appendix should certify that identification rather than treating the displayed recurrence alone as its definition.

## 5. Boundaries of the conclusion

1. **Do not present Theorem 5.6 as refuted with its hypotheses verified.** The example is not independently proved to satisfy all of (C1)–(C3). The contradicted assertion is that the universal construction supplies the package yielding the stated residual cap. The conditional paired-skein implication above remains valid.

2. **Use the entire residual cube.** The all-positive length-$23$ state belongs to $Q_\rho$. It is not one of the two special non-extreme states of the residual sign face $F_Z=\{Z^+,Z^-\}$ in Definition 5.9. Those two states have fixed opposite-sign pairs that cancel. Lemma 5.8 asserts its bound on $Q_\rho$, so the example directly addresses its stated quantifier.

3. **Do not treat the trefoil as an anchor-vanishing example.** It has nonconstant Jones polynomial. The contradiction occurs before Theorem 5.10's anchor-vanishing assumption. Choosing $L=23>22$ also meets the later length inequality, but does not make the trefoil satisfy the later vanishing assumption, and that inequality is unnecessary for the present contradiction.

4. **Do not claim a counterexample to the main theorem or Jones detection.** Theorem 6.8, pp. 50–53, claims $N\leq3c(K)$ for every nontrivial $J_N$-trivial knot; Theorem 6.9, p. 53, claims Jones unknot detection. Every $K_L$ here has nonconstant Jones polynomial. The proof of Theorem 6.8 invokes the two-machine descent (Theorem 5.11), which uses Lemma 5.8's initialization. The false universal package means the submitted argument does not establish the main theorem. It does not prove that theorem false or preclude a different argument under additional hypotheses.

5. **The usual crossing-number cap survives.** The ordinary $K_L$ diagram has $L+2$ crossings, so Corollary 3.7 gives the compatible estimate $\deg_p V_L\leq3L+6$. The contradiction is to keeping the cap attached to the fixed three-crossing pre-planting host while allowing an arbitrarily long residual block.

6. **Minimality and fixed-overhead repairs have precise limits.** The chosen pre-planting trefoil diagram is already minimal, so adding only host minimality cannot repair the universal package. A larger fixed overhead cannot repair its unbounded-degree conclusion. This does not rule out a newly restricted claim for minimal diagrams of hypothetical nontrivial Jones-unit knots; the present family supplies no example in that class.

7. **No isolated G2 verdict follows from this note's argument.** LATE-04 contains a separate geometric investigation, but the residual-degree calculation alone does not isolate one false local movie or one false clause of Proposition 5.12. Avoid incorporating that stronger assertion without separately presenting its evidence. The present obstruction is complete without it.

## 6. Suggested abstract-level wording

“We give an explicit obstruction to the uniform residual-degree bound used in Carmi and Cohen's arXiv:2606.22410v1. At a marked anti-parallel crossing of a minimal three-crossing trefoil diagram, the odd residual twist family has Jones–Vassiliev degree $2L+5$. The package of Proposition 5.12, Theorem 5.6, and Lemma 5.8 instead gives the constant bound $22$. In particular, the length-$23$ member has $b_{51}=-1$. This disproves the universal intermediate package and prevents the proof as written from establishing its main theorem. It does not give a counterexample to that theorem or to Jones unknot detection.”

## 7. Authorship and disclosure decision

Apply the decision in `collab/msgs/20261103-215308-claude.md`: author **Caleb Barnett**, contact **barnettcaleb1.github.io**, no invented affiliation. Immediately before the references, use an unnumbered section headed **Statement on the use of AI systems** with the following exact approved sentence:

“The computation in this note was carried out within an AI collaboration directed by the author (GPT-6 through Codex and Claude Fable 5.1 through Claude Code) and verified independently by both systems; the author takes responsibility for every statement.”

No external contact, submission, or publication is part of this review.
