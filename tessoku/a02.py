res=False
s=int(input().split()[1])
for sfd in input().split():
    if int(sfd)==s:
        break
else:
    print("No")
    exit()
print("Yes")