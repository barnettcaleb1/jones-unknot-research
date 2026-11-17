"""Exact tests of determinantal / activity / stability bridges for actual knots."""
from pathlib import Path
from collections import Counter,defaultdict
from fractions import Fraction as F
from itertools import combinations,combinations_with_replacement
import json
import tree_probe as t
from spherogram.links.simplify import basic_simplify

def det(a):
    a=[[F(v)for v in row]for row in a];out=F(1)
    for i in range(len(a)):
        pivot=next((j for j in range(i,len(a))if a[j][i]),None)
        if pivot is None:return F(0)
        if pivot!=i:a[i],a[pivot]=a[pivot],a[i];out=-out
        d=a[i][i];out*=d
        for j in range(i+1,len(a)):
            q=a[j][i]/d
            for k in range(i,len(a)):a[j][k]-=q*a[i][k]
    return out
def inverse(a):
    n=len(a);a=[[F(v)for v in row]+[F(i==j)for j in range(n)]for i,row in enumerate(a)]
    for i in range(n):
        p=next(j for j in range(i,n)if a[j][i]);a[i],a[p]=a[p],a[i]
        d=a[i][i];a[i]=[x/d for x in a[i]]
        for j in range(n):
            if j!=i:
                q=a[j][i];a[j]=[x-q*y for x,y in zip(a[j],a[i])]
    return [row[n:]for row in a]
def transfer(n,E):
    incidence=[]
    for a,b,s in E:
        col=[0]*(n-1)
        if a<n-1:col[a]+=1
        if b<n-1:col[b]-=1
        incidence.append(col)
    L=[[sum(c[i]*c[j]for c in incidence)for j in range(n-1)]for i in range(n-1)]
    Li=inverse(L);negative=[c for c,e in zip(incidence,E)if e[2]<0]
    K=[[sum(a[i]*Li[i][j]*b[j]for i in range(n-1)for j in range(n-1))for b in negative]for a in negative]
    return det(L),K

rows=[]
for name in ['3_1','4_1','8_19','8_20','10_124','11n34','11n42','hard_unknot']:
    L=t.Link(braid_closure=[1,2,1,-2,-1,-2,1,2])if name=='hard_unknot'else t.Link(name)
    n,E=t.graph(L);_,terms=t.tree_terms(L);w=L.writhe()
    J=Counter();hist=Counter();spectra=defaultdict(lambda:[0,0]);energies=[]
    for power,sign,k,T in terms:
        assert (power+3*w)%4==0
        energy=(power+3*w)//4;coefficient=sign*(-1 if w%2 else 1)
        omega=coefficient*(-1 if energy%2 else 1)
        J[energy]+=coefficient;hist[k]+=1;spectra[energy][0 if omega>0 else 1]+=1
        energies.append(energy)
    J={e:c for e,c in J.items()if c}
    R=t.regina.Link.fromPD([[x+1 for x in row]for row in L.PD_code()]);p=R.jones()
    actual={e//2:int(str(p[e]))for e in range(p.minExp(),p.maxExp()+1)if p[e]!=0}
    assert J==actual
    signed=sum(v*(-1 if k%2 else 1)for k,v in hist.items())
    tau,K=transfer(n,E);m=len(K)
    ratio=det([[F(i==j)-2*K[i][j]for j in range(m)]for i in range(m)])
    assert tau==len(terms) and tau*ratio==signed
    # A nonfactorization witness: equal total edge incidence, unequal products.
    seen={};rectangle=None
    for i,j in combinations_with_replacement(range(len(terms)),2):
        a,b=terms[i],terms[j]
        key=tuple(int(e in a[3])+int(e in b[3])for e in range(len(E)))
        value=(energies[i]+energies[j],a[1]*b[1])
        if key in seen and seen[key][0]!=value:
            old,ij=seen[key]
            rectangle={'four_trees_zero_based_edges':[terms[k][3]for k in[*ij,i,j]],
                       'Jones_exponent_sums':[old[0],value[0]],'sign_products':[old[1],value[1]]};break
        seen[key]=(value,(i,j))
    # Positive activity deformation: real stability implies all Rayleigh differences >=0.
    failures=[]
    for u in [F(1,2),F(2),F(4),F(1,4)]:
        weights=[u**j for j in energies];Z=sum(weights)
        Zi=[sum(v for v,tt in zip(weights,terms)if i in tt[3])for i in range(len(E))]
        for i,j in combinations(range(len(E)),2):
            Zij=sum(v for v,tt in zip(weights,terms)if i in tt[3]and j in tt[3])
            rayleigh=Zi[i]*Zi[j]-Z*Zij
            if rayleigh<0:
                failures.append({'u':str(u),'edges':[i,j],'Z':str(Z),'Zi':str(Zi[i]),'Zj':str(Zi[j]),'Zij':str(Zij),'Rayleigh_difference':str(rayleigh)});break
        if failures:break
    sign=lambda e:-1 if e%2 else 1
    row={'name':name,'PD_zero_based':L.PD_code(),'vertices':n,'signed_Tait_edges':E,
         'spanning_trees':len(terms),'negative_edge_count_histogram':dict(hist),
         'signed_tree_sum':signed,'transfer_kernel_negative_edges':[[str(x)for x in r]for r in K],
         'det_I_minus_2K':str(ratio),'Jones_in_t':J,
         'Jones_at_minus_one':sum(c*sign(e)for e,c in J.items()),
         'Jones_derivative_at_minus_one':sum(c*e*sign(e-1)for e,c in J.items()),
         'Jones_second_derivative_at_minus_one':sum(c*e*(e-1)*sign(e-2)for e,c in J.items()),
         'signed_activity_spectrum_positive_negative':dict(spectra),
         'edge_factorization_obstruction':rectangle,'positive_activity_Rayleigh_failure':failures}
    if name=='hard_unknot':
        basic_simplify(L);row['crossings_after_type_I_II_simplification']=len(L.crossings)
        L.simplify('global');row['crossings_after_global_simplification']=len(L.crossings)
        assert row['crossings_after_type_I_II_simplification']==8 and not L.crossings
    rows.append(row)
out={'identity':'V(-exp(h))=sum_T omega_T exp(h*j(T)); omega_T is a diagram-wide sign times (-1)^number_negative_edges_in_T',
     'determinantal_identity':'signed_tree_sum=tau(G)*det(I-2K_negative)',
     'rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
for row in rows:
    print(row['name'],'trees',row['spanning_trees'],'det',abs(row['signed_tree_sum']),
          'Vprime(-1)',row['Jones_derivative_at_minus_one'],
          'factorization_obstruction',bool(row['edge_factorization_obstruction']),
          'Rayleigh_failure',bool(row['positive_activity_Rayleigh_failure']))
