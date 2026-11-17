#!/usr/bin/env python3
"""Replay exact RI/RII/RIII certificates for two closed four-strand braids.

Requires Regina's Python package (tested with wheel 7.4.1). No Jones or
Alexander polynomial is used as an unknot recognition criterion.
"""
import collections,json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parent
# The optional first argument is a local directory containing regina.
if len(sys.argv)>1:sys.path.insert(0,sys.argv[1])
import regina

def snapshot(L):
    return {'crossings':L.size(),'components':L.countComponents(),'brief':L.brief()}

def braid_gauss(word,n=4):
    """Independent direct encoding, without Spherogram.

Track each original strand through all crossings, then connect the bottom
in each position to the top in that position. The completed diagram is
rotated in 3D to agree with the PD projection used in the certificate.
"""
    positions=list(range(n));visits=[[] for _ in range(n)]
    for k,g in enumerate(word,1):
        i=abs(g)-1
        assert 0<=i<n-1
        a,b=positions[i:i+2];sign=1 if g>0 else -1
        visits[a].append(sign*k);visits[b].append(-sign*k)
        positions[i],positions[i+1]=b,a
    components=[];unvisited=set(range(n))
    while unvisited:
        start=a=min(unvisited);component=[]
        while a in unvisited:
            unvisited.remove(a);component.extend(visits[a]);a=positions.index(a)
        assert a==start
        components.append(component)
    link=regina.Link.fromData([1 if g>0 else -1 for g in word],components)
    link.rotate()  # an ordinary rotation in 3-space, not a crossing change
    return link

def move(L,op):
    kind=op[0]
    if kind=='r1':return L.r1(L.crossing(op[1]))
    if kind=='r2':return L.r2(L.crossing(op[1]))
    if kind=='r3':return L.r3(L.crossing(op[1]),op[2])
    if kind=='r1add':
        return L.r1(regina.StrandRef(L.crossing(op[1]),op[2]),op[3],op[4])
    raise ValueError('Unknown move '+repr(op))

rows=json.loads((ROOT/'reidemeister_certificates.json').read_text())
assert [r['index'] for r in rows]==[82,86]
for row in rows:
    L=regina.Link.fromPD(row['pd'])
    direct=braid_gauss(row['word'])
    assert L.isClassical() and direct.isClassical()
    # Allow relabelling only: reflection, reversal and rotation are disabled.
    assert L.sig(False,False,False)==direct.sig(False,False,False)
    assert L.countComponents()==1
    initial=L.size();max_crossings=initial
    for step in row['steps']:
        assert snapshot(L)==step['before']
        assert move(L,step['move']), ('Invalid move',step)
        assert snapshot(L)==step['after']
        assert L.countComponents()==1
        max_crossings=max(max_crossings,L.size())
    assert L.size()==0 and L.countComponents()==1
    counts=dict(collections.Counter(step['move'][0] for step in row['steps']))
    print(f"Index {row['index']}: {initial} crossings -> 0, one component; "
          f"{len(row['steps'])} valid Reidemeister moves, {counts}.")
print('Both closures are certified unknots.')
