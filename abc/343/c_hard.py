x=0
res=[]
while True:
    b=x*x*x
    if b>=10**18:
        break
    res.append(b)
    x=1+x
print(res)