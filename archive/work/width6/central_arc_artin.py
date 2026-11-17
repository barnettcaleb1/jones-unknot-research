"""Faithful Artin-action certificate that Bigelow6 fixes the central arc."""
import json
from pathlib import Path
import kernel_words as k

def inv(w):return [-x for x in reversed(w)]
def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return out
def action(word,n=6):
    images=[[i+1] for i in range(n)]
    for z in word:
        i=abs(z)-1;a,b=images[i:i+2]
        if z>0:images[i],images[i+1]=red(a+b+inv(a)),a
        else:images[i],images[i+1]=b,red(inv(b)+a+b)
    return images

if __name__=='__main__':
    assert action([1,-1])==action([])
    assert action([1,2,1])==action([2,1,2])
    assert action([1,3])==action([3,1])
    word=k.comm(k.BIGELOW6_REN,[3]);images=action(word)
    out={'word':word,'convention':'sigma_i sends xi to xi xi+1 xi^-1, and xi+1 to xi; compose rightward along the word',
         'images':images,'identity':images==[[i+1] for i in range(6)],
         'image_lengths':[len(x) for x in images]}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(out)
