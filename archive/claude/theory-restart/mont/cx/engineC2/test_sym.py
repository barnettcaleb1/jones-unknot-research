import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import theta, sym, lp
def pal(J): return J=={-e:c for e,c in J.items()}
for m in range(-3,4):
    for B in ['', 'y0', 'x0', 'r2.x1.u1', 'r2.x1.y0.u1', 'y0.r2.x1.u1', 'r2.y1.y0.y0.u1']:
        ev=sym.symmetric(sym.Sneck_top(m,B))
        J=theta.J_events(ev)
        print(m, repr(B), 'J=',sorted(J.items()) if J else J, 'pal' if J and pal(J) else 'NOT PAL', 'span',lp.span(J) if J else None)
