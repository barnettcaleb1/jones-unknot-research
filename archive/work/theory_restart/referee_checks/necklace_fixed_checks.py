"""Two fixed algebra checks, no enumeration or search.

Requires SymPy. Checks the odd-closure inference and the P(2,3,5) calibration.
The topological identification is in necklace_skein_referee.md, not this script.
"""
import json
from pathlib import Path
import sympy as s

t = s.symbols('t')
phi = 1+t+t**2

def coefficients(f):
    f = s.expand(s.cancel(f))
    out = {}
    for term in s.Add.make_args(f):
        power = int(term.as_powers_dict().get(t, 0))
        coefficient = s.simplify(term / t**power)
        assert coefficient.is_Integer
        out[power] = out.get(power, 0) + int(coefficient)
    return dict(sorted((p,c) for p,c in out.items() if c))

# j=n=1 in the closure formula quoted by Claude120708.
Jstar = s.cancel(1+t*(t+1)*(t**-12-1)/phi)
Vstar = s.cancel(t**12*(1+(1+t**-1)*phi/(1+t)**2*(Jstar-1)))
divisibility_witness = s.cancel(t*(Jstar-1)/(1+t)**2)
assert Vstar == 1
assert Jstar.subs(t,-1) == 1
assert s.diff(Jstar,t).subs(t,-1) == 0
assert len(coefficients(Jstar)) > 1
coefficients(divisibility_witness)  # verifies it is an integral Laurent polynomial

def row(j):
    a = 1+t**-3*(1-t)*(1+t**2)*(1-(-t)**j)
    b = a+(t**-3-1)*(-t)**j
    return s.expand(a),s.expand(b)

# Two odd rows 3,5, marked special exponent mu=1: P(+2,3,5).
a,b = row(1)
c,d = row(2)
raw = s.cancel(((t+(1+t**2)*(-t))*a*c+(1+t**2)*(1+t)*b*d)/phi)
preferred = s.cancel(t**-12*raw)
assert preferred.subs(t,-1) == 1
assert s.diff(preferred,t).subs(t,-1) == 0
assert s.diff(preferred,t,2).subs(t,-1) == 0
assert len(coefficients(preferred)) == 11

result = dict(
    odd_closure_formal_J=coefficients(Jstar),
    odd_closure_divisibility_witness=coefficients(divisibility_witness),
    odd_closure_value=1,
    warning="Formal algebra counterexample to an implication; no tangle realization claimed.",
    pretzel_2_3_5_raw_J=coefficients(raw),
    pretzel_2_3_5_preferred_J=coefficients(preferred),
    pretzel_a2_from_banked_moment_identity=0,
)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
