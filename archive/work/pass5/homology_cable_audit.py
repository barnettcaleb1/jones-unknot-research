"""Independent actual-diagram audit of zero-framing and color-three convention."""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'braid_classification/packages'))
from spherogram import Link
import regina

def add(*ps):
    q={}
    for p in ps:
        for e,c in p.items():q[e]=q.get(e,0)+c
    return {e:c for e,c in q.items() if c}
def mul(p,q):return add(*({e+f:c*d} for e,c in p.items() for f,d in q.items()))
def shift(p,n):return {e+n:c for e,c in p.items()}
def regina_jones(word):
    L=Link(braid_closure=word)
    R=regina.Link.fromPD([[x+1 for x in row] for row in L.PD_code()])
    j=R.jones()
    p={e:int(str(j[e])) for e in range(j.minExp(),j.maxExp()+1) if j[e]!=0}
    return L,p

trefoil_word=[1,1,1]
# Blackboard two-cabling replaces sigma1 by sigma2 sigma1 sigma3 sigma2.
# Six inverse crossings between the two copies remove linking number three.
cable_word=[2,1,3,2]*3+[-1]*6
C,V=regina_jones(trefoil_word)
L,W=regina_jones(cable_word)
assert len(L.link_components)==2 and L.linking_number()==0
assert all(e%2==0 for e in V)
Vq={e//2:c for e,c in V.items()}
assert Vq=={1:1,3:1,4:-1}
delta_x={1:-1,-1:-1}
J3_x=add(mul(delta_x,W),{0:-1})
assert all(e%2==0 for e in J3_x)
J3_q={e//2:c for e,c in J3_x.items()}

# Habiro's trefoil expansion in the convention matching the ordinary Jones.
P1=mul({0:1,4:-1},{0:1,-2:-1})
P2=mul({0:1,5:-1},{0:1,-1:-1})
H3=add({0:1},shift(P1,1),shift(mul(P1,P2),2))
assert mul({1:1,0:1,-1:1},H3)==J3_q
assert sum(H3.values())==1
assert sum(e*c for e,c in H3.items())==0
assert sum(e*e*c for e,c in H3.items())==-16

# Exact consequences of H3=1 from its two nonconstant Habiro terms.
D=mul(mul({0:1,5:-1},{0:1,3:-1}),mul({0:1,-1:-1},{0:1,-1:-1}))
cyclo=mul(mul({1:1,0:-1},{1:1,0:-1}),mul({1:1,0:-1},{1:1,0:-1}))
cyclo=mul(mul(cyclo,{2:1,1:1,0:1}),{4:1,3:1,2:1,1:1,0:1})
assert D==shift(cyclo,-2)
assert sum(c*(-1)**e for e,c in D.items())==16

out={'companion_braid':trefoil_word,'zero_parallel_braid':cable_word,
     'parallel_components':len(L.link_components),'parallel_linking_number':L.linking_number(),
     'parallel_total_writhe':L.writhe(),'Regina_variable':'x=q^(1/2), q=A^(-4)',
     'ordinary_trefoil_Jones_in_q':Vq,'parallel_Jones_in_x':W,
     'unreduced_color_three_in_q':J3_q,'reduced_color_three_in_q':H3,
     'direct_cable_matches_Habiro':True,'H3_log_first_derivative':0,'H3_log_second_derivative':-16,
     'necessary_divisor_V_minus1_in_q':D,
     'cyclotomic_divisor':'Phi_1^4 Phi_3 Phi_5 (up to Laurent unit)',
     'necessary_signed_Jones_at_minus1_residue_mod16':1}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
