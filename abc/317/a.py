raw_in=input().split()
moku=int(raw_in[2])-int(raw_in[1])
res=1
for p in input().split():
    if moku<=int(p):
        print(res)
        break
    res=res+1