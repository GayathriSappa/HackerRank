from itertools import product


k, m = map(int, input().split())

it = [map(lambda x: pow(int(x), 2), input().split()[1:]) for _ in range(k)]
s = map(lambda x: sum(x) % m, product(*it))
print(max(s))
