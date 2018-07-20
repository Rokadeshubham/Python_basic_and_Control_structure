n = int(input('Enter no'))
i = 2

sqrt= n**0.5
while i<= sqrt:
    if n% i == 0:
        print('not prime')
        break
    i += 1
else:
    print('prime')