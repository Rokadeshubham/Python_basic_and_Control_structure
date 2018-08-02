g = 9.8
def fun():
    g = 10
def start():
    print ('Before: ', g)
    fun()
    print ('After: ', g)
start()
