sheet=[]
for  ads in range(3):
    sheet=sheet+input().split()

tyosa=[[0,1],[0,2],[1,2]]

nogakkari=[]

#縦調査
for gf in range(3):
    ston=gf*3
    gakka=0
    for sir in tyosa:
        if sheet[sir[0]+ston]!=sheet[sir[1]+ston]:
            gakka=gakka+1
    nogakkari.append(gakka/3)
for  ge in range(3):
    gakka=0
    for sir in tyosa:
        if sheet[(sir[0]*3)+ge]!=sheet[(sir[1]*3)+ge]:
            gakka=gakka+1
    nogakkari.append(gakka/3)
gakka=0
for sir in tyosa:
    if sheet[(sir[0]*4)]!=sheet[(sir[1]*4)]:
        gakka=gakka+1
nogakkari.append(gakka/3)
gakka=0
for sir in tyosa:
    if sheet[1+(sir[0])*2]!=sheet[1+(sir[1])*2]:
        gakka=gakka+1
nogakkari.append(gakka/3)
res=1
for tar in nogakkari:
    res=(tar)*res
print(res)