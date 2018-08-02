from functools import lru_cache

@lru_cache(maxsize=2000)
def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
for n in range(0,1700):
    print(n,'-->',fib(n))