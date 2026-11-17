"""Exact finite-jet obstruction proving the full Laurent channel is never zero.

This uses Taylor coefficients to prove nonvanishing, not to infer equality.
"""
from pathlib import Path
from fractions import Fraction as Q
import contextlib,io,runpy,math,json
with contextlib.redirect_stdout(io.StringIO()):
    data=runpy.run_path(str(Path(__file__).with_name('tangle_three_site_locus.py')))

# Convert A^2 times a Laurent polynomial in x=-A^-4 to its x form.
# Every term has exponent alpha*p+beta*q+gamma*r+constant.
terms=[]
for powers,f in data['Fs'].items():
    for e,c in f.items():
        k=(e-2)//4
        assert e==4*k+2
        terms.append((*powers,-k,c*(-1 if k%2 else 1)))

def multiply(a,b):
    out={}
    for e,x in a.items():
        for f,y in b.items():
            n=tuple(u+v for u,v in zip(e,f))
            out[n]=out.get(n,Q(0))+x*y
    return {e:c for e,c in out.items() if c}

coefficients=[]
for order in range(4):
    out={}
    for p,q,r,c,w in terms:
        value={(0,0,0):Q(w,math.factorial(order))}
        for j in range(order):
            value=multiply(value,{(1,0,0):p,(0,1,0):q,(0,0,1):r,(0,0,0):c-j})
        for exponent,a in value.items():out[exponent]=out.get(exponent,Q(0))+a
    coefficients.append({e:c for e,c in out.items() if c})
assert coefficients[:2]==[{},{}]
assert coefficients[2]=={(1,0,0):Q(25),(0,1,0):Q(25)}
substituted={}
for (p,q,r),c in coefficients[3].items():
    exponent=(p+q,r)
    substituted[exponent]=substituted.get(exponent,Q(0))+c*(-1 if q%2 else 1)
substituted={e:c for e,c in substituted.items() if c}
assert substituted=={(2,0):Q(25),(1,0):Q(60),(0,0):Q(59)}

result={'normalized_channel':'N(x)=A^-2 delta^2 A^(-p-q-r) [z^2] bracket, x=-A^-4',
        'coefficient_of_(x-1)^2':'25(p+q)',
        'coefficient_of_(x-1)^3':'25/2*(p^2+q^2)+35/2*p-85/2*q+59-8*r*(p+q)',
        'after_q_equals_minus_p':'25*p^2+60*p+59=(5*p+6)^2+23',
        'conclusion':'For every integer p,q,r the z^2 channel is nonzero.',
        'proof':'An identically zero Laurent polynomial would have both Taylor coefficients zero. The first forces q=-p and then the second is strictly positive.',
        'exact_affine_x_monomials':terms}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k!='exact_affine_x_monomials'},indent=2))
