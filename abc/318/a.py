raw=input().split()
n=int(raw[0])
m=int(raw[1])
p=int(raw[2])
res=0
n=n-m
while True:
    if n<0:
        break
    else:
        res=res+1
    n=n-p
print(res)