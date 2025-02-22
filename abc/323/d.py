s={}
kazunau=[]
for fdsa in range(int(input())):
    raw_in=input().split()
    size=int(raw_in[0])
    kazu=int(raw_in[1])
    kazunau.append(size)
    s[size]=kazu
res=0
while True:
    if len(kazunau)==0:
        break
    tar=kazunau[0]
    goseid=s[tar]//2
    if goseid>0:
        dai=tar*2
        if dai in s:
            s[dai]=s[dai]+goseid
        else:
            s[dai]=goseid
            kt=0
            for dab in kazunau:
                if dab>dai:
                    kazunau.splice(kt,0,dai)
                    break
                kt=kt+1
        res=goseid%2+res
    else:
        res=s[tar]%2+res
    del s[tar]
    del kazunau[0]
print(res)