import sys, time
sys.path.insert(0, '.')
from harness import *

# Reproduce designer's numbers
A0 = IdentityBraid(2) | IntegerTangle(3).rotate(1)
B0 = IntegerTangle(-3).rotate(1) | IdentityBraid(2)
h = h_block()
print('mates T.rotate(1):', boundary_mates(IntegerTangle(3).rotate(1)))
print('mates U.rotate(1):', boundary_mates(IntegerTangle(-3).rotate(1)))
print('mates h:', boundary_mates(h))
Lt = A0 * h * h * B0
print('mates A0*h*h*B0:', boundary_mates(Lt))
L = Lt.braid_closure()
r = abs_bracket(L)
print('link crossings', r['crossings'], 'components', r['components'], 'writhe', r['writhe'])
print('<L>_abs =', pstr(r['bracket']))
V = jones_from_abs(r['bracket'], r['writhe'])
print('V(L) =', jones_str(V))

# H2 knot
K = (A0 * h * sigma2(1) * h * B0).braid_closure()
r = abs_bracket(K)
print('H2 K(0,0): crossings', r['crossings'], 'components', r['components'], 'writhe', r['writhe'])
print('V =', jones_str(jones_from_abs(r['bracket'], r['writhe'])))

# harness versions
L2 = assemble(T_piece('lit', 'I'), U_piece('lit', 'I')).braid_closure()
r2 = abs_bracket(L2); print('harness lit/I link:', r2['crossings'], r2['components'], pstr(r2['bracket']))
L3 = assemble(T_piece('seed', 'I'), U_piece('seed', 'I')).braid_closure()
r3 = abs_bracket(L3); print('harness seed/I link:', r3['crossings'], r3['components'], pstr(r3['bracket']))
print('V seed/I =', jones_str(jones_from_abs(r3['bracket'], r3['writhe'])))
# omega(infinity) check
print('mates omega(I2):', boundary_mates(omega(IdentityBraid(2))), ' IntegerTangle(3):', boundary_mates(IntegerTangle(3)))
print('mates omega_bar(I2):', boundary_mates(omega_bar(IdentityBraid(2))), ' IntegerTangle(-3):', boundary_mates(IntegerTangle(-3)))
# brackets of the (2,2) tangles via numerator closures as a check that omega(I2) ~ 3 and omega_bar(I2) ~ -3
for name, T in (('omega(I2)', omega(IdentityBraid(2))), ('3', IntegerTangle(3)), ('omega_bar(I2)', omega_bar(IdentityBraid(2))), ('-3', IntegerTangle(-3))):
    for cl in ('numerator_closure', 'braid_closure'):
        Lk = getattr(T, cl)()
        rr = abs_bracket(Lk)
        print(f'  {name:14s} {cl:18s} cr={rr["crossings"]:2d} comps={rr["components"]} V={jones_str(jones_from_abs(rr["bracket"], rr["writhe"]))}')
