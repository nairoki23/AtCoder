import sys
def input():
    return sys.stdin.readline()[:-1]
raw=input().split()
d=int(raw[1])
p=int(raw[2])
max_set=0
while True:
    max_set=max_set+1
    if int(raw[0])<(d*max_set):
        break
days=[]
now=0
for ra in input().split():
    kr=int(ra)
    now=kr+now
    days.append(int(kr))
res=[max_set*p,now]
days.sort()
for bou in range(max_set-1):
    bou=bou+1
    for ata in range(d):
        now=now-days.pop()
    res.append((bou*p)+now)
res.sort()
print(res[0])