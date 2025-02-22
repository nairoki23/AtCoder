x=input()
ren=len(x)
for tar in range(ren-1):
    if x[tar]<=x[tar+1]:
        print("No")
        exit()
print("Yes")