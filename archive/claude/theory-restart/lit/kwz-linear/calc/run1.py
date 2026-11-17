import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-linear/calc')
from hf import *

print("== special curves s_2n'(0) against arcs (rotate by 90deg to get the slope-infinity statements) ==")
for npr in (1, 2, 3):
    S = s_curve(npr)
    print(f"--- {S.name}: {len(S.idem)} generators")
    report(hf(arc0(), S), f"HF(a(0), {S.name})   [<-> (a(inf), s_{2*npr}(inf))]")
    report(hf(arcinf(), S), f"HF(a(inf), {S.name}) [<-> (a(0), s_{2*npr}(inf))]")
    for n in (1, 2, 3, 4, 5, 6):
        report(hf(arc_int(-n), S), f"HF(a({-n}), {S.name})  [<-> (a(1/{n}), s_{2*npr}(inf))]")
