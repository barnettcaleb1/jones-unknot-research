"""independent box vector from two raw closures (BRIEF sec. 4): v = (alpha_0, (t^2 alpha_-1 - alpha_0)/(1-t^4)),
alpha_m = lp.J_raw(s.r2.(y1)^m.B.u1), m = 0, -1.  Returns channels (a, b) or None."""
import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen')
sys.path.insert(1, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import rg_core as C
import lp
def pdivexact(p, d):
    p = dict(p); q = {}
    if not p: return {}
    dt = max(d); dc = d[dt]; lo = min(p) - min(d)
    while p:
        e = max(p); c = p[e]; k = e - dt
        if k < lo or c % dc: return None
        q[k] = c // dc
        for f, g in d.items():
            ee = k + f; nv = p.get(ee, 0) - g * (c // dc)
            if nv: p[ee] = nv
            else: p.pop(ee, None)
    return q
def vec_from_J(body):
    a0 = lp.J_raw('s.r2.' + body + '.u1') if body else lp.J_raw('s.r2.u1')
    am = lp.J_raw('s.r2.x1.' + body + '.u1') if body else lp.J_raw('s.r2.x1.u1')
    if a0 is None or am is None: return None
    v2 = pdivexact(C.psub(C.pshift(am, 2), a0), C.ONEMT4)
    if v2 is None: return None
    return C.chans((a0, v2))
def same_up_to_unit(v, w):
    if not v[0] or not w[0]: return False
    j = max(v[0]) - max(w[0]); s = v[0][max(v[0])] // w[0][max(w[0])]
    if s not in (1, -1) or v[0][max(v[0])] != s * w[0][max(w[0])]: return False
    return all(C.psub(vi, {e + j: s * c for e, c in wi.items()}) == {} for vi, wi in zip(v, w))
