"""Cancellation analysis of near misses: tropical (max-plus/min-plus) prediction of the extreme degrees of
PHI.rho(W).v versus the actual ones; per-step local cancellation events (step, letter, basis component, loss)."""
import sys, json, glob
from collections import Counter
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
import fastJ, rho2
def parse_hw(hw):
    toks = hw.split('.')
    assert toks[0] == 's' and toks[1:3] == ['l1', 'l1'] and toks[-2:] == ['u2', 'u2']
    return toks[3:-2]
def width_one(W):
    return all(L in ('x0', 'y0', 'x1', 'y1') for L in W)
def no_axis(W):
    return all(L not in ('x0', 'y0') for L in W)
def analyse(hw):
    W = parse_hw(hw)
    tr = fastJ.tropical('l1.l1', W, 'u2.u2')
    ev = tr['events']
    loc_top = sum(e[3] for e in ev if isinstance(e[3], int) and e[0] != 'close')
    loc_bot = sum(e[4] for e in ev if isinstance(e[4], int) and e[0] != 'close')
    close = [e for e in ev if e[0] == 'close'][0]
    comps = Counter(e[2] for e in ev if e[0] != 'close')
    lets = Counter(e[1] for e in ev if e[0] != 'close')
    return {'len': len(W), 'trop_span': tr['trop_span'], 'span_raw': tr['span'], 'deficit': tr['deficit'],
            'close_top_loss': close[3], 'close_bot_loss': close[4], 'inner_top_loss': loc_top, 'inner_bot_loss': loc_bot,
            'events_by_component': dict(comps), 'events_by_letter': dict(lets), 'width_one': width_one(W), 'no_axis': no_axis(W)}
if __name__ == '__main__':
    for hw in sys.argv[1:]:
        print(hw, analyse(hw))
