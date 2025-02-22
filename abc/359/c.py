import math
res=0
s=input().split()
sx=int(s[0])
sy=int(s[1])
t=input().split()
tx=int(t[0])
ty=int(t[1])

res=abs(ty-sy)
dx=tx-sx#+なら→に移動
idokyoyo=res+(((sx%2)+(dx>0)+(sy%2))%2)
ba=idokyoyo-dx
if (ba)>0:
    print(res)
else:
    print(res+math.ceil(-ba/2))