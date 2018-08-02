#printing no digits in a reverse direction
n=int(input('enter no'))
while n > 0:
    r = n%10
    print (r, end='')
    n //= 10