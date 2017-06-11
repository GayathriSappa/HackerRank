from collections import Counter


X = int(input())
xs = map(int, input().split())
d = Counter(xs)
N = int(input())
s = 0
for i in range(N):
    k, v = map(int, input().split())
    if d.get(k) and d[k] > 0:
        s += v
        d[k] -= 1

print(s)
