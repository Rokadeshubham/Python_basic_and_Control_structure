import copy
def modify(p):
    p[2][1] = 999
def main():
    l = [7, 8, [4, 3, 5], 9]
    dup = copy.copy(l)
    modify(dup)
    print(l)
if __name__ == '__main__':
    main()