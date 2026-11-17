import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-linear/calc')
from hf import *

print("== rational curves r_n'(0) against arcs (rotate by 90deg to get the slope-infinity statements) ==")
for npr in (1, 2, 3, 4):
    R = r_curve(npr)
    print(f"--- {R.name}: {len(R.idem)} generators")
    report(hf(arc0(), R), f"HF(a(0), {R.name})   [<-> (a(inf), r_{npr}(inf))]")
    report(hf(arcinf(), R), f"HF(a(inf), {R.name}) [<-> (a(0), r_{npr}(inf))]")
    for n in (1, 2, 3, 4, 5):
        report(hf(arc_int(-n), R), f"HF(a({-n}), {R.name})  [<-> (a(1/{n}), r_{npr}(inf))]")
