"""Exploratory exact bracket models; geometric shell identification is separate."""
from pathlib import Path
import runpy
ns=runpy.run_path(str(Path(__file__).resolve().parents[1]/'transmission18'/'exact_factor_certificate.py'))
add,mul,shift,power=(ns[k] for k in ('add','mul','shift','power'))
prod,integer,numerator,denominator=(ns[k] for k in ('product','integer_tangle','numerator','denominator'))
one=ns['ONE']; delta=ns['DELTA']
def rational(p,q):
    if not q: return ({},{0:1})
    if q<0:p,q=-p,-q
    n=p//q;r=p-n*q
    if not r:return integer(n)
    return prod(integer(n),rational(-q,r)[::-1])
def torus_fixed(q,base=None):
    if base is None:base=q
    r=prod(prod(integer(-1),rational(1,2)),rational(q-1,2*q))
    return prod(r[::-1],integer(-2*base))
def norm(t):
    u=denominator(t)
    assert len(u)==1,(u,t)
    (e,c),=u.items()
    assert c in (-1,1)
    return tuple(shift(p,-e,c) for p in t)
def x(t):return norm(t)[1]
def div_unit(p,q):
    assert len(q)==1
    (e,c),=q.items();assert c in (-1,1)
    return shift(p,-e,c)
def rem8(p):
    o={}
    for e,c in p.items():
        n,r=divmod(e,4)
        o[r]=o.get(r,0)+c*(-1 if n%2 else 1)
    return {e:c for e,c in o.items() if c}
def txt(p):return str(sorted(p.items()))
if __name__=='__main__':
    for q in (1,3,5,15,17,-1,-3):
        t0=torus_fixed(q)
        print('q',q,'meridian',denominator(t0),'longitude determinant remainder',rem8(numerator(t0)))
        x0=x(t0)
        for sign in (1,-1):
            # Fixed-boundary candidate based on q -> q+2n.
            y=torus_fixed(q+2*sign,base=q)
            d=div_unit(add(x(y),shift(x0,0,-1)),x(integer(sign)))
            print('sign',sign,'ddeg',min(d),max(d),'droot',rem8(d),'d',txt(d))

def cable_shell(q,t):
    assert q%2
    j=prod(integer((q-1)//2),t)
    h=prod(integer(-2),j[::-1])[::-1]
    r=prod(prod(integer(-1),rational(1,2)),h)
    return prod(r[::-1],integer(-2*q))

def scalar(p,s):return mul(p,s)

def eval_one(p):return sum(p.values())
def derivative_one(p):return sum(e*c for e,c in p.items())

if __name__=='__main__':
    for q in (1,3,5,15,17,-1,-3):
        col0=cable_shell(q,(one,{}))
        coli=cable_shell(q,({},one))
        u=denominator(col0)
        assert denominator(coli)==mul(u,delta)
        for n in (-2,-1,0,1,2):
            assert norm(cable_shell(q,integer(n)))==norm(torus_fixed(q+2*n,base=q))
        # Normalize each column by the SAME u, not by its own closure.
        (e,c),=u.items()
        nh0=tuple(shift(p,-e,c) for p in col0)
        nhi=tuple(shift(p,-e,c) for p in coli)
        x0=nh0[1]
        d=add(nhi[1],shift(mul(delta,x0),0,-1))
        expected=shift(mul({0:1,4:-1},{0:1,8:1}),6*(q-1),(-1 if ((q-1)//2)%2 else 1))
        assert d==expected,(q,d,expected)
        assert rem8(d)=={0:4}
        dprime=derivative_one(d);xprime=derivative_one(x0)
        print('DIRECT SHELL q',q,'u',u,'dprime(1)',dprime,'xprime(1)',xprime,'target x(1)',-xprime/dprime)

def quotient_remainder(a,b):
    if not a:return {},{}
    sa=min(a);sb=min(b)
    a=shift(a,-sa);b=shift(b,-sb)
    q={}
    while a and max(a)>=max(b):
        i=max(a)-max(b)
        assert a[max(a)]%b[max(b)]==0
        c=a[max(a)]//b[max(b)]
        q[i]=q.get(i,0)+c
        a=add(a,shift(b,i,-c))
    return shift(q,sa-sb),shift(a,sa)

if __name__=='__main__':
    for q in (1,3,5,15,17,-1,-3):
        c0=cable_shell(q,(one,{}));ci=cable_shell(q,({},one))
        (e,c),=denominator(c0).items()
        a=shift(c0[1],-e,c)
        d=add(shift(ci[1],-e,c),shift(mul(delta,a),0,-1))
        quot,rem=quotient_remainder(a,d)
        assert not rem, (q,rem)
        s=-1 if ((q-1)//2)%2 else 1
        assert eval_one(quot)==(1-s*q)//2
        assert derivative_one(a)==4*(q-s)
        next_col=cable_shell(q+2,(one,{}))
        next_a=norm(next_col)[1]
        next_d=shift(mul({0:1,4:-1},{0:1,8:1}),6*(q+1),-s)
        next_quot,next_rem=quotient_remainder(next_a,next_d)
        assert not next_rem
        recurrence=add(shift(quot,4,-1),{2:1},{-6*q-4:s})
        assert next_quot==recurrence,(q,next_quot,recurrence)
        print('DIVISIBILITY q',q,'remainder',rem,'x0/d',txt(quot),'target xJ(1)',-eval_one(quot))
    print('PASS: exact divisibility, target evaluations, linking derivative, and recurrence at the specified samples.')
