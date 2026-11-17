import sys, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import relabel, theta, sym, plat2, lp
# sanity 1: half-word thetas (A1 = A_out). For a two-bridge inversion the sister is the OTHER inversion's J?  just print a few
for w in ['s.l1.y0.x1.u2','s.l1.x1.y0.u2','s.l1.y0.y0.x1.x1.u2','s.r2.y1.y1.y0.u1']:
    ev=theta.from_halfword(w); print(w,'J',lp.J(w),' sister',relabel.Jsister(ev))
# sanity 2: trivial symmetric thetas
for w in ['', 'a', 'aa', 'b','ab']:
    ev=sym.symmetric(plat2.top_events(w)); print(repr(w),'J',theta.J_events(ev),'sister',relabel.Jsister(ev))
