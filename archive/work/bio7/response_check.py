"""Exact Laurent checks for a processive two-strand synapse (stdlib)."""
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'generic'))
from tangle_unit_check import add,mul,shift,neg,pairmul,ONE,ZERO,DELTA
B=({1:1},{-1:1}); BI=({-1:1},{1:1})
def power(n):
    out=(ONE,ZERO)
    for _ in range(abs(n)):out=pairmul(out,B if n>=0 else BI)
    return out
def close(T):return add(mul(DELTA,T[0]),T[1])
def normalized_braid(n):return shift(close(power(n)),-3*n,-1 if n%2 else 1)
det=add({3:1},neg(shift(DELTA,-3)))
assert det==shift(add(mul(DELTA,DELTA),neg(ONE)),-1)
tests=[]
for i in range(-7,8):
    for j in range(-5,6):
        T=pairmul(power(i),power(j)[::-1])
        F={n:close(pairmul(T,power(n))) for n in range(-5,7)}
        for n in range(-5,5):
            assert F[n+2]==add(mul({1:1,-3:-1},F[n+1]),shift(F[n],-2))
        assert mul(det,T[0])==neg(add(shift(F[0],-3),F[1]))
        assert mul(det,T[1])==add(shift(F[0],3),mul(DELTA,F[1]))
        tests.append([i,j])
u_before=normalized_braid(1); u_reverse=normalized_braid(-1)
trefoil=normalized_braid(3)
assert u_before==u_reverse==ONE
assert trefoil=={-4:1,-12:1,-16:-1}
out={'tested_tangles':len(tests),'recurrence_instances':10*len(tests),
     'reconstruction_determinant':det,'unknot_base':u_before,
     'unknot_negative_full_twist':u_reverse,
     'positive_full_twist_trefoil_A':trefoil,
     'positive_full_twist_trefoil_t':{1:1,3:1,4:-1}}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
