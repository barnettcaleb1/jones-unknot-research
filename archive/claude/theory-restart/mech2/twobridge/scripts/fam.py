#!/usr/bin/env python3
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import run as R
def summary(w,timeout=120):
    rec=R.run(w,timeout)
    if rec.get('bn') is None: return '%s ERROR'%w
    an=R.analyse(rec)
    kh=[l for l in (rec['kh'] or []) if ' r(' in l or 'r(' in l]
    import re
    k=None
    for l in rec['kh'] or []:
        m=re.search(r'\br\(([^)]*)\)',l)
        if m: k=m.group(1)
    return '%-12s dim=%3d k=%4s arc=%s x0=%s sq=%s%s'%(w,len(an['N']),k,an['arc'],an['x0'],sorted(an['squares']),' OTHER' if an['other'] else '')
if __name__=='__main__':
    for w in sys.argv[1:]: print(summary(w),flush=True)
