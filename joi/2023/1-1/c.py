n=int(input())
s=input()
t=input()
res=0
for fs in range(n):
    res=res+(s[fs]!=t[fs])
print(res)