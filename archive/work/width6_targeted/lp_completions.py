"""Three fixed Long--Paton completions; no word search or tightness claim."""
from pathlib import Path
from collections import defaultdict
import json,sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'width6'))
sys.path.insert(0,str(HERE.parent/'width6_lift'))
import probe
import kernel_eval
import lift_pairing as lp
import topology_classifier as tc
from kernel_words import LONG_PATON6 as BETA,inv

P=101
def mul(a,b):
    return ((a[0]*b[0]+a[1]*b[2])%P,(a[0]*b[1]+a[1]*b[3])%P,
            (a[2]*b[0]+a[3]*b[2])%P,(a[2]*b[1]+a[3]*b[3])%P)
def inverse(a): return (a[3],-a[1]%P,-a[2]%P,a[0])
SEED=[(1,i,i,1+i*i)for i in range(1,7)]
def artin_eval(w):
    v=SEED[:]
    for z in w:
        k=abs(z)-1;a,b=v[k:k+2]
        if z>0:v[k],v[k+1]=mul(mul(a,b),inverse(a)),a
        else:v[k],v[k+1]=b,mul(mul(inverse(b),a),b)
    return v

def poly_mul(a,b):
    z=defaultdict(int)
    for i,c in a.items():
        for j,d in b.items():z[i+j]+=c*d
    return {k:c for k,c in z.items()if c}
def poly_sub(a,b):
    z=defaultdict(int,a)
    for i,c in b.items():z[i]-=c
    return {k:c for k,c in z.items()if c}
def cap_pair(i,j):
    if i==j:return {1:-1,-1:-1} # delta in s=A^-2
    if abs(i-j)==1:return {0:1}
    return {}

def divide_one_minus_t(poly):
    groups=defaultdict(dict);out={}
    for (a,b),c in poly.items():groups[a][b]=c
    for a,bs in groups.items():
        prev=0
        for b in range(min(bs),max(bs)+1):
            now=bs.get(b,0)+prev
            if b==max(bs):assert now==0
            elif now:out[a,b]=now
            prev=now
    assert lp.mul(out,{(0,0):1,(0,1):-1})==poly
    return out

def run():
    permutation=list(range(6))
    for z in BETA:
        i=abs(z)-1;permutation[i],permutation[i+1]=permutation[i+1],permutation[i]
    assert permutation==list(range(6))
    states,B=kernel_eval.rho(BETA,6,4)
    assert not kernel_eval.defect(B)
    htwist=BETA+[3]+inv(BETA)
    evaluated=artin_eval(htwist)
    assert evaluated[0]!=SEED[0]
    essential={'prime':P,'free_generator_images':SEED,'half_twist_word':htwist,
      'evaluated_images':evaluated,
      'certificate':'LP(arc34) cannot be isotoped off the vertical noodle between p2 and p3: if it lay in the right-hand subdisk, its half-twist would fix x1,x2, but the explicit SL2(F101) evaluation changes x1.'}
    cases=[]
    for label,i,j in [('A',3,0),('B',2,7),('C',3,7)]:
        C=[(a+1,b+1)for a,b in probe.caps(probe.STATES[i])]
        D=[(a+1,b+1)for a,b in probe.caps(probe.STATES[j])]
        assert all(b==a+1 for a,b in C+D)
        # N_C are the literal vertical noodles crossing the indicated cap gaps.
        # Since LP is a Burau kernel, pairings equal those before applying LP.
        noodle_M=[[int(a==d)for d,e in D]for a,b in C]
        assert noodle_M==[[0,0],[0,0]]
        cap_M=[[cap_pair(a,d)for d,e in D]for a,b in C]
        det=poly_sub(poly_mul(cap_M[0][0],cap_M[1][1]),poly_mul(cap_M[0][1],cap_M[1][0]))
        J=probe.coefficient(BETA,i,j)
        geometry=probe.geometry(BETA,i,j)
        assert geometry['closed_components']==0 and J
        pair=lp.pairing(BETA,i,j)
        at_t1=defaultdict(int);div_at_t1=defaultdict(int)
        for (a,b),c in pair.items():
            at_t1[a]+=c;div_at_t1[a]-=b*c
        assert not {a:c for a,c in at_t1.items()if c}
        limit={a:c for a,c in div_at_t1.items()if c}
        expected={a+2:c for a,c in det.items()}
        assert limit==expected,(label,limit,expected)
        H=lp.mul(divide_one_minus_t(pair),{(0,0):1,(-2,0):-2,(-4,0):1})
        Hspec=lp.specialize(H)
        Js={-e//2:c for e,c in J.items()}
        assert Hspec==poly_mul({2:1,0:-2,-2:1},Js)
        degree=max(Hspec)
        top=[{'s_exponent':a,'t_exponent':b,'coefficient':c,
              'specialized_contribution':int(c*(-1)**b)}
             for (a,b),c in sorted(H.items())if a-2*b==degree]
        simplification=tc.classify(BETA,i,j)
        # H=(q-1)^2 q^-2 P/(1-t), so H(q,1)=((q-1)^2/q)det(cap_M).
        cases.append({'label':label,'top_state':i,'bottom_state':j,'top_caps':C,'bottom_arcs_before_LP':D,
          'genuine_vertical_noodle_M':noodle_M,'one_cup_cap_Gram_M_in_s':cap_M,'cap_Gram_determinant_in_s':det,
          'geometry':geometry,'J_in_A':J,'J_A_degrees':[min(J),max(J)],'J_terms':len(J),
          'regularized_P_in_s_t':lp.encode(pair),'P_terms':len(pair),
          'P_div_1_minus_t_at_t1_in_s':limit,
          'H_t1_formula':'((q-1)^2/q)*det(cap_Gram_M), not the determinant of the literal vertical-noodle M',
          'absolute_H_in_s_t':lp.encode(H),'H_terms':len(H),
          'H_TL_specialization_in_s':Hspec,'H_top_s_degree':degree,
          'H_top_aggregated_monomials':top,
          'H_top_distinct_b':len(set(x['t_exponent']for x in top)),
          'relative_R1_R2_diagnostic':simplification,
          'tightness':'NOT CERTIFIED; no global minimum over cap slides has been computed.'})
        print(label,'J terms/degrees',len(J),min(J),max(J),'P terms',len(pair),'det cap M',det,
              'Htop',top,'R12 remaining',simplification['remaining_crossings'],flush=True)
    out={'word':BETA,'length':len(BETA),'Burau_exact_identity':True,'pure':True,
      'target_arc':'LP(arc34)','target_noodle':'vertical arc between p2,p3',
      'essential_pair_certificate':essential,'cases':cases,
      'scope':'Distinct marked completion configurations: J breadths differ. Literal noodles and cap-Gram duals must not be identified. No genuine intersection-pair lists or tightness certificates are produced.'}
    (HERE/'lp_completions.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
