cache ={1:1,2:2}
cnt=0
def fib(n):
    global cnt
    cnt +=1
    if n not in cache:
        cache[n]=fib(n-1)+fib(n-2)
    return cache[n]
print(fib(55),'--->',cnt)