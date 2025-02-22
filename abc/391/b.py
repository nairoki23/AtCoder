s=[]
t=[]
n,m=input().split()
n=int(n)
m=int(m)
p=[]
for i in range(n):
    s.append([])
    for a in input():
        s[i].append(a=="#")

for i in range(m):
    t.append([])
    for a in input():
        t[i].append(a=="#")

for i in range(n):
    for j in range(n):
        count=0
        for k in range(m):
            if (k+i>=n):
                break
            for l in range(m):
                if(l+j>=n):
                    break
                count=count+int(s[i+k][j+l]==t[k][l])
        if(count==m*m):
            print(str(1+i)+" "+str(1+j))
            exit()