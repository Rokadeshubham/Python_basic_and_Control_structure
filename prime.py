n=int(input('enter no'))
rt=int(n**0.5)
i=2
for i in range(2,rt+1):
    if n%i==0:
        print('prime')
        break
    
else:
    print('not prime')

