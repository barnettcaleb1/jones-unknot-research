"""Fixed algebra and named calibrations; no scan.

J is lp.J with quotient t=A^4; V uses its standard bracket variable a^-4.
Uniform quotient A^-4 notation instead gives J_minus(t)=V(t^-2).
"""
from pathlib import Path
import json
import sympy as S

Q,t,z=S.symbols('Q t z')
phi5=Q**4+Q**3+Q**2+Q+1
phi10=t**4-t**3+t**2-t+1
checks={}
def check(name,condition):
    checks[name]=bool(condition)
    assert checks[name],name
def zero(x): return S.cancel(x)==0
def rem_laurent(x,var,poly):
    num,den=S.fraction(S.cancel(x))
    return S.rem(num,poly,var)

rm,rp=Q**-2,Q**3
dm,dp=1-Q-Q**-1,(Q+Q**-1)**2
check('braid parameters differ by fifth power',zero(rp-rm-Q**-2*(Q**5-1)))
check('loop parameters differ by Phi5',zero(dp-dm-Q**-2*phi5))
check('original trace channel obeys BMW',zero(Q**2-Q**-2-(Q-Q**-1)*(1-dm)))
check('cover trace channel obeys BMW',zero(Q**-3-Q**3-(Q-Q**-1)*(1-dp)))
check('Phi5 is fourth power modulo five',S.Poly(phi5-(Q-1)**4,Q,modulus=5).is_zero)
check('Phi10 is fourth power modulo five',S.Poly(phi10-(t+1)**4,t,modulus=5).is_zero)
check('change of cyclotomic variable',zero(Q**4*phi10.subs(t,-Q**-1)-phi5))
check('projector denominators agree cyclotomically',rem_laurent(Q**2-Q**-3,Q,phi5)==0)
check('boundary denominator is a cyclotomic unit',S.resultant(phi5,Q**3+1,Q)==1)
check('boundary denominators are units at Q1', (Q**2+Q**-1).subs(Q,1)==2 and (Q**-3+Q**-1).subs(Q,1)==2)

# These fixed n values check implementation/signs of the displayed all-n identity.
# Its all-n proof is Q^(5n)-1 divisibility, not extrapolation from this check.
for n in (0,1,2,3):
    lm=Q**(2*n)-(Q+Q**-1)*(-Q**-1)**n
    lp=Q**(-3*n)+(Q**2+1+Q**-2)*(-Q**-1)**n
    defect=Q**(-3*n)*(Q**(5*n)-1)-Q**-2*phi5*(-Q**-1)**n
    check(f'trace identity n={n}',zero(lm-lp-defect))
    if n:
        check(f'framed generator equality n={n}',rem_laurent(rm**(n-1)*lm-rp**(n-1)*lp,Q,phi5)==0)

# Framing equality using Q=u^2 avoids any fractional-power simplification.
u=S.symbols('u',nonzero=True)
for n in (1,2,3):
    check(f'cover curl correction n={n}',zero((-u**3)**(n-2)-u**(6*(n-1))*(-u**-3)**n))

examples=[
 ('trefoil',-t**-3+t**-4+t**-7,t+t**3-t**4),
 ('figure_eight',t**-6+t**-3-t**-2+1-t,t**-2-t**-1+1-t+t**2),
 ('8_19',-t**14+t**13+t**10-t**9+t**8,t**3+t**5-t**8),
]
for row in json.loads(Path(__file__).with_name('degree3_eta_gate.json').read_text())['rows']:
    J=sum(c*t**int(e) for e,c in row['J'].items())
    V=sum(c*t**int(e) for e,c in row['V'].items())
    examples.append((row['name'],J,V))
for name,J,V in examples:
    check(name+' preferred normalization',J.subs(t,-1)==1 and S.diff(J,t).subs(t,-1)==0)
    check(name+' exact Phi10 remainder',rem_laurent(J-V.subs(t,t*t),t,phi10)==0)

result={'all_passed':all(checks.values()),'checks':checks,
 'conventions':{'J':'lp.J, quotient t=A^4','V':'standard Jones, variable a^-4',
                'uniform_form':'J_minus(t)=J_lp(t^-1)=V_K(t^-2) modulo Phi10'},
 'scope':'Fixed algebra and named calibrations only; universal claim requires annular spanning and marked projector proof.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(f'ALL {len(checks)} CHECKS PASSED')
