from collections import Counter


n = int(input())
a = [int(i) for i in input().split()]

c = Counter(a)
print(n - c.most_common(1)[0][1])
