#!/bin/python3

import sys


def twoStrings(s1, s2):
    # Complete this function
    substring = set(s1).intersection(set(s2))
    return 'YES' if substring else 'NO'

q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print(result)
