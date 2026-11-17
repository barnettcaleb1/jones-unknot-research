from load import load
import re
def parse_word(w):
    # returns list of signed runs [('A',n) or ('B',n)] where A = axis crossings (y0:+, x0:-), B = off-axis (x1:+, y1:-), or None if other letters
    toks=w.split('.')
    assert toks[0]=='s' and toks[1] in ('l1','r1') and toks[-1]=='u2', w
    runs=[]
    for t in toks[2:-1]:
        if t=='y0': s=('A',1)
        elif t=='x0': s=('A',-1)
        elif t=='x1': s=('B',1)
        elif t=='y1': s=('B',-1)
        else: return None
        if runs and runs[-1][0]==s[0] and (runs[-1][1]>0)==(s[1]>0): runs[-1]=(s[0],runs[-1][1]+s[1])
        else: runs.append(s)
    return runs
def recs():
    out=[]
    seen=set()
    for r in load():
        runs=parse_word(r['word'])
        r['runs']=runs
        key=r['word'][5:]
        r['dup']= key in seen
        seen.add(key)
        out.append(r)
    return out
def levels(sp):
    lev={}
    for c,d in sp: lev.setdefault(d,[]).append(c)
    return {d:sorted(v) for d,v in lev.items()}
if __name__=='__main__':
    rs=[r for r in recs() if not r['dup']]
    print(len(rs),'distinct words')
    rs.sort(key=lambda r:(len(r['runs']) if r['runs'] else 99, str(r['runs'])))
    for r in rs:
        print(r['runs'] if r['runs'] else r['word'],'| k',r['k'],'j',r['j'],'|',' '.join('%d:%s'%(d,v) for d,v in sorted(levels(r['specials']).items())))
