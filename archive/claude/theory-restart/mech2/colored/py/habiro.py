#!/usr/bin/env python3
"""For each doubled two-bridge example: V_K from cxCKh-c2 (BN~ of the knot), J_3 from the b-generators of BN~(T_K),
Habiro coefficients a_1,a_2 :  J_3 = 1 + a_1 X_1 + a_2 X_1 X_2,  X_1=(t^2-t^-2)(t-t^-1), X_2=(t^{5/2}-t^{-5/2})(t^{1/2}-t^{-1/2})."""
import sys,os,re,glob,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from chains import parse_file,bgens,lattice
import sympy as sp
t=sp.symbols('t')
D='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/dbl/examples/knots/2-bridge_knots'
def knot_kh(name):
    """generators (h,q) of Kh~(K) from BN~(K) chains: free generator + H-torsion pairs"""
    comps=[]
    fn=os.path.join(D,name,'cxCKh-c2')
    gens=[]
    for l in open(fn).read().splitlines():
        m=re.match(r'^\s*\d+\)\s+h\^\s*(-?\d+)\s+q\^\s*(-?\d+)\s+δ\^\s*(-?[\d/]+)\s+(\S.*)$',l)
        if not m: continue
        h,q=int(m.group(1)),int(m.group(2)); ch=m.group(4).strip()
        if ch=='⬮': gens.append((h,q,'free'))
        else:
            mm=re.match(r'^⬮——H(\^(\d+))?—>⬮$',ch)
            assert mm, ch
            k=int(mm.group(2)) if mm.group(2) else 1
            gens.append((h,q,'tor')); gens.append((h+1,q+2*k,'tor'))
    return gens
def norm(expr):
    return sp.expand(expr)
def laurent(expr):
    e=sp.expand(expr)
    d=collections.OrderedDict()
    for term in sp.Add.make_args(e):
        c,p=term.as_coeff_exponent(t)
        d[int(p)]=d.get(int(p),0)+int(c)
    return dict(sorted((k,v) for k,v in d.items() if v))
def show(expr):
    d=laurent(expr)
    return ' '.join('%+d·t^%d'%(v,k) for k,v in sorted(d.items()))
X1=(t**2-t**-2)*(t-1/t)
X2=sp.expand((t**sp.Rational(5,2)-t**sp.Rational(-5,2))*(t**sp.Rational(1,2)-t**sp.Rational(-1,2)))
def analyse(name,verbose=True):
    kh=knot_kh(name)
    V=sum((-1)**h*t**sp.Rational(q,2) for h,q,_ in kh)
    free=[(h,q) for h,q,k in kh if k=='free'][0]
    rho,arc,sq,other=lattice(os.path.join(D,name,'cxBNr-c2-d'))
    assert not other
    pts=list(arc)
    for (a,b) in sq: pts+= [(a,b),(a+1,b),(a,b+1),(a+1,b+1)]
    chi=sum((-t)**a*(-t**4)**b for a,b in pts)
    chi=sp.expand(chi)
    c1=chi.subs(t,1); dchi=sp.diff(chi,t).subs(t,1)
    e=-dchi/c1
    J=sp.expand(chi*t**e/c1)
    R=sp.cancel((J-1)/X1)
    a1=sp.cancel((V-1)/((t**sp.Rational(3,2)-t**sp.Rational(-3,2))*(t**sp.Rational(1,2)-t**sp.Rational(-1,2))))
    a2=sp.cancel((R-a1)/X2)
    out=dict(name=name,V=V,J=J,a1=sp.expand(a1),a2=sp.expand(a2),free=free,rho=rho,arc=arc,sq=sq,unit=(c1,e),npts=len(pts))
    if verbose:
        print('==',name,'det^2=',len(pts),' s(q of free gen)=',free,' rho(h,q)=',rho,' |arc|=',len(arc),' #sq=',len(sq),' unit: sign',c1,'t^',e)
        print('  V   =',show(V))
        print('  J_3 =',show(J))
        print('  a_1 =',show(out['a1']), '   |a_1|=',sum(abs(v) for v in laurent(out['a1']).values()))
        try:
            print('  a_2 =',show(out['a2']), '   |a_2|=',sum(abs(v) for v in laurent(out['a2']).values()))
        except Exception as ex:
            print('  a_2 not Laurent:',out['a2'])
    return out
if __name__=='__main__':
    names=sys.argv[1:] or sorted([os.path.basename(p)[:-4] for p in glob.glob(D+'/*.kht') if os.path.exists(os.path.join(p[:-4],'cxBNr-c2-d'))],key=lambda s:[int(x) for x in s[1:].split('_')])
    for n in names:
        try: analyse(n)
        except Exception as ex: print('==',n,'ERROR',repr(ex))
