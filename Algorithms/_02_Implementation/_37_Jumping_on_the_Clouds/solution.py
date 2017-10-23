#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

k = 0
i = 0
while i <= n - 3:
    if c[i+2] != 1:
        i += 2
        k += 1
    else:
        i += 1
        k += 1
if i != n:
    k += n - 1 - i
print(k)
