res=False
sence=[]

def check(sen):
    m=len(sen)
    con=0
    while con<(m/2):
        if sen[con]!=sen[m-1-con]:
            return False
        con=con+1
    print("Yes")
    exit()
#Let's ドチャシコサラマンダー
for sdsaf in range(int(input())):
    sence.append(input())
for sfda in sence:
    for koyu in sence:
        if koyu==sfda:
            continue
        check(koyu+sfda)
print("No")