# Exact (Laurent) depth of [Phi0, s3 Phi0 s3^-1] and its mirror in every convention, B4 and B5,
# plus the iterated commutators in U and R.  Reuses only indep3.py's own classes (no phi0_check import).
import sys, os
sys.argv = ['x']
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, 'indep3.py')).read()
cut = src.index('# ------------------------------------------------------------------ claim: Fox Jacobian')
ns = {'__file__': os.path.join(here, 'indep3.py'), '__name__': 'indep3_lib'}
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src[:cut], 'indep3_head', 'exec'), ns)
LPR, rep, mat_sub_I, CONVS = ns['LPR'], ns['rep'], ns['mat_sub_I'], ns['CONVS']
C, Phi0r, conj3, wcomm, wred, mirror = ns['C'], ns['Phi0r'], ns['conj3'], ns['wcomm'], ns['wred'], ns['mirror']
def depth_lp(M):
    vals = [e.mult_minus1() for row in mat_sub_I(LPR, M) for e in row if not e.iszero()]
    return min(vals) if vals else float('inf')
for n in (4, 5):
    for conv in CONVS:
        print(f'B{n} {conv:2}: depth C = {depth_lp(rep(LPR, conv, n, C))}, depth mirror(C) = {depth_lp(rep(LPR, conv, n, mirror(C)))}')
# where does U differ from RT: show the valuation pattern of U(C) - I entries
M = mat_sub_I(LPR, rep(LPR, 'U', 4, C))
print('U(C) - I entry valuations (B4):')
for row in M: print('   ', [e.mult_minus1() if not e.iszero() else '-' for e in row])
M = mat_sub_I(LPR, rep(LPR, 'R', 4, C))
print('R(C) - I entry valuations (B4):')
for row in M: print('   ', [e.mult_minus1() if not e.iszero() else '-' for e in row])
# iterated commutators [Phi0, [Phi0, ..., C]] in U and R (B4), power series to keep it fast
PS = ns['RingPS'](12)
def depth_ps(M):
    D = mat_sub_I(PS, M)
    vals = [next((k for k, x in enumerate(e) if x), None) for row in D for e in row]
    vals = [v for v in vals if v is not None]
    return min(vals) if vals else '>=%d' % PS.K
Ck = C
for k in range(1, 4):
    print(f'iterated commutator #{k}: |word| = {len(Ck)}, depth U = {depth_ps(rep(PS, "U", 4, Ck))}, R = {depth_ps(rep(PS, "R", 4, Ck))}, UT = {depth_ps(rep(PS, "UT", 4, Ck))}, RT = {depth_ps(rep(PS, "RT", 4, Ck))}')
    Ck = wred(wcomm(Phi0r, Ck))
