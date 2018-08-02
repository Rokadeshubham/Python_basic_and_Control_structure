def add(x,y):
    z=x+y
    return z
print(add(5,4))

def square(x):

    s=x*x
    return s
print(square(x=int(input('enter no:'))))

def fact(a):
    f=1
    for i in range(1,a+1):
        f=f*i
        return f
n=5
r=3
res=fact(n)/(fact(n-r)*fact(r))
print('ncr=',res)
