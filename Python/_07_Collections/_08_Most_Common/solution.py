from collections import Counter, OrderedDict

S = input()


class OrderedCounter(Counter, OrderedDict):
    pass

c = OrderedCounter(sorted(S))
for k, v in c.most_common(3):
    print(k, v)
