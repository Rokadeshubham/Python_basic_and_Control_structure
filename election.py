from collections import Counter, defaultdict

votes = ['Kenny', 'Amanda', 'John', 'Vicky', 'Alex', 'Amanda',
         'John', 'Alex', 'Kenny', 'Vicky', 'Charles', 'Alex',
         'Kenny', 'Eric', 'Charles', 'Eric', 'Laura', 'Michelle',
         'Eric', 'Vicky']
age = {'Kenny': 61, 'Amanda': 54, 'Alex': 79,
       'John': 80, 'Vicky': 34, 'Eric': 50,
       'Laura': 55, 'Michelle': 42, 'Charles': 70}

# Finding vote count for each contestant
namecnt = Counter(votes)
names = defaultdict(list)
# Grouping constestants with same count
for n, count in namecnt.items():
    names[count].append(n)
# finding winner
count, candidate = max(names.items())
# Finding max by their age
winner = max(candidate, key=lambda x: age[x])
print('Winner is:', winner, ' With Count:', count)

