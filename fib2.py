cache = {}
def fibo(n):
    if n in cache:
        return cache[n]
    else:
        if n==0 or n==1:
            value =1
            return value
        else:
            value = fibo(n-1)+fibo(n-2)
            cache[n] = value
            return value

for n in range(0,100):
    print(n,fibo(n))