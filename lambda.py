l=[1,9,3,7,5,5,5,2,8]
d={}
n=10
for x in l:
    if x not in d:
        d[x]=1
    else:
        d[x]+=1
print(d)
for x in d.keys():
    if x == n//2:
        c=d[x]//2
        d[x]-=2*c
    elif n-x in d:
        c=min(d[x],d[n-x])
        d[x]-=c
        d[n-x]-=c
    for i in range(c):
        print(x,n-x)
print(d)


