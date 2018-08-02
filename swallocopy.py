import copy
def modify(p):
    p[2]=99
def start():
    l=[22,33,44,55,66]
    dup=copy.copy(l)
    modify(dup)
    print(l,dup)
start()