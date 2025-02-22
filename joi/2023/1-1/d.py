input()
nu=[]
for sfd in input().split():
    nu.append(int(sfd))
for res in set(sorted(nu)):
    print(res)