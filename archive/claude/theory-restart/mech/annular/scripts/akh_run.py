import sys, time
from akh import *
word = sys.argv[1]
t = time.time()
r = khovanov(word, [('top', 0, True), (1, 2, True)])
print('word', word)
print('crossings', r['n'], 'n+', r['npl'], 'n-', r['nmi'], 'components', r['ncomp'], 'time %.1fs' % (time.time() - t))
print('Kh(h,q):', fmt(r['Kh']))
A = r['AKh']
for k in (2, 0, -2):
    print('AKh k=%d (h,q):' % k, ', '.join('(%d,%d):%d' % (h, q, v) for (h, q, kk), v in sorted(A.items()) if kk == k))
print('dims by k:', {k: sum(v for (h, q, kk), v in A.items() if kk == k) for k in (4, 2, 0, -2, -4)})
