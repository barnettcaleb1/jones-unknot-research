# Generalised Lemma 2 in the matrix model: if rho(Y) == I mod (t+1)^d, then for pure X the
# arc data q_j(X) = rho(X)[3][j]/(1-t), j = 1,2 (class of the noose / (1-t)) satisfy
# q_j(YX) == q_j(X) and q_j(XY) == q_j(X) mod (t+1)^d.  Exact Laurent arithmetic.
import json, random
src = open(__file__.replace("lemma2_deep.py", "depth.py")).read()
src = src.split("# ---------------- iterated commutators")[0].split('print("Phi0 word length"')[0]
exec(src)
def divide_by(a, d):
    if not a: return {}
    a = dict(a); q = {}; dh = max(d)
    while a:
        lead = max(a)
        if a[lead] % d[dh]: return None
        c = a[lead] // d[dh]; e = lead - dh
        q[e] = q.get(e, 0) + c
        a = padd(a, pshift(pscale(d, c), e), -1)
        if len(q) > 20000: return None
    return q
words = json.load(open(__file__.replace("lemma2_deep.py", "odd_depth2_words.json")))
gens = [A(i, j) for i in range(1, 4) for j in range(i + 1, 5)]
random.seed(3)
for dkey in ("2", "3", "4"):
    Y = words[dkey]; d = int(dkey)
    worst = 99
    for trial in range(6):
        X = []
        for _ in range(random.randint(1, 5)):
            g = random.choice(gens); X += g if random.random() < .5 else winv(g)
        RX, RYX, RXY = rho(4, X), rho(4, Y + X), rho(4, X + Y)
        for j in (0, 1):
            qX = divide_by(RX[2][j], ONEMT); qYX = divide_by(RYX[2][j], ONEMT); qXY = divide_by(RXY[2][j], ONEMT)
            assert None not in (qX, qYX, qXY)
            worst = min(worst, val_tplus1(padd(qYX, qX, -1)), val_tplus1(padd(qXY, qX, -1)))
    print(f"Y of depth {d}: min (t+1)-adic valuation of q(YX)-q(X), q(XY)-q(X) over trials = {worst}")
