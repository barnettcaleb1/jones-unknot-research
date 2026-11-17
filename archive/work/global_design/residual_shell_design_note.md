# A marked Borromean infection of the two nonorientable bands: rejected

2026-11-03. One explicit candidate, not a scan. Holder/root request:
residual unit11 invariant tensor. Computed with archived exact TL algebra;
root independently reproduced all eight corners from planar diagrams in
Regina. The independent program and saved PD codes are in
two_band_infection_independent.py and two_band_infection_independent.json.
No known-class escape or novelty claim.

## Complete diagram specification

Use six braid strands, top nodes0,...,5 and bottom nodes6,...,11. Close by
these fixed exterior pairs:

    Q=[(6,9),(7,8),(1,2),(3,4),(5,11),(0,10)].

Use sigma_i=A I+A^-1 e_i and stack words top to bottom. Put two marked
boxes AT THE TOP, acting on strands(1,2) and(3,4): a0 filling is I and
a1 filling is respectively e1 or e3 (generator indices one-based).
All four raw brackets use this one diagram and this one framing.

For a three-strand core braid define its ribbon cable by

    cable(sigma_i)=(sigma_(2i),sigma_(2i-1),sigma_(2i+1),sigma_(2i)),

and cable an inverse by reversing that block and reversing its signs.
The exact baseline and candidate are

    beta=[sigma1^2,sigma2^2]
        = [1,1,2,2,-1,-1,-2,-2],
    w0 = sigma1^3 sigma3^3 cable(sigma2),
    w  = sigma1^3 sigma3^3 cable(beta sigma2).

Explicit candidate word:

    [1,1,1,3,3,3,2,1,3,2,2,1,3,2,4,3,5,4,4,3,5,4,
     -2,-3,-1,-2,-2,-3,-1,-2,-4,-5,-3,-4,-4,-5,-3,-4,4,3,5,4].

The last core sigma2 specifies the hairpin return side. It swaps the
middle and last core strands, after which the two bottom ribbon cups
(6,9),(7,8) join core strands1 and2. In original core labels band1 thus
uses strands1 and3, and band2 uses strand2. The return passes OVER the
middle core at that final positive sigma2; there is no unspecified
choice of side. The exterior pairs describe a disk with the two band
attachments alternating around its boundary. Each band has three
positive half-twists, supplied by sigma1^3 and sigma3^3.

Replacing beta by the identity gives the ordinary rational calibration.
The top cuts sever the ribbons. Cutting both leaves an embedded disk,
hence an actual unknot. Cutting either ribbon deletes at least one of
beta's core strands. Every such deletion of beta is the identity braid,
with the inherited ribbon framing. Thus the three proper corners are
unchanged; the only nontrivial certificate is the joint corner00.

## Exact result

The baseline tensor is exactly -A^-3 G Omega, with

    C00^0=-A^6+A^2-2A^-2+A^-6-2A^-10+A^-14,
    C01^0=C10^0=A^-4+A^-12-A^-16,
    C11^0=A^-18.

The candidate has the SAME three proper corners. Its joint bracket is

    C00=A^-30-A^-26-A^-10-A^-2+A^2-A^6+A^10-A^14.

The only invariant-tensor defect is therefore

    D=C00-C00^0=A^-30(1-A^4)(1-A^16)(1-A^24),

which is nonzero. This ONE candidate is rejected as a universally
opposite-Omega invariant shell. The defect vanishes at zeta8, so it passes
the entire signed determinant pattern(8,3,3,1); determinants alone could
not have rejected it. This does not exclude other two-band infections.

No claim is made that its orbit knots lie outside every known detection
class. A rational THREE-CORE cap presentation does not by itself classify
the FOUR-boundary-strand ribbon construction. That issue was deliberately
not used to reject this candidate: the exact joint bracket decides it.

## Reproduction of the exact calculation

The following uses only the already archived TL multiplication. It does
not enumerate braids, parameters, or placements.

