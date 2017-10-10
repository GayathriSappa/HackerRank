#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    num = str(n)
    print(len([i for i in num if int(i) != 0 and n % int(i) == 0]))


