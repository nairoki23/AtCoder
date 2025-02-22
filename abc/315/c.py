zisyo={}
for ahfgui in range(int(input())):
    ra=input().split()
    if ra[0] not in zisyo:
        zisyo[ra[0]]=[int(ra[1])]
    else:
        zisyo[ra[0]].append(int(ra[1]))
res=0
ket=[]
for ky in zisyo:
    zisyo[ky].sort(reverse=True)
    if len(zisyo[ky])==1:
        ket.append(zisyo[ky][0])
        continue
    kouho=(zisyo[ky][0]+int(zisyo[ky][1]/2))
    if kouho >res:
        res=kouho
    ket.append(zisyo[ky][0])
if len(ket)>1:
    ket.sort(reverse=True)
    kouho=ket[0]+ket[1]
    if kouho >res:
        res=kouho

print(res)