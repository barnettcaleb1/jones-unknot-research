# JT2 gadgets: formal differences, serial carriers, and component cost

17 November 2026. Exact algebra for the active link-complexity program. No enumeration. All statements below concern specified architectures; none is a general obstruction to JT2 hardness. The formulas were independently read by the root agent during their development. External review and novelty remain unassessed.

## 1. Conventions and the finite-difference identity

Let R=Z[A,A^-1], delta=-A^2-A^-2, and TL2=R[I,e]/(e^2=delta e). Use raw framed brackets until a final common writhe normalization is specified. A marked planar context with m slots induces an R-multilinear map C on their relative skein modules. The output may be another relative module or a scalar closure.

For pairs T_i,S_i in those modules, multilinearity gives

    C(T_1-S_1,...,T_m-S_m)
      = sum_(E subset {1,...,m}) (-1)^(m-|E|)
          C(U_1(E),...,U_m(E)),

where U_i(E)=T_i when i is in E and S_i otherwise. If T_i-S_i=kappa_i D_i, then the result is

    (product_i kappa_i) C(D_1,...,D_m).                  (1)

Thus the proposed product of vanishing factors is correct **in the linear skein category**. For actual inputs, the left side is generally a signed sum of 2^m actual diagrams. Equation (1) does not compile that sum into one actual diagram. A hardness construction needs such a compiler, or a different direct realization of the resulting tensor, with size and component count controlled.

For the two crossing operators

    R_+ = A I + A^-1 e,
    R_- = A^-1 I + A e,

one particularly useful identity is

    R_+ - A^2 R_- = A^-1(1-A^4)e.                     (2)

This is a monomial-weighted difference. It is not the ordinary unweighted crossing difference of ambient-isotopy Jones polynomials. The monomial weights must be tracked when comparing different closures; a separate normalization per sample cannot be discarded. Raw R_+-R_- instead equals (A-A^-1)(I-e), whose divided defect is itself a signed skein combination.

## 2. A pure vanishing defect is not an actual tangle

**Lemma.** The complete relative bracket of a nonempty actual classical tangle does not vanish after A=1. Consequently a nonzero skein vector divisible by A-1 cannot be the complete bracket of an actual tangle, even up to a Laurent monomial unit.

**Proof.** Close the tangle by any actual closing tangle to obtain a nonempty link L. The absolute value of its reduced bracket at A=1 is 2^(c(L)-1), hence nonzero. If the relative vector specialized to zero, every such closure would be zero. A monomial unit specializes to a sign and does not change this argument. The same conclusion for an already closed diagram follows directly from its component count.

So a difference tensor that carries a factor 1-t cannot simply be used as an actual standalone gadget. It needs a nonvanishing background channel. This does not prohibit individual coordinates of an actual tangle vector from vanishing at A=1, nor their use as encoded data.

### Specialization already determines matching and closed-component count

The banked boundary-connectivity lemma requires only its specialized hypothesis:

    [T](1) = +/- [S](1),                              (3)

not equality of the full Laurent vectors. To see this, let pi,sigma be their endpoint matchings, let r,s count closed components, and let ell be the number of cycles of pi union sigma. Close both by a common actual tangle for pi, and then by a common actual tangle for sigma; crossingful closing tangles are allowed. Absolute bracket values imply

    r+n=s+ell,    r+ell=s+n.

Thus ell=n, pi=sigma, and r=s. This observation will fix the topology of the projector carriers below.

## 3. Exact criterion for a background-plus-product gate

Choose backgrounds P_i and defects D_i, and introduce independent formal variables z_i. The multilinear context polynomial is

    F(z_1,...,z_m)=C(P_1+z_1D_1,...,P_m+z_mD_m).

For E a subset of the slots, write

    h_E=C(D_i for i in E; P_i for i outside E).

Then

    F=h_empty + H product_i z_i                       (4)

holds if and only if

    h_E=0 for every nonempty proper E,
    h_full=H.                                         (5)

This is also the exact criterion if (4) is requested for every Boolean input z_i in {0,1}, since a multilinear polynomial is determined by its Boolean evaluations over this characteristic-zero domain. Thus the problem is not merely to create a high-order mixed difference. It is to annihilate every proper-subset contribution while retaining the full one.

### Bare smoothing defects fail the criterion

Suppose each P_i is a monomial unit times an actual tangle, each D_i=kappa_i E_i with nonzero scalar kappa_i and actual tangle E_i, and C is an actual closed context. Each h_E is then a product of nonzero scalars times the bracket of one actual link. The latter is nonzero by its A=1 value. Therefore **every h_E is nonzero**.

For m>=2 such a context cannot satisfy (5). In particular, using (2) at every variable slot does give a product factor in the alternating difference, but no actual outside wiring can turn that elementary interpolation into only a background and the all-variable product. Every proper-subset smoothing coefficient survives.

This is a universal independent-variable identity obstruction. It does not exclude cancellations after special values z_i(A) are substituted, instance-dependent identities, more elaborate signed defects, encoded fusion bases, or larger-boundary selectors. EKT-type divided defects need not be scalar multiples of actual tangles, so they are not ruled out by this argument without checking that hypothesis.

