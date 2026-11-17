def row(r, ax='y', off='y'):
    """symmetric horizontal twist row with r=2j+1 crossings (r odd, can be negative via letter swap)"""
    assert r%2==1 or r%2==-1
    j=(abs(r)-1)//2
    a=ax if r>0 else {'x':'y','y':'x'}[ax]
    o=off if r>0 else {'x':'y','y':'x'}[off]
    w=['r1']*j+[a+'0']+[o+str(2*i) for i in range(1,j+1)]+['u1']*j
    return w
def mont(m, rows, tw='y', ax='y', off='y'):
    """horizontal inversion of P(2m, rows...): s.r2.(tw1)^|m|.ROW...ROW.u1"""
    t = tw if m>=0 else {'x':'y','y':'x'}[tw]
    w=['s','r2']+[t+'1']*abs(m)
    for r in rows: w+=row(r,ax,off)
    w+=['u1']
    return '.'.join(w)
