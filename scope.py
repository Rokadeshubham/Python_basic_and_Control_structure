g = 9.8
def fun(n):
    x = 50
    y = 90
    n = n*10
    print ('---- in side fun()-------')
    print ('----- locals() ----------')
    print (locals())
    print ('----- globals() ----------')
    print (globals())
def start():
    x = 20
    n = 30
    fun(n)
    print ('---- in side fun()-------')
    print ('----- locals() ----------')
    print (locals())
    print ('----- globals() ----------')
    print (globals())
start()
