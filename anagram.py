from collections import defaultdict
words = ['hell', 'cat', 'bell',
         'tab','tac', 'apt', 'dell',
         'act', 'tap', 'bat']
d = defaultdict(list)
for word in words:
    ana=''.join(sorted(word))
    d[ana].append(word)
for ana,anagram in d.items():
    if len(anagram)>1:
        print(anagram)