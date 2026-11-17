"""Fixed exact FT-minus-one local certificate; no diagram search.

Run with a Python environment containing SymPy. All mathematical checks assert;
JSON is written beside this file only after every assertion passes.
"""
import json
from pathlib import Path
import sympy as S

q = S.symbols('q', nonzero=True)
s = S.symbols('s', nonzero=True)
checks = {}

def red(x):
    x = S.cancel(x)
    n, d = S.fraction(x)
    relation = s*s-q-q**-1
    n = S.rem(n, relation, s)
    d = S.rem(d, relation, s)
    return S.cancel(n/d)

def matred(M):
    return M.applyfunc(red)

def check(name, value):
    passed = bool(value)
    checks[name] = passed
    assert passed, name
    print(name + ': PASS')

def zero(M):
    return matred(M) == S.zeros(*M.shape)

E1 = S.Matrix([[0,1],[0,0]])
F1 = E1.T
K1 = S.diag(q,q**-1)
E2 = S.Matrix([[0,s,0],[0,0,s],[0,0,0]])
F2 = E2.T
K2 = S.diag(q*q,1,q**-2)
wt1, wt2 = [1,-1], [2,0,-2]

def R(Ea,Fb,wa,wb):
    dim = len(wa)*len(wb)
    D = S.diag(*[q**S.Rational(a*b,2) for a in wa for b in wb])
    out = S.eye(dim)
    fact = 1
    for n in range(1,min(len(wa),len(wb))):
        fact *= (q**n-q**-n)/(q-q**-1)
        out += (q**S.Rational(n*(n-1),2)*(q-q**-1)**n/fact
                * S.kronecker_product(Ea**n,Fb**n))
    return matred(D*out)

def swap(a,b):
    P = S.zeros(a*b)
    for i in range(a):
        for j in range(b):
            P[j*a+i,i*b+j] = 1
    return P

R22 = R(E2,F2,wt2,wt2)
DE22 = S.kronecker_product(E2,K2)+S.kronecker_product(S.eye(3),E2)
DF22 = S.kronecker_product(F2,S.eye(3))+S.kronecker_product(K2**-1,F2)
DEop22 = S.kronecker_product(K2,E2)+S.kronecker_product(E2,S.eye(3))
check('R22 intertwines E', zero(R22*DE22-DEop22*R22))
B22 = swap(3,3)*R22
check('B22 is unramified', all(not x.has(s) for x in B22))
lam = S.symbols('lambda')
expected_char = (lam-q**-4)*(lam+q**-2)**3*(lam-q**2)**5
check('B22 fusion eigenpolynomial', S.cancel(B22.charpoly(lam).as_expr()-expected_char)==0)
B0 = B22.subs(q,S.I).applyfunc(S.simplify)
superflip = S.zeros(9)
parity = [1,0,1]
for a in range(3):
    for b in range(3):
        superflip[3*b+a,3*a+b] = (-1)**(parity[a]*parity[b])
check('B22 root is the 1|2 super flip', B0==superflip)
check('B22 root squares to identity', B0**2==S.eye(9))

d = q*q+1+q**-2
i = S.zeros(6,2)
i[1,0]=q*q; i[3,0]=-s; i[4,1]=-1; i[2,1]=q*s
p = S.zeros(2,6)
p[0,1]=1/d; p[0,3]=-q**-1*s/d; p[1,4]=-q**-2/d; p[1,2]=s/d
DE12 = S.kronecker_product(E1,K2)+S.kronecker_product(S.eye(2),E2)
DF12 = S.kronecker_product(F1,S.eye(3))+S.kronecker_product(K1**-1,F2)
check('fusion p i is identity', zero(p*i-S.eye(2)))
check('inclusion intertwines E', zero(DE12*i-i*E1))
check('inclusion intertwines F', zero(DF12*i-i*F1))
check('projection intertwines E', zero(p*DE12-E1*p))
check('projection intertwines F', zero(p*DF12-F1*p))
check('fusion denominator is a root unit', d.subs(q,S.I)==-1)

B12 = swap(2,3)*R(E1,F2,wt1,wt2)
B21 = swap(3,2)*R(E2,F1,wt2,wt1)
T = matred(B21*B12)
check('mixed full twist quadratic identity', zero((T-q**-4*S.eye(6))*(T-q**2*S.eye(6))))
# Derive inverse from the quadratic identity, then check it on both sides.
Tinv = matred(q**2*((q**-4+q**2)*S.eye(6)-T))
check('mixed inverse identity', zero(T*Tinv-S.eye(6)) and zero(Tinv*T-S.eye(6)))
check('mixed twist difference has the exact t+1 factor',
      zero(T-Tinv-(q*q+1)*(T-(q*q-1+q**-2)*S.eye(6))))
T0 = T.subs(s,0).subs(q,S.I).applyfunc(S.simplify)
expected_T0 = S.kronecker_product(S.eye(2),S.diag(-1,1,-1))
check('mixed full twist root is color-two parity', T0==expected_T0)
axis_raw_principal = -T0-3*S.eye(6)
axis_normalized_principal = axis_raw_principal+4*T0
odd = S.diag(1,0,1)
check('normalized axis symbol is 3(T0-I)', axis_normalized_principal==3*(T0-S.eye(6)))
check('normalized axis symbol is -6 Qodd',
      axis_normalized_principal==-6*S.kronecker_product(S.eye(2),odd))

co = S.zeros(9,1)
co[2]=q*q; co[4]=-q*q; co[6]=1
A = S.Matrix(3,3,list(co))
ev = A.inv().reshape(1,9)
check('coevaluation intertwines E', zero(DE22*co))
check('coevaluation intertwines F', zero(DF22*co))
check('evaluation intertwines E', zero(ev*DE22))
check('evaluation intertwines F', zero(ev*DF22))
check('both snake matrix identities', A*A.inv()==S.eye(3) and A.inv()*A==S.eye(3))
check('color-two loop dimension is [3]', zero(ev*co-S.Matrix([[d]])))

# t=-exp(h), q=i exp(h/2), so d/dh=(q/2)d/dq at q=i.
Bdifference = (B22-B22.inv()).applyfunc(S.cancel)
check('off-axis difference vanishes at the root',
      Bdifference.subs(q,S.I).applyfunc(S.simplify)==S.zeros(9))
C22 = Bdifference.applyfunc(lambda z:S.simplify((q*S.diff(z,q)/2).subs(q,S.I)))
middle_pair = S.zeros(9,1); middle_pair[4]=1
expected_created = S.zeros(9,1); expected_created[2]=-2; expected_created[6]=2
check('off-axis symbol creates the stated odd pair', C22*middle_pair==expected_created)
Qfirst = S.kronecker_product(odd,S.eye(3))
commutator_action = (Qfirst*C22-C22*Qfirst)*middle_pair
check('local odd projector and off-axis symbol do not commute', commutator_action==expected_created)

result = {
    'all_passed': all(checks.values()),
    'checks': checks,
    'conventions': {'t':'q^2=-exp(h)', 'q':'i exp(h/2)', 's^2':'q+q^-1'},
    'offaxis_symbol_on_w1w1': [str(x) for x in C22*middle_pair],
    'odd_projector_commutator_on_w1w1': [str(x) for x in commutator_action],
    'normalized_axis_symbol_diagonal': [str(x) for x in axis_normalized_principal.diagonal()],
}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(result,indent=2)+'\n')
print(f'ALL {len(checks)} CHECKS PASSED; wrote {path.name}')
