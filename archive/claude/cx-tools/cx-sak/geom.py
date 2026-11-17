#!/usr/bin/env python3
"""
geom.py -- geometric pipeline for Sakuma links (cx-sak task).

Conventions (see c2_sakuma_recipe.md):
  * diagram plane = xy-plane, strong-inversion axis = y-axis,
    tau(x,y,z) = (-x, y, -z).
  * Symmetric knot K built from a mirror-symmetric planar waypoint list, lifted
    with z-bumps (+h on the over strand, -h on the under strand at every crossing).
  * Anti-equivariant normal field v = normalize(e_z - (e_z.T)T), rotated by
    k = -writhe/2 full right-handed turns on an interval I of K_1 and extended by
    v'(tau p) = -tau_* v'(p).  lambda_+ = K + eps v'.
  * Quotient p(x,y,z) = (x^2 - z^2, y, 2xz); B = y-axis (closed far away on the
    left), L = p(lambda_+).
  * PD extraction from a generic rotated projection; PD convention as in kb.py.
"""
import math
import numpy as np
from collections import defaultdict

# ------------------------------------------------------------------ curves

def subdivide(wps, lmax=1.0):
    """Insert points so that no waypoint segment is longer than lmax (closed list)."""
    wps = np.asarray(wps, dtype=float)
    n = len(wps)
    out = []
    for i in range(n):
        p, q = wps[i], wps[(i + 1) % n]
        m = max(1, int(math.ceil(np.linalg.norm(q - p) / lmax)))
        for k in range(m):
            out.append(p + (q - p) * (k / m))
    return np.array(out)

def catmull_rom_closed(wps, spacing, alpha=0.5, lmax=1.0):
    """Closed centripetal (alpha=0.5) Catmull-Rom spline through the waypoints
    (after subdividing long segments); sampled with ~spacing.  Collinear control
    points give exactly straight pieces; centripetal parametrisation avoids
    overshoot loops for uneven spacing (Barry-Goldman form)."""
    wps = subdivide(wps, lmax)
    n = len(wps)
    pts = []
    for i in range(n):
        p0, p1, p2, p3 = wps[(i - 1) % n], wps[i], wps[(i + 1) % n], wps[(i + 2) % n]
        seglen = np.linalg.norm(p2 - p1)
        m = max(2, int(math.ceil(seglen / spacing)))
        t0 = 0.0
        t1 = t0 + max(np.linalg.norm(p1 - p0), 1e-9) ** alpha
        t2 = t1 + max(np.linalg.norm(p2 - p1), 1e-9) ** alpha
        t3 = t2 + max(np.linalg.norm(p3 - p2), 1e-9) ** alpha
        t = t1 + (t2 - t1) * (np.arange(m) / m)
        t = t[:, None]
        A1 = (t1 - t) / (t1 - t0) * p0 + (t - t0) / (t1 - t0) * p1
        A2 = (t2 - t) / (t2 - t1) * p1 + (t - t1) / (t2 - t1) * p2
        A3 = (t3 - t) / (t3 - t2) * p2 + (t - t2) / (t3 - t2) * p3
        B1 = (t2 - t) / (t2 - t0) * A1 + (t - t0) / (t2 - t0) * A2
        B2 = (t3 - t) / (t3 - t1) * A2 + (t - t1) / (t3 - t1) * A3
        C = (t2 - t) / (t2 - t1) * B1 + (t - t1) / (t2 - t1) * B2
        pts.append(C)
    return np.vstack(pts)

def resample_uniform(P, spacing, closed=True):
    """Resample a closed polyline to (approximately) uniform arclength spacing."""
    P = np.asarray(P, float)
    if closed:
        Q = np.vstack([P, P[:1]])
    else:
        Q = P
    d = np.linalg.norm(np.diff(Q, axis=0), axis=1)
    s = np.concatenate([[0.0], np.cumsum(d)])
    total = s[-1]
    m = max(8, int(round(total / spacing)))
    ss = np.linspace(0, total, m, endpoint=not closed)
    out = np.empty((len(ss), Q.shape[1]))
    for j in range(Q.shape[1]):
        out[:, j] = np.interp(ss, s, Q[:, j])
    return out

