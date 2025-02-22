input()
days=[]
day_all=1
for day_num in input().split():
    day_num=int(day_num)
    days.append(day_num)
    day_all=day_all+day_num
tar_day=day_all/2
res_m=0
for date in days:
    res_m=res_m+1
    if tar_day>date:#この付きじゃねえ
        tar_day=tar_day-date
    else:
        print(str(res_m)+" "+str(int(tar_day)))
        break