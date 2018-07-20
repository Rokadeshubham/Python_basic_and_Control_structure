#Print count of the digits in the given number
n = int(input("Enter x:"))
c = 0
b = n
while n > 0:
    n //= 10
    c += 1
print ('Number of digits in {} is {}'.format(b, c))

