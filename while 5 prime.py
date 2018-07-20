n=int(input('number is'))
rt=n**0.5
i = 2
c=0
while i<rt:
    if n%i==0:
        print('not prime')
        c+=1
    i+=1
if c==0:
    print('Prime')
