"""Soundness probe for the Tietze certifiers: on random NONTRIVIAL knots (exact V_K != 1) neither tietze.certify_multi nor
tietze2.certify2 may ever reach <a | >; on random knots with V_K = 1 (unknots at this size) record the success rate."""
import sys, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
import tietze, tietze2, vk, rules
rnd = random.Random(2024); nontriv = 0; false_cert = 0; triv = 0; triv_ok = 0
while nontriv < 300:
    W = [rnd.choice(list(rules.CODE)) for _ in range(rnd.randint(4, 14))]
    hw = 's.l1.l1.' + '.'.join(W) + '.u2.u2'
    if vk.ncross(hw) is None: continue
    V = vk.VK(hw)
    a, _ = tietze2.certify2(hw); b, _ = tietze.certify_multi(hw, tries=4)
    if V != {0: 1}:
        nontriv += 1
        if a or b: false_cert += 1; print('FALSE CERT', hw)
    else:
        triv += 1; triv_ok += (a or b)
print('nontrivial knots', nontriv, 'false Tietze certificates', false_cert, '| V=1 knots', triv, 'Tietze-certified', triv_ok)
