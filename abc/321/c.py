hy="0"
def serch(jh,x):
    var=str(int(jh)+x)
    rep=False
    ind=len(str(x))-1
    if int(var[-1-ind])==0:
        pass
    elif int(var[-2-ind])<=int(var[-1-ind]):
        rep=True
    if rep:
        jh=list(jh)
        fds=len(str(x))
        jh[-(fds)]="0"
        return serch("".join(jh),x*10)
    return var
for fdfsfda in range(int(input())):
    hy=serch(hy,1)
print(hy)