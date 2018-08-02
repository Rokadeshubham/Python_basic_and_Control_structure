trans = [(1237, 87522),
         (1234, 1000),
         (1236, 6754),
         (1234, 200),
         (1236, 1700),
         (1234, 400),
         (1234, 600),
         (1236, 788),
         (1234, 500),
         (1237, 126653),
         (1999, 1000)]
deposite={}
for _id, cash in trans:
    if _id not in deposite:
        deposite[_id] = [cash]
    else:
        deposite[_id].append(cash)
print(deposite)

print('Maximum deposite',max(deposite.items(),key=lambda x:x[1]))
print('Minimum deposite',min(deposite.items(),key=lambda x:x[1]))
print('Sum of deposite',max(deposite.items(),key=lambda x:sum(x[1])))



