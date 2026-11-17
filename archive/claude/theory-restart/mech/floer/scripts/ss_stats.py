import sys, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/floer/scripts')
from ss_match import analyse
from load import load138
T = load138()
c = collections.Counter(); rev_ok = []; slack = collections.Counter(); ratio=[]
for rec in T:
    D, Dp, out = analyse(rec, L=30)
    k = rec['k']
    for m, res in out.items():
        valid = all(need >= 0 for (_,need,_,_) in res)
        plus = valid and all(need <= mp for (_,need,mp,mm) in res)
        minus = valid and all(need <= mm for (_,need,mp,mm) in res)
        tag = 'm=0' if m == 0 else ('same sign as k' if m*k > 0 else ('opposite sign to k' if m*k < 0 else 'k=0,m!=0'))
        c[(tag,'rank ok')] += valid
        c[(tag,'rule + feasible')] += plus
        c[(tag,'rule - feasible')] += minus
        c[(tag,'total')] += 1
        if minus: rev_ok.append((rec['name'], m, res))
        if plus:
            for (_,need,mp,mm) in res:
                if mp: ratio.append(need/mp)
                slack[mp-need] += 1
for kk in sorted(c): print(kk, c[kk])
print('reversed rule feasible:', [(n,m) for n,m,_ in rev_ok])
import statistics
print('need/max(+) over feasible cases: min %.2f median %.2f max %.2f' % (min(ratio), statistics.median(ratio), max(ratio)))
print('tight cases (need == max):', slack[0], 'of', sum(slack.values()))
