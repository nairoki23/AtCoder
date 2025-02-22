points=[]
user=[]
tores=[]
atode=range(int(input().split()[0]))
for fd in input().split():
    points.append(int(fd))
gati=0
for aggbsf in atode:
    gati=gati+1
    ct=0
    kibou=[]
    now=gati
    for std in input():
        if std=="o":
            now=points[ct]+now
        else:
            kibou.append(points[ct])
        ct=ct+1
    kibou.sort(reverse=True)
    tores.append(kibou)
    user.append(now)
saikou=sorted(user,reverse=True)[0]
depo=False
for tir in atode:
    res=0
    if (saikou==user[tir])and (not depo):
        depo=True
        print(res)
        continue
    while saikou>=user[tir]:
        user[tir]=tores[tir][res]+user[tir]
        res=res+1
    print(res)