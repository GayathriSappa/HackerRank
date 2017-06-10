from itertools import product

A = map(int, input().split())
B = map(int, input().split())

[print(i, end=' ') for i in product(A, B)]
