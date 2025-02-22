import sys
sys.setrecursionlimit(200000)
bord=[]
outed=[]
for fasd in range(int(input())):
    bord.append([])
    raw=input().split()
    del raw[0]
    for ji in raw:
        bord[-1].append(int(ji))

def check (satsu):
    satsuc=satsu-1
    if len(bord [satsuc])!=0:
        for gf in bord[satsuc]:
            check(gf)
    if satsu in outed:
        return
    print(satsu,end = " ")
    outed.append(satsu)
    

for rs in bord[0]:
    check(rs)