n = int(input('Enter no'))
i = 2
c =0
sqrt= n**0.5
while i<= sqrt:
    if n% i == 0:
        c +=1
    i += 1
if c==0:
    print('prime')
else:
    print('not prime')