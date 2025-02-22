raw_in=input().split()
h=int(raw_in[0])
w=int(raw_in[1])
bord=[]
for af9jewo in range(h):
    bord.append(list(input()))
diec=0
kurika=True
while kurika :
    shi=[]
    shirusi=[0,0]
    bf_diec=diec
    diec=0
    for gyo in range(h):
        unc=0
        oc=[]
        ct_len=0
        for fdsa in bord[gyo]:
            ct_len=ct_len+1
            if fdsa==".":
                unc=1+unc
            else:
                oc.append(fdsa)
        if (len(set(oc))==1) and ((ct_len-unc)>1):
            shirusi[0]=shirusi[0]+1
            for sum in range(w):
                shi.append((gyo,sum))

    for retsu in range(w):
        unc=0
        oc=[]
        haaku=0
        for teki in range(h):
            for fdsa in bord[teki][retsu]:
                haaku=haaku+1
                if fdsa==".":
                    unc=1+unc
                else:
                    oc.append(fdsa)
        if (len(set(oc))==1) and ((haaku-unc)>1):
            shirusi[1]=shirusi[1]+1
            for sum in range(h):
                shi.append((sum,retsu))
    while len(shi)>0:
        bord[shi[0][0]][shi[0][1]]="."
        del shi[0]
    diec=(shirusi[0]*w)+(shirusi[1]*h)
    kurika=False
    if diec==bf_diec:
        break
    else:
        kurika=True
print((h*w)-diec)