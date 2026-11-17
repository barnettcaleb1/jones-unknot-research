"""Raw-marking check of Section 8 for arbitrary bodies, a=-3..3 (odd AND even), no normalisation:
   A^(8a) <Theta_a(B)> / Delta2  ==  sum_c lambda_c^a K_c(a_raw, b_raw)      (8.4)
with (a_raw,b_raw) computed independently from the body tangle by the TL3 sandwich p T p = c1 p + c_e U
(a = T_I + T_e1 Delta2/delta, b = T_I), and <Theta_a> computed by the direct colored evaluator (f2 on
the arc and on the l1 band).  Also checks: closure s.B gives a_raw*Delta2 (my evaluator), flat_search
y(s.B) == a_raw, and partial trace F_0 == a + (t+1/t) b."""
import sys, json, random
from r2lib import *
def lam2(a): return mono(4*a, (-1)**(a%2))      # (-t)^a
def lam4(a): return mono(12*a)                  # t^(3a)
T1=mono(4); T2=mono(8); TINV=mono(-4)
def R_of(a, da, db):
    r = pmul(T1, da)
    r = padd(r, pmul(lam2(a), padd(pmul(padd(ONE,T2), da), pmul(T1, db))))
    r = padd(r, pmul(lam4(a), pmul(pmul(TINV, PHI5), db)))
    return r
def vword(B,a):
    tw=('x2.' if a>0 else 'y2.')*abs(a)
    return 's.l1.'+(B+'.' if B else '')+tw+'u1'
def check_body(B, arange=range(-3,4), verbose=False):
    da, db = body_ab(B) if B else (DELTA, DELTA)
    res = {}
    # closure s.B: delta*<Theta> == Delta2 * (delta a)
    v,k = theta_eval('s.'+B if B else 's.')
    res['sB'] = (v == pmul(DELTA2, da))
    if B:
        y,x = fs.bracket_vector(alex.parse('s.'+B))
        res['flat_y'] = (pmul(DELTA, y) == da)
    for a in arange:
        v,k = theta_eval(vword(B,a), extra=[(1,4)])
        assert k==2
        lhs = pmul(pmul(mono(8*a), v), PHI3)
        rhs = pmul(pmul(DELTA, DELTA2), R_of(a, da, db))
        res[a] = (lhs == rhs)
    # partial trace F0 = a + (t + 1/t) b  <=>  delta*F0 = da + (t+1/t) db
    v,k = theta_eval(vword(B,0), extra=[(1,4)])   # delta^2 <Theta_0>
    lhs = v
    rhs = pmul(pmul(DELTA, DELTA2), padd(da, pmul({4:1,-4:1}, db)))
    res['ptrace'] = (lhs == rhs)
    return res, da, db
if __name__=='__main__':
    L=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/general_boxes.json'))
    bodies=['', 'y0', 'x0', 'y0.y0', 'x0.x0.x0', 'r1.y0.y2.u1', 'l1.x0.x2.u1', 'r1.y0.y2.r1.y0.y2.u1.u1']+[B for B,_ in L[:int(sys.argv[1]) if len(sys.argv)>1 else 6]]
    for B in bodies:
        res,da,db=check_body(B)
        print(repr(B), all(res.values()), res if not all(res.values()) else '')