```python
import importlib.util
from collections import defaultdict
s=importlib.util.spec_from_file_location('tl','work/generic_evidence/tl_exact.py')
t=importlib.util.module_from_spec(s); s.loader.exec_module(t)
n=6
ident,ts,_=t.tables(n)
order=list(range(n))+list(range(2*n-1,n-1,-1))
basis=[t.canonical(p,n) for p in t.matchings(order)]
Q=[(6,9),(7,8),(1,2),(3,4),(5,11),(0,10)]
loops=[len(set(t.components(
    [(j,a[j]) for j in range(12) if j<a[j]]+Q,12))) for a in basis]

def cable(word):
    out=[]
    for s in word:
        i=abs(s); b=[2*i,2*i-1,2*i+1,2*i]
        out += b if s>0 else [-j for j in b[::-1]]
    return out

def ev(word,cuts):
    vec=[{} for _ in basis]; vec[ident]={0:1}
    for typ,x in [('e',i) for i in cuts]+[('s',i) for i in word]:
        nxt=[defaultdict(int) for _ in basis]
        for j,p in enumerate(vec):
            if typ=='s': t.addto(nxt[j],p,1 if x>0 else -1)
            dest,lp=ts[abs(x)-1][j]; qq=p
            for _ in range(lp): qq=t.loopmul(qq)
            t.addto(nxt[dest],qq,
                (-1 if x>0 else 1) if typ=='s' else 0)
        vec=[t.clean(p) for p in nxt]
    out=defaultdict(int)
    for j,p in enumerate(vec):
        for _ in range(loops[j]-1): p=t.loopmul(p)
        t.addto(out,p)
    return dict(sorted(t.clean(out).items()))

beta=[1,1,2,2,-1,-1,-2,-2]
w0=[1]*3+[3]*3+cable([2])
w=[1]*3+[3]*3+cable(beta+[2])
for cuts in ([],[1],[3],[1,3]):
    print(cuts,ev(w0,cuts),ev(w,cuts))
```

## All-parameter finish for this fixed opposite-Omega orbit

Root supplied an independent direct PD/Regina check of all eight raw
corner polynomials (baseline and candidate). The11 corner simplifies to
one crossing-free component, the singles to three-crossing diagrams,
and the joint candidate corner to15 crossings. The following strengthens
rejection of invariance to rejection of EVERY nonzero orbit parameter;
it uses no orbit evaluations.

Write C=C^0+D E00, u=C^0_11=A^-18, d=det(Omega)=-A^-6, and let e_1 here
mean the second standard coordinate vector (slot index1). For the actual
rational input pair Omega^n e_1, Omega^-n e_1, the raw closure bracket is

    P_n=e_1^T(Omega^T)^n C Omega^-n e_1
       =u+D (Omega^n)_01 (Omega^-n)_01
       =u-D b_n^2/d^n,     b_n=(Omega^n)_01.

The second equality uses the exact invariance of C^0. The third uses
the inverse formula for a two-by-two matrix. All entries are Laurent
polynomials: det(Omega) is a Laurent unit.

For every nonzero integer n, Cayley--Hamilton over the quadratic splitting
field gives

    b_n=Omega_01 (lambda1^n-lambda2^n)/(lambda1-lambda2).

Here Omega_01=A^-3 is nonzero, and the eigenvalue ratio is not a root of
unity by the previously banked omega_orbit_rigidity.md proof. Therefore
b_n is nonzero whenever n is nonzero. Since D is nonzero, P_n differs
from u for every such n.

This also rules out a monomial from an untracked framing shift. D vanishes
to order three at A=1, and all matrix entries are regular there. Hence

    P_n(1)=1,        P'_n(1)=-18.

These are actual link brackets. Their absolute value at1 is2^(c-1), so
all the closures have exactly ONE component, including odd n. If any
had normalized Jones polynomial1, its raw bracket would be a monomial
+/-A^k. The two displayed evaluations force that monomial to be A^-18=u,
contrary to P_n!=u for n!=0. The n=0 corner is the actual unknot.

Thus the Jones-unit locus of this entire fixed-input orbit is EXACTLY
{0}, and that parameter is the unknot. This is an exact family exclusion,
not a known-class classification or a statement about other infections.
The derivation was independently checked by /root/residual_shell_design
at root's request after the direct-diagram replay.
