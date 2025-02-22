kakaru=int(input().split()[1])
next=0
for fd in input().split():
    mu=0
    f=int(fd)
    if next<f:
        mu=f-next
    next=kakaru+next+mu
    print(next)