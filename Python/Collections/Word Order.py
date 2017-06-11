from collections import OrderedDict, Counter


class OrderedCounter(Counter, OrderedDict):
    pass


c = OrderedCounter()
n = int(input())
for _ in range(n):
    s = input()
    c[s] += 1


print(len(c))
for i in c.values():
    print(i, end=' ')
