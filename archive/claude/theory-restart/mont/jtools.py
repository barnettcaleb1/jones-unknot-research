import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import flat_search as fs, alex
import sympy as sp
t=sp.symbols('t')
def J_raw(word):
    half=alex.parse(word)
    full=alex.symmetrize(half)
    if full is None or alex.diagram(full) is None: return None
    y,x=fs.bracket_vector(half)
    u={}; fs.padd(u,y); fs.padd(u,fs.pdelta(x))
    u={e:c for e,c in u.items() if c}
    assert len(u)==1
    (eu,cu),=u.items()
    return sp.expand(sum(c*cu*t**sp.Rational(e-eu,4) for e,c in y.items() if c))
def normalize(J):
    """unique unit multiple of J with J = 1 mod (t+1)^2 (None if impossible)"""
    J=sp.expand(J)
    for k in range(-60,61):
        for s in (1,-1):
            K=sp.expand(s*t**k*J)
            if sp.simplify(K.subs(t,-1)-1)==0 and sp.simplify(sp.diff(K,t).subs(t,-1))==0:
                return K
    return None
def a2(J):
    return sp.Rational(-1,24)*sp.diff(J,t,2).subs(t,-1)
X=sp.Matrix([[1,1-t**4],[0,-t]]); Y=sp.Matrix([[1,0],[t**-3,t**-3]])
e1=sp.Matrix([1,0])
def star(v,w):
    return sp.Matrix([sp.expand(v[0]*w[0]), sp.expand(v[0]*w[1]+v[1]*w[0]+(1-t**3)*v[1]*w[1])])