## 4. Serial TL2 carriers: binary closure cancellation is not reusable multiplication

Work over K=Q(A). Let ell:TL2(K)->K be a scalar closure functional, and set

    alpha=ell(I), beta=ell(e), alpha!=0.

Consider the serial architecture

    ell(product_i (I+z_i D_i)).                        (6)

All singleton terms vanish precisely when ell(D_i)=0. The kernel of ell is one-dimensional, generated by

    Z=beta I-alpha e.

A direct multiplication gives

    ell(Z^2)=alpha beta(alpha delta-beta).             (7)

Thus a **formal binary gate** exists whenever (7) is nonzero:

    ell((I+xZ)(I+yZ))
       =alpha+xy alpha beta(alpha delta-beta).         (8)

For the reduced trace closure, alpha=delta,beta=1, and the mixed coefficient is delta(delta^2-1). This is a genuine skein algebra identity. It does not say that I+xZ is an actual tangle for the desired x(A).

More importantly, the open output before closure still has the singleton terms (x+y)Z. Closing kills them; it does not remove them from the state so that the state can be fed into the next multiplication gate.

**Serial obstruction.** For m>=3 there are no D_i giving a nonzero H in

    ell(product_i(I+z_iD_i))=alpha+H product_i z_i.     (9)

**Proof.** A nonzero full coefficient implies every D_i is nonzero. Vanishing singleton terms makes D_i=s_iZ with all s_i nonzero. Any pair is now a proper subset, so (5) forces ell(Z^2)=0 as well as ell(Z)=0. The quadratic relation for Z is

    Z^2-(2beta-alpha delta)Z
      +beta(beta-alpha delta)I=0.

Applying ell and using alpha!=0 shows beta(beta-alpha delta)=0. Hence Z^2 is a scalar multiple of Z, and ell(Z^k)=0 for every k>=1. The full coefficient in (9) is zero, a contradiction.

The argument also applies to invertible backgrounds P_i in this commutative K-algebra: factor their product out, replace D_i by P_i^-1 D_i, and replace ell by multiplication by the product followed by ell, provided the background closed value is nonzero. An actual closed background has this property.

This is a fixed two-state **serial** obstruction. It does not apply to arbitrary planar networks, larger fusion spaces, tensor products retaining several registers, or noninvertible backgrounds. The next section treats the most natural noninvertible escape.

## 5. The projector multiplier works algebraically and costs components geometrically

Over K define the orthogonal idempotents

    p0=e/delta, p1=I-e/delta.

They obey p0p1=0 and p_i^2=p_i. Therefore

    product_i(p0+z_i p1)=p0+(product_i z_i)p1.          (10)

This is the desired arbitrary-arity product carrier. In the integral lattice, put

    C(z)=e+z(delta I-e)=delta(p0+z p1).

Then (10) becomes

    product_i C(z_i)
      =delta^(m-1)[e+(product_i z_i)(delta I-e)].      (11)

The nonunit delta factors cannot be removed by a writhe monomial.

**Component-cost theorem.** Suppose each C(z_i(A)), with z_i(1)=0, is the full bracket of an actual two-string tangle T_i up to a monomial unit. Then any actual closure of their serial composition has at least m components. In particular this literal architecture cannot produce a two-component JT2 instance when m>=3.

**Proof.** At A=1, each state is e up to sign. By (3), each T_i has the cup-cap endpoint matching and no closed component, just as e does. Composing m such matchings creates exactly m-1 closed components internally: at each interface the bottom cup of one matching meets the top cap of the next. Their geometry may be knotted or linked; the claim is only their number. The remaining two arcs acquire at least one additional component on any actual external closure. Therefore the total is at least m. Already-closed components cannot be fused by a context acting only on the remaining external boundary. This proves the theorem independently of the polynomial factor in (11).

Thus clearing the projector denominators exposes a real topological cost. A normalized projector expression is not automatically a realizable two-component link gadget. The hypothesis z_i(1)=0 is exactly the proposed placement of a vanishing factor on each input register; it is essential to this particular matching conclusion.

Changing the wiring by cutting inside earlier carriers, retaining additional boundary strands, or using a larger state space can escape the theorem. Those operations change the tensor problem and require a new exact compiler. The theorem does not rule them out.

## 6. What the next actual object must supply

The exact requirement is now concrete. A proposed actual multiplication/clause package should state:

1. Its logical background and defect states, including their specialized endpoint matchings and any closed components.
2. The marked open output tensor, not only one closing evaluation.
3. Which proper-subset coefficients vanish and why, as in (5).
4. How repeated use preserves the intended carrier, all framing units, diagram size, and exactly two final components.

Bare smoothing differences fail item 3; the binary serial closure identity fails reusable item 2; the projector accumulator fails item 4 in the two-component setting. These are precise excluded architectures, not a classification of the full Temperley–Lieb tensor-network model. No hardness reduction or universal structural no-go is claimed.
