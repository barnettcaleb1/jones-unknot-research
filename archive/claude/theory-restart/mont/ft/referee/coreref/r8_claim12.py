# Referee: claim 12. (a) Is M_3 in the Q-span of {1, a2, v3 of K, K_in, K_out, j}? Own constituent builder + rank test.
# (b) Delta M_3 pattern for pairs of inversions of the same two-bridge knot, length <= 8 (grouped by V_K AND Alexander values).
import sys, random, itertools, collections
import rlib, lp, alex, kauffman
from rlib import Fr
import sympy as sp
def bracket_morse(ops):
    st={(1,0):{0:1}}
    for c,i in ops:
        new={}
        for m,p in st.items():
            if c in 'lr': kauffman.padd(new.setdefault(kauffman.cap(m,i),{}),p)
            elif c=='u':
                m2,loop=kauffman.cup(m,i); kauffman.padd(new.setdefault(m2,{}),kauffman.pdelta(p) if loop else p)
            else:
                a,b=(1,-1) if c=='x' else (-1,1)
                kauffman.padd(new.setdefault(m,{}),kauffman.pshift(p,a))
                m2,loop=kauffman.cup(m,i); qq=kauffman.pdelta(p) if loop else p
                kauffman.padd(new.setdefault(kauffman.cap(m2,i),{}),kauffman.pshift(qq,b))
        st={m:p for m,p in new.items() if p}
    assert set(st)<={()}
    p=dict(st.get((),{})); r={}
    while p:
        e=max(p); v=p[e]; r[e-2]=-v; kauffman.padd(p,{e:-v,e-4:-v})
    return r
def V_of(kb):
    kb=rlib.cl(kb); ex=sorted(kb); r=ex[0]%4
    if any((e-r)%4 for e in ex): return None
    V={(r-e)//4:c for e,c in kb.items()}; s=sum(V.values())
    if s not in (1,-1): return None
    V={e:c*s for e,c in V.items()}; d=sum(e*c for e,c in V.items()); return {e-d:c for e,c in V.items()}
def constituents(word):
    """K_in: arc + inner axis segment (on-axis crossing -> full twist (c,0)(c,0)); K_out: arc + outer axis (on-axis letters dropped).
    Quotient positions: 0 = axis segment, half-strand k at k+1; letters (c,s), s>=1 act at position s (strands s, s+1)."""
    kin=[];kout=[]
    for c,s in alex.parse(word):
        if c in 'xy' and s==0: kin+=[(c,0),(c,0)]
        else: kin.append((c,s)); kout.append((c,s))
    kin.append(('u',0)); kout.append(('u',0))
    return V_of(bracket_morse(kin)),V_of(bracket_morse(kout))
mode=sys.argv[1]
if mode=='fit':
    rnd=random.Random(int(sys.argv[2])); rows=[]; seen=set()
    while len(rows)<int(sys.argv[3]):
        w,J=rlib.rand_word(rnd,6,18)
        if w in seen or J=={0:1}: continue
        seen.add(w); V=rlib.VK(w); Vi,Vo=constituents(w)
        if None in (V,Vi,Vo): continue
        rows.append(([1,rlib.a2V(V),rlib.v3V(V),rlib.a2V(Vi),rlib.v3V(Vi),rlib.a2V(Vo),rlib.v3V(Vo),-rlib.deriv_at(J,1,1)/8],rlib.mom(J,3)))
    A=sp.Matrix([[sp.Rational(x.numerator,x.denominator) if isinstance(x,Fr) else x for x in r] for r,_ in rows])
    b=sp.Matrix([m for _,m in rows])
    print('rows',len(rows),' rank(features)=',A.rank(),' rank([features|M3])=',A.row_join(b).rank())
    # also with products j*a2, a2*v3 etc. (not claimed, exploratory)
    nontriv_out=sum(1 for r,_ in rows if r[5]!=0 or r[6]!=0)
    print('rows with K_out nontrivial:',nontriv_out)
elif mode=='pairs':
    Lmax=int(sys.argv[2]); groups=collections.defaultdict(dict)
    for L in range(1,Lmax+1):
        for W in itertools.product(['y0','x0','x1','y1'],repeat=L):
            if any(W[i][1:]==W[i+1][1:] and W[i][0]!=W[i+1][0] for i in range(L-1)): continue
            w='s.l1.'+'.'.join(W)+'.u2'; J=lp.J(w)
            if J is None or J=={0:1}: continue
            V=rlib.VK(w)
            if V=={0:1}: continue
            key=(tuple(sorted(V.items())),alex.alex_eval(w,2),alex.alex_eval(w,3),alex.alex_eval(w,5))
            groups[key].setdefault(tuple(sorted(J.items())),w)
    tab=collections.Counter(); sizes=collections.Counter(); viol=[]
    for key,d in groups.items():
        sizes[len(d)]+=1
        if len(d)<2: continue
        rows=[(int(-rlib.deriv_at(dict(k),1,1)/8),rlib.mom(dict(k),3),w) for k,w in d.items()]
        for (j1,m1,w1),(j2,m2,w2) in itertools.combinations(rows,2):
            dm=m2-m1; dj=j2-j1
            ok=(dm%360==0) and ((dm//360-dj//2)%2==0 if dj%2==0 else False)
            tab['ok' if ok else 'VIOLATION']+=1
            if not ok and len(viol)<6: viol.append((w1,w2,j1,j2,m1,m2))
    print('group sizes (number of distinct J per (V,Alexander) class):',dict(sizes))
    print('pairs:',dict(tab)); print('violations:',viol)
