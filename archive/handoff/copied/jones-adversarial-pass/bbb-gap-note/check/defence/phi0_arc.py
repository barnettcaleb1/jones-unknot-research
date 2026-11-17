# Disk sequences of proper products Phi = Phi'.Gamma_1 (word criterion) with rho_4(Phi) = I at t = -1:
#  (S) small non-Brunnian example  Y = [Delta_3^4, A34] = [y3^-2, y1]
#  (N) the note's Brunnian Phi0 = [y3^-2, [[g1,g2],g3]] (= [delta^-2, b]), conjugated into the form Phi'.Gamma_1
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lp import *
from curves import *
from lemma63 import PUSH, push_word, W, G1, LEMMA63

I4 = [[int(i == j) for j in range(4)] for i in range(4)]
IMG = {}
for k in (1, 2, 3):
    IMG[k] = act(4, PUSH[k]); IMG[-k] = act(4, finv(PUSH[k]))

def act_y(yword, w):
    t0 = time.time()
    for idx, y in enumerate(yword):
        w = subst(w, IMG[y])
    return w

def g2y(gw):  # g1 = y3 y2^-1, g2 = y2 y1^-1, g3 = y1
    m = {1: [3, -2], 2: [2, -1], 3: [1]}
    out = []
    for x in gw:
        img = m[abs(x)]; out += img if x > 0 else finv(img)
    return fred(out)

def report(name, Phiy, n=4):
    Phiy = fred(Phiy)
    t0 = time.time()
    br = push_word(Phiy)
    R = burau(4, br)
    triv = meval(R, -1) == I4; nontriv = meval(R, 2) != I4
    loop = to_u(act_y(Phiy, [3]), 4)
    v, c = arc_from_loop(loop)
    cr = crossings(v, 4)
    ks = [sum(l) for _, l in cr]; k0 = ks[0]
    terms = [(e, k - k0) for (e, _), k in zip(cr, ks)]
    disks = []
    for i in range(len(cr) - 1):
        D = [b - a for a, b in zip(cr[i][1], cr[i + 1][1])]
        P = frozenset(m + 1 for m, x in enumerate(D) if x)
        disks.append(dict(P=P, changing=cr[i][0] != cr[i + 1][0], W=sum(D)))
    bad = [d for d in disks if LEMMA63.get(d['P']) != ('chg' if d['changing'] else 'pres')]
    n4 = sum(1 for d in disks if d['P'] == frozenset({1, 2, 3, 4}))
    has3 = any(d['P'] == frozenset({1, 2, 3}) for d in disks)
    Mm1 = sum(e * (-1) ** (k % 2) for e, k in terms)
    c_ = [e * (-1) ** (k % 2) for e, k in terms]
    flips = [i for i in range(len(c_) - 1) if c_[i] != c_[i + 1]]
    fourpos = [i for i, d in enumerate(disks) if d['P'] == frozenset({1, 2, 3, 4})]
    print(f"[{name}]  y-word length {len(Phiy)}, sigma-length {len(br)}")
    print(f"   rho_4(Phi)=I at t=-1: {triv};  rho_4(Phi)!=I at t=2: {nontriv}")
    print(f"   m = iota(alpha,(beta3*)Phi) = {len(terms)};  4-disks: {n4};  disks outside the Lemma 6.3 list: {len(bad)};"
          f"  3-disk {{p1,p2,p3}} present: {has3};  parity holds: {not bad and n4 == 0}")
    print(f"   M_Phi(-1) = {Mm1}  (note's Lemma 2 predicts 0);  c_i = eps_i(-1)^k_i flips exactly at the 4-disks: {flips == fourpos}")
    blocks = [b - a for a, b in zip([-1] + fourpos, fourpos + [len(c_) - 1])]
    print(f"   sizes of the {len(blocks)} blocks cut out by the 4-disks: first few {blocks[:12]} ; alternating sum = {sum(((-1)**i)*x for i,x in enumerate(blocks))}")
    print(f"   [time {time.time()-t0:.1f}s]")
    sys.stdout.flush()

if __name__ == '__main__':
    Winv = finv(W)
    # (S)
    Y = fred([-3, -3, 1, 3, 3, -1])          # [y3^-2, y1]
    assert act(4, push_word(Y)) == act(4, fcomm([1, 2] * 6, [3, 3]))   # equals [Delta_3^4, A34] as braids
    PhiP = Winv + Y
    assert fred(PhiP) == PhiP and PhiP[-1] != 2
    report("S: Phi = Gamma1^-1 [y3^-2, y1] Gamma1", PhiP + W)
    # (N)
    bg = fred(fcomm(fcomm([1], [2]), [3]))
    b_y = g2y(bg)
    Phi0y = fred(fcomm([-3, -3], b_y))
    print("Phi0 = [y3^-2, b], b = [[g1,g2],g3];  reduced y-word of Phi0:", Phi0y, "length", len(Phi0y))
    def A(i, j):
        up = list(range(j - 1, i, -1)); return up + [i, i] + finv(up)
    phi0_sigma = fcomm([1, 2] * 6, fcomm(fcomm(A(1, 4), A(2, 4)), A(3, 4)))
    for tv in (2, 3, -2, 5):
        assert meval(burau(4, push_word(Phi0y)), tv) == meval(burau(4, phi0_sigma), tv)
    print("   Burau of Push(Phi0 y-word) equals Burau of the note's sigma-word at t = 2, 3, -2, 5")
    cand = Winv + Phi0y
    ok = fred(cand) == cand and cand[-1] != 2
    print("   Gamma1^-1 . Phi0 freely reduced and not ending in y2:", ok)
    sys.stdout.flush()
    if ok:
        report("N: Phi = Gamma1^-1 Phi0 Gamma1  (a conjugate of the note's Phi0 of the form Phi'.Gamma1)", cand + W)