# ------------------------------------------------------------------ crossings

def find_crossings(curves2d, depths, cell=None):
    """curves2d: list of (N_i,2) closed polylines (projected); depths: list of (N_i,)
    Returns list of crossing dicts with keys: ci,si,ti, cj,sj,tj, pt, over ('i' or 'j')
    (ci,si) = component index and segment index; ti in [0,1) parameter on the segment.
    Adjacent segments of the same component are skipped."""
    segs = []  # (comp, idx, P1, P2, z1, z2)
    allP1, allP2, allz1, allz2, comp, idx = [], [], [], [], [], []
    for c, (C, Z) in enumerate(zip(curves2d, depths)):
        N = len(C)
        P1 = C
        P2 = np.roll(C, -1, axis=0)
        allP1.append(P1); allP2.append(P2)
        allz1.append(Z); allz2.append(np.roll(Z, -1))
        comp.append(np.full(N, c)); idx.append(np.arange(N))
    P1 = np.vstack(allP1); P2 = np.vstack(allP2)
    z1 = np.concatenate(allz1); z2 = np.concatenate(allz2)
    comp = np.concatenate(comp); idx = np.concatenate(idx)
    ncomp = [len(C) for C in curves2d]
    M = len(P1)
    seglen = np.linalg.norm(P2 - P1, axis=1)
    if cell is None:
        cell = max(np.percentile(seglen, 90) * 1.5, 1e-9)
    lo = np.minimum(P1, P2); hi = np.maximum(P1, P2)
    cl = np.floor(lo / cell).astype(np.int64)
    ch = np.floor(hi / cell).astype(np.int64)
    buckets = defaultdict(list)
    for k in range(M):
        for ix in range(cl[k, 0], ch[k, 0] + 1):
            for iy in range(cl[k, 1], ch[k, 1] + 1):
                buckets[(ix, iy)].append(k)
    # candidate pairs (vectorised per bucket; deduplicated with integer keys)
    keys = []
    for key, lst in buckets.items():
        if len(lst) < 2:
            continue
        arr = np.array(lst, dtype=np.int64)
        ia, ib = np.triu_indices(len(arr), 1)
        a = arr[ia]; b = arr[ib]
        swap = a > b
        a2 = np.where(swap, b, a); b2 = np.where(swap, a, b)
        same = comp[a2] == comp[b2]
        Nc = np.array([ncomp[c] for c in comp[a2]])
        di = (idx[a2] - idx[b2]) % Nc
        adjacent = same & ((di == 0) | (di == 1) | (di == Nc - 1))
        keep = ~adjacent
        keys.append(a2[keep] * M + b2[keep])
    if not keys:
        return []
    keys = np.unique(np.concatenate(keys))
    ka = keys // M; kb = keys % M
    d1 = P2[ka] - P1[ka]; d2 = P2[kb] - P1[kb]
    r = P1[kb] - P1[ka]
    denom = d1[:, 0] * d2[:, 1] - d1[:, 1] * d2[:, 0]
    ok = np.abs(denom) > 1e-14 * (seglen[ka] * seglen[kb] + 1e-300)
    t = np.where(ok, (r[:, 0] * d2[:, 1] - r[:, 1] * d2[:, 0]) / np.where(ok, denom, 1.0), -1)
    u = np.where(ok, (r[:, 0] * d1[:, 1] - r[:, 1] * d1[:, 0]) / np.where(ok, denom, 1.0), -1)
    hit = ok & (t >= 0) & (t < 1) & (u >= 0) & (u < 1)
    out = []
    for q in np.nonzero(hit)[0]:
        a, b = ka[q], kb[q]
        pt = P1[a] + t[q] * d1[q]
        za = z1[a] + t[q] * (z2[a] - z1[a])
        zb = z1[b] + u[q] * (z2[b] - z1[b])
        if abs(za - zb) < 1e-9:
            raise RuntimeError("degenerate crossing (equal depth) at %s" % pt)
        out.append(dict(ci=int(comp[a]), si=int(idx[a]), ti=float(t[q]),
                        cj=int(comp[b]), sj=int(idx[b]), tj=float(u[q]),
                        pt=pt.copy(), over='i' if za > zb else 'j',
                        di=d1[q].copy(), dj=d2[q].copy(), dz=float(za - zb)))
    return out

