#!/usr/bin/env python3
"""
pipeline.py -- symmetric diagram -> tau-symmetric space curve -> zero-framed longitude
pair -> quotient Sakuma link -> PD code -> exact Jones polynomial.  All checks included.
"""
import sys, json, math, time
import numpy as np
sys.path.insert(0, '/private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-sak')
import kb, geom, templates

OUT = '/private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-sak/out'
import os
os.makedirs(OUT, exist_ok=True)

ROT_COVER = geom.rotation_matrix(0.45, 0.35, 0.05)
ROT_Q1 = geom.rotation_matrix(0.37, 0.29, 0.11)
ROT_Q2 = geom.rotation_matrix(-0.43, 0.33, -0.17)
ROT_Q3 = geom.rotation_matrix(0.52, -0.41, 0.23)


def best_order(pd, xs):
    """Choose the crossing absorption order with the smallest cutwidth among 12 sweep
    directions and the greedy order."""
    pts = np.array([z['pt'] for z in xs])
    pdt = [tuple(x) for x in pd]
    cands = {}
    for ang in np.linspace(0, math.pi, 12, endpoint=False):
        proj = pts[:, 0] * math.cos(ang) + pts[:, 1] * math.sin(ang)
        cands['sweep%.0f' % math.degrees(ang)] = [int(i) for i in np.argsort(proj)]
    cands['greedy'] = kb.greedy_order(pdt)
    cw = {k: kb.cutwidth(pdt, o) for k, o in cands.items()}
    best = min(cw, key=cw.get)
    return best, cands[best], cw


def pd_json(pd, signs, comps, lk):
    return dict(pd=[list(map(int, x)) for x in pd], signs=[int(s) for s in signs],
                components=[list(map(int, c)) for c in comps], lk=lk.tolist())


