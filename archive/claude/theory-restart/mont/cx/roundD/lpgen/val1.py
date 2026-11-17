"""VALIDATION 1: transcription of C1 casework; rational-only re-derivations (Q-MONT, V3) and the n=1 negative control."""
import sys, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen')
import lpg, runner, v3b, h3b
from fractions import Fraction as Fr
random.seed(1)
# (1) transcription check against v3b.cases / h3b.cases_pq
bad=0; tot=0
for trial in range(300):
    Bd=tuple(Fr(random.randint(-12,12),random.choice([1,2,3,6])) for _ in range(4))
    mB=Fr(random.randint(-6,6),random.choice([1,2]))
    for cl in lpg.closure_classes():
        if cl['kind']=='V': ref=v3b.cases(Bd,mB,cl['typ'],cl['a3'])
        else: ref=h3b.cases_pq(Bd,mB,cl['p'],cl['q'],allow_r1=(mB!=0))
        mine=lpg.case_rows(cl['p'],cl['q'])+lpg.case_rows(cl['p'],cl['q'],m=mB,allow_r1=(mB!=0))
        md={nm:rows for nm,rows in mine}
        for name,eqs,P0 in ref:
            tot+=1
            rows=md[name]
            E=list(eqs)+[(0,1,0,0,P0)]
            for (co,a),e in zip(rows,E):
                if tuple(Fr(x) for x in e[:4])!=co or lpg.evalaff(a,*Bd,mB)!=Fr(e[4]): bad+=1; print('MISMATCH',cl['name'],name,co,e); break
        assert set(md)==set(n for n,_,_ in ref), (set(md),set(n for n,_,_ in ref))
print('transcription check: %d case systems compared, %d mismatches'%(tot,bad))
# (2) rational-only
for nmin,lab in ((1,'V3 (n>=1)'),(2,'V3/Q-MONT (n>=2)')):
    out=runner.run_all([],nmin,kmin=0)
    print(lab, runner.summary(out))
    for k,v in sorted(runner.opens(out).items(),key=str): print('   OPEN',k,v)
