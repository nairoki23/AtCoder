s=[]
for i in input().split():
    s.append(i=="sick")
if(s[0] and s[1]):
    print(1)
elif(s[0]):
    print(2)
elif(s[1]):
    print(3)
else:
    print(4)