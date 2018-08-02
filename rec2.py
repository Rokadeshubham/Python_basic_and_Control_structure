cache = {2:2, 1:1}
count = 0
def cways(n):
    global count
    count += 1
    if n not in cache:
        cache[n] = cways(n-1) + cways(n-2)
    return cache[n]
print (cways(4), '->', count)