def pd_from_curves(curves3d, rot=None, return_info=False):
    """Generic projection of closed 3D polylines -> PD code.
    rot: 3x3 rotation applied before projecting along z (viewer at +z).
    Returns pd (list of [a,b,c,d]), signs, comps (list of edge-label lists), lk matrix."""
    if rot is None:
        rot = np.eye(3)
    curves = [np.asarray(C, float) @ rot.T for C in curves3d]
    curves2d = [C[:, :2] for C in curves]
    depths = [C[:, 2] for C in curves]
    xs = find_crossings(curves2d, depths)
    # passages per component: (position, crossing id, role)
    passages = [[] for _ in curves]
    for cid, x in enumerate(xs):
        passages[x['ci']].append((x['si'] + x['ti'], cid, 'i'))
        passages[x['cj']].append((x['sj'] + x['tj'], cid, 'j'))
    # edge labels
    offset = 0
    comps = []
    # for each crossing passage: in-label, out-label, direction
    inlab = {}; outlab = {}
    for c, plist in enumerate(passages):
        plist.sort()
        m = len(plist)
        if m == 0:
            raise RuntimeError("component %d has no crossings; PD cannot represent it" % c)
        labels = [offset + j + 1 for j in range(m)]
        comps.append(labels)
        for j, (pos, cid, role) in enumerate(plist):
            # edge from passage j to j+1 has label labels[j]; incoming edge of passage j is labels[j-1]
            inlab[(cid, role)] = labels[(j - 1) % m]
            outlab[(cid, role)] = labels[j]
        offset += m
    pd = []
    signs = []
    ncomp = len(curves)
    lk = np.zeros((ncomp, ncomp))
    for cid, x in enumerate(xs):
        if x['over'] == 'i':
            over, under = 'i', 'j'
            o_dir, u_dir = x['di'], x['dj']
            oc, uc = x['ci'], x['cj']
        else:
            over, under = 'j', 'i'
            o_dir, u_dir = x['dj'], x['di']
            oc, uc = x['cj'], x['ci']
        a = inlab[(cid, under)]; cc = outlab[(cid, under)]
        oi = inlab[(cid, over)]; oo = outlab[(cid, over)]
        cr = o_dir[0] * u_dir[1] - o_dir[1] * u_dir[0]   # (o x u)_z
        if cr > 0:
            sign = +1
            b, d = oo, oi     # over runs d->b
        else:
            sign = -1
            b, d = oi, oo     # over runs b->d
        pd.append([a, b, cc, d])
        signs.append(sign)
        if oc != uc:
            lk[oc, uc] += sign / 2.0
            lk[uc, oc] += sign / 2.0
    if return_info:
        return pd, signs, comps, lk, xs
    return pd, signs, comps, lk

def rotation_matrix(ax, ay, az=0.0):
    """Rotation about x by ax, then about y by ay, then about z by az."""
    cx, sx = math.cos(ax), math.sin(ax)
    cy, sy = math.cos(ay), math.sin(ay)
    cz, sz = math.cos(az), math.sin(az)
    Rx = np.array([[1, 0, 0], [0, cx, -sx], [0, sx, cx]])
    Ry = np.array([[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]])
    Rz = np.array([[cz, -sz, 0], [sz, cz, 0], [0, 0, 1]])
    return Rz @ Ry @ Rx

# ------------------------------------------------------------------ symmetric knot lift

def bump(u):
    """C^2 bump on (-1,1): (1-u^2)^3."""
    out = np.zeros_like(u)
    m = np.abs(u) < 1
    out[m] = (1 - u[m] ** 2) ** 3
    return out

def lift_symmetric(P2, markers, h, width, verify_mirror=True):
    """P2: (N,2) uniformly sampled closed planar curve (mirror symmetric about x=0).
    markers: list of (x, y, (ux,uy)) : crossing location and the over-strand direction.
    Returns K (N,3), list of crossing info, and the mirror index map."""
    N = len(P2)
    xs = find_crossings([P2], [np.zeros(N)]) if False else None
    # crossings of the planar curve (depth irrelevant here: use index as fake depth)
    fake = np.arange(N, dtype=float)
    xs = find_crossings([P2], [fake])
    if len(xs) != len(markers):
        raise RuntimeError("found %d planar crossings but %d markers" % (len(xs), len(markers)))
    z = np.zeros(N)
    used = [False] * len(xs)
    spacing = np.linalg.norm(P2[1] - P2[0])
    wid_idx = width / spacing
    info = []
    for (mx, my, (ux, uy)) in markers:
        dmin, best = 1e9, None
        for q, x in enumerate(xs):
            dd = math.hypot(x['pt'][0] - mx, x['pt'][1] - my)
            if dd < dmin:
                dmin, best = dd, q
        if dmin > 0.25 or used[best]:
            raise RuntimeError("marker (%g,%g) not matched (dmin=%g, used=%s)" % (mx, my, dmin, used[best]))
        used[best] = True
        x = xs[best]
        u = np.array([ux, uy], float); u /= np.linalg.norm(u)
        di = x['di'] / np.linalg.norm(x['di']); dj = x['dj'] / np.linalg.norm(x['dj'])
        ci, cj = abs(di @ u), abs(dj @ u)
        if ci > 0.8 and cj < 0.6:
            over_pos, under_pos = x['si'] + x['ti'], x['sj'] + x['tj']
        elif cj > 0.8 and ci < 0.6:
            over_pos, under_pos = x['sj'] + x['tj'], x['si'] + x['ti']
        else:
            raise RuntimeError("marker direction ambiguous at (%g,%g): %g %g" % (mx, my, ci, cj))
        idx = np.arange(N, dtype=float)
        for pos, sgn in ((over_pos, +1), (under_pos, -1)):
            dd = (idx - pos + N / 2) % N - N / 2
            z += sgn * h * bump(dd / wid_idx)
        info.append(dict(pt=x['pt'], over_pos=over_pos, under_pos=under_pos))
    K = np.column_stack([P2[:, 0], P2[:, 1], z])
    mirror = None
    if verify_mirror:
        # find index map k -> k' with P[k'] = (-x, y)
        # by construction the sampled set is mirror-symmetric; locate via nearest point of first few.
        tau2 = np.column_stack([-P2[:, 0], P2[:, 1]])
        # match k=0
        d0 = np.linalg.norm(P2 - tau2[0], axis=1)
        k0 = int(np.argmin(d0))
        # candidate maps: k' = (k0 - k) mod N  (orientation reversing)
        cand = (k0 - np.arange(N)) % N
        err = np.linalg.norm(P2[cand] - tau2, axis=1).max()
        if err > 1e-6:
            raise RuntimeError("planar curve not mirror symmetric: err %g" % err)
        zerr = np.abs(z[cand] + z).max()
        if zerr > 1e-6:
            raise RuntimeError("lift not tau-symmetric: z err %g" % zerr)
        mirror = cand
    # verify over/under separation at each crossing
    for x in info:
        zo = np.interp(x['over_pos'], np.arange(N), z)  # approx
        zu = np.interp(x['under_pos'], np.arange(N), z)
        if not (zo > zu + 0.5 * h):
            raise RuntimeError("bad z separation at crossing %s: %g %g" % (x['pt'], zo, zu))
    return K, info, mirror

def tangents(K):
    T = np.roll(K, -1, axis=0) - np.roll(K, 1, axis=0)
    T /= np.linalg.norm(T, axis=1)[:, None]
    return T

def vertical_normal(K):
    T = tangents(K)
    ez = np.array([0, 0, 1.0])
    v = ez[None, :] - (T @ ez)[:, None] * T
    nrm = np.linalg.norm(v, axis=1)
    if nrm.min() < 0.3:
        raise RuntimeError("tangent too vertical somewhere: min |v| = %g" % nrm.min())
    return v / nrm[:, None], T

def smoothstep(s):
    s = np.clip(s, 0, 1)
    return s * s * s * (s * (6 * s - 15) + 10)   # C^2 quintic step

