a=int(input())
if(a%4!=0):
    print("365")
else:
    if(a%100==0 and a%400!=0):
        print("365")
    else:
        print("366")