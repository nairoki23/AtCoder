input()
a=[]
for fd in input().split():
    a.append(int(fd))
a.sort()
st=a[0]
for tr in a:
    if st!=tr:
        print(st,end=" ")
        break
    st=st+1