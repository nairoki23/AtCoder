import math
x=int(input())
while True:
    xp=str(x)
    Bad=False
    for sad in range(int(len(xp)/2)):
        Bad=Bad+(xp[sad]!=xp[-(sad+1)])
    if Bad:
        x=x-1
        continue
    if not math.cbrt(x).is_integer():
        x=x-1
        continue
   
    break
print(x)