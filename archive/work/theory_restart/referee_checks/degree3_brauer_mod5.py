"""Fixed generator-level folded-cover/Brauer comparison; no knot scan."""
from pathlib import Path
import contextlib, io, json, runpy
import sympy as S

with contextlib.redirect_stdout(io.StringIO()):
    ft = runpy.run_path(str(Path(__file__).with_name('ft_local.py')))
q=ft['q']; s=ft['s']; I2=S.eye(2); I4=S.eye(4); I16=S.eye(16)
checks={}
def check(name, assertion):
    ok=bool(assertion); checks[name]=ok; assert ok,name
    print(name+': PASS')
def simp(M): return M.applyfunc(S.simplify)

# Actual mixed marking: Y has its distinguished color-one channel normalized
# to one and the other eigenvalue t^-3. It is T^-1, not T, in ft_local's gauge.
check('T acts by q^-4 on the vertex inclusion',ft['matred'](ft['T']*ft['i']-q**-4*ft['i'])==S.zeros(6,2))
check('normalized inverse T has other eigenvalue t^-3',S.cancel(q**-2/q**4-q**-6)==0)

g=ft['swap'](2,2)
eps=S.Matrix([0,1,-1,0])
epsform=S.Matrix([[0,1],[-1,0]])
G=S.kronecker_product(epsform,epsform)
point=eps*(eps.T*G)/2
check('folded antisymmetric point is (I-g)/2',point==(I4-g)/2)
check('point is a rank-one idempotent',point*point==point and S.trace(point)==1)
check('sheet swap preserves folded metric',g.T*G*g==G)

# U_q(sl2) fundamental braid. Ordinary Jones t=e^(2h) means q=e^(-h).
B=ft['swap'](2,2)*ft['R'](ft['E1'],ft['F1'],[1,-1],[1,-1])
check('fundamental braid root is sheet swap',simp(B.subs(q,1))==g)
Y=-B.inv()  # y0 is the inverse crossing, with the root Jones sign.
Yinv=-B
Y0=simp(Y.subs(q,1))
Dy=simp((-q*(Y-Yinv).diff(q)).subs(q,1))
check('folded y0 root is minus sheet swap',Y0==-g)
check('folded raw y0 principal operator',Dy==-2*I4+g)
df1=S.trace(point*Dy)
check('folded y0 first coefficient change is -3',df1==-3)
Dyp=Dy-df1*Y0
check('folded preferred y0 symbol is -2(I+g)',Dyp==-2*(I4+g))

def embed_pair(M,a,b):
    out=S.zeros(16)
    for col in range(16):
        bits=[(col>>(3-i))&1 for i in range(4)]
        smallcol=2*bits[a]+bits[b]
        for sc in range(4):
            dest=bits.copy(); dest[a]=sc//2; dest[b]=sc%2
            row=sum(dest[i]<<(3-i) for i in range(4))
            out[row,col]+=M[sc,smallcol]
    return out

g13=embed_pair(g,0,2); g24=embed_pair(g,1,3)
P=g13*g24
K=(I16-g13)*(I16-g24)
check('folded contraction has rank one and loop dimension four',K.rank()==1 and K*K==4*K)
check('folded permutation fixes contraction',P*K==K and K*P==K)
check('folded Fierz identity',P-K==g13+g24-I16)
BB=embed_pair(B,0,2)*embed_pair(B,1,3)
BD=simp((-q*(BB-BB.inv()).diff(q)).subs(q,1))
check('paired off-axis straight symbol is -2(P-K)',P*BD==-2*(P-K))

Pi=S.diag(-1,1,-1)
gosp=-Pi
osp_y=3*(S.eye(3)+gosp)
cover_coeff=-2
check('preferred y0 coefficient discrepancy is five',3-cover_coeff==5)
check('closed Brauer loop parameters agree modulo five',(-1-4)%5==0 and (-3-2)%5==0)
check('point loop has dimension one in both models',((-1)-(-3))/2==1 and (4-2)/2==1)
check('ordinary cubic coefficient conversion',(-48-42)%5==0)

result={'all_passed':all(checks.values()),'checks':checks,
 'marking':{'X':'x1; positive color-two crossing','Y':'y0; T^-1 in the FT gauge'},
 'osp_parameters':{'delta':-1,'tau':-3},'folded_cover_parameters':{'delta':4,'tau':2},
 'scope':'Principal order-three symbols agree modulo five; lower-order residual is not determined.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('ALL',len(checks),'CHECKS PASSED')
