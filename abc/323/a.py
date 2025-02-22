target=[1,3,5,7,9,11,13,15]
s=input()
for taisyo in target:
    if s[taisyo]=="1":
        print("No")
        exit()
print("Yes")