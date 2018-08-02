#Remove all occurances of an element
l=[15,3,4,5,5,22,33,44,55,15]
r=5
t=15
id=[]
for i ,x in enumerate(l):
    if x==r or x==t:
        id.append(i)
id.reverse()
for i in id:
    l.pop(i)
print(l)