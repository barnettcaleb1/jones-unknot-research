# Symbol of v_3(K) on equivariant configurations, and of iota := (M_3/36 - 7 v_3)/5 (brief F3).
# Jones symbol (upstairs, single crossings, all eps = +1), derived in REPORT 3.6:
#   W^V_m(D) = sum_{U subset chords} (3/2)^{|U|} (1/2)^{m-|U|} sum_{or/un on the rest} (+-1) (-2)^{c-1}, c = #circles after smoothing.
#   [h^3] V(e^h) = -6 v_3, so the symbol of v_3 is -W^V_3/6.
import itertools, math, sys
from fractions import Fraction as F
import abstract as ab, check_1t as c1
def circle_components(n_pts,chords,choice):
    adj={}
    def link(u,v): adj.setdefault(u,[]).append(v); adj.setdefault(v,[]).append(u)
    for p in range(n_pts): link(('out',p),('in',(p+1)%n_pts))
    sm=set()
    for (a,b),ch in zip(chords,choice):
        if ch=='or': link(('in',a),('out',b)); link(('in',b),('out',a))
        else: link(('in',a),('in',b)); link(('out',a),('out',b))
        sm|={a,b}
    for p in range(n_pts):
        if p not in sm: link(('in',p),('out',p))
    seen=set(); c=0
    for u in adj:
        if u in seen: continue
        c+=1; st=[u]; seen.add(u)
        while st:
            x=st.pop()
            for y in adj[x]:
                if y not in seen: seen.add(y); st.append(y)
    return c
def WV(chords_angles):
    pts=sorted(set(a for ch in chords_angles for a in ch)); idx={a:i for i,a in enumerate(pts)}
    chords=[(idx[a],idx[b]) for a,b in chords_angles]; m=len(chords); tot=F(0)
    for U in itertools.product([0,1],repeat=m):
        act=[c for c,u in zip(chords,U) if not u]
        inner=0
        for ch in itertools.product(('or','un'),repeat=len(act)):
            sg=1
            for x in ch: sg*=(1 if x=='or' else -1)
            inner+=sg*(-2)**(circle_components(len(pts),act,ch)-1)
        tot+=F(3,2)**sum(U)*F(1,2)**(m-sum(U))*inner
    return tot
def v3_symbol(D):
    ups=c1.lift(D); groups={}
    for g,c in ups: groups.setdefault(g,[]).append(c)
    tot=F(0)
    for pick in itertools.product(*groups.values()):
        tot+=-WV(list(pick))/6
    return tot
if __name__=='__main__':
    # sanity: circle diagrams P2 (crossing pair) -> W^V_2 = -3 ; P3, K3 values
    print('W^V_2(crossed pair) =',WV([(0,2),(1,3)]),' (expect -3 = -3 Delta^2 a_2)')
    print('W^V_3(P3: a b a c b c) =',WV([(0,2),(1,4),(3,5)]),'  W^V_3(K3: a b c a b c) =',WV([(0,3),(1,4),(2,5)]))
    import json
    tab=json.load(open('w3_table.json'))
    out=[]
    for (no,nn) in [(3,0),(2,1),(1,2)]:
        toks=[('E',i) for i in range(no) for _ in (0,1)]+[('O',j) for j in range(nn)]; seen=set()
        for perm in set(itertools.permutations(toks)):
            for parity in itertools.product([0,1],repeat=len(perm)-1):
                D=[perm[0]]
                for gb,tk in zip(parity,perm[1:]):
                    if gb: D.append(('T',))
                    D.append(tk)
                key=ab.shape(D)
                if key in seen: continue
                seen.add(key)
                W3=ab.w(D); sv=v3_symbol(D); si=(F(W3,6)-7*sv)/5   # brief F3 uses lp variable t'=1/t: Delta^3 M3^lp/36 = +W3/6
                out.append((key,W3,sv,si))
    nonint=[o for o in out if o[3].denominator!=1]
    print('types',len(out),' iota symbol non-integral in',len(nonint),'types')
    for key,W3,sv,si in sorted(out,key=lambda o:(o[0][0].count('o'),o[0])):
        if W3 or sv or si: print('  %-22s %-4s  W3=%5d  Delta3 v3=%5s  Delta3 iota=%5s'%(key[0],''.join(map(str,key[1])),W3,sv,si))
