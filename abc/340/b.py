the=[]
for _ in range(int(input())):
    raw=input().split()
    if raw[0]=="1":
        the.append(raw[1])
    else:
        print(the[-int(raw[1])])