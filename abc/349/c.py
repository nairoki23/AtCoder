area=input()
airport=input()
if airport[2]=="X":
    airport=airport[0:2]
renzokusei=0
for asfd in airport.lower():
    b=area.find(asfd)
    if b==-1:
        break
    area=area[b+1:]
else:
    print("Yes")
    exit()
print("No")