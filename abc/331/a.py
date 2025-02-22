raw=input().split()
dm=int(raw[1])
mm=int(raw[0])
now=input().split()
res_y=int(now[0])
theday=int(now[1])*dm+int(now[2])+1
res_m=int(theday/dm)
res_d=((theday)%dm)
if res_d==0:
    res_d=1
if (res_m>mm):
    res_y=res_y+1
    res_m=1
print(str(res_y)+" "+str(res_m)+" "+str(res_d))