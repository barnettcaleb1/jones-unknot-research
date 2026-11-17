"""sign_control.py -- control: the J test discriminates the handedness in rule (R).  For the first 400 words containing
d or D (enumeration order), compare lp.J of the correct translation and of the WRONG-handed one (d -> y0.y1.y0.y1)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import translate as TR
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import enum2, plat2, lp
WR = dict(TR.T); WR['d'] = 'y0.y1.y0.y1'; WR['D'] = 'x0.x1.x0.x1'
n = ok = wrong_eq = 0
for first in 'aBd':
    for W in enum2.words(first, 5):
        if not plat2.is_arc(W) or not any(ch in 'dDcC' for ch in W): continue
        Jp = plat2.J(W)
        hw = '.'.join(['s', 'l2'] + [WR[ch] for ch in W + TR.fword(W)] + ['u1'])
        n += 1; ok += (lp.J(TR.s2_halfword_closed(W)) == Jp); wrong_eq += (lp.J(hw) == Jp)
        if n >= 400: break
    if n >= 400: break
print('words', n, 'correct-handed J equal', ok, 'wrong-handed J equal', wrong_eq)
