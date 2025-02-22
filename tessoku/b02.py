res=False
raw=input().split()
counter=int(raw[0])
while counter<=int(raw[1]):
    if (100%counter)==0:
        res=True
    counter=counter+1
print({True:"Yes",False:"No"}[res])