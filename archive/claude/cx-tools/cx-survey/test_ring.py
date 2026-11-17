import sys; sys.path.insert(0, '.')
from harness import *
from bracket import Diagram
R = ring_box()
print('ring mates', boundary_mates(R))
L = R.braid_closure()
pd = L.PD_code()
D = Diagram(pd)
print('ring closure: crossings', len(pd), 'comps', D.num_components(), 'lk', dict(D.linking_matrix()))
# site tracing test on H2 knot
A = IdentityBraid(2) | IntegerTangle(3).rotate(1)
B = IntegerTangle(-3).rotate(1) | IdentityBraid(2)
X = A * (IdentityBraid(2) | labeled_identity('T')) * h_block() * sigma2(1) * h_block() * (labeled_identity('U') | IdentityBraid(2)) * B
L, edges = braid_closure_traced(X, ('T', 'U'))
pd = L.PD_code()
print('H2 traced: cr', len(pd), 'edges', edges)
print(pd)
# the ring around the T site, in the H2 knot, 3-comp link
X2 = A * (IdentityBraid(2) | ring_box()) * h_block() * sigma2(1) * h_block() * (ring_box() | IdentityBraid(2)) * B
L2 = X2.braid_closure()
pd2 = L2.PD_code(); D2 = Diagram(pd2)
print('H2 + two rings: cr', len(pd2), 'comps', D2.num_components(), 'lk', dict(D2.linking_matrix()))
import snappy
M = L2.exterior(); print('volume', M.volume(), M.solution_type())
