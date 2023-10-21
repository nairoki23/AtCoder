tar=int(input().split()[1])
now=[]
goke=0
for core in input().split():
    goke=int(core)+goke
    now.append(int(core))
now.sort()
ares=tar-(goke-now[0]-now[-1])
if ares>100:
    print(-1)
elif ares<=now[0]:
    print(0)
elif ares<=now[-1]:
    print(ares)
else:
    print(-1)