#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    h = 1
    if n:
        for i in range(1, n+1):
            if i % 2 == 1:
                h *= 2
            else:
                h += 1
        print(h)
    else:
        print(h)
