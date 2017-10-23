#!/bin/python3

import sys


def sockMerchant(n, ar):
    # Complete this function
    cache = {}
    c = 0
    for i in ar:
        cache[i] = cache.get(i, 0)
        cache[i] += 1
        if cache.get(i) == 2:
            cache[i] = 0
            c += 1
    return c

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
