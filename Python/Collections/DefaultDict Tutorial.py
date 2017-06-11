from collections import defaultdict


A, B = map(int, input().split())
d = defaultdict(list)

for index, _ in enumerate(range(A), start=1):
    word = input()
    d[word].append(str(index))

for i in range(B):
    word = input()
    if word in d:
        print(' '.join(d[word]))
    else:
        print('-1')
