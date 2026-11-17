"""Exact root-ring reflection checks and an actual-knot reconstruction test."""
from pathlib import Path
from fractions import Fraction
import sys,json,math
ROOT=Path(__file__).resolve().parents[2]
checks=0
derivative_checks=0
def laurent_mul(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items():out[i+j]=out.get(i+j,0)+x*y
    return {i:x for i,x in out.items() if x}
for r in range(3,15):
    # Work exactly in Z[q]/(q^r-1), a stronger check than reduction
    # modulo only the primitive-root cyclotomic factor.
    def plus(a,b):return tuple(x+y for x,y in zip(a,b))
    def scale(a,c):return tuple(c*x for x in a)
    def times(a,b):
        out=[0]*r
        for i,x in enumerate(a):
            for j,y in enumerate(b):out[(i+j)%r]+=x*y
        return tuple(out)
    def qp(n):return tuple(int(i==n%r) for i in range(r))
    def value(N):
        # Deliberately arbitrary integral Laurent cyclotomic coefficients.
        total=qp(0);term=qp(0)
        for k in range(1,N):
            factor=plus(plus(qp(N),qp(-N)),scale(plus(qp(k),qp(-k)),-1))
            term=times(term,factor)
            coeff=plus(scale(qp(k),k+1),scale(qp(-k),-k))
            total=plus(total,times(term,coeff))
        return total
    for n in range(1,r):
        assert value(n)==value(r-n)==value(r+n)
        checks+=2
    if r>=5:
        N=r-2;total={0:1};term={0:1}
        for k in range(1,N):
            term=laurent_mul(term,{N:1,-N:1,k:-1,-k:-1})
            for e,c in term.items():total[e]=total.get(e,0)+c
        direct=[0]*r
        for e,c in total.items():direct[(e-1)%r]+=e*c
        d1=plus(scale(plus(qp(-3),scale(qp(1),-1)),r-2),
                scale(plus(qp(0),scale(qp(-2),-1)),-1))
        d2=scale(plus(qp(-3),scale(qp(1),-1)),r)
        f1=plus(plus(qp(2),qp(-2)),scale(plus(qp(1),qp(-1)),-1))
        prod=qp(0);Q=qp(0)
        for j in range(3,r-2):
            prod=times(prod,plus(plus(qp(2),qp(-2)),scale(plus(qp(j),qp(-j)),-1)))
            Q=plus(Q,prod)
        assert tuple(direct)==plus(d1,times(times(f1,d2),Q))
        derivative_checks+=1

sys.path.insert(0,str(ROOT/'creative6'))
from quantum_two_copy_test import colored,WORDS,search
ordinary=[search.jones_a(WORDS['5_1'],2),search.jones_a(WORDS['10_132'],5)]
assert ordinary[0]==ordinary[1]
spinone=[colored(WORDS['5_1'],2),colored(WORDS['10_132'],5)]
assert spinone==[Fraction(208357048576),Fraction(12565016366179,4)]
assert spinone[0]!=spinone[1]

table=[]
for r in [10,20,40,80,160,320]:
    # Figure-eight Habiro coefficients are all1. At color r the
    # cyclotomic factors are the positive numbers4sin²(pi*j/r).
    term=1.0;total=1.0
    for j in range(1,r):
        term*=4*math.sin(math.pi*j/r)**2
        total+=term
    near=1+2*math.cos(4*math.pi/r)-2*math.cos(2*math.pi/r)
    theta=math.pi/r
    f1=2*math.cos(4*theta)-2*math.cos(2*theta)
    Q=1.0;Qsum=1.0
    for j in range(3,r-2):
        Q*=4*math.sin((j-2)*theta)*math.sin((j+2)*theta)
        Qsum+=Q
    # derivative=(-2i/zeta)*real_derivative_coefficient
    derivative_coefficient=(r-2)*math.sin(4*theta)+math.sin(2*theta)+f1*r*math.sin(4*theta)*Qsum
    derivative_abs=2*abs(derivative_coefficient)
    table.append({'r':r,'color_r_minus_1':1,
        'color_r_minus_2':near,
        '2pi_log_abs_color_r_minus_2_over_r':2*math.pi*math.log(abs(near))/r if near else '-infinity',
        '2pi_log_abs_first_derivative_color_r_minus_2_over_r':2*math.pi*math.log(derivative_abs)/r,
        '2pi_log_color_r_over_r':2*math.pi*math.log(total)/r})
out={'exact_reflection_checks':checks,'exact_derivative_identity_checks':derivative_checks,
    'actual_knots':{'braids':WORDS,'ordinary_Jones_A':ordinary[0],
      'color3_at_quantum_group_q2':list(map(str,spinone)),
      'consequence':'All orders r give equal colors r±1 andr±2 at primitive rth roots, although color3 differs as a Laurent polynomial.'},
    'figure_eight_boundary_layer':table}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
