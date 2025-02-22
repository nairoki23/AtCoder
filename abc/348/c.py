sdfa={}
for  fdsa in range(int(input())):
    ris=[]
    for dsf in input().split():
        ris.append(int(dsf))
    if ris[1] in sdfa:
        if sdfa[ris[1]] > ris[0]:
            sdfa[ris[1]]=ris[0]
    else:
        sdfa[ris[1]]=ris[0]
print(sorted(sdfa.items(), key=lambda x:x[1], reverse=True)[0][1])