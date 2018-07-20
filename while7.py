#sum of digits in a number
n=int(input('No iS:'))
sum=0
while 0<n:
    r=n%10
    n//=10
    sum+=r
print('sum is',sum)
