"""Exactly the two kernel configurations assigned in Claude043608."""
from pathlib import Path
from collections import defaultdict
import json,sys,time
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'width6_targeted'))
import lp_e_completions as ec
from lp_completions import divide_one_minus_t
from kernel_words import BIGELOW6_REN,LONG_PATON6
from kernel_parity import certify as certify_parity
probe,lp=ec.probe,ec.lp

def run():
    i,j=0,6
    assert [(a+1,b+1)for a,b in probe.caps(probe.STATES[i])]==[(3,4),(5,6)]
    assert [(a+1,b+1)for a,b in probe.caps(probe.STATES[j])]==[(1,2),(4,5)]
    original=ec.one_point_cap_matrix([],i,j)
    print('UNTRANSPORTED_M',original,flush=True)
    rows=[]
    for label,w in [('Bigelow6',BIGELOW6_REN),('LongPaton6',LONG_PATON6)]:
        start=time.monotonic();exponent=sum(1 if z>0 else-1 for z in w)
        J=probe.coefficient(w,i,j);Jhat={-(a-exponent)//2:c for a,c in J.items()}
        geo=probe.geometry(w,i,j);M=ec.one_point_cap_matrix(w,i,j)
        assert M==original
        P=lp.pairing(w,i,j);Phi=lp.shift(divide_one_minus_t(P),-4)
        specialization=lp.specialize(Phi)
        assert specialization=={a-2:c for a,c in Jhat.items()}
        at_t1=defaultdict(int)
        for (a,b),c in Phi.items():at_t1[a]+=c
        at_t1={a:c for a,c in at_t1.items()if c}
        assert not at_t1
        row={'label':label,'word':w,'i':i,'j':j,'top_caps':[[3,4],[5,6]],'bottom_cups':[[1,2],[4,5]],
             'exponent_sum':exponent,'geometry':geo,'one_point_cap_matrix_in_s':M,
             'J_in_A':J,'Jhat_in_s':Jhat,'P_in_s_t':lp.encode(P),'Phi_in_s_t':lp.encode(Phi),
             'Phi_TL_in_s':specialization,'Phi_at_t1':at_t1,
             'Phi_generic_L1':sum(abs(c)for c in Phi.values()),'seconds':time.monotonic()-start}
        if J:certify_parity(row)
        print(label,'len',len(w),'J',J,'geometry',geo,'M',M,'Phi_terms',len(Phi),'Phi_L1',row['Phi_generic_L1'],flush=True)
        if not J:
            row['topology_R12']=ec.tc.classify(w,i,j)
            print('TOPOLOGY',row['topology_R12'],flush=True)
            if row['topology_R12']['classification']=='unknown':
                row['topology_RIII']=ec.tc.classify_with_III(w,i,j,seed=0,steps=1000)
            row['closures']=probe.closure_checks(w,i,j)
        rows.append(row)
        (HERE/'kernel_specific.json').write_text(json.dumps({'untransported_M':original,'cases':rows},indent=2)+'\n')
    return rows
if __name__=='__main__':run()
