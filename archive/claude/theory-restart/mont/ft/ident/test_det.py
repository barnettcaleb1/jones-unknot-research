# validation: det(K) = det(K_in) det(K_out) (Z/2 x Z/2 branched cover of the quotient theta-curve; transfer argument)
import sys, random, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import diag, lp, flat_search as fs
def det(P): return abs(sum(c*(-1)**(e%2) for e,c in P.items()))
rows=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident3_rows.json'))
ok=0; bad=0; okU=0; n=0; nontriv=0
for r in rows:
    w=r[0]; inv=diag.all_invariants(w)
    dK=det(inv['K']['Delta']); di=det(inv['Kin']['Delta']); do=det(inv['Kout']['Delta'])
    du1=det(inv['Uin']['Delta']); du2=det(inv['Uout']['Delta'])
    n+=1
    if dK==di*do: ok+=1
    else: bad+=1; print('FAIL',w,dK,di,do)
    if dK==du1*du2: okU+=1
    if di>1 and do>1: nontriv+=1
print('n',n,'det(K)=det(Kin)det(Kout):',ok,'fail',bad,' (both factors >1 in',nontriv,') ; det(K)=det(Uin)det(Uout):',okU)
for w in ['s.r1.y2.y2.y2.u1','s.r2.r1.y0.y2.u1.u1']:
    inv=diag.all_invariants(w)
    print(w,{k:(sorted(inv[k]['V'].items()),det(inv[k]['Delta'])) for k in inv})
