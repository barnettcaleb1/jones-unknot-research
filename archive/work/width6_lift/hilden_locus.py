"""Bounded Hilden double-coset trace test; actual unknot closure is built in.

Uses one fixed unknot-closure seed and Tawn generators of H_8, converted
to the nested cap system for D. No identity is inferred from a matrix
specialization: intersection with B6 is certified by faithful Artin action.
"""
from pathlib import Path
import sys,json,itertools,time
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'width6'))
import probe as p
from central_arc_artin import action
from kernel_eval import rho
import topology_classifier as tc

C0=7
GAMMA=[5,6]
SEED=[4,3,2,1,5,4,3,2,3,4]
H={'r1':[2,1,-3,-2], 'r2':[4,3,2,1,-5,-4,-3,-2]}
H.update({f's{i}':[2*i,2*i-1,2*i+1,2*i]for i in range(1,4)})
H.update({f't{i}':[2*i-1]for i in range(1,5)})

def permutation(word,n=8):
    labels=list(range(1,n+1))
    for g in word:
        i=abs(g)-1;labels[i],labels[i+1]=labels[i+1],labels[i]
    return labels

def delete_external(word):
    labels=list(range(1,9));out=[]
    for g in word:
        i=abs(g)-1
        if labels[i]<=6 and labels[i+1]<=6:
            j=1+sum(x<=6 for x in labels[:i]);out.append(j if g>0 else-j)
        labels[i],labels[i+1]=labels[i+1],labels[i]
    return p.reduce(out)

def in_embedded_B6(word):
    if permutation(word)[6:]!=[7,8]:return None
    deleted=delete_external(word)
    if action(word,8)==action(deleted,8):return deleted
    return None

def checks():
    states,m=rho(GAMMA,8,0)
    std=(1,0,3,2,5,4,7,6);nested=(1,0,3,2,7,6,5,4)
    col=states.index(std)
    assert [m[i][col]for i in range(len(states))]==[{0:1}if s==nested else{}for s in states]
    for name,w in H.items():
        states,m=rho(w,8,0);col=states.index(std)
        assert all(not m[i][col]for i,s in enumerate(states)if s!=std),(name,'not cap stabilizer')
        assert len(m[col][col])==1
    c=p.closure_checks(SEED,C0,C0)
    assert c['denominator_closure']['unknot_certified']
    assert p.coefficient(SEED,C0,C0)=={}
    return c

def main():
    start=time.monotonic();seedcheck=checks()
    gens=[('1',[])]+[(name,w)for name,w in H.items()]+[(name+'^-1',p.inv(w))for name,w in H.items()]
    rows=[];seen=set();counts={'generated_H_pair_cases':0,'return_B6':0,'distinct_B6_words':0,'zeros':0,'split':0,'closure_errors':0}
    for (ln,lw),(rn,rw) in itertools.product(gens,repeat=2):
        counts['generated_H_pair_cases']+=1
        word=p.reduce(GAMMA+lw+p.inv(GAMMA)+SEED+GAMMA+rw+p.inv(GAMMA))
        beta=in_embedded_B6(word)
        if beta is None:continue
        counts['return_B6']+=1
        if tuple(beta)in seen:continue
        seen.add(tuple(beta));counts['distinct_B6_words']+=1
        coeff=p.coefficient(beta,C0,C0);cl=p.closure_checks(beta,C0,C0)
        if not cl['denominator_closure']['unknot_certified']:counts['closure_errors']+=1
        rec={'left_H':ln,'right_H':rn,'word_B8':word,'beta':beta,'coefficient':coeff,
             'geometry':p.geometry(beta,C0,C0),'closures':cl}
        if not coeff:
            counts['zeros']+=1
            top=tc.classify(beta,C0,C0);rec['topology']=top
            if top['classification']=='split_certified':counts['split']+=1
            else:
                # Actual U2 and U fillings supply the Property R certificate.
                n=cl['numerator_closure'];d=cl['denominator_closure']
                if n['simplified_crossings']==0 and n['simplified_components']==2 and d['unknot_certified']:
                    counts['split']+=1;rec['property_R_split']=True
        rows.append(rec)
    out={'status':'TRUSTED bounded computation','counts':counts,'seconds':time.monotonic()-start,
         'gamma':GAMMA,'seed':SEED,'seed_closures':seedcheck,'generators':H,'cases':rows}
    (HERE/'hilden_locus_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(counts,indent=2));print('seconds',out['seconds'])
if __name__=='__main__':main()
