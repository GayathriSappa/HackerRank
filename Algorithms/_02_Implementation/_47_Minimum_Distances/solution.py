#!/bin/python3

import sys


n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]

cache = {}
for i in range(len(A)):
    v = cache.get(A[i])
    if v:
        cache[A[i]][0] += 1
        cache[A[i]][1] = i - v[1]
    else:
        cache[A[i]] = [1, i]


d = [i for i in cache.values() if i[0] > 1]
d.sort(key=lambda x: x[1])
print(d[0][1] if d else -1)