def plateau_profile(u, u1=0.08, u2=0.38):
    """S(u) on [0,1] with S(1-u) = 1-S(u): rises 0 -> 1/2 on [u1,u2], flat 1/2 on
    [u2, 1-u2], rises 1/2 -> 1 on [1-u2, 1-u1].  Twisting is kept away from the
    middle of the interval (the fixed point)."""
    u = np.asarray(u, float)
    out = np.empty_like(u)
    lo = u <= 0.5
    out[lo] = 0.5 * smoothstep((u[lo] - u1) / (u2 - u1))
    out[~lo] = 1.0 - 0.5 * smoothstep(((1.0 - u[~lo]) - u1) / (u2 - u1))
    return out

def corrected_normal(K, mirror, interval, kturns):
    """Rotate the vertical normal right-handedly about T by the angle
    theta = 2*pi*kturns*S(u) along a tau-SYMMETRIC index interval [ia, ib] through a
    fixed point (mirror[ia] == ib).  Since S(1-u) = 1 - S(u), theta(tau p) = 2 pi k - theta(p),
    so the field stays anti-equivariant for every integer kturns (odd included).
    The framing of K + eps v' is  writhe + kturns."""
    v, T = vertical_normal(K)
    N = len(K)
    ia, ib = interval
    if abs(int(mirror[ia]) - ib) > 1:
        raise RuntimeError("interval not tau-symmetric: mirror[%d]=%d != %d" % (ia, mirror[ia], ib))
    vp = v.copy()
    if kturns != 0:
        ks = np.arange(ia, ib + 1)
        th = 2 * math.pi * kturns * plateau_profile((ks - ia) / float(ib - ia))
        Tk = T[ks]; vk = v[ks]
        cross = np.cross(Tk, vk)
        vp[ks] = np.cos(th)[:, None] * vk + np.sin(th)[:, None] * cross
    err = np.abs(vp[mirror] + vp * np.array([-1, 1, -1])).max()
    if err > 1e-5:
        raise RuntimeError("normal field not anti-equivariant: %g" % err)
    # also check it is a unit normal field
    assert np.abs(np.einsum('ij,ij->i', vp, T)).max() < 1e-6
    return vp, T

TAU = np.array([-1.0, 1.0, -1.0])

def quotient(P):
    x, y, z = P[:, 0], P[:, 1], P[:, 2]
    return np.column_stack([x * x - z * z, y, 2 * x * z])

def axis_curve(L, margin=3.0, seg=0.5):
    """B = y-axis from -R to R (R beyond L's y-extent), closed by a rectangle far on the
    left (x' < -(|x'|max + margin)), all at z'=0.  Oriented upwards along the axis.
    Segments of length ~seg so the grid intersection finder stays efficient."""
    R = float(np.abs(L[:, 1]).max() + margin)
    Rleft = float(np.abs(L[:, 0]).max() + margin)
    pts = [(0, -R, 0), (0, R, 0), (-Rleft, R, 0), (-Rleft, -R, 0)]
    out = []
    for i in range(4):
        p, q = np.array(pts[i], float), np.array(pts[(i + 1) % 4], float)
        n = max(2, int(np.ceil(np.linalg.norm(q - p) / seg)))
        for t in np.arange(n) / n:
            out.append(p + t * (q - p))
    return np.array(out)

def gauss_linking(C1, C2):
    """Numerical Gauss linking integral for two closed polylines (for a sanity check)."""
    # midpoint rule on segments (fine sampling assumed)
    A = C1; B = C2
    dA = np.roll(A, -1, axis=0) - A; dB = np.roll(B, -1, axis=0) - B
    mA = A + 0.5 * dA; mB = B + 0.5 * dB
    tot = 0.0
    chunk = 100
    for i in range(0, len(A), chunk):
        r = mA[i:i + chunk, None, :] - mB[None, :, :]
        n3 = np.linalg.norm(r, axis=2) ** 3
        cr = np.cross(dA[i:i + chunk, None, :], dB[None, :, :])
        tot += np.sum(np.sum(cr * r, axis=2) / n3)
    return tot / (4 * math.pi)
