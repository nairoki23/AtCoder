raw=input().split()
j=int(raw[1])
res=0
ne=[]
for fd in input().split():  
    ne.append(int(fd))
m=[]

for fd in input().split():  
    m.append(int(fd))

ne.sort()
m.sort()

by=0

for d in ne:
    if j==0:
        break
    if d>=m[by]:
        res=d+res
        j=j-1
        by=by+1
             
if j!=0:
        print(-1)
else:
    print(res)