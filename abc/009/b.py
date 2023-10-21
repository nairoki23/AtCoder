a=[]
for fda in range(int(input())):
  a.append(int(input()))
a=sorted(list(set(a)))
print(a[-2])