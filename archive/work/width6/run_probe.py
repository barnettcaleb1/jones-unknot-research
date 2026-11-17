"""Deterministic structured search; every reported zero is exact over Z[A^+-1]."""
from pathlib import Path
import json,time,itertools,random,sys
import probe as p
import kernel_words as k
ROOT=Path(__file__).resolve().parent

def families():
    yield 'identity',[]
    for i in range(1,6):
        for n in (-3,-1,1,3):yield 'one_generator',[i if n>0 else -i]*abs(n)
    # Ren's four-through-channel zero, tested in the two-through-channel.
    for a,b in itertools.product((-3,-1,1,3),repeat=2):
        yield 'Ren_standard',[-2]+([1]*a if a>0 else [-1]*-a)+[-2,4]+([5]*b if b>0 else [-5]*-b)+[4]
    for label,w in [('Bigelow6',k.BIGELOW6_REN),('LongPaton6',k.LONG_PATON6)]:
        yield label,w
        yield label+'_inverse',p.inv(w)
        for i in range(1,6):
            yield label+'_comm_generator',p.comm(w,[i])
            for s in (-1,1):yield label+'_conjugate',k.conj(w,[s*i])
    rng=random.Random(20261103)
    paths=[[],[1,2],[5,4],[2,-1],[4,-5],[1,2,3],[5,4,3]]
    paths += [p.reduce([rng.choice([-5,-4,-3,-2,-1,1,2,3,4,5]) for _ in range(n)]) for n in (4,5,6,7,8,9) for _ in range(4)]
    arcs=[k.conj([3],c) for c in paths]
    for a,b in zip(arcs,arcs[1:]+arcs[:1]):
        yield 'arc_commutator',p.comm(a,b)
        yield 'product_conjugates',p.reduce(a+b)
        yield 'product_opposite_conjugates',p.reduce(a+p.inv(b))
    for c in paths:
        w=k.conj(k.BIGELOW6_REN,c)
        yield 'kernel_conjugate_path',w
        yield 'kernel_arc_commutator',p.comm(k.BIGELOW6_REN,k.conj([3],c))

def main():
    start=time.time();seen=set();rows=[];wordrows=[];zeros=0;closed=0;byfamily={}
    for label,word in families():
        word=p.reduce(word);key=tuple(word)
        if key in seen:continue
        seen.add(key)
        matrix=p.coefficient_matrix(word)
        hits=[]
        for i,row in enumerate(matrix):
            for j,poly in enumerate(row):
                if poly:continue
                zeros+=1;g=p.geometry(word,i,j)
                if g['closed_components']:closed+=1
                hit={'family':label,'word':word,'i':i,'j':j,'caps_top':p.caps(p.STATES[i]),'cups_bottom':p.caps(p.STATES[j]),'geometry':g,'c_id':{}}
                rows.append(hit);hits.append([i,j,g['closed_components']])
        byfamily[label]=byfamily.get(label,0)+1
        wordrows.append({'family':label,'word':word,'zeros':hits})
        if len(seen)%10==0:
            print(json.dumps({'words':len(seen),'coefficients':81*len(seen),'zeros':zeros,'without_closed':zeros-closed,'seconds':round(time.time()-start,2)}),flush=True)
            (ROOT/'probe_candidates.json').write_text(json.dumps(rows,indent=2))
        if time.time()-start>480:break
    out={'words':len(seen),'coefficient_tests':81*len(seen),'zero_coefficients':zeros,'zero_with_closed_components':closed,'zero_without_closed_components':zeros-closed,'seconds':time.time()-start,'family_counts':byfamily,'states':p.STATES,'word_results':wordrows}
    (ROOT/'probe_results.json').write_text(json.dumps(out,indent=2))
    (ROOT/'probe_candidates.json').write_text(json.dumps(rows,indent=2))
    print(json.dumps({k:v for k,v in out.items() if k not in ('word_results','states')}),flush=True)
if __name__=='__main__':main()
