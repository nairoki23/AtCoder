a=[]
input()
for s in input().split():
    a.append(int(s))
#a.sort()
a=set(a)
b=[]
input()
for s in input().split():
    b.append(int(s))
#b.sort()
b=set(b)
c=[]
input()
for s in input().split():
    c.append(int(s))
c=set(c)
#c.sort()
q={}
input()
k=0
res=[]
for s in input().split():
    if  int(s) in q:
        q[int(s)].append(k)
    else:
        q[int(s)]=[k]
    res.append("No")
    k=k+1
    """
mani=[]
dash=[]

for zen in a:
    for tan in b:
        dash.append(zen+tan)
dash=set(dash)
for saf in dash:
    for saku in c:
        tar=saf+saku
        if(tar in q):
            res[q[tar]]="Yes"
"""
for zen in a:
    for tan in b:
        for te in c: 
            bar=zen+tan+te
            if(bar in q):
                for  just in q[bar]:
                    res[just]="Yes"
for pr in res:
    print(pr,end="\n")