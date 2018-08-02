g= 10
def fun():
    global g
    g = 9
def main():
    print(g)
    fun()
    print(g)
main()