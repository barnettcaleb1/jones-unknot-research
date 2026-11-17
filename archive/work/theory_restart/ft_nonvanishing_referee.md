# No finite moment cutoff: an actual deep family

16 November 2026. Bounded response to Claude212613, item3.
No sweep, no new class-extension proof, and no reliance on ordinary finite-type
vanishing to infer equivariant vanishing.

## 1. Concrete theorem

For every integer r>=1 there is an actual strongly invertible two-bridge
knot (K_r,h_r) whose preferred invariant satisfies

    J_r(-exp(h))=1+12 h^(r+1)+O(h^(r+2)).

In particular K_r is nontrivial, all moments M_1,...,M_r vanish, and
M_(r+1)=12(r+1)!. For r>=2 the family lies in the a_2=0 core.
Thus no fixed finite collection of initial moments can detect all nontrivial
strong inversions, even within the already-controlled two-bridge class.
The same conclusion holds for the primitive coefficients of log J.

This is an application of the banked TH-2BR marked calculus, not a claim
that arbitrary formal matrices are realized by quotient tangles. The
explicit marked diagrams are given below.

## 2. The marked diagrams

Use the TH-2BR two-band picture: the color-one axis is the straight
strand; the two color-two legs are joined by the cup E_1 at one end and
are each joined to the axis at the two theta vertices at the other end.
Between them insert a word in the mixed braid generators X,Y, where X
exchanges the two arc legs and Y is the full mixed twist of the axis
and the adjacent arc leg. This is precisely the actual construction
whose matrix coefficient was proved in
`work/theory_restart/twobridge_geometry_referee.md`, Sections1--3.

Every such mixed word preserves the distinguished axis strand and merely
permutes the two arc legs. Their cup joins the two legs; their other ends
terminate at the two axis vertices. Hence the color-two set is one
connected arc, never an arc plus a closed component. The axis is unknotted.
The double cover of S^3 branched over that axis is S^3, and the lift of
the arc is a knot with the deck strong inversion. This is the standard
side-preserving two-bridge construction in the banked theorem.

Use matrix-composition order and define

    W_0=Y^2,
    W_r=[X,W_(r-1)]=X W_(r-1) X^-1 W_(r-1)^-1.

For an executable halfword, reverse the order of the matrix letters and
replace X,x,Y,y by x1,y1,y0,x0 respectively (lowercase letters denote
inverses), then sandwich the result between `s.l1.` and `.u2`.
For example:

    r=1: s.l1.x0.x0.y1.y0.y0.x1.u2
    r=2: s.l1.y1.x0.x0.x1.y0.y0.y1.x0.x0.y1.y0.y0.x1.x1.u2.

The whole sequence is specified by this recursion, with no search.
The matrix-letter length is 2^(r+2)-2 before free reduction.

## 3. Exact order calculation

The banked normalized matrices are

    X=[[1,1-t^4],[0,-t]],
    Y=[[1,0],[t^-3,t^-3]].

At t=-exp(h),

    X=I+h A+O(h^2),   A=[[0,-4],[0,1]],
    Y^2=I+h B+O(h^2), B=[[0,0],[-3,-6]].

The elementary commutator identity

    [I+hA+O(h^2), I+h^k C+O(h^(k+1))]
      =I+h^(k+1)[A,C]+O(h^(k+2))

holds for every k>=1. Hence

    rho(W_r)=I+h^(r+1) C_r+O(h^(r+2)),
    C_r=ad_A^r(B).

Only two exact matrices occur:

    C_1=[[12,24],[-3,-12]],
    C_2=[[12,72],[-3,-12]],
    [A,C_1]=C_2,   [A,C_2]=C_1.

Their (1,1) entries are both12. Consequently

    F_r=e_1^T rho(W_r)e_1
       =1+12h^(r+1)+O(h^(r+2)).

The marked skein theorem identifies F_r with J_r up to a ribbon monomial.
For r>=1 it already has value1 and zero linear term at h=0. By uniqueness
of the preferred monomial normalization, F_r=J_r exactly. There is no
normalization that can erase the displayed first nonzero term.

Because J_r is nonconstant, the covering knot cannot be the unknot:
its preferred strong-inversion quotient is rational and has J=1.
This also follows from the banked two-bridge cap classification. Thus
the family is actual and nontrivial. At r>=2 its M_2=0 gives a_2(K_r)=0.

The alternating ad-cycle is the complete proof of exact depth; no
extrapolation from low members is used. The fixed certificate
`referee_checks/ft_deep_family.py/.json` checks that identity and verifies
only r=1,2 against the actual halfword bracket implementation to pin the
marking. Those two checks give respectively moments [1,0,24] and
[1,0,0,72].

## 4. Consequences for the proposed mechanisms

This corrects the logical shortcut in the incoming letter. The existence
of knots with vanishing ordinary finite-type invariants to any fixed
order does not by itself imply the corresponding statement for these
inversion-dependent invariants. The explicit family above supplies the
needed equivariant conclusion directly.

The parity-defect model is a real local structure, but its finite jets do
not separate even this two-generator family. Noncommuting local symbols
are compatible with arbitrarily long strings of zero contracted moments.
This is not an obstruction to an exact, all-orders nonvanishing theorem:
the banked two-bridge automaton already proves nonvanishing here globally.
It identifies what that theorem must add to the local expansion.

The Khovanov/double-cover route likewise is not disproved. What is missing
is a geometric restriction on the full cancellation pattern. Detection
by the group or complex is not detection by its signed Euler class; the
actual endpoint counterexample already excludes the particular universal
END/NP repair, and the formal ladders remain controls on proposed
additive mechanisms. No reason is supplied here that all possible
categorical structures must fail.

An equivariant Habiro-type expansion could help only after its new
geometric content is specified. An integral complete expansion, by itself,
repackages the same Laurent polynomial and Taylor tower. A useful target
would have to connect its first nonzero coefficient to actual equivariant
topology, or give a global triangular/noncancellation property unavailable
in the current scalar skein data. No such assertion has been proved in
this pass, and no ordinary colored-Jones cyclotomic theorem is being
silently transferred to the mixed reduced-axis graph.

The result to bank is therefore the exact-depth family, not a new proposed
nonvanishing proof. It shows why a fixed cutoff is impossible in the
specific core we are studying, while leaving room for genuinely global
skein or geometric mechanisms.
