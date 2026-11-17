import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import sympy as sp
import famres
t=sp.symbols('t')
w3=sp.Rational(-1,2)+sp.sqrt(3)*sp.I/2
for fam in [('','a','bD'),('A','a','B'),('','a','ab'),('','a','Db')]:
    F,K=famres.fitfam(*fam)
    q3=F.index(3)
    M=sp.Matrix([[K[0][0][q3],K[0][1][q3]],[K[1][0][q3],K[1][1][q3]]]).applyfunc(sp.factor)
    print('family',fam,' K_3 =',M.tolist(),' det =',sp.factor(M.det()))
    if sp.simplify(M.det())==0:
        # M = u * w~^T : rows proportional; u from a nonzero column, w from a nonzero row
        r=0 if any(x!=0 for x in M.row(0)) else 1
        c=0 if any(x!=0 for x in M.col(0)) else 1
        u=[sp.factor(M[0,c]),sp.factor(M[1,c])]; wt=[sp.factor(M[r,0]),sp.factor(M[r,1])]
        for name,vec in [('left kernel u.v=0',u),('right kernel w.v=0 (w = mirror of row)',[sp.factor(wt[0].subs(t,1/t)),sp.factor(wt[1].subs(t,1/t))])]:
            if vec[1]==0: print('   ',name,': a = 0 impossible (a(-1)=1)'); continue
            q=sp.factor(-vec[0]/vec[1])
            qm1=sp.simplify(q.subs(t,-1)); qw=sp.nsimplify(sp.simplify(q.subs(t,w3)))
            ok_m1 = qm1 in (1,-1)
            # with Y^N shift: q -> t^{3N} q ; at t=-1 sign (-1)^N, at omega: invariant
            print('    %s: slope q = %s ;  q(-1) = %s ; q(omega) = %s  => %s'%(name,q,qm1,sp.simplify(qw),
                  'REALISABILITY EXCLUDED' if (abs(qm1)!=1 or sp.simplify(qw-1)!=0) else 'passes both tests'))
