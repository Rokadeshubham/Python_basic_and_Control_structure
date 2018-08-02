import copy
def modify(p):
    p[2][1]=99
def main():
    l=[1,2,[5,4,3],8,9]
    dup=copy.deepcopy(l)
    modify(dup)
    print(l)
    print(dup)
main()
