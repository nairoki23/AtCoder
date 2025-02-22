sheet=[]
for fd in range(101):
    lsa=[]
    for dj in range(101):
        lsa.append(False)
    sheet.append(lsa)
for fds in range(int(input())):
    nw=[]
    for fsdd in input().split() :
        nw.append(int(fsdd))
    nw.append(nw[0])
    while True:
        nw[0]=nw[4]
        while True:
            sheet[nw[2]][nw[0]]=True
            nw[0]=nw[0]+1
            if nw[0]==nw[1]:
                break
        nw[2]=nw[2]+1
        if nw[2]==nw[3]:
            break
        
res=0
for fd in range(101):
    for dj in range(101):
        res=sheet[fd][dj]+res

print(res)