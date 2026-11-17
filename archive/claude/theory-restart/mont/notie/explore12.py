from nt import *
for boxes in [[(-2,)]*6, [(-2,)]*3+[(-3,)]*3, [(-2,),(-3,),(-4,),(-2,),(-2,),(-5,)]]:
    vs=[box(s) for s in boxes]
    for N in (1,2,3):
      for mu in (-2,-3,-1):
        Jv=neck(mu,N,vs); e=top(Jv); b=bot(Jv)
        A=prod(vs)[0]
        print(boxes[:3],'..','mu',mu,'N',N,'span',span(Jv),'top coeffs',[Jv.get(e-i,0) for i in range(4)],'bot coeffs',[Jv.get(b+i,0) for i in range(4)],'spanA',span(A))
