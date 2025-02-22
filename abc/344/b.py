res=[]
while True:
    wa=input()
    res.append(wa)
    if (wa=="0"):
        break
res.reverse()
for b in res:
    print(b)