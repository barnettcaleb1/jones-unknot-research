"""validate tl.py against known brackets."""
from tl import *
def closed(word):
    br = evaluate_tangle(word, 0, 0)
    assert list(br) == [()]
    return pdiv_delta(br[()])
# plat closures of 4-braids sigma_2^k: (2,k) torus links
for k in range(1, 6):
    w = [('cap', 0), ('cap', 2)] + [('x', 1)] * k + [('cup', 2), ('cup', 0)]
    print('sigma2^%d plat:' % k, pstr(closed(w)))
# figure eight: plat closure of sigma2 sigma1^-1 sigma2 ... use rational tangle 2 1 1? use known: 4_1 = plat of s2 s1^-1 s2? test
w = [('cap', 0), ('cap', 2), ('x', 1), ('x', 1), ('y', 0), ('y', 0), ('cup', 2), ('cup', 0)]
print('fig8 candidate:', pstr(closed(w)))
# compare with tools/diagram.py on the same structure via kauffman? (independent check: compute Jones of trefoil)