def run(tag, waypoints, markers, meta, spacing=0.005, h=0.4, bumpw=0.6, eps=0.1,
        rots=(ROT_Q1, ROT_Q2), extra_kinks=0, verbose=True, framing=0):
    t0 = time.time()
    log = []
    logpath = os.path.join(OUT, '%s_log.txt' % tag)
    open(logpath, 'w').close()
    def say(*a):
        s = ' '.join(str(x) for x in a)
        log.append(s)
        with open(logpath, 'a') as f:
            f.write(s + '\n')
        if verbose:
            print(s, flush=True)
    say("=== %s ===" % tag)
    # 1. planar curve
    P = geom.catmull_rom_closed(waypoints, spacing * 2)
    P = geom.resample_uniform(P, spacing)
    N = len(P)
    P = np.roll(P, N // 2, axis=0)   # move the top fixed point (waypoint 0) away from the index seam
    say("samples N=%d  length=%.2f" % (N, N * spacing))
    # 2. lift
    K, cinfo, mirror = geom.lift_symmetric(P, markers, h, bumpw)
    say("crossings matched: %d (markers %d)" % (len(cinfo), len(markers)))
    # 3. symmetric diagram PD (projection along z) -> writhe, knot Jones polynomial
    if len(markers) == 0:
        pdK, sK, cK, lkK = [], [], [[]], np.zeros((1, 1))
        x = 0
        VK = {0: 1}
        say("symmetric diagram: 0 crossings (round unknot), writhe 0")
    else:
        pdK, sK, cK, lkK = geom.pd_from_curves([K], np.eye(3))
        x = sum(sK)
        say("symmetric diagram: %d crossings, writhe x = %d" % (len(pdK), x))
        VK, wK, mxK = kb.jones_from_pd(pdK, signs=sK)
    say("Jones(K) =", kb.jones_str(VK))
    detK = abs(sum(c * ((-1) ** (k // 2)) for k, c in VK.items()))   # |V(-1)| with t^(1/2)=i -> careful
    # determinant |V_K(-1)|: t=-1 -> t^(k/2) with k even = (-1)^(k/2)
    say("det(K) = |V_K(-1)| =", detK)
    if x % 2 != 0:
        say("NOTE: odd writhe; preferred framing needs a half-integer number of turns per side -> handled by k = -x/2 turns on each side (symmetric split).")
    kturns = framing - x   # lk(K, lambda_+) = x + kturns = framing
    # 4. correction interval: the straight top run through the top fixed point, |x| < x_far - 1
    Y_TOP = meta['Y_TOP']
    idx = np.nonzero((np.abs(K[:, 1] - Y_TOP) < 1e-6) & (np.abs(K[:, 0]) < meta['x_far'] - 1.0) & (np.abs(K[:, 2]) < 1e-9))[0]
    assert len(idx) > 50, len(idx)
    gaps = np.nonzero(np.diff(idx) != 1)[0]
    assert len(gaps) == 0, "interval not contiguous"
    ia, ib = int(idx[0]), int(idx[-1])
    say("correction interval: indices %d..%d (%d samples, x from %.2f to %.2f, through the top fixed point), k = %g turns" % (ia, ib, ib - ia + 1, K[ia, 0], K[ib, 0], kturns))
    vp, T = geom.corrected_normal(K, mirror, (ia, ib), kturns)
    lam_p = K + eps * vp
    lam_m = lam_p * geom.TAU[None, :]
    lam_m = lam_m[mirror]    # tau(lambda_+) reparametrised along K's orientation
    # distances sanity: lambda+ must stay away from K's other strands: min dist between lam_p and K excluding nearby indices is ~eps
    # 5. cover linking numbers from a generic projection
    pdC, sC, cC, lkC = geom.pd_from_curves([K, lam_p, lam_m], ROT_COVER)
    say("cover projection: %d crossings; lk(K,l+)=%g lk(K,l-)=%g lk(l+,l-)=%g" % (len(pdC), lkC[0, 1], lkC[0, 2], lkC[1, 2]))
    gl = geom.gauss_linking(K[::16], lam_p[::16])
    say("Gauss integral lk(K,l+) ~ %.4f" % gl)
    framing_ok = (abs(lkC[0, 1] - framing) < 1e-9 and abs(lkC[0, 2] - framing) < 1e-9 and abs(lkC[1, 2] - framing) < 1e-9)
    if not framing_ok:
        raise RuntimeError("framing check failed: %s" % lkC.tolist())
    # 6. quotient
    L = geom.quotient(lam_p)
    Bx = geom.axis_curve(L)
    results = []
    for ri, rot in enumerate(rots):
        pdQ, sQ, cQ, lkQ, xsQ = geom.pd_from_curves([Bx, L], rot, return_info=True)
        ncomp = len(cQ)
        best, order, cw = best_order(pdQ, xsQ)
        say("  bracket order: %s (cutwidth %d; others: %s)" % (best, cw[best], sorted(set(cw.values()))))
        VQ, wQ, mxQ = kb.jones_from_pd(pdQ, signs=sQ, order=order)
        # components: B alone / L alone unknot checks via Jones of each sub-diagram? (skip; check via snappy later)
        JQ = kb.jones_to_snape_q(VQ)
        say("quotient proj %d: %d crossings (B-L: %d, L-L: %d), lk(B,L)=%g, writhe %d, maxstates %d" % (
            ri, len(pdQ), sum(1 for z in xsQ if z['ci'] != z['cj']), sum(1 for z in xsQ if z['ci'] == z['cj']), lkQ[0, 1], wQ, mxQ))
        say("  V_S(t)   =", kb.jones_str(VQ))
        say("  J_S(q)   =", kb.poly_str_q(JQ), "   [Snape normalisation, t^(1/2) = -q]")
        say("  equals 2-unlink V = -t^(1/2) - t^(-1/2)?", VQ == kb.UNLINK2)
        results.append(dict(pd=pd_json(pdQ, sQ, cQ, lkQ), V=VQ, J=JQ, ncross=len(pdQ), lkBL=float(lkQ[0, 1]), writhe=wQ))
        with open(os.path.join(OUT, '%s_sakuma_proj%d.json' % (tag, ri)), 'w') as f:
            json.dump(dict(tag=tag, pd=pd_json(pdQ, sQ, cQ, lkQ), jones_t_half_exponents=VQ,
                           jones_snape_q=JQ, V_str=kb.jones_str(VQ), J_str=kb.poly_str_q(JQ)), f, indent=1)
    allsame = all(r['V'] == results[0]['V'] for r in results)
    say("projections agree:", allsame)
    # also: unknottedness of L alone (Jones of L alone must be 1) and B alone trivially
    pdL, sL, cL, lkL, xsL = geom.pd_from_curves([L], rots[0], return_info=True)
    bestL, orderL, cwL = best_order(pdL, xsL)
    say("  L-alone bracket order: %s (cutwidth %d)" % (bestL, cwL[bestL]))
    VL, wL, mxL = kb.jones_from_pd(pdL, signs=sL, order=orderL)
    say("L alone: %d crossings, Jones(L) = %s (unknot iff 1)" % (len(pdL), kb.jones_str(VL)))
    with open(os.path.join(OUT, '%s_knot.json' % tag), 'w') as f:
        json.dump(dict(tag=tag, pd=pd_json(pdK, sK, cK, lkK), writhe=x, jones=VK, V_str=kb.jones_str(VK), det=detK,
                       cover_lk=dict(K_lp=float(lkC[0, 1]), K_lm=float(lkC[0, 2]), lp_lm=float(lkC[1, 2]))), f, indent=1)
    with open(os.path.join(OUT, '%s_log.txt' % tag), 'w') as f:
        f.write('\n'.join(log) + '\n')
    say("time %.1fs" % (time.time() - t0))
    return dict(tag=tag, VK=VK, x=x, detK=detK, framing_ok=framing_ok, VS=results[0]['V'], JS=results[0]['J'],
                ncrossS=results[0]['ncross'], lkBL=results[0]['lkBL'], allsame=allsame, VL=VL,
                unlink=(results[0]['V'] == kb.UNLINK2), log=log)


if __name__ == '__main__':
    pass
