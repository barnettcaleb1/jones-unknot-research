# Referee: DIRECT computation of the branch sets T(1/n) from the quotient tangle (independent of BRIEF 1.3):
# run the quotient word of flat_search (same state machine), then add n half-twists between the bottom ends b1, b2
# (positions 0,1), cup b2-b3, close T-b1. Bracket -> V normalised (V(1)=1, V'(1)=0) in t = A^-4 (std) and t = A^4 (J-var).
import sys
import rlib, lp
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import flat_search as fs, alex
from kauffman import padd, pshift, pdelta
def run(word_ops,state):
    for c,i in word_ops:
        new={}
        for m,p in state.items():
            W=len(m)-1
            if c in 'lr':
                padd(new.setdefault(fs.cap(m,i),{}),p)
            elif c=='u':
                assert i+1<W
                m2,loop=fs.cup(m,i); padd(new.setdefault(m2,{}),pdelta(p) if loop else p)
            else:
                assert i+1<W
                a,b=(1,-1) if c=='x' else (-1,1)
                padd(new.setdefault(m,{}),pshift(p,a))
                m2,loop=fs.cup(m,i); q=pdelta(p) if loop else p
                padd(new.setdefault(fs.cap(m2,i),{}),pshift(q,b))
        state={m:p for m,p in new.items() if p}
    return state
def closure_bracket(word,n,letter=None):
    half=alex.parse(word)
    st=run(fs.quotient_word(half),{(1,0):{0:1}})
    assert set(st)<= {(3,2,1,0),(1,0,3,2)}, st.keys()
    c=letter if letter else ('x' if n>0 else 'y')
    st=run([(c,0)]*abs(n)+[('u',1)],st)
    assert set(st)<={(1,0)}
    return st.get((1,0),{})
def V_from_bracket(kb,std=True):
    kb=rlib.cl(kb); exps=sorted(kb); r=exps[0]%4
    assert all((e-r)%4==0 for e in exps)
    V={((r-e)//4 if std else (e-r)//4):c for e,c in kb.items()}
    s=sum(V.values()); assert s in (1,-1)
    V={e:c*s for e,c in V.items()}; d=sum(e*c for e,c in V.items())
    return {e-d:c for e,c in V.items()}
def V13(J,n):
    """BRIEF 1.3 in the J variable."""
    G=rlib.divmod_laurent(rlib.psub(J,rlib.ONE),{0:1,1:2,2:1}); assert G is not None
    f=rlib.psub(rlib.ONE,{-n:(-1)**(n%2)})
    V=rlib.padd(rlib.ONE,rlib.pmul(rlib.pmul(f,rlib.C3),G))
    if n%2:
        d=rlib.deriv_at(J,1,1); j=-d/8; assert j.denominator==1
        V={e+12*int(j):c for e,c in V.items()}
    return V
if __name__=='__main__':
    words=sys.argv[1:] or ['s.l1.y0.x1.u2','s.l1.x0.y1.u2','s.l1.y0.y0.x1.u2','s.l1.x0.x0.y1.u2','s.l1.y0.x1.y0.x1.u2','s.l1.x0.x0.x0.x1.x1.u2']
    for w in words:
        J=lp.J(w); print(w,' J=',sorted(J.items()))
        for n in (1,2,3):
            for c in ('x','y'):
                kb=closure_bracket(w,n,c)
                Vs=V_from_bracket(kb,True); Vj=V_from_bracket(kb,False)
                det=abs(sum(v*(-1)**(e%2) for e,v in Vs.items()))
                match=[m for m in (n,-n) if V13(J,m)==Vj]
                matchs=[m for m in (n,-n) if V13(J,m)==Vs]
                print('   %d twists of type %s: det=%d  V(J-var)=1.3 at n=%s ; V(std)=1.3 at n=%s'%(n,c,det,match,matchs))

def closure_bracket_framed(word,k,n):
    """T_raw + k half-twists on (b2,b3) [x if k>0, y if k<0], then n half-twists on (b1,b2) [x if n>0], cup b2-b3, close."""
    half=alex.parse(word)
    st=run(fs.quotient_word(half),{(1,0):{0:1}})
    ops=[('x' if k>0 else 'y',1)]*abs(k)+[('x' if n>0 else 'y',0)]*abs(n)+[('u',1)]
    st=run(ops,st); assert set(st)<={(1,0)}
    return st.get((1,0),{})
def det_of(kb):
    try: V=V_from_bracket(kb,True)
    except AssertionError: return None
    return abs(sum(v*(-1)**(e%2) for e,v in V.items()))
def find_framing(word,K=12):
    good=[]
    for k in range(-K,K+1):
        if all(det_of(closure_bracket_framed(word,k,n))==1 for n in (1,-1,2,-2,3)): good.append(k)
    return good
def compare13(word,ns=(1,-1,2,-2,3,-3)):
    J=lp.J(word); ks=find_framing(word)
    if len(ks)!=1: return ('framing?',ks)
    k=ks[0]; res=[]
    for n in ns:
        kb=closure_bracket_framed(word,k,n)
        Vs=V_from_bracket(kb,True); Vj=V_from_bracket(kb,False)
        tag=[]
        for m in (n,-n):
            if V13(J,m)==Vj: tag.append(('Jvar',m))
            if V13(J,m)==Vs: tag.append(('std',m))
        res.append((n,tag))
    return k,res
