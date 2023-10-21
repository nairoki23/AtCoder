n=int(input())
ku=0
win=0
tab={}
for fdsaf in range(n):
    raw_in=input().split()
    rawt=int(raw_in[2])
    ku=rawt+ku
    if int(raw_in[0])>int(raw_in[1]):
        win=win+rawt
        continue
    if rawt not in tab:
        tab[int(raw_in[2])]=[int((int(raw_in[1])+int(raw_in[0]))/2)+1-int(raw_in[0])]
    else:
        tab[int(raw_in[2])].append(int((int(raw_in[1])+int(raw_in[0]))/2)+1-int(raw_in[0]))
nokori=(int(ku/2)+1)-win
if nokori<=0:
    print(0)
    exit()
hyosu=[]
trn={}
#print(sorted(tab.items()))
for tros in sorted(tab.items()):
    kuk=tros[0]
    for tro in tros[1]:
        if nokori>kuk:
            trn[tro]=kuk
        else:
            hyosu.append(tro)

zibu=0
sukun=sorted(trn.items())
#print(win)
#print(suku)

def sfda(suku):
    global hyosu
    zibu=0
    for chn in suku:
        st=chn[1]
        lo=chn[0]
        hiki=suku.copy()
        del hiki[zibu]
        if st>=win:
            hyosu.append(lo)
            return
        sfda(hiki)
        zibu=zibu+1
    
sfda(sukun)
    
print(sorted(hyosu)[0])