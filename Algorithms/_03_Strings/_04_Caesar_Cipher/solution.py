#!/bin/python3

import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+k) % 26 + c)
print(''.join([d.get(c, c) for c in s]))
