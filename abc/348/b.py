import math
zahyo=[]
for fds in range(int(input())):
    fd=[]
    for f in input().split():  
        fd.append(int(f))
    zahyo.append(fd)
sfd=zahyo.copy()
zahyo.reverse()
for z in sfd:
    res=0
    nau=0
    basu=len(zahyo)
    for zh in zahyo:
        x=z[0]-zh[0]
        y=z[1]-zh[1]
        the=math.sqrt((x*x)+(y*y))
        #print(the)
        #print(nau)
        if the>=nau:
            res=basu
            nau=the
        basu=basu-1
    print(res)