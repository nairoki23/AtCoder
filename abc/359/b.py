count=int(input())*2
tar=input().split()
i=2
res=0
for fd in tar:
    if(i==count):
        break
    res=res+(tar[i]==fd)
    i=i+1
print(res)