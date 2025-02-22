a={}
for tar in input():
    if tar in a:
        a[tar]=a[tar]+1
    else:
        a[tar]=1
naka=sorted(a.items(), key=lambda x:x[1])
res={}
for ky in naka:
    js=ky[1]
    if js in res:
        res[js]=res[js]+1
    else:
        res[js]=1
for mawa in res:
    if res[mawa]!=2:
        break
else:
    print("Yes")
    exit()
print("No")