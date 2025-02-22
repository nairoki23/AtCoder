import math
tas=[int(input())]

memo={2:2,3:5,4:8,5:12,6:16,7:20,8:24,9:29,100000000000000000:5655884811924144128}
memo={}
yen=0
while True :
    tas.sort()
    if tas[-1]<2:
        break
    tar=tas.pop()
    if tar in memo:
        yen=memo[tar]+yen
        tas.append(1)
    else:
        yen=yen+tar
        a=tar/2
        tas.append(math.floor(a))
        tas.append(math.ceil(a))

print(yen)
# 2,3,4, 5, 6, 7, 8,9,10,11,12,13,14,15,16
# 2,5,8,12,16,20,24,29,

