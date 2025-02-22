info=input().split()
a=[]
for an in input().split():
    a.append(int(an))
print(int(info[0])-len(a))
for i in range(int(info[0])):
    i=i+1
    if(i in a):
        continue
    print(i,end=" ")