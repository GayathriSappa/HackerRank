from collections import OrderedDict


N = int(input())
d = OrderedDict()
for i in range(N):
    temp = input().split()
    net_price = int(temp.pop())
    item_name = ' '.join(temp)
    if d.get(item_name):
        d[item_name] += net_price
    else:
        d[item_name] = net_price

for k, v in d.items():
    print(k, v)
