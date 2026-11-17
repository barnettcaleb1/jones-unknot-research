import sys, time
sys.path.insert(0, '$HOME/jones-adversarial-pass/bbb-gap-note/check/compute')
from braidlib import *
A14 = parse("s3 s2 s1 s1 s2^-1 s3^-1"); A24 = parse("s3 s2 s2 s3^-1"); A34 = parse("s3 s3")
X = power([1, 2], 6); b = comm(comm(A14, A24), A34); Phi0 = comm(X, b)
t0 = time.time(); im = artin_right(reduce_word(Phi0), 4); print("right action F4 on reduced Phi0:", round(time.time()-t0,1), "s", [len(im[j]) for j in im])
t0 = time.time(); bu = burau(Phi0, 4, 'U'); print("Burau U:", round(time.time()-t0,2), "s")
t0 = time.time(); bu = burau(Phi0, 5, 'U'); print("Burau U B5:", round(time.time()-t0,2), "s")
# block composition: images under X and b, then compose
t0 = time.time()
def compose_right(imgs_u, imgs_v):
    # x.(uv) = phi_v(phi_u(x)): substitute imgs_v into imgs_u
    out = {}
    for j, wd in imgs_u.items():
        r = []
        for c in wd:
            r.extend(imgs_v[abs(c)] if c > 0 else inv(imgs_v[abs(c)]))
        out[j] = reduce_word(r)
    return out
iX = artin_right(X, 4); ib = artin_right(reduce_word(b), 4); iXi = artin_right(inv(X), 4); ibi = artin_right(inv(reduce_word(b)), 4)
print(" block sizes X", [len(v) for v in iX.values()], "b", [len(v) for v in ib.values()])
r = compose_right(compose_right(compose_right(iX, ib), iXi), ibi)
print("block composition:", round(time.time()-t0,1), "s", [len(r[j]) for j in r], "agrees:", r == im)
