"""Three e-type completions of one LP essential Burau-zero pair."""
import json,sys
from collections import defaultdict
from pathlib import Path
import lp_completions as base
from lp_completions import probe,kernel_eval,lp,tc,BETA,HERE,poly_mul,poly_sub
from braid_ren_cable import cap_weight

def one_point_cap_matrix(w,i,j):
    states,m=kernel_eval.rho(w,6,4);ix={s:k for k,s in enumerate(states)}
    exponent=sum(1 if z>0 else -1 for z in w)
    out=[]
    for a,b in probe.caps(probe.STATES[i]):
        row=[]
        for d,e in probe.caps(probe.STATES[j]):
            st=[-1]*6;st[d]=e;st[e]=d;col=ix[tuple(st)];p={}
            for state,entries in zip(states,m):
                loops=cap_weight(state,[(a,b)])
                if loops is None:continue
                term=entries[col]
                for _ in range(loops):term=probe.delta(term)
                z=defaultdict(int,p)
                for k,v in term.items():z[k]+=v
                p={k:v for k,v in z.items()if v}
            assert all((k-exponent)%2==0 for k in p)
            row.append({-(k-exponent)//2:v for k,v in p.items()})
        out.append(row)
    return out

def run(generator=4):
    rows=[]
    assert generator in (1,4)
    for tau in ([],[generator,generator],[-generator,-generator]):
        w=[-z for z in reversed(tau)]+BETA
        exponent=sum(1 if z>0 else -1 for z in w)
        i,j=2,7
        J=probe.coefficient(w,i,j)
        geo=probe.geometry(w,i,j)
        assert geo['closed_components']==0 and geo['boundary_pairs']==[[0,1],[2,3]]
        M=one_point_cap_matrix(w,i,j)
        det=poly_sub(poly_mul(M[0][0],M[1][1]),poly_mul(M[0][1],M[1][0]))
        P=lp.pairing(w,i,j)
        quotient=base.divide_one_minus_t(P)
        H=lp.mul(quotient,{(0,0):1,(-2,0):-2,(-4,0):1})
        Hspec=lp.specialize(H)
        Jnorm={-(e-exponent)//2:c for e,c in J.items()}
        assert Hspec==poly_mul({2:1,0:-2,-2:1},Jnorm)
        qlim=defaultdict(int)
        for (a,b),c in quotient.items():qlim[a]+=c
        qlim={a:c for a,c in qlim.items()if c}
        if det:
            shift=min(qlim)-min(det);sign=qlim[min(qlim)]//det[min(det)]
            assert sign in (-1,1)
            assert qlim=={a+shift:sign*c for a,c in det.items()}
            unit={'s_exponent':shift-2,'coefficient':sign}
        else:
            assert not qlim;unit=None
        deg=max(Hspec)
        top=[{'s_exponent':a,'t_exponent':b,'coefficient':c,'specialized_contribution':int(c*(-1)**b)}
             for (a,b),c in sorted(H.items())if a-2*b==deg]
        simplify=tc.classify(w,i,j)
        rows.append({'top_cap_transport_tau':tau,'effective_word_tau_inverse_beta':w,
          'top_caps_before_transport':[[2,3],[5,6]],'bottom_arcs_before_beta':[[1,2],[3,4]],
          'genuine_vertical_noodle_M':[[0,0],[0,0]],
          'one_point_cap_M_in_s':M,'cap_M_determinant_in_s':det,
          'H_t1_factor':'((q-1)^2/q) * unit * det(cap_M)', 'H_t1_unit':unit,
          'exponent_sum':exponent,'J_id_in_A':J,'J_hat_in_s':Jnorm,'J_id_A_range':[min(J),max(J)],
          'J_id_A_breadth':max(J)-min(J),'geometry':geo,
          'P_in_s_t':lp.encode(P),'H_in_s_t':lp.encode(H),'H_top_s_degree':deg,'H_top_aggregated_monomials':top,
          'R12_diagnostic':simplify,'tightness':'Not certified; no global cap-slide minimum asserted.'})
        print('tau',tau,'Jrange',min(J),max(J),'Mcap',M,'det',det,'H_t1unit',unit,'Htop',top,
              'R12',simplify['remaining_crossings'],flush=True)
    name='lp_e_completions.json' if generator==4 else 'lp_e_fixed_cap_completions.json'
    (HERE/name).write_text(json.dumps(rows,indent=2)+'\n')
if __name__=='__main__':run(int(sys.argv[1]) if len(sys.argv)>1 else 4)
