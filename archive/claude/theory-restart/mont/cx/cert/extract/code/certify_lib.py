"""Shared certification pipeline: word reduction (reduce.py) + exact V_K (vk.py) on the reduced diagram.
status: 'CERT_c_empty'  : W reduced to the empty word by valid moves -> 0-crossing diagram (standard (c))
        'CERT_a_TS24'   : reduced diagram has <= 24 crossings and exact V_K = 1 (standard (a), Tuzun-Sikora)
        'UNRESOLVED'    : reduced diagram still has > 24 crossings
        'ALARM_V_ne_1'  : a reduced diagram with V_K != 1 (would mean a bug or a non-unknot): reported loudly"""
import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
import rules, reduce as R, vk
def halfword(w): return 's.l1.l1.' + (rules.dec(w) + '.' if w else '') + 'u2.u2'
def certify_word(w, budget=3000):
    w = tuple(w)
    r, moves = R.reduce_word(w, budget=budget)
    assert R.replay(w, moves) == r
    hw = halfword(r)
    nc = vk.ncross(hw)
    if nc is None: return {'status': 'ALARM_not_knot', 'reduced': rules.dec(r), 'moves': moves}
    if not r: st = 'CERT_c_empty'
    elif nc <= 24:
        V = vk.VK(hw)
        st = 'CERT_a_TS24' if V == {0: 1} else 'ALARM_V_ne_1'
    else: st = 'UNRESOLVED'
    return {'status': st, 'reduced': rules.dec(r), 'ncross_reduced': nc, 'moves': moves}
