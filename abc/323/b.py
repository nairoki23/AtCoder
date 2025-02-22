result={}
for fasdf in range(int(input())):
    counter=0
    for zya in input():
        if zya=="o":
            counter=counter+1
    result[fasdf]=counter
for asf in sorted(result.items(), key=lambda x:x[1], reverse=True):
    print(asf[0]+1,end=" ")