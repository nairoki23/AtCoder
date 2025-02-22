num = int(input())
yakusu = {}
for i in range(1,10):
    if num % i == 0:
        yakusu[num/i]=i
for i in range(num+1):
    atai=[]
    for bai in yakusu:
        if (i%bai)==0:
            atai.append(yakusu[bai])
    if len(atai)==0:
        print("-",end="")
        continue
    atai.sort()
    print(atai[0],end="")