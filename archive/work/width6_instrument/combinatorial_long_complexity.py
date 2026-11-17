"""Four fixed words: exact free-group complexity, no geometric reconstruction."""
from pathlib import Path
import json,sys,time,itertools
from combinatorial_validate import artin
from combinatorial_winding import reduced
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'width6_lift'))
import lift_pairing as lp


def cyclic_reduce(w):
    w=reduced(w)
    k=0
    while 2*k<len(w) and w[k]==-w[-k-1]:k+=1
    return w[k:len(w)-k] if k else w


class WordLimit(Exception):
    pass


def bounded_artin(word,limit=5000000):
    images=[[i]for i in range(1,7)]
    for step,g in enumerate(word):
        i=abs(g)-1
        a,b=images[i:i+2]
        stream=(itertools.chain(a,b,(-x for x in reversed(a))) if g>0
                else itertools.chain((-x for x in reversed(b)),a,b))
        out=[]
        for x in stream:
            if out and out[-1]==-x:out.pop()
            else:out.append(x)
            if len(out)>limit:
                raise WordLimit({'action_step':step+1,'limit_per_word':limit,
                                 'previous_meridian_lengths':[len(x)for x in images]})
        images[i],images[i+1]=(out,a)if g>0 else(b,out)
    return images


def measures(effective):
    # Geometric word = -effective; upward-cut convention converts to
    # reversal of each Artin image for the reversed effective word.
    try:images=[list(reversed(w))for w in bounded_artin(list(reversed(effective)))]
    except WordLimit as e:return {'status':'STOPPED_AT_WORD_LIMIT',**e.args[0]}
    caps=[]
    for a,b in ((1,2),(3,4)):
        word=reduced(images[b-1]+images[a-1])
        cycle=cyclic_reduce(word)
        caps.append({'source_cap':[a,b],'based_boundary_length':len(word),
                     'cyclic_boundary_length':len(cycle)})
    return {'status':'EXACT_COUNTS_COMPLETE','meridian_image_lengths':[len(w)for w in images],
            'source_cap_boundaries':caps}


def run():
    archive=json.loads((HERE.parent/'width6_lift/c3_samples.json').read_text())
    transports={r['target']:r['word']for r in lp.TRANSPORT}
    labels=['Bigelow_nonzero','LP_nonzero','prior_zero_kernel_arc_commutator']
    cases=[]
    for label in labels:
        x=next(r for r in archive if r['label']==label)
        effective=transports[x['i']][::-1]+x['word']+[-a for a in transports[x['j']]]
        cases.append((label,effective,x['i'],x['j']))
    cases.append(('witness14',[4,3,2,1,5,4,3,2,3,4,2,3,-1,-2],7,7))
    results=[]
    for label,w,i,j in cases:
        start=time.monotonic()
        r={'label':label,'i':i,'j':j,'effective_matrix_word':w,'effective_word_length':len(w),**measures(w)}
        r['seconds']=time.monotonic()-start
        attempt=HERE/(label+'_attempt.json')
        if attempt.exists():
            x=json.loads(attempt.read_text())
            if x.get('trace'):
                last=x['trace'][-1]
                pref=w[:last['prefix']]
                r['stopped_PL_prefix']={**last,**measures(pref)}
        results.append(r)
        print(label,'word',len(w),'meridians',r.get('meridian_image_lengths'),
              'cap_cyclic',[x['cyclic_boundary_length']for x in r.get('source_cap_boundaries',[])],
              'seconds',round(r['seconds'],3),flush=True)
    out={'status':'EXACT_FREE_GROUP_COUNTS_FOR_FOUR_FIXED_WORDS',
         'quantity':'Word length in the fixed six-meridian free basis; cap boundaries are cyclically reduced conjugacy classes of enclosing curves',
         'not_claimed':'These are not geometric cap-arc intersection counts, two-point pair counts, or slide-minimal complexity',
         'cases':results}
    (HERE/'combinatorial_long_complexity.json').write_text(json.dumps(out,indent=2)+'\n')
    return out

if __name__=='__main__':run()
