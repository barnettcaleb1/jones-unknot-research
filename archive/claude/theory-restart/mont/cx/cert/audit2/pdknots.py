"""pdknots.py -- AUDIT-2 PD-route test knots (built here; the public certify() API only takes halfwords).

Every knot is given as an oriented PD code (0-based, consecutive labels, ccw from incoming under) + signs, with
an independent label of what it is.  Morse-word constructions use a2lib (own code); KT comes from the Knot Atlas PD
stored in cx-tools/katlas_reference.json (data)."""
import sys, json, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit2')
import a2lib

KATLAS = '/Users/calebbarnett/jones-lanes/cx-tools/katlas_reference.json'


def katlas_pd(name):
    d = json.load(open(KATLAS))[name]
    X = [tuple(e - 1 for e in x) for x in d['pd_list']]
    return a2lib.relabel_pd(X)


# ---- Morse companions
TREFOIL = a2lib.plat4_full([('x', 1)] * 3)                       # 4-plat closure of sigma_2^3 = trefoil
FIG8 = a2lib.plat4_full([('x', 1), ('y', 0), ('x', 1), ('x', 1)])  # figure-eight (V checked = t^-2-t^-1+1-t+t^2)


def from_full(full):
    X, sg = a2lib.pd_from_full(full)
    return [tuple(x) for x in X], list(sg)


def cancel_insert_full(full, rng, nins=3, wlen=8):
    """insert braid words W W^-1 at random points of a Morse word (positions valid for the current strand count)."""
    full = list(full)
    for _ in range(nins):
        # strand counts before each position
        cnt = [2]
        for c, i in full:
            if c in 'lr': cnt.append(cnt[-1] + 2)
            elif c == 'u': cnt.append(cnt[-1] - 2)
            else: cnt.append(cnt[-1])
        cand = [j for j in range(len(full)) if cnt[j] >= 2]
        j = rng.choice(cand)
        m = cnt[j]
        W = a2lib.random_braid_word(rng, m - 1, wlen)
        full = full[:j] + W + a2lib.inverse_braid(W) + full[j:]
    return full
