s=input()
l=len(s)
res=0
for haba in range(int((l-1)/2)):
    a=0
    while(2+a+haba*2<l):
        res=res+( s[a]=="A" and s[a+haba+1]=="B" and s[a+haba*2+2]=="C" )
        a=a+1
print(res)