x=int(input().split()[1])
counter=1
table={}
for fd in input().split():
    table[int(fd)]=counter
    counter=counter+1
print(table[x])