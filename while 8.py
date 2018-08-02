#magic number
n = int(input("Enter x:"))
b = n
s = n
while s > 9:
    n = s
    s = 0
    while n > 0:
        r = n%10
        s += r
        n //= 10
print ('Magic number of {} is {}'.format(b, s